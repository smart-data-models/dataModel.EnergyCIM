/* (Beta) Export of data model GovHydro2 of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE GovHydro2_type AS ENUM ('GovHydro2');
CREATE TABLE GovHydro2 (address JSON, alternateName TEXT, areaServed TEXT, aturb NUMERIC, bturb NUMERIC, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, db1 NUMERIC, db2 NUMERIC, description TEXT, eps NUMERIC, gv1 NUMERIC, gv2 NUMERIC, gv3 NUMERIC, gv4 NUMERIC, gv5 NUMERIC, gv6 NUMERIC, id TEXT PRIMARY KEY, kturb NUMERIC, location JSON, mwbase NUMERIC, name TEXT, owner JSON, pgv1 NUMERIC, pgv2 NUMERIC, pgv3 NUMERIC, pgv4 NUMERIC, pgv5 NUMERIC, pgv6 NUMERIC, pmax NUMERIC, pmin NUMERIC, rperm NUMERIC, rtemp NUMERIC, seeAlso JSON, source TEXT, tg NUMERIC, tp NUMERIC, tr NUMERIC, tw NUMERIC, type GovHydro2_type, uc NUMERIC, uo NUMERIC);