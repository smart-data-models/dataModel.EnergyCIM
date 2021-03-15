Entity: ProprietaryParameterDynamics  
====================================  
[Open License](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ProprietaryParameterDynamics/LICENSE.md)  
Global description: **Adapted from CIM data models. Supports definition of one or more parameters of several different datatypes for use by proprietary user-defined models.  NOTE: This class does not inherit from IdentifiedObject since it is not intended that a single instance of it be referenced by more than one proprietary user-defined model instance.**  

## List of properties  

- `AsynchronousMachineUserDefined`: Proprietary user-defined model with which this parameter is associated. Default: None  - `DiscontinuousExcitationControlUserDefined`: Proprietary user-defined model with which this parameter is associated. Default: None  - `ExcitationSystemUserDefined`: Proprietary user-defined model with which this parameter is associated. Default: None  - `LoadUserDefined`: Proprietary user-defined model with which this parameter is associated. Default: None  - `MechanicalLoadUserDefined`: Proprietary user-defined model with which this parameter is associated. Default: None  - `OverexcitationLimiterUserDefined`: Proprietary user-defined model with which this parameter is associated. Default: None  - `PFVArControllerType1UserDefined`: Proprietary user-defined model with which this parameter is associated. Default: None  - `PFVArControllerType2UserDefined`: Proprietary user-defined model with which this parameter is associated. Default: None  - `PowerSystemStabilizerUserDefined`: Proprietary user-defined model with which this parameter is associated. Default: None  - `SynchronousMachineUserDefined`: Proprietary user-defined model with which this parameter is associated. Default: None  - `TurbineGovernorUserDefined`: Proprietary user-defined model with which this parameter is associated. Default: None  - `TurbineLoadControllerUserDefined`: Proprietary user-defined model with which this parameter is associated. Default: None  - `UnderexcitationLimiterUserDefined`: Proprietary user-defined model with which this parameter is associated. Default: None  - `VoltageAdjusterUserDefined`: Proprietary user-defined model with which this parameter is associated. Default: None  - `VoltageCompensatorUserDefined`: Proprietary user-defined model with which this parameter is associated. Default: None  - `WindPlantUserDefined`: Proprietary user-defined model with which this parameter is associated. Default: None  - `WindType1or2UserDefined`: Proprietary user-defined model with which this parameter is associated. Default: None  - `WindType3or4UserDefined`: Proprietary user-defined model with which this parameter is associated. Default: None  - `address`: The mailing address  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided  - `booleanParameterValue`: Used for boolean parameter value. If this attribute is populated, integerParameterValue and floatParameterValue will not be. Default: False  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `floatParameterValue`: Used for floating point parameter value.  If this attribute is populated, booleanParameterValue and integerParameterValue will not be. Default: 0.0  - `id`: Unique identifier of the entity  - `integerParameterValue`: Used for integer parameter value.  If this attribute is populated, booleanParameterValue and floatParameterValue will not be. Default: 0  - `location`:   - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `parameterNumber`: Sequence number of the parameter among the set of parameters associated with the related proprietary user-defined model. Default: 0  - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `type`: NGSI type. It has to be ProprietaryParameterDynamics    
Required properties  
This data model is a direct conversion of the Common Information Model (CIM) specified by the IEC61970 standard into smart data models. The python classes this model is based on were developed by these entities Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) and RWTH University Aachen, Germany. some properties can have wrong type. This was the case, pelase raise an issue or send mail to alberto.abella@fiware.org  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ProprietaryParameterDynamics:    
  description: 'Adapted from CIM data models. Supports definition of one or more parameters of several different datatypes for use by proprietary user-defined models.  NOTE: This class does not inherit from IdentifiedObject since it is not intended that a single instance of it be referenced by more than one proprietary user-defined model instance.'    
  properties:    
    AsynchronousMachineUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    DiscontinuousExcitationControlUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ExcitationSystemUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    LoadUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    MechanicalLoadUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    OverexcitationLimiterUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    PFVArControllerType1UserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    PFVArControllerType2UserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    PowerSystemStabilizerUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    SynchronousMachineUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    TurbineGovernorUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    TurbineLoadControllerUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    UnderexcitationLimiterUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    VoltageAdjusterUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    VoltageCompensatorUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    WindPlantUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    WindType1or2UserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    WindType3or4UserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/areaServed'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/https://schema.org/postalCode'''    
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
    booleanParameterValue:    
      description: 'Used for boolean parameter value. If this attribute is populated, integerParameterValue and floatParameterValue will not be. Default: False'    
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
    floatParameterValue:    
      description: 'Used for floating point parameter value.  If this attribute is populated, booleanParameterValue and integerParameterValue will not be. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &proprietaryparameterdynamics_-_properties_-_owner_-_items_-_anyof    
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
    integerParameterValue:    
      description: 'Used for integer parameter value.  If this attribute is populated, booleanParameterValue and floatParameterValue will not be. Default: 0'    
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
        anyOf: *proprietaryparameterdynamics_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    parameterNumber:    
      description: 'Sequence number of the parameter among the set of parameters associated with the related proprietary user-defined model. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
      description: 'NGSI type. It has to be ProprietaryParameterDynamics'    
      enum:    
        - ProprietaryParameterDynamics    
      type: Property    
  required: []    
  type: object    
```  
</details>    
## Example payloads    
Not available the example of a ProprietaryParameterDynamics in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
Not available the example of a ProprietaryParameterDynamics in JSON format as normalized. This is compatible with NGSI V2 when not using options and returns the context data of an individual entity.  
Not available the example of a ProprietaryParameterDynamics in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
Not available the example of a ProprietaryParameterDynamics in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
