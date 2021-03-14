Entidad: ExcSK  
==============  
[Licencia abierta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExcSK/LICENSE.md)  
Descripción global: **Adaptado de los modelos de datos CIM. Modelo de sistema de excitación eslovaco.  En este modelo se incluyen el limitador de subexcitación y el control de la tensión secundaria. Cuando se utiliza este modelo, no puede haber un modelo separado de limitador de subexcitación o de controlador de VAr.**  

## Lista de propiedades  

- `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `efdmax`: Límite de recorte de la tensión de campo (Efdmax). Por defecto: 0,0  - `efdmin`: Límite de recorte de la tensión de campo (Efdmin). Por defecto: 0,0  - `emax`: Salida máxima de tensión de campo (Emax).  Valor típico = 20. Por defecto: 0,0  - `emin`: Salida mínima de tensión de campo (Emin).  Valor típico = -20. Por defecto: 0,0  - `id`: Identificador único de la entidad  - `k`: Ganancia (K).  Valor típico = 1. Por defecto: 0,0  - `k1`: Parámetro del límite de subexcitación (K1).  Valor típico = 0,1364. Por defecto: 0,0  - `k2`: Parámetro del límite de subexcitación (K2).  Valor típico = -0,3861. Por defecto: 0,0  - `kc`: Ganancia del controlador PI (Kc).  Valor típico = 70. Por defecto: 0,0  - `kce`: Factor de regulación del rectificador (Kce).  Valor típico = 0. Por defecto: 0.0  - `kd`: Reactancia interna del excitador (Kd).  Valor típico = 0. Por defecto: 0.0  - `kgob`: Ganancia del regulador P (Kgob).  Valor típico = 10. Por defecto: 0,0  - `kp`: Ganancia del controlador PI (Kp).  Valor típico = 1. Por defecto: 0,0  - `kqi`: Ganancia del controlador PI de la componente integral (Kqi).  Valor típico = 0. Por defecto: 0.0  - `kqob`: Tasa de aumento de la potencia reactiva (Kqob). Por defecto: 0,0  - `kqp`: Ganancia del controlador PI (Kqp).  Valor típico = 0. Por defecto: 0.0  - `location`:   - `name`: El nombre de este artículo.  - `nq`: Banda muerta de la potencia reactiva (nq).  Determina el rango de sensibilidad.  Valor típico = 0,001. Por defecto: 0,0  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `qconoff`: Estado del control de la tensión secundaria (Qc_on_off). verdadero = el control de la tensión secundaria está activado falso = el control de la tensión secundaria está desactivado. Valor típico = falso. Por defecto: Falso  - `qz`: Valor deseado (consigna) de la potencia reactiva, ajuste manual (Qz). Por defecto: 0,0  - `remote`: Selector para aplicar el cálculo automático en el modelo de controlador secundario. verdadero = se activa el cálculo automático falso = se activa el ajuste manual; se requiere el uso del valor deseado de potencia reactiva (Qz). Valor típico = verdadero. Por defecto: Falso  - `sbase`: Potencia aparente de la unidad (Sbase).  Unidad = MVA.  Valor típico = 259. Por defecto: 0,0  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `tc`: Constante de tiempo de avance de fase del controlador PI (Tc).  Valor típico = 8. Por defecto: 0  - `te`: Constante de tiempo del bloque de ganancia (Te).  Valor típico = 0,1. Por defecto: 0  - `ti`: Constante de tiempo de avance de fase del controlador PI (Ti).  Valor típico = 2. Por defecto: 0  - `tp`: Constante de tiempo (Tp).  Valor típico = 0,1. Por defecto: 0  - `tr`: Constante de tiempo del transductor de tensión (Tr).  Valor típico = 0,01. Por defecto: 0  - `type`: Tipo de NGSI. Tiene que ser ExcSK  - `uimax`: Error máximo (Uimax).  Valor típico = 10. Por defecto: 0,0  - `uimin`: Error mínimo (UImin).  Valor típico = -10. Por defecto: 0,0  - `urmax`: Salida máxima del regulador (URmax).  Valor típico = 10. Por defecto: 0,0  - `urmin`: Salida mínima del regulador (URmin).  Valor típico = -10. Por defecto: 0,0  - `vtmax`: Entrada de tensión máxima en los terminales (Vtmax).  Determina el rango de banda muerta de tensión.  Valor típico = 1,05. Por defecto: 0,0  - `vtmin`: Entrada mínima de tensión en los terminales (Vtmin).  Determina el rango de banda muerta de tensión.  Valor típico = 0,95. Por defecto: 0,0  - `yp`: Salida máxima (Yp).  Salida mínima = 0. Valor típico = 1. Por defecto: 0,0    
Propiedades requeridas  
Este modelo de datos es una conversión directa del Modelo de Información Común (CIM) especificado por la norma IEC61970 en modelos de datos inteligentes. Las clases de python en las que se basa este modelo fueron desarrolladas por estas entidades Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) y RWTH University Aachen, Alemania. algunas propiedades pueden tener un tipo incorrecto. Este es el caso, por favor, plantee un problema o envíe un correo a alberto.abella@fiware.org  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ExcSK:    
  description: 'Adapted from CIM data models. Slovakian Excitation System Model.  UEL and secondary voltage control are included in this model. When this model is used, there cannot be a separate underexcitation limiter or VAr controller model.'    
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
    efdmax:    
      description: 'Field voltage clipping limit (Efdmax). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    efdmin:    
      description: 'Field voltage clipping limit (Efdmin). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    emax:    
      description: 'Maximum field voltage output (Emax).  Typical Value = 20. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    emin:    
      description: 'Minimum field voltage output (Emin).  Typical Value = -20. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &excsk_-_properties_-_owner_-_items_-_anyof    
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
    k:    
      description: 'Gain (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    k1:    
      description: 'Parameter of underexcitation limit (K1).  Typical Value = 0.1364. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    k2:    
      description: 'Parameter of underexcitation limit (K2).  Typical Value = -0.3861. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kc:    
      description: 'PI controller gain (Kc).  Typical Value = 70. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kce:    
      description: 'Rectifier regulation factor (Kce).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kd:    
      description: 'Exciter internal reactance (Kd).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kgob:    
      description: 'P controller gain (Kgob).  Typical Value = 10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kp:    
      description: 'PI controller gain (Kp).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kqi:    
      description: 'PI controller gain of integral component (Kqi).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kqob:    
      description: 'Rate of rise of the reactive power (Kqob). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kqp:    
      description: 'PI controller gain (Kqp).  Typical Value = 0. Default: 0.0'    
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
    nq:    
      description: 'Dead band of reactive power (nq).  Determines the range of sensitivity.  Typical Value = 0.001. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *excsk_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    qconoff:    
      description: 'Secondary voltage control state (Qc_on_off). true = secondary voltage control is ON false = secondary voltage control is OFF. Typical Value = false. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    qz:    
      description: 'Desired value (setpoint) of reactive power, manual setting (Qz). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    remote:    
      description: 'Selector to apply automatic calculation in secondary controller model. true = automatic calculation is activated false = manual set is active; the use of desired value of reactive power (Qz) is required. Typical Value = true. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    sbase:    
      description: 'Apparent power of the unit (Sbase).  Unit = MVA.  Typical Value = 259. Default: 0.0'    
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
      description: 'PI controller phase lead time constant (Tc).  Typical Value = 8. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    te:    
      description: 'Time constant of gain block (Te).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ti:    
      description: 'PI controller phase lead time constant (Ti).  Typical Value = 2. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tp:    
      description: 'Time constant (Tp).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tr:    
      description: 'Voltage transducer time constant (Tr).  Typical Value = 0.01. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be ExcSK'    
      enum:    
        - ExcSK    
      type: Property    
    uimax:    
      description: 'Maximum error (Uimax).  Typical Value = 10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    uimin:    
      description: 'Minimum error (UImin).  Typical Value = -10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    urmax:    
      description: 'Maximum controller output (URmax).  Typical Value = 10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    urmin:    
      description: 'Minimum controller output (URmin).  Typical Value = -10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vtmax:    
      description: 'Maximum terminal voltage input (Vtmax).  Determines the range of voltage dead band.  Typical Value = 1.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vtmin:    
      description: 'Minimum terminal voltage input (Vtmin).  Determines the range of voltage dead band.  Typical Value = 0.95. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    yp:    
      description: 'Maximum output (Yp).  Minimum output = 0.  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
No está disponible el ejemplo de un ExcSK en formato JSON como valores-clave. Esto es compatible con NGSI V2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un ExcSK en formato JSON como normalizado. Esto es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un ExcSK en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un ExcSK en formato JSON-LD como normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
