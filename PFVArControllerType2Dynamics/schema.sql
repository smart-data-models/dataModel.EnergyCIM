/* (Beta) Export of data model PFVArControllerType2Dynamics of the subject dataModel.EnergyCIM for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE PFVArControllerType2Dynamics_type AS ENUM ('PFVArControllerType2Dynamics');
CREATE TABLE PFVArControllerType2Dynamics (ExcitationSystemDynamics text, address json, alternateName text, areaServed text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, id text, location json, name text, owner json, seeAlso json, source text, type PFVArControllerType2Dynamics_type);