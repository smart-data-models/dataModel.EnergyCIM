/* (Beta) Export of data model SynchronousMachineDetailed of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE SynchronousMachineDetailed_type AS ENUM ('SynchronousMachineDetailed');
CREATE TABLE SynchronousMachineDetailed (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, efdBaseRatio NUMERIC, ifdBaseType NUMERIC, ifdBaseValue NUMERIC, name TEXT, owner JSON, saturationFactor120QAxis NUMERIC, saturationFactorQAxis NUMERIC, source TEXT, type SynchronousMachineDetailed_type);