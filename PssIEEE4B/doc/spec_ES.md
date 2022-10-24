<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: PssIEEE4B  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/PssIEEE4B/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Adaptado de los modelos de datos CIM. La clase representa el modelo de estabilizador del sistema de potencia del tipo PSS2B de la norma IEEE 421.5-2005. El modelo PSS4B representa una estructura basada en múltiples bandas de frecuencia de trabajo. En este PSS delta-omega (entrada de velocidad) se utilizan tres bandas separadas, dedicadas respectivamente a los modos de oscilación de baja, media y alta frecuencia.  Referencia: IEEE 4B 421.5-2005 Sección 8.4.**  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>  
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `bwh1[number]`: Filtro Notch 1 (banda de alta frecuencia): Ancho de banda de 3 dB (B). Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bwh2[number]`: Filtro Notch 2 (banda de alta frecuencia): Ancho de banda de tres dB (B). Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bwl1[number]`: Filtro Notch 1 (banda de baja frecuencia): Ancho de banda de 3 dB (B). Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bwl2[number]`: Filtro Notch 2 (banda de baja frecuencia): Ancho de banda de tres dB (B). Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated[string]`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified[string]`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description[string]`: Una descripción de este artículo  - `id[*]`: Identificador único de la entidad  - `kh[number]`: Ganancia de banda alta (K).  Valor típico = 120. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kh1[number]`: Ganancia del filtro diferencial de banda alta (K).  Valor típico = 66. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kh11[number]`: Coeficiente de bloqueo de la primera banda alta (K).  Valor típico = 1. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kh17[number]`: Coeficiente de bloqueo de la primera banda alta (K).  Valor típico = 1. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kh2[number]`: Ganancia del filtro diferencial de banda alta (K).  Valor típico = 66. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ki[number]`: Ganancia de banda intermedia (K).  Valor típico = 30. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ki1[number]`: Ganancia del filtro diferencial de banda intermedia (K).  Valor típico = 66. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ki11[number]`: Coeficiente de bloqueo de la primera banda intermedia (K).  Valor típico = 1. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ki17[number]`: Coeficiente de bloqueo de la primera banda intermedia (K).  Valor típico = 1. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ki2[number]`: Ganancia del filtro diferencial de banda intermedia (K).  Valor típico = 66. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kl[number]`: Ganancia en banda baja (K).  Valor típico = 7,5. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kl1[number]`: Ganancia del filtro diferencial de banda baja (K).  Valor típico = 66. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kl11[number]`: Coeficiente de primeros bloqueos de la banda baja (K).  Valor típico = 1. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kl17[number]`: Coeficiente de primeros bloqueos de la banda baja (K).  Valor típico = 1. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kl2[number]`: Ganancia del filtro diferencial de banda baja (K).  Valor típico = 66. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name[string]`: El nombre de este artículo.  - `omeganh1[number]`: Filtro Notch 1 (banda de alta frecuencia): frecuencia del filtro (omega). Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `omeganh2[number]`: Filtro Notch 2 (banda de alta frecuencia): frecuencia del filtro (omega). Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `omeganl1[number]`: Filtro Notch 1 (banda de baja frecuencia): frecuencia del filtro (omega). Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `omeganl2[number]`: Filtro Notch 2 (banda de baja frecuencia): frecuencia del filtro (omega). Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `th1[number]`: Constante de tiempo de banda alta (T).  Valor típico = 0,01513. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th10[number]`: Constante de tiempo de banda alta (T).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th11[number]`: Constante de tiempo de banda alta (T).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th12[number]`: Constante de tiempo de banda alta (T).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th2[number]`: Constante de tiempo de banda alta (T).  Valor típico = 0,01816. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th3[number]`: Constante de tiempo de banda alta (T).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th4[number]`: Constante de tiempo de banda alta (T).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th5[number]`: Constante de tiempo de banda alta (T).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th6[number]`: Constante de tiempo de banda alta (T).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th7[number]`: Constante de tiempo de banda alta (T).  Valor típico = 0,01816. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th8[number]`: Constante de tiempo de banda alta (T).  Valor típico = 0,02179. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th9[number]`: Constante de tiempo de banda alta (T).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti1[number]`: Constante de tiempo de la banda intermedia (T).  Valor típico = 0,173. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti10[number]`: Constante de tiempo de la banda intermedia (T).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti11[number]`: Constante de tiempo de la banda intermedia (T).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti12[number]`: Constante de tiempo de la banda intermedia (T).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti2[number]`: Constante de tiempo de la banda intermedia (T).  Valor típico = 0,2075. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti3[number]`: Constante de tiempo de la banda intermedia (T).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti4[number]`: Constante de tiempo de la banda intermedia (T).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti5[number]`: Constante de tiempo de la banda intermedia (T).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti6[number]`: Constante de tiempo de la banda intermedia (T).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti7[number]`: Constante de tiempo de la banda intermedia (T).  Valor típico = 0,2075. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti8[number]`: Constante de tiempo de la banda intermedia (T).  Valor típico = 0,2491. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti9[number]`: Constante de tiempo de la banda intermedia (T).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl1[number]`: Constante de tiempo de banda baja (T).  Valor típico = 1,73. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl10[number]`: Constante de tiempo de banda baja (T).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl11[number]`: Constante de tiempo de banda baja (T).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl12[number]`: Constante de tiempo de banda baja (T).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl2[number]`: Constante de tiempo de banda baja (T).  Valor típico = 2,075. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl3[number]`: Constante de tiempo de banda baja (T).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl4[number]`: Constante de tiempo de banda baja (T).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl5[number]`: Constante de tiempo de banda baja (T).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl6[number]`: Constante de tiempo de banda baja (T).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl7[number]`: Constante de tiempo de banda baja (T).  Valor típico = 2,075. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl8[number]`: Constante de tiempo de banda baja (T).  Valor típico = 2,491. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl9[number]`: Constante de tiempo de banda baja (T).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Tipo NGSI. Tiene que ser PssIEEE4B  - `vhmax[number]`: Límite máximo de salida de banda alta (V).  Valor típico = 0,6. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vhmin[number]`: Límite mínimo de salida de banda alta (V).  Valor típico = -0,6. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vimax[number]`: Límite máximo de salida de banda intermedia (V).  Valor típico = 0,6. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vimin[number]`: Límite mínimo de salida de banda intermedia (V).  Valor típico = -0,6. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vlmax[number]`: Límite máximo de salida en banda baja (V).  Valor típico = 0,075. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vlmin[number]`: Límite mínimo de salida en banda baja (V).  Valor típico = -0,075. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vstmax[number]`: Límite máximo de la salida PSS (V).  Valor típico = 0,15. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vstmin[number]`: Límite mínimo de salida del PSS (V).  Valor típico = -0,15. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
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
PssIEEE4B:    
  description: 'Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type PSS2B power system stabilizer model. The PSS4B model represents a structure based on multiple working frequency bands. Three separate bands, respectively dedicated to the low-, intermediate- and high-frequency modes of oscillations, are used in this delta-omega (speed input) PSS.  Reference: IEEE 4B 421.5-2005 Section 8.4.'    
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
    bwh1:    
      description: 'Notch filter 1 (high-frequency band): Three dB bandwidth (B). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bwh2:    
      description: 'Notch filter 2 (high-frequency band): Three dB bandwidth (B). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bwl1:    
      description: 'Notch filter 1 (low-frequency band): Three dB bandwidth (B). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bwl2:    
      description: 'Notch filter 2 (low-frequency band): Three dB bandwidth (B). Default: 0.0'    
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
      anyOf: &pssieee4b_-_properties_-_owner_-_items_-_anyof    
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
    kh:    
      description: 'High band gain (K).  Typical Value = 120. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kh1:    
      description: 'High band differential filter gain (K).  Typical Value = 66. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kh11:    
      description: 'High band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kh17:    
      description: 'High band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kh2:    
      description: 'High band differential filter gain (K).  Typical Value = 66. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ki:    
      description: 'Intermediate band gain (K).  Typical Value = 30. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ki1:    
      description: 'Intermediate band differential filter gain (K).  Typical Value = 66. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ki11:    
      description: 'Intermediate band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ki17:    
      description: 'Intermediate band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ki2:    
      description: 'Intermediate band differential filter gain (K).  Typical Value = 66. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kl:    
      description: 'Low band gain (K).  Typical Value = 7.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kl1:    
      description: 'Low band differential filter gain (K).  Typical Value = 66. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kl11:    
      description: 'Low band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kl17:    
      description: 'Low band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kl2:    
      description: 'Low band differential filter gain (K).  Typical Value = 66. Default: 0.0'    
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
    omeganh1:    
      description: 'Notch filter 1 (high-frequency band): filter frequency (omega). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    omeganh2:    
      description: 'Notch filter 2 (high-frequency band): filter frequency (omega). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    omeganl1:    
      description: 'Notch filter 1 (low-frequency band): filter frequency (omega). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    omeganl2:    
      description: 'Notch filter 2 (low-frequency band): filter frequency (omega). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *pssieee4b_-_properties_-_owner_-_items_-_anyof    
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
    th1:    
      description: 'High band time constant (T).  Typical Value = 0.01513. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th10:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th11:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th12:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th2:    
      description: 'High band time constant (T).  Typical Value = 0.01816. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th3:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th4:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th5:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th6:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th7:    
      description: 'High band time constant (T).  Typical Value = 0.01816. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th8:    
      description: 'High band time constant (T).  Typical Value = 0.02179. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th9:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti1:    
      description: 'Intermediate band time constant (T).  Typical Value = 0.173. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti10:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti11:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti12:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti2:    
      description: 'Intermediate band time constant (T).  Typical Value = 0.2075. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti3:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti4:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti5:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti6:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti7:    
      description: 'Intermediate band time constant (T).  Typical Value = 0.2075. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti8:    
      description: 'Intermediate band time constant (T).  Typical Value = 0.2491. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti9:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl1:    
      description: 'Low band time constant (T).  Typical Value = 1.73. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl10:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl11:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl12:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl2:    
      description: 'Low band time constant (T).  Typical Value = 2.075. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl3:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl4:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl5:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl6:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl7:    
      description: 'Low band time constant (T).  Typical Value = 2.075. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl8:    
      description: 'Low band time constant (T).  Typical Value = 2.491. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl9:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be PssIEEE4B'    
      enum:    
        - PssIEEE4B    
      type: string    
      x-ngsi:    
        type: Property    
    vhmax:    
      description: 'High band output maximum limit (V).  Typical Value = 0.6. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vhmin:    
      description: 'High band output minimum limit (V).  Typical Value = -0.6. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vimax:    
      description: 'Intermediate band output maximum limit (V).  Typical Value = 0.6. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vimin:    
      description: 'Intermediate band output minimum limit (V).  Typical Value = -0.6. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vlmax:    
      description: 'Low band output maximum limit (V).  Typical Value = 0.075. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vlmin:    
      description: 'Low band output minimum limit (V).  Typical Value = -0.075. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vstmax:    
      description: 'PSS output maximum limit (V).  Typical Value = 0.15. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vstmin:    
      description: 'PSS output minimum limit (V).  Typical Value = -0.15. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PssIEEE4B/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/PssIEEE4B/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
No está disponible el ejemplo de una PssIEEE4B en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un PssIEEE4B en formato JSON-LD como normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de una PssIEEE4B en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un PssIEEE4B en formato JSON-LD como normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
