Entidad: LoadComposite  
======================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/LoadComposite/LICENSE.md)  
Descripción global: **Adaptado de los modelos de datos CIM. Este modelo combina los efectos de la carga estática y de la carga del motor de inducción. La dinámica del motor se simplifica linealizando las ecuaciones de la máquina de inducción.**  

## Lista de propiedades  

- `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `epfd`: Índice de dependencia carga-frecuencia activa (dinámica) (Epfd).  Valor típico = 1,5. Por defecto: 0,0  - `epfs`: Índice de dependencia carga-frecuencia activa (estática) (Epfs).  Valor típico = 1,5. Por defecto: 0,0  - `epvd`: Índice de dependencia carga-tensión activa (dinámica) (Epvd).  Valor típico = 0,7. Por defecto: 0,0  - `epvs`: Índice de dependencia carga-tensión activa (estática) (Epvs).  Valor típico = 0,7. Por defecto: 0,0  - `eqfd`: Índice de dependencia carga reactiva-frecuencia (dinámica) (Eqfd).  Valor típico = 0. Por defecto: 0.0  - `eqfs`: Índice de dependencia carga reactiva-frecuencia (estática) (Eqfs).  Valor típico = 0. Por defecto: 0.0  - `eqvd`: Índice de dependencia carga reactiva-tensión (dinámica) (Eqvd).  Valor típico = 2. Por defecto: 0,0  - `eqvs`: Índice de dependencia carga reactiva-voltaje (estático) (Eqvs).  Valor típico = 2. Por defecto: 0,0  - `h`: Constante de inercia (H).  Valor típico = 2,5. Por defecto: 0  - `id`: Identificador único de la entidad  - `lfrac`: Factor de carga - relación entre la P inicial y la base de MVA del motor (Lfrac).  Valor típico = 0,8. Por defecto: 0,0  - `location`:   - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `pfrac`: Fracción de carga de potencia constante que debe representar este modelo de motor (Pfrac) (>=0,0 y <=1,0).  Valor típico = 0,5. Por defecto: 0,0  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `type`: Tipo de NGSI. Tiene que ser LoadComposite    
Propiedades requeridas  
Este modelo de datos es una conversión directa del Modelo de Información Común (CIM) especificado por la norma IEC61970 en modelos de datos inteligentes. Las clases de python en las que se basa este modelo fueron desarrolladas por estas entidades Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) y RWTH University Aachen, Alemania. algunas propiedades pueden tener un tipo incorrecto. Este es el caso, por favor, plantee un problema o envíe un correo a alberto.abella@fiware.org  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
LoadComposite:    
  description: 'Adapted from CIM data models. This models combines static load and induction motor load effects. The dynamics of the motor are simplified by linearizing the induction machine equations.'    
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
    epfd:    
      description: 'Active load-frequency dependence index (dynamic) (Epfd).  Typical Value = 1.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    epfs:    
      description: 'Active load-frequency dependence index (static) (Epfs).  Typical Value = 1.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    epvd:    
      description: 'Active load-voltage dependence index (dynamic) (Epvd).  Typical Value = 0.7. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    epvs:    
      description: 'Active load-voltage dependence index (static) (Epvs).  Typical Value = 0.7. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    eqfd:    
      description: 'Reactive load-frequency dependence index (dynamic) (Eqfd).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    eqfs:    
      description: 'Reactive load-frequency dependence index (static) (Eqfs).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    eqvd:    
      description: 'Reactive load-voltage dependence index (dynamic) (Eqvd).  Typical Value = 2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    eqvs:    
      description: 'Reactive load-voltage dependence index (static) (Eqvs).  Typical Value = 2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    h:    
      description: 'Inertia constant (H).  Typical Value = 2.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &loadcomposite_-_properties_-_owner_-_items_-_anyof    
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
    lfrac:    
      description: 'Loading factor - ratio of initial P to motor MVA base (Lfrac).  Typical Value = 0.8. Default: 0.0'    
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
        anyOf: *loadcomposite_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    pfrac:    
      description: 'Fraction of constant-power load to be represented by this motor model (Pfrac) (>=0.0 and <=1.0).  Typical Value = 0.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    type:    
      description: 'NGSI type. It has to be LoadComposite'    
      enum:    
        - LoadComposite    
      type: Property    
  required: []    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
No está disponible el ejemplo de un LoadComposite en formato JSON como key-values. Esto es compatible con NGSI V2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un LoadComposite en formato JSON como normalizado. Esto es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un LoadComposite en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un LoadComposite en formato JSON-LD como normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
