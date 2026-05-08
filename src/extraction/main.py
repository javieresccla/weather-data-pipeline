from src.extraction.base import BaseELTJob
from src.db import PostgresConnection, insert_into_bronze, get_cities
from prefect import flow, task
import os

from dotenv import load_dotenv

load_dotenv()


@task(retries=3, retry_delay_seconds=10, name="Extract and save data", cache_policy=None)
def execute_extractor(extractor, conn):
    source = extractor.get_name()
    data = extractor.fetch_data()
    # Add city metadata for traceability in Silver layer
    data["_city"] = extractor.city

    insert_into_bronze(
        conn=conn,
        target_table="bronze.weather_raw",
        source=source,
        data=data,
    )
    return True


@flow(name="Bronze_pipeline", log_prints=True)
def run_pipeline():
    extractor_classes = BaseELTJob.__subclasses__()

    with PostgresConnection() as conn:
        cities = get_cities(conn)
        if not cities:
            print("No cities in bronze.cities; run seed first.")
            return

        for name, country in cities:
            city = f"{name},{country}" if country else name
            for ExtractorClass in extractor_classes:
                extractor = ExtractorClass(city)
                try:
                    execute_extractor(extractor, conn)
                except Exception as e:
                    print(f"Error [{city}][{ExtractorClass.__name__}]: {e}")


if __name__ == "__main__":
    run_pipeline.serve(
        name=f"extraction-{os.getenv('ENVIRONMENT')}",
        cron=os.getenv("CRON"),
    )