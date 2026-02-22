# 🌦️ Weather Data Pipeline (End-to-End)

🚧 **Status: Work In Progress (Phase 1 completed: Bronze layer)** 🚧

This project is a full elt pipeline using a modern stack, maintaining scalability, modularization and using the best practices. From extracting weather data from multiple sources to serving it, with the complete transformation process.

The main goal of this project is not only he implementation and real use of itself, but also put the best practices in use, analysing multiple options for each part of the project and deciding and exposing the design decision made (see complete technical documentation soon). I'm using this project for both research on new technologies and usage of the ones I'm already familiar with.

## 🛠️ Tecnologies Stack

* **Language:** Python 3.12
* **Orchestration:** Prefect 3.0
* **Database:** PostgreSQL
* **Infrasructure:** Docker & Docker Compose

---

## 🏗️ Structure

This project follows a modular structure, segregating extraction logic, db connection and the structure config:

* **Dynamic environment managing** with easy-to-use comands in the Makefile. Complete customization via .env file.
* **Orchestration and failure managing** using Prefect. This is one of the most important parts of the project, since we will be working with real data gathered from different sources. One failure can't make the hole pipeline fall.
* **Multiple-layered structure** for different purpuses of the data. I choose ELT over ETL since each source gives data in their own way and keep the possibility of re-procesing data if a certain source changes it's format.

```text
weather-data-pipeline/
├── .env                 # environment config
├── Makefile             # Ready-to-use commands
├── docker-compose.yml   # Services definition and orquestation on build up
├── docs/                # Technical documentation using Mkocs
└── src/
    ├── extraction/      # Extraction logic
    └── db/              # Database connection and allowed commands
```


## 🗺️ Project Roadmap
* [x] Phase 1: Raw Ingestion (Bronze Layer)
    * Extraction from external Weather APIs.
    * Loading raw JSON data into PostgreSQL.
    * Infrastructure setup with Docker and Orchestration with Prefect.
* [ ] Phase 2: Transformation (Silver Layer)
    * Data cleaning, normalization, and tabular modeling.
* [ ] Phase 3: Quality & Observability
    * Logging API errors directly into the database.
    * Setting up alerts and notifications for pipeline failures.
* [ ] Phase 4: Consumption (Gold Layer / API)
    * Creating materialized views for business value.
    * Developing a FastAPI endpoint to serve the structured data.