/* (Beta) Export of data model GeneratingUnit of the subject dataModel.EnergyCIM for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE GeneratingUnit_type AS ENUM ('GeneratingUnit');
CREATE TABLE GeneratingUnit (ControlAreaGeneratingUnit text, GrossToNetActivePowerCurves text, RotatingMachine text, address json, alternateName text, areaServed text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, genControlSource text, governorSCD text, id text, initialP text, location json, longPF text, maxOperatingP text, maximumAllowableSpinningReserve text, minOperatingP text, name text, nominalP text, normalPF text, owner json, ratedGrossMaxP text, ratedGrossMinP text, ratedNetMaxP text, seeAlso json, shortPF text, source text, startupCost text, totalEfficiency text, type GeneratingUnit_type, variableCost text);