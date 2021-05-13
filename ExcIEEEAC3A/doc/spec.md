Entity: ExcIEEEAC3A  
===================  
[Open License](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExcIEEEAC3A/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type AC3A model. The model represents the field-controlled alternator-rectifier excitation systems designated Type AC3A. These excitation systems include an alternator main exciter with non-controlled rectifiers. The exciter employs self-excitation, and the voltage regulator power is derived from the exciter output voltage.  Therefore, this system has an additional nonlinearity, simulated by the use of a multiplier whose inputs are the voltage regulator command signal, , and the exciter output voltage, , times .  This model is applicable to excitation systems employing static voltage regulators.   Reference: IEEE Standard 421.5-2005 Section 6.3.**  

## List of properties  

- `address`: The mailing address  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `efdn`: Value of at which feedback gain changes (E).  Typical Value = 2.36. Default: 0.0  - `id`: Unique identifier of the entity  - `ka`: Voltage regulator gain (K).  Typical Value = 45.62. Default: 0.0  - `kc`: Rectifier loading factor proportional to commutating reactance (K).  Typical Value = 0.104. Default: 0.0  - `kd`: Demagnetizing factor, a function of exciter alternator reactances (K).  Typical Value = 0.499. Default: 0.0  - `ke`: Exciter constant related to self-excited field (K).  Typical Value = 1. Default: 0.0  - `kf`: Excitation control system stabilizer gains (K).  Typical Value = 0.143. Default: 0.0  - `kn`: Excitation control system stabilizer gain (K).  Typical Value = 0.05. Default: 0.0  - `kr`: Constant associated with regulator and alternator field power supply (K).  Typical Value = 3.77. Default: 0.0  - `location`:   - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso`: list of uri pointing to additional resources about the item  - `seve1`: Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance (S[V]).  Typical Value = 1.143. Default: 0.0  - `seve2`: Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance (S[V]).  Typical Value = 0.1. Default: 0.0  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `ta`: Voltage regulator time constant (T).  Typical Value = 0.013. Default: 0  - `tb`: Voltage regulator time constant (T).  Typical Value = 0. Default: 0  - `tc`: Voltage regulator time constant (T).  Typical Value = 0. Default: 0  - `te`: Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 1.17. Default: 0  - `tf`: Excitation control system stabilizer time constant (T).  Typical Value = 1. Default: 0  - `type`: NGSI type. It has to be ExcIEEEAC3A  - `vamax`: Maximum voltage regulator output (V).  Typical Value = 1. Default: 0.0  - `vamin`: Minimum voltage regulator output (V).  Typical Value = -0.95. Default: 0.0  - `ve1`: Exciter alternator output voltages back of commutating reactance at which saturation is defined (V) equals V(V).  Typical Value = 6.24. Default: 0.0  - `ve2`: Exciter alternator output voltages back of commutating reactance at which saturation is defined (V).  Typical Value = 4.68. Default: 0.0  - `vemin`: Minimum exciter voltage output (V).  Typical Value = 0.1. Default: 0.0  - `vfemax`: Exciter field current limit reference (V).  Typical Value = 16. Default: 0.0    
Required properties  
Adapted from CIM data models and CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). This data model is a direct conversion of the Common Information Model (CIM) specified by the IEC61970 standard into smart data models. The python classes this model is based on were developed by these entities Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) and RWTH University Aachen, Germany. Some properties can have wrong type. This was the case, please raise an issue or send mail to info@smartdatamodels.org.  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ExcIEEEAC3A:    
  description: 'Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type AC3A model. The model represents the field-controlled alternator-rectifier excitation systems designated Type AC3A. These excitation systems include an alternator main exciter with non-controlled rectifiers. The exciter employs self-excitation, and the voltage regulator power is derived from the exciter output voltage.  Therefore, this system has an additional nonlinearity, simulated by the use of a multiplier whose inputs are the voltage regulator command signal, , and the exciter output voltage, , times .  This model is applicable to excitation systems employing static voltage regulators.   Reference: IEEE Standard 421.5-2005 Section 6.3.'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    efdn:    
      description: 'Value of at which feedback gain changes (E).  Typical Value = 2.36. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &excieeeac3a_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      type: Property    
    ka:    
      description: 'Voltage regulator gain (K).  Typical Value = 45.62. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kc:    
      description: 'Rectifier loading factor proportional to commutating reactance (K).  Typical Value = 0.104. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kd:    
      description: 'Demagnetizing factor, a function of exciter alternator reactances (K).  Typical Value = 0.499. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ke:    
      description: 'Exciter constant related to self-excited field (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kf:    
      description: 'Excitation control system stabilizer gains (K).  Typical Value = 0.143. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kn:    
      description: 'Excitation control system stabilizer gain (K).  Typical Value = 0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kr:    
      description: 'Constant associated with regulator and alternator field power supply (K).  Typical Value = 3.77. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      title: 'GeoJSON Geometry'    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *excieeeac3a_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    seve1:    
      description: 'Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance (S[V]).  Typical Value = 1.143. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    seve2:    
      description: 'Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance (S[V]).  Typical Value = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    ta:    
      description: 'Voltage regulator time constant (T).  Typical Value = 0.013. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tb:    
      description: 'Voltage regulator time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tc:    
      description: 'Voltage regulator time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    te:    
      description: 'Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 1.17. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tf:    
      description: 'Excitation control system stabilizer time constant (T).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be ExcIEEEAC3A'    
      enum:    
        - ExcIEEEAC3A    
      type: Property    
    vamax:    
      description: 'Maximum voltage regulator output (V).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vamin:    
      description: 'Minimum voltage regulator output (V).  Typical Value = -0.95. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ve1:    
      description: 'Exciter alternator output voltages back of commutating reactance at which saturation is defined (V) equals V(V).  Typical Value = 6.24. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ve2:    
      description: 'Exciter alternator output voltages back of commutating reactance at which saturation is defined (V).  Typical Value = 4.68. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vemin:    
      description: 'Minimum exciter voltage output (V).  Typical Value = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vfemax:    
      description: 'Exciter field current limit reference (V).  Typical Value = 16. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Example payloads    
Not available the example of a ExcIEEEAC3A in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
Not available the example of a ExcIEEEAC3A in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
Not available the example of a ExcIEEEAC3A in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
Not available the example of a ExcIEEEAC3A in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
