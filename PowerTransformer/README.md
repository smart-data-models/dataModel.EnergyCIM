[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)
# PowerTransformer
Version: 0.0.1

## Description 

Adapted from CIM data models. An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow). A power transformer may be composed of separate transformer tanks that need not be identical. A power transformer can be modeled with or without tanks and is intended for use in both balanced and unbalanced representations.   A power transformer typically has two terminals, but may have one (grounding), three or more terminals. The inherited association ConductingEquipment.BaseVoltage should not be used.  The association from TransformerEnd to BaseVoltage should be used instead.
### Specification

Link to the [interactive specification](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.EnergyCIM/PowerTransformer/swagger.yaml)

Link to the [specification](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PowerTransformer/doc/spec.md)

Enlace a la [Especificación en español](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PowerTransformer/doc/spec_ES.md)

Lien vers le [spécification en français](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PowerTransformer/doc/spec_FR.md)

Link zur [deutschen Spezifikation](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PowerTransformer/doc/spec_DE.md)

Link alla [specifica](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PowerTransformer/doc/spec_IT.md)

[仕様へのリンク](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PowerTransformer/doc/spec_JA.md)

[链接到规范](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PowerTransformer/doc/spec_ZH.md)
### Examples
### Dynamic Examples generation

Link to the [Generator](https://smartdatamodels.org/extra/ngsi-ld_generator.php?schemaUrl=https://raw.githubusercontent.com/smart-data-models/dataModel.EnergyCIM/master/PowerTransformer/schema.json&email=info@smartdatamodels.org) of NGSI-LD normalized payloads compliant with this data model. Refresh for new values

Link to the [Generator](https://smartdatamodels.org/extra/ngsi-ld_generator_keyvalues.php?schemaUrl=https://raw.githubusercontent.com/smart-data-models/dataModel.EnergyCIM/master/PowerTransformer/schema.json&email=info@smartdatamodels.org) of NGSI-LD keyvalues payloads compliant with this data model. Refresh for new values

Link to the [Generator](https://smartdatamodels.org/extra/geojson_features_generator.php?schemaUrl=https://raw.githubusercontent.com/smart-data-models/dataModel.EnergyCIM/master/PowerTransformer/schema.json&email=info@smartdatamodels.org) of geojson feature format payloads compliant with this data model. Refresh for new values
### PostgreSQL schema

Link to the [PostgreSQL schema](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PowerTransformer/schema.sql) of this data model
### Contribution

 If you have any issue on this data model you can raise an [issue](https://github.com/smart-data-models/dataModel.EnergyCIM/issues)  or contribute with a [PR](https://github.com/smart-data-models/dataModel.EnergyCIM/pulls)

 If you wish to develop your own data model you can start from [contribution manual](https://bit.ly/contribution_manual). Several services have been developed to help with: 
 - [Test data model repository](https://smartdatamodels.org/index.php/data-models-contribution-api/) including the schema and example payloads, etc
 - [Generate PostgreSQL schema](https://smartdatamodels.org/index.php/sql-service/) to help create a table, create type, etc