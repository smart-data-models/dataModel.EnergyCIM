/* (Beta) Export of data model GovHydro1 of the subject dataModel.EnergyCIM for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE GovHydro1_type AS ENUM ('GovHydro1');
CREATE TABLE GovHydro1 (address json, alternateName text, areaServed text, at text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, dturb text, gmax text, gmin text, hdam text, id text, location json, mwbase text, name text, owner json, qnl text, rperm text, rtemp text, seeAlso json, source text, tf text, tg text, tr text, tw text, type GovHydro1_type, velm text);