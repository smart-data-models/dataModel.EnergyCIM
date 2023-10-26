/* (Beta) Export of data model Seconds of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Seconds_type AS ENUM ('Seconds');
CREATE TABLE Seconds (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, id TEXT PRIMARY KEY, location JSON, multiplier NUMERIC, name TEXT, owner JSON, seeAlso JSON, source TEXT, type Seconds_type, unit NUMERIC, value NUMERIC);