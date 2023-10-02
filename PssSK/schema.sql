/* (Beta) Export of data model PssSK of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE PssSK_type AS ENUM ('PssSK');
CREATE TABLE PssSK (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, k1 NUMERIC, k2 NUMERIC, k3 NUMERIC, name TEXT, owner JSON, source TEXT, t1 NUMERIC, t2 NUMERIC, t3 NUMERIC, t4 NUMERIC, t5 NUMERIC, t6 NUMERIC, type PssSK_type, vsmax NUMERIC, vsmin NUMERIC);