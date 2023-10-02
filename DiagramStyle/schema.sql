/* (Beta) Export of data model DiagramStyle of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE DiagramStyle_type AS ENUM ('DiagramStyle');
CREATE TABLE DiagramStyle (Diagram NUMERIC, address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, name TEXT, owner JSON, source TEXT, type DiagramStyle_type);