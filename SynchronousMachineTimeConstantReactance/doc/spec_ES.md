Entidad: SynchronousMachineTimeConstantReactance  
================================================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/SynchronousMachineTimeConstantReactance/LICENSE.md)  
Descripción global: **Adaptado de los modelos de datos CIM. Los tipos de modelización detallada de las máquinas síncronas se definen mediante la combinación de los atributos SynchronousMachineTimeConstantReactance.modelType y SynchronousMachineTimeConstantReactance.rotorType.     Los parámetros utilizados para los modelos expresados en forma de reactancia constante en el tiempo incluyen:**  

## Lista de propiedades  

- `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `id`: Identificador único de la entidad  - `ks`: Factor de corrección de la carga de saturación (Ks) (>= 0).  Utilizado sólo por el modelo tipo J.  Valor típico = 0. Por defecto: 0.0  - `location`:   - `modelType`: Tipo de modelo de máquina síncrona utilizado en las aplicaciones de simulación dinámica. Por defecto: Ninguno  - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `rotorType`: Tipo de rotor en la máquina física. Por defecto: Ninguno  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `tc`: Constante de tiempo de amortiguación para la reactancia "Canay".  Valor típico = 0. Por defecto: 0  - `tpdo`: Constante de tiempo del rotor transitorio de eje directo (T`do) (> T``do).  Valor típico = 5. Por defecto: 0  - `tppdo`: Constante de tiempo del rotor subtransitorio del eje directo (T``do) (> 0).  Valor típico = 0,03. Por defecto: 0  - `tppqo`: Constante de tiempo del subtransitorio del eje de cuadratura (T``qo) (> 0). Valor típico = 0,03. Por defecto: 0  - `tpqo`: Constante de tiempo del rotor transitorio del eje de cuadratura (T`qo) (> T``qo). Valor típico = 0,5. Por defecto: 0  - `type`: Tipo NGSI. Debe ser SynchronousMachineTimeConstantReactance  - `xDirectSubtrans`: Reactancia subtransitoria del eje directo (no saturado) (X``d) (> Xl).  Valor típico = 0,2. Por defecto: 0,0  - `xDirectSync`: Reactancia sincrónica de eje directo (Xd) (>= X`d). Cociente entre el valor sostenido de la componente de CA de la tensión de inducido que se produce por el flujo total del eje directo debido a la corriente de inducido del eje directo y el valor de la componente de CA de esta corriente, la máquina funcionando a velocidad nominal. Valor típico = 1,8. Por defecto: 0,0  - `xDirectTrans`: Reactancia transitoria del eje directo (no saturado) (X`d) (> =X``d).  Valor típico = 0,5. Por defecto: 0,0  - `xQuadSubtrans`: Reactancia subtransitoria del eje de cuadratura (X``q) (> Xl).  Valor típico = 0,2. Por defecto: 0,0  - `xQuadSync`: Reactancia sincrónica del eje de cuadratura (Xq) (> =X`q). Relación entre la componente de la tensión reactiva de la armadura, debida a la componente del eje de cuadratura de la corriente de la armadura, y esta componente de la corriente, en condiciones de estado estacionario y a la frecuencia nominal.  Valor típico = 1,6. Por defecto: 0,0  - `xQuadTrans`: Reactancia transitoria del eje de cuadratura (X`q) (> =X``q).  Valor típico = 0,3. Por defecto: 0,0    
Propiedades requeridas  
Este modelo de datos es una conversión directa del Modelo de Información Común (CIM) especificado por la norma IEC61970 en modelos de datos inteligentes. Las clases de python en las que se basa este modelo fueron desarrolladas por estas entidades Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) y RWTH University Aachen, Alemania. algunas propiedades pueden tener un tipo incorrecto. Este es el caso, por favor, plantee un problema o envíe un correo a alberto.abella@fiware.org  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
SynchronousMachineTimeConstantReactance:    
  description: 'Adapted from CIM data models. Synchronous machine detailed modelling types are defined by the combination of the attributes SynchronousMachineTimeConstantReactance.modelType and SynchronousMachineTimeConstantReactance.rotorType.     The parameters used for models expressed in time constant reactance form include:'    
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
      anyOf: &synchronousmachinetimeconstantreactance_-_properties_-_owner_-_items_-_anyof    
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
    ks:    
      description: 'Saturation loading correction factor (Ks) (>= 0).  Used only by Type J model.  Typical Value = 0. Default: 0.0'    
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
    modelType:    
      description: 'Type of synchronous machine model used in Dynamic simulation applications. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *synchronousmachinetimeconstantreactance_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    rotorType:    
      description: 'Type of rotor on physical machine. Default: None'    
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
    tc:    
      description: 'Damping time constant for `Canay` reactance.  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tpdo:    
      description: 'Direct-axis transient rotor time constant (T`do) (> T``do).  Typical Value = 5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tppdo:    
      description: 'Direct-axis subtransient rotor time constant (T``do) (> 0).  Typical Value = 0.03. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tppqo:    
      description: 'Quadrature-axis subtransient rotor time constant (T``qo) (> 0). Typical Value = 0.03. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tpqo:    
      description: 'Quadrature-axis transient rotor time constant (T`qo) (> T``qo). Typical Value = 0.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be SynchronousMachineTimeConstantReactance'    
      enum:    
        - SynchronousMachineTimeConstantReactance    
      type: Property    
    xDirectSubtrans:    
      description: 'Direct-axis subtransient reactance (unsaturated) (X``d) (> Xl).  Typical Value = 0.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    xDirectSync:    
      description: 'Direct-axis synchronous reactance (Xd) (>= X`d). The quotient of a sustained value of that AC component of armature voltage that is produced by the total direct-axis flux due to direct-axis armature current and the value of the AC component of this current, the machine running at rated speed. Typical Value = 1.8. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    xDirectTrans:    
      description: 'Direct-axis transient reactance (unsaturated) (X`d) (> =X``d).  Typical Value = 0.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    xQuadSubtrans:    
      description: 'Quadrature-axis subtransient reactance (X``q) (> Xl).  Typical Value = 0.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    xQuadSync:    
      description: 'Quadrature-axis synchronous reactance (Xq) (> =X`q). The ratio of the component of reactive armature voltage, due to the quadrature-axis component of armature current, to this component of current, under steady state conditions and at rated frequency.  Typical Value = 1.6. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    xQuadTrans:    
      description: 'Quadrature-axis transient reactance (X`q) (> =X``q).  Typical Value = 0.3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
No está disponible el ejemplo de una SynchronousMachineTimeConstantReactance en formato JSON como key-values. Esto es compatible con NGSI V2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un SynchronousMachineTimeConstantReactance en formato JSON como normalizado. Esto es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de una SynchronousMachineTimeConstantReactance en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un SynchronousMachineTimeConstantReactance en formato JSON-LD como normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
