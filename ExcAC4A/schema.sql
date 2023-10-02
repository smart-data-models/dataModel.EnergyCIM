/* (Beta) Export of data model ExcAC4A of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE ExcAC4A_type AS ENUM ('ExcAC4A');
CREATE TABLE ExcAC4A (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, ka NUMERIC, kc NUMERIC, name TEXT, owner JSON, source TEXT, ta NUMERIC, tb NUMERIC, tc NUMERIC, type ExcAC4A_type, vimax NUMERIC, vimin NUMERIC, vrmax NUMERIC, vrmin NUMERIC);