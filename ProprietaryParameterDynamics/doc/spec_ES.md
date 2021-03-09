Entidad: ProprietaryParameterDynamics  
=====================================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ProprietaryParameterDynamics/LICENSE.md)  
Descripción global: **Adaptado de los modelos de datos CIM. Admite la definición de uno o más parámetros de varios tipos de datos diferentes para su uso por modelos propietarios definidos por el usuario.  NOTA: Esta clase no hereda de IdentifiedObject porque no se pretende que una sola instancia de la misma sea referenciada por más de una instancia de modelo propietario definido por el usuario.**  

## Lista de propiedades  

- `AsynchronousMachineUserDefined`: Modelo propio definido por el usuario al que se asocia este parámetro. Por defecto: Ninguno  - `DiscontinuousExcitationControlUserDefined`: Modelo propio definido por el usuario al que se asocia este parámetro. Por defecto: Ninguno  - `ExcitationSystemUserDefined`: Modelo propio definido por el usuario al que se asocia este parámetro. Por defecto: Ninguno  - `LoadUserDefined`: Modelo propio definido por el usuario al que se asocia este parámetro. Por defecto: Ninguno  - `MechanicalLoadUserDefined`: Modelo propio definido por el usuario al que se asocia este parámetro. Por defecto: Ninguno  - `OverexcitationLimiterUserDefined`: Modelo propio definido por el usuario al que se asocia este parámetro. Por defecto: Ninguno  - `PFVArControllerType1UserDefined`: Modelo propio definido por el usuario al que se asocia este parámetro. Por defecto: Ninguno  - `PFVArControllerType2UserDefined`: Modelo propio definido por el usuario al que se asocia este parámetro. Por defecto: Ninguno  - `PowerSystemStabilizerUserDefined`: Modelo propio definido por el usuario al que se asocia este parámetro. Por defecto: Ninguno  - `SynchronousMachineUserDefined`: Modelo propio definido por el usuario al que se asocia este parámetro. Por defecto: Ninguno  - `TurbineGovernorUserDefined`: Modelo propio definido por el usuario al que se asocia este parámetro. Por defecto: Ninguno  - `TurbineLoadControllerUserDefined`: Modelo propio definido por el usuario al que se asocia este parámetro. Por defecto: Ninguno  - `UnderexcitationLimiterUserDefined`: Modelo propio definido por el usuario al que se asocia este parámetro. Por defecto: Ninguno  - `VoltageAdjusterUserDefined`: Modelo propio definido por el usuario al que se asocia este parámetro. Por defecto: Ninguno  - `VoltageCompensatorUserDefined`: Modelo propio definido por el usuario al que se asocia este parámetro. Por defecto: Ninguno  - `WindPlantUserDefined`: Modelo propio definido por el usuario al que se asocia este parámetro. Por defecto: Ninguno  - `WindType1or2UserDefined`: Modelo propio definido por el usuario al que se asocia este parámetro. Por defecto: Ninguno  - `WindType3or4UserDefined`: Modelo propio definido por el usuario al que se asocia este parámetro. Por defecto: Ninguno  - `address`: La dirección postal.  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `booleanParameterValue`: Se utiliza para el valor del parámetro booleano. Si este atributo está poblado, integerParameterValue y floatParameterValue no lo estarán. Por defecto: False  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `floatParameterValue`: Se utiliza para el valor del parámetro en coma flotante.  Si este atributo está poblado, booleanParameterValue y integerParameterValue no lo estarán. Por defecto: 0,0  - `id`: Identificador único de la entidad  - `integerParameterValue`: Se utiliza para el valor del parámetro entero.  Si este atributo está poblado, booleanParameterValue y floatParameterValue no lo estarán. Por defecto: 0  - `location`:   - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `parameterNumber`: Número de secuencia del parámetro entre el conjunto de parámetros asociados con el modelo propietario definido por el usuario relacionado. Por defecto: 0  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `type`: Tipo NGSI. Tiene que ser ProprietaryParameterDynamics    
Propiedades requeridas  
Este modelo de datos es una conversión directa del Modelo de Información Común (CIM) especificado por la norma IEC61970 en modelos de datos inteligentes. Las clases de python en las que se basa este modelo fueron desarrolladas por estas entidades Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) y RWTH University Aachen, Alemania. algunas propiedades pueden tener un tipo incorrecto. Este es el caso, por favor, plantee un problema o envíe un correo a alberto.abella@fiware.org  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
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
## Ejemplo de carga útil  
No está disponible el ejemplo de un ProprietaryParameterDynamics en formato JSON como key-values. Esto es compatible con NGSI V2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un ProprietaryParameterDynamics en formato JSON como normalizado. Esto es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un ProprietaryParameterDynamics en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un ProprietaryParameterDynamics en formato JSON-LD como normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
