/* (Beta) Export of data model ExcST2A of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE ExcST2A_type AS ENUM ('ExcST2A');
CREATE TABLE ExcST2A (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, efdmax NUMERIC, id TEXT PRIMARY KEY, ka NUMERIC, kc NUMERIC, ke NUMERIC, kf NUMERIC, ki NUMERIC, kp NUMERIC, location JSON, name TEXT, owner JSON, seeAlso JSON, source TEXT, ta NUMERIC, tb NUMERIC, tc NUMERIC, te NUMERIC, tf NUMERIC, type ExcST2A_type, uelin NUMERIC, vrmax NUMERIC, vrmin NUMERIC);