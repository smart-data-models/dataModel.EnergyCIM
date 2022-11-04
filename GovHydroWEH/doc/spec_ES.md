Entidad: GovHydroWEH  
====================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovHydroWEH/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Adaptado de los modelos de datos CIM. Modelo de gobernador hidroeléctrico de Woodward.**  

## Lista de propiedades  

- `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `db`: Banda muerta de velocidad (db). Por defecto: 0,0  - `description`: Una descripción de este artículo  - `dicn`: Valor que permite al regulador integral avanzar más allá de los límites de la puerta (Dicn). Por defecto: 0,0  - `dpv`: Valor que permite al controlador de la válvula piloto avanzar más allá de los límites de la puerta (Dpv). Por defecto: 0,0  - `dturb`: Factor de amortiguación de la turbina (Dturb).  Unidad = delta P (PU de MWbase) / delta velocidad (PU). Por defecto: 0,0  - `feedbackSignal`: Selección de la señal de realimentación (Sw). verdadero = Salida PID (si R-Perm-Gate=droop y R-Perm-Pe=0) falso = Potencia eléctrica (si R-Perm-Gate=0 y R-Perm-Pe=droop) o falso = Posición de la puerta (si R-Perm-Gate=droop y R-Perm-Pe=0). Por defecto: Falso  - `fl1`: Flujo de la compuerta 1 (Fl1).  Valor de flujo para el punto de posición de la compuerta 1 para la tabla de consulta que representa el flujo de agua a través de la turbina como una función de la posición de la compuerta para producir un flujo de estado estable. Por defecto: 0,0  - `fl2`: Flujo de la compuerta 2 (Fl2).  Valor de flujo para el punto de posición de la compuerta 2 para la tabla de consulta que representa el flujo de agua a través de la turbina como una función de la posición de la compuerta para producir un flujo de estado estable. Por defecto: 0,0  - `fl3`: Flujo de la compuerta 3 (Fl3).  Valor de flujo para el punto de posición de la compuerta 3 para la tabla de consulta que representa el flujo de agua a través de la turbina como una función de la posición de la compuerta para producir un flujo de estado estable. Por defecto: 0,0  - `fl4`: Flujo de la compuerta 4 (Fl4).  Valor de flujo para el punto de posición de la compuerta 4 para la tabla de consulta que representa el flujo de agua a través de la turbina como una función de la posición de la compuerta para producir un flujo de estado estable. Por defecto: 0,0  - `fl5`: Flujo de la compuerta 5 (Fl5).  Valor de flujo para el punto de posición de la compuerta 5 para la tabla de consulta que representa el flujo de agua a través de la turbina como una función de la posición de la compuerta para producir un flujo de estado estable. Por defecto: 0,0  - `fp1`: Caudal P1 (Fp1).  Valor del caudal de la turbina para el punto 1 de la tabla de consulta que representa la potencia mecánica por unidad en la clasificación MVA de la máquina en función del caudal de la turbina. Por defecto: 0,0  - `fp10`: Caudal P10 (Fp10).  Valor del caudal de la turbina para el punto 10 de la tabla de consulta que representa la potencia mecánica por unidad en la clasificación MVA de la máquina en función del caudal de la turbina. Por defecto: 0,0  - `fp2`: Caudal P2 (Fp2).  Valor del caudal de la turbina para el punto 2 de la tabla de consulta que representa la potencia mecánica por unidad en la clasificación MVA de la máquina en función del caudal de la turbina. Por defecto: 0,0  - `fp3`: Caudal P3 (Fp3).  Valor del caudal de la turbina para el punto 3 de la tabla de consulta que representa la potencia mecánica por unidad en la clasificación MVA de la máquina en función del caudal de la turbina. Por defecto: 0,0  - `fp4`: Caudal P4 (Fp4).  Valor del caudal de la turbina para el punto 4 de la tabla de consulta que representa la potencia mecánica por unidad en la clasificación MVA de la máquina en función del caudal de la turbina. Por defecto: 0,0  - `fp5`: Caudal P5 (Fp5).  Valor del caudal de la turbina para el punto 5 de la tabla de consulta que representa la potencia mecánica por unidad en la clasificación MVA de la máquina en función del caudal de la turbina. Por defecto: 0,0  - `fp6`: Caudal P6 (Fp6).  Valor del caudal de la turbina para el punto 6 de la tabla de consulta que representa la potencia mecánica por unidad en la clasificación MVA de la máquina en función del caudal de la turbina. Por defecto: 0,0  - `fp7`: Caudal P7 (Fp7).  Valor del caudal de la turbina para el punto 7 de la tabla de consulta que representa la potencia mecánica por unidad en la clasificación MVA de la máquina en función del caudal de la turbina. Por defecto: 0,0  - `fp8`: Caudal P8 (Fp8).  Valor del caudal de la turbina para el punto 8 de la tabla de consulta que representa la potencia mecánica por unidad en la clasificación MVA de la máquina en función del caudal de la turbina. Por defecto: 0,0  - `fp9`: Caudal P9 (Fp9).  Valor del caudal de la turbina para el punto 9 de la tabla de consulta que representa la potencia mecánica por unidad en la clasificación MVA de la máquina en función del caudal de la turbina. Por defecto: 0,0  - `gmax`: Posición máxima de la puerta (Gmax). Por defecto: 0,0  - `gmin`: Posición mínima de la puerta (Gmin). Por defecto: 0,0  - `gtmxcl`: Velocidad máxima de cierre de la puerta (Gtmxcl). Por defecto: 0,0  - `gtmxop`: Tasa máxima de apertura de la puerta (Gtmxop). Por defecto: 0,0  - `gv1`: Puerta 1 (Gv1).  Valor de la posición de la compuerta para el punto 1 de la tabla de consulta que representa el flujo de agua a través de la turbina como una función de la posición de la compuerta para producir un flujo de estado estable. Por defecto: 0.0  - `gv2`: Puerta 2 (Gv2).  Valor de la posición de la compuerta para el punto 2 de la tabla de consulta que representa el flujo de agua a través de la turbina como una función de la posición de la compuerta para producir un flujo de estado estable. Por defecto: 0.0  - `gv3`: Puerta 3 (Gv3).  Valor de la posición de la compuerta para el punto 3 de la tabla de consulta que representa el flujo de agua a través de la turbina como una función de la posición de la compuerta para producir un flujo de estado estable. Por defecto: 0.0  - `gv4`: Puerta 4 (Gv4).  Valor de la posición de la compuerta para el punto 4 de la tabla de consulta que representa el flujo de agua a través de la turbina como una función de la posición de la compuerta para producir un flujo de estado estable. Por defecto: 0.0  - `gv5`: Puerta 5 (Gv5).  Valor de la posición de la compuerta para el punto 5 de la tabla de consulta que representa el flujo de agua a través de la turbina como una función de la posición de la compuerta para producir un flujo de estado estable. Por defecto: 0.0  - `id`: Identificador único de la entidad  - `kd`: Ganancia de la derivada del regulador (Kd). Por defecto: 0,0  - `ki`: Controlador derivativo Ganancia integral (Ki). Por defecto: 0,0  - `kp`: Ganancia de control derivativo (Kp). Por defecto: 0,0  - `location`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `mwbase`: Base para valores de potencia (MWbase) (>0).  Unidad = MW. Por defecto: 0,0  - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `pmss1`: Flujo Pmss P1 (Pmss1).  Potencia mecánica de salida Pmss para el punto 1 de flujo de la turbina para la tabla de consulta que representa la potencia mecánica por unidad en la clasificación MVA de la máquina como función del flujo de la turbina. Por defecto: 0,0  - `pmss10`: Flujo Pmss P10 (Pmss10).  Potencia mecánica de salida Pmss para el punto 10 del caudal de la turbina para la tabla de consulta que representa la potencia mecánica por unidad en la clasificación MVA de la máquina en función del caudal de la turbina. Por defecto: 0,0  - `pmss2`: Flujo Pmss P2 (Pmss2).  Potencia mecánica de salida Pmss para el punto 2 del caudal de la turbina para la tabla de consulta que representa la potencia mecánica por unidad en la clasificación MVA de la máquina en función del caudal de la turbina. Por defecto: 0,0  - `pmss3`: Flujo Pmss P3 (Pmss3).  Potencia mecánica de salida Pmss para el punto 3 del caudal de la turbina para la tabla de consulta que representa la potencia mecánica por unidad en la clasificación MVA de la máquina en función del caudal de la turbina. Por defecto: 0,0  - `pmss4`: Flujo Pmss P4 (Pmss4).  Potencia mecánica de salida Pmss para el punto 4 de flujo de la turbina para la tabla de consulta que representa la potencia mecánica por unidad en la clasificación MVA de la máquina en función del flujo de la turbina. Por defecto: 0,0  - `pmss5`: Flujo Pmss P5 (Pmss5).  Potencia mecánica de salida Pmss para el punto 5 de flujo de la turbina para la tabla de consulta que representa la potencia mecánica por unidad en la clasificación MVA de la máquina en función del flujo de la turbina. Por defecto: 0,0  - `pmss6`: Flujo Pmss P6 (Pmss6).  Potencia mecánica de salida Pmss para el punto 6 del caudal de la turbina para la tabla de consulta que representa la potencia mecánica por unidad en la clasificación MVA de la máquina en función del caudal de la turbina. Por defecto: 0,0  - `pmss7`: Flujo Pmss P7 (Pmss7).  Potencia mecánica de salida Pmss para el punto 7 del caudal de la turbina para la tabla de consulta que representa la potencia mecánica por unidad en la clasificación MVA de la máquina en función del caudal de la turbina. Por defecto: 0,0  - `pmss8`: Flujo Pmss P8 (Pmss8).  Potencia mecánica de salida Pmss para el punto 8 del caudal de la turbina para la tabla de consulta que representa la potencia mecánica por unidad en la clasificación MVA de la máquina en función del caudal de la turbina. Por defecto: 0,0  - `pmss9`: Flujo Pmss P9 (Pmss9).  Potencia mecánica de salida Pmss para el punto 9 del caudal de la turbina para la tabla de consulta que representa la potencia mecánica por unidad en la clasificación MVA de la máquina en función del caudal de la turbina. Por defecto: 0,0  - `rpg`: Estatismo permanente para la retroalimentación de la salida del regulador (R-Perm-Gate). Por defecto: 0,0  - `rpp`: Estatismo permanente para la retroalimentación de la potencia eléctrica (R-Perm-Pe). Por defecto: 0,0  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `td`: Constante de tiempo del controlador de la derivada para limitar la característica de la derivada más allá de una frecuencia de ruptura para evitar la amplificación del ruido de alta frecuencia (Td). Por defecto: 0  - `tdv`: Constante de tiempo de retardo de la válvula distribuidora (Tdv). Por defecto: 0  - `tg`: Valor que permite al controlador de la válvula de distribución avanzar más allá del límite de velocidad de movimiento de la compuerta (Tg). Por defecto: 0  - `tp`: Constante de tiempo de retardo de la válvula piloto (Tp). Por defecto: 0  - `tpe`: Constante de tiempo de estatismo de la potencia eléctrica (Tpe). Por defecto: 0  - `tw`: Constante de tiempo de inercia del agua (Tw) (>0). Por defecto: 0  - `type`: Tipo de NGSI. Tiene que ser GovHydroWEH    
Propiedades requeridas  
Adaptado de los modelos de datos CIM y CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Este modelo de datos es una conversión directa del Modelo de Información Común (CIM) especificado por la norma IEC61970 en modelos de datos inteligentes. Las clases de python en las que se basa este modelo fueron desarrolladas por estas entidades Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) y RWTH University Aachen, Alemania. Algunas propiedades pueden tener un tipo incorrecto. Este es el caso, por favor, plantee una cuestión o envíe un correo a info@smartdatamodels.org.  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GovHydroWEH:    
  description: 'Adapted from CIM data models. Woodward Electric Hydro Governor Model.'    
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
      description: 'Speed Dead Band (db). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    description:    
      description: 'A description of this item'    
      type: Property    
    dicn:    
      description: 'Value to allow the integral controller to advance beyond the gate limits (Dicn). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    dpv:    
      description: 'Value to allow the Pilot valve controller to advance beyond the gate limits (Dpv). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    dturb:    
      description: 'Turbine damping factor (Dturb).  Unit = delta P (PU of MWbase) / delta speed (PU). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    feedbackSignal:    
      description: 'Feedback signal selection (Sw). true = PID Output (if R-Perm-Gate=droop and R-Perm-Pe=0) false = Electrical Power (if R-Perm-Gate=0 and R-Perm-Pe=droop) or false = Gate Position (if R-Perm-Gate=droop and R-Perm-Pe=0). Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fl1:    
      description: 'Flow Gate 1 (Fl1).  Flow value for gate position point 1 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fl2:    
      description: 'Flow Gate 2 (Fl2).  Flow value for gate position point 2 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fl3:    
      description: 'Flow Gate 3 (Fl3).  Flow value for gate position point 3 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fl4:    
      description: 'Flow Gate 4 (Fl4).  Flow value for gate position point 4 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fl5:    
      description: 'Flow Gate 5 (Fl5).  Flow value for gate position point 5 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fp1:    
      description: 'Flow P1 (Fp1).  Turbine Flow value for point 1 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fp10:    
      description: 'Flow P10 (Fp10).  Turbine Flow value for point 10 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fp2:    
      description: 'Flow P2 (Fp2).  Turbine Flow value for point 2 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fp3:    
      description: 'Flow P3 (Fp3).  Turbine Flow value for point 3 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fp4:    
      description: 'Flow P4 (Fp4).  Turbine Flow value for point 4 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fp5:    
      description: 'Flow P5 (Fp5).  Turbine Flow value for point 5 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fp6:    
      description: 'Flow P6 (Fp6).  Turbine Flow value for point 6 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fp7:    
      description: 'Flow P7 (Fp7).  Turbine Flow value for point 7 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fp8:    
      description: 'Flow P8 (Fp8).  Turbine Flow value for point 8 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fp9:    
      description: 'Flow P9 (Fp9).  Turbine Flow value for point 9 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gmax:    
      description: 'Maximum Gate Position (Gmax). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gmin:    
      description: 'Minimum Gate Position (Gmin). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gtmxcl:    
      description: 'Maximum gate closing rate (Gtmxcl). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gtmxop:    
      description: 'Maximum gate opening rate (Gtmxop). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv1:    
      description: 'Gate 1 (Gv1).  Gate Position value for point 1 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv2:    
      description: 'Gate 2 (Gv2).  Gate Position value for point 2 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv3:    
      description: 'Gate 3 (Gv3).  Gate Position value for point 3 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv4:    
      description: 'Gate 4 (Gv4).  Gate Position value for point 4 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv5:    
      description: 'Gate 5 (Gv5).  Gate Position value for point 5 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &govhydroweh_-_properties_-_owner_-_items_-_anyof    
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
    kd:    
      description: 'Derivative controller derivative gain (Kd). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ki:    
      description: 'Derivative controller Integral gain (Ki). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kp:    
      description: 'Derivative control gain (Kp). Default: 0.0'    
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
    mwbase:    
      description: 'Base for power values (MWbase) (>0).  Unit = MW. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *govhydroweh_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    pmss1:    
      description: 'Pmss Flow P1 (Pmss1).  Mechanical Power output Pmss for Turbine Flow point 1 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmss10:    
      description: 'Pmss Flow P10 (Pmss10).  Mechanical Power output Pmss for Turbine Flow point 10 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmss2:    
      description: 'Pmss Flow P2 (Pmss2).  Mechanical Power output Pmss for Turbine Flow point 2 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmss3:    
      description: 'Pmss Flow P3 (Pmss3).  Mechanical Power output Pmss for Turbine Flow point 3 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmss4:    
      description: 'Pmss Flow P4 (Pmss4).  Mechanical Power output Pmss for Turbine Flow point 4 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmss5:    
      description: 'Pmss Flow P5 (Pmss5).  Mechanical Power output Pmss for Turbine Flow point 5 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmss6:    
      description: 'Pmss Flow P6 (Pmss6).  Mechanical Power output Pmss for Turbine Flow point 6 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmss7:    
      description: 'Pmss Flow P7 (Pmss7).  Mechanical Power output Pmss for Turbine Flow point 7 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmss8:    
      description: 'Pmss Flow P8 (Pmss8).  Mechanical Power output Pmss for Turbine Flow point 8 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmss9:    
      description: 'Pmss Flow P9 (Pmss9).  Mechanical Power output Pmss for Turbine Flow point 9 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rpg:    
      description: 'Permanent droop for governor output feedback (R-Perm-Gate). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rpp:    
      description: 'Permanent droop for electrical power feedback (R-Perm-Pe). Default: 0.0'    
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
    td:    
      description: 'Derivative controller time constant to limit the derivative characteristic beyond a breakdown frequency to avoid amplification of high-frequency noise (Td). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tdv:    
      description: 'Distributive Valve time lag time constant (Tdv). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tg:    
      description: 'Value to allow the Distribution valve controller to advance beyond the gate movement rate limit (Tg). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tp:    
      description: 'Pilot Valve time lag time constant (Tp). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tpe:    
      description: 'Electrical power droop time constant (Tpe). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tw:    
      description: 'Water inertia time constant (Tw) (>0). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be GovHydroWEH'    
      enum:    
        - GovHydroWEH    
      type: Property    
  required: []    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
No está disponible el ejemplo de un GovHydroWEH en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un GovHydroWEH en formato JSON-LD normalizado. Es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un GovHydroWEH en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un GovHydroWEH en formato JSON-LD normalizado. Es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud