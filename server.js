// Minimal, dependency-free static server for the MonstarX Indonesia MCP playground.
// Serves ./public, respects Railway's $PORT, exposes /health, and proxies POST /mcp
// to local ID-MCP (or MCP_URL) with a staging fallback so live Run is same-origin.
const http = require("http");
const fs = require("fs");
const path = require("path");

const PORT = process.env.PORT || 8080;
const ROOT = path.join(__dirname, "public");
const MCP_PRIMARY = (process.env.MCP_URL || "http://127.0.0.1:8787").replace(/\/$/, "");
const MCP_FALLBACK = (process.env.MCP_FALLBACK || "https://id-mcp-staging.monstarxapp.com").replace(/\/$/, "");

const TYPES = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "application/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".svg": "image/svg+xml",
  ".png": "image/png",
  ".ico": "image/x-icon",
  ".txt": "text/plain; charset=utf-8",
};

function collectBody(req) {
  return new Promise((resolve, reject) => {
    const chunks = [];
    req.on("data", (c) => chunks.push(c));
    req.on("end", () => resolve(Buffer.concat(chunks)));
    req.on("error", reject);
  });
}

async function proxyMcp(req, res) {
  if (req.method === "OPTIONS") {
    res.writeHead(204, {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET,POST,DELETE,OPTIONS",
      "Access-Control-Allow-Headers":
        "Content-Type,mcp-session-id,Last-Event-ID,mcp-protocol-version,Authorization",
    });
    return res.end();
  }

  const body = req.method === "GET" || req.method === "HEAD" ? undefined : await collectBody(req);
  const origins = [...new Set([MCP_PRIMARY, MCP_FALLBACK])];
  const errors = [];

  for (const origin of origins) {
    const local = /localhost|127\.0\.0\.1/i.test(origin);
    const timeoutMs = local ? 8000 : 20000;
    try {
      const headers = {
        "Content-Type": req.headers["content-type"] || "application/json",
        Accept: req.headers.accept || "application/json, text/event-stream",
        "mcp-protocol-version": req.headers["mcp-protocol-version"] || "2025-06-18",
      };
      const upstream = await fetch(origin + "/mcp", {
        method: req.method,
        headers,
        body: body && body.length ? body : undefined,
        signal: AbortSignal.timeout(timeoutMs),
      });
      const buf = Buffer.from(await upstream.arrayBuffer());
      const out = {
        "Content-Type": upstream.headers.get("content-type") || "application/json",
      };
      const session = upstream.headers.get("mcp-session-id");
      if (session) out["mcp-session-id"] = session;
      res.writeHead(upstream.status, out);
      return res.end(buf);
    } catch (err) {
      errors.push({
        origin,
        error: err.cause?.code || err.code || err.name,
        message: err.message,
      });
    }
  }

  res.writeHead(502, { "Content-Type": "application/json" });
  res.end(
    JSON.stringify({
      error: "MCP upstream unreachable",
      tried: errors,
      hint: "Staging MCP timed out. Start local ID-MCP (`npm run dev` in ../ID-MCP) so this playground can proxy to http://127.0.0.1:8787/mcp.",
    }),
  );
}

const server = http.createServer((req, res) => {
  const url = decodeURIComponent((req.url || "/").split("?")[0]);

  if (url === "/mcp") {
    return proxyMcp(req, res).catch((err) => {
      if (!res.headersSent) {
        res.writeHead(500, { "Content-Type": "application/json" });
        res.end(JSON.stringify({ error: String(err) }));
      }
    });
  }

  if (url === "/health") {
    res.writeHead(200, { "Content-Type": "application/json" });
    return res.end(JSON.stringify({ status: "ok", service: "id-mcp-playground" }));
  }

  let rel = url === "/" ? "/index.html" : url === "/favicon.ico" ? "/favicon.svg" : url;
  let filePath = path.normalize(path.join(ROOT, rel));
  if (!filePath.startsWith(ROOT)) {
    res.writeHead(403);
    return res.end("Forbidden");
  }

  fs.readFile(filePath, (err, data) => {
    if (err) {
      return fs.readFile(path.join(ROOT, "index.html"), (e2, home) => {
        if (e2) {
          res.writeHead(404);
          return res.end("Not found");
        }
        res.writeHead(200, { "Content-Type": TYPES[".html"] });
        res.end(home);
      });
    }
    const ext = path.extname(filePath).toLowerCase();
    res.writeHead(200, {
      "Content-Type": TYPES[ext] || "application/octet-stream",
      "Cache-Control": ext === ".html" ? "no-cache" : "public, max-age=3600",
    });
    res.end(data);
  });
});

server.listen(PORT, () => {
  console.log(`id-mcp-playground listening on ${PORT} (MCP proxy → ${MCP_PRIMARY})`);
});
