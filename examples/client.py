"""Minimal Python client for MonstarX Indonesia MCP (stdlib only)."""
from __future__ import annotations

import json
import os
import urllib.request

BASE = os.environ.get("ID_MCP_URL", "https://id-mcp-staging.monstarxapp.com/mcp")


def call_tool(name: str, arguments: dict | None = None):
    body = json.dumps(
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/call",
            "params": {"name": name, "arguments": arguments or {}},
        }
    ).encode()
    req = urllib.request.Request(
        BASE,
        data=body,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
            "mcp-protocol-version": "2025-06-18",
        },
    )
    with urllib.request.urlopen(req) as r:
        result = json.load(r)["result"]
    if result.get("isError"):
        raise RuntimeError(result["content"][0]["text"])
    return result.get("structuredContent") or json.loads(result["content"][0]["text"])


if __name__ == "__main__":
    wx = call_tool("id_weather_24h", {"area_code": "31.71.03.1001"})
    print("Jakarta 24h hours:", len((wx.get("data") or {}).get("hourly", {}).get("time") or []))

    geo = call_tool("id_geocode", {"query": "Monas Jakarta", "limit": 2})
    print("Geocode results:", geo.get("shown"), geo.get("results"))

    quakes = call_tool("id_earthquake_list", {"limit": 3})
    print("Recent quakes shown:", quakes.get("shown"))
