/* (Beta) Export of data model OverexcLim2 of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE OverexcLim2_type AS ENUM ('OverexcLim2');
CREATE TABLE OverexcLim2 (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, id TEXT PRIMARY KEY, ifdlim NUMERIC, koi NUMERIC, location JSON, name TEXT, owner JSON, seeAlso JSON, source TEXT, type OverexcLim2_type, voimax NUMERIC, voimin NUMERIC);