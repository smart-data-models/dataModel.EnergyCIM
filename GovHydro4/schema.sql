/* (Beta) Export of data model GovHydro4 of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE GovHydro4_type AS ENUM ('GovHydro4');
CREATE TABLE GovHydro4 (address JSON, alternateName TEXT, areaServed TEXT, at NUMERIC, bgv0 NUMERIC, bgv1 NUMERIC, bgv2 NUMERIC, bgv3 NUMERIC, bgv4 NUMERIC, bgv5 NUMERIC, bmax NUMERIC, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, db1 NUMERIC, db2 NUMERIC, description TEXT, dturb NUMERIC, eps NUMERIC, gmax NUMERIC, gmin NUMERIC, gv0 NUMERIC, gv1 NUMERIC, gv2 NUMERIC, gv3 NUMERIC, gv4 NUMERIC, gv5 NUMERIC, hdam NUMERIC, id TEXT PRIMARY KEY, location JSON, mwbase NUMERIC, name TEXT, owner JSON, pgv0 NUMERIC, pgv1 NUMERIC, pgv2 NUMERIC, pgv3 NUMERIC, pgv4 NUMERIC, pgv5 NUMERIC, qn1 NUMERIC, rperm NUMERIC, rtemp NUMERIC, seeAlso JSON, source TEXT, tblade NUMERIC, tg NUMERIC, tp NUMERIC, tr NUMERIC, tw NUMERIC, type GovHydro4_type, uc NUMERIC, uo NUMERIC);