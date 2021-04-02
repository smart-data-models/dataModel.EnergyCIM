# LoadResponseCharacteristic

## Description 

Adapted from CIM data models. Models the characteristic response of the load demand due to changes in system conditions such as voltage and frequency. This is not related to demand response.  If LoadResponseCharacteristic.exponentModel is True, the voltage exponents are specified and used as to calculate:  Active power component = Pnominal * (Voltage/cim:BaseVoltage.nominalVoltage) ** cim:LoadResponseCharacteristic.pVoltageExponent  Reactive power component = Qnominal * (Voltage/cim:BaseVoltage.nominalVoltage)** cim:LoadResponseCharacteristic.qVoltageExponent  Where  * means 'multiply' and ** is 'raised to power of'.
### Specification

Link to the [interactive specification](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.EnergyCIM/LoadResponseCharacteristic/swagger.yaml)

Link to the [specification](https://smart-data-models.github.io/dataModel.EnergyCIM/LoadResponseCharacteristic/doc/spec.md)

Link to the [specification in Spanish](https://smart-data-models.github.io/dataModel.EnergyCIM/LoadResponseCharacteristic/doc/spec_ES.md)

Link to the [specification in French](https://smart-data-models.github.io/dataModel.EnergyCIM/LoadResponseCharacteristic/doc/spec_FR.md)
### Examples
### Dynamic Examples generation

Link to the [Generator](https://smartdatamodels.org/extra/ngsi-ld_generator_v0.91.php?schemaUrl=https://raw.githubusercontent.com/smart-data-models/dataModel.EnergyCIM/master/LoadResponseCharacteristic/schema.json&email=info@smartdatamodels.org) of NGSI-LD payloads compliant with this data model. Refresh for new values
### Contribution

 If you have any issue on this data model you can raise an [issue](https://github.com/smart-data-models/dataModel.EnergyCIM/issues)  or contribute with a [PR](https://github.com/smart-data-models/dataModel.EnergyCIM/pulls)