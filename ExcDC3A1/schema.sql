/* (Beta) Export of data model ExcDC3A1 of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE ExcDC3A1_type AS ENUM ('ExcDC3A1');
CREATE TABLE ExcDC3A1 (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, exclim NUMERIC, ka NUMERIC, ke NUMERIC, kf NUMERIC, ki NUMERIC, kp NUMERIC, name TEXT, owner JSON, source TEXT, ta NUMERIC, te NUMERIC, tf NUMERIC, type ExcDC3A1_type, vb1max NUMERIC, vblim NUMERIC, vbmax NUMERIC, vrmax NUMERIC, vrmin NUMERIC);