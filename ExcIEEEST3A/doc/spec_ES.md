Entidad: ExcIEEEST3A  
====================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExcIEEEST3A/LICENSE.md)  
Descripción global: **Adaptado de los modelos de datos CIM. La clase representa el modelo IEEE Std 421.5-2005 tipo ST3A.  Algunos sistemas estáticos utilizan un bucle de control de la tensión de campo para linealizar la característica de control del excitador. Esto también hace que la salida sea independiente de las variaciones de la fuente de alimentación hasta que se alcancen las limitaciones de suministro.  Estos sistemas utilizan una variedad de diseños de rectificadores controlados: complementos de tiristores completos o puentes híbridos en configuraciones en serie o en derivación. La fuente de alimentación puede consistir únicamente en una fuente de potencial, ya sea alimentada desde los terminales de la máquina o desde los devanados internos. Algunos diseños pueden tener fuentes de potencia compuestas que utilizan tanto el potencial como la corriente de la máquina. Estas fuentes de potencia se representan como combinaciones fasoriales de corriente y tensión en los terminales de la máquina y se acomodan mediante parámetros adecuados en el modelo Tipo ST3A que se representa con ExcIEEEST3A.   Referencia: Norma IEEE 421.5-2005, apartado 7.3.**  

## Lista de propiedades  

- `address`: La dirección postal.  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `id`: Identificador único de la entidad  - `ka`: Ganancia del regulador de tensión (K). Es el parámetro K de la norma IEEE. Valor típico = 200. Por defecto: 0,0  - `kc`: Factor de carga del rectificador proporcional a la reactancia de conmutación (K). Valor típico = 0,2. Por defecto: 0,0  - `kg`: Constante de ganancia de retroalimentación del regulador de campo del bucle interior (K).  Valor típico = 1. Por defecto: 0,0  - `ki`: Coeficiente de ganancia del circuito potencial (K).  Valor típico = 0. Por defecto: 0.0  - `km`: Constante de ganancia de avance del regulador de campo del bucle interior (K).  Valor típico = 7,93. Por defecto: 0,0  - `kp`: Coeficiente de ganancia del circuito potencial (K).  Valor típico = 6,15. Por defecto: 0,0  - `location`:   - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `ta`: Constante de tiempo del regulador de tensión (T).  Valor típico = 0. Por defecto: 0  - `tb`: Constante de tiempo del regulador de tensión (T).  Valor típico = 10. Por defecto: 0  - `tc`: Constante de tiempo del regulador de tensión (T).  Valor típico = 1. Por defecto: 0  - `thetap`: Ángulo de fase del circuito de potencial (thetap).  Valor típico = 0. Por defecto: 0.0  - `tm`: Constante de tiempo de avance del regulador de campo del bucle interior (T).  Valor típico = 0,4. Por defecto: 0  - `type`: Tipo NGSI. Tiene que ser ExcIEEEST3A  - `vbmax`: Tensión máxima de excitación (V).  Valor típico = 6,9. Por defecto: 0,0  - `vgmax`: Tensión máxima de retroalimentación del bucle interno (V).  Valor típico = 5,8. Por defecto: 0,0  - `vimax`: Límite máximo de entrada del regulador de tensión (V).  Valor típico = 0,2. Por defecto: 0,0  - `vimin`: Límite mínimo de entrada del regulador de tensión (V).  Valor típico = -0,2. Por defecto: 0,0  - `vmmax`: Salida máxima del bucle interior (V).  Valor típico = 1. Por defecto: 0,0  - `vmmin`: Salida mínima del bucle interior (V).  Valor típico = 0. Por defecto: 0.0  - `vrmax`: Salida máxima del regulador de tensión (V).  Valor típico = 10. Por defecto: 0,0  - `vrmin`: Salida mínima del regulador de tensión (V).  Valor típico = -10. Por defecto: 0,0  - `xl`: Reactancia asociada a la fuente de potencial (X).  Valor típico = 0,081. Por defecto: 0,0    
Propiedades requeridas  
Este modelo de datos es una conversión directa del Modelo de Información Común (CIM) especificado por la norma IEC61970 en modelos de datos inteligentes. Las clases de python en las que se basa este modelo fueron desarrolladas por estas entidades Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) y RWTH University Aachen, Alemania. algunas propiedades pueden tener un tipo incorrecto. Este es el caso, por favor, plantee un problema o envíe un correo a alberto.abella@fiware.org  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ExcIEEEST3A:    
  description: 'Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type ST3A model.  Some static systems utilize a field voltage control loop to linearize the exciter control characteristic. This also makes the output independent of supply source variations until supply limitations are reached.  These systems utilize a variety of controlled-rectifier designs: full thyristor complements or hybrid bridges in either series or shunt configurations. The power source may consist of only a potential source, either fed from the machine terminals or from internal windings. Some designs may have compound power sources utilizing both machine potential and current. These power sources are represented as phasor combinations of machine terminal current and voltage and are accommodated by suitable parameters in model Type ST3A which is represented by ExcIEEEST3A.   Reference: IEEE Standard 421.5-2005 Section 7.3.'    
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
      anyOf: &excieeest3a_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Voltage regulator gain (K). This is parameter K in the IEEE Std. Typical Value = 200. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kc:    
      description: 'Rectifier loading factor proportional to commutating reactance (K). Typical Value = 0.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kg:    
      description: 'Feedback gain constant of the inner loop field regulator (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ki:    
      description: 'Potential circuit gain coefficient (K).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    km:    
      description: 'Forward gain constant of the inner loop field regulator (K).  Typical Value = 7.93. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kp:    
      description: 'Potential circuit gain coefficient (K).  Typical Value = 6.15. Default: 0.0'    
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
        anyOf: *excieeest3a_-_properties_-_owner_-_items_-_anyof    
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
    ta:    
      description: 'Voltage regulator time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tb:    
      description: 'Voltage regulator time constant (T).  Typical Value = 10. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tc:    
      description: 'Voltage regulator time constant (T).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    thetap:    
      description: 'Potential circuit phase angle (thetap).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tm:    
      description: 'Forward time constant of inner loop field regulator (T).  Typical Value = 0.4. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be ExcIEEEST3A'    
      enum:    
        - ExcIEEEST3A    
      type: Property    
    vbmax:    
      description: 'Maximum excitation voltage (V).  Typical Value = 6.9. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vgmax:    
      description: 'Maximum inner loop feedback voltage (V).  Typical Value = 5.8. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vimax:    
      description: 'Maximum voltage regulator input limit (V).  Typical Value = 0.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vimin:    
      description: 'Minimum voltage regulator input limit (V).  Typical Value = -0.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vmmax:    
      description: 'Maximum inner loop output (V).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vmmin:    
      description: 'Minimum inner loop output (V).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vrmax:    
      description: 'Maximum voltage regulator output (V).  Typical Value = 10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vrmin:    
      description: 'Minimum voltage regulator output (V).  Typical Value = -10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    xl:    
      description: 'Reactance associated with potential source (X).  Typical Value = 0.081. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
No está disponible el ejemplo de un ExcIEEEST3A en formato JSON como valores-clave. Esto es compatible con NGSI V2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un ExcIEEEST3A en formato JSON como normalizado. Esto es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de una ExcIEEEST3A en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un ExcIEEEST3A en formato JSON-LD como normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
