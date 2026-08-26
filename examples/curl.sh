#!/usr/bin/env bash
# Minimal curl examples against MonstarX Indonesia MCP
set -euo pipefail

BASE="${ID_MCP_URL:-https://id-mcp-staging.monstarxapp.com/mcp}"

hdr() {
  echo "--- $1 ---"
}

hdr "tools/list"
curl -sS -X POST "$BASE" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "mcp-protocol-version: 2025-06-18" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}' | head -c 500
echo

hdr "id_weather_24h (Jakarta Pusat Kemayoran 31.71.03.1001)"
curl -sS -X POST "$BASE" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "mcp-protocol-version: 2025-06-18" \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"id_weather_24h","arguments":{"area_code":"31.71.03.1001"}}}' | head -c 800
echo

hdr "id_geocode (Monas Jakarta)"
curl -sS -X POST "$BASE" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "mcp-protocol-version: 2025-06-18" \
  -d '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"id_geocode","arguments":{"query":"Monas Jakarta","limit":2}}}' | head -c 800
echo
