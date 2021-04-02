# AsynchronousMachineEquivalentCircuit

## Description 

Adapted from CIM data models. The electrical equations of all variations of the asynchronous model are based on the AsynchronousEquivalentCircuit diagram for the direct and quadrature axes, with two equivalent rotor windings in each axis.      =  +   =  +  *  / ( + )  =  +  * *  / ( *  +  *  +  * )  = ( + ) / ( * )  = ( *  +  *  +  * ) / ( *  * (+ ) Same equations using CIM attributes from AsynchronousMachineTimeConstantReactance class on left of = sign and AsynchronousMachineEquivalentCircuit class on right (except as noted): xs = xm + RotatingMachineDynamics.statorLeakageReactance xp = RotatingMachineDynamics.statorLeakageReactance + xm * xlr1 / (xm + xlr1) xpp = RotatingMachineDynamics.statorLeakageReactance + xm * xlr1* xlr2 / (xm * xlr1 + xm * xlr2 + xlr1 * xlr2) tpo = (xm + xlr1) / (2*pi*nominal frequency * rr1) tppo = (xm * xlr1 + xm * xlr2 + xlr1 * xlr2) / (2*pi*nominal frequency * rr2 * (xm + xlr1).
### Specification

Link to the [interactive specification](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.EnergyCIM/AsynchronousMachineEquivalentCircuit/swagger.yaml)

Link to the [specification](https://smart-data-models.github.io/dataModel.EnergyCIM/AsynchronousMachineEquivalentCircuit/doc/spec.md)

Link to the [specification in Spanish](https://smart-data-models.github.io/dataModel.EnergyCIM/AsynchronousMachineEquivalentCircuit/doc/spec_ES.md)

Link to the [specification in French](https://smart-data-models.github.io/dataModel.EnergyCIM/AsynchronousMachineEquivalentCircuit/doc/spec_FR.md)
### Examples
### Dynamic Examples generation

Link to the [Generator](https://smartdatamodels.org/extra/ngsi-ld_generator_v0.91.php?schemaUrl=https://raw.githubusercontent.com/smart-data-models/dataModel.EnergyCIM/master/AsynchronousMachineEquivalentCircuit/schema.json&email=info@smartdatamodels.org) of NGSI-LD payloads compliant with this data model. Refresh for new values
### Contribution

 If you have any issue on this data model you can raise an [issue](https://github.com/smart-data-models/dataModel.EnergyCIM/issues)  or contribute with a [PR](https://github.com/smart-data-models/dataModel.EnergyCIM/pulls)