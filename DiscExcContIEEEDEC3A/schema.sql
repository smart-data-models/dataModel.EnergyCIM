/* (Beta) Export of data model DiscExcContIEEEDEC3A of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE DiscExcContIEEEDEC3A_type AS ENUM ('DiscExcContIEEEDEC3A');
CREATE TABLE DiscExcContIEEEDEC3A (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, name TEXT, owner JSON, source TEXT, tdr NUMERIC, type DiscExcContIEEEDEC3A_type, vtmin NUMERIC);