/* (Beta) Export of data model PhaseTapChangerTabular of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE PhaseTapChangerTabular_type AS ENUM ('PhaseTapChangerTabular');
CREATE TABLE PhaseTapChangerTabular (PhaseTapChangerTable NUMERIC, address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, name TEXT, owner JSON, source TEXT, type PhaseTapChangerTabular_type);