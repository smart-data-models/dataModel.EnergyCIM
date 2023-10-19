[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)
# PowerTransformerEnd
Version: 0.0.1

## Description 

Adapted from CIM data models. A PowerTransformerEnd is associated with each Terminal of a PowerTransformer. The impedance values r, r0, x, and x0 of a PowerTransformerEnd represents a star equivalent as follows 1) for a two Terminal PowerTransformer the high voltage PowerTransformerEnd has non zero values on r, r0, x, and x0 while the low voltage PowerTransformerEnd has zero values for r, r0, x, and x0. 2) for a three Terminal PowerTransformer the three PowerTransformerEnds represents a star equivalent with each leg in the star represented by r, r0, x, and x0 values. 3) for a PowerTransformer with more than three Terminals the PowerTransformerEnd impedance values cannot be used. Instead use the TransformerMeshImpedance or split the transformer into multiple PowerTransformers.
### Specification

Link to the [interactive specification](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.EnergyCIM/PowerTransformerEnd/swagger.yaml)

Link to the [specification](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PowerTransformerEnd/doc/spec.md)

Enlace a la [Especificación en español](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PowerTransformerEnd/doc/spec_ES.md)

Lien vers le [spécification en français](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PowerTransformerEnd/doc/spec_FR.md)

Link zur [deutschen Spezifikation](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PowerTransformerEnd/doc/spec_DE.md)

Link alla [specifica](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PowerTransformerEnd/doc/spec_IT.md)

[仕様へのリンク](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PowerTransformerEnd/doc/spec_JA.md)

[链接到规范](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PowerTransformerEnd/doc/spec_ZH.md)
### Examples
### Dynamic Examples generation

Link to the [Generator](https://smartdatamodels.org/extra/ngsi-ld_generator.php?schemaUrl=https://raw.githubusercontent.com/smart-data-models/dataModel.EnergyCIM/master/PowerTransformerEnd/schema.json&email=info@smartdatamodels.org) of NGSI-LD normalized payloads compliant with this data model. Refresh for new values

Link to the [Generator](https://smartdatamodels.org/extra/ngsi-ld_generator_keyvalues.php?schemaUrl=https://raw.githubusercontent.com/smart-data-models/dataModel.EnergyCIM/master/PowerTransformerEnd/schema.json&email=info@smartdatamodels.org) of NGSI-LD keyvalues payloads compliant with this data model. Refresh for new values

Link to the [Generator](https://smartdatamodels.org/extra/geojson_features_generator.php?schemaUrl=https://raw.githubusercontent.com/smart-data-models/dataModel.EnergyCIM/master/PowerTransformerEnd/schema.json&email=info@smartdatamodels.org) of geojson feature format payloads compliant with this data model. Refresh for new values
### PostgreSQL schema

Link to the [PostgreSQL schema](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PowerTransformerEnd/schema.sql) of this data model
### Contribution

 If you have any issue on this data model you can raise an [issue](https://github.com/smart-data-models/dataModel.EnergyCIM/issues)  or contribute with a [PR](https://github.com/smart-data-models/dataModel.EnergyCIM/pulls)

 If you wish to develop your own data model you can start from [contribution manual](https://bit.ly/contribution_manual). Several services have been developed to help with: 
 - [Test data model repository](https://smartdatamodels.org/index.php/data-models-contribution-api/) including the schema and example payloads, etc
 - [Generate PostgreSQL schema](https://smartdatamodels.org/index.php/sql-service/) to help create a table, create type, etc