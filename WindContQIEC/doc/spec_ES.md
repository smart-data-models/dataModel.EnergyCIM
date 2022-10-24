<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: WindContQIEC  
=====================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/WindContQIEC/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Adaptado de los modelos de datos CIM. Modelo de control Q.  Referencia: Norma IEC 61400-27-1 Sección 6.6.5.6.**  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>  
- `WindTurbineType3or4IEC[number]`: Modelo de aerogenerador tipo 3 o 4 al que se asocia este modo de control reactivo. Por defecto: Ninguno  . Model: [https://schema.org/Number](https://schema.org/Number)- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated[string]`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified[string]`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description[string]`: Una descripción de este artículo  - `id[*]`: Identificador único de la entidad  - `iqh1[number]`: Máxima inyección de corriente reactiva durante la inmersión (i). Es un parámetro que depende del tipo. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `iqmax[number]`: Máxima inyección de corriente reactiva (i). Es un parámetro que depende del tipo. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `iqmin[number]`: Inyección mínima de corriente reactiva (i). Es un parámetro que depende del tipo. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `iqpost[number]`: Inyección de corriente reactiva tras la avería (). Es un parámetro que depende del proyecto. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kiq[number]`: Ganancia de integración del controlador PI de potencia reactiva (). Es un parámetro dependiente del tipo. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kiu[number]`: Ganancia de integración del controlador PI de tensión (). Es un parámetro que depende del tipo. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kpq[number]`: Ganancia proporcional del controlador PI de potencia reactiva (). Es un parámetro dependiente del tipo. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kpu[number]`: Ganancia proporcional del controlador PI de tensión (). Es un parámetro dependiente del tipo. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kqv[number]`: Factor de escala de tensión para la corriente LVRT (). Es un parámetro que depende del proyecto. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name[string]`: El nombre de este artículo.  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `qmax[number]`: Potencia reactiva máxima (q). Es un parámetro que depende del tipo. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `qmin[number]`: Potencia reactiva mínima (q). Es un parámetro que depende del tipo. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rdroop[number]`: Componente resistivo de la impedancia de caída de tensión (). Es un parámetro que depende del proyecto. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `tiq[number]`: Constante de tiempo en el retraso de la corriente reactiva (T). Es un parámetro que depende del tipo. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tpfilt[number]`: Constante de tiempo del filtro de medición de potencia (). Es un parámetro que depende del tipo. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tpost[number]`: Duración del periodo de tiempo en el que se inyecta la potencia reactiva posterior a la avería (). Es un parámetro que depende del proyecto. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tqord[number]`: Constante de tiempo en el retardo de orden de la potencia reactiva (). Es un parámetro dependiente del tipo. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tufilt[number]`: Constante de tiempo del filtro de medición de tensión (). Es un parámetro dependiente del tipo. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Tipo de NGSI. Tiene que ser WindContQIEC  - `udb1[number]`: Límite inferior de la banda muerta de tensión (). Es un parámetro que depende del tipo. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `udb2[number]`: Límite superior de la banda muerta de tensión (). Es un parámetro que depende del tipo. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `umax[number]`: Tensión máxima en el término integral del controlador PI de tensión (u). Es un parámetro que depende del tipo. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `umin[number]`: Tensión mínima en el término integral del controlador PI de tensión (u). Es un parámetro que depende del tipo. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `uqdip[number]`: Umbral de tensión para la detección de LVRT en el control q (). Es un parámetro dependiente del tipo. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `uref0[number]`: Sesgo definido por el usuario en la referencia de tensión (), utilizado cuando =. Es un parámetro que depende del caso. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `windLVRTQcontrolModesType[number]`: Tipos de modos de control de LVRT Q (). Es un parámetro que depende del proyecto. Por defecto: Ninguno  . Model: [https://schema.org/Number](https://schema.org/Number)- `windQcontrolModesType[number]`: Tipos de modos de control general de la turbina eólica Q ().  Es un parámetro que depende del proyecto. Por defecto: Ninguno  . Model: [https://schema.org/Number](https://schema.org/Number)- `xdroop[number]`: Componente inductivo de la impedancia de caída de tensión (). Es un parámetro que depende del proyecto. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
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
WindContQIEC:    
  description: 'Adapted from CIM data models. Q control model.  Reference: IEC Standard 61400-27-1 Section 6.6.5.6.'    
  properties:    
    WindTurbineType3or4IEC:    
      description: 'Wind turbine type 3 or 4 model with which this reactive control mode is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
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
      anyOf: &windcontqiec_-_properties_-_owner_-_items_-_anyof    
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
    iqh1:    
      description: 'Maximum reactive current injection during dip (i). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    iqmax:    
      description: 'Maximum reactive current injection (i). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    iqmin:    
      description: 'Minimum reactive current injection (i). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    iqpost:    
      description: 'Post fault reactive current injection (). It is project dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kiq:    
      description: 'Reactive power PI controller integration gain (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kiu:    
      description: 'Voltage PI controller integration gain (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kpq:    
      description: 'Reactive power PI controller proportional gain (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kpu:    
      description: 'Voltage PI controller proportional gain (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kqv:    
      description: 'Voltage scaling factor for LVRT current (). It is project dependent parameter. Default: 0.0'    
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
        anyOf: *windcontqiec_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    qmax:    
      description: 'Maximum reactive power (q). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    qmin:    
      description: 'Minimum reactive power (q). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rdroop:    
      description: 'Resistive component of voltage drop impedance (). It is project dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    tiq:    
      description: 'Time constant in reactive current lag (T). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tpfilt:    
      description: 'Power measurement filter time constant (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tpost:    
      description: 'Length of time period where post fault reactive power is injected (). It is project dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tqord:    
      description: 'Time constant in reactive power order lag (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tufilt:    
      description: 'Voltage measurement filter time constant (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be WindContQIEC'    
      enum:    
        - WindContQIEC    
      type: string    
      x-ngsi:    
        type: Property    
    udb1:    
      description: 'Voltage dead band lower limit (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    udb2:    
      description: 'Voltage dead band upper limit (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    umax:    
      description: 'Maximum voltage in voltage PI controller integral term (u). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    umin:    
      description: 'Minimum voltage in voltage PI controller integral term (u). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    uqdip:    
      description: 'Voltage threshold for LVRT detection in q control (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    uref0:    
      description: 'User defined bias in voltage reference (), used when  =. It is case dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    windLVRTQcontrolModesType:    
      description: 'Types of LVRT Q control modes (). It is project dependent parameter. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    windQcontrolModesType:    
      description: 'Types of general wind turbine Q control modes ().  It is project dependent parameter. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    xdroop:    
      description: 'Inductive component of voltage drop impedance (). It is project dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindContQIEC/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/WindContQIEC/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
No está disponible el ejemplo de un WindContQIEC en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un WindContQIEC en formato JSON-LD normalizado. Es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un WindContQIEC en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un WindContQIEC en formato JSON-LD como normalizado. Es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
