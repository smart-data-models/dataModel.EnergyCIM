/* (Beta) Export of data model VCompIEEEType2 of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE VCompIEEEType2_type AS ENUM ('VCompIEEEType2');
CREATE TABLE VCompIEEEType2 (GenICompensationForGenJ NUMERIC, address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, id TEXT PRIMARY KEY, location JSON, name TEXT, owner JSON, seeAlso JSON, source TEXT, tr NUMERIC, type VCompIEEEType2_type);