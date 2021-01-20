Entity: PowerTransformer  
========================  
[Open License](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/PowerTransformer/LICENSE.md)  
Global description: **Adapted from CIM data models. An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow). A power transformer may be composed of separate transformer tanks that need not be identical. A power transformer can be modeled with or without tanks and is intended for use in both balanced and unbalanced representations.   A power transformer typically has two terminals, but may have one (grounding), three or more terminals. The inherited association ConductingEquipment.BaseVoltage should not be used.  The association from TransformerEnd to BaseVoltage should be used instead.**  

## List of properties  

- `PowerTransformerEnd`: The power transformer of this power transformer end. Default: "list"  - `address`: The mailing address.  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided  - `beforeShCircuitHighestOperatingCurrent`: The highest operating current (Ib in the IEC 60909-0) before short circuit (depends on network configuration and relevant reliability philosophy). It is used for calculation of the impedance correction factor KT defined in IEC 60909-0. Default: 0.0  - `beforeShCircuitHighestOperatingVoltage`: The highest operating voltage (Ub in the IEC 60909-0) before short circuit. It is used for calculation of the impedance correction factor KT defined in IEC 60909-0. This is worst case voltage on the low side winding (Section 3.7.1 in the standard). Used to define operating conditions. Default: 0.0  - `beforeShortCircuitAnglePf`: The angle of power factor before short circuit (phib in the IEC 60909-0). It is used for calculation of the impedance correction factor KT defined in IEC 60909-0. This is the worst case power factor. Used to define operating conditions. Default: 0.0  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `highSideMinOperatingU`: The minimum operating voltage (uQmin in the IEC 60909-0) at the high voltage side (Q side) of the unit transformer of the power station unit. A value well established from long-term operating experience of the system. It is used for calculation of the impedance correction factor KG defined in IEC 60909-0 Default: 0.0  - `id`: Unique identifier of the entity  - `isPartOfGeneratorUnit`: Indicates whether the machine is part of a power station unit. Used for short circuit data exchange according to IEC 60909 Default: False  - `location`:   - `name`: The name of this item.  - `operationalValuesConsidered`: It is used to define if the data (other attributes related to short circuit data exchange) defines long term operational conditions or not. Used for short circuit data exchange according to IEC 60909. Default: False  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `type`: NGSI type. It has to be PowerTransformer    
Required properties  
This data model is a direct conversion of the Common Information Model (CIM) specified by the IEC61970 standard into smart data models. The python classes this model is based on were developed by these entities Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) and RWTH University Aachen, Germany. some properties can have wrong type. This was the case, pelase raise an issue or send mail to alberto.abella@fiware.org  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PowerTransformer:    
  description: 'Adapted from CIM data models. An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow). A power transformer may be composed of separate transformer tanks that need not be identical. A power transformer can be modeled with or without tanks and is intended for use in both balanced and unbalanced representations.   A power transformer typically has two terminals, but may have one (grounding), three or more terminals. The inherited association ConductingEquipment.BaseVoltage should not be used.  The association from TransformerEnd to BaseVoltage should be used instead.'    
  properties:    
    PowerTransformerEnd:    
      description: 'The power transformer of this power transformer end. Default: "list"'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/Text'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/Text'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/Text'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/Text'''    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    beforeShCircuitHighestOperatingCurrent:    
      description: 'The highest operating current (Ib in the IEC 60909-0) before short circuit (depends on network configuration and relevant reliability philosophy). It is used for calculation of the impedance correction factor KT defined in IEC 60909-0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    beforeShCircuitHighestOperatingVoltage:    
      description: 'The highest operating voltage (Ub in the IEC 60909-0) before short circuit. It is used for calculation of the impedance correction factor KT defined in IEC 60909-0. This is worst case voltage on the low side winding (Section 3.7.1 in the standard). Used to define operating conditions. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    beforeShortCircuitAnglePf:    
      description: 'The angle of power factor before short circuit (phib in the IEC 60909-0). It is used for calculation of the impedance correction factor KT defined in IEC 60909-0. This is the worst case power factor. Used to define operating conditions. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    highSideMinOperatingU:    
      description: 'The minimum operating voltage (uQmin in the IEC 60909-0) at the high voltage side (Q side) of the unit transformer of the power station unit. A value well established from long-term operating experience of the system. It is used for calculation of the impedance correction factor KG defined in IEC 60909-0 Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &powertransformer_-_properties_-_owner_-_items_-_anyof    
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
    isPartOfGeneratorUnit:    
      description: 'Indicates whether the machine is part of a power station unit. Used for short circuit data exchange according to IEC 60909 Default: False'    
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
    operationalValuesConsidered:    
      description: 'It is used to define if the data (other attributes related to short circuit data exchange) defines long term operational conditions or not. Used for short circuit data exchange according to IEC 60909. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *powertransformer_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI type. It has to be PowerTransformer'    
      enum:    
        - PowerTransformer    
      type: Property    
  required: []    
  type: object    
```  
</details>    
## Example payloads    
Not available the example of a PowerTransformer in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
Not available the example of a PowerTransformer in JSON format as normalized. This is compatible with NGSI V2 when not using options and returns the context data of an individual entity.  
Not available the example of a PowerTransformer in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
Not available the example of a PowerTransformer in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
