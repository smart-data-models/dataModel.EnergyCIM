Entidad: GovHydroFrancis  
========================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovHydroFrancis/LICENSE.md)  
Descripción global: **Adaptado de los modelos de datos de la CIM. Unidad hidroeléctrica detallada - Modelo Francis.  Este modelo puede utilizarse para representar tres tipos de gobernadores. En el diagrama DetailedHydroModelHydraulicSystem se proporciona un esquema del sistema hidráulico de los modelos de unidades hidroeléctricas detalladas, como Francis y Pelton.**  

## Lista de propiedades  

- `address`: La dirección postal.  - `alternateName`: Un nombre alternativo para este artículo  - `am`: Sección de apertura S al máximo rendimiento (Am).  Valor típico = 0,7. Por defecto: 0,0  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `av0`: Área del depósito de compensación (A). Unidad = m. Valor típico = 30. Por defecto: 0,0  - `av1`: Área del depósito de compensación (A). Unidad = m. Valor típico = 700. Por defecto: 0,0  - `bp`: Caída (Bp).  Valor típico = 0,05. Por defecto: 0,0  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `db1`: Ancho de banda muerta intencional (DB1).  Unidad = Hz.  Valor típico = 0. Por defecto: 0.0  - `description`: Una descripción de este artículo  - `etamax`: Eficiencia máxima (EtaMax).  Valor típico = 1,05. Por defecto: 0,0  - `governorControl`: Bandera de control del gobernador (Cflag).  Valor típico = mechanicHydrolicTachoAccelerator. Por defecto: Ninguno  - `h1`: Altura del nivel de agua de la cámara de compensación con respecto al nivel de la tubería forzada (H).  Unidad = m. Valor típico = 4. Por defecto: 0,0  - `h2`: Altura del nivel de agua del depósito de compensación con respecto al nivel de la tubería forzada (H).  Unidad = m. Valor típico = 40. Por defecto: 0,0  - `hn`: Altura hidráulica nominal (H).  Unidad = m. Valor típico = 250. Por defecto: 0,0  - `id`: Identificador único de la entidad  - `kc`: Coeficiente de pérdida de la tubería forzada (debido a la fricción) (Kc).  Valor típico = 0,025. Por defecto: 0,0  - `kg`: Coeficiente de pérdidas en el túnel de agua y en la cámara de sobretensión (debido a la fricción) (Kg).  Valor típico = 0,025. Por defecto: 0,0  - `kt`: Ganancia de lavado (Kt).  Valor típico = 0,25. Por defecto: 0,0  - `location`:   - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `qc0`: Caudal de la turbina en vacío a la altura nominal (Qc0).  Valor típico = 0,21. Por defecto: 0,0  - `qn`: Caudal nominal (Q). Unidad = m/s. Valor típico = 40. Por defecto: 0,0  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `ta`: Ganancia derivativa (Ta).  Valor típico = 3. Por defecto: 0  - `td`: Constante de tiempo de lavado (Td).  Valor típico = 3. Por defecto: 0  - `ts`: Constante de tiempo del servo de la puerta (Ts).  Valor típico = 0,5. Por defecto: 0  - `twnc`: Constante de tiempo de inercia del agua (Twnc).  Valor típico = 1. Por defecto: 0  - `twng`: Constante de tiempo de inercia del túnel de agua y de la cámara de compensación (Twng). Valor típico = 3. Por defecto: 0  - `tx`: Ganancia de retroalimentación derivada (Tx).  Valor típico = 1. Por defecto: 0  - `type`: Tipo NGSI. Tiene que ser GovHydroFrancis  - `va`: Velocidad máxima de apertura de la puerta (Va).  Unidad = PU/seg.  Valor típico = 0,011. Por defecto: 0,0  - `valvmax`: Apertura máxima de la puerta (ValvMax).  Valor típico = 1. Por defecto: 0,0  - `valvmin`: Apertura mínima de la puerta (ValvMin).  Valor típico = 0. Por defecto: 0.0  - `vc`: Velocidad máxima de cierre de la puerta (Vc).  Unidad = PU/seg.  Valor típico = -0,011. Por defecto: 0,0  - `waterTunnelSurgeChamberSimulation`: Simulación del túnel de agua y de la cámara de sobretensión (Tflag). true = habilitar la simulación del túnel de agua y de la cámara de sobretensión false = inhibir la simulación del túnel de agua y de la cámara de sobretensión. Valor típico = falso. Por defecto: Falso  - `zsfc`: Altura del nivel superior del agua con respecto al nivel de la tubería forzada (Zsfc).  Unidad = m. Valor típico = 25. Por defecto: 0,0    
Propiedades requeridas  
Este modelo de datos es una conversión directa del Modelo de Información Común (CIM) especificado por la norma IEC61970 en modelos de datos inteligentes. Las clases de python en las que se basa este modelo fueron desarrolladas por estas entidades Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) y RWTH University Aachen, Alemania. algunas propiedades pueden tener un tipo incorrecto. Este es el caso, por favor, plantee un problema o envíe un correo a alberto.abella@fiware.org  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GovHydroFrancis:    
  description: 'Adapted from CIM data models. Detailed hydro unit - Francis model.  This model can be used to represent three types of governors. A schematic of the hydraulic system of detailed hydro unit models, like Francis and Pelton, is provided in the DetailedHydroModelHydraulicSystem diagram.'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/Text'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/Text'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/Text'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/Text'''    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    am:    
      description: 'Opening section S at the maximum efficiency (Am).  Typical Value = 0.7. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    av0:    
      description: 'Area of the surge tank (A). Unit = m. Typical Value = 30. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    av1:    
      description: 'Area of the compensation tank (A). Unit = m. Typical Value = 700. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    bp:    
      description: 'Droop (Bp).  Typical Value = 0.05. Default: 0.0'    
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
    db1:    
      description: 'Intentional dead-band width (DB1).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    description:    
      description: 'A description of this item'    
      type: Property    
    etamax:    
      description: 'Maximum efficiency (EtaMax).  Typical Value = 1.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    governorControl:    
      description: 'Governor control flag (Cflag).  Typical Value = mechanicHydrolicTachoAccelerator. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    h1:    
      description: 'Head of compensation chamber water level with respect to the level of penstock (H).  Unit = m. Typical Value = 4. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    h2:    
      description: 'Head of surge tank water level with respect to the level of penstock (H).  Unit = m. Typical Value = 40. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    hn:    
      description: 'Rated hydraulic head (H).  Unit = m. Typical Value = 250. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &govhydrofrancis_-_properties_-_owner_-_items_-_anyof    
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
    kc:    
      description: 'Penstock loss coefficient (due to friction) (Kc).  Typical Value = 0.025. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kg:    
      description: 'Water tunnel and surge chamber loss coefficient (due to friction) (Kg).  Typical Value = 0.025. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kt:    
      description: 'Washout gain (Kt).  Typical Value = 0.25. Default: 0.0'    
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
        anyOf: *govhydrofrancis_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    qc0:    
      description: 'No-load turbine flow at nominal head (Qc0).  Typical Value = 0.21. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    qn:    
      description: 'Rated flow (Q). Unit = m/s. Typical Value = 40. Default: 0.0'    
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
    ta:    
      description: 'Derivative gain (Ta).  Typical Value = 3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    td:    
      description: 'Washout time constant (Td).  Typical Value = 3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ts:    
      description: 'Gate servo time constant (Ts).  Typical Value = 0.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    twnc:    
      description: 'Water inertia time constant (Twnc).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    twng:    
      description: 'Water tunnel and surge chamber inertia time constant (Twng). Typical Value = 3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tx:    
      description: 'Derivative feedback gain (Tx).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be GovHydroFrancis'    
      enum:    
        - GovHydroFrancis    
      type: Property    
    va:    
      description: 'Maximum gate opening velocity (Va).  Unit = PU/sec.  Typical Value = 0.011. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    valvmax:    
      description: 'Maximum gate opening (ValvMax).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    valvmin:    
      description: 'Minimum gate opening (ValvMin).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vc:    
      description: 'Maximum gate closing velocity (Vc).  Unit = PU/sec.  Typical Value = -0.011. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    waterTunnelSurgeChamberSimulation:    
      description: 'Water tunnel and surge chamber simulation (Tflag). true = enable of water tunnel and surge chamber simulation false = inhibit of water tunnel and surge chamber simulation. Typical Value = false. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    zsfc:    
      description: 'Head of upper water level with respect to the level of penstock (Zsfc).  Unit = m.  Typical Value = 25. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
No está disponible el ejemplo de un GovHydroFrancis en formato JSON como key-values. Esto es compatible con NGSI V2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un GovHydroFrancis en formato JSON normalizado. Esto es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un GovHydroFrancis en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un GovHydroFrancis en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
