Entidad: GovCT2  
===============  
[Licencia abierta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovCT2/LICENSE.md)  
Descripción global: **Adaptado de los modelos de datos CIM. Modelo de regulador general con límite de flujo de combustible dependiente de la frecuencia.  Este modelo es una modificación del modelo GovCT1 para representar el límite de flujo de combustible dependiente de la frecuencia de un fabricante específico de turbinas de gas.  

## Lista de propiedades  

- `address`: La dirección postal.  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `aset`: Consigna del limitador de aceleración (Aset).  Unidad = PU/seg.  Valor típico = 10. Por defecto: 0,0  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `db`: Banda muerta del regulador de velocidad por unidad de velocidad (db).  En la mayoría de las aplicaciones, se recomienda que este valor se ajuste a cero.  Valor típico = 0. Por defecto: 0.0  - `description`: Una descripción de este artículo  - `dm`: Coeficiente de sensibilidad a la velocidad (Dm).  Dm puede representar la variación de la potencia del motor con la velocidad del eje o la variación de la capacidad de potencia máxima con la velocidad del eje.  Si es positivo, describe la pendiente descendente de la característica de velocidad del motor frente a la potencia a medida que aumenta la velocidad. Una característica ligeramente descendente es típica de los motores alternativos y de algunas turbinas aero-derivadas.  Si es negativo, se supone que la potencia del motor no se ve afectada por la velocidad del eje, pero se considera que el caudal de combustible máximo admisible disminuye al disminuir la velocidad del eje. Esto es característico de las turbinas industriales de un solo eje debido a los límites de temperatura de escape.  Valor típico = 0. Por defecto: 0.0  - `flim1`: Umbral de frecuencia 1 (Flim1).  Unidad = Hz.  Valor típico = 59. Por defecto: 0,0  - `flim10`: Umbral de frecuencia 10 (Flim10).  Unidad = Hz.  Valor típico = 0. Por defecto: 0.0  - `flim2`: Umbral de frecuencia 2 (Flim2).  Unidad = Hz.  Valor típico = 0. Por defecto: 0.0  - `flim3`: Umbral de frecuencia 3 (Flim3).  Unidad = Hz.  Valor típico = 0. Por defecto: 0.0  - `flim4`: Umbral de frecuencia 4 (Flim4).  Unidad = Hz.  Valor típico = 0. Por defecto: 0.0  - `flim5`: Umbral de frecuencia 5 (Flim5).  Unidad = Hz.  Valor típico = 0. Por defecto: 0.0  - `flim6`: Umbral de frecuencia 6 (Flim6).  Unidad = Hz.  Valor típico = 0. Por defecto: 0.0  - `flim7`: Umbral de frecuencia 7 (Flim7).  Unidad = Hz.  Valor típico = 0. Por defecto: 0.0  - `flim8`: Umbral de frecuencia 8 (Flim8).  Unidad = Hz.  Valor típico = 0. Por defecto: 0.0  - `flim9`: Umbral de frecuencia 9 (Flim9).  Unidad = Hz.  Valor típico = 0. Por defecto: 0.0  - `id`: Identificador único de la entidad  - `ka`: Ganancia del limitador de aceleración (Ka).  Valor típico = 10. Por defecto: 0,0  - `kdgov`: Ganancia de la derivada del regulador (Kdgov).  Valor típico = 0. Por defecto: 0.0  - `kigov`: Ganancia integral del regulador (Kigov).  Valor típico = 0,45. Por defecto: 0,0  - `kiload`: Ganancia integral del limitador de carga para el controlador PI (Kiload).  Valor típico = 1. Por defecto: 0,0  - `kimw`: Ganancia del controlador de potencia (reset) (Kimw).  El valor por defecto de 0,01 corresponde a un tiempo de rearme de 100 segundos.  Un valor de 0,001 corresponde a un controlador de carga de acción relativamente lenta.  Valor típico = 0. Por defecto: 0,0  - `kpgov`: Ganancia proporcional del regulador (Kpgov).  Valor típico = 4. Por defecto: 0,0  - `kpload`: Ganancia proporcional del limitador de carga para el controlador PI (Kpload).  Valor típico = 1. Por defecto: 0,0  - `kturb`: Ganancia de la turbina (Kturb).  Valor típico = 1,9168. Por defecto: 0,0  - `ldref`: Valor de referencia del limitador de carga (Ldref).  Valor típico = 1. Por defecto: 0,0  - `location`:   - `maxerr`: Valor máximo de la señal de error de velocidad (Maxerr).  Valor típico = 1. Por defecto: 0,0  - `minerr`: Valor mínimo de la señal de error de velocidad (Minerr).  Valor típico = -1. Por defecto: 0,0  - `mwbase`: Base para los valores de potencia (MWbase) (> 0).  Unidad = MW. Por defecto: 0,0  - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `plim1`: Límite de potencia 1 (Plim1).  Valor típico = 0,8325. Por defecto: 0,0  - `plim10`: Límite de potencia 10 (Plim10).  Valor típico = 0. Por defecto: 0.0  - `plim2`: Límite de potencia 2 (Plim2).  Valor típico = 0. Por defecto: 0.0  - `plim3`: Límite de potencia 3 (Plim3).  Valor típico = 0. Por defecto: 0.0  - `plim4`: Límite de potencia 4 (Plim4).  Valor típico = 0. Por defecto: 0.0  - `plim5`: Límite de potencia 5 (Plim5).  Valor típico = 0. Por defecto: 0.0  - `plim6`: Límite de potencia 6 (Plim6).  Valor típico = 0. Por defecto: 0.0  - `plim7`: Límite de potencia 7 (Plim7).  Valor típico = 0. Por defecto: 0.0  - `plim8`: Límite de potencia 8 (Plim8).  Valor típico = 0. Por defecto: 0.0  - `plim9`: Límite de potencia 9 (Plim9).  Valor típico = 0. Por defecto: 0.0  - `prate`: Tasa de rampa para el límite de potencia dependiente de la frecuencia (Prate).  Valor típico = 0,017. Por defecto: 0,0  - `r`: Caída permanente (R).  Valor típico = 0,05. Por defecto: 0,0  - `rclose`: Velocidad mínima de cierre de la válvula (Rclose).  Unidad = PU/seg.  Valor típico = -99. Por defecto: 0,0  - `rdown`: Tasa máxima de disminución del límite de carga (Rdown).  Valor típico = -99. Por defecto: 0,0  - `ropen`: Velocidad máxima de apertura de la válvula (Ropen).  Unidad = PU/seg.  Valor típico = 99. Por defecto: 0,0  - `rselect`: Señal de retroalimentación para el estatismo (Rselect).  Valor típico = electricalPower. Por defecto: Ninguno  - `rup`: Tasa máxima de aumento del límite de carga (Rup).  Valor típico = 99. Por defecto: 0,0  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `ta`: Constante de tiempo del limitador de aceleración (Ta).  Valor típico = 1. Por defecto: 0  - `tact`: Constante de tiempo del actuador (Tact).  Valor típico = 0,4. Por defecto: 0  - `tb`: Constante de tiempo de retraso de la turbina (Tb).  Valor típico = 0,1. Por defecto: 0  - `tc`: Constante de tiempo de espera de la turbina (Tc).  Valor típico = 0. Por defecto: 0  - `tdgov`: Constante de tiempo del controlador derivado del gobernador (Tdgov).  Valor típico = 1. Por defecto: 0  - `teng`: Retraso del tiempo de transporte para el motor diésel utilizado en la representación de motores diésel en los que existe un pequeño pero medible retraso de transporte entre un cambio en el ajuste del flujo de combustible y el desarrollo del par motor (Teng).  Teng debe ser cero en todos los casos, excepto en los especiales, en los que este retardo de transporte es de especial interés.  Valor típico = 0. Por defecto: 0  - `tfload`: Constante de tiempo del limitador de carga (Tfload).  Valor típico = 3. Por defecto: 0  - `tpelec`: Constante de tiempo del transductor de potencia eléctrica (Tpelec).  Valor típico = 2,5. Por defecto: 0  - `tsa`: Constante de tiempo de espera de detección de temperatura (Tsa).  Valor típico = 0. Por defecto: 0  - `tsb`: Constante de tiempo de retardo en la detección de temperatura (Tsb).  Valor típico = 50. Por defecto: 0  - `type`: Tipo de NGSI. Tiene que ser GovCT2  - `vmax`: Límite de posición máxima de la válvula (Vmax).  Valor típico = 1. Por defecto: 0,0  - `vmin`: Límite mínimo de posición de la válvula (Vmin).  Valor típico = 0,175. Por defecto: 0,0  - `wfnl`: Caudal de combustible en vacío (Wfnl).  Valor típico = 0,187. Por defecto: 0,0  - `wfspd`: Interruptor para que la característica de la fuente de combustible reconozca que el flujo de combustible, para una carrera dada de la válvula de combustible, puede ser proporcional a la velocidad del motor (Wfspd). verdadero = flujo de combustible proporcional a la velocidad (para algunas turbinas de gas y motores diesel con inyectores de combustible de desplazamiento positivo) falso = el sistema de control de combustible mantiene el flujo de combustible independiente de la velocidad del motor. Valor típico = falso. Por defecto: Falso    
Propiedades requeridas  
Este modelo de datos es una conversión directa del Modelo de Información Común (CIM) especificado por la norma IEC61970 en modelos de datos inteligentes. Las clases de python en las que se basa este modelo fueron desarrolladas por estas entidades Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) y RWTH University Aachen, Alemania. algunas propiedades pueden tener un tipo incorrecto. Este es el caso, por favor, plantee un problema o envíe un correo a alberto.abella@fiware.org  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GovCT2:    
  description: 'Adapted from CIM data models. General governor model with frequency-dependent fuel flow limit.  This model is a modification of the GovCT1model in order to represent the frequency-dependent fuel flow limit of a specific gas turbine manufacturer.'    
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
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    aset:    
      description: 'Acceleration limiter setpoint (Aset).  Unit = PU/sec.  Typical Value = 10. Default: 0.0'    
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
    db:    
      description: 'Speed governor dead band in per unit speed (db).  In the majority of applications, it is recommended that this value be set to zero.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    description:    
      description: 'A description of this item'    
      type: Property    
    dm:    
      description: 'Speed sensitivity coefficient (Dm).  Dm can represent either the variation of the engine power with the shaft speed or the variation of maximum power capability with shaft speed.  If it is positive it describes the falling slope of the engine speed verses power characteristic as speed increases. A slightly falling characteristic is typical for reciprocating engines and some aero-derivative turbines.  If it is negative the engine power is assumed to be unaffected by the shaft speed, but the maximum permissible fuel flow is taken to fall with falling shaft speed. This is characteristic of single-shaft industrial turbines due to exhaust temperature limits.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    flim1:    
      description: 'Frequency threshold 1 (Flim1).  Unit = Hz.  Typical Value = 59. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    flim10:    
      description: 'Frequency threshold 10 (Flim10).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    flim2:    
      description: 'Frequency threshold 2 (Flim2).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    flim3:    
      description: 'Frequency threshold 3 (Flim3).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    flim4:    
      description: 'Frequency threshold 4 (Flim4).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    flim5:    
      description: 'Frequency threshold 5 (Flim5).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    flim6:    
      description: 'Frequency threshold 6 (Flim6).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    flim7:    
      description: 'Frequency threshold 7 (Flim7).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    flim8:    
      description: 'Frequency threshold 8 (Flim8).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    flim9:    
      description: 'Frequency threshold 9 (Flim9).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &govct2_-_properties_-_owner_-_items_-_anyof    
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
    ka:    
      description: 'Acceleration limiter Gain (Ka).  Typical Value = 10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kdgov:    
      description: 'Governor derivative gain (Kdgov).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kigov:    
      description: 'Governor integral gain (Kigov).  Typical Value = 0.45. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kiload:    
      description: 'Load limiter integral gain for PI controller (Kiload).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kimw:    
      description: 'Power controller (reset) gain (Kimw).  The default value of 0.01 corresponds to a reset time of 100 seconds.  A value of 0.001 corresponds to a relatively slow acting load controller.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kpgov:    
      description: 'Governor proportional gain (Kpgov).  Typical Value = 4. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kpload:    
      description: 'Load limiter proportional gain for PI controller (Kpload).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kturb:    
      description: 'Turbine gain (Kturb).  Typical Value = 1.9168. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ldref:    
      description: 'Load limiter reference value (Ldref).  Typical Value = 1. Default: 0.0'    
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
    maxerr:    
      description: 'Maximum value for speed error signal (Maxerr).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    minerr:    
      description: 'Minimum value for speed error signal (Minerr).  Typical Value = -1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    mwbase:    
      description: 'Base for power values (MWbase) (> 0).  Unit = MW. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *govct2_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    plim1:    
      description: 'Power limit 1 (Plim1).  Typical Value = 0.8325. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    plim10:    
      description: 'Power limit 10 (Plim10).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    plim2:    
      description: 'Power limit 2 (Plim2).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    plim3:    
      description: 'Power limit 3 (Plim3).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    plim4:    
      description: 'Power limit 4 (Plim4).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    plim5:    
      description: 'Power limit 5 (Plim5).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    plim6:    
      description: 'Power limit 6 (Plim6).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    plim7:    
      description: 'Power limit 7 (Plim7).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    plim8:    
      description: 'Power limit 8 (Plim8).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    plim9:    
      description: 'Power Limit 9 (Plim9).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    prate:    
      description: 'Ramp rate for frequency-dependent power limit (Prate).  Typical Value = 0.017. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    r:    
      description: 'Permanent droop (R).  Typical Value = 0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rclose:    
      description: 'Minimum valve closing rate (Rclose).  Unit = PU/sec.  Typical Value = -99. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rdown:    
      description: 'Maximum rate of load limit decrease (Rdown).  Typical Value = -99. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ropen:    
      description: 'Maximum valve opening rate (Ropen).  Unit = PU/sec.  Typical Value = 99. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rselect:    
      description: 'Feedback signal for droop (Rselect).  Typical Value = electricalPower. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rup:    
      description: 'Maximum rate of load limit increase (Rup).  Typical Value = 99. Default: 0.0'    
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
      description: 'Acceleration limiter time constant (Ta).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tact:    
      description: 'Actuator time constant (Tact).  Typical Value = 0.4. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tb:    
      description: 'Turbine lag time constant (Tb).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tc:    
      description: 'Turbine lead time constant (Tc).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tdgov:    
      description: 'Governor derivative controller time constant (Tdgov).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    teng:    
      description: 'Transport time delay for diesel engine used in representing diesel engines where there is a small but measurable transport delay between a change in fuel flow setting and the development of torque (Teng).  Teng should be zero in all but special cases where this transport delay is of particular concern.  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tfload:    
      description: 'Load Limiter time constant (Tfload).  Typical Value = 3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tpelec:    
      description: 'Electrical power transducer time constant (Tpelec).  Typical Value = 2.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tsa:    
      description: 'Temperature detection lead time constant (Tsa).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tsb:    
      description: 'Temperature detection lag time constant (Tsb).  Typical Value = 50. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be GovCT2'    
      enum:    
        - GovCT2    
      type: Property    
    vmax:    
      description: 'Maximum valve position limit (Vmax).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vmin:    
      description: 'Minimum valve position limit (Vmin).  Typical Value = 0.175. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    wfnl:    
      description: 'No load fuel flow (Wfnl).  Typical Value = 0.187. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    wfspd:    
      description: 'Switch for fuel source characteristic to recognize that fuel flow, for a given fuel valve stroke, can be proportional to engine speed (Wfspd). true = fuel flow proportional to speed (for some gas turbines and diesel engines with positive displacement fuel injectors) false = fuel control system keeps fuel flow independent of engine speed. Typical Value = false. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
No está disponible el ejemplo de un GovCT2 en formato JSON como key-values. Esto es compatible con NGSI V2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un GovCT2 en formato JSON normalizado. Esto es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un GovCT2 en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un GovCT2 en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
