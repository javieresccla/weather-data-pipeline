"""Seed bronze.cities from config/cities.yaml. Idempotent: skips existing (name, country)."""
from pathlib import Path

import yaml


def _get_config_path() -> Path:
    """Resolve config/cities.yaml relative to project root."""
    base = Path(__file__).resolve().parent.parent.parent
    return base / "config" / "cities.yaml"


def load_cities_from_config() -> list[tuple[str, str]]:
    """Parse config/cities.yaml and return list of (name, country) tuples."""
    path = _get_config_path()
    if not path.exists():
        return []
    with open(path) as f:
        data = yaml.safe_load(f)
    cities = data.get("cities") or []
    result = []
    for item in cities:
        if isinstance(item, str) and "," in item:
            parts = item.split(",", 1)
            result.append((parts[0].strip(), parts[1].strip()))
        elif isinstance(item, dict):
            result.append((item.get("name", ""), item.get("country", "")))
        else:
            continue
    return result


def seed_from_config(conn) -> int:
    """Insert cities from config into bronze.cities. Uses ON CONFLICT DO NOTHING. Returns count inserted."""
    cities = load_cities_from_config()
    if not cities:
        return 0
    query = """
        INSERT INTO bronze.cities (name, country)
        VALUES (%s, %s)
        ON CONFLICT (name, country) DO NOTHING;
    """
    with conn.cursor() as cur:
        cur.executemany(query, cities)
    return len(cities)
