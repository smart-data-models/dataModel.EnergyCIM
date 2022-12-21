/* (Beta) Export of data model PowerSystemResource of the subject dataModel.EnergyCIM for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE PowerSystemResource_type AS ENUM ('PowerSystemResource');
CREATE TABLE PowerSystemResource (Controls text, Location text, Measurements text, address json, alternateName text, areaServed text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, id text, location json, name text, owner json, seeAlso json, source text, type PowerSystemResource_type);