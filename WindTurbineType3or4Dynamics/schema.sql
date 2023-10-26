/* (Beta) Export of data model WindTurbineType3or4Dynamics of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE WindTurbineType3or4Dynamics_type AS ENUM ('WindTurbineType3or4Dynamics');
CREATE TABLE WindTurbineType3or4Dynamics (EnergySource NUMERIC, RemoteInputSignal NUMERIC, WindPlantDynamics NUMERIC, address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, id TEXT PRIMARY KEY, location JSON, name TEXT, owner JSON, seeAlso JSON, source TEXT, type WindTurbineType3or4Dynamics_type);