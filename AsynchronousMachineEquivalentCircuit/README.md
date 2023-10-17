[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)
# AsynchronousMachineEquivalentCircuit
Version: 0.0.1

## Description 

Adapted from CIM data models. The electrical equations of all variations of the asynchronous model are based on the AsynchronousEquivalentCircuit diagram for the direct and quadrature axes, with two equivalent rotor windings in each axis.      =  +   =  +  *  / ( + )  =  +  * *  / ( *  +  *  +  * )  = ( + ) / ( * )  = ( *  +  *  +  * ) / ( *  * (+ ) Same equations using CIM attributes from AsynchronousMachineTimeConstantReactance class on left of = sign and AsynchronousMachineEquivalentCircuit class on right (except as noted): xs = xm + RotatingMachineDynamics.statorLeakageReactance xp = RotatingMachineDynamics.statorLeakageReactance + xm * xlr1 / (xm + xlr1) xpp = RotatingMachineDynamics.statorLeakageReactance + xm * xlr1* xlr2 / (xm * xlr1 + xm * xlr2 + xlr1 * xlr2) tpo = (xm + xlr1) / (2*pi*nominal frequency * rr1) tppo = (xm * xlr1 + xm * xlr2 + xlr1 * xlr2) / (2*pi*nominal frequency * rr2 * (xm + xlr1).
### Specification

Link to the [interactive specification](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.EnergyCIM/AsynchronousMachineEquivalentCircuit/swagger.yaml)

Link to the [specification](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/AsynchronousMachineEquivalentCircuit/doc/spec.md)

Enlace a la [Especificación en español](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/AsynchronousMachineEquivalentCircuit/doc/spec_ES.md)

Lien vers le [spécification en français](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/AsynchronousMachineEquivalentCircuit/doc/spec_FR.md)

Link zur [deutschen Spezifikation](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/AsynchronousMachineEquivalentCircuit/doc/spec_DE.md)

Link alla [specifica](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/AsynchronousMachineEquivalentCircuit/doc/spec_IT.md)

[仕様へのリンク](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/AsynchronousMachineEquivalentCircuit/doc/spec_JA.md)

[链接到规范](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/AsynchronousMachineEquivalentCircuit/doc/spec_ZH.md)
### Examples
### Dynamic Examples generation

Link to the [Generator](https://smartdatamodels.org/extra/ngsi-ld_generator.php?schemaUrl=https://raw.githubusercontent.com/smart-data-models/dataModel.EnergyCIM/master/AsynchronousMachineEquivalentCircuit/schema.json&email=info@smartdatamodels.org) of NGSI-LD normalized payloads compliant with this data model. Refresh for new values

Link to the [Generator](https://smartdatamodels.org/extra/ngsi-ld_generator_keyvalues.php?schemaUrl=https://raw.githubusercontent.com/smart-data-models/dataModel.EnergyCIM/master/AsynchronousMachineEquivalentCircuit/schema.json&email=info@smartdatamodels.org) of NGSI-LD keyvalues payloads compliant with this data model. Refresh for new values

Link to the [Generator](https://smartdatamodels.org/extra/geojson_features_generator.php?schemaUrl=https://raw.githubusercontent.com/smart-data-models/dataModel.EnergyCIM/master/AsynchronousMachineEquivalentCircuit/schema.json&email=info@smartdatamodels.org) of geojson feature format payloads compliant with this data model. Refresh for new values
### PostgreSQL schema

Link to the [PostgreSQL schema](https://smart-data-models.github.io/dataModel.EnergyCIM/AsynchronousMachineEquivalentCircuit/schema.sql) of this data model
### Contribution

 If you have any issue on this data model you can raise an [issue](https://github.com/smart-data-models/dataModel.EnergyCIM/issues)  or contribute with a [PR](https://github.com/smart-data-models/dataModel.EnergyCIM/pulls)

 If you wish to develop your own data model you can start from [contribution manual](https://bit.ly/contribution_manual). Several services have been developed to help with: 
 - [Test data model repository](https://smartdatamodels.org/index.php/data-models-contribution-api/) including the schema and example payloads, etc
 - [Generate PostgreSQL schema](https://smartdatamodels.org/index.php/sql-service/) to help create a table, create type, etc