#!/usr/bin/env python3
"""Write build/data.min.json for the Indonesia MCP playground."""
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
TS = "2026-08-26T04:00:00.000Z"
JKT = {"latitude": -6.175392, "longitude": 106.827153}
ADM4 = "31.71.03.1001"
LOC = {
    "area_code": ADM4,
    "name": "Kemayoran",
    "city": "Jakarta Pusat",
    "province": "DKI Jakarta",
    **JKT,
    "timezone": "Asia/Jakarta",
}


def p(name, typ, required, desc):
    return {"name": name, "type": typ, "required": required, "desc": desc}


def tool(cat, desc, params, args, response):
    return {"cat": cat, "desc": desc, "params": params, "args": args, "response": response}


bmkg = {
    "source": "BMKG open data",
    "agency": "Badan Meteorologi, Klimatologi, dan Geofisika",
    "retrieved_at": TS,
    "license": "Follow BMKG website terms; attribution to BMKG is required",
    "auth": "none",
}
om = {"source": "Open-Meteo Forecast", "agency": "Open-Meteo", "retrieved_at": TS, "auth": "none"}
omaq = {"source": "Open-Meteo Air Quality", "agency": "Open-Meteo", "retrieved_at": TS, "auth": "none"}
nom = {
    "source": "OpenStreetMap Nominatim",
    "agency": "OpenStreetMap contributors",
    "retrieved_at": TS,
    "license": "ODbL",
    "auth": "none",
}
osm = {
    "source": "OpenStreetMap Overpass API",
    "agency": "OpenStreetMap contributors",
    "retrieved_at": TS,
    "auth": "none",
    "license": "ODbL",
}
hdx = {
    "source": "HDX CKAN (Indonesia group)",
    "agency": "OCHA / Humanitarian Data Exchange",
    "retrieved_at": TS,
    "license": "Per-dataset license (often CC BY); follow HDX terms",
    "auth": "none",
}

area_param = p("area_code", "string", False, "BMKG adm4 village code, for example '31.71.03.1001' for Kemayoran, Jakarta Pusat.")
limit_eq = p("limit", "integer", False, "Maximum events to return.")

categories = [
    {
        "key": "weather",
        "label": "Weather & Environment",
        "blurb": "BMKG village forecasts and Open-Meteo hourly readings. Most tools take a BMKG adm4 area_code (Jakarta Pusat Kemayoran = 31.71.03.1001).",
        "tools": [
            "id_weather_areas",
            "id_weather_overview",
            "id_weather_week_overview",
            "id_weather_warnings",
            "id_weather_24h",
            "id_weather_4day",
            "id_uv_index",
            "id_rainfall",
            "id_air_temperature",
            "id_relative_humidity",
            "id_air_quality",
        ],
    },
    {
        "key": "hazards",
        "label": "Hazards & Disasters",
        "blurb": "BMKG earthquakes and tsunami potential, Jakarta flood reports, and a volcano catalog.",
        "tools": ["id_earthquake_list", "id_tsunami_list", "id_flood_reports", "id_volcanoes"],
    },
    {
        "key": "geo",
        "label": "Geocoding & Wilayah",
        "blurb": "Nominatim address search, geocode, reverse geocode, postal codes, elevation, and Kemendagri wilayah codes.",
        "tools": [
            "id_address_search",
            "id_geocode",
            "id_reverse_geocode",
            "id_postal_code",
            "id_elevation",
            "id_provinces",
            "id_regencies",
            "id_districts",
            "id_villages",
        ],
    },
    {
        "key": "civic",
        "label": "Civic & Safety",
        "blurb": "Public holidays, cuti bersama, evacuation points, disease datasets, NIK format parse, 2024 election archive, and national heroes.",
        "tools": [
            "id_public_holidays",
            "id_cuti_bersama",
            "id_evacuation_shelters",
            "id_disease_reports",
            "id_parse_nik",
            "id_kpu_election_2024",
            "id_heroes",
        ],
    },
    {
        "key": "places",
        "label": "Tourism",
        "blurb": "Nearby tourism spots from OpenStreetMap Overpass.",
        "tools": ["id_tourism_spots"],
    },
    {
        "key": "transport",
        "label": "Commuter (KRL)",
        "blurb": "KAI Commuter station list and departures via the public Comuline API.",
        "tools": ["id_krl_stations", "id_krl_schedule"],
    },
    {
        "key": "news",
        "label": "News",
        "blurb": "Indonesian headlines from CNN, CNBC, Detik, Kompas, Tempo, and Republika.",
        "tools": ["id_news", "id_news_category", "id_news_search"],
    },
    {
        "key": "health",
        "label": "Health",
        "blurb": "Nearby hospitals and clinics from OpenStreetMap (not an official Kemenkes directory).",
        "tools": ["id_faskes"],
    },
    {
        "key": "finance",
        "label": "Finance",
        "blurb": "Bank Indonesia FX, gold prices, bank directory, OJK investment lists, and Indodax tickers.",
        "tools": ["id_bi_finance", "id_gold_price", "id_banks", "id_ojk_invest", "id_indodax_ticker"],
    },
    {
        "key": "culture",
        "label": "Language & Faith",
        "blurb": "KBBI dictionary, prayer times, Quran, hadith, daily doa, and Asmaul Husna.",
        "tools": [
            "id_kbbi",
            "id_prayer_cities",
            "id_prayer_schedule",
            "id_quran_list",
            "id_quran_surah",
            "id_hadith",
            "id_doa",
            "id_asmaul_husna",
        ],
    },
    {
        "key": "catalog",
        "label": "Open Data Catalog",
        "blurb": "Search and query HDX Indonesia CKAN open datasets.",
        "tools": ["id_datasets_search", "id_dataset_show", "id_dataset_metadata", "id_dataset_query"],
    },
]

tools = {
    "id_weather_areas": tool(
        "weather",
        "List starter BMKG adm4 village codes (for example Jakarta Pusat Kemayoran = 31.71.03.1001). No API key required.",
        [],
        {},
        {
            **bmkg,
            "api": "starter adm4 catalog",
            "total_areas": 15,
            "areas": [
                {"area_code": ADM4, "name": "Kemayoran", "city": "Jakarta Pusat", "province": "DKI Jakarta"},
                {"area_code": "51.71.04.2006", "name": "Dauh Puri Kaja", "city": "Denpasar", "province": "Bali"},
                {"area_code": "32.73.05.1001", "name": "Bandung", "city": "Bandung", "province": "Jawa Barat"},
            ],
        },
    ),
    "id_weather_overview": tool(
        "weather",
        "Get BMKG 3-hourly weather overview text for a village adm4 code.",
        [area_param],
        {"area_code": ADM4},
        {
            **bmkg,
            "api": "publik/prakiraan-cuaca",
            "area_code": ADM4,
            "data": {
                "targetArea": "Kemayoran, Jakarta Pusat",
                "reportDatetime": "2026-08-26T11:00:00+07:00",
                "text": "DKI Jakarta: partly cloudy to rain this afternoon. Temperature around 26–33°C, humidity 65–90%.",
            },
        },
    ),
    "id_weather_week_overview": tool(
        "weather",
        "Get BMKG 3-day weather overview for a village adm4 code (BMKG public forecast horizon).",
        [area_param],
        {"area_code": ADM4},
        {
            **bmkg,
            "api": "publik/prakiraan-cuaca",
            "area_code": ADM4,
            "note": "BMKG publishes a 3-day village forecast",
            "data": {"targetArea": "Kemayoran", "text": "Day 1 rain possible afternoon. Day 2 partly cloudy. Day 3 isolated showers."},
        },
    ),
    "id_weather_warnings": tool(
        "weather",
        "Extract rain/storm/fog slots from the BMKG village forecast. No API key required.",
        [area_param],
        {"area_code": ADM4},
        {
            **bmkg,
            "api": "publik/prakiraan-cuaca (severe slots)",
            "area_code": ADM4,
            "data": {
                "areaTypes": [
                    {
                        "areas": [
                            {
                                "name": "Kemayoran",
                                "code": ADM4,
                                "warnings": [{"code": "RAIN", "status": "Moderate rain 14:00–17:00"}],
                            }
                        ]
                    }
                ]
            },
        },
    ),
    "id_weather_24h": tool(
        "weather",
        "Get 24-hour forecast (temperature, humidity, wind, rain, weather code) for a BMKG adm4 area_code.",
        [area_param],
        {"area_code": ADM4},
        {
            **om,
            "api": "v1/forecast (hourly forecast 24h)",
            "area_code": ADM4,
            "location": LOC,
            "data": {
                "hourly": {
                    "time": ["2026-08-26T00:00", "2026-08-26T01:00"],
                    "temperature_2m": [26.4, 26.1],
                    "relative_humidity_2m": [82, 84],
                    "rain": [0.0, 0.2],
                    "weather_code": [2, 61],
                }
            },
        },
    ),
    "id_weather_4day": tool(
        "weather",
        "Get 4-day forecast (conditions, temperature range, precipitation sum) for a BMKG adm4 area_code.",
        [area_param],
        {"area_code": ADM4},
        {
            **om,
            "api": "v1/forecast (daily forecast 4d)",
            "area_code": ADM4,
            "location": LOC,
            "data": {
                "daily": {
                    "time": ["2026-08-26", "2026-08-27", "2026-08-28", "2026-08-29"],
                    "weather_code": [61, 2, 3, 80],
                    "temperature_2m_min": [24.1, 24.0, 24.3, 24.2],
                    "temperature_2m_max": [32.8, 33.1, 32.4, 31.9],
                    "precipitation_sum": [4.2, 0.4, 1.1, 8.0],
                }
            },
        },
    ),
    "id_uv_index": tool(
        "weather",
        "Get hourly UV index readings for a BMKG adm4 area_code (no API key required).",
        [area_param],
        {"area_code": ADM4},
        {**om, "api": "v1/forecast (hourly uv index 24h)", "area_code": ADM4, "location": LOC, "data": {"hourly": {"time": ["2026-08-26T12:00"], "uv_index": [9.4]}}},
    ),
    "id_rainfall": tool(
        "weather",
        "Get hourly rainfall readings for a BMKG adm4 area_code (no API key required).",
        [area_param],
        {"area_code": ADM4},
        {**om, "api": "v1/forecast (hourly rain 24h)", "area_code": ADM4, "location": LOC, "data": {"hourly": {"time": ["2026-08-26T14:00"], "rain": [1.8]}}},
    ),
    "id_air_temperature": tool(
        "weather",
        "Get hourly air temperature readings for a BMKG adm4 area_code (no API key required).",
        [area_param],
        {"area_code": ADM4},
        {**om, "api": "v1/forecast (hourly temperature 24h)", "area_code": ADM4, "location": LOC, "data": {"hourly": {"time": ["2026-08-26T12:00"], "temperature_2m": [32.1]}}},
    ),
    "id_relative_humidity": tool(
        "weather",
        "Get hourly relative humidity readings for a BMKG adm4 area_code (no API key required).",
        [area_param],
        {"area_code": ADM4},
        {**om, "api": "v1/forecast (hourly humidity 24h)", "area_code": ADM4, "location": LOC, "data": {"hourly": {"time": ["2026-08-26T12:00"], "relative_humidity_2m": [68]}}},
    ),
    "id_air_quality": tool(
        "weather",
        "Get hourly air quality (PM2.5, PM10, NO2, O3, SO2, CO, European AQI) for a BMKG adm4 area_code. No API key required.",
        [area_param],
        {"area_code": ADM4},
        {
            **omaq,
            "api": "v1/air-quality",
            "area_code": ADM4,
            "location": LOC,
            "data": {"hourly": {"time": ["2026-08-26T12:00"], "european_aqi": [54], "pm2_5": [22.1], "pm10": [38.0], "ozone": [41]}},
        },
    ),
    "id_earthquake_list": tool(
        "hazards",
        "List recent BMKG earthquakes (latest, M 5.0+, felt). No API key required.",
        [limit_eq],
        {"limit": 5},
        {
            **bmkg,
            "api": "DataMKG/TEWS autogempa + gempaterkini + gempadirasakan",
            "total": 16,
            "shown": 2,
            "events": [
                {"magnitude": 5.2, "hypocenter": "84 km SW of Bengkulu", "issued_at": "2026-08-25T21:14:00+07:00", "event_id": "20260825211400"},
                {"magnitude": 4.1, "hypocenter": "18 km N of Sukabumi", "issued_at": "2026-08-25T08:02:00+07:00"},
            ],
        },
    ),
    "id_tsunami_list": tool(
        "hazards",
        "List recent BMKG earthquake events with tsunami potential. No API key required.",
        [limit_eq],
        {"limit": 5},
        {**bmkg, "api": "DataMKG/TEWS (Potensi tsunami)", "total": 0, "shown": 0, "events": []},
    ),
    "id_flood_reports": tool(
        "hazards",
        "Get recent Jakarta flood / inundation reports from PetaBencana.id. No API key required.",
        [p("limit", "integer", False, "Maximum reports to return.")],
        {"limit": 10},
        {
            "source": "PetaBencana.id",
            "agency": "PetaBencana / Jakarta flood reports",
            "retrieved_at": TS,
            "auth": "none",
            "api": "reports?admin=ID-JK",
            "admin": "ID-JK",
            "total": 2,
            "shown": 2,
            "reports": [
                {"title": "Flood report", "area": "Kemayoran", "status": "confirmed", "latitude": -6.16, "longitude": 106.85},
                {"title": "Inundation", "area": "Cempaka Putih", "status": "confirmed", "latitude": -6.17, "longitude": 106.87},
            ],
        },
    ),
    "id_volcanoes": tool(
        "hazards",
        "Search Indonesian volcanoes by name, type, or height. MAGMA official REST is not public; this uses a static catalog. No API key required.",
        [
            p("name", "string", False, "Optional volcano name, for example 'merapi'."),
            p("type", "string", False, "Optional type, for example 'stratovulkan' or 'kaldera'."),
            p("min_height", "integer", False, "Optional minimum height in meters."),
            p("max_height", "integer", False, "Optional maximum height in meters."),
            p("limit", "integer", False, "Maximum volcanoes to return."),
        ],
        {"name": "merapi", "limit": 5},
        {
            "source": "Indonesia Public Static API",
            "agency": "yogski / Wikipedia volcano catalog",
            "retrieved_at": TS,
            "auth": "none",
            "api": "api/volcanoes",
            "total": 1,
            "volcanoes": [{"name": "Merapi", "type": "Stratovulkan", "height_m": 2910, "province": "Jawa Tengah / DIY"}],
        },
    ),
    "id_address_search": tool(
        "geo",
        "Search Indonesian addresses, place names, and landmarks using OpenStreetMap Nominatim. No API key required.",
        [
            p("query", "string", True, "Indonesian address or place name, for example 'Monas' or 'Jl. Thamrin Jakarta'."),
            p("limit", "integer", False, "Maximum results to return."),
        ],
        {"query": "Monas", "limit": 5},
        {
            **nom,
            "api": "search",
            "query": "Monas",
            "found": 1,
            "shown": 1,
            "results": [{"title": "Monumen Nasional", "latitude": JKT["latitude"], "longitude": JKT["longitude"], "address_code": "ID"}],
        },
    ),
    "id_geocode": tool(
        "geo",
        "Convert an Indonesian address or place name to latitude/longitude using Nominatim.",
        [
            p("query", "string", True, "Indonesian address or place name to geocode."),
            p("limit", "integer", False, "Maximum coordinate matches to return."),
        ],
        {"query": "Monas Jakarta", "limit": 3},
        {
            **nom,
            "api": "search",
            "query": "Monas Jakarta",
            "found": 1,
            "shown": 1,
            "results": [{"title": "Monumen Nasional", "latitude": JKT["latitude"], "longitude": JKT["longitude"]}],
        },
    ),
    "id_reverse_geocode": tool(
        "geo",
        "Convert latitude/longitude to an Indonesian address using Nominatim. No API key required.",
        [
            p("latitude", "number", True, "Latitude, for example -6.175392 for Monas, Jakarta."),
            p("longitude", "number", True, "Longitude, for example 106.827153 for Monas, Jakarta."),
        ],
        JKT,
        {
            **nom,
            "api": "reverse",
            **JKT,
            "result": {"found": True, "address": "Monumen Nasional, Gambir, Jakarta Pusat", "latitude": JKT["latitude"], "longitude": JKT["longitude"]},
        },
    ),
    "id_postal_code": tool(
        "geo",
        "Convert a 5-digit Indonesian postal code to province/city/district/village via CariKodePos. No API key required.",
        [p("zipcode", "string", True, "Indonesian postal code, for example '10110'.")],
        {"zipcode": "10110"},
        {
            "source": "CariKodePos",
            "agency": "CariKodePos.ID",
            "retrieved_at": TS,
            "auth": "none",
            "api": "api/postal-codes",
            "zipcode": "10110",
            "found": 1,
            "addresses": [{"province": "DKI Jakarta", "city": "Jakarta Pusat", "district": "Gambir", "village": "Gambir", "zipcode": "10110"}],
        },
    ),
    "id_elevation": tool(
        "geo",
        "Get elevation (meters) for a latitude/longitude using Open-Meteo DEM. No API key required.",
        [
            p("latitude", "number", True, "Latitude, for example -6.175392."),
            p("longitude", "number", True, "Longitude, for example 106.827153."),
        ],
        JKT,
        {
            "source": "Open-Meteo Elevation",
            "agency": "Open-Meteo",
            "retrieved_at": TS,
            "auth": "none",
            "api": "v1/elevation",
            "result": {"elevation_m": 8, "latitude": JKT["latitude"], "longitude": JKT["longitude"], "data_source": "Open-Meteo DEM"},
        },
    ),
    "id_provinces": tool(
        "geo",
        "List all Indonesian provinces with Kemendagri codes. No API key required.",
        [],
        {},
        {
            "source": "API Wilayah Indonesia (EMSIFA)",
            "agency": "Kemendagri codes via EMSIFA static JSON",
            "retrieved_at": TS,
            "auth": "none",
            "api": "provinces.json",
            "total": 38,
            "provinces": [{"id": "31", "name": "DKI JAKARTA"}, {"id": "32", "name": "JAWA BARAT"}, {"id": "51", "name": "BALI"}],
        },
    ),
    "id_regencies": tool(
        "geo",
        "List kabupaten/kota for a province Kemendagri code (for example '31' = DKI Jakarta). No API key required.",
        [p("province_id", "string", False, "2-digit province code, for example '31' for DKI Jakarta.")],
        {"province_id": "31"},
        {
            "source": "API Wilayah Indonesia (EMSIFA)",
            "agency": "Kemendagri codes via EMSIFA static JSON",
            "retrieved_at": TS,
            "auth": "none",
            "api": "regencies/{province_id}.json",
            "province_id": "31",
            "total": 6,
            "regencies": [{"id": "3173", "name": "KOTA JAKARTA PUSAT"}, {"id": "3171", "name": "KOTA JAKARTA SELATAN"}],
        },
    ),
    "id_districts": tool(
        "geo",
        "List kecamatan for a kabupaten/kota code (for example '3173' = Jakarta Pusat). No API key required.",
        [p("regency_id", "string", False, "4-digit regency/city code, for example '3173' for Kota Jakarta Pusat.")],
        {"regency_id": "3173"},
        {
            "source": "API Wilayah Indonesia (EMSIFA)",
            "agency": "Kemendagri codes via EMSIFA static JSON",
            "retrieved_at": TS,
            "auth": "none",
            "api": "districts/{regency_id}.json",
            "regency_id": "3173",
            "total": 8,
            "districts": [{"id": "3173060", "name": "KEMAYORAN"}, {"id": "3173080", "name": "GAMBIR"}],
        },
    ),
    "id_villages": tool(
        "geo",
        "List desa/kelurahan for a kecamatan code (for example '3173060' = Kemayoran). No API key required.",
        [p("district_id", "string", False, "District code, for example '3173060' for Kemayoran, Jakarta Pusat.")],
        {"district_id": "3173060"},
        {
            "source": "API Wilayah Indonesia (EMSIFA)",
            "agency": "Kemendagri codes via EMSIFA static JSON",
            "retrieved_at": TS,
            "auth": "none",
            "api": "villages/{district_id}.json",
            "district_id": "3173060",
            "total": 8,
            "villages": [{"id": "3173060001", "name": "KEMAYORAN"}, {"id": "3173060002", "name": "GUNUNG SAHARI SELATAN"}],
        },
    ),
    "id_public_holidays": tool(
        "civic",
        "List Indonesian public holidays for a calendar year via Nager.Date. No API key required.",
        [p("year", "integer", False, "Calendar year, for example 2026.")],
        {"year": 2026},
        {
            "source": "Nager.Date",
            "agency": "Nager.Date",
            "retrieved_at": TS,
            "auth": "none",
            "api": "PublicHolidays/{year}/ID",
            "year": 2026,
            "total": 17,
            "holidays": [
                {"date": "2026-01-01", "local_name": "Tahun Baru Masehi", "name": "New Year's Day"},
                {"date": "2026-08-17", "local_name": "Hari Kemerdekaan", "name": "Independence Day"},
            ],
        },
    ),
    "id_cuti_bersama": tool(
        "civic",
        "List Indonesian national holidays and joint leave (cuti bersama) for a year. Complements id_public_holidays. No API key required.",
        [
            p("year", "integer", False, "Calendar year, for example 2026."),
            p("month", "integer", False, "Optional month number 1-12."),
            p("cuti_only", "boolean", False, "If true, return cuti bersama rows only."),
        ],
        {"year": 2026},
        {
            "source": "API Hari Libur Indonesia",
            "agency": "National holidays and cuti bersama",
            "retrieved_at": TS,
            "auth": "none",
            "api": "api?year={year}",
            "year": 2026,
            "total": 2,
            "holidays": [
                {"date": "2026-08-17", "name": "Hari Kemerdekaan", "cuti": False},
                {"date": "2026-12-24", "name": "Cuti bersama Natal", "cuti": True},
            ],
        },
    ),
    "id_evacuation_shelters": tool(
        "civic",
        "List nearby evacuation / emergency assembly points from OpenStreetMap. Provide lat/lon. No API key required.",
        [
            p("latitude", "number", True, "Latitude, for example -6.175392 for Monas, Jakarta."),
            p("longitude", "number", True, "Longitude, for example 106.827153 for Monas, Jakarta."),
            p("type", "string", False, "'evacuation' = shelters / assembly points, 'emergency' = emergency assembly points only."),
            p("radius_m", "integer", False, "Search radius in meters."),
            p("limit", "integer", False, "Maximum shelters to return."),
        ],
        {**JKT, "type": "evacuation", "radius_m": 3000, "limit": 8},
        {
            **osm,
            "api": "overpass-api.de/api/interpreter",
            **JKT,
            "type": "evacuation",
            "radius_m": 3000,
            "total": 2,
            "shown": 2,
            "shelters": [
                {"name": "Lapangan Banteng", "address": "Jakarta Pusat", "latitude": -6.1705, "longitude": 106.8339},
                {"name": "Monas grounds", "address": "Gambir", "latitude": JKT["latitude"], "longitude": JKT["longitude"]},
            ],
        },
    ),
    "id_disease_reports": tool(
        "civic",
        "Search HDX Indonesia datasets for infectious-disease related open data (dengue, malaria, etc.). No API key required.",
        [
            p("query", "string", False, "Search keyword, for example 'dengue', 'malaria', or 'penyakit'."),
            p("rows", "integer", False, "Number of datasets to return."),
        ],
        {"query": "dengue", "rows": 5},
        {**hdx, "api": "package_search", "query": "dengue", "total": 4, "shown": 1, "datasets": [{"title": "Indonesia dengue-related dataset", "name": "idn-dengue", "organization": "HDX"}]},
    ),
    "id_parse_nik": tool(
        "civic",
        "Locally decode a 16-digit NIK (province/regency/district codes, date of birth, gender). Format parser only — does not validate identity against Dukcapil. No HTTP and no API key.",
        [p("nik", "string", True, "16-digit NIK, for example '3173061501850001'.")],
        {"nik": "3173061501850001"},
        {
            "source": "Local NIK format parser",
            "agency": "Kemendagri digit layout (not Dukcapil)",
            "retrieved_at": TS,
            "auth": "none",
            "dukcapil_validated": False,
            "nik": "3173061501850001",
            "province_code": "31",
            "regency_code": "3173",
            "district_code": "317306",
            "gender": "male",
            "date_of_birth": "1985-01-15",
        },
    ),
    "id_kpu_election_2024": tool(
        "civic",
        "Historical 2024 presidential (PPWP) archive from KPU SIREKAP public JSON. Not a live election tool. No API key required.",
        [
            p("view", "string", False, "candidates = paslon list, wilayah = province/regency tree, results = vote tallies."),
            p("wilayah_codes", "string", False, "Optional nested KPU codes, for example '31' (DKI Jakarta) or '31/3173'."),
        ],
        {"view": "candidates"},
        {
            "source": "KPU SIREKAP public storage",
            "agency": "Komisi Pemilihan Umum (2024 archive)",
            "retrieved_at": TS,
            "auth": "none",
            "api": "ppwp candidates",
            "view": "candidates",
            "candidates": [{"nomor": 1, "nama": "Paslon 1"}, {"nomor": 2, "nama": "Paslon 2"}],
        },
    ),
    "id_heroes": tool(
        "civic",
        "Search Indonesian national heroes (pahlawan nasional). No API key required.",
        [
            p("name", "string", False, "Optional name filter, for example 'soekarno'."),
            p("limit", "integer", False, "Maximum heroes to return."),
        ],
        {"name": "soekarno", "limit": 5},
        {
            "source": "Indonesia Public Static API",
            "agency": "yogski national heroes catalog",
            "retrieved_at": TS,
            "auth": "none",
            "api": "api/heroes",
            "total": 1,
            "heroes": [{"name": "Soekarno", "birth": "1901", "death": "1970"}],
        },
    ),
    "id_tourism_spots": tool(
        "places",
        "Search nearby tourism spots (attractions, museums, viewpoints, etc.) via OpenStreetMap Overpass. No API key required.",
        [
            p("latitude", "number", True, "Latitude, for example -6.175392."),
            p("longitude", "number", True, "Longitude, for example 106.827153."),
            p("radius_m", "integer", False, "Search radius in meters."),
            p("limit", "integer", False, "Maximum spots to return."),
        ],
        {**JKT, "radius_m": 1500, "limit": 8},
        {
            **osm,
            "api": "overpass-api.de/api/interpreter",
            **JKT,
            "radius_m": 1500,
            "found": 2,
            "shown": 2,
            "spots": [
                {"name": "Monumen Nasional", "tourism": "attraction", **JKT},
                {"name": "Museum Nasional", "tourism": "museum", "latitude": -6.1764, "longitude": 106.8216},
            ],
        },
    ),
    "id_krl_stations": tool(
        "transport",
        "List KAI Commuter (KRL) stations for Jabodetabek and Yogyakarta-Solo via the public Comuline API. No API key required.",
        [
            p("query", "string", False, "Optional station id or name filter, for example 'MRI' or 'manggarai'."),
            p("limit", "integer", False, "Maximum stations to return."),
        ],
        {"query": "manggarai", "limit": 10},
        {
            "source": "Comuline API",
            "agency": "Community KAI Commuter mirror (Jabodetabek / Yogyakarta-Solo)",
            "retrieved_at": TS,
            "auth": "none",
            "api": "v1/station",
            "total": 1,
            "stations": [{"id": "MRI", "name": "Manggarai"}],
        },
    ),
    "id_krl_schedule": tool(
        "transport",
        "Get KAI Commuter (KRL) departures for a station code (MRI, GMR, AC, …) via Comuline. No API key required.",
        [
            p("station_id", "string", False, "Comuline station id, for example 'MRI' (Manggarai) or 'GMR' (Gambir)."),
            p("line", "string", False, "Optional line name filter, for example 'BOGOR' or 'CIKARANG'."),
            p("limit", "integer", False, "Maximum schedule rows to return."),
        ],
        {"station_id": "MRI", "limit": 10},
        {
            "source": "Comuline API",
            "agency": "Community KAI Commuter mirror (Jabodetabek / Yogyakarta-Solo)",
            "retrieved_at": TS,
            "auth": "none",
            "api": "v1/schedule/MRI",
            "station_id": "MRI",
            "total": 2,
            "shown": 2,
            "schedule": [
                {"dest": "Bogor", "time": "12:15", "line": "BOGOR"},
                {"dest": "Cikarang", "time": "12:22", "line": "CIKARANG"},
            ],
        },
    ),
    "id_news": tool(
        "news",
        "Get latest Indonesian news headlines from CNN, CNBC, Detik, Kompas, Tempo, or Republika. No API key required.",
        [
            p("source", "string", False, "News source slug: cnn-news, cnbc-news, detik-news, kompas-news, tempo-news, republika-news."),
            p("limit", "integer", False, "Maximum headlines to return."),
        ],
        {"source": "cnn-news", "limit": 5},
        {
            "source": "Berita Indo API",
            "agency": "Indonesian news RSS → JSON",
            "retrieved_at": TS,
            "auth": "none",
            "api": "v1/cnn-news",
            "total": 20,
            "shown": 1,
            "headlines": [{"title": "Sample CNN Indonesia headline", "link": "https://www.cnnindonesia.com/", "isoDate": TS}],
        },
    ),
    "id_news_category": tool(
        "news",
        "Get Indonesian news headlines for a source category (for example CNN nasional). No API key required.",
        [
            p("source", "string", False, "News source slug."),
            p("category", "string", False, "Category slug. CNN: nasional, internasional, ekonomi, olahraga, teknologi, hiburan, gaya-hidup."),
            p("limit", "integer", False, "Maximum headlines to return."),
        ],
        {"source": "cnn-news", "category": "nasional", "limit": 5},
        {
            "source": "Berita Indo API",
            "agency": "Indonesian news RSS → JSON",
            "retrieved_at": TS,
            "auth": "none",
            "api": "v1/cnn-news/nasional",
            "total": 10,
            "shown": 1,
            "headlines": [{"title": "Nasional headline", "isoDate": TS}],
        },
    ),
    "id_news_search": tool(
        "news",
        "Search Indonesian headlines by title/snippet on CNN, CNBC, Detik, Kompas, Tempo, or Republika. No API key required.",
        [
            p("source", "string", False, "News source slug."),
            p("query", "string", True, "Search text, for example 'jakarta' or 'gempa'."),
            p("category", "string", False, "Optional category slug for the chosen source."),
            p("limit", "integer", False, "Maximum headlines to return."),
        ],
        {"source": "cnn-news", "query": "jakarta", "limit": 5},
        {
            "source": "Berita Indo API",
            "agency": "Indonesian news RSS → JSON",
            "retrieved_at": TS,
            "auth": "none",
            "api": "v1/cnn-news?search=",
            "query": "jakarta",
            "total": 3,
            "shown": 1,
            "headlines": [{"title": "Jakarta traffic update", "isoDate": TS}],
        },
    ),
    "id_faskes": tool(
        "health",
        "Search nearby hospitals and clinics via OpenStreetMap Overpass. OSM community data — not an official Kemenkes directory. No API key required.",
        [
            p("latitude", "number", True, "Latitude, for example -6.175392."),
            p("longitude", "number", True, "Longitude, for example 106.827153."),
            p("radius_m", "integer", False, "Search radius in meters."),
            p("limit", "integer", False, "Maximum facilities to return."),
        ],
        {**JKT, "radius_m": 2000, "limit": 8},
        {
            **osm,
            "agency": "OpenStreetMap contributors (hospitals/clinics — not an official Kemenkes directory)",
            "api": "overpass-api.de/api/interpreter",
            **JKT,
            "found": 2,
            "shown": 2,
            "facilities": [
                {"name": "RSUPN Cipto Mangunkusumo", "amenity": "hospital", "latitude": -6.1865, "longitude": 106.8468},
                {"name": "Clinic sample", "amenity": "clinic", "latitude": -6.18, "longitude": 106.83},
            ],
        },
    ),
    "id_bi_finance": tool(
        "finance",
        "Get Bank Indonesia USD/IDR (and other pairs) via Frankfurter. Default returns the latest USD/IDR rate. No API key required.",
        [
            p("from", "string", False, "Base currency code, for example 'USD'."),
            p("to", "string", False, "Quote currency code, for example 'IDR'."),
            p("start_date", "string", False, "Optional start date as YYYY-MM-DD."),
            p("end_date", "string", False, "Optional end date as YYYY-MM-DD."),
            p("include_metadata", "boolean", False, "If true, also return provider metadata."),
        ],
        {"from": "USD", "to": "IDR"},
        {
            "source": "Frankfurter (Bank Indonesia provider)",
            "agency": "Bank Indonesia",
            "retrieved_at": TS,
            "auth": "none",
            "api": "v2/rate/{from}/{to}?providers=BI",
            "from": "USD",
            "to": "IDR",
            "data": {"amount": 1, "base": "USD", "date": "2026-08-25", "rates": {"IDR": 16250.0}},
            "metadata": None,
        },
    ),
    "id_gold_price": tool(
        "finance",
        "Get current Antam / logam mulia gold sell and buyback prices in IDR. No API key required.",
        [
            p("source", "string", False, "Gold price source slug: anekalogam, hargaemas-org, lakuemas, pegadaian, indogold."),
            p("limit", "integer", False, "Maximum price rows to return."),
        ],
        {"source": "anekalogam", "limit": 10},
        {
            "source": "Logam Mulia API",
            "agency": "Community gold prices (Aneka Logam / Antam listings)",
            "retrieved_at": TS,
            "auth": "none",
            "api": "api/prices/anekalogam",
            "total": 1,
            "prices": [{"material": "Antam 1gr", "sell": 1450000, "buyback": 1380000}],
        },
    ),
    "id_banks": tool(
        "finance",
        "Search Indonesian banks by name (BRI, Mandiri, BCA, etc.) with OJK type and contact details. No API key required.",
        [
            p("keyword", "string", False, "Bank name keyword, for example 'bri', 'mandiri', or 'bca'."),
            p("limit", "integer", False, "Maximum banks to return."),
        ],
        {"keyword": "bri", "limit": 5},
        {
            "source": "Seme Bank ID API",
            "agency": "OJK bank directory via bank.thecloudalert.com",
            "retrieved_at": TS,
            "auth": "none",
            "api": "api/get/?keyword={keyword}",
            "total": 1,
            "banks": [{"name": "Bank Rakyat Indonesia", "code": "002"}],
        },
    ),
    "id_ojk_invest": tool(
        "finance",
        "Search unofficial OJK lists of illegal investments, legal mutual-fund apps, or investment products. No API key required.",
        [
            p("category", "string", False, "'illegal' = flagged entities, 'apps' = legal apps, 'products' = products."),
            p("query", "string", False, "Optional name filter, for example 'binary' or 'bibit'."),
            p("limit", "integer", False, "Maximum rows to return."),
        ],
        {"category": "illegal", "query": "binary", "limit": 5},
        {
            "source": "OJK Invest API (unofficial)",
            "agency": "Otoritas Jasa Keuangan public investment lists",
            "retrieved_at": TS,
            "auth": "none",
            "api": "api/illegals",
            "total": 1,
            "shown": 1,
            "items": [{"name": "Sample flagged entity", "category": "illegal"}],
        },
    ),
    "id_indodax_ticker": tool(
        "finance",
        "Get a public Indodax crypto ticker (no API key). Default pair is BTC/IDR.",
        [p("pair", "string", False, "Indodax market pair, for example 'btcidr', 'ethidr', or 'usdtidr'.")],
        {"pair": "btcidr"},
        {
            "source": "Indodax Public REST",
            "agency": "Indodax",
            "retrieved_at": TS,
            "auth": "none",
            "api": "api/ticker/{pair}",
            "ticker": {"pair": "btcidr", "last": "1650000000", "high": "1680000000", "low": "1620000000"},
        },
    ),
    "id_kbbi": tool(
        "culture",
        "Look up an Indonesian word in Kamus Besar Bahasa Indonesia. No API key required.",
        [p("word", "string", True, "Indonesian word, for example 'rumah' or 'merdeka'.")],
        {"word": "merdeka"},
        {
            "source": "KBBI Open API",
            "agency": "Kamus Besar Bahasa Indonesia",
            "retrieved_at": TS,
            "auth": "none",
            "api": "kbbi?search={word}",
            "word": "merdeka",
            "found": 1,
            "results": [{"word": "merdeka", "meaning": "bebas (dari penghambaan, penjajahan, dan sebagainya)"}],
        },
    ),
    "id_prayer_cities": tool(
        "culture",
        "Search MyQuran/Kemenag city ids for Islamic prayer schedules. No API key required.",
        [p("query", "string", False, "City name, for example 'jakarta', 'bandung', or 'surabaya'.")],
        {"query": "jakarta"},
        {
            "source": "MyQuran API v2",
            "agency": "Kemenag prayer times via MyQuran",
            "retrieved_at": TS,
            "auth": "none",
            "api": "sholat/kota/cari/{query}",
            "query": "jakarta",
            "found": 1,
            "cities": [{"id": "1301", "name": "KOTA JAKARTA"}],
        },
    ),
    "id_prayer_schedule": tool(
        "culture",
        "Get monthly Islamic prayer times (Fajr, Dhuhr, Asr, Maghrib, Isha) for a MyQuran city id. No API key required.",
        [
            p("city_id", "string", False, "MyQuran city id, for example '1301' for Kota Jakarta."),
            p("year", "integer", False, "Calendar year."),
            p("month", "integer", False, "Month number 1-12."),
        ],
        {"city_id": "1301", "year": 2026, "month": 8},
        {
            "source": "MyQuran API v2",
            "agency": "Kemenag prayer times via MyQuran",
            "retrieved_at": TS,
            "auth": "none",
            "api": "sholat/jadwal/{city_id}/{year}/{month}",
            "city_id": "1301",
            "year": 2026,
            "month": 8,
            "data": {"lokasi": "KOTA JAKARTA", "jadwal": [{"tanggal": "2026-08-26", "subuh": "04:42", "dzuhur": "11:56", "ashar": "15:17", "maghrib": "17:56", "isya": "19:05"}]},
        },
    ),
    "id_quran_list": tool(
        "culture",
        "List all 114 Quran surahs with Latin names and ayah counts via EQuran.id. No API key required.",
        [],
        {},
        {
            "source": "EQuran.id API v2",
            "agency": "EQuran.id",
            "retrieved_at": TS,
            "auth": "none",
            "api": "surat",
            "total": 114,
            "surahs": [{"number": 1, "name_latin": "Al-Fatihah", "ayah_count": 7}],
        },
    ),
    "id_quran_surah": tool(
        "culture",
        "Get a Quran surah with Arabic, Latin, and Indonesian text via EQuran.id. No API key required.",
        [p("number", "integer", False, "Surah number 1-114, for example 1 = Al-Fatihah.")],
        {"number": 1},
        {
            "source": "EQuran.id API v2",
            "agency": "EQuran.id",
            "retrieved_at": TS,
            "auth": "none",
            "api": "surat/{number}",
            "number": 1,
            "surah": {"number": 1, "name_latin": "Al-Fatihah", "ayah_count": 7, "verses": [{"ayah": 1, "arab": "بِسْمِ اللَّهِ", "latin": "Bismillahirrahmanirrahim", "id": "Dengan nama Allah"}]},
        },
    ),
    "id_hadith": tool(
        "culture",
        "Get a hadith by narrator slug and number via MyQuran, or list narrators when list_narrators is true. No API key required.",
        [
            p("list_narrators", "boolean", False, "If true, return the narrator (perawi) catalog instead of a hadith."),
            p("perawi", "string", False, "Narrator slug, for example 'bukhari', 'muslim', or 'abu-dawud'."),
            p("number", "integer", False, "Hadith number within the narrator collection."),
        ],
        {"perawi": "bukhari", "number": 1},
        {
            "source": "MyQuran API v2",
            "agency": "Hadith collection via MyQuran",
            "retrieved_at": TS,
            "auth": "none",
            "api": "hadits/{perawi}/{number}",
            "hadith": {"perawi": "bukhari", "number": 1, "arab": "…", "id": "…"},
        },
    ),
    "id_doa": tool(
        "culture",
        "Search Indonesian daily doa (prayers) with Arabic, Latin, and meaning. No API key required.",
        [
            p("query", "string", False, "Optional title/meaning filter, for example 'tidur' or 'makan'."),
            p("limit", "integer", False, "Maximum doa to return."),
        ],
        {"query": "makan", "limit": 5},
        {
            "source": "Doa Harian API",
            "agency": "Community daily doa collection",
            "retrieved_at": TS,
            "auth": "none",
            "api": "/",
            "total": 1,
            "doa": [{"title": "Doa sebelum makan", "latin": "Allahumma barik lana fima razaqtana", "id": "Ya Allah, berkahilah rezeki yang Engkau berikan"}],
        },
    ),
    "id_asmaul_husna": tool(
        "culture",
        "List the 99 names of Allah (Asmaul Husna) in Arabic, Latin, and Indonesian. No API key required.",
        [p("number", "integer", False, "Optional name number 1-99. Omit to return all 99 names.")],
        {"number": 1},
        {
            "source": "MyQuran API v2",
            "agency": "Asmaul Husna via MyQuran",
            "retrieved_at": TS,
            "auth": "none",
            "api": "husna/semua",
            "total": 1,
            "names": [{"number": 1, "latin": "Ar-Rahman", "id": "Yang Maha Pengasih"}],
        },
    ),
    "id_datasets_search": tool(
        "catalog",
        "Search HDX Indonesia open datasets via CKAN package_search. No API key required.",
        [
            p("query", "string", True, "Search keyword, for example 'cuaca', 'penduduk', or 'earthquake'."),
            p("rows", "integer", False, "Number of datasets to return."),
            p("start", "integer", False, "Result offset for pagination."),
            p("fq", "string", False, "Optional CKAN filter query. Defaults to 'groups:idn'."),
        ],
        {"query": "earthquake", "rows": 5},
        {**hdx, "api": "package_search", "query": "earthquake", "total": 12, "shown": 1, "datasets": [{"title": "Indonesia earthquake-related dataset", "name": "idn-earthquake", "organization": "HDX"}]},
    ),
    "id_dataset_show": tool(
        "catalog",
        "Get full HDX dataset metadata and resources by package id or name. No API key required.",
        [p("id", "string", True, "CKAN package id or name, for example 'cod-ab-idn' or 'wfp-food-prices-for-indonesia'.")],
        {"id": "cod-ab-idn"},
        {
            **hdx,
            "api": "package_show",
            "id": "cod-ab-idn",
            "dataset": {"title": "Indonesia Administrative Boundaries", "name": "cod-ab-idn", "organization": "OCHA", "tags": ["administrative boundaries"], "resources": [{"name": "ADM1", "format": "SHP", "id": "sample-resource"}]},
        },
    ),
    "id_dataset_metadata": tool(
        "catalog",
        "Alias of id_dataset_show for Singapore-style naming. Get HDX package metadata by id/name.",
        [p("id", "string", True, "CKAN package id or name, for example 'cod-ab-idn'.")],
        {"id": "cod-ab-idn"},
        {**hdx, "api": "package_show", "id": "cod-ab-idn", "dataset": {"title": "Indonesia Administrative Boundaries", "name": "cod-ab-idn", "organization": "OCHA"}},
    ),
    "id_dataset_query": tool(
        "catalog",
        "Query tabular HDX datastore records by resource_id (CKAN datastore_search). No API key required.",
        [
            p("resource_id", "string", True, "CKAN resource id that has datastore enabled."),
            p("limit", "integer", False, "Maximum records to return."),
            p("offset", "integer", False, "Record offset for pagination."),
            p("q", "string", False, "Optional full-text query across datastore fields."),
            p("filters", "string", False, "Optional JSON filters string, for example '{\"col\":\"value\"}'."),
            p("sort", "string", False, "Optional sort expression, for example 'col asc'."),
            p("fields", "string", False, "Optional comma-separated field list to return."),
        ],
        {"resource_id": "cod-ab-idn-sample", "limit": 5},
        {**hdx, "api": "datastore_search", "resource_id": "cod-ab-idn-sample", "total": 38, "shown": 2, "records": [{"adm1_name": "DKI JAKARTA"}, {"adm1_name": "JAWA BARAT"}]},
    ),
}

# postalView in JP uses prefecture/city/town — Indonesia uses province/city/district/village.
# The visualizer will be adapted. Keep both shapes where helpful.
tools["id_postal_code"]["response"]["addresses"][0]["prefecture"] = "DKI Jakarta"
tools["id_postal_code"]["response"]["addresses"][0]["town"] = "Gambir"

named = set(tools)
declared = {n for c in categories for n in c["tools"]}
assert named == declared, f"mismatch {named ^ declared}"

out = {"categories": categories, "tools": tools}
path = os.path.join(BASE, "data.min.json")
with open(path, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
    f.write("\n")
print(f"wrote {path} ({len(tools)} tools, {len(categories)} categories)")
