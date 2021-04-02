# Measurement

## Description 

Adapted from CIM data models. A Measurement represents any measured, calculated or non-measured non-calculated quantity. Any piece of equipment may contain Measurements, e.g. a substation may have temperature measurements and door open indications, a transformer may have oil temperature and tank pressure measurements, a bay may contain a number of power flow measurements and a Breaker may contain a switch status measurement.  The PSR - Measurement association is intended to capture this use of Measurement and is included in the naming hierarchy based on EquipmentContainer. The naming hierarchy typically has Measurements as leafs, e.g. Substation-VoltageLevel-Bay-Switch-Measurement. Some Measurements represent quantities related to a particular sensor location in the network, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is not captured in the PSR - Measurement association. Instead it is captured by the Measurement - Terminal association that is used to define the sensing location in the network topology. The location is defined by the connection of the Terminal to ConductingEquipment.  If both a Terminal and PSR are associated, and the PSR is of type ConductingEquipment, the associated Terminal should belong to that ConductingEquipment instance. When the sensor location is needed both Measurement-PSR and Measurement-Terminal are used. The Measurement-Terminal association is never used alone.
### Specification

Link to the [interactive specification](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.EnergyCIM/Measurement/swagger.yaml)

Link to the [specification](https://smart-data-models.github.io/dataModel.EnergyCIM/Measurement/doc/spec.md)

Link to the [specification in Spanish](https://smart-data-models.github.io/dataModel.EnergyCIM/Measurement/doc/spec_ES.md)

Link to the [specification in French](https://smart-data-models.github.io/dataModel.EnergyCIM/Measurement/doc/spec_FR.md)
### Examples
### Dynamic Examples generation

Link to the [Generator](https://smartdatamodels.org/extra/ngsi-ld_generator_v0.91.php?schemaUrl=https://raw.githubusercontent.com/smart-data-models/dataModel.EnergyCIM/master/Measurement/schema.json&email=info@smartdatamodels.org) of NGSI-LD payloads compliant with this data model. Refresh for new values
### Contribution

 If you have any issue on this data model you can raise an [issue](https://github.com/smart-data-models/dataModel.EnergyCIM/issues)  or contribute with a [PR](https://github.com/smart-data-models/dataModel.EnergyCIM/pulls)