/* (Beta) Export of data model SwitchSchedule of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE SwitchSchedule_type AS ENUM ('SwitchSchedule');
CREATE TABLE SwitchSchedule (Switch NUMERIC, address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, id TEXT PRIMARY KEY, location JSON, name TEXT, owner JSON, seeAlso JSON, source TEXT, type SwitchSchedule_type);