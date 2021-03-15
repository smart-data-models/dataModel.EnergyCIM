Entidad: WindPlantReactiveControlIEC  
====================================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/WindPlantReactiveControlIEC/LICENSE.md)  
Descripción global: **Adaptado de los modelos de datos de la CIM. Modelo simplificado de control de la tensión y la potencia reactiva de la planta para su uso con modelos de aerogeneradores de tipo 3 y 4.  Referencia: Norma IEC 61400-27-1 Anexo E.**  

## Lista de propiedades  

- `WindPlantIEC`: Modelo de planta eólica al que se asocia este control reactivo del viento. Por defecto: Ninguno  - `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `id`: Identificador único de la entidad  - `kiwpx`: Ganancia integral del controlador Q de la planta (). Es un parámetro dependiente del tipo. Por defecto: 0.0  - `kpwpx`: Ganancia proporcional del controlador Q de la planta (). Es un parámetro dependiente del tipo. Por defecto: 0,0  - `kwpqu`: Estatismo de control de la tensión de la planta (). Es un parámetro que depende del proyecto. Por defecto: 0,0  - `location`:   - `mwppf`: Selector de modos de control del factor de potencia (). Sólo se utiliza si mwpu está ajustado a false. true = 1: control del factor de potencia false = 0: control de la potencia reactiva. Es un parámetro que depende del proyecto. Por defecto: Falso  - `mwpu`: Selector de modos de control de potencia reactiva (). verdadero = 1: control de tensión falso = 0: control de potencia reactiva. Es un parámetro que depende del proyecto. Por defecto: Falso  - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `twppfilt`: Constante de tiempo del filtro para la medición de la potencia activa (). Es un parámetro que depende del tipo. Por defecto: 0  - `twpqfilt`: Constante de tiempo del filtro para la medición de la potencia reactiva (). Es un parámetro que depende del tipo. Por defecto: 0  - `twpufilt`: Constante de tiempo del filtro para la medición de la tensión (). Es un parámetro que depende del tipo. Por defecto: 0  - `txft`: Constante de tiempo de espera en la función de transferencia del valor de referencia (). Es un parámetro dependiente del tipo. Por defecto: 0  - `txfv`: Constante de tiempo de retraso en la función de transferencia del valor de referencia (). Es un parámetro dependiente del tipo. Por defecto: 0  - `type`: Tipo NGSI. Debe ser WindPlantReactiveControlIEC  - `uwpqdip`: Umbral de tensión para la detección de LVRT en el control q (). Es un parámetro dependiente del tipo. Por defecto: 0,0  - `xrefmax`: Petición máxima ( o delta ) del controlador de la planta (). Es un parámetro que depende del proyecto. Por defecto: 0,0  - `xrefmin`: Petición mínima ( o delta) del controlador de la planta (). Es un parámetro que depende del proyecto. Por defecto: 0,0    
Propiedades requeridas  
Este modelo de datos es una conversión directa del Modelo de Información Común (CIM) especificado por la norma IEC61970 en modelos de datos inteligentes. Las clases de python en las que se basa este modelo fueron desarrolladas por estas entidades Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) y RWTH University Aachen, Alemania. algunas propiedades pueden tener un tipo incorrecto. Este es el caso, por favor, plantee un problema o envíe un correo a alberto.abella@fiware.org  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WindPlantReactiveControlIEC:    
  description: 'Adapted from CIM data models. Simplified plant voltage and reactive power control model for use with type 3 and type 4 wind turbine models.  Reference: IEC Standard 61400-27-1 Annex E.'    
  properties:    
    WindPlantIEC:    
      description: 'Wind plant model with which this wind reactive control is associated. Default: None'    
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
      anyOf: &windplantreactivecontroliec_-_properties_-_owner_-_items_-_anyof    
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
    kiwpx:    
      description: 'Plant Q controller integral gain (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kpwpx:    
      description: 'Plant Q controller proportional gain (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kwpqu:    
      description: 'Plant voltage control droop (). It is project dependent parameter. Default: 0.0'    
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
    mwppf:    
      description: 'Power factor control modes selector (). Used only if mwpu is set to false. true = 1: power factor control false = 0: reactive power control. It is project dependent parameter. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    mwpu:    
      description: 'Reactive power control modes selector (). true = 1: voltage control false = 0: reactive power control. It is project dependent parameter. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *windplantreactivecontroliec_-_properties_-_owner_-_items_-_anyof    
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
    twppfilt:    
      description: 'Filter time constant for active power measurement (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    twpqfilt:    
      description: 'Filter time constant for reactive power measurement (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    twpufilt:    
      description: 'Filter time constant for voltage measurement (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    txft:    
      description: 'Lead time constant in reference value transfer function (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    txfv:    
      description: 'Lag time constant in reference value transfer function (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be WindPlantReactiveControlIEC'    
      enum:    
        - WindPlantReactiveControlIEC    
      type: Property    
    uwpqdip:    
      description: 'Voltage threshold for LVRT detection in q control (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    xrefmax:    
      description: 'Maximum  ( or delta ) request from the plant controller (). It is project dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    xrefmin:    
      description: 'Minimum  ( or delta) request from the plant controller (). It is project dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
No está disponible el ejemplo de un WindPlantReactiveControlIEC en formato JSON como key-values. Esto es compatible con NGSI V2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un WindPlantReactiveControlIEC en formato JSON normalizado. Es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un WindPlantReactiveControlIEC en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un WindPlantReactiveControlIEC en formato JSON-LD como normalizado. Es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
