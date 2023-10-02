/* (Beta) Export of data model WindContQIEC of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE WindContQIEC_type AS ENUM ('WindContQIEC');
CREATE TABLE WindContQIEC (WindTurbineType3or4IEC NUMERIC, address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, iqh1 NUMERIC, iqmax NUMERIC, iqmin NUMERIC, iqpost NUMERIC, kiq NUMERIC, kiu NUMERIC, kpq NUMERIC, kpu NUMERIC, kqv NUMERIC, name TEXT, owner JSON, qmax NUMERIC, qmin NUMERIC, rdroop NUMERIC, source TEXT, tiq NUMERIC, tpfilt NUMERIC, tpost NUMERIC, tqord NUMERIC, tufilt NUMERIC, type WindContQIEC_type, udb1 NUMERIC, udb2 NUMERIC, umax NUMERIC, umin NUMERIC, uqdip NUMERIC, uref0 NUMERIC, windLVRTQcontrolModesType NUMERIC, windQcontrolModesType NUMERIC, xdroop NUMERIC);