/* (Beta) Export of data model WindAeroConstIEC of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE WindAeroConstIEC_type AS ENUM ('WindAeroConstIEC');
CREATE TABLE WindAeroConstIEC (WindGenTurbineType1IEC NUMERIC, address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, id TEXT PRIMARY KEY, location JSON, name TEXT, owner JSON, seeAlso JSON, source TEXT, type WindAeroConstIEC_type);