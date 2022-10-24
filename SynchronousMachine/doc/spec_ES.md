<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: SynchronousMachine  
===========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/SynchronousMachine/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Adaptado de los modelos de datos CIM. Dispositivo electromecánico que funciona con un eje que gira sincrónicamente con la red. Se trata de una máquina única que funciona como generador o condensador síncrono o bomba.**  
versión: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>  
- `InitialReactiveCapabilityCurve[number]`: Las máquinas síncronas utilizan esta curva por defecto. Por defecto: Ninguno  . Model: [https://schema.org/Number](https://schema.org/Number)- `SynchronousMachineDynamics[number]`: Modelo de dinámica de la máquina síncrona utilizado para describir el comportamiento dinámico de esta máquina síncrona. Por defecto: Ninguno  . Model: [https://schema.org/Number](https://schema.org/Number)- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated[string]`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified[string]`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description[string]`: Una descripción de este artículo  - `earthing[number]`: Indica si el generador está conectado a tierra o no. Se utiliza para el intercambio de datos de cortocircuito según la norma IEC 60909: Falso  . Model: [https://schema.org/Number](https://schema.org/Number)- `earthingStarPointR[number]`: Resistencia de puesta a tierra del punto de estrella del generador (Re). Se utiliza para el intercambio de datos de cortocircuito según la norma IEC 60909.  . Model: [https://schema.org/Number](https://schema.org/Number)- `earthingStarPointX[number]`: Reactancia de puesta a tierra del punto de estrella del generador (Xe). Se utiliza para el intercambio de datos de cortocircuito según la norma IEC 60909.  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identificador único de la entidad  - `ikk[number]`: Corriente de cortocircuito en estado estacionario (en A para el perfil) del generador con excitación compuesta durante un cortocircuito trifásico. - Ikk=0: Generador sin excitación compuesta. - Ikk?0: Generador con excitación compuesta. Ikk se utiliza para calcular la corriente de cortocircuito mínima en estado estacionario para los generadores con excitación compuesta (apartado 4.6.1.2 de la CEI 60909-0). (Apartado 4.3.4.2. de la CEI 60909-0) Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `maxQ[number]`: Límite máximo de potencia reactiva. Es el límite máximo (nominal) de la unidad. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `minQ[number]`: Límite mínimo de potencia reactiva para la unidad. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `mu[number]`: Factor para calcular la corriente de corte (apartado 4.5.2.1 de la CEI 60909-0). Se utiliza sólo para el cortocircuito de una sola alimentación en un generador (apartado 4.3.4.2. de la CEI 60909-0). Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: El nombre de este artículo.  - `operatingMode[number]`: Modo de funcionamiento actual. Por defecto: Ninguno  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `qPercent[number]`: Porcentaje del control reactivo coordinado que proviene de esta máquina. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `r[number]`: Resistencia equivalente (RG) del generador. La RG se considera para el cálculo de todas las corrientes, excepto para el cálculo de la corriente de pico ip. Se utiliza para el intercambio de datos de cortocircuito según la norma IEC 60909 Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `r0[number]`: Resistencia de secuencia cero de la máquina síncrona. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `r2[number]`: Resistencia de secuencia negativa. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `referencePriority[number]`: Prioridad de la unidad para su uso como selección del bus de referencia del ángulo de fase de la tensión del flujo de potencia. 0 = no importa (por defecto) 1 = máxima prioridad. 2 es menor que 1 y así sucesivamente. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `satDirectSubtransX[number]`: Reactancia subtransitoria del eje directo saturada, también conocida como Xd`sat. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `satDirectSyncX[number]`: Reactancia sincrónica saturada de eje directo (xdsat); recíproca de la relación de cortocircuito. Se utiliza para el intercambio de datos de cortocircuito, sólo para el cortocircuito de una sola alimentación en un generador. (Apartado 4.3.4.2. de la norma IEC 60909-0). Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `satDirectTransX[number]`: Reactancia transitoria de eje directo saturado. El atributo se utiliza principalmente para los cálculos de cortocircuito según ANSI. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `shortCircuitRotorType[number]`: Tipo de rotor, utilizado por las aplicaciones de cortocircuito, sólo para el cortocircuito alimentado individualmente según IEC 60909. Por defecto: Ninguno  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `type[string]`: Modos en los que puede funcionar esta máquina síncrona. Por defecto: Ninguno. Tipo de entidad NGSI. Tiene que ser SynchronousMachine  . Model: [https://schema.org/Number](https://schema.org/Number)- `voltageRegulationRange[number]`: Rango de regulación de la tensión del generador (PG en la IEC 60909-0) utilizado para el cálculo del factor de corrección de la impedancia KG definido en la IEC 60909-0 Este atributo se utiliza para describir la tensión de funcionamiento de la unidad generadora. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `x0[number]`: Reactancia de secuencia cero de la máquina síncrona. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `x2[number]`: Reactancia de secuencia negativa. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
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
SynchronousMachine:    
  description: 'Adapted from CIM data models. An electromechanical device that operates with shaft rotating synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.'    
  properties:    
    InitialReactiveCapabilityCurve:    
      description: 'Synchronous machines using this curve as default. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    SynchronousMachineDynamics:    
      description: 'Synchronous machine dynamics model used to describe dynamic behavior of this synchronous machine. Default: None'    
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
    earthing:    
      description: 'Indicates whether or not the generator is earthed. Used for short circuit data exchange according to IEC 60909 Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    earthingStarPointR:    
      description: 'Generator star point earthing resistance (Re). Used for short circuit data exchange according to IEC 60909 Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    earthingStarPointX:    
      description: 'Generator star point earthing reactance (Xe). Used for short circuit data exchange according to IEC 60909 Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &synchronousmachine_-_properties_-_owner_-_items_-_anyof    
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
    ikk:    
      description: 'Steady-state short-circuit current (in A for the profile) of generator with compound excitation during 3-phase short circuit. - Ikk=0: Generator with no compound excitation. - Ikk?0: Generator with compound excitation. Ikk is used to calculate the minimum steady-state short-circuit current for generators with compound excitation (Section 4.6.1.2 in the IEC 60909-0) Used only for single fed short circuit on a generator. (Section 4.3.4.2. in the IEC 60909-0) Default: 0.0'    
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
    maxQ:    
      description: 'Maximum reactive power limit. This is the maximum (nameplate) limit for the unit. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    minQ:    
      description: 'Minimum reactive power limit for the unit. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    mu:    
      description: 'Factor to calculate the breaking current (Section 4.5.2.1 in the IEC 60909-0). Used only for single fed short circuit on a generator (Section 4.3.4.2. in the IEC 60909-0). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    operatingMode:    
      description: 'Current mode of operation. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *synchronousmachine_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    qPercent:    
      description: 'Percent of the coordinated reactive control that comes from this machine. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    r:    
      description: 'Equivalent resistance (RG) of generator. RG is considered for the calculation of all currents, except for the calculation of the peak current ip. Used for short circuit data exchange according to IEC 60909 Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    r0:    
      description: 'Zero sequence resistance of the synchronous machine. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    r2:    
      description: 'Negative sequence resistance. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    referencePriority:    
      description: 'Priority of unit for use as powerflow voltage phase angle reference bus selection. 0 = don t care (default) 1 = highest priority. 2 is less than 1 and so on. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    satDirectSubtransX:    
      description: 'Direct-axis subtransient reactance saturated, also known as Xd`sat. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    satDirectSyncX:    
      description: 'Direct-axes saturated synchronous reactance (xdsat); reciprocal of short-circuit ration. Used for short circuit data exchange, only for single fed short circuit on a generator. (Section 4.3.4.2. in the IEC 60909-0). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    satDirectTransX:    
      description: 'Saturated Direct-axis transient reactance. The attribute is primarily used for short circuit calculations according to ANSI. Default: 0.0'    
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
    shortCircuitRotorType:    
      description: 'Type of rotor, used by short circuit applications, only for single fed short circuit according to IEC 60909. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'Modes that this synchronous machine can operate in. Default: None. NGSI entity type. it has to be SynchronousMachine'    
      enum:    
        - SynchronousMachine    
      type: string    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    voltageRegulationRange:    
      description: 'Range of generator voltage regulation (PG in the IEC 60909-0) used for calculation of the impedance correction factor KG defined in IEC 60909-0 This attribute is used to describe the operating voltage of the generating unit. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    x0:    
      description: 'Zero sequence reactance of the synchronous machine. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    x2:    
      description: 'Negative sequence reactance. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/SynchronousMachine/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/SynchronousMachine/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
No está disponible el ejemplo de una SynchronousMachine en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de una SynchronousMachine en formato JSON-LD como normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de una SynchronousMachine en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de una SynchronousMachine en formato JSON-LD como normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
