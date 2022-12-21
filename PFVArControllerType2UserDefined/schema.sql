/* (Beta) Export of data model PFVArControllerType2UserDefined of the subject dataModel.EnergyCIM for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE PFVArControllerType2UserDefined_type AS ENUM ('PFVArControllerType2UserDefined');
CREATE TABLE PFVArControllerType2UserDefined (ProprietaryParameterDynamics text, address json, alternateName text, areaServed text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, id text, location json, name text, owner json, proprietary text, seeAlso json, source text, type PFVArControllerType2UserDefined_type);