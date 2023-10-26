/* (Beta) Export of data model GovHydroFrancis of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE GovHydroFrancis_type AS ENUM ('GovHydroFrancis');
CREATE TABLE GovHydroFrancis (address JSON, alternateName TEXT, am NUMERIC, areaServed TEXT, av0 NUMERIC, av1 NUMERIC, bp NUMERIC, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, db1 NUMERIC, description TEXT, etamax NUMERIC, governorControl NUMERIC, h1 NUMERIC, h2 NUMERIC, hn NUMERIC, id TEXT PRIMARY KEY, kc NUMERIC, kg NUMERIC, kt NUMERIC, location JSON, name TEXT, owner JSON, qc0 NUMERIC, qn NUMERIC, seeAlso JSON, source TEXT, ta NUMERIC, td NUMERIC, ts NUMERIC, twnc NUMERIC, twng NUMERIC, tx NUMERIC, type GovHydroFrancis_type, va NUMERIC, valvmax NUMERIC, valvmin NUMERIC, vc NUMERIC, waterTunnelSurgeChamberSimulation NUMERIC, zsfc NUMERIC);