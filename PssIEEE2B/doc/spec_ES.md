<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: PssIEEE2B  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/PssIEEE2B/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Adaptado de los modelos de datos CIM. La clase representa el modelo de estabilizador de sistema de potencia IEEE Std 421.5-2005 tipo PSS2B. Este modelo de estabilizador está diseñado para representar una variedad de estabilizadores de doble entrada, que normalmente utilizan combinaciones de potencia y velocidad o frecuencia para derivar la señal estabilizadora.  Referencia: IEEE 2B 421.5-2005 Sección 8.2.**  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>  
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated[string]`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified[string]`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description[string]`: Una descripción de este artículo  - `id[*]`: Identificador único de la entidad  - `inputSignal1Type[number]`: Tipo de señal de entrada #1.  Valor típico = rotorSpeed. Por defecto: Ninguno  . Model: [https://schema.org/Number](https://schema.org/Number)- `inputSignal2Type[number]`: Tipo de señal de entrada #2.  Valor típico = generatorElectricalPower. Por defecto: Ninguno  . Model: [https://schema.org/Number](https://schema.org/Number)- `ks1[number]`: Ganancia del estabilizador (Ks1).  Valor típico = 12. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ks2[number]`: Ganancia en la señal #2 (Ks2).  Valor típico = 0,2. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ks3[number]`: Ganancia en la entrada de la señal #2 antes del filtro de seguimiento de rampa (Ks3).  Valor típico = 1. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `m[number]`: Orden del denominador del filtro de seguimiento de rampa (M).  Valor típico = 5. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `n[number]`: Orden del filtro de seguimiento de rampa (N).  Valor típico = 1. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: El nombre de este artículo.  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `t1[number]`: Constante de tiempo de avance/retraso (T1).  Valor típico = 0,12. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t10[number]`: Constante de tiempo de avance/retraso (T10).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t11[number]`: Constante de tiempo de avance/retraso (T11).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t2[number]`: Constante de tiempo de avance/retraso (T2).  Valor típico = 0,02. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t3[number]`: Constante de tiempo de avance/retraso (T3).  Valor típico = 0,3. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t4[number]`: Constante de tiempo de avance/retraso (T4).  Valor típico = 0,02. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t6[number]`: Constante de tiempo en la señal #1 (T6).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t7[number]`: Constante de tiempo en la señal #2 (T7).  Valor típico = 2. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t8[number]`: Conducción del filtro de seguimiento de rampa (T8).  Valor típico = 0,2. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t9[number]`: Retraso del filtro de seguimiento de rampa (T9).  Valor típico = 0,1. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw1[number]`: Primer lavado en la señal #1 (Tw1).  Valor típico = 2. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw2[number]`: Segundo lavado en la señal #1 (Tw2).  Valor típico = 2. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw3[number]`: Primer lavado en la señal #2 (Tw3).  Valor típico = 2. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw4[number]`: Segundo lavado en la señal #2 (Tw4).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Tipo NGSI. Tiene que ser PssIEEE2B  - `vsi1max[number]`: Límite máximo de la señal de entrada #1 (Vsi1max).  Valor típico = 2. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vsi1min[number]`: Límite mínimo de la señal de entrada #1 (Vsi1min).  Valor típico = -2. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vsi2max[number]`: Límite máximo de la señal de entrada #2 (Vsi2max).  Valor típico = 2. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vsi2min[number]`: Límite mínimo de la señal de entrada #2 (Vsi2min).  Valor típico = -2. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vstmax[number]`: Límite máximo de salida del estabilizador (Vstmax).  Valor típico = 0,1. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vstmin[number]`: Límite mínimo de salida del estabilizador (Vstmin).  Valor típico = -0,1. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
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
PssIEEE2B:    
  description: 'Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type PSS2B power system stabilizer model. This stabilizer model is designed to represent a variety of dual-input stabilizers, which normally use combinations of power and speed or frequency to derive the stabilizing signal.  Reference: IEEE 2B 421.5-2005 Section 8.2.'    
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
    id:    
      anyOf: &pssieee2b_-_properties_-_owner_-_items_-_anyof    
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
    inputSignal1Type:    
      description: "Type of input signal #1.  Typical Value = rotorSpeed. Default: None"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    inputSignal2Type:    
      description: "Type of input signal #2.  Typical Value = generatorElectricalPower. Default: None"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ks1:    
      description: 'Stabilizer gain (Ks1).  Typical Value = 12. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ks2:    
      description: "Gain on signal #2 (Ks2).  Typical Value = 0.2. Default: 0.0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ks3:    
      description: "Gain on signal #2 input before ramp-tracking filter (Ks3).  Typical Value = 1. Default: 0.0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        type: GeoProperty    
    m:    
      description: 'Denominator order of ramp tracking filter (M).  Typical Value = 5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    n:    
      description: 'Order of ramp tracking filter (N).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *pssieee2b_-_properties_-_owner_-_items_-_anyof    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    t1:    
      description: 'Lead/lag time constant (T1).  Typical Value = 0.12. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t10:    
      description: 'Lead/lag time constant (T10).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t11:    
      description: 'Lead/lag time constant (T11).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t2:    
      description: 'Lead/lag time constant (T2).  Typical Value = 0.02. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t3:    
      description: 'Lead/lag time constant (T3).  Typical Value = 0.3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t4:    
      description: 'Lead/lag time constant (T4).  Typical Value = 0.02. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t6:    
      description: "Time constant on signal #1 (T6).  Typical Value = 0. Default: 0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t7:    
      description: "Time constant on signal #2 (T7).  Typical Value = 2. Default: 0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t8:    
      description: 'Lead of ramp tracking filter (T8).  Typical Value = 0.2. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t9:    
      description: 'Lag of ramp tracking filter (T9).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tw1:    
      description: "First washout on signal #1 (Tw1).  Typical Value = 2. Default: 0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tw2:    
      description: "Second washout on signal #1 (Tw2).  Typical Value = 2. Default: 0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tw3:    
      description: "First washout on signal #2 (Tw3).  Typical Value = 2. Default: 0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tw4:    
      description: "Second washout on signal #2 (Tw4).  Typical Value = 0. Default: 0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be PssIEEE2B'    
      enum:    
        - PssIEEE2B    
      type: string    
      x-ngsi:    
        type: Property    
    vsi1max:    
      description: "Input signal #1 max limit (Vsi1max).  Typical Value = 2. Default: 0.0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vsi1min:    
      description: "Input signal #1 min limit (Vsi1min).  Typical Value = -2. Default: 0.0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vsi2max:    
      description: "Input signal #2 max limit (Vsi2max).  Typical Value = 2. Default: 0.0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vsi2min:    
      description: "Input signal #2 min limit (Vsi2min).  Typical Value = -2. Default: 0.0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vstmax:    
      description: 'Stabilizer output max limit (Vstmax).  Typical Value = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vstmin:    
      description: 'Stabilizer output min limit (Vstmin).  Typical Value = -0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PssIEEE2B/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/PssIEEE2B/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
No está disponible el ejemplo de un PssIEEE2B en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un PssIEEE2B en formato JSON-LD como normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un PssIEEE2B en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un PssIEEE2B en formato JSON-LD como normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
