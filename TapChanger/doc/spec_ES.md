Entidad: TapChanger  
===================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/TapChanger/LICENSE.md)  
Descripción global: **Adaptado de los modelos de datos CIM. Mecanismo para cambiar las posiciones de las tomas del devanado del transformador.**  

## Lista de propiedades  

- `SvTapStep`: El estado del paso de toma asociado al cambiador de tomas. Por defecto: Ninguno  - `TapChangerControl`: Los cambiadores de tomas que participan en este esquema de control de tomas reguladoras. Por defecto: Ninguno  - `TapSchedules`: Un TapSchedule está asociado a un TapChanger. Por defecto: 'list'  - `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `controlEnabled`: Especifica el estado de regulación del equipo.  Verdadero es regulación, falso es no regulación. Por defecto: Falso  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `highStep`: La posición más alta posible del paso de rosca, avance desde el punto neutro. El atributo debe ser mayor que lowStep. Por defecto: 0  - `id`: Identificador único de la entidad  - `location`:   - `lowStep`: Posición de paso de toma más baja posible, retardo desde el punto muerto Predeterminado: 0  - `ltcFlag`: Especifica si un TapChanger tiene o no capacidad de cambio de tomas de carga. Por defecto: Falso  - `name`: El nombre de este artículo.  - `neutralStep`: La posición de paso de la toma neutra para este devanado. El atributo debe ser igual o mayor que lowStep e igual o menor que highStep. Por defecto: 0  - `neutralU`: Tensión a la que funciona el devanado en el ajuste de la toma neutra. Por defecto: 0,0  - `normalStep`: La posición del paso de toma utilizado en el funcionamiento `normal` de la red para este devanado. Para un cambiador de tomas fijo, indica la posición física actual de la toma. El atributo debe ser igual o mayor que lowStep e igual o menor que highStep. Por defecto: 0  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `step`: Posición del cambiador de tomas. Paso inicial para una solución de estado estacionario. Se permiten valores no enteros para soportar variables de toma continuas. Las razones para el valor continuo son apoyar los casos de estudio en los que aún no se han diseñado cambiadores de tomas discretos, una solución en la que una banda de tensión estrecha obliga al paso de la toma a oscilar o acomodar una solución continua como entrada. El atributo deberá ser igual o mayor que lowStep e igual o menor que highStep. Por defecto: 0.0  - `type`: Tipo de NGSI. Tiene que ser TapChanger    
Propiedades requeridas  
Este modelo de datos es una conversión directa del Modelo de Información Común (CIM) especificado por la norma IEC61970 en modelos de datos inteligentes. Las clases de python en las que se basa este modelo fueron desarrolladas por estas entidades Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) y RWTH University Aachen, Alemania. algunas propiedades pueden tener un tipo incorrecto. Este es el caso, por favor, plantee un problema o envíe un correo a alberto.abella@fiware.org  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
TapChanger:    
  description: 'Adapted from CIM data models. Mechanism for changing transformer winding tap positions.'    
  properties:    
    SvTapStep:    
      description: 'The tap step state associated with the tap changer. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    TapChangerControl:    
      description: 'The tap changers that participates in this regulating tap control scheme. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    TapSchedules:    
      description: 'A TapSchedule is associated with a TapChanger. Default: ''list'''    
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
    controlEnabled:    
      description: 'Specifies the regulation status of the equipment.  True is regulating, false is not regulating. Default: False'    
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
    highStep:    
      description: 'Highest possible tap step position, advance from neutral. The attribute shall be greater than lowStep. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &tapchanger_-_properties_-_owner_-_items_-_anyof    
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
    lowStep:    
      description: 'Lowest possible tap step position, retard from neutral Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ltcFlag:    
      description: 'Specifies whether or not a TapChanger has load tap changing capabilities. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    name:    
      description: 'The name of this item.'    
      type: Property    
    neutralStep:    
      description: 'The neutral tap step position for this winding. The attribute shall be equal or greater than lowStep and equal or less than highStep. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    neutralU:    
      description: 'Voltage at which the winding operates at the neutral tap setting. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    normalStep:    
      description: 'The tap step position used in `normal` network operation for this winding. For a `Fixed` tap changer indicates the current physical tap setting. The attribute shall be equal or greater than lowStep and equal or less than highStep. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *tapchanger_-_properties_-_owner_-_items_-_anyof    
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
    step:    
      description: 'Tap changer position. Starting step for a steady state solution. Non integer values are allowed to support continuous tap variables. The reasons for continuous value are to support study cases where no discrete tap changers has yet been designed, a solutions where a narrow voltage band force the tap step to oscillate or accommodate for a continuous solution as input. The attribute shall be equal or greater than lowStep and equal or less than highStep. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be TapChanger'    
      enum:    
        - TapChanger    
      type: Property    
  required: []    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
No está disponible el ejemplo de un TapChanger en formato JSON como key-values. Esto es compatible con NGSI V2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un TapChanger en formato JSON como normalizado. Esto es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un TapChanger en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un TapChanger en formato JSON-LD como normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
