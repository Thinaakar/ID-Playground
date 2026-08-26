#!/usr/bin/env python3
"""Adapt the copied Japan playground build.py into the Indonesia playground."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
src = (ROOT / "build.py").read_text(encoding="utf-8")

src = src.replace("MonstarX Japan MCP playground", "MonstarX Indonesia MCP playground")
src = src.replace("japan-mcp-playground.html", "indonesia-mcp-playground.html")
src = src.replace(
    "--dot-catalog:#64748b;--dot-weather:#16a34a;--dot-hazards:#dc2626;--dot-geo:#0891b2;"
    "--dot-civic:#7c3aed;--dot-places:#db2777;--dot-finance:#ea580c;",
    "--dot-catalog:#64748b;--dot-weather:#16a34a;--dot-hazards:#dc2626;--dot-geo:#0891b2;"
    "--dot-civic:#7c3aed;--dot-places:#db2777;--dot-finance:#ea580c;"
    "--dot-transport:#2563eb;--dot-news:#0ea5e9;--dot-health:#059669;--dot-culture:#d97706;",
)

src = src.replace("Japan&nbsp;MCP", "Indonesia&nbsp;MCP")
src = src.replace("jp-mcp-staging.monstarxapp.com/mcp", "id-mcp-staging.monstarxapp.com/mcp")
src = src.replace('placeholder="Filter 27 tools…"', 'placeholder="Filter 55 tools…"')
src = src.replace("MonstarX · Japan MCP", "MonstarX · Indonesia MCP")
src = src.replace(
    """Japan's public data, <span class="hl">ready for your AI</span>.""",
    """Indonesia's public data, <span class="hl">ready for your AI</span>.""",
)
src = src.replace(
    "Weather, earthquakes, geocoding, postal codes, holidays, evacuation shelters, tourism spots, Bank of Japan series, open datasets — Japan's free public APIs live across many agencies, each with its own formats and quirks. <b>MonstarX unifies them into 27 tools any AI agent can call</b>, through one endpoint, with no API keys. Stop writing integration glue. Start shipping Japan-smart products.",
    "Weather, earthquakes, geocoding, wilayah codes, holidays, KRL, news, prayer times, gold prices, open datasets — Indonesia's free public APIs live across many agencies, each with its own formats and quirks. <b>MonstarX unifies them into 55 tools any AI agent can call</b>, through one endpoint, with no API keys. Stop writing integration glue. Start shipping Indonesia-smart products.",
)
src = src.replace('<div class="n">27</div>', '<div class="n">55</div>')
src = src.replace('<div class="n">9</div>', '<div class="n">25</div>')
src = src.replace("streams back real Japan data", "streams back real Indonesia data")

chips = """          <button class="chip-ex" data-ex="wx24" data-i18n-chip="chipWx"><span class="e">⛅</span> Jakarta weather 24h</button>
          <button class="chip-ex" data-ex="quake" data-i18n-chip="chipQuake"><span class="e">🌋</span> Recent quakes</button>
          <button class="chip-ex" data-ex="geo" data-i18n-chip="chipGeo"><span class="e">📍</span> Geocode Monas</button>
          <button class="chip-ex" data-ex="postal" data-i18n-chip="chipPostal"><span class="e">✉️</span> Postal 10110</button>
          <button class="chip-ex" data-ex="holiday" data-i18n-chip="chipHoliday"><span class="e">🇮🇩</span> Holidays 2026</button>
          <button class="chip-ex" data-ex="krl" data-i18n-chip="chipKrl"><span class="e">🚆</span> KRL Manggarai</button>
          <button class="chip-ex" data-ex="tourism" data-i18n-chip="chipTourism"><span class="e">🕌</span> Tourism near Monas</button>
          <button class="chip-ex" data-ex="datasets" data-i18n-chip="chipDatasets"><span class="e">📚</span> Search earthquake datasets</button>"""
old_chips_start = src.index('          <button class="chip-ex" data-ex="wx24"')
old_chips_end = src.index("        </div>\n        <div class=\"pg-body\">", old_chips_start)
src = src[:old_chips_start] + chips + "\n" + src[old_chips_end:]

src = src.replace(
    """        <div class="use"><div class="ico">⛅</div><h4 data-i18n="useWxT">Weather-aware apps</h4><p data-i18n="useWxP">Area codes, daily/weekly JMA text, 24h/4-day forecasts, UV, rain, and air quality for Tokyo or any prefecture office.</p><div class="tools"><code>jp_weather_24h</code><code>jp_weather_warnings</code><code>jp_uv_index</code></div></div>
        <div class="use"><div class="ico">🌋</div><h4 data-i18n="useDisT">Disaster awareness</h4><p data-i18n="useDisP">Surface recent earthquakes, tsunami advisories, and nearby designated evacuation shelters.</p><div class="tools"><code>jp_earthquake_list</code><code>jp_tsunami_list</code><code>jp_evacuation_shelters</code></div></div>
        <div class="use"><div class="ico">📍</div><h4 data-i18n="useMapT">Maps &amp; addressing</h4><p data-i18n="useMapP">Search places, geocode, reverse-geocode, resolve postal codes, and read GSI elevation — all without keys.</p><div class="tools"><code>jp_geocode</code><code>jp_postal_code</code><code>jp_elevation</code></div></div>
        <div class="use"><div class="ico">🗾</div><h4 data-i18n="useTourT">Travel &amp; tourism</h4><p data-i18n="useTourP">Find nearby attractions from OpenStreetMap and pair with weather or holiday calendars.</p><div class="tools"><code>jp_tourism_spots</code><code>jp_public_holidays</code></div></div>
        <div class="use"><div class="ico">📈</div><h4 data-i18n="useFinT">Macro / finance bots</h4><p data-i18n="useFinP">Pull Bank of Japan series such as overnight call rates into research or agent workflows.</p><div class="tools"><code>jp_boj_finance</code></div></div>
        <div class="use"><div class="ico">📚</div><h4 data-i18n="useDataT">Open data explorer</h4><p data-i18n="useDataP">Search DATA.GO.JP / e-Gov packages, inspect metadata, and query datastore tables.</p><div class="tools"><code>jp_datasets_search</code><code>jp_dataset_query</code></div></div>""",
    """        <div class="use"><div class="ico">⛅</div><h4 data-i18n="useWxT">Weather-aware apps</h4><p data-i18n="useWxP">Adm4 village codes, BMKG overviews, 24h/4-day forecasts, UV, rain, and air quality for Jakarta or any Indonesian village.</p><div class="tools"><code>id_weather_24h</code><code>id_weather_warnings</code><code>id_uv_index</code></div></div>
        <div class="use"><div class="ico">🌋</div><h4 data-i18n="useDisT">Disaster awareness</h4><p data-i18n="useDisP">Surface recent earthquakes, tsunami potential, Jakarta floods, volcanoes, and nearby evacuation points.</p><div class="tools"><code>id_earthquake_list</code><code>id_flood_reports</code><code>id_evacuation_shelters</code></div></div>
        <div class="use"><div class="ico">📍</div><h4 data-i18n="useMapT">Maps &amp; addressing</h4><p data-i18n="useMapP">Search places, geocode, reverse-geocode, resolve postal codes, and walk Kemendagri wilayah — all without keys.</p><div class="tools"><code>id_geocode</code><code>id_postal_code</code><code>id_provinces</code></div></div>
        <div class="use"><div class="ico">🚆</div><h4 data-i18n="useTourT">Travel &amp; commuting</h4><p data-i18n="useTourP">Find nearby attractions, KRL departures, and prayer times for the same city.</p><div class="tools"><code>id_tourism_spots</code><code>id_krl_schedule</code><code>id_prayer_schedule</code></div></div>
        <div class="use"><div class="ico">📈</div><h4 data-i18n="useFinT">Finance bots</h4><p data-i18n="useFinP">Pull Bank Indonesia USD/IDR, gold prices, bank directories, or Indodax tickers into agent workflows.</p><div class="tools"><code>id_bi_finance</code><code>id_gold_price</code><code>id_indodax_ticker</code></div></div>
        <div class="use"><div class="ico">📚</div><h4 data-i18n="useDataT">Open data explorer</h4><p data-i18n="useDataP">Search HDX Indonesia packages, inspect metadata, and query datastore tables — plus live news headlines.</p><div class="tools"><code>id_datasets_search</code><code>id_news</code></div></div>""",
)

src = src.replace("MonstarX Japan MCP is a remote HTTP server", "MonstarX Indonesia MCP is a remote HTTP server")
src = src.replace(
    "Upstream platform — JMA bosai, Open-Meteo, GSI, DATA.GO.JP, BOJ, zipcloud, etc.",
    "Upstream platform — BMKG, Open-Meteo, Nominatim, HDX, Comuline, Nager.Date, etc.",
)
src = src.replace(
    "Originating body — Japan Meteorological Agency, GSI, Digital Agency, Bank of Japan, …",
    "Originating body — BMKG, Bank Indonesia, KPU, Kemenag, OJK, …",
)
src = src.replace("Live timestamps inside payloads are often JST (+09:00).", "Live timestamps inside payloads are often WIB (+07:00).")
src = src.replace("All 27 tools", "All 55 tools")
src = src.replace("Every tool is prefixed <code>jp_</code>", "Every tool is prefixed <code>id_</code>")
src = src.replace(
    """      <div class="top"><span class="logo"><svg class="mx" viewBox="0 0 30 30" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M29.3493 25.3568L20.5472 16.5546L16.5546 20.5472L25.3568 29.3493L29.3493 25.3568ZM8.76813 12.7607L12.7607 8.76813L3.99257 0L0 3.99257L8.76813 12.7607ZM9.03679e-07 25.3568L8.8024 16.5543L12.795 20.5469L3.99257 29.3493L9.03679e-07 25.3568ZM20.5814 12.7605L16.5889 8.7679L25.3568 0L29.3493 3.99257L20.5814 12.7605Z"/></svg></span> <b>MonstarX</b> <span style="color:var(--faint)">Japan MCP</span></div>
      <div class="cols">
        <div><h4 data-i18n="ftSources">Data sources</h4><div><a href="https://www.jma.go.jp/bosai/">JMA bosai</a> · weather, quakes, tsunami</div><div><a href="https://open-meteo.com/">Open-Meteo</a> · hourly / air quality</div><div><a href="https://www.gsi.go.jp/">GSI</a> · address, elevation</div><div><a href="https://www.e-gov.go.jp/">DATA.GO.JP / e-Gov</a> · open catalog</div><div><a href="https://www.boj.or.jp/">Bank of Japan</a> · time-series</div></div>""",
    """      <div class="top"><span class="logo"><svg class="mx" viewBox="0 0 30 30" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M29.3493 25.3568L20.5472 16.5546L16.5546 20.5472L25.3568 29.3493L29.3493 25.3568ZM8.76813 12.7607L12.7607 8.76813L3.99257 0L0 3.99257L8.76813 12.7607ZM9.03679e-07 25.3568L8.8024 16.5543L12.795 20.5469L3.99257 29.3493L9.03679e-07 25.3568ZM20.5814 12.7605L16.5889 8.7679L25.3568 0L29.3493 3.99257L20.5814 12.7605Z"/></svg></span> <b>MonstarX</b> <span style="color:var(--faint)">Indonesia MCP</span></div>
      <div class="cols">
        <div><h4 data-i18n="ftSources">Data sources</h4><div><a href="https://data.bmkg.go.id/">BMKG</a> · weather, quakes, tsunami</div><div><a href="https://open-meteo.com/">Open-Meteo</a> · hourly / air quality / elevation</div><div><a href="https://nominatim.openstreetmap.org/">Nominatim</a> · address, geocode</div><div><a href="https://data.humdata.org/">HDX</a> · open catalog</div><div><a href="https://www.bi.go.id/">Bank Indonesia</a> · FX via Frankfurter</div></div>""",
)
src = src.replace("MonstarX Japan MCP · v0.1.0", "MonstarX Indonesia MCP · v0.1.0")
src = src.replace(
    "Data remains subject to each source's terms (JMA, GSI, Open-Meteo, DATA.GO.JP/e-Gov, BOJ, zipcloud, Nager.Date, OpenStreetMap ODbL). You are responsible for complying with the source licences. MonstarX is an independent wrapper and is not endorsed by any government agency. This is a staging deployment — don't build production load on it. Example payloads captured for documentation 2026-08-07.",
    "Data remains subject to each source's terms (BMKG, Open-Meteo, Nominatim/OSM ODbL, HDX, Nager.Date, Comuline, KPU SIREKAP archive, and others listed in the tools). You are responsible for complying with the source licences. MonstarX is an independent wrapper and is not endorsed by any government agency. This is a staging deployment — don't build production load on it. Example payloads captured for documentation 2026-08-26.",
)
src = src.replace("🇯🇵 日本語", "🇮🇩 Bahasa Indonesia")
src = src.replace("data-lang=\"ja\"", "data-lang=\"id\"")

src = src.replace("const EP='https://jp-mcp-staging.monstarxapp.com';", "const EP='https://id-mcp-staging.monstarxapp.com';")
src = src.replace("let LANG=localStorage.getItem('mx-lang-jp')||'en';", "let LANG=localStorage.getItem('mx-lang-id')||'en';")
src = src.replace("localStorage.setItem('mx-lang-jp',lang);", "localStorage.setItem('mx-lang-id',lang);")
src = src.replace("localStorage.getItem('mx-theme-jp')", "localStorage.getItem('mx-theme-id')")
src = src.replace("localStorage.setItem('mx-theme-jp',nx);", "localStorage.setItem('mx-theme-id',nx);")
src = src.replace("monstarx-mcp-jp", "monstarx-mcp-id")
src = src.replace("jp-mcp ", "id-mcp ")
src = src.replace("jp-mcp'+", "id-mcp'+")
src = src.replace("{mcpServers:{japan:{type:\"http\",url:EP+'/mcp'}}}", "{mcpServers:{indonesia:{type:\"http\",url:EP+'/mcp'}}}")
src = src.replace("{mcpServers:{japan:{command:\"npx\",args:[\"-y\",\"mcp-remote\",EP+'/mcp']}}}", "{mcpServers:{indonesia:{command:\"npx\",args:[\"-y\",\"mcp-remote\",EP+'/mcp']}}}")

# Language switcher labels
src = src.replace("if(lbl)lbl.textContent=lang==='ja'?'日本語':'EN';", "if(lbl)lbl.textContent=lang==='id'?'ID':'EN';")
src = src.replace("document.documentElement.lang=lang==='ja'?'ja':'en';", "document.documentElement.lang=lang==='id'?'id':'en';")
src = src.replace("if(!I18N[lang])lang='en';", "if(!I18N[lang])lang='en';")

src = src.replace("en-JP", "en-ID")
src = src.replace("+09:00", "+07:00")
src = src.replace("'JMA overview", "'BMKG overview")
src = src.replace("' JMA forecast offices", "' BMKG starter areas")
src = src.replace("p.offices||[]", "p.offices||p.areas||[]")
src = src.replace("p.total_offices||o.length", "p.total_offices||p.total_areas||o.length")
src = src.replace("esc(x.en_name||'')", "esc(x.en_name||x.city||x.province||'')")
src = src.replace("Japan public holidays", "Indonesia public holidays")
src = src.replace("BOJ · ", "BI · ")
src = src.replace("'toLocaleString('en-US')", "'toLocaleString('en-ID')")

# I18N English pack replacements
en_repls = [
    ("filterTools:'Filter 27 tools…'", "filterTools:'Filter 55 tools…'"),
    ("eyebrow:'MonstarX · Japan MCP'", "eyebrow:'MonstarX · Indonesia MCP'"),
    (
        'heroTitle:"Japan\'s public data, <span class=\\"hl\\">ready for your AI</span>."',
        'heroTitle:"Indonesia\'s public data, <span class=\\"hl\\">ready for your AI</span>."',
    ),
    (
        'heroLede:"Weather, earthquakes, geocoding, postal codes, holidays, evacuation shelters, tourism spots, Bank of Japan series, open datasets — Japan\'s free public APIs live across many agencies, each with its own formats and quirks. <b>MonstarX unifies them into 27 tools any AI agent can call</b>, through one endpoint, with no API keys. Stop writing integration glue. Start shipping Japan-smart products."',
        'heroLede:"Weather, earthquakes, geocoding, wilayah codes, holidays, KRL, news, prayer times, gold prices, open datasets — Indonesia\'s free public APIs live across many agencies, each with its own formats and quirks. <b>MonstarX unifies them into 55 tools any AI agent can call</b>, through one endpoint, with no API keys. Stop writing integration glue. Start shipping Indonesia-smart products."',
    ),
    ("streams back real Japan data", "streams back real Indonesia data"),
    ("chipWx:'Tokyo weather 24h'", "chipWx:'Jakarta weather 24h'"),
    ("chipGeo:'Geocode 東京駅'", "chipGeo:'Geocode Monas'"),
    ("chipPostal:'Postal 100-0001'", "chipPostal:'Postal 10110'"),
    ("chipHoliday:'Holidays 2026',chipShelter:'Shelters · Chiyoda',chipTourism:'Tourism near Tokyo St.',chipDatasets:'Search 天気 datasets'",
     "chipHoliday:'Holidays 2026',chipKrl:'KRL Manggarai',chipTourism:'Tourism near Monas',chipDatasets:'Search earthquake datasets'"),
    ("useWxP:'Area codes, daily/weekly JMA text, 24h/4-day forecasts, UV, rain, and air quality for Tokyo or any prefecture office.'",
     "useWxP:'Adm4 village codes, BMKG overviews, 24h/4-day forecasts, UV, rain, and air quality for Jakarta or any Indonesian village.'"),
    ("useDisP:'Surface recent earthquakes, tsunami advisories, and nearby designated evacuation shelters.'",
     "useDisP:'Surface recent earthquakes, tsunami potential, Jakarta floods, volcanoes, and nearby evacuation points.'"),
    ("useMapT:'Maps & addressing',useMapP:'Search places, geocode, reverse-geocode, resolve postal codes, and read GSI elevation — all without keys.'",
     "useMapT:'Maps & addressing',useMapP:'Search places, geocode, reverse-geocode, resolve postal codes, and walk Kemendagri wilayah — all without keys.'"),
    ("useTourT:'Travel & tourism',useTourP:'Find nearby attractions from OpenStreetMap and pair with weather or holiday calendars.'",
     "useTourT:'Travel & commuting',useTourP:'Find nearby attractions, KRL departures, and prayer times for the same city.'"),
    ("useFinT:'Macro / finance bots',useFinP:'Pull Bank of Japan series such as overnight call rates into research or agent workflows.'",
     "useFinT:'Finance bots',useFinP:'Pull Bank Indonesia USD/IDR, gold prices, bank directories, or Indodax tickers into agent workflows.'"),
    ("useDataP:'Search DATA.GO.JP / e-Gov packages, inspect metadata, and query datastore tables.'",
     "useDataP:'Search HDX Indonesia packages, inspect metadata, and query datastore tables — plus live news headlines.'"),
    ("secConnectBlurb:'MonstarX Japan MCP is a remote HTTP server speaking the Model Context Protocol. Point any MCP-capable client at the endpoint — no auth handshake, it\\'s stateless.'",
     "secConnectBlurb:'MonstarX Indonesia MCP is a remote HTTP server speaking the Model Context Protocol. Point any MCP-capable client at the endpoint — no auth handshake, it\\'s stateless.'"),
    ("fSource:'Upstream platform — JMA bosai, Open-Meteo, GSI, DATA.GO.JP, BOJ, zipcloud, etc.'",
     "fSource:'Upstream platform — BMKG, Open-Meteo, Nominatim, HDX, Comuline, Nager.Date, etc.'"),
    ("fAgency:'Originating body — Japan Meteorological Agency, GSI, Digital Agency, Bank of Japan, …'",
     "fAgency:'Originating body — BMKG, Bank Indonesia, KPU, Kemenag, OJK, …'"),
    ("fRetrieved:'Server fetch time (UTC). Live timestamps inside payloads are often JST (+09:00).'",
     "fRetrieved:'Server fetch time (UTC). Live timestamps inside payloads are often WIB (+07:00).'"),
    ("secTools:'All 27 tools'", "secTools:'All 55 tools'"),
    ("secToolsBlurb:'Every tool is prefixed <code>jp_</code>;", "secToolsBlurb:'Every tool is prefixed <code>id_</code>;"),
    (
        "ftDisc:'Data remains subject to each source\\'s terms (JMA, GSI, Open-Meteo, DATA.GO.JP/e-Gov, BOJ, zipcloud, Nager.Date, OpenStreetMap ODbL). You are responsible for complying with the source licences. MonstarX is an independent wrapper and is not endorsed by any government agency. This is a staging deployment — don\\'t build production load on it. Example payloads captured for documentation 2026-08-07.'",
        "ftDisc:'Data remains subject to each source\\'s terms (BMKG, Open-Meteo, Nominatim/OSM ODbL, HDX, Nager.Date, Comuline, KPU SIREKAP archive, and others listed in the tools). You are responsible for complying with the source licences. MonstarX is an independent wrapper and is not endorsed by any government agency. This is a staging deployment — don\\'t build production load on it. Example payloads captured for documentation 2026-08-26.'",
    ),
    (
        "cat_weather:'Weather & Environment',cat_hazards:'Earthquakes & Tsunami',cat_geo:'Geocoding & Addresses',cat_civic:'Civic & Safety',cat_places:'Tourism',cat_finance:'Finance (BOJ)',cat_catalog:'Open Data Catalog',",
        "cat_weather:'Weather & Environment',cat_hazards:'Hazards & Disasters',cat_geo:'Geocoding & Wilayah',cat_civic:'Civic & Safety',cat_places:'Tourism',cat_transport:'Commuter (KRL)',cat_news:'News',cat_health:'Health',cat_finance:'Finance',cat_culture:'Language & Faith',cat_catalog:'Open Data Catalog',",
    ),
]
for a, b in en_repls:
    if a not in src:
        print("WARN missing EN fragment:", a[:80])
    else:
        src = src.replace(a, b, 1)

# Replace Japanese I18N block with Bahasa Indonesia
ja_start = src.find("\nja:{")
ja_end = src.find("\n}", ja_start)
if ja_start < 0 or ja_end < 0:
    raise SystemExit("ja I18N block not found")
id_block = r"""
id:{
navPlayground:'Playground',navTools:'Alat',navConnect:'Sambungkan',
navLivePg:'▶ Playground langsung',navUseCases:'Yang bisa dibangun',navConnectAgent:'Sambungkan agen',navResponse:'Format respons',navErrors:'Kesalahan',
filterTools:'Saring 55 alat…',eyebrow:'MonstarX · Indonesia MCP',
heroTitle:'Data publik Indonesia, <span class="hl">siap untuk AI Anda</span>.',
heroLede:'Cuaca, gempa, geocoding, kode wilayah, hari libur, KRL, berita, jadwal sholat, harga emas, dataset terbuka — API publik gratis Indonesia tersebar di banyak lembaga, masing-masing dengan format sendiri. <b>MonstarX menyatukannya menjadi 55 alat yang bisa dipanggil agen AI</b>, satu endpoint, tanpa API key. Berhenti menulis glue integration. Mulai kirim produk yang paham Indonesia.',
ctaTry:'▶ Coba langsung di browser',ctaConnect:'Sambungkan Claude atau Cursor',
statTools:'alat siap pakai',statSources:'sumber publik gratis',statKeys:'API key atau daftar',statLiveN:'Live',statLive:'data real-time',
secPlayground:'Playground langsung',
secPlaygroundBlurb:'Pilih alat, ubah input, tekan <b>Jalankan</b> — kueri langsung ke server MCP dan mengembalikan data Indonesia nyata. Tanpa daftar. Coba contoh sekali klik:',
tryLabel:'Coba',
chipWx:'Cuaca Jakarta 24 jam',chipQuake:'Gempa terbaru',chipGeo:'Geocode Monas',chipPostal:'Kode pos 10110',
chipHoliday:'Libur 2026',chipKrl:'KRL Manggarai',chipTourism:'Wisata dekat Monas',chipDatasets:'Cari dataset gempa',
secUse:'Yang bisa dibangun',secUseBlurb:'Hackathon akhir pekan atau fitur produksi — semua hanya beberapa pemanggilan alat.',
useWxT:'Aplikasi sadar cuaca',useWxP:'Kode adm4, ringkasan BMKG, prakiraan 24 jam/4 hari, UV, hujan, dan kualitas udara.',
useDisT:'Kesadaran bencana',useDisP:'Gempa, potensi tsunami, banjir Jakarta, gunung berapi, dan titik evakuasi.',
useMapT:'Peta & alamat',useMapP:'Cari tempat, geocode, reverse-geocode, kode pos, dan wilayah Kemendagri — tanpa kunci.',
useTourT:'Perjalanan & KRL',useTourP:'Tempat wisata, keberangkatan KRL, dan jadwal sholat untuk kota yang sama.',
useFinT:'Bot keuangan',useFinP:'Kurs BI USD/IDR, harga emas, direktori bank, atau ticker Indodax.',
useDataT:'Penjelajah data terbuka',useDataP:'Cari paket HDX Indonesia, metadata, datastore, plus berita.',
secConnect:'Sambungkan agen Anda',
secConnectBlurb:'MonstarX Indonesia MCP adalah server HTTP jarak jauh Model Context Protocol. Arahkan klien MCP ke endpoint — tanpa handshake auth, stateless.',
labClaude:'Claude Code',labCursor:'Cursor / klien HTTP native',
labDesk:'Claude Desktop — <span style="text-transform:none;letter-spacing:0;font-weight:400;color:var(--faint)">claude_desktop_config.json</span>',
labCurl:'Atau cURL saja',
secResponse:'Format respons',
secResponseBlurb:'Setiap panggilan mengembalikan payload dua kali — string JSON di <code>content[0].text</code> dan objek di <code>structuredContent</code> (lebih disarankan). Setiap payload dibungkus amplop sumber, lembaga, dan waktu ambil.',
thField:'Bidang',thMeaning:'Arti',
fSource:'Platform hulu — BMKG, Open-Meteo, Nominatim, HDX, Comuline, Nager.Date, dll.',
fAgency:'Lembaga asal — BMKG, Bank Indonesia, KPU, Kemenag, OJK, …',
fApi:'API hulu spesifik yang dikueri.',
fLicense:'Lisensi / syarat data bila ada.',
fRetrieved:'Waktu ambil server (UTC). Stempel waktu di payload sering WIB (+07:00).',
fData:'Isi. Alat daftar menambahkan <code>total</code> / <code>shown</code> / <code>found</code>.',
secErrors:'Kesalahan',
secErrorsBlurb:'Kesalahan kembali sebagai hasil biasa dengan <code>isError: true</code> dan pesan di <code>content[0].text</code>. Argumen tidak valid mengembalikan MCP <code>-32602</code>. Daftar kosong adalah "tidak ada hasil", bukan error.',
secTools:'Semua 55 alat',
secToolsBlurb:'Semua berawalan <code>id_</code>; parameter wajib ditandai <span style="color:var(--accent)">*</span>. Tekan <b>Coba di playground</b> untuk memuat contoh.',
ftSources:'Sumber data',ftEndpoints:'Endpoint',ftServer:'Server',
ftDisc:'Data tetap tunduk pada syarat masing-masing sumber (BMKG, Open-Meteo, Nominatim/OSM ODbL, HDX, Nager.Date, Comuline, arsip KPU SIREKAP, dan lainnya). Kepatuhan lisensi adalah tanggung jawab pengguna. MonstarX adalah wrapper independen dan tidak didukung lembaga pemerintah. Ini staging — jangan bangun beban produksi di atasnya. Contoh dokumentasi 2026-08-26.',
cat_weather:'Cuaca & Lingkungan',cat_hazards:'Bencana',cat_geo:'Geocoding & Wilayah',cat_civic:'Sipil & Keselamatan',cat_places:'Pariwisata',cat_transport:'KRL',cat_news:'Berita',cat_health:'Kesehatan',cat_finance:'Keuangan',cat_culture:'Bahasa & Iman',cat_catalog:'Katalog Data Terbuka',
runQuery:'▶ Jalankan kueri',running:'Menjalankan…',copyCurl:'Salin sebagai cURL',copiedCurl:'cURL tersalin',resetEx:'Kembali ke contoh',
noParams:'Alat ini tanpa parameter — langsung jalankan.',sampleReqs:'Contoh permintaan',tryPlay:'▶ Coba di playground',
exCall:'Contoh panggilan & respons',exCallSub:'Contoh panggilan',exRespSub:'Contoh respons — dipangkas',
noParamsBadge:'tanpa param',tabVisual:'Visual',tabJson:'JSON',tabRaw:'Raw',
contacting:'menghubungi server…',hintCors:'Panggilan langsung butuh server MCP yang bisa dijangkau browser (CORS terbuka). Gunakan URL staging atau monstarx-mcp-id lokal.',
previewNote:'<b>Mode pratinjau.</b> Kueri langsung dibatasi sandbox — unduh halaman ini dan buka dari host Anda sendiri untuk menjalankan ke server.',
paramRequired:'wajib',paramOptional:'opsional'
}"""
src = src[:ja_start] + id_block + src[ja_end + 2 :]

# Connect / envelope / error samples
src = src.replace(
    "curlFor('jp_weather_24h',{area_code:'130000'})",
    "curlFor('id_weather_24h',{area_code:'31.71.03.1001'})",
)
src = src.replace(
    "codeblock('structuredContent — jp_weather_24h',hl({source:\"Open-Meteo JMA\",agency:\"Open-Meteo\",retrieved_at:\"2026-08-07T04:00:00.000Z\",api:\"v1/jma (hourly forecast 24h)\",area_code:\"130000\",location:{latitude:35.6895,longitude:139.6917},data:{hourly:{time:[\"2026-08-07T00:00\"],temperature_2m:[26.1]}}}))",
    "codeblock('structuredContent — id_weather_24h',hl({source:\"Open-Meteo Forecast\",agency:\"Open-Meteo\",retrieved_at:\"2026-08-26T04:00:00.000Z\",api:\"v1/forecast (hourly forecast 24h)\",area_code:\"31.71.03.1001\",location:{latitude:-6.175392,longitude:106.827153},data:{hourly:{time:[\"2026-08-26T00:00\"],temperature_2m:[26.4]}}}))",
)
src = src.replace("jp_postal_code", "id_postal_code")

SAMPLES = r"""const SAMPLES={
 id_weather_overview:{area_code:['31.71.03.1001','32.73.05.1001','51.71.04.2006','35.78.07.1001','12.71.01.1001']},
 id_weather_week_overview:{area_code:['31.71.03.1001','32.73.05.1001','51.71.04.2006']},
 id_weather_warnings:{area_code:['31.71.03.1001','32.73.05.1001','13.71.01.1001']},
 id_weather_24h:{area_code:['31.71.03.1001','32.73.05.1001','51.71.04.2006','35.78.07.1001','12.71.01.1001']},
 id_weather_4day:{area_code:['31.71.03.1001','32.73.05.1001','51.71.04.2006']},
 id_uv_index:{area_code:['31.71.03.1001','51.71.04.2006']},
 id_rainfall:{area_code:['31.71.03.1001','32.73.05.1001']},
 id_air_temperature:{area_code:['31.71.03.1001','32.73.05.1001']},
 id_relative_humidity:{area_code:['31.71.03.1001','32.73.05.1001']},
 id_air_quality:{area_code:['31.71.03.1001','32.73.05.1001']},
 id_earthquake_list:{limit:['5','10','20']},
 id_tsunami_list:{limit:['5','10','20']},
 id_flood_reports:{limit:['5','10','20']},
 id_volcanoes:{name:['merapi','krakatau','semeru']},
 id_postal_code:{zipcode:['10110','40115','80234','60241','20111']},
 id_public_holidays:{year:['2026','2025','2027']},
 id_cuti_bersama:{year:['2026','2025']},
 id_elevation:{latitude:['-6.175392','-8.409518','-7.7956'],longitude:['106.827153','115.188919','110.3695']},
 id_bi_finance:{from:['USD','EUR','JPY'],to:['IDR']},
 id_disease_reports:{query:['dengue','malaria','penyakit']},
 id_evacuation_shelters:{latitude:['-6.175392','-6.9175'],longitude:['106.827153','107.6191']},
 id_tourism_spots:{latitude:['-6.175392','-8.409518','-7.7956'],longitude:['106.827153','115.188919','110.3695']},
 id_address_search:{query:['Monas','Jl. Thamrin Jakarta','Malioboro','Kuta','Braga']},
 id_geocode:{query:['Monas Jakarta','Bandung','Denpasar','Surabaya','Medan']},
 id_reverse_geocode:{latitude:['-6.175392','-6.9175','-8.409518'],longitude:['106.827153','107.6191','115.188919']},
 id_datasets_search:{query:['earthquake','penduduk','cuaca','banjir']},
 id_dataset_show:{id:['cod-ab-idn','wfp-food-prices-for-indonesia']},
 id_dataset_metadata:{id:['cod-ab-idn']},
 id_dataset_query:{resource_id:['cod-ab-idn-sample']},
 id_regencies:{province_id:['31','32','51','35']},
 id_districts:{regency_id:['3173','3273','5171']},
 id_villages:{district_id:['3173060','3173080']},
 id_news:{source:['cnn-news','detik-news','kompas-news']},
 id_news_category:{source:['cnn-news'],category:['nasional','ekonomi','teknologi']},
 id_news_search:{query:['jakarta','gempa']},
 id_krl_stations:{query:['MRI','GMR','manggarai','bogor']},
 id_krl_schedule:{station_id:['MRI','GMR','BKS','AC']},
 id_kpu_election_2024:{view:['candidates','wilayah','results'],wilayah_codes:['31','31/3173']},
 id_parse_nik:{nik:['3173061501850001']},
 id_faskes:{latitude:['-6.175392'],longitude:['106.827153']},
 id_kbbi:{word:['rumah','merdeka','gotong royong']},
 id_prayer_cities:{query:['jakarta','bandung','surabaya']},
 id_prayer_schedule:{city_id:['1301']},
 id_quran_surah:{number:['1','18','36','55']},
 id_gold_price:{source:['anekalogam','pegadaian']},
 id_banks:{keyword:['bri','mandiri','bca']},
 id_ojk_invest:{category:['illegal','apps','products']},
 id_indodax_ticker:{pair:['btcidr','ethidr','usdtidr']},
 id_hadith:{perawi:['bukhari','muslim']},
 id_doa:{query:['makan','tidur','perjalanan']}
};"""
ASK = r"""const ASK={
 id_weather_areas:"What BMKG adm4 village codes can I use for forecasts?",
 id_weather_overview:"What's the BMKG overview for Kemayoran, Jakarta Pusat?",
 id_weather_week_overview:"What's the 3-day outlook for Jakarta Pusat?",
 id_weather_warnings:"Are there rain or storm slots in the Jakarta forecast?",
 id_weather_24h:"What's the hourly forecast in Jakarta for the next 24 hours?",
 id_weather_4day:"What's the 4-day forecast for Jakarta?",
 id_uv_index:"How high is the UV index in Jakarta today?",
 id_rainfall:"Is it raining in Jakarta right now (hourly)?",
 id_air_temperature:"What are hourly temperatures in Jakarta?",
 id_relative_humidity:"How humid is it in Jakarta hour by hour?",
 id_air_quality:"How's the air quality (PM2.5 / AQI) in Jakarta?",
 id_earthquake_list:"What earthquakes has BMKG reported recently?",
 id_tsunami_list:"Are there any recent tsunami-potential events?",
 id_flood_reports:"Any recent Jakarta flood reports?",
 id_volcanoes:"Find volcanoes named Merapi.",
 id_postal_code:"What address is postal code 10110?",
 id_public_holidays:"Which public holidays does Indonesia have in 2026?",
 id_cuti_bersama:"What cuti bersama days are in 2026?",
 id_elevation:"What's the elevation at Monas?",
 id_bi_finance:"What's the latest USD/IDR rate from Bank Indonesia?",
 id_disease_reports:"Find open datasets about dengue.",
 id_evacuation_shelters:"Where are evacuation points near Monas?",
 id_tourism_spots:"What tourist attractions are near Monas?",
 id_address_search:"Find addresses matching Monas.",
 id_geocode:"What are the coordinates of Monas Jakarta?",
 id_reverse_geocode:"What's the address at -6.175392, 106.827153?",
 id_datasets_search:"What open datasets mention earthquake?",
 id_dataset_show:"Show metadata for package cod-ab-idn.",
 id_dataset_metadata:"Get dataset metadata by package id.",
 id_dataset_query:"Query rows from an HDX datastore resource.",
 id_provinces:"List Indonesian provinces.",
 id_regencies:"List kabupaten/kota in DKI Jakarta.",
 id_districts:"List kecamatan in Jakarta Pusat.",
 id_villages:"List kelurahan in Kemayoran.",
 id_news:"Latest CNN Indonesia headlines?",
 id_news_category:"CNN nasional headlines?",
 id_news_search:"Search CNN headlines for Jakarta.",
 id_krl_stations:"Find the Manggarai KRL station.",
 id_krl_schedule:"What trains leave Manggarai (MRI) next?",
 id_kpu_election_2024:"Show the 2024 presidential candidate archive.",
 id_parse_nik:"Decode NIK 3173061501850001 (format only).",
 id_faskes:"Hospitals and clinics near Monas?",
 id_kbbi:"What does merdeka mean in KBBI?",
 id_prayer_cities:"Find the prayer-time city id for Jakarta.",
 id_prayer_schedule:"August 2026 prayer times for Kota Jakarta?",
 id_quran_list:"List all 114 surahs.",
 id_quran_surah:"Get Al-Fatihah with Indonesian translation.",
 id_hadith:"Show Bukhari hadith number 1.",
 id_doa:"Daily doa about eating.",
 id_asmaul_husna:"The first of the 99 names.",
 id_gold_price:"Current Antam gold sell/buyback?",
 id_banks:"Search the bank directory for BRI.",
 id_ojk_invest:"Search OJK illegal-investment list for binary.",
 id_indodax_ticker:"What's the BTC/IDR ticker on Indodax?",
 id_heroes:"Search national heroes named Soekarno."
};"""
PRESETS = r"""const PRESETS={
 id_reverse_geocode:[
  {label:'Monas',args:{latitude:-6.175392,longitude:106.827153}},
  {label:'Bandung',args:{latitude:-6.9175,longitude:107.6191}},
  {label:'Denpasar',args:{latitude:-8.409518,longitude:115.188919}}
 ],
 id_elevation:[
  {label:'Monas',args:{latitude:-6.175392,longitude:106.827153}},
  {label:'Merapi area',args:{latitude:-7.5407,longitude:110.4461}}
 ],
 id_tourism_spots:[
  {label:'Monas',args:{latitude:-6.175392,longitude:106.827153,radius_m:1500,limit:10}},
  {label:'Kuta',args:{latitude:-8.718,longitude:115.169,radius_m:2000,limit:10}}
 ],
 id_evacuation_shelters:[
  {label:'Near Monas',args:{latitude:-6.175392,longitude:106.827153,limit:10}},
  {label:'Bandung',args:{latitude:-6.9175,longitude:107.6191,limit:10}}
 ],
 id_faskes:[
  {label:'Near Monas',args:{latitude:-6.175392,longitude:106.827153,radius_m:2000,limit:10}}
 ]
};"""

def replace_block(text, start_marker, end_marker, new_block):
    a = text.find(start_marker)
    b = text.find(end_marker, a)
    if a < 0 or b < 0:
        raise SystemExit(f"block not found: {start_marker[:40]}")
    return text[:a] + new_block + "\n" + text[b:]

src = replace_block(src, "const SAMPLES={", "const ASK={", SAMPLES + "\n")
src = replace_block(src, "const ASK={", "const PRESETS={", ASK + "\n")
src = replace_block(src, "const PRESETS={", "/* ---------- visual helpers ---------- */", PRESETS + "\n")

MAP = r"""/* Indonesia map bounds (Sumatra to Papua) */
const IDB={lo:94.5,ln:141.5,la:-11.5,lt:6.5};
const ID_OUTLINE=[[95.0,5.5],[97.5,5.6],[106.0,6.0],[119.0,5.0],[125.0,2.0],[131.0,0.5],[141.0,-2.5],[141.0,-9.2],[131.0,-8.4],[125.0,-8.6],[115.5,-8.8],[114.4,-8.7],[105.3,-6.9],[102.2,-5.6],[95.2,5.4]];
function prj(lng,lat){return [((lng-IDB.lo)/(IDB.ln-IDB.lo))*1000,((IDB.lt-lat)/(IDB.lt-IDB.la))*600];}
function mapView(points,note){
 points=(points||[]).filter(p=>isFinite(p.lat)&&isFinite(p.lng)&&p.lat>-12&&p.lat<8&&p.lng>94&&p.lng<142);
 if(!points.length)return null;
 const cap=60,shown=points.slice(0,cap);
 const path='M'+ID_OUTLINE.map(c=>prj(c[0],c[1]).map(n=>n.toFixed(1)).join(',')).join(' L')+' Z';
 const pins=shown.map(p=>{const a=prj(p.lng,p.lat);return '<g><circle cx="'+a[0].toFixed(1)+'" cy="'+a[1].toFixed(1)+'" r="9" fill="var(--accent)" fill-opacity="0.92" stroke="#fff" stroke-width="2"/>'+(p.value?'<text x="'+a[0].toFixed(1)+'" y="'+(a[1]-14).toFixed(1)+'" class="pv">'+esc(p.value)+'</text>':'')+'<title>'+esc((p.label||'')+(p.sub?' · '+p.sub:''))+'</title></g>';}).join('');
 const list=shown.map(p=>'<li><span class="dotp"></span><b>'+esc(p.label||'—')+'</b>'+(p.sub?' <span>'+esc(p.sub)+'</span>':'')+(p.value?' <em>'+esc(p.value)+'</em>':'')+'</li>').join('');
 return '<div class="vmap"><svg viewBox="0 0 1000 600" preserveAspectRatio="xMidYMid meet"><path d="'+path+'" fill="var(--map-land)" stroke="var(--map-stroke)" stroke-width="2" stroke-linejoin="round"/>'+pins+'</svg></div><ol class="vlist">'+list+'</ol>'+(points.length>cap?'<div class="vnote">Showing '+cap+' of '+points.length+' points.</div>':'')+(note?'<div class="vnote">'+esc(note)+'</div>':'');
}
"""
src = replace_block(src, "/* Japan map bounds", "function locHead(p)", MAP)

# postal cards: show province too
src = src.replace(
    "esc((x.prefecture||'')+(x.city||'')+(x.town||''))",
    "esc((x.province||x.prefecture||'')+' '+(x.city||'')+' '+(x.district||x.town||'')+' '+(x.village||''))",
)
src = src.replace(
    "<span>Prefecture</span><b>'+esc(x.prefecture||'—')+'</b>",
    "<span>Province</span><b>'+esc(x.province||x.prefecture||'—')+'</b",
)

VIZ = r"""function visualize(name,p){try{return _viz(name,p);}catch(e){console.warn('viz fail',name,e);return null;}}
function listTable(title,rows,cols){
 if(!rows||!rows.length)return '<div class="vhead">'+esc(title)+'</div>'+vstat('—','no rows');
 const keys=cols||Object.keys(rows[0]).slice(0,6);
 return '<div class="vhead">'+esc(title)+' · '+num(rows.length)+'</div><div class="vtwrap"><table class="vt"><thead><tr>'+keys.map(k=>'<th>'+esc(k)+'</th>').join('')+'</tr></thead><tbody>'+rows.slice(0,40).map(r=>'<tr>'+keys.map(k=>'<td>'+esc(r[k]==null?'':(typeof r[k]==='object'?JSON.stringify(r[k]):r[k]))+'</td>').join('')+'</tr>').join('')+'</tbody></table></div>';
}
function _viz(name,p){if(!p||typeof p!=='object')return null;switch(name){
 case 'id_weather_areas':return officesView(p);
 case 'id_weather_overview':
 case 'id_weather_week_overview':return overviewText(p);
 case 'id_weather_warnings':return warningsView(p);
 case 'id_weather_24h':return wx24(p);
 case 'id_weather_4day':return wx4(p);
 case 'id_uv_index':return uvView(p);
 case 'id_rainfall':return rainView(p);
 case 'id_air_temperature':return tempView(p);
 case 'id_relative_humidity':return humView(p);
 case 'id_air_quality':return aqView(p);
 case 'id_earthquake_list':return eventsView(p,'Earthquakes');
 case 'id_tsunami_list':return eventsView(p,'Tsunami potential');
 case 'id_flood_reports':return listTable('Jakarta flood reports',p.reports||[],['title','area','status']);
 case 'id_volcanoes':return listTable('Volcanoes',p.volcanoes||[],['name','type','height_m','province']);
 case 'id_postal_code':return postalView(p);
 case 'id_public_holidays':
 case 'id_cuti_bersama':return holidaysView(p);
 case 'id_elevation':return elevView(p);
 case 'id_bi_finance':{
  const d=p.data||{};const rates=d.rates||{};
  return '<div class="vhead">Bank Indonesia · '+esc(d.base||p.from||'')+' → '+esc(p.to||Object.keys(rates)[0]||'')+'</div>'+vstat((rates.IDR!=null?num(rates.IDR):Object.values(rates)[0]||'—'),esc(d.date||''),'rate');
 }
 case 'id_disease_reports':return datasetsView(p);
 case 'id_evacuation_shelters':return shelterView(p);
 case 'id_tourism_spots':return tourismView(p);
 case 'id_address_search':
 case 'id_geocode':return geoResults(p);
 case 'id_reverse_geocode':return reverseView(p);
 case 'id_datasets_search':return datasetsView(p);
 case 'id_dataset_show':
 case 'id_dataset_metadata':return datasetShow(p);
 case 'id_dataset_query':return genTable(p.records)||null;
 case 'id_provinces':return listTable('Provinces',p.provinces||[],['id','name']);
 case 'id_regencies':return listTable('Regencies / cities',p.regencies||[],['id','name']);
 case 'id_districts':return listTable('Districts',p.districts||[],['id','name']);
 case 'id_villages':return listTable('Villages',p.villages||[],['id','name']);
 case 'id_news':
 case 'id_news_category':
 case 'id_news_search':return listTable('Headlines',p.headlines||[],['title','isoDate']);
 case 'id_krl_stations':return listTable('KRL stations',p.stations||[],['id','name']);
 case 'id_krl_schedule':return listTable('KRL schedule '+esc(p.station_id||''),p.schedule||[],['time','dest','line']);
 case 'id_kpu_election_2024':return listTable('KPU 2024 archive',p.candidates||p.wilayah||(p.results?[p.results]:[])||[]);
 case 'id_parse_nik':return '<div class="vhead">NIK format parse</div><div class="ccard"><div class="cg"><span>NIK</span><b class="mono">'+esc(p.nik||'')+'</b></div><div class="cg"><span>Province</span><b>'+esc(p.province_code||'')+'</b></div><div class="cg"><span>Regency</span><b>'+esc(p.regency_code||'')+'</b></div><div class="cg"><span>DOB</span><b>'+esc(p.date_of_birth||'')+'</b></div><div class="cg"><span>Gender</span><b>'+esc(p.gender||'')+'</b></div></div>';
 case 'id_faskes':{
  const s=p.facilities||[];const pts=s.filter(x=>x.latitude!=null).map(x=>({lat:+x.latitude,lng:+x.longitude,label:x.name,sub:x.amenity}));
  return '<div class="vhead">Health facilities · '+num(p.shown||s.length)+'</div>'+(mapView(pts)||'')+listTable('Facilities',s,['name','amenity']);
 }
 case 'id_kbbi':return listTable('KBBI',p.results||[],['word','meaning']);
 case 'id_prayer_cities':return listTable('Prayer cities',p.cities||[],['id','name']);
 case 'id_prayer_schedule':{
  const j=(p.data&&p.data.jadwal)||[];
  return '<div class="vhead">Prayer schedule · '+esc((p.data&&p.data.lokasi)||p.city_id||'')+'</div>'+listTable('Jadwal',Array.isArray(j)?j.slice(0,10):[],['tanggal','subuh','dzuhur','ashar','maghrib','isya']);
 }
 case 'id_quran_list':return listTable('Surahs',p.surahs||[],['number','name_latin','ayah_count']);
 case 'id_quran_surah':{
  const s=p.surah||{};const v=s.verses||[];
  return '<div class="vhead">'+esc(s.name_latin||('Surah '+s.number))+'</div>'+listTable('Ayah',v,['ayah','latin','id']);
 }
 case 'id_gold_price':return listTable('Gold prices',p.prices||[]);
 case 'id_banks':return listTable('Banks',p.banks||[],['name','code']);
 case 'id_ojk_invest':return listTable('OJK list',p.items||[],['name','category']);
 case 'id_indodax_ticker':{
  const t=p.ticker||{};return '<div class="vhead">Indodax · '+esc(t.pair||'')+'</div><div class="statrow">'+vstat(esc(t.last||'—'),'last')+vstat(esc(t.high||'—'),'high')+vstat(esc(t.low||'—'),'low')+'</div>';
 }
 case 'id_hadith':return p.narrators?listTable('Narrators',p.narrators):('<div class="vhead">Hadith</div><div class="ccard"><div style="white-space:pre-wrap">'+esc(JSON.stringify(p.hadith||p,null,2).slice(0,1200))+'</div></div>');
 case 'id_doa':return listTable('Doa',p.doa||[],['title','latin','id']);
 case 'id_asmaul_husna':return listTable('Asmaul Husna',p.names||[],['number','latin','id']);
 case 'id_heroes':return listTable('National heroes',p.heroes||[],['name','birth','death']);
}return null;}
"""
src = replace_block(src, "function visualize(name,p)", "DATA.categories.forEach(cat=>{\n  const gl=", VIZ)

EX = r"""const EXAMPLES={
  wx24:['id_weather_24h',{area_code:'31.71.03.1001'}],
  quake:['id_earthquake_list',{limit:5}],
  geo:['id_geocode',{query:'Monas Jakarta',limit:3}],
  postal:['id_postal_code',{zipcode:'10110'}],
  holiday:['id_public_holidays',{year:2026}],
  krl:['id_krl_schedule',{station_id:'MRI',limit:8}],
  tourism:['id_tourism_spots',{latitude:-6.175392,longitude:106.827153,radius_m:1500,limit:8}],
  datasets:['id_datasets_search',{query:'earthquake',rows:5}]
};"""
src = replace_block(src, "const EXAMPLES={", "document.querySelectorAll('.chip-ex')", EX + "\n")
src = src.replace("selectTool('jp_weather_24h');", "selectTool('id_weather_24h');")

src = src.replace("MonstarX Japan MCP | Live", "MonstarX Indonesia MCP | Live")
src = src.replace(
    "Japan government open data as 27 MCP tools any AI agent can call. Live in-browser playground: weather, earthquakes, geocoding, holidays, shelters, tourism, open data.",
    "Indonesia government and public open data as 55 MCP tools any AI agent can call. Live in-browser playground: weather, earthquakes, geocoding, KRL, news, holidays, open data.",
)
src = src.replace("wrote public/index.html and japan-mcp-playground.html", "wrote public/index.html and indonesia-mcp-playground.html")

(ROOT / "build.py").write_text(src, encoding="utf-8")
print("patched build.py", len(src), "chars")
