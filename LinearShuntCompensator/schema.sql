/* (Beta) Export of data model LinearShuntCompensator of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE LinearShuntCompensator_type AS ENUM ('LinearShuntCompensator');
CREATE TABLE LinearShuntCompensator (address JSON, alternateName TEXT, areaServed TEXT, b0PerSection NUMERIC, bPerSection NUMERIC, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, g0PerSection NUMERIC, gPerSection NUMERIC, name TEXT, owner JSON, source TEXT, type LinearShuntCompensator_type);