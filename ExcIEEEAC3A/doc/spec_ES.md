<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: ExcIEEEAC3A  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExcIEEEAC3A/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Adaptado de los modelos de datos CIM. La clase representa el modelo IEEE Std 421.5-2005 tipo AC3A. El modelo representa los sistemas de excitación del alternador-rectificador controlados por el campo designados como tipo AC3A. Estos sistemas de excitación incluyen un excitador principal del alternador con rectificadores no controlados. El excitador emplea la autoexcitación, y la potencia del regulador de tensión se deriva de la tensión de salida del excitador.  Por lo tanto, este sistema tiene una no linealidad adicional, simulada mediante el uso de un multiplicador cuyas entradas son la señal de mando del regulador de tensión, , y la tensión de salida del excitador, , veces .  Este modelo es aplicable a los sistemas de excitación que emplean reguladores de tensión estáticos.   Referencia: Norma IEEE 421.5-2005, apartado 6.3.**  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>  
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated[string]`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified[string]`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description[string]`: Una descripción de este artículo  - `efdn[number]`: Valor a partir del cual cambia la ganancia de retroalimentación (E).  Valor típico = 2,36. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identificador único de la entidad  - `ka[number]`: Ganancia del regulador de tensión (K).  Valor típico = 45,62. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kc[number]`: Factor de carga del rectificador proporcional a la reactancia de conmutación (K).  Valor típico = 0,104. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kd[number]`: Factor de desmagnetización, en función de las reactancias del alternador de la excitadora (K).  Valor típico = 0,499. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ke[number]`: Constante de excitación relacionada con el campo autoexcitado (K).  Valor típico = 1. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kf[number]`: Ganancias del estabilizador del sistema de control de la excitación (K).  Valor típico = 0,143. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kn[number]`: Ganancia del estabilizador del sistema de control de la excitación (K).  Valor típico = 0,05. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kr[number]`: Constante asociada a la alimentación del regulador y del campo del alternador (K).  Valor típico = 3,77. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name[string]`: El nombre de este artículo.  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `seve1[number]`: Valor de la función de saturación del excitador a la tensión correspondiente del excitador, V, detrás de la reactancia de conmutación (S[V]).  Valor típico = 1,143. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seve2[number]`: Valor de la función de saturación del excitador a la tensión correspondiente del excitador, V, detrás de la reactancia de conmutación (S[V]).  Valor típico = 0,1. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `ta[number]`: Constante de tiempo del regulador de tensión (T).  Valor típico = 0,013. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tb[number]`: Constante de tiempo del regulador de tensión (T).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tc[number]`: Constante de tiempo del regulador de tensión (T).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `te[number]`: Constante de tiempo del excitador, tasa de integración asociada al control del excitador (T).  Valor típico = 1,17. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tf[number]`: Constante de tiempo del estabilizador del sistema de control de la excitación (T).  Valor típico = 1. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Tipo NGSI. Tiene que ser ExcIEEEAC3A  - `vamax[number]`: Salida máxima del regulador de tensión (V).  Valor típico = 1. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vamin[number]`: Salida mínima del regulador de tensión (V).  Valor típico = -0,95. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ve1[number]`: Las tensiones de salida del alternador del excitador en la parte posterior de la reactancia de conmutación a la que se define la saturación (V) son iguales a V(V).  Valor típico = 6,24. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ve2[number]`: Tensiones de salida del alternador del excitador detrás de la reactancia de conmutación a la que se define la saturación (V).  Valor típico = 4,68. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vemin[number]`: Tensión mínima de salida del excitador (V).  Valor típico = 0,1. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vfemax[number]`: Referencia de límite de corriente de campo del excitador (V).  Valor típico = 16. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
<!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Adaptado de los modelos de datos CIM y CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Este modelo de datos es una conversión directa del Modelo de Información Común (CIM) especificado por la norma IEC61970 en modelos de datos inteligentes. Las clases de python en las que se basa este modelo fueron desarrolladas por estas entidades Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) y RWTH University Aachen, Alemania. Algunas propiedades pueden tener un tipo incorrecto. Este es el caso, por favor, plantee una cuestión o envíe un correo a info@smartdatamodels.org.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ExcIEEEAC3A:    
  description: 'Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type AC3A model. The model represents the field-controlled alternator-rectifier excitation systems designated Type AC3A. These excitation systems include an alternator main exciter with non-controlled rectifiers. The exciter employs self-excitation, and the voltage regulator power is derived from the exciter output voltage.  Therefore, this system has an additional nonlinearity, simulated by the use of a multiplier whose inputs are the voltage regulator command signal, , and the exciter output voltage, , times .  This model is applicable to excitation systems employing static voltage regulators.   Reference: IEEE Standard 421.5-2005 Section 6.3.'    
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
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    efdn:    
      description: 'Value of at which feedback gain changes (E).  Typical Value = 2.36. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &excieeeac3a_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    ka:    
      description: 'Voltage regulator gain (K).  Typical Value = 45.62. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kc:    
      description: 'Rectifier loading factor proportional to commutating reactance (K).  Typical Value = 0.104. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kd:    
      description: 'Demagnetizing factor, a function of exciter alternator reactances (K).  Typical Value = 0.499. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ke:    
      description: 'Exciter constant related to self-excited field (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kf:    
      description: 'Excitation control system stabilizer gains (K).  Typical Value = 0.143. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kn:    
      description: 'Excitation control system stabilizer gain (K).  Typical Value = 0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kr:    
      description: 'Constant associated with regulator and alternator field power supply (K).  Typical Value = 3.77. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
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
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *excieeeac3a_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
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
      x-ngsi:    
        type: Property    
    seve1:    
      description: 'Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance (S[V]).  Typical Value = 1.143. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    seve2:    
      description: 'Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance (S[V]).  Typical Value = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    ta:    
      description: 'Voltage regulator time constant (T).  Typical Value = 0.013. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tb:    
      description: 'Voltage regulator time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tc:    
      description: 'Voltage regulator time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    te:    
      description: 'Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 1.17. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tf:    
      description: 'Excitation control system stabilizer time constant (T).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be ExcIEEEAC3A'    
      enum:    
        - ExcIEEEAC3A    
      type: string    
      x-ngsi:    
        type: Property    
    vamax:    
      description: 'Maximum voltage regulator output (V).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vamin:    
      description: 'Minimum voltage regulator output (V).  Typical Value = -0.95. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ve1:    
      description: 'Exciter alternator output voltages back of commutating reactance at which saturation is defined (V) equals V(V).  Typical Value = 6.24. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ve2:    
      description: 'Exciter alternator output voltages back of commutating reactance at which saturation is defined (V).  Typical Value = 4.68. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vemin:    
      description: 'Minimum exciter voltage output (V).  Typical Value = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vfemax:    
      description: 'Exciter field current limit reference (V).  Typical Value = 16. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcIEEEAC3A/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/ExcIEEEAC3A/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
No está disponible el ejemplo de una ExcIEEEAC3A en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un ExcIEEEAC3A en formato JSON-LD como normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de una ExcIEEEAC3A en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un ExcIEEEAC3A en formato JSON-LD como normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
