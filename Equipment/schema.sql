/* (Beta) Export of data model Equipment of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Equipment_type AS ENUM ('Equipment');
CREATE TABLE Equipment (EquipmentContainer NUMERIC, OperationalLimitSet NUMERIC, address JSON, aggregate NUMERIC, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, id TEXT PRIMARY KEY, location JSON, name TEXT, owner JSON, seeAlso JSON, source TEXT, type Equipment_type);