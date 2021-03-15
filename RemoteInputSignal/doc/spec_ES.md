Entidad: RemoteInputSignal  
==========================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/RemoteInputSignal/LICENSE.md)  
Descripción global: **Adaptado de los modelos de datos CIM. Admite la conexión a un terminal asociado a un bus remoto del que procede una señal de entrada de un tipo específico.**  

## Lista de propiedades  

- `DiscontinuousExcitationControlDynamics`: Modelo de control de la excitación discontinua mediante esta señal de entrada remota. Por defecto: Ninguno  - `PFVArControllerType1Dynamics`: Modelo de controlador de factor de potencia o VAr Tipo I que utiliza esta señal de entrada remota. Por defecto: Ninguno  - `PowerSystemStabilizerDynamics`: Modelo de estabilizador del sistema de potencia que utiliza esta señal de entrada remota. Por defecto: Ninguno  - `Terminal`: Terminal remoto al que se asocia esta señal de entrada. Por defecto: Ninguno  - `UnderexcitationLimiterDynamics`: Modelo de limitador de subexcitación que utiliza esta señal de entrada remota. Por defecto: Ninguno  - `VoltageCompensatorDynamics`: Modelo de compensador de tensión que utiliza esta señal de entrada remota. Por defecto: Ninguno  - `WindPlantDynamics`: La señal remota con la que está asociada esta central. Por defecto: Ninguno  - `WindTurbineType1or2Dynamics`: Modelo de generador eólico Tipo 1 o Tipo 2 que utiliza esta señal de entrada remota. Por defecto: Ninguno  - `WindTurbineType3or4Dynamics`: Señal de entrada remota utilizada por estos modelos de aerogeneradores Tipo 3 o 4. Por defecto: Ninguno  - `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `id`: Identificador único de la entidad  - `location`:   - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `remoteSignalType`: Tipo de señal de entrada. Por defecto: Ninguno  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `type`: Tipo NGSI. Tiene que ser RemoteInputSignal    
Propiedades requeridas  
Este modelo de datos es una conversión directa del Modelo de Información Común (CIM) especificado por la norma IEC61970 en modelos de datos inteligentes. Las clases de python en las que se basa este modelo fueron desarrolladas por estas entidades Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) y RWTH University Aachen, Alemania. algunas propiedades pueden tener un tipo incorrecto. Este es el caso, por favor, plantee un problema o envíe un correo a alberto.abella@fiware.org  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
RemoteInputSignal:    
  description: 'Adapted from CIM data models. Supports connection to a terminal associated with a remote bus from which an input signal of a specific type is coming.'    
  properties:    
    DiscontinuousExcitationControlDynamics:    
      description: 'Discontinuous excitation control model using this remote input signal. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    PFVArControllerType1Dynamics:    
      description: 'Power Factor or VAr controller Type I model using this remote input signal. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    PowerSystemStabilizerDynamics:    
      description: 'Power system stabilizer model using this remote input signal. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    Terminal:    
      description: 'Remote terminal with which this input signal is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    UnderexcitationLimiterDynamics:    
      description: 'Underexcitation limiter model using this remote input signal. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    VoltageCompensatorDynamics:    
      description: 'Voltage compensator model using this remote input signal. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    WindPlantDynamics:    
      description: 'The remote signal with which this power plant is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    WindTurbineType1or2Dynamics:    
      description: 'Wind generator Type 1 or Type 2 model using this remote input signal. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    WindTurbineType3or4Dynamics:    
      description: 'Remote input signal used by these wind turbine Type 3 or 4 models. Default: None'    
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
    id:    
      anyOf: &remoteinputsignal_-_properties_-_owner_-_items_-_anyof    
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
        anyOf: *remoteinputsignal_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    remoteSignalType:    
      description: 'Type of input signal. Default: None'    
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
      description: 'NGSI type. It has to be RemoteInputSignal'    
      enum:    
        - RemoteInputSignal    
      type: Property    
  required: []    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
No está disponible el ejemplo de una RemoteInputSignal en formato JSON como key-values. Esto es compatible con NGSI V2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de una RemoteInputSignal en formato JSON como normalizado. Esto es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de una RemoteInputSignal en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de una RemoteInputSignal en formato JSON-LD como normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
