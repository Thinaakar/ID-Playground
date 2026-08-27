# MonstarX Indonesia MCP — Playground

A self-contained **live playground and docs site** for the [MonstarX Indonesia MCP](../../Backend/ID_mcp) server: **55 free `id_*` tools** (weather, earthquakes, geocoding, wilayah, holidays, KRL, news, prayer times, gold, open data).

Same design system as the Japan MCP playground — Indonesia tools and data only. Backend: `ID_mcp` (`@monstarx/monstarx-mcp-id`).

> 🔌 **MCP endpoint (staging):** `https://id-mcp-staging.monstarxapp.com/mcp`  
> Local: `http://localhost:8787/mcp` (from `Backend/ID_mcp` + `npm run dev`)

---

## Run locally & deploy

```bash
npm start           # serves public/ on http://localhost:8080  (respects $PORT)
```

Live **Run** on Cloudflare Pages calls staging MCP directly (`EP`, CORS open on the Worker). Locally (`npm start` on localhost), it posts to same-origin `/mcp`, which `server.js` proxies to local ID MCP (`http://127.0.0.1:8787`, override with `MCP_URL`) and falls back to staging. Start the Worker with `npm run dev` in `Backend/ID_mcp`.

**Deploy to Cloudflare Pages** (same pattern as UAE / MY / JP):

```bash
npm run build
$env:CLOUDFLARE_ACCOUNT_ID="bf6b2bcb226d2847802880925b23f57e"
npx wrangler pages deploy public --project-name id-mcp-playground --branch main --commit-dirty=true
```

Optional Railway: `railway up --ci` (uses `server.js` + `/mcp` proxy).

**Regenerate the page** after editing tool metadata or `build/build.py`:

```bash
python build/gen_data.py  # optional: rewrite build/data.min.json from the generator
python build/build.py     # rewrites public/index.html + indonesia-mcp-playground.html
```

To point live **Run** at a different MCP, set `MCP_URL` for the proxy, or open the playground with `?mcp=http://localhost:8787`.

---

## Repository layout

```
├── public/index.html                  # playground (served)
├── indonesia-mcp-playground.html      # standalone copy
├── server.js                          # static server + /health
├── package.json
├── railway.json
├── build/
│   ├── build.py                       # HTML generator
│   ├── data.min.json                  # 55 id_* tools + example payloads
│   ├── gen_data.py                    # regenerates data.min.json
│   └── assemble_id.py                 # optional assembler for build.py
├── examples/                          # curl / Python / TS clients
└── README.md
```

---

## Quick start (MCP)

```bash
# List tools
curl -X POST https://id-mcp-staging.monstarxapp.com/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "mcp-protocol-version: 2025-06-18" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'

# Jakarta 24h weather (Kemayoran, Jakarta Pusat)
curl -X POST https://id-mcp-staging.monstarxapp.com/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "mcp-protocol-version: 2025-06-18" \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"id_weather_24h","arguments":{"area_code":"31.71.03.1001"}}}'
```

---

## Connect from MCP clients

### Claude Code

```bash
claude mcp add --transport http id-mcp https://id-mcp-staging.monstarxapp.com/mcp
```

### Cursor / native HTTP

```jsonc
{
  "mcpServers": {
    "indonesia": {
      "type": "http",
      "url": "https://id-mcp-staging.monstarxapp.com/mcp"
    }
  }
}
```

### Claude Desktop (`mcp-remote`)

```jsonc
{
  "mcpServers": {
    "indonesia": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://id-mcp-staging.monstarxapp.com/mcp"]
    }
  }
}
```

---

## Tools (55)

| Category | Tools |
|---|---|
| Weather & environment | `id_weather_areas`, `id_weather_overview`, `id_weather_week_overview`, `id_weather_warnings`, `id_weather_24h`, `id_weather_4day`, `id_uv_index`, `id_rainfall`, `id_air_temperature`, `id_relative_humidity`, `id_air_quality` |
| Hazards & disasters | `id_earthquake_list`, `id_tsunami_list`, `id_flood_reports`, `id_volcanoes` |
| Geocoding & wilayah | `id_address_search`, `id_geocode`, `id_reverse_geocode`, `id_postal_code`, `id_elevation`, `id_provinces`, `id_regencies`, `id_districts`, `id_villages` |
| Civic & safety | `id_public_holidays`, `id_cuti_bersama`, `id_evacuation_shelters`, `id_disease_reports`, `id_parse_nik`, `id_kpu_election_2024`, `id_heroes` |
| Tourism | `id_tourism_spots` |
| Commuter (KRL) | `id_krl_stations`, `id_krl_schedule` |
| News | `id_news`, `id_news_category`, `id_news_search` |
| Health | `id_faskes` |
| Finance | `id_bi_finance`, `id_gold_price`, `id_banks`, `id_ojk_invest`, `id_indodax_ticker` |
| Language & faith | `id_kbbi`, `id_prayer_cities`, `id_prayer_schedule`, `id_quran_list`, `id_quran_surah`, `id_hadith`, `id_doa`, `id_asmaul_husna` |
| Open data catalog | `id_datasets_search`, `id_dataset_show`, `id_dataset_metadata`, `id_dataset_query` |

Full parameter docs and example responses are in the playground (**Tools** section) and in `build/data.min.json`.

---

## Data sources

| Source | Used by |
|---|---|
| [BMKG](https://data.bmkg.go.id/) | Areas, overview, warnings, earthquake, tsunami |
| [Open-Meteo](https://open-meteo.com/) | 24h/4day, rain, temp, humidity, UV, air quality, elevation |
| [Nominatim](https://nominatim.openstreetmap.org/) | Address search, geocode, reverse geocode |
| [CariKodePos](https://carikodepos.id/) | Postal code |
| [Nager.Date](https://date.nager.at/) | Public holidays |
| [Frankfurter BI](https://frankfurter.dev/providers/bi/) | Bank Indonesia FX |
| [HDX CKAN](https://data.humdata.org/) | Dataset catalog |
| [OpenStreetMap Overpass](https://overpass-api.de/) | Tourism, shelters, nearby hospitals |
| [API Wilayah Indonesia](https://emsifa.github.io/api-wilayah-indonesia/) | Provinces, kabupaten, kecamatan, desa |
| [Comuline](https://api.comuline.com/) | KRL stations and schedules |
| [Berita Indo API](https://berita-indo-api.vercel.app/) | News headlines |

No API keys required for these free sources. MonstarX is an independent wrapper and is not endorsed by any government agency.

---

## Response format

Successful tool calls return:

- `content[0].text` — JSON string  
- `structuredContent` — same payload as object (prefer this)

Envelope fields typically include `source`, `agency`, `api`, `retrieved_at`, and often `license` / `auth`.

---

*Server: MonstarX Indonesia MCP v0.1.0 · Protocol `2025-06-18`*
