/* (Beta) Export of data model GovSteam2 of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE GovSteam2_type AS ENUM ('GovSteam2');
CREATE TABLE GovSteam2 (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, dbf NUMERIC, description TEXT, id TEXT PRIMARY KEY, k NUMERIC, location JSON, mnef NUMERIC, mxef NUMERIC, name TEXT, owner JSON, pmax NUMERIC, pmin NUMERIC, seeAlso JSON, source TEXT, t1 NUMERIC, t2 NUMERIC, type GovSteam2_type);