Entidad: Calidad61850  
=====================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/Quality61850/LICENSE.md)  
Descripción global: **Adaptado de los modelos de datos CIM. Los indicadores de calidad de esta clase son los definidos en la norma IEC 61850, a excepción de estimatorReplaced, que se ha incluido en esta clase por comodidad.**  

## Lista de propiedades  

- `address`: La dirección postal.  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `badReference`: El valor de la medición puede ser incorrecto debido a que la referencia está descalibrada. Por defecto: Falso  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `estimatorReplaced`: El valor ha sido sustituido por el Estimador de Estado. estimatorReplaced no es un bit de calidad IEC61850 pero se ha puesto en esta clase por comodidad. Por defecto: Falso  - `failure`: Este identificador indica que una función de supervisión ha detectado un fallo interno o externo, por ejemplo, un fallo de comunicación. Por defecto: Falso  - `id`: Identificador único de la entidad  - `location`:   - `name`: El nombre de este artículo.  - `oldData`: El valor de la medición es antiguo y posiblemente no válido, ya que no se ha actualizado con éxito durante un intervalo de tiempo especificado. Por defecto: Falso  - `operatorBlocked`: El valor de la medición está bloqueado y, por tanto, no está disponible para su transmisión. Por defecto: Falso  - `oscillatory`: Para evitar una sobrecarga de la comunicación, es conveniente detectar y suprimir las entradas binarias oscilantes (que cambian rápidamente). Si una señal cambia en un tiempo definido (tosc) dos veces en la misma dirección (de 0 a 1 o de 1 a 0), se detecta la oscilación y se establece el identificador de calidad de detalle "oscilatorio". Si se detecta un número configurado de cambios transitorios puede pasar. En este tiempo se establece el estado de validez "cuestionable". Si después de este número definido de cambios la señal sigue en estado oscilante, el valor se establecerá en el estado opuesto al valor estable anterior o en un valor predeterminado definido. En este caso, el estado de validez `cuestionable` se restablece y se establece `invalido` mientras la señal esté oscilando. Si se configura de forma que no se produzcan cambios transitorios, se establece inmediatamente el estado de validez `inválido` además del identificador de calidad de detalle `oscilante` (utilizado sólo para información de estado). Por defecto: Falso  - `outOfRange`: El valor de la medición está más allá de un rango de valor predefinido. Por defecto: Falso  - `overFlow`: El valor de la medida está más allá de la capacidad de ser representado correctamente. Por ejemplo, el valor de un contador se desborda desde el recuento máximo hasta un valor de cero. Por defecto: Falso  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: La fuente da información relacionada con el origen de un valor. El valor puede ser adquirido del proceso, por defecto o sustituido. Por defecto: Ninguno  - `suspect`: Una función de correlación ha detectado que el valor no es consitente con otros valores. Típicamente se establece por un Estimador de Estado de la red. Por defecto: Falso  - `test`: El valor de la medición se transmite con fines de prueba. Por defecto: Falso  - `type`: Tipo NGSI. Tiene que ser Quality61850  - `validity`: Validez del valor de medición. Por defecto: Ninguno    
Propiedades requeridas  
Este modelo de datos es una conversión directa del Modelo de Información Común (CIM) especificado por la norma IEC61970 en modelos de datos inteligentes. Las clases de python en las que se basa este modelo fueron desarrolladas por estas entidades Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) y RWTH University Aachen, Alemania. algunas propiedades pueden tener un tipo incorrecto. Este es el caso, por favor, plantee un problema o envíe un correo a alberto.abella@fiware.org  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Quality61850:    
  description: 'Adapted from CIM data models. Quality flags in this class are as defined in IEC 61850, except for estimatorReplaced, which has been included in this class for convenience.'    
  properties:    
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
    badReference:    
      description: 'Measurement value may be incorrect due to a reference being out of calibration. Default: False'    
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
    estimatorReplaced:    
      description: 'Value has been replaced by State Estimator. estimatorReplaced is not an IEC61850 quality bit but has been put in this class for convenience. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    failure:    
      description: 'This identifier indicates that a supervision function has detected an internal or external failure, e.g. communication failure. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &quality61850_-_properties_-_owner_-_items_-_anyof    
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
    oldData:    
      description: 'Measurement value is old and possibly invalid, as it has not been successfully updated during a specified time interval. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    operatorBlocked:    
      description: 'Measurement value is blocked and hence unavailable for transmission. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    oscillatory:    
      description: 'To prevent some overload of the communication it is sensible to detect and suppress oscillating (fast changing) binary inputs. If a signal changes in a defined time (tosc) twice in the same direction (from 0 to 1 or from 1 to 0) then oscillation is detected and the detail quality identifier `oscillatory` is set. If it is detected a configured numbers of transient changes could be passed by. In this time the validity status `questionable` is set. If after this defined numbers of changes the signal is still in the oscillating state the value shall be set either to the opposite state of the previous stable value or to a defined default value. In this case the validity status `questionable` is reset and `invalid` is set as long as the signal is oscillating. If it is configured such that no transient changes should be passed by then the validity status `invalid` is set immediately in addition to the detail quality identifier `oscillatory` (used for status information only). Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    outOfRange:    
      description: 'Measurement value is beyond a predefined range of value. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    overFlow:    
      description: 'Measurement value is beyond the capability of being  represented properly. For example, a counter value overflows from maximum count back to a value of zero. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *quality61850_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Source gives information related to the origin of a value. The value may be acquired from the process, defaulted or substituted. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    suspect:    
      description: 'A correlation function has detected that the value is not consitent with other values. Typically set by a network State Estimator. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    test:    
      description: 'Measurement value is transmitted for test purposes. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be Quality61850'    
      enum:    
        - Quality61850    
      type: Property    
    validity:    
      description: 'Validity of the measurement value. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
No está disponible el ejemplo de un Quality61850 en formato JSON como key-values. Esto es compatible con NGSI V2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un Quality61850 en formato JSON como normalizado. Esto es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un Quality61850 en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un Quality61850 en formato JSON-LD como normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
