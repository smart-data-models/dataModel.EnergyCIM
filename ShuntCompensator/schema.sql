/* (Beta) Export of data model ShuntCompensator of the subject dataModel.EnergyCIM for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE ShuntCompensator_type AS ENUM ('ShuntCompensator');
CREATE TABLE ShuntCompensator (SvShuntCompensatorSections text, aVRDelay text, address json, alternateName text, areaServed text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, grounded text, id text, location json, maximumSections text, name text, nomU text, normalSections text, owner json, sections text, seeAlso json, source text, switchOnCount text, switchOnDate text, type ShuntCompensator_type, voltageSensitivity text);