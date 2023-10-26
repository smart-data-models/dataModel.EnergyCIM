/* (Beta) Export of data model EnergyConsumer of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE EnergyConsumer_type AS ENUM ('EnergyConsumer');
CREATE TABLE EnergyConsumer (LoadDynamics NUMERIC, LoadResponse NUMERIC, address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, id TEXT PRIMARY KEY, location JSON, name TEXT, owner JSON, p NUMERIC, pfixed NUMERIC, pfixedPct NUMERIC, q NUMERIC, qfixed NUMERIC, qfixedPct NUMERIC, seeAlso JSON, source TEXT, type EnergyConsumer_type);