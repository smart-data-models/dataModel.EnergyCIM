/* (Beta) Export of data model ProprietaryParameterDynamics of the subject dataModel.EnergyCIM for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE ProprietaryParameterDynamics_type AS ENUM ('ProprietaryParameterDynamics');
CREATE TABLE ProprietaryParameterDynamics (AsynchronousMachineUserDefined text, DiscontinuousExcitationControlUserDefined text, ExcitationSystemUserDefined text, LoadUserDefined text, MechanicalLoadUserDefined text, OverexcitationLimiterUserDefined text, PFVArControllerType1UserDefined text, PFVArControllerType2UserDefined text, PowerSystemStabilizerUserDefined text, SynchronousMachineUserDefined text, TurbineGovernorUserDefined text, TurbineLoadControllerUserDefined text, UnderexcitationLimiterUserDefined text, VoltageAdjusterUserDefined text, VoltageCompensatorUserDefined text, WindPlantUserDefined text, WindType1or2UserDefined text, WindType3or4UserDefined text, address json, alternateName text, areaServed text, booleanParameterValue text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, floatParameterValue text, id text, integerParameterValue text, location json, name text, owner json, parameterNumber text, seeAlso json, source text, type ProprietaryParameterDynamics_type);