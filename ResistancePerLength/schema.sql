/* (Beta) Export of data model ResistancePerLength of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE ResistancePerLength_type AS ENUM ('ResistancePerLength');
CREATE TABLE ResistancePerLength (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, denominatorMultiplier NUMERIC, denominatorUnit NUMERIC, description TEXT, multiplier NUMERIC, name TEXT, owner JSON, source TEXT, type ResistancePerLength_type, unit NUMERIC, value NUMERIC);