/* (Beta) Export of data model Command of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Command_type AS ENUM ('Command');
CREATE TABLE Command (DiscreteValue NUMERIC, ValueAliasSet NUMERIC, address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, name TEXT, normalValue NUMERIC, owner JSON, source TEXT, type Command_type, value NUMERIC);