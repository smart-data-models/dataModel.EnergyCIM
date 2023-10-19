[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)
# ExcIEEEAC8B
Version: 0.0.1

## Description 

Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type AC8B model. This model represents a PID voltage regulator with either a brushless exciter or dc exciter. The AVR in this model consists of PID control, with separate constants for the proportional (), integral (), and derivative () gains. The representation of the brushless exciter (, , , , ) is similar to the model Type AC2A. The Type AC8B model can be used to represent static voltage regulators applied to brushless excitation systems. Digitally based voltage regulators feeding dc rotating main exciters can be represented with the AC Type AC8B model with the parameters  and  set to 0.  For thyristor power stages fed from the generator terminals, the limits  and  should be a function of terminal voltage:  * and  * .     Reference: IEEE Standard 421.5-2005 Section 6.8.
### Specification

Link to the [interactive specification](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.EnergyCIM/ExcIEEEAC8B/swagger.yaml)

Link to the [specification](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcIEEEAC8B/doc/spec.md)

Enlace a la [Especificación en español](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcIEEEAC8B/doc/spec_ES.md)

Lien vers le [spécification en français](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcIEEEAC8B/doc/spec_FR.md)

Link zur [deutschen Spezifikation](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcIEEEAC8B/doc/spec_DE.md)

Link alla [specifica](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcIEEEAC8B/doc/spec_IT.md)

[仕様へのリンク](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcIEEEAC8B/doc/spec_JA.md)

[链接到规范](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcIEEEAC8B/doc/spec_ZH.md)
### Examples
### Dynamic Examples generation

Link to the [Generator](https://smartdatamodels.org/extra/ngsi-ld_generator.php?schemaUrl=https://raw.githubusercontent.com/smart-data-models/dataModel.EnergyCIM/master/ExcIEEEAC8B/schema.json&email=info@smartdatamodels.org) of NGSI-LD normalized payloads compliant with this data model. Refresh for new values

Link to the [Generator](https://smartdatamodels.org/extra/ngsi-ld_generator_keyvalues.php?schemaUrl=https://raw.githubusercontent.com/smart-data-models/dataModel.EnergyCIM/master/ExcIEEEAC8B/schema.json&email=info@smartdatamodels.org) of NGSI-LD keyvalues payloads compliant with this data model. Refresh for new values

Link to the [Generator](https://smartdatamodels.org/extra/geojson_features_generator.php?schemaUrl=https://raw.githubusercontent.com/smart-data-models/dataModel.EnergyCIM/master/ExcIEEEAC8B/schema.json&email=info@smartdatamodels.org) of geojson feature format payloads compliant with this data model. Refresh for new values
### PostgreSQL schema

Link to the [PostgreSQL schema](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcIEEEAC8B/schema.sql) of this data model
### Contribution

 If you have any issue on this data model you can raise an [issue](https://github.com/smart-data-models/dataModel.EnergyCIM/issues)  or contribute with a [PR](https://github.com/smart-data-models/dataModel.EnergyCIM/pulls)

 If you wish to develop your own data model you can start from [contribution manual](https://bit.ly/contribution_manual). Several services have been developed to help with: 
 - [Test data model repository](https://smartdatamodels.org/index.php/data-models-contribution-api/) including the schema and example payloads, etc
 - [Generate PostgreSQL schema](https://smartdatamodels.org/index.php/sql-service/) to help create a table, create type, etc