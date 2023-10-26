/* (Beta) Export of data model ACDCConverterDCTerminal of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE ACDCConverterDCTerminal_type AS ENUM ('ACDCConverterDCTerminal');
CREATE TABLE ACDCConverterDCTerminal (DCConductingEquipment NUMERIC, address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, id TEXT PRIMARY KEY, location JSON, name TEXT, owner JSON, polarity NUMERIC, seeAlso JSON, source TEXT, type ACDCConverterDCTerminal_type);