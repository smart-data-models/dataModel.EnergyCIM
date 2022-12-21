/* (Beta) Export of data model ExcST1A of the subject dataModel.EnergyCIM for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE ExcST1A_type AS ENUM ('ExcST1A');
CREATE TABLE ExcST1A (address json, alternateName text, areaServed text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, id text, ilr text, ka text, kc text, kf text, klr text, location json, name text, owner json, seeAlso json, source text, ta text, tb text, tb1 text, tc text, tc1 text, tf text, type ExcST1A_type, vamax text, vamin text, vimax text, vimin text, vrmax text, vrmin text, xe text);