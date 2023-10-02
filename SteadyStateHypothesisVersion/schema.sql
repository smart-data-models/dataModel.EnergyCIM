/* (Beta) Export of data model SteadyStateHypothesisVersion of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE SteadyStateHypothesisVersion_type AS ENUM ('SteadyStateHypothesisVersion');
CREATE TABLE SteadyStateHypothesisVersion (address JSON, alternateName TEXT, areaServed TEXT, baseUML NUMERIC, baseURI NUMERIC, dataProvider TEXT, date NUMERIC, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, differenceModelURI NUMERIC, entsoeUML NUMERIC, entsoeURI NUMERIC, modelDescriptionURI NUMERIC, name TEXT, namespaceRDF NUMERIC, namespaceUML NUMERIC, owner JSON, shortName NUMERIC, source TEXT, type SteadyStateHypothesisVersion_type);