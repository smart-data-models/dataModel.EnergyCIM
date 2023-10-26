/* (Beta) Export of data model TurbLCFB1 of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE TurbLCFB1_type AS ENUM ('TurbLCFB1');
CREATE TABLE TurbLCFB1 (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, db NUMERIC, description TEXT, emax NUMERIC, fb NUMERIC, fbf NUMERIC, id TEXT PRIMARY KEY, irmax NUMERIC, ki NUMERIC, kp NUMERIC, location JSON, mwbase NUMERIC, name TEXT, owner JSON, pbf NUMERIC, pmwset NUMERIC, seeAlso JSON, source TEXT, speedReferenceGovernor NUMERIC, tpelec NUMERIC, type TurbLCFB1_type);