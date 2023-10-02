/* (Beta) Export of data model ExcAVR3 of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE ExcAVR3_type AS ENUM ('ExcAVR3');
CREATE TABLE ExcAVR3 (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, e1 NUMERIC, e2 NUMERIC, ka NUMERIC, name TEXT, owner JSON, se1 NUMERIC, se2 NUMERIC, source TEXT, t1 NUMERIC, t2 NUMERIC, t3 NUMERIC, t4 NUMERIC, te NUMERIC, type ExcAVR3_type, vrmn NUMERIC, vrmx NUMERIC);