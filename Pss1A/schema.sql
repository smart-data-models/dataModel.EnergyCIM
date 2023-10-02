/* (Beta) Export of data model Pss1A of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Pss1A_type AS ENUM ('Pss1A');
CREATE TABLE Pss1A (a1 NUMERIC, a2 NUMERIC, a3 NUMERIC, a4 NUMERIC, a5 NUMERIC, a6 NUMERIC, a7 NUMERIC, a8 NUMERIC, address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, inputSignalType NUMERIC, kd NUMERIC, ks NUMERIC, name TEXT, owner JSON, source TEXT, t1 NUMERIC, t2 NUMERIC, t3 NUMERIC, t4 NUMERIC, t5 NUMERIC, t6 NUMERIC, tdelay NUMERIC, type Pss1A_type, vcl NUMERIC, vcu NUMERIC, vrmax NUMERIC, vrmin NUMERIC);