Entidad: WindPlantFreqPcontrolIEC  
=================================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/WindPlantFreqPcontrolIEC/LICENSE.md)  
Descripción global: **Adaptado de los modelos de datos CIM. Modelo de controlador de frecuencia y potencia activa.  Referencia: Norma IEC 61400-27-1 Anexo E.**  

## Lista de propiedades  

- `WindDynamicsLookupTable`: El modelo de control de la planta eólica de frecuencia y potencia activa con el que se asocia esta tabla de búsqueda de dinámica eólica. Por defecto: 'list'  - `WindPlantIEC`: Modelo de planta eólica al que se asocia este control de frecuencia y potencia activa de la planta eólica. Por defecto: Ninguno  - `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `dprefmax`: Tasa de rampa máxima de solicitud del controlador de la planta a los aerogeneradores (). Es un parámetro que depende del proyecto. Por defecto: 0,0  - `dprefmin`: Tasa de rampa mínima (negativa) de solicitud del controlador de la planta a los aerogeneradores (). Es un parámetro que depende del proyecto. Por defecto: 0,0  - `id`: Identificador único de la entidad  - `kiwpp`: Ganancia integral del controlador de la planta P (). Es un parámetro dependiente del tipo. Por defecto: 0,0  - `kpwpp`: Ganancia proporcional del controlador de la planta P (). Es un parámetro dependiente del tipo. Por defecto: 0,0  - `location`:   - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `prefmax`: Petición máxima del controlador de la planta a los aerogeneradores (). Es un parámetro que depende del tipo. Por defecto: 0,0  - `prefmin`: Petición mínima del controlador de la planta a los aerogeneradores (). Es un parámetro que depende del tipo. Por defecto: 0,0  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `tpft`: Constante de tiempo de espera en la función de transferencia del valor de referencia (). Es un parámetro dependiente del tipo. Por defecto: 0  - `tpfv`: Constante de tiempo de retraso en la función de transferencia del valor de referencia (). Es un parámetro dependiente del tipo. Por defecto: 0  - `twpffilt`: Constante de tiempo del filtro para la medición de la frecuencia (). Es un parámetro que depende del tipo. Por defecto: 0  - `twppfilt`: Constante de tiempo del filtro para la medición de la potencia activa (). Es un parámetro que depende del tipo. Por defecto: 0  - `type`: Tipo NGSI. Debe ser WindPlantFreqPcontrolIEC    
Propiedades requeridas  
Este modelo de datos es una conversión directa del Modelo de Información Común (CIM) especificado por la norma IEC61970 en modelos de datos inteligentes. Las clases de python en las que se basa este modelo fueron desarrolladas por estas entidades Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) y RWTH University Aachen, Alemania. algunas propiedades pueden tener un tipo incorrecto. Este es el caso, por favor, plantee un problema o envíe un correo a alberto.abella@fiware.org  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WindPlantFreqPcontrolIEC:    
  description: 'Adapted from CIM data models. Frequency and active power controller model.  Reference: IEC Standard 61400-27-1 Annex E.'    
  properties:    
    WindDynamicsLookupTable:    
      description: 'The frequency and active power wind plant control model with which this wind dynamics lookup table is associated. Default: ''list'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    WindPlantIEC:    
      description: 'Wind plant model with which this wind plant frequency and active power control is associated. Default: None'    
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
    dprefmax:    
      description: 'Maximum ramp rate of  request from the plant controller to the wind turbines (). It is project dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    dprefmin:    
      description: 'Minimum (negative) ramp rate of  request from the plant controller to the wind turbines (). It is project dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &windplantfreqpcontroliec_-_properties_-_owner_-_items_-_anyof    
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
    kiwpp:    
      description: 'Plant P controller integral gain (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kpwpp:    
      description: 'Plant P controller proportional gain (). It is type dependent parameter. Default: 0.0'    
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
        anyOf: *windplantfreqpcontroliec_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    prefmax:    
      description: 'Maximum  request from the plant controller to the wind turbines (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    prefmin:    
      description: 'Minimum  request from the plant controller to the wind turbines (). It is type dependent parameter. Default: 0.0'    
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
    tpft:    
      description: 'Lead time constant in reference value transfer function (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tpfv:    
      description: 'Lag time constant in reference value transfer function (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    twpffilt:    
      description: 'Filter time constant for frequency measurement (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    twppfilt:    
      description: 'Filter time constant for active power measurement (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be WindPlantFreqPcontrolIEC'    
      enum:    
        - WindPlantFreqPcontrolIEC    
      type: Property    
  required: []    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
No está disponible el ejemplo de un WindPlantFreqPcontrolIEC en formato JSON como key-values. Esto es compatible con NGSI V2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un WindPlantFreqPcontrolIEC en formato JSON como normalizado. Esto es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un WindPlantFreqPcontrolIEC en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un WindPlantFreqPcontrolIEC en formato JSON-LD como normalizado. Es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
