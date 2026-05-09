# 🌦️ Weather Data Pipeline (End-to-End)

🚧 **Status: Work In Progress (Phase 1 completed: Bronze layer)** 🚧

This project is a full elt pipeline using a modern stack, maintaining scalability, modularization and using the best practices. From extracting weather data from multiple sources to serving it, with the complete transformation process.

The main goal of this project is not only he implementation and real use of itself, but also put the best practices in use, analysing multiple options for each part of the project and deciding and exposing the design decision made (see complete technical documentation soon). I'm using this project for both research on new technologies and usage of the ones I'm already familiar with.

## 🛠️ Tecnologies Stack

* **Language:** Python 3.12
* **Orchestration:** Prefect 3.0
* **Database:** PostgreSQL
* **Infrastructure:** Docker

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

## 🚀 How to Run (Quickstart)

This project includes a `Makefile` to simplify Docker commands and environment management, ensuring a smooth setup process.

1. **Setup Environment Variables:**
   Copy `.env.template` into your directory with name `.env` and fulfill it with the info requested. 

2. **Run in Development Mode:**
   Spins up the containers and runs the pipeline using local testing configurations (e.g., executing every minute).
   ```bash
   make dev
   ```
3. **Run in Production Mode:**
   Runs final production config, such as executing every day at 7AM.
   ```bash
   make prod
   ```
4. **Gently stop the pipeline:**
   Switching off the containers ensuring data reliability.
   ```bash
   make down
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

## 🧠 What I Learned so far
* Good practices in project organization. Using make to set up a quick start command.
* Docker: This is the first time I build a hole proyect in docker from scratch. Even though I knew the basics, building the Dockerfile and more precisely the docker-compose made me fully comprehend the architecture.
* Postgre as db engine: In my current job I always used MariaDB. I made my research on postgre, analysing it's pros and cons.
* Data pipelines design basics: Even though there's many concepts to go deep in, this proyect allowed me to understand the importance of researching a field before diving into the desing. As an example, I was aware of ETL design, but discovered that for my use case ELT was the appropiate choice.

## 🧐 Decisions Breakdown
* ELT over ETL: In order to open the door for future re-processing of the data extracted from the API's, I think ELT is the correct choice. On top of that, this design pattern is the most accepted as of today. The reason, among others, is the allowance of a post-failure layer. The costs of storing the raw data in this proyect is not important enough (raw json's can be cheaply stored nowadays) to disregard ELT.
* Building from ingestion to comsumption: Since this proyect is for personal development, I have no requirements on the final business value yet. This way, and maintaining clean code patterns (such us microservices and singleton), I will discover the value I can extract from the data in along the way.
