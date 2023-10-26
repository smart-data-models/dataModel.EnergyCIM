/* (Beta) Export of data model EquivalentShunt of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE EquivalentShunt_type AS ENUM ('EquivalentShunt');
CREATE TABLE EquivalentShunt (address JSON, alternateName TEXT, areaServed TEXT, b NUMERIC, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, g NUMERIC, id TEXT PRIMARY KEY, location JSON, name TEXT, owner JSON, seeAlso JSON, source TEXT, type EquivalentShunt_type);