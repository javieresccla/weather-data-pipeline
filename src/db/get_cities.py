"""Retrieve cities from bronze.cities for extraction."""
from __future__ import annotations


def get_cities(conn) -> list[tuple[str, str]]:
    """
    Return list of (name, country) from bronze.cities.
    country may be None for legacy rows without migration 3.
    """
    query = """
        SELECT name, country FROM bronze.cities
        ORDER BY id;
    """
    with conn.cursor() as cur:
        cur.execute(query)
        rows = cur.fetchall()
    return [(row[0], row[1] or "") for row in rows]
