import json
from datetime import datetime, timezone

def insert_into_bronze(conn, target_table, source, data):
    query = f"""
        INSERT INTO {target_table} (source, data, extraction_date)
        VALUES (%s, %s, %s);
    """

    json_string = json.dumps(data, ensure_ascii=False)

    extraction_date = datetime.now(timezone.utc)

    with conn.cursor() as cur:
        cur.execute(query, (source, json_string, extraction_date))

