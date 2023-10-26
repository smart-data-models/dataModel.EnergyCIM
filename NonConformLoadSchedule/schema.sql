/* (Beta) Export of data model NonConformLoadSchedule of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE NonConformLoadSchedule_type AS ENUM ('NonConformLoadSchedule');
CREATE TABLE NonConformLoadSchedule (NonConformLoadGroup NUMERIC, address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, id TEXT PRIMARY KEY, location JSON, name TEXT, owner JSON, seeAlso JSON, source TEXT, type NonConformLoadSchedule_type);