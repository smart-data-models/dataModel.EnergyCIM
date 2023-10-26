/* (Beta) Export of data model WindDynamicsLookupTable of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE WindDynamicsLookupTable_type AS ENUM ('WindDynamicsLookupTable');
CREATE TABLE WindDynamicsLookupTable (WindContCurrLimIEC NUMERIC, WindContPType3IEC NUMERIC, WindContRotorRIEC NUMERIC, WindPlantFreqPcontrolIEC NUMERIC, address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, id TEXT PRIMARY KEY, input NUMERIC, location JSON, lookupTableFunctionType NUMERIC, name TEXT, output NUMERIC, owner JSON, seeAlso JSON, sequence NUMERIC, source TEXT, type WindDynamicsLookupTable_type);