/* (Beta) Export of data model ExcIEEEDC4B of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE ExcIEEEDC4B_type AS ENUM ('ExcIEEEDC4B');
CREATE TABLE ExcIEEEDC4B (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, efd1 NUMERIC, efd2 NUMERIC, id TEXT PRIMARY KEY, ka NUMERIC, kd NUMERIC, ke NUMERIC, kf NUMERIC, ki NUMERIC, kp NUMERIC, location JSON, name TEXT, oelin NUMERIC, owner JSON, seeAlso JSON, seefd1 NUMERIC, seefd2 NUMERIC, source TEXT, ta NUMERIC, td NUMERIC, te NUMERIC, tf NUMERIC, type ExcIEEEDC4B_type, uelin NUMERIC, vemin NUMERIC, vrmax NUMERIC, vrmin NUMERIC);