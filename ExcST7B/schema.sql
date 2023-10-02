/* (Beta) Export of data model ExcST7B of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE ExcST7B_type AS ENUM ('ExcST7B');
CREATE TABLE ExcST7B (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, kh NUMERIC, kia NUMERIC, kl NUMERIC, kpa NUMERIC, name TEXT, oelin NUMERIC, owner JSON, source TEXT, tb NUMERIC, tc NUMERIC, tf NUMERIC, tg NUMERIC, tia NUMERIC, ts NUMERIC, type ExcST7B_type, uelin NUMERIC, vmax NUMERIC, vmin NUMERIC, vrmax NUMERIC, vrmin NUMERIC);