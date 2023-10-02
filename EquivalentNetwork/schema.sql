/* (Beta) Export of data model EquivalentNetwork of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE EquivalentNetwork_type AS ENUM ('EquivalentNetwork');
CREATE TABLE EquivalentNetwork (EquivalentEquipments NUMERIC, address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, name TEXT, owner JSON, source TEXT, type EquivalentNetwork_type);