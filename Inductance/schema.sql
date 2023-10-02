/* (Beta) Export of data model Inductance of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Inductance_type AS ENUM ('Inductance');
CREATE TABLE Inductance (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, multiplier NUMERIC, name TEXT, owner JSON, source TEXT, type Inductance_type, unit NUMERIC, value NUMERIC);