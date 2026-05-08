ALTER TABLE bronze.cities ADD COLUMN IF NOT EXISTS country VARCHAR(10);

-- Unique constraint for idempotent seeding (config defaults won't duplicate)
ALTER TABLE bronze.cities ADD CONSTRAINT cities_name_country_unique UNIQUE (name, country);
