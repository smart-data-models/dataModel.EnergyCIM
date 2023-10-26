/* (Beta) Export of data model DynamicsFunctionBlock of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE DynamicsFunctionBlock_type AS ENUM ('DynamicsFunctionBlock');
CREATE TABLE DynamicsFunctionBlock (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, enabled NUMERIC, id TEXT PRIMARY KEY, location JSON, name TEXT, owner JSON, seeAlso JSON, source TEXT, type DynamicsFunctionBlock_type);