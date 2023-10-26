/* (Beta) Export of data model UnderexcLimIEEE1 of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE UnderexcLimIEEE1_type AS ENUM ('UnderexcLimIEEE1');
CREATE TABLE UnderexcLimIEEE1 (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, id TEXT PRIMARY KEY, kuc NUMERIC, kuf NUMERIC, kui NUMERIC, kul NUMERIC, kur NUMERIC, location JSON, name TEXT, owner JSON, seeAlso JSON, source TEXT, tu1 NUMERIC, tu2 NUMERIC, tu3 NUMERIC, tu4 NUMERIC, type UnderexcLimIEEE1_type, vucmax NUMERIC, vuimax NUMERIC, vuimin NUMERIC, vulmax NUMERIC, vulmin NUMERIC, vurmax NUMERIC);