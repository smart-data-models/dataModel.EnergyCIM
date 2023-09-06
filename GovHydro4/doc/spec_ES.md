<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: GovHydro4  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovHydro4/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Adaptado de los modelos de datos CIM. Turbina hidráulica y regulador. Representa centrales con configuraciones sencillas de tuberías forzadas y reguladores hidráulicos del tipo tradicional "dashpot".  Este modelo puede utilizarse para representar turbinas simples, Francis, Pelton o Kaplan.  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.  
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: El país. Por ejemplo, España  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localidad en la que se encuentra la dirección postal, y que está en la región  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La región en la que se encuentra la localidad, y que está en el país  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distrito es un tipo de división administrativa que, en algunos países, gestiona el gobierno local    
	- `postOfficeBoxNumber[string]`: El número del apartado de correos para las direcciones de apartados postales. Por ejemplo, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: El código postal. Por ejemplo, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: La dirección  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `at[number]`: Ganancia de la turbina (At).  Valor típico = 1,2. Valor por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bgv0[number]`: Punto 0 del servo de la pala Kaplan (Bgv0).  Valor típico = 0. Predeterminado: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bgv1[number]`: Punto 1 del servo de la pala Kaplan (Bgv1).  Valor típico = 0. Predeterminado: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bgv2[number]`: Punto 2 del servo de la pala Kaplan (Bgv2). Valor típico = 0. Valor típico Francisco = 0, Kaplan = 0,1. Valor por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bgv3[number]`: Punto 3 del servo de la pala Kaplan (Bgv3). Valor típico = 0. Valor típico Francisco = 0, Kaplan = 0,667. Valor por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bgv4[number]`: Punto 4 del servo de la pala Kaplan (Bgv4).  Valor típico = 0. Valor típico Francisco = 0, Kaplan = 0,9. Valor por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bgv5[number]`: Punto 5 del servo de la pala Kaplan (Bgv5). Valor típico = 0. Valor típico Francis = 0, Kaplan = 1. Valor por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bmax[number]`: Factor de ajuste máximo de las palas (Bmax). Valor típico = 0. Valor típico Francisco = 0, Kaplan = 1,1276. Valor por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `db1[number]`: Ancho de banda muerta intencional (db1).  Unidad = Hz.  Valor típico = 0. Predeterminado: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `db2[number]`: Banda muerta involuntaria (db2).  Unidad = MW.  Valor típico = 0. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: Descripción de este artículo  - `dturb[number]`: Factor de amortiguación de la turbina (Dturb).  Unidad = delta P (PU de MWbase) / delta velocidad (PU). Valor típico = 0,5.  Valor típico Francis = 1,1, Kaplan = 1,1. Valor por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `eps[number]`: Histéresis db intencional (eps).  Unidad = Hz.  Valor típico = 0. Predeterminado: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gmax[number]`: Apertura máxima de la puerta, PU de MWbase (Gmax).  Valor típico = 1. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gmin[number]`: Apertura mínima de la puerta, PU de MWbase (Gmin).  Valor típico = 0. Predeterminado: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv0[number]`: Punto de ganancia no lineal 0, PU gv (Gv0). Valor típico = 0. Valor típico Francisco = 0,1, Kaplan = 0,1. Valor por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv1[number]`: Punto de ganancia no lineal 1, PU gv (Gv1). Valor típico = 0. Valor típico Francisco = 0,4, Kaplan = 0,4. Valor por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv2[number]`: Punto de ganancia no lineal 2, PU gv (Gv2). Valor típico = 0. Valor típico Francisco = 0,5, Kaplan = 0,5. Valor por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv3[number]`: Punto de ganancia no lineal 3, PU gv (Gv3). Valor típico = 0. Valor típico Francisco = 0,7, Kaplan = 0,7. Valor por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv4[number]`: Punto de ganancia no lineal 4, PU gv (Gv4). Valor típico = 0. Valor típico Francisco = 0,8, Kaplan = 0,8. Valor por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv5[number]`: Punto de ganancia no lineal 5, PU gv (Gv5). Valor típico = 0. Valor típico Francisco = 0,9, Kaplan = 0,9. Valor por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `hdam[number]`: Altura disponible en la presa (hdam).  Valor típico = 1. Valor por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identificador único de la entidad  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `mwbase[number]`: Base para valores de potencia (MWbase) (>0).  Unidad = MW. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: El nombre de este artículo  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `pgv0[number]`: Punto de ganancia no lineal 0, potencia PU (Pgv0).  Valor típico = 0. Predeterminado: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pgv1[number]`: Punto de ganancia no lineal 1, potencia PU (Pgv1). Valor típico = 0. Valor típico Francisco = 0,42, Kaplan = 0,35. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pgv2[number]`: Punto de ganancia no lineal 2, potencia PU (Pgv2). Valor típico = 0. Valor típico Francisco = 0,56, Kaplan = 0,468. Valor por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pgv3[number]`: Punto de ganancia no lineal 3, potencia PU (Pgv3). Valor típico = 0. Valor típico Francisco = 0,8, Kaplan = 0,796. Valor por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pgv4[number]`: Punto de ganancia no lineal 4, potencia PU (Pgv4). Valor típico = 0. Valor típico Francisco = 0,9, Kaplan = 0,917. Valor por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pgv5[number]`: Ganancia no lineal punto 5, potencia PU (Pgv5).  Valor típico = 0. Valor típico Francisco = 0,97, Kaplan = 0,99. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `qn1[number]`: Caudal en vacío a la altura nominal (Qnl). Valor típico = 0,08.  Valor típico Francis = 0, Kaplan = 0. Predeterminado: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rperm[number]`: Estatismo permanente (Rperm).  Valor típico = 0,05. Valor por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rtemp[number]`: Estatismo temporal (Rtemp).  Valor típico = 0,3. Valor por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `tblade[number]`: Constante de tiempo del servo de la pala (Tblade).  Valor típico = 100. Valor por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tg[number]`: Constante de tiempo del servo de la puerta (Tg) (>0).  Valor típico = 0,5. Valor por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tp[number]`: Constante de tiempo del servo piloto (Tp).  Valor típico = 0,1. Valor por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tr[number]`: Constante de tiempo del amortiguador (Tr) (>0).  Valor típico = 5. Valor por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw[number]`: Constante de tiempo de inercia del agua (Tw) (>0).  Valor típico = 1. Valor por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Tipo NGSI. Tiene que ser GovHydro4  - `uc[number]`: Velocidad máxima de cierre de la puerta (Uc).  Valor típico = 0,2. Valor por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `uo[number]`: Velocidad máxima de apertura de la puerta (Uo).  Vlaue típica = 0,2. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
<!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Adaptado de los modelos de datos CIM y CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Este modelo de datos es una conversión directa del Modelo de Información Común (CIM) especificado por la norma IEC61970 en modelos de datos inteligentes. Las clases python en las que se basa este modelo fueron desarrolladas por estas entidades Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) y RWTH University Aachen, Alemania. Algunas propiedades pueden tener un tipo incorrecto. En este caso, por favor, plantee una cuestión o envíe un correo a info@smartdatamodels.org.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción de las propiedades del modelo de datos  
Ordenados alfabéticamente (pulse para más detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GovHydro4:    
  description: 'Adapted from CIM data models. Hydro turbine and governor. Represents plants with straight-forward penstock configurations and hydraulic governors of traditional ''dashpot'' type.  This model can be used to represent simple, Francis, Pelton or Kaplan turbines.'    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    at:    
      description: 'Turbine gain (At).  Typical Value = 1.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bgv0:    
      description: 'Kaplan blade servo point 0 (Bgv0).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bgv1:    
      description: 'Kaplan blade servo point 1 (Bgv1).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bgv2:    
      description: 'Kaplan blade servo point 2 (Bgv2). Typical Value = 0.  Typical Value Francis = 0, Kaplan = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bgv3:    
      description: 'Kaplan blade servo point 3 (Bgv3). Typical Value = 0.  Typical Value Francis = 0, Kaplan = 0.667. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bgv4:    
      description: 'Kaplan blade servo point 4 (Bgv4).  Typical Value = 0.  Typical Value Francis = 0, Kaplan = 0.9. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bgv5:    
      description: 'Kaplan blade servo point 5 (Bgv5). Typical Value = 0.  Typical Value Francis = 0, Kaplan = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bmax:    
      description: 'Maximum blade adjustment factor (Bmax). Typical Value = 0.  Typical Value Francis = 0, Kaplan = 1.1276. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    db1:    
      description: 'Intentional deadband width (db1).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    db2:    
      description: 'Unintentional dead-band (db2).  Unit = MW.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    dturb:    
      description: 'Turbine damping factor (Dturb).  Unit = delta P (PU of MWbase) / delta speed (PU). Typical Value = 0.5.  Typical Value Francis = 1.1, Kaplan = 1.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    eps:    
      description: 'Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gmax:    
      description: 'Maximum gate opening, PU of MWbase (Gmax).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gmin:    
      description: 'Minimum gate opening, PU of MWbase (Gmin).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv0:    
      description: 'Nonlinear gain point 0, PU gv (Gv0). Typical Value = 0.  Typical Value Francis = 0.1, Kaplan = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv1:    
      description: 'Nonlinear gain point 1, PU gv (Gv1). Typical Value = 0.  Typical Value Francis = 0.4, Kaplan = 0.4. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv2:    
      description: 'Nonlinear gain point 2, PU gv (Gv2). Typical Value = 0.  Typical Value Francis = 0.5, Kaplan = 0.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv3:    
      description: 'Nonlinear gain point 3, PU gv (Gv3). Typical Value = 0.  Typical Value Francis = 0.7, Kaplan = 0.7. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv4:    
      description: 'Nonlinear gain point 4, PU gv (Gv4). Typical Value = 0.  Typical Value Francis = 0.8, Kaplan = 0.8. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv5:    
      description: 'Nonlinear gain point 5, PU gv (Gv5). Typical Value = 0.  Typical Value Francis = 0.9, Kaplan = 0.9. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    hdam:    
      description: 'Head available at dam (hdam).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
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
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
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
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
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
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
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
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    mwbase:    
      description: 'Base for power values (MWbase) (>0).  Unit = MW. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    pgv0:    
      description: 'Nonlinear gain point 0, PU power (Pgv0).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pgv1:    
      description: 'Nonlinear gain point 1, PU power (Pgv1). Typical Value = 0.  Typical Value Francis = 0.42, Kaplan = 0.35. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pgv2:    
      description: 'Nonlinear gain point 2, PU power (Pgv2). Typical Value = 0.  Typical Value Francis = 0.56, Kaplan = 0.468. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pgv3:    
      description: 'Nonlinear gain point 3, PU power (Pgv3). Typical Value = 0.  Typical Value Francis = 0.8, Kaplan = 0.796. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pgv4:    
      description: 'Nonlinear gain point 4, PU power (Pgv4). Typical Value = 0.  Typical Value Francis = 0.9, Kaplan = 0.917. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pgv5:    
      description: 'Nonlinear gain point 5, PU power (Pgv5).  Typical Value = 0.  Typical Value Francis = 0.97, Kaplan = 0.99. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    qn1:    
      description: 'No-load flow at nominal head (Qnl). Typical Value = 0.08.  Typical Value Francis = 0, Kaplan = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rperm:    
      description: 'Permanent droop (Rperm).  Typical Value = 0.05. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rtemp:    
      description: 'Temporary droop (Rtemp).  Typical Value = 0.3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    tblade:    
      description: 'Blade servo time constant (Tblade).  Typical Value = 100. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tg:    
      description: 'Gate servo time constant (Tg) (>0).  Typical Value = 0.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tp:    
      description: 'Pilot servo time constant (Tp).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tr:    
      description: 'Dashpot time constant (Tr) (>0).  Typical Value = 5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tw:    
      description: 'Water inertia time constant (Tw) (>0).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: NGSI type. It has to be GovHydro4    
      enum:    
        - GovHydro4    
      type: string    
      x-ngsi:    
        type: Property    
    uc:    
      description: 'Max gate closing velocity (Uc).  Typical Value = 0.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    uo:    
      description: 'Max gate opening velocity (Uo).  Typical Vlaue = 0.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovHydro4/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/GovHydro4/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
No disponible el ejemplo de un GovHydro4 en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No disponible el ejemplo de un GovHydro4 en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No disponible el ejemplo de un GovHydro4 en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No disponible el ejemplo de un GovHydro4 en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
