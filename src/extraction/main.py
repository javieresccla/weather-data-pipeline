import src.extraction.extractors as ex
from src.extraction.base import BaseELTJob
from src.db import PostgresConnection, insert_into_bronze
from prefect import flow, task
import os

from dotenv import load_dotenv

load_dotenv()

@task(retries=3, retry_delay_seconds=10, name="Extract and save data", cache_policy=None)
def execute_extractor(extractor, conn):
    source = extractor.get_name()
    data = extractor.fetch_data()
                
    insert_into_bronze(
        conn = conn,
        target_table = "bronze.weather_raw",
        source = source,
        data = data
    )
    return True

@flow(name="Bronze_pipeline", log_prints=True)
def run_pipeline():
    ExtractorClases = BaseELTJob.__subclasses__()
    city = "Cordoba,ES"

    with PostgresConnection() as conn:
        for ExtractorClass in ExtractorClases:
            extractor = ExtractorClass(city)

            try:
               execute_extractor(extractor, conn)
            except Exception as e:
                print(f"Error: {e}") 

if __name__ == "__main__":
    run_pipeline.serve(
        name=f"extraction-{os.getenv('ENVIRONMENT')}",
        cron=os.getenv('CRON')
    )