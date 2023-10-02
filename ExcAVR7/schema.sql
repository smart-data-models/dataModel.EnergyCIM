/* (Beta) Export of data model ExcAVR7 of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE ExcAVR7_type AS ENUM ('ExcAVR7');
CREATE TABLE ExcAVR7 (a1 NUMERIC, a2 NUMERIC, a3 NUMERIC, a4 NUMERIC, a5 NUMERIC, a6 NUMERIC, address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, k1 NUMERIC, k3 NUMERIC, k5 NUMERIC, name TEXT, owner JSON, source TEXT, t1 NUMERIC, t2 NUMERIC, t3 NUMERIC, t4 NUMERIC, t5 NUMERIC, t6 NUMERIC, type ExcAVR7_type, vmax1 NUMERIC, vmax3 NUMERIC, vmax5 NUMERIC, vmin1 NUMERIC, vmin3 NUMERIC, vmin5 NUMERIC);