/* (Beta) Export of data model LoadGenericNonLinear of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE LoadGenericNonLinear_type AS ENUM ('LoadGenericNonLinear');
CREATE TABLE LoadGenericNonLinear (address JSON, alternateName TEXT, areaServed TEXT, bs NUMERIC, bt NUMERIC, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, genericNonLinearLoadModelType NUMERIC, ls NUMERIC, lt NUMERIC, name TEXT, owner JSON, pt NUMERIC, qt NUMERIC, source TEXT, tp NUMERIC, tq NUMERIC, type LoadGenericNonLinear_type);