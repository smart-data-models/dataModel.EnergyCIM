/* (Beta) Export of data model ExcSCRX of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE ExcSCRX_type AS ENUM ('ExcSCRX');
CREATE TABLE ExcSCRX (address JSON, alternateName TEXT, areaServed TEXT, cswitch NUMERIC, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, emax NUMERIC, emin NUMERIC, k NUMERIC, name TEXT, owner JSON, rcrfd NUMERIC, source TEXT, tatb NUMERIC, tb NUMERIC, te NUMERIC, type ExcSCRX_type);