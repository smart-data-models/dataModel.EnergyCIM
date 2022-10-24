<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: GovCT2  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovCT2/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Adaptado de los modelos de datos CIM. Modelo de regulador general con límite de flujo de combustible dependiente de la frecuencia.  Este modelo es una modificación del modelo GovCT1 para representar el límite de flujo de combustible dependiente de la frecuencia de un fabricante específico de turbinas de gas.  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>  
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `aset[number]`: Consigna del limitador de aceleración (Aset).  Unidad = PU/seg.  Valor típico = 10. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated[string]`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified[string]`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `db[number]`: Banda muerta del regulador de velocidad por unidad de velocidad (db).  En la mayoría de las aplicaciones, se recomienda que este valor se ajuste a cero.  Valor típico = 0. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: Una descripción de este artículo  - `dm[number]`: Coeficiente de sensibilidad a la velocidad (Dm).  Dm puede representar la variación de la potencia del motor con la velocidad del eje o la variación de la capacidad de potencia máxima con la velocidad del eje.  Si es positivo, describe la pendiente descendente de la característica de velocidad del motor frente a la potencia a medida que aumenta la velocidad. Una característica ligeramente descendente es típica de los motores alternativos y de algunas turbinas aero-derivadas.  Si es negativo, se supone que la potencia del motor no se ve afectada por la velocidad del eje, pero se considera que el caudal de combustible máximo admisible disminuye al disminuir la velocidad del eje. Esto es característico de las turbinas industriales de un solo eje debido a los límites de temperatura de escape.  Valor típico = 0. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `flim1[number]`: Umbral de frecuencia 1 (Flim1).  Unidad = Hz.  Valor típico = 59. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `flim10[number]`: Umbral de frecuencia 10 (Flim10).  Unidad = Hz.  Valor típico = 0. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `flim2[number]`: Umbral de frecuencia 2 (Flim2).  Unidad = Hz.  Valor típico = 0. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `flim3[number]`: Umbral de frecuencia 3 (Flim3).  Unidad = Hz.  Valor típico = 0. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `flim4[number]`: Umbral de frecuencia 4 (Flim4).  Unidad = Hz.  Valor típico = 0. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `flim5[number]`: Umbral de frecuencia 5 (Flim5).  Unidad = Hz.  Valor típico = 0. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `flim6[number]`: Umbral de frecuencia 6 (Flim6).  Unidad = Hz.  Valor típico = 0. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `flim7[number]`: Umbral de frecuencia 7 (Flim7).  Unidad = Hz.  Valor típico = 0. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `flim8[number]`: Umbral de frecuencia 8 (Flim8).  Unidad = Hz.  Valor típico = 0. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `flim9[number]`: Umbral de frecuencia 9 (Flim9).  Unidad = Hz.  Valor típico = 0. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identificador único de la entidad  - `ka[number]`: Ganancia del limitador de aceleración (Ka).  Valor típico = 10. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kdgov[number]`: Ganancia de la derivada del regulador (Kdgov).  Valor típico = 0. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kigov[number]`: Ganancia integral del regulador (Kigov).  Valor típico = 0,45. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kiload[number]`: Ganancia integral del limitador de carga para el controlador PI (Kiload).  Valor típico = 1. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kimw[number]`: Ganancia del controlador de potencia (reset) (Kimw).  El valor por defecto de 0,01 corresponde a un tiempo de rearme de 100 segundos.  Un valor de 0,001 corresponde a un controlador de carga de acción relativamente lenta.  Valor típico = 0. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kpgov[number]`: Ganancia proporcional del regulador (Kpgov).  Valor típico = 4. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kpload[number]`: Ganancia proporcional del limitador de carga para el controlador PI (Kpload).  Valor típico = 1. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kturb[number]`: Ganancia de la turbina (Kturb).  Valor típico = 1,9168. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ldref[number]`: Valor de referencia del limitador de carga (Ldref).  Valor típico = 1. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `maxerr[number]`: Valor máximo de la señal de error de velocidad (Maxerr).  Valor típico = 1. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `minerr[number]`: Valor mínimo de la señal de error de velocidad (Minerr).  Valor típico = -1. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `mwbase[number]`: Base para valores de potencia (MWbase) (> 0).  Unidad = MW. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: El nombre de este artículo.  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `plim1[number]`: Límite de potencia 1 (Plim1).  Valor típico = 0,8325. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `plim10[number]`: Límite de potencia 10 (Plim10).  Valor típico = 0. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `plim2[number]`: Límite de potencia 2 (Plim2).  Valor típico = 0. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `plim3[number]`: Límite de potencia 3 (Plim3).  Valor típico = 0. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `plim4[number]`: Límite de potencia 4 (Plim4).  Valor típico = 0. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `plim5[number]`: Límite de potencia 5 (Plim5).  Valor típico = 0. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `plim6[number]`: Límite de potencia 6 (Plim6).  Valor típico = 0. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `plim7[number]`: Límite de potencia 7 (Plim7).  Valor típico = 0. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `plim8[number]`: Límite de potencia 8 (Plim8).  Valor típico = 0. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `plim9[number]`: Límite de potencia 9 (Plim9).  Valor típico = 0. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `prate[number]`: Tasa de rampa para el límite de potencia dependiente de la frecuencia (Prate).  Valor típico = 0,017. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `r[number]`: Caída permanente (R).  Valor típico = 0,05. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rclose[number]`: Velocidad mínima de cierre de la válvula (Rclose).  Unidad = PU/seg.  Valor típico = -99. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rdown[number]`: Tasa máxima de disminución del límite de carga (Rdown).  Valor típico = -99. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ropen[number]`: Velocidad máxima de apertura de la válvula (Ropen).  Unidad = PU/seg.  Valor típico = 99. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rselect[number]`: Señal de retroalimentación para el estatismo (Rselect).  Valor típico = electricalPower. Por defecto: Ninguno  . Model: [https://schema.org/Number](https://schema.org/Number)- `rup[number]`: Tasa máxima de aumento del límite de carga (Rup).  Valor típico = 99. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `ta[number]`: Constante de tiempo del limitador de aceleración (Ta).  Valor típico = 1. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tact[number]`: Constante de tiempo del actuador (Tact).  Valor típico = 0,4. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tb[number]`: Constante de tiempo de retraso de la turbina (Tb).  Valor típico = 0,1. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tc[number]`: Constante de tiempo de espera de la turbina (Tc).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tdgov[number]`: Constante de tiempo del controlador derivado del gobernador (Tdgov).  Valor típico = 1. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `teng[number]`: Retraso del tiempo de transporte para el motor diésel utilizado en la representación de motores diésel en los que existe un pequeño pero medible retraso de transporte entre un cambio en el ajuste del flujo de combustible y el desarrollo del par motor (Teng).  Teng debe ser cero en todos los casos, excepto en los especiales, en los que este retardo de transporte es de especial interés.  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tfload[number]`: Constante de tiempo del limitador de carga (Tfload).  Valor típico = 3. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tpelec[number]`: Constante de tiempo del transductor de potencia eléctrica (Tpelec).  Valor típico = 2,5. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tsa[number]`: Constante de tiempo de espera de detección de temperatura (Tsa).  Valor típico = 0. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tsb[number]`: Constante de tiempo de retardo en la detección de temperatura (Tsb).  Valor típico = 50. Por defecto: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Tipo de NGSI. Tiene que ser GovCT2  - `vmax[number]`: Límite de posición máxima de la válvula (Vmax).  Valor típico = 1. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vmin[number]`: Límite mínimo de posición de la válvula (Vmin).  Valor típico = 0,175. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `wfnl[number]`: Caudal de combustible en vacío (Wfnl).  Valor típico = 0,187. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `wfspd[number]`: Interruptor para que la característica de la fuente de combustible reconozca que el flujo de combustible, para una carrera dada de la válvula de combustible, puede ser proporcional a la velocidad del motor (Wfspd). verdadero = flujo de combustible proporcional a la velocidad (para algunas turbinas de gas y motores diesel con inyectores de combustible de desplazamiento positivo) falso = el sistema de control de combustible mantiene el flujo de combustible independiente de la velocidad del motor. Valor típico = falso. Por defecto: Falso  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
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
GovCT2:    
  description: 'Adapted from CIM data models. General governor model with frequency-dependent fuel flow limit.  This model is a modification of the GovCT1model in order to represent the frequency-dependent fuel flow limit of a specific gas turbine manufacturer.'    
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
    aset:    
      description: 'Acceleration limiter setpoint (Aset).  Unit = PU/sec.  Typical Value = 10. Default: 0.0'    
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
    db:    
      description: 'Speed governor dead band in per unit speed (db).  In the majority of applications, it is recommended that this value be set to zero.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    dm:    
      description: 'Speed sensitivity coefficient (Dm).  Dm can represent either the variation of the engine power with the shaft speed or the variation of maximum power capability with shaft speed.  If it is positive it describes the falling slope of the engine speed verses power characteristic as speed increases. A slightly falling characteristic is typical for reciprocating engines and some aero-derivative turbines.  If it is negative the engine power is assumed to be unaffected by the shaft speed, but the maximum permissible fuel flow is taken to fall with falling shaft speed. This is characteristic of single-shaft industrial turbines due to exhaust temperature limits.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    flim1:    
      description: 'Frequency threshold 1 (Flim1).  Unit = Hz.  Typical Value = 59. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    flim10:    
      description: 'Frequency threshold 10 (Flim10).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    flim2:    
      description: 'Frequency threshold 2 (Flim2).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    flim3:    
      description: 'Frequency threshold 3 (Flim3).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    flim4:    
      description: 'Frequency threshold 4 (Flim4).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    flim5:    
      description: 'Frequency threshold 5 (Flim5).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    flim6:    
      description: 'Frequency threshold 6 (Flim6).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    flim7:    
      description: 'Frequency threshold 7 (Flim7).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    flim8:    
      description: 'Frequency threshold 8 (Flim8).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    flim9:    
      description: 'Frequency threshold 9 (Flim9).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
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
      x-ngsi:    
        type: Property    
    ka:    
      description: 'Acceleration limiter Gain (Ka).  Typical Value = 10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kdgov:    
      description: 'Governor derivative gain (Kdgov).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kigov:    
      description: 'Governor integral gain (Kigov).  Typical Value = 0.45. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kiload:    
      description: 'Load limiter integral gain for PI controller (Kiload).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kimw:    
      description: 'Power controller (reset) gain (Kimw).  The default value of 0.01 corresponds to a reset time of 100 seconds.  A value of 0.001 corresponds to a relatively slow acting load controller.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kpgov:    
      description: 'Governor proportional gain (Kpgov).  Typical Value = 4. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kpload:    
      description: 'Load limiter proportional gain for PI controller (Kpload).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kturb:    
      description: 'Turbine gain (Kturb).  Typical Value = 1.9168. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ldref:    
      description: 'Load limiter reference value (Ldref).  Typical Value = 1. Default: 0.0'    
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
    maxerr:    
      description: 'Maximum value for speed error signal (Maxerr).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    minerr:    
      description: 'Minimum value for speed error signal (Minerr).  Typical Value = -1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    mwbase:    
      description: 'Base for power values (MWbase) (> 0).  Unit = MW. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *govct2_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    plim1:    
      description: 'Power limit 1 (Plim1).  Typical Value = 0.8325. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    plim10:    
      description: 'Power limit 10 (Plim10).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    plim2:    
      description: 'Power limit 2 (Plim2).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    plim3:    
      description: 'Power limit 3 (Plim3).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    plim4:    
      description: 'Power limit 4 (Plim4).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    plim5:    
      description: 'Power limit 5 (Plim5).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    plim6:    
      description: 'Power limit 6 (Plim6).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    plim7:    
      description: 'Power limit 7 (Plim7).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    plim8:    
      description: 'Power limit 8 (Plim8).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    plim9:    
      description: 'Power Limit 9 (Plim9).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    prate:    
      description: 'Ramp rate for frequency-dependent power limit (Prate).  Typical Value = 0.017. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    r:    
      description: 'Permanent droop (R).  Typical Value = 0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rclose:    
      description: 'Minimum valve closing rate (Rclose).  Unit = PU/sec.  Typical Value = -99. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rdown:    
      description: 'Maximum rate of load limit decrease (Rdown).  Typical Value = -99. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ropen:    
      description: 'Maximum valve opening rate (Ropen).  Unit = PU/sec.  Typical Value = 99. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rselect:    
      description: 'Feedback signal for droop (Rselect).  Typical Value = electricalPower. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rup:    
      description: 'Maximum rate of load limit increase (Rup).  Typical Value = 99. Default: 0.0'    
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
    ta:    
      description: 'Acceleration limiter time constant (Ta).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tact:    
      description: 'Actuator time constant (Tact).  Typical Value = 0.4. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tb:    
      description: 'Turbine lag time constant (Tb).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tc:    
      description: 'Turbine lead time constant (Tc).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tdgov:    
      description: 'Governor derivative controller time constant (Tdgov).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    teng:    
      description: 'Transport time delay for diesel engine used in representing diesel engines where there is a small but measurable transport delay between a change in fuel flow setting and the development of torque (Teng).  Teng should be zero in all but special cases where this transport delay is of particular concern.  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tfload:    
      description: 'Load Limiter time constant (Tfload).  Typical Value = 3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tpelec:    
      description: 'Electrical power transducer time constant (Tpelec).  Typical Value = 2.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tsa:    
      description: 'Temperature detection lead time constant (Tsa).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tsb:    
      description: 'Temperature detection lag time constant (Tsb).  Typical Value = 50. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be GovCT2'    
      enum:    
        - GovCT2    
      type: string    
      x-ngsi:    
        type: Property    
    vmax:    
      description: 'Maximum valve position limit (Vmax).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vmin:    
      description: 'Minimum valve position limit (Vmin).  Typical Value = 0.175. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    wfnl:    
      description: 'No load fuel flow (Wfnl).  Typical Value = 0.187. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    wfspd:    
      description: 'Switch for fuel source characteristic to recognize that fuel flow, for a given fuel valve stroke, can be proportional to engine speed (Wfspd). true = fuel flow proportional to speed (for some gas turbines and diesel engines with positive displacement fuel injectors) false = fuel control system keeps fuel flow independent of engine speed. Typical Value = false. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovCT2/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/GovCT2/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
No está disponible el ejemplo de un GovCT2 en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un GovCT2 en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un GovCT2 en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un GovCT2 en formato JSON-LD normalizado. Es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
