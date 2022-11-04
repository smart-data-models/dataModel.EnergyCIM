Entidad: GovSteamFV4  
====================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovSteamFV4/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Adaptado de los modelos de datos CIM. Regulador electrohidráulico detallado para la unidad de vapor.**  

## Lista de propiedades  

- `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `cpsmn`: Valor mínimo de la salida del regulador de presión (Cpsmn).  Valor típico = -1. Por defecto: 0,0  - `cpsmx`: Valor máximo de la salida del regulador de presión (Cpsmx).  Valor típico = 1. Por defecto: 0,0  - `crmn`: Valor mínimo de la consigna del regulador (Crmn).  Valor típico = 0. Por defecto: 0.0  - `crmx`: Valor máximo de la consigna del regulador (Crmx).  Valor típico = 1,2. Por defecto: 0,0  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `id`: Identificador único de la entidad  - `kdc`: Ganancia derivativa del regulador de presión (Kdc).  Valor típico = 1. Por defecto: 0,0  - `kf1`: Sesgo de frecuencia (recíproco del estatismo) (Kf1).  Valor típico = 20. Por defecto: 0,0  - `kf3`: Control de frecuencia (recíproco del estatismo) (Kf3).  Valor típico = 20. Por defecto: 0,0  - `khp`: Fracción de la potencia total de la turbina generada por la parte HP (Khp).  Valor típico = 0,35. Por defecto: 0,0  - `kic`: Ganancia integral del regulador de presión (Kic).  Valor típico = 0,0033. Por defecto: 0,0  - `kip`: Ganancia integral del regulador de retroalimentación de presión (Kip).  Valor típico = 0,5. Por defecto: 0,0  - `kit`: Ganancia integral del regulador electrohidráulico (Kit).  Valor típico = 0,04. Por defecto: 0,0  - `kmp1`: Primer coeficiente de ganancia de la característica de las válvulas de intercepción (Kmp1).  Valor típico = 0,5. Por defecto: 0,0  - `kmp2`: Segundo coeficiente de ganancia de la característica de las válvulas de intercepción (Kmp2).  Valor típico = 3,5. Por defecto: 0,0  - `kpc`: Ganancia proporcional del regulador de presión (Kpc).  Valor típico = 0,5. Por defecto: 0,0  - `kpp`: Ganancia proporcional del regulador de retroalimentación de presión (Kpp).  Valor típico = 1. Por defecto: 0,0  - `kpt`: Ganancia proporcional del regulador electrohidráulico (Kpt).  Valor típico = 0,3. Por defecto: 0,0  - `krc`: Variación máxima del caudal de combustible (Krc).  Valor típico = 0,05. Por defecto: 0,0  - `ksh`: Pérdida de presión debida a la fricción del flujo en los tubos de la caldera (Ksh).  Valor típico = 0,08. Por defecto: 0,0  - `location`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `lpi`: Máximo error de potencia negativa (Lpi).  Valor típico = -0,15. Por defecto: 0,0  - `lps`: Máximo error de potencia positiva (Lps).  Valor típico = 0,03. Por defecto: 0,0  - `mnef`: Límite inferior de la corrección de frecuencia (MN).  Valor típico = -0,05. Por defecto: 0,0  - `mxef`: Límite superior de la corrección de frecuencia (MX).  Valor típico = 0,05. Por defecto: 0,0  - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `pr1`: Primer valor de la característica estática del punto de ajuste de la presión (Pr1).  Valor típico = 0,2. Por defecto: 0,0  - `pr2`: Segundo valor de la característica estática del punto de consigna de presión, correspondiente a Ps0 = 1,0 PU (Pr2).  Valor típico = 0,75. Por defecto: 0,0  - `psmn`: Valor mínimo de la característica estática del punto de ajuste de presión (Psmn).  Valor típico = 1. Por defecto: 0,0  - `rsmimn`: Valor mínimo del regulador integral (Rsmimn).  Valor típico = 0. Por defecto: 0.0  - `rsmimx`: Valor máximo del regulador integral (Rsmimx).  Valor típico = 1,1. Por defecto: 0,0  - `rvgmn`: Valor mínimo del regulador integral (Rvgmn).  Valor típico = 0. Por defecto: 0.0  - `rvgmx`: Valor máximo del regulador integral (Rvgmx).  Valor típico = 1,2. Por defecto: 0,0  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `srmn`: Apertura mínima de la válvula (Srmn).  Valor típico = 0. Por defecto: 0.0  - `srmx`: Apertura máxima de la válvula (Srmx).  Valor típico = 1,1. Por defecto: 0,0  - `srsmp`: Punto de discontinuidad característico de las válvulas de intercepción (Srsmp).  Valor típico = 0,43. Por defecto: 0,0  - `svmn`: Velocidad máxima de cierre de la puerta del regulador (Svmn).  Valor típico = -0,0333. Por defecto: 0,0  - `svmx`: Velocidad máxima de apertura de la compuerta del regulador (Svmx).  Valor típico = 0,0333. Por defecto: 0,0  - `ta`: Tiempo de apertura de las válvulas de control (Ta).  Valor típico = 0,8. Por defecto: 0  - `tam`: Tiempo de apertura de la tasa de las válvulas de intercepción (Tam).  Valor típico = 0,8. Por defecto: 0  - `tc`: Tiempo de cierre de las válvulas de control (Tc).  Valor típico = 0,5. Por defecto: 0  - `tcm`: Tiempo de cierre de la tasa de las válvulas de intercepción (Tcm).  Valor típico = 0,5. Por defecto: 0  - `tdc`: Constante de tiempo derivada del regulador de presión (Tdc).  Valor típico = 90. Por defecto: 0  - `tf1`: Constante de tiempo de regulación del combustible (Tf1).  Valor típico = 10. Por defecto: 0  - `tf2`: Constante de tiempo del pecho de vapor (Tf2).  Valor típico = 10. Por defecto: 0  - `thp`: Constante de tiempo de alta presión (HP) de la turbina (Thp).  Valor típico = 0,15. Por defecto: 0  - `tmp`: Constante de tiempo de baja presión (LP) de la turbina (Tmp).  Valor típico = 0,4. Por defecto: 0  - `trh`: Constante de tiempo del recalentador de la turbina (Trh).  Valor típico = 10. Por defecto: 0  - `tv`: Constante de tiempo de la caldera (Tv).  Valor típico = 60. Por defecto: 0  - `ty`: Constante de tiempo de las válvulas de control (Ty).  Valor típico = 0,1. Por defecto: 0  - `type`: Tipo de NGSI. Tiene que ser GovSteamFV4  - `y`: Coeficiente de las ecuaciones lineales de la turbina (formulación de Stodola) (Y).  Valor típico = 0,13. Por defecto: 0,0  - `yhpmn`: Posición mínima de la válvula de control (Yhpmn).  Valor típico = 0. Por defecto: 0.0  - `yhpmx`: Posición máxima de la válvula de control (Yhpmx).  Valor típico = 1,1. Por defecto: 0,0  - `ympmn`: Posición mínima de la válvula de intercepción (Ympmn).  Valor típico = 0. Por defecto: 0.0  - `ympmx`: Posición máxima de la válvula de intercepción (Ympmx).  Valor típico = 1,1. Por defecto: 0,0    
Propiedades requeridas  
Adaptado de los modelos de datos CIM y CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Este modelo de datos es una conversión directa del Modelo de Información Común (CIM) especificado por la norma IEC61970 en modelos de datos inteligentes. Las clases de python en las que se basa este modelo fueron desarrolladas por estas entidades Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) y RWTH University Aachen, Alemania. Algunas propiedades pueden tener un tipo incorrecto. Este es el caso, por favor, plantee una cuestión o envíe un correo a info@smartdatamodels.org.  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GovSteamFV4:    
  description: 'Adapted from CIM data models. Detailed electro-hydraulic governor for steam unit.'    
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
    cpsmn:    
      description: 'Minimum value of pressure regulator output (Cpsmn).  Typical Value = -1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    cpsmx:    
      description: 'Maximum value of pressure regulator output (Cpsmx).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    crmn:    
      description: 'Minimum value of regulator set-point (Crmn).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    crmx:    
      description: 'Maximum value of regulator set-point (Crmx).  Typical Value = 1.2. Default: 0.0'    
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
    id:    
      anyOf: &govsteamfv4_-_properties_-_owner_-_items_-_anyof    
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
    kdc:    
      description: 'Derivative gain of pressure regulator (Kdc).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kf1:    
      description: 'Frequency bias (reciprocal of droop) (Kf1).  Typical Value = 20. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kf3:    
      description: 'Frequency control (reciprocal of droop) (Kf3).  Typical Value = 20. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    khp:    
      description: 'Fraction  of total turbine output generated by HP part (Khp).  Typical Value = 0.35. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kic:    
      description: 'Integral gain of pressure regulator (Kic).  Typical Value = 0.0033. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kip:    
      description: 'Integral gain of pressure feedback regulator (Kip).  Typical Value = 0.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kit:    
      description: 'Integral gain of electro-hydraulic regulator (Kit).  Typical Value = 0.04. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kmp1:    
      description: 'First gain coefficient of  intercept valves characteristic (Kmp1).  Typical Value = 0.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kmp2:    
      description: 'Second gain coefficient of intercept valves characteristic (Kmp2).  Typical Value = 3.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kpc:    
      description: 'Proportional gain of pressure regulator (Kpc).  Typical Value = 0.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kpp:    
      description: 'Proportional gain of pressure feedback regulator (Kpp).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kpt:    
      description: 'Proportional gain of electro-hydraulic regulator (Kpt).  Typical Value = 0.3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    krc:    
      description: 'Maximum variation of fuel flow (Krc).  Typical Value = 0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ksh:    
      description: 'Pressure loss due to flow friction in the boiler tubes (Ksh).  Typical Value = 0.08. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
      type: GeoProperty    
    lpi:    
      description: 'Maximum negative power error (Lpi).  Typical Value = -0.15. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    lps:    
      description: 'Maximum positive power error (Lps).  Typical Value = 0.03. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    mnef:    
      description: 'Lower limit for frequency correction (MN).  Typical Value = -0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    mxef:    
      description: 'Upper limit for frequency correction (MX).  Typical Value = 0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *govsteamfv4_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    pr1:    
      description: 'First value of pressure set point static characteristic (Pr1).  Typical Value = 0.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pr2:    
      description: 'Second value of pressure set point static characteristic, corresponding to Ps0 = 1.0 PU (Pr2).  Typical Value = 0.75. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    psmn:    
      description: 'Minimum value of pressure set point static characteristic (Psmn).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rsmimn:    
      description: 'Minimum value of integral regulator (Rsmimn).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rsmimx:    
      description: 'Maximum value of integral regulator (Rsmimx).  Typical Value = 1.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rvgmn:    
      description: 'Minimum value of integral regulator (Rvgmn).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rvgmx:    
      description: 'Maximum value of integral regulator (Rvgmx).  Typical Value = 1.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    srmn:    
      description: 'Minimum valve opening (Srmn).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    srmx:    
      description: 'Maximum valve opening (Srmx).  Typical Value = 1.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    srsmp:    
      description: 'Intercept valves characteristic discontinuity point (Srsmp).  Typical Value = 0.43. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    svmn:    
      description: 'Maximum regulator gate closing velocity (Svmn).  Typical Value = -0.0333. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    svmx:    
      description: 'Maximum regulator gate opening velocity (Svmx).  Typical Value = 0.0333. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ta:    
      description: 'Control valves rate opening time (Ta).  Typical Value = 0.8. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tam:    
      description: 'Intercept valves rate opening time (Tam).  Typical Value = 0.8. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tc:    
      description: 'Control valves rate closing time (Tc).  Typical Value = 0.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tcm:    
      description: 'Intercept valves rate closing time (Tcm).  Typical Value = 0.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tdc:    
      description: 'Derivative time constant of pressure regulator (Tdc).  Typical Value = 90. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tf1:    
      description: 'Time constant of fuel regulation (Tf1).  Typical Value = 10. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tf2:    
      description: 'Time constant of steam chest (Tf2).  Typical Value = 10. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    thp:    
      description: 'High pressure (HP) time constant of the turbine (Thp).  Typical Value = 0.15. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tmp:    
      description: 'Low pressure (LP) time constant of the turbine (Tmp).  Typical Value = 0.4. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    trh:    
      description: 'Reheater  time constant of the turbine (Trh).  Typical Value = 10. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tv:    
      description: 'Boiler time constant (Tv).  Typical Value = 60. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ty:    
      description: 'Control valves servo time constant (Ty).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be GovSteamFV4'    
      enum:    
        - GovSteamFV4    
      type: Property    
    y:    
      description: 'Coefficient of linearized equations of turbine (Stodola formulation) (Y).  Typical Value = 0.13. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    yhpmn:    
      description: 'Minimum control valve position (Yhpmn).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    yhpmx:    
      description: 'Maximum control valve position (Yhpmx).  Typical Value = 1.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ympmn:    
      description: 'Minimum intercept valve position (Ympmn).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ympmx:    
      description: 'Maximum intercept valve position (Ympmx).  Typical Value = 1.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
No está disponible el ejemplo de un GovSteamFV4 en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un GovSteamFV4 en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un GovSteamFV4 en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un GovSteamFV4 en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud