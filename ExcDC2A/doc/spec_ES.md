Entidad: ExcDC2A  
================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExcDC2A/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Adaptado de los modelos de datos CIM. Excitadores de corriente continua IEEE DC2A modificados con entrada de velocidad, un bloque de patas más en el bucle de realimentación y sin entradas de limitadores de subexcitación (UEL).  Modelo de sistema de excitación de corriente continua de tipo 2 con multiplicador de velocidad añadido, retardo de la pata y límites dependientes de la tensión.**  

## Lista de propiedades  

- `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `efd1`: Tensión de excitación a la que se define la saturación del excitador (Efd1).  Valor típico = 3,05. Por defecto: 0,0  - `efd2`: Tensión de excitación a la que se define la saturación del excitador (Efd2).  Valor típico = 2,29. Por defecto: 0,0  - `exclim`: (exclim).  La norma IEEE es ambigua sobre el límite inferior de la salida del excitador. true = se aplica un límite inferior de cero a la salida del integrador false = no se aplica un límite inferior de cero a la salida del integrador. Valor típico = verdadero. Por defecto: Falso  - `id`: Identificador único de la entidad  - `ka`: Ganancia del regulador de tensión (Ka).  Valor típico = 300. Por defecto: 0,0  - `ke`: Constante de excitación relacionada con el campo autoexcitado (Ke).  Si se introduce Ke como cero, el modelo calcula un valor efectivo de Ke tal que el valor de condición inicial de Vr es cero. El valor cero de Ke no se modifica.  Si Ke se introduce como distinto de cero, su valor se utiliza directamente, sin cambios.  Valor típico = 1. Por defecto: 0,0  - `kf`: Ganancia del estabilizador del sistema de control de la excitación (Kf).  Valor típico = 0,1. Por defecto: 0,0  - `ks`: Coeficiente para permitir un uso diferente del coeficiente de velocidad del modelo (Ks).  Valor típico = 0. Por defecto: 0.0  - `location`:   - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `seefd1`: Valor de la función de saturación del excitador en la tensión de excitación correspondiente, Efd1 (Se[Eefd1]).  Valor típico = 0,279. Por defecto: 0,0  - `seefd2`: Valor de la función de saturación del excitador en la tensión de excitación correspondiente, Efd2 (Se[Efd2]).  Valor típico = 0,117. Por defecto: 0,0  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `ta`: Constante de tiempo del regulador de tensión (Ta).  Valor típico = 0,01. Por defecto: 0  - `tb`: Constante de tiempo del regulador de tensión (Tb).  Valor típico = 0. Por defecto: 0  - `tc`: Constante de tiempo del regulador de tensión (Tc).  Valor típico = 0. Por defecto: 0  - `te`: Constante de tiempo del excitador, tasa de integración asociada al control del excitador (Te).  Valor típico = 1,33. Por defecto: 0  - `tf`: Constante de tiempo del estabilizador del sistema de control de la excitación (Tf).  Valor típico = 0,675. Por defecto: 0  - `tf1`: Constante de tiempo del estabilizador del sistema de control de excitación (Tf1).  Valor típico = 0. Por defecto: 0  - `type`: Tipo NGSI. Tiene que ser ExcDC2A  - `vrmax`: Salida máxima del regulador de tensión (Vrmax).  Valor típico = 4,95. Por defecto: 0,0  - `vrmin`: Salida mínima del regulador de tensión (Vrmin).  Valor típico = -4,9. Por defecto: 0,0  - `vtlim`: (Vtlim). verdadero = el limitador en el bloque [Ka/(1+sTa)] depende de Vt falso = el limitador en el bloque no depende de Vt. Valor típico = verdadero. Por defecto: Falso    
Propiedades requeridas  
Adaptado de los modelos de datos CIM y CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Este modelo de datos es una conversión directa del Modelo de Información Común (CIM) especificado por la norma IEC61970 en modelos de datos inteligentes. Las clases de python en las que se basa este modelo fueron desarrolladas por estas entidades Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) y RWTH University Aachen, Alemania. Algunas propiedades pueden tener un tipo incorrecto. Este es el caso, por favor, plantee una cuestión o envíe un correo a info@smartdatamodels.org.  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ExcDC2A:    
  description: 'Adapted from CIM data models. Modified IEEE DC2A direct current commutator exciters with speed input, one more leg block in feedback loop and without underexcitation limiters (UEL) inputs.  DC type 2 excitation system model with added speed multiplier, added lead-lag, and voltage-dependent limits.'    
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
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
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
    efd1:    
      description: 'Exciter voltage at which exciter saturation is defined (Efd1).  Typical Value = 3.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    efd2:    
      description: 'Exciter voltage at which exciter saturation is defined (Efd2).  Typical Value = 2.29. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    exclim:    
      description: '(exclim).  IEEE standard is ambiguous about lower limit on exciter output. true = a lower limit of zero is applied to integrator output false = a lower limit of zero is not applied to integrator output. Typical Value = true. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &excdc2a_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Voltage regulator gain (Ka).  Typical Value = 300. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ke:    
      description: 'Exciter constant related to self-excited field (Ke).  If Ke is entered as zero, the model calculates an effective value of Ke such that the initial condition value of Vr is zero. The zero value of Ke is not changed.  If Ke is entered as non-zero, its value is used directly, without change.  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kf:    
      description: 'Excitation control system stabilizer gain (Kf).  Typical Value = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ks:    
      description: 'Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0. Default: 0.0'    
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
        anyOf: *excdc2a_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    seefd1:    
      description: 'Exciter saturation function value at the corresponding exciter voltage, Efd1 (Se[Eefd1]).  Typical Value = 0.279. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    seefd2:    
      description: 'Exciter saturation function value at the corresponding exciter voltage, Efd2 (Se[Efd2]).  Typical Value = 0.117. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    ta:    
      description: 'Voltage regulator time constant (Ta).  Typical Value = 0.01. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tb:    
      description: 'Voltage regulator time constant (Tb).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tc:    
      description: 'Voltage regulator time constant (Tc).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    te:    
      description: 'Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 1.33. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tf:    
      description: 'Excitation control system stabilizer time constant (Tf).  Typical Value = 0.675. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tf1:    
      description: 'Excitation control system stabilizer time constant (Tf1).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be ExcDC2A'    
      enum:    
        - ExcDC2A    
      type: Property    
    vrmax:    
      description: 'Maximum voltage regulator output (Vrmax).  Typical Value = 4.95. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vrmin:    
      description: 'Minimum voltage regulator output (Vrmin).  Typical Value = -4.9. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vtlim:    
      description: '(Vtlim). true = limiter at the block [Ka/(1+sTa)] is dependent on Vt  false = limiter at the block is not dependent on Vt. Typical Value = true. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
No está disponible el ejemplo de un ExcDC2A en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un ExcDC2A en formato JSON-LD como normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un ExcDC2A en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un ExcDC2A en formato JSON-LD como normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
