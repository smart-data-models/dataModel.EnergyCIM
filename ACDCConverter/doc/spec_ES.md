<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: ACDCConverter  
======================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ACDCConverter/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Adaptado de los modelos de datos CIM. Una unidad con válvulas para tres fases, junto con el equipo de control de la unidad, los dispositivos esenciales de protección y conmutación, los condensadores de almacenamiento de CC, las reactancias de fase y los auxiliares, si los hay, utilizados para la conversión.**  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>  
- `DCTerminals[number]`:  Por defecto: "lista  . Model: [https://schema.org/Number](https://schema.org/Number)- `PccTerminal[number]`: Todos los lados de CC de los convertidores vinculados a este punto de terminal de acoplamiento común. Por defecto: Ninguno  . Model: [https://schema.org/Number](https://schema.org/Number)- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `baseS[number]`: Potencia aparente base del polo del convertidor. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated[string]`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified[string]`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description[string]`: Una descripción de este artículo  - `id[*]`: Identificador único de la entidad  - `idc[number]`: Corriente continua del convertidor, también llamada Id. Variable de estado del convertidor, resultado del flujo de potencia. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `idleLoss[number]`: Pérdida de potencia activa en el polo sin transferencia de potencia. Datos de configuración del convertidor utilizados en el flujo de potencia. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `maxUdc[number]`: La tensión máxima en el lado de CC a la que debe funcionar el convertidor. Datos de configuración del convertidor utilizados en el flujo de potencia. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `minUdc[number]`: Tensión de CC mínima permitida del convertidor. Datos de configuración del convertidor utilizados en el flujo de potencia. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: El nombre de este artículo.  - `numberOfValves[number]`: Número de válvulas en el convertidor. Se utiliza en los cálculos de pérdidas. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `p[number]`: Potencia activa en el punto de acoplamiento común. Se utiliza la convención del signo de la carga, es decir, el signo positivo significa que el flujo sale de un nodo. Valor inicial para una solución de estado estacionario en el caso de que se utilice un modelo de flujo de potencia simplificado. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `poleLossP[number]`: La pérdida de potencia activa en un polo de CC = idleLoss + switchingLoss*|Idc| + resitiveLoss*Idc^2 Para el funcionamiento sin pérdidas Pdc=Pac Para el funcionamiento del rectificador con pérdidas Pdc=Pac-lossP Para el funcionamiento del inversor con pérdidas Pdc=Pac+lossP Variable de estado del convertidor utilizada en el flujo de potencia. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `q[number]`: Potencia reactiva en el punto de acoplamiento común. Se utiliza la convención del signo de la carga, es decir, el signo positivo significa que el flujo sale de un nodo. Valor inicial para una solución de estado estacionario en el caso de que se utilice un modelo de flujo de potencia simplificado. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ratedUdc[number]`: Tensión nominal de CC del convertidor, también llamada UdN. Datos de configuración del convertidor utilizados en el flujo de potencia. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `resistiveLoss[number]`: Datos de configuración del convertidor utilizados en el flujo de potencia. Consulte poleLossP. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `switchingLoss[number]`: Pérdidas de conmutación, relativas a la potencia aparente base `baseS`. Consulte poleLossP. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `targetPpcc[number]`: Objetivo de inyección de potencia real en la red de CA, en el punto de acoplamiento común. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `targetUdc[number]`: Valor objetivo de la magnitud de la tensión continua. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Tipo NGSI. Tiene que ser ACDCConverter  - `uc[number]`: Tensión del convertidor, la tensión en el lado de CA del puente. Variable de estado del convertidor, resultado del flujo de potencia. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `udc[number]`: Tensión del convertidor en el lado de CC, también llamada Ud. Variable de estado del convertidor, resultado del flujo de potencia. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `valveU0[number]`: Tensión de umbral de la válvula. Caída de tensión hacia delante cuando la válvula está conduciendo. Se utiliza en los cálculos de pérdidas, es decir, el switchLoss depende del numberOfValves * valveU0. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
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
ACDCConverter:    
  description: 'Adapted from CIM data models. A unit with valves for three phases, together with unit control equipment, essential protective and switching devices, DC storage capacitors, phase reactors and auxiliaries, if any, used for conversion.'    
  properties:    
    DCTerminals:    
      description: ' Default: ''list'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    PccTerminal:    
      description: 'All converters` DC sides linked to this point of common coupling terminal. Default: None'    
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
    baseS:    
      description: 'Base apparent power of the converter pole. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
      anyOf: &acdcconverter_-_properties_-_owner_-_items_-_anyof    
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
    idc:    
      description: 'Converter DC current, also called Id. Converter state variable, result from power flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    idleLoss:    
      description: 'Active power loss in pole at no power transfer. Converter configuration data used in power flow. Default: 0.0'    
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
    maxUdc:    
      description: 'The maximum voltage on the DC side at which the converter should operate. Converter configuration data used in power flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    minUdc:    
      description: 'Min allowed converter DC voltage. Converter configuration data used in power flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    numberOfValves:    
      description: 'Number of valves in the converter. Used in loss calculations. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *acdcconverter_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    p:    
      description: 'Active power at the point of common coupling. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution in the case a simplified power flow model is used. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    poleLossP:    
      description: 'The active power loss at a DC Pole  = idleLoss + switchingLoss*|Idc| + resitiveLoss*Idc^2 For lossless operation Pdc=Pac For rectifier operation with losses Pdc=Pac-lossP For inverter operation with losses Pdc=Pac+lossP Converter state variable used in power flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    q:    
      description: 'Reactive power at the point of common coupling. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution in the case a simplified power flow model is used. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ratedUdc:    
      description: 'Rated converter DC voltage, also called UdN. Converter configuration data used in power flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    resistiveLoss:    
      description: 'Converter configuration data used in power flow. Refer to poleLossP. Default: 0.0'    
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
    switchingLoss:    
      description: 'Switching losses, relative to the base apparent power `baseS`. Refer to poleLossP. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    targetPpcc:    
      description: 'Real power injection target in AC grid, at point of common coupling. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    targetUdc:    
      description: 'Target value for DC voltage magnitude. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be ACDCConverter'    
      enum:    
        - ACDCConverter    
      type: string    
      x-ngsi:    
        type: Property    
    uc:    
      description: 'Converter voltage, the voltage at the AC side of the bridge. Converter state variable, result from power flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    udc:    
      description: 'Converter voltage at the DC side, also called Ud. Converter state variable, result from power flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    valveU0:    
      description: 'Valve threshold voltage. Forward voltage drop when the valve is conducting. Used in loss calculations, i.e. the switchLoss depend on numberOfValves * valveU0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ACDCConverter/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/ACDCConverter/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
No está disponible el ejemplo de un ACDCConverter en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un ACDCConverter en formato JSON-LD como normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un ACDCConverter en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un ACDCConverter en formato JSON-LD como normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
