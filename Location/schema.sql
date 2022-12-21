/* (Beta) Export of data model Location of the subject dataModel.EnergyCIM for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Location_type AS ENUM ('Location');
CREATE TABLE Location (CoordinateSystem text, PositionPoints text, PowerSystemResources text, address json, alternateName text, areaServed text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, id text, location json, name text, owner json, seeAlso json, source text, type Location_type);