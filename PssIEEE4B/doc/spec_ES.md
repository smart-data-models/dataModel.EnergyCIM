Entidad: PssIEEE4B  
==================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/PssIEEE4B/LICENSE.md)  
Descripción global: **Adaptado de los modelos de datos CIM. La clase representa el modelo de estabilizador del sistema de potencia del tipo PSS2B de la norma IEEE 421.5-2005. El modelo PSS4B representa una estructura basada en múltiples bandas de frecuencia de trabajo. En este PSS delta-omega (entrada de velocidad) se utilizan tres bandas separadas, dedicadas respectivamente a los modos de oscilación de baja, media y alta frecuencia.  Referencia: IEEE 4B 421.5-2005 Sección 8.4.**  

## Lista de propiedades  

- `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `bwh1`: Filtro Notch 1 (banda de alta frecuencia): Ancho de banda de tres dB (B). Por defecto: 0,0  - `bwh2`: Filtro Notch 2 (banda de alta frecuencia): Ancho de banda de tres dB (B). Por defecto: 0,0  - `bwl1`: Filtro Notch 1 (banda de baja frecuencia): Ancho de banda de tres dB (B). Por defecto: 0,0  - `bwl2`: Filtro Notch 2 (banda de baja frecuencia): Ancho de banda de 3 dB (B). Por defecto: 0,0  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `id`: Identificador único de la entidad  - `kh`: Ganancia de banda alta (K).  Valor típico = 120. Por defecto: 0,0  - `kh1`: Ganancia del filtro diferencial de banda alta (K).  Valor típico = 66. Por defecto: 0,0  - `kh11`: Coeficiente de bloqueo de la primera banda alta (K).  Valor típico = 1. Por defecto: 0,0  - `kh17`: Coeficiente de bloqueo de la primera banda alta (K).  Valor típico = 1. Por defecto: 0,0  - `kh2`: Ganancia del filtro diferencial de banda alta (K).  Valor típico = 66. Por defecto: 0,0  - `ki`: Ganancia de banda intermedia (K).  Valor típico = 30. Por defecto: 0,0  - `ki1`: Ganancia del filtro diferencial de banda intermedia (K).  Valor típico = 66. Por defecto: 0,0  - `ki11`: Coeficiente de bloqueo de la primera banda intermedia (K).  Valor típico = 1. Por defecto: 0,0  - `ki17`: Coeficiente de bloqueo de la primera banda intermedia (K).  Valor típico = 1. Por defecto: 0,0  - `ki2`: Ganancia del filtro diferencial de banda intermedia (K).  Valor típico = 66. Por defecto: 0,0  - `kl`: Ganancia en banda baja (K).  Valor típico = 7,5. Por defecto: 0,0  - `kl1`: Ganancia del filtro diferencial de banda baja (K).  Valor típico = 66. Por defecto: 0,0  - `kl11`: Coeficiente de primeros bloqueos de la banda baja (K).  Valor típico = 1. Por defecto: 0,0  - `kl17`: Coeficiente de primeros bloqueos de la banda baja (K).  Valor típico = 1. Por defecto: 0,0  - `kl2`: Ganancia del filtro diferencial de banda baja (K).  Valor típico = 66. Por defecto: 0,0  - `location`:   - `name`: El nombre de este artículo.  - `omeganh1`: Filtro Notch 1 (banda de alta frecuencia): frecuencia del filtro (omega). Por defecto: 0,0  - `omeganh2`: Filtro Notch 2 (banda de alta frecuencia): frecuencia del filtro (omega). Por defecto: 0,0  - `omeganl1`: Filtro Notch 1 (banda de baja frecuencia): frecuencia del filtro (omega). Por defecto: 0,0  - `omeganl2`: Filtro Notch 2 (banda de baja frecuencia): frecuencia del filtro (omega). Por defecto: 0,0  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `th1`: Constante de tiempo de banda alta (T).  Valor típico = 0,01513. Por defecto: 0  - `th10`: Constante de tiempo de banda alta (T).  Valor típico = 0. Por defecto: 0  - `th11`: Constante de tiempo de banda alta (T).  Valor típico = 0. Por defecto: 0  - `th12`: Constante de tiempo de banda alta (T).  Valor típico = 0. Por defecto: 0  - `th2`: Constante de tiempo de banda alta (T).  Valor típico = 0,01816. Por defecto: 0  - `th3`: Constante de tiempo de banda alta (T).  Valor típico = 0. Por defecto: 0  - `th4`: Constante de tiempo de banda alta (T).  Valor típico = 0. Por defecto: 0  - `th5`: Constante de tiempo de banda alta (T).  Valor típico = 0. Por defecto: 0  - `th6`: Constante de tiempo de banda alta (T).  Valor típico = 0. Por defecto: 0  - `th7`: Constante de tiempo de banda alta (T).  Valor típico = 0,01816. Por defecto: 0  - `th8`: Constante de tiempo de banda alta (T).  Valor típico = 0,02179. Por defecto: 0  - `th9`: Constante de tiempo de banda alta (T).  Valor típico = 0. Por defecto: 0  - `ti1`: Constante de tiempo de la banda intermedia (T).  Valor típico = 0,173. Por defecto: 0  - `ti10`: Constante de tiempo de la banda intermedia (T).  Valor típico = 0. Por defecto: 0  - `ti11`: Constante de tiempo de la banda intermedia (T).  Valor típico = 0. Por defecto: 0  - `ti12`: Constante de tiempo de la banda intermedia (T).  Valor típico = 0. Por defecto: 0  - `ti2`: Constante de tiempo de la banda intermedia (T).  Valor típico = 0,2075. Por defecto: 0  - `ti3`: Constante de tiempo de la banda intermedia (T).  Valor típico = 0. Por defecto: 0  - `ti4`: Constante de tiempo de la banda intermedia (T).  Valor típico = 0. Por defecto: 0  - `ti5`: Constante de tiempo de la banda intermedia (T).  Valor típico = 0. Por defecto: 0  - `ti6`: Constante de tiempo de la banda intermedia (T).  Valor típico = 0. Por defecto: 0  - `ti7`: Constante de tiempo de la banda intermedia (T).  Valor típico = 0,2075. Por defecto: 0  - `ti8`: Constante de tiempo de la banda intermedia (T).  Valor típico = 0,2491. Por defecto: 0  - `ti9`: Constante de tiempo de la banda intermedia (T).  Valor típico = 0. Por defecto: 0  - `tl1`: Constante de tiempo de banda baja (T).  Valor típico = 1,73. Por defecto: 0  - `tl10`: Constante de tiempo de banda baja (T).  Valor típico = 0. Por defecto: 0  - `tl11`: Constante de tiempo de banda baja (T).  Valor típico = 0. Por defecto: 0  - `tl12`: Constante de tiempo de banda baja (T).  Valor típico = 0. Por defecto: 0  - `tl2`: Constante de tiempo de banda baja (T).  Valor típico = 2,075. Por defecto: 0  - `tl3`: Constante de tiempo de banda baja (T).  Valor típico = 0. Por defecto: 0  - `tl4`: Constante de tiempo de banda baja (T).  Valor típico = 0. Por defecto: 0  - `tl5`: Constante de tiempo de banda baja (T).  Valor típico = 0. Por defecto: 0  - `tl6`: Constante de tiempo de banda baja (T).  Valor típico = 0. Por defecto: 0  - `tl7`: Constante de tiempo de banda baja (T).  Valor típico = 2,075. Por defecto: 0  - `tl8`: Constante de tiempo de banda baja (T).  Valor típico = 2,491. Por defecto: 0  - `tl9`: Constante de tiempo de banda baja (T).  Valor típico = 0. Por defecto: 0  - `type`: Tipo NGSI. Tiene que ser PssIEEE4B  - `vhmax`: Límite máximo de salida de banda alta (V).  Valor típico = 0,6. Por defecto: 0,0  - `vhmin`: Límite mínimo de salida de banda alta (V).  Valor típico = -0,6. Por defecto: 0,0  - `vimax`: Límite máximo de salida de banda intermedia (V).  Valor típico = 0,6. Por defecto: 0,0  - `vimin`: Límite mínimo de salida de banda intermedia (V).  Valor típico = -0,6. Por defecto: 0,0  - `vlmax`: Límite máximo de salida en banda baja (V).  Valor típico = 0,075. Por defecto: 0,0  - `vlmin`: Límite mínimo de salida en banda baja (V).  Valor típico = -0,075. Por defecto: 0,0  - `vstmax`: Límite máximo de la salida PSS (V).  Valor típico = 0,15. Por defecto: 0,0  - `vstmin`: Límite mínimo de salida del PSS (V).  Valor típico = -0,15. Por defecto: 0,0    
Propiedades requeridas  
Este modelo de datos es una conversión directa del Modelo de Información Común (CIM) especificado por la norma IEC61970 en modelos de datos inteligentes. Las clases de python en las que se basa este modelo fueron desarrolladas por estas entidades Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) y RWTH University Aachen, Alemania. algunas propiedades pueden tener un tipo incorrecto. Este es el caso, por favor, plantee un problema o envíe un correo a alberto.abella@fiware.org  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
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
    bwh1:    
      description: 'Notch filter 1 (high-frequency band): Three dB bandwidth (B). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    bwh2:    
      description: 'Notch filter 2 (high-frequency band): Three dB bandwidth (B). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    bwl1:    
      description: 'Notch filter 1 (low-frequency band): Three dB bandwidth (B). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    bwl2:    
      description: 'Notch filter 2 (low-frequency band): Three dB bandwidth (B). Default: 0.0'    
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
      type: Property    
    kh:    
      description: 'High band gain (K).  Typical Value = 120. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kh1:    
      description: 'High band differential filter gain (K).  Typical Value = 66. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kh11:    
      description: 'High band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kh17:    
      description: 'High band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kh2:    
      description: 'High band differential filter gain (K).  Typical Value = 66. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ki:    
      description: 'Intermediate band gain (K).  Typical Value = 30. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ki1:    
      description: 'Intermediate band differential filter gain (K).  Typical Value = 66. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ki11:    
      description: 'Intermediate band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ki17:    
      description: 'Intermediate band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ki2:    
      description: 'Intermediate band differential filter gain (K).  Typical Value = 66. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kl:    
      description: 'Low band gain (K).  Typical Value = 7.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kl1:    
      description: 'Low band differential filter gain (K).  Typical Value = 66. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kl11:    
      description: 'Low band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kl17:    
      description: 'Low band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kl2:    
      description: 'Low band differential filter gain (K).  Typical Value = 66. Default: 0.0'    
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
    omeganh1:    
      description: 'Notch filter 1 (high-frequency band): filter frequency (omega). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    omeganh2:    
      description: 'Notch filter 2 (high-frequency band): filter frequency (omega). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    omeganl1:    
      description: 'Notch filter 1 (low-frequency band): filter frequency (omega). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    omeganl2:    
      description: 'Notch filter 2 (low-frequency band): filter frequency (omega). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *pssieee4b_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
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
    th1:    
      description: 'High band time constant (T).  Typical Value = 0.01513. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    th10:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    th11:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    th12:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    th2:    
      description: 'High band time constant (T).  Typical Value = 0.01816. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    th3:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    th4:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    th5:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    th6:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    th7:    
      description: 'High band time constant (T).  Typical Value = 0.01816. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    th8:    
      description: 'High band time constant (T).  Typical Value = 0.02179. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    th9:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ti1:    
      description: 'Intermediate band time constant (T).  Typical Value = 0.173. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ti10:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ti11:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ti12:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ti2:    
      description: 'Intermediate band time constant (T).  Typical Value = 0.2075. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ti3:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ti4:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ti5:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ti6:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ti7:    
      description: 'Intermediate band time constant (T).  Typical Value = 0.2075. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ti8:    
      description: 'Intermediate band time constant (T).  Typical Value = 0.2491. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ti9:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tl1:    
      description: 'Low band time constant (T).  Typical Value = 1.73. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tl10:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tl11:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tl12:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tl2:    
      description: 'Low band time constant (T).  Typical Value = 2.075. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tl3:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tl4:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tl5:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tl6:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tl7:    
      description: 'Low band time constant (T).  Typical Value = 2.075. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tl8:    
      description: 'Low band time constant (T).  Typical Value = 2.491. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tl9:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be PssIEEE4B'    
      enum:    
        - PssIEEE4B    
      type: Property    
    vhmax:    
      description: 'High band output maximum limit (V).  Typical Value = 0.6. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vhmin:    
      description: 'High band output minimum limit (V).  Typical Value = -0.6. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vimax:    
      description: 'Intermediate band output maximum limit (V).  Typical Value = 0.6. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vimin:    
      description: 'Intermediate band output minimum limit (V).  Typical Value = -0.6. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vlmax:    
      description: 'Low band output maximum limit (V).  Typical Value = 0.075. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vlmin:    
      description: 'Low band output minimum limit (V).  Typical Value = -0.075. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vstmax:    
      description: 'PSS output maximum limit (V).  Typical Value = 0.15. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vstmin:    
      description: 'PSS output minimum limit (V).  Typical Value = -0.15. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
No está disponible el ejemplo de un PssIEEE4B en formato JSON como key-values. Esto es compatible con NGSI V2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un PssIEEE4B en formato JSON como normalizado. Esto es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de una PssIEEE4B en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un PssIEEE4B en formato JSON-LD como normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
