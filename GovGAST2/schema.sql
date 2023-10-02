/* (Beta) Export of data model GovGAST2 of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE GovGAST2_type AS ENUM ('GovGAST2');
CREATE TABLE GovGAST2 (a NUMERIC, address JSON, af1 NUMERIC, af2 NUMERIC, alternateName TEXT, areaServed TEXT, b NUMERIC, bf1 NUMERIC, bf2 NUMERIC, c NUMERIC, cf2 NUMERIC, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, ecr NUMERIC, etd NUMERIC, k3 NUMERIC, k4 NUMERIC, k5 NUMERIC, k6 NUMERIC, kf NUMERIC, mwbase NUMERIC, name TEXT, owner JSON, source TEXT, t NUMERIC, t3 NUMERIC, t4 NUMERIC, t5 NUMERIC, tc NUMERIC, tcd NUMERIC, tf NUMERIC, tmax NUMERIC, tmin NUMERIC, tr NUMERIC, trate NUMERIC, tt NUMERIC, type GovGAST2_type, w NUMERIC, x NUMERIC, y NUMERIC, z NUMERIC);