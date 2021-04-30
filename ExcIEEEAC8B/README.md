# ExcIEEEAC8B

## Description 

Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type AC8B model. This model represents a PID voltage regulator with either a brushless exciter or dc exciter. The AVR in this model consists of PID control, with separate constants for the proportional (), integral (), and derivative () gains. The representation of the brushless exciter (, , , , ) is similar to the model Type AC2A. The Type AC8B model can be used to represent static voltage regulators applied to brushless excitation systems. Digitally based voltage regulators feeding dc rotating main exciters can be represented with the AC Type AC8B model with the parameters  and  set to 0.  For thyristor power stages fed from the generator terminals, the limits  and  should be a function of terminal voltage:  * and  * .     Reference: IEEE Standard 421.5-2005 Section 6.8.
### Specification

Link to the [interactive specification](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.EnergyCIM/ExcIEEEAC8B/swagger.yaml)

Link to the [specification](https://smart-data-models.github.io/dataModel.EnergyCIM/ExcIEEEAC8B/doc/spec.md)

Link to the [specification in Spanish](https://smart-data-models.github.io/dataModel.EnergyCIM/ExcIEEEAC8B/doc/spec_ES.md)

Link to the [specification in French](https://smart-data-models.github.io/dataModel.EnergyCIM/ExcIEEEAC8B/doc/spec_FR.md)

Link to the [specification in German](https://smart-data-models.github.io/dataModel.EnergyCIM/ExcIEEEAC8B/doc/spec_DE.md)
### Examples
### Dynamic Examples generation

Link to the [Generator](https://smartdatamodels.org/extra/ngsi-ld_generator_v0.92.php?schemaUrl=https://raw.githubusercontent.com/smart-data-models/dataModel.EnergyCIM/master/ExcIEEEAC8B/schema.json&email=info@smartdatamodels.org) of NGSI-LD normalized payloads compliant with this data model. Refresh for new values

Link to the [Generator](https://smartdatamodels.org/extra/ngsi-ld_generator_keyvalues_v0.92.php?schemaUrl=https://raw.githubusercontent.com/smart-data-models/dataModel.EnergyCIM/master/ExcIEEEAC8B/schema.json&email=info@smartdatamodels.org) of NGSI-LD keyvalues payloads compliant with this data model. Refresh for new values
### Contribution

 If you have any issue on this data model you can raise an [issue](https://github.com/smart-data-models/dataModel.EnergyCIM/issues)  or contribute with a [PR](https://github.com/smart-data-models/dataModel.EnergyCIM/pulls)