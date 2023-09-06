<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: GovHydroWEH  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovHydroWEH/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Adaptado de los modelos de datos CIM. Woodward Electric Hydro Governor Model.**  
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
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `db[number]`: Banda muerta de velocidad (db). Predeterminado: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: Descripción de este artículo  - `dicn[number]`: Valor para permitir que el controlador integral avance más allá de los límites de la puerta (Dicn). Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dpv[number]`: Valor para permitir que el controlador de la válvula piloto avance más allá de los límites de la puerta (Dpv). Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dturb[number]`: Factor de amortiguación de la turbina (Dturb).  Unidad = delta P (PU de MWbase) / delta velocidad (PU). Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `feedbackSignal[number]`: Selección de señal de realimentación (Sw). verdadero = Salida PID (si R-Perm-Gate=droop y R-Perm-Pe=0) falso = Alimentación Eléctrica (si R-Perm-Gate=0 y R-Perm-Pe=droop) o falso = Posición de Puerta (si R-Perm-Gate=droop y R-Perm-Pe=0). Por defecto: Falso  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl1[number]`: Flujo compuerta 1 (Fl1).  Valor de caudal para el punto de posición de la compuerta 1 para la tabla de consulta que representa el caudal de agua a través de la turbina en función de la posición de la compuerta para producir un caudal en estado estacionario. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl2[number]`: Flujo compuerta 2 (Fl2).  Valor de caudal para el punto de posición de la compuerta 2 para la tabla de consulta que representa el caudal de agua a través de la turbina en función de la posición de la compuerta para producir un caudal de estado estacionario. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl3[number]`: Flujo compuerta 3 (Fl3).  Valor de caudal para el punto 3 de la posición de la compuerta para la tabla de consulta que representa el caudal de agua a través de la turbina en función de la posición de la compuerta para producir un caudal en estado estacionario. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl4[number]`: Compuerta de caudal 4 (Fl4).  Valor de caudal para el punto de posición de la compuerta 4 para la tabla de consulta que representa el caudal de agua a través de la turbina en función de la posición de la compuerta para producir un caudal en estado estacionario. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl5[number]`: Compuerta de caudal 5 (Fl5).  Valor de caudal para el punto de posición de la compuerta 5 para la tabla de consulta que representa el caudal de agua a través de la turbina en función de la posición de la compuerta para producir un caudal en estado estacionario. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp1[number]`: Caudal P1 (Fp1).  Valor del caudal de la turbina para el punto 1 de la tabla de consulta que representa la potencia mecánica unitaria en el valor nominal de MVA de la máquina en función del caudal de la turbina. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp10[number]`: Caudal P10 (Fp10).  Valor del caudal de la turbina para el punto 10 de la tabla de consulta que representa la potencia mecánica unitaria en el valor nominal de MVA de la máquina en función del caudal de la turbina. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp2[number]`: Caudal P2 (Fp2).  Valor del caudal de la turbina para el punto 2 de la tabla de consulta que representa la potencia mecánica unitaria en el valor nominal de MVA de la máquina en función del caudal de la turbina. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp3[number]`: Caudal P3 (Fp3).  Valor del caudal de la turbina para el punto 3 de la tabla de consulta que representa la potencia mecánica unitaria en el valor nominal de MVA de la máquina en función del caudal de la turbina. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp4[number]`: Caudal P4 (Fp4).  Valor del caudal de la turbina para el punto 4 de la tabla de consulta que representa la potencia mecánica unitaria en el valor nominal de MVA de la máquina en función del caudal de la turbina. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp5[number]`: Caudal P5 (Fp5).  Valor del caudal de la turbina para el punto 5 de la tabla de consulta que representa la potencia mecánica unitaria en el valor nominal de MVA de la máquina en función del caudal de la turbina. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp6[number]`: Caudal P6 (Fp6).  Valor del caudal de la turbina para el punto 6 de la tabla de consulta que representa la potencia mecánica unitaria en el valor nominal de MVA de la máquina en función del caudal de la turbina. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp7[number]`: Caudal P7 (Fp7).  Valor del caudal de la turbina para el punto 7 de la tabla de consulta que representa la potencia mecánica unitaria en el valor nominal de MVA de la máquina en función del caudal de la turbina. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp8[number]`: Caudal P8 (Fp8).  Valor del caudal de la turbina para el punto 8 de la tabla de consulta que representa la potencia mecánica unitaria en el valor nominal de MVA de la máquina en función del caudal de la turbina. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp9[number]`: Caudal P9 (Fp9).  Valor del caudal de la turbina para el punto 9 de la tabla de consulta que representa la potencia mecánica unitaria en el valor nominal de MVA de la máquina en función del caudal de la turbina. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gmax[number]`: Posición máxima de la puerta (Gmax). Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gmin[number]`: Posición mínima de la puerta (Gmin). Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gtmxcl[number]`: Velocidad máxima de cierre de la puerta (Gtmxcl). Predeterminado: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gtmxop[number]`: Velocidad máxima de apertura de la puerta (Gtmxop). Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv1[number]`: Compuerta 1 (Gv1).  Valor de la posición de la compuerta para el punto 1 de la tabla de consulta que representa el caudal de agua a través de la turbina en función de la posición de la compuerta para producir un caudal en estado estacionario. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv2[number]`: Compuerta 2 (Gv2).  Valor de la posición de la compuerta para el punto 2 de la tabla de consulta que representa el caudal de agua a través de la turbina en función de la posición de la compuerta para producir un caudal en estado estacionario. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv3[number]`: Puerta 3 (Gv3).  Valor de la posición de la compuerta para el punto 3 de la tabla de consulta que representa el caudal de agua a través de la turbina en función de la posición de la compuerta para producir un caudal en estado estacionario. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv4[number]`: Puerta 4 (Gv4).  Valor de la posición de la compuerta para el punto 4 de la tabla de consulta que representa el caudal de agua a través de la turbina en función de la posición de la compuerta para producir un caudal en estado estacionario. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv5[number]`: Compuerta 5 (Gv5).  Valor de posición de la compuerta para el punto 5 de la tabla de consulta que representa el caudal de agua a través de la turbina en función de la posición de la compuerta para producir un caudal en estado estacionario. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identificador único de la entidad  - `kd[number]`: Ganancia derivativa del regulador derivativo (Kd). Predeterminado: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ki[number]`: Regulador derivativo Ganancia integral (Ki). Predeterminado: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kp[number]`: Ganancia de control derivativo (Kp). Predeterminado: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `mwbase[number]`: Base para valores de potencia (MWbase) (>0).  Unidad = MW. Por defecto: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: El nombre de este artículo  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `pmss1[number]`: Flujo Pmss P1 (Pmss1).  Potencia mecánica de salida Pmss para el punto 1 de caudal de la turbina para la tabla de consulta que representa la potencia mecánica unitaria en el valor nominal de MVA de la máquina en función del caudal de la turbina. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss10[number]`: Flujo Pmss P10 (Pmss10).  Salida de potencia mecánica Pmss para el punto de caudal 10 de la turbina para la tabla de consulta que representa la potencia mecánica unitaria en el valor nominal de MVA de la máquina en función del caudal de la turbina. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss2[number]`: Flujo Pmss P2 (Pmss2).  Salida de potencia mecánica Pmss para el punto 2 de caudal de la turbina para la tabla de consulta que representa la potencia mecánica unitaria en el valor nominal de MVA de la máquina en función del caudal de la turbina. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss3[number]`: Flujo Pmss P3 (Pmss3).  Potencia mecánica de salida Pmss para el punto 3 del caudal de la turbina para la tabla de consulta que representa la potencia mecánica unitaria en el valor nominal de MVA de la máquina en función del caudal de la turbina. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss4[number]`: Flujo Pmss P4 (Pmss4).  Potencia mecánica de salida Pmss para el punto 4 del caudal de la turbina para la tabla de consulta que representa la potencia mecánica unitaria en el valor nominal de MVA de la máquina en función del caudal de la turbina. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss5[number]`: Flujo Pmss P5 (Pmss5).  Potencia mecánica de salida Pmss para el punto 5 de caudal de la turbina para la tabla de consulta que representa la potencia mecánica unitaria en el valor nominal de MVA de la máquina en función del caudal de la turbina. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss6[number]`: Flujo Pmss P6 (Pmss6).  Salida de potencia mecánica Pmss para el punto 6 de caudal de turbina para la tabla de consulta que representa la potencia mecánica unitaria en la clasificación MVA de la máquina en función del caudal de turbina. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss7[number]`: Flujo Pmss P7 (Pmss7).  Salida de potencia mecánica Pmss para el punto 7 de caudal de la turbina para la tabla de consulta que representa la potencia mecánica unitaria en el valor nominal de MVA de la máquina en función del caudal de la turbina. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss8[number]`: Flujo Pmss P8 (Pmss8).  Salida de potencia mecánica Pmss para el punto 8 de caudal de turbina para la tabla de consulta que representa la potencia mecánica unitaria en la clasificación MVA de la máquina en función del caudal de turbina. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss9[number]`: Flujo Pmss P9 (Pmss9).  Potencia mecánica de salida Pmss para el punto 9 de caudal de la turbina para la tabla de consulta que representa la potencia mecánica unitaria en el valor nominal de MVA de la máquina en función del caudal de la turbina. Por defecto: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rpg[number]`: Estatismo permanente para la realimentación de salida del regulador (R-Perm-Gate). Predeterminado: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rpp[number]`: Estatismo permanente para la realimentación de potencia eléctrica (R-Perm-Pe). Predeterminado: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `td[number]`: Constante de tiempo del controlador derivativo para limitar la característica derivativa más allá de una frecuencia de ruptura para evitar la amplificación del ruido de alta frecuencia (Td). Predeterminado: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tdv[number]`: Constante de tiempo de retardo de la válvula distribuidora (Tdv). Predeterminado: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tg[number]`: Valor para permitir que el controlador de la válvula de distribución avance más allá del límite de velocidad de movimiento de la compuerta (Tg). Predeterminado: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tp[number]`: Constante de tiempo de retardo de la válvula piloto (Tp). Predeterminado: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tpe[number]`: Constante de tiempo de estatismo de la potencia eléctrica (Tpe). Predeterminado: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw[number]`: Constante de tiempo de inercia del agua (Tw) (>0). Predeterminado: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Tipo de NGSI. Tiene que ser GovHydroWEH  <!-- /30-PropertiesList -->  
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
GovHydroWEH:    
  description: Adapted from CIM data models. Woodward Electric Hydro Governor Model.    
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
    db:    
      description: 'Speed Dead Band (db). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    dicn:    
      description: 'Value to allow the integral controller to advance beyond the gate limits (Dicn). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dpv:    
      description: 'Value to allow the Pilot valve controller to advance beyond the gate limits (Dpv). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dturb:    
      description: 'Turbine damping factor (Dturb).  Unit = delta P (PU of MWbase) / delta speed (PU). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    feedbackSignal:    
      description: 'Feedback signal selection (Sw). true = PID Output (if R-Perm-Gate=droop and R-Perm-Pe=0) false = Electrical Power (if R-Perm-Gate=0 and R-Perm-Pe=droop) or false = Gate Position (if R-Perm-Gate=droop and R-Perm-Pe=0). Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fl1:    
      description: 'Flow Gate 1 (Fl1).  Flow value for gate position point 1 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fl2:    
      description: 'Flow Gate 2 (Fl2).  Flow value for gate position point 2 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fl3:    
      description: 'Flow Gate 3 (Fl3).  Flow value for gate position point 3 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fl4:    
      description: 'Flow Gate 4 (Fl4).  Flow value for gate position point 4 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fl5:    
      description: 'Flow Gate 5 (Fl5).  Flow value for gate position point 5 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp1:    
      description: 'Flow P1 (Fp1).  Turbine Flow value for point 1 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp10:    
      description: 'Flow P10 (Fp10).  Turbine Flow value for point 10 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp2:    
      description: 'Flow P2 (Fp2).  Turbine Flow value for point 2 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp3:    
      description: 'Flow P3 (Fp3).  Turbine Flow value for point 3 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp4:    
      description: 'Flow P4 (Fp4).  Turbine Flow value for point 4 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp5:    
      description: 'Flow P5 (Fp5).  Turbine Flow value for point 5 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp6:    
      description: 'Flow P6 (Fp6).  Turbine Flow value for point 6 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp7:    
      description: 'Flow P7 (Fp7).  Turbine Flow value for point 7 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp8:    
      description: 'Flow P8 (Fp8).  Turbine Flow value for point 8 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp9:    
      description: 'Flow P9 (Fp9).  Turbine Flow value for point 9 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gmax:    
      description: 'Maximum Gate Position (Gmax). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gmin:    
      description: 'Minimum Gate Position (Gmin). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gtmxcl:    
      description: 'Maximum gate closing rate (Gtmxcl). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gtmxop:    
      description: 'Maximum gate opening rate (Gtmxop). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv1:    
      description: 'Gate 1 (Gv1).  Gate Position value for point 1 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv2:    
      description: 'Gate 2 (Gv2).  Gate Position value for point 2 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv3:    
      description: 'Gate 3 (Gv3).  Gate Position value for point 3 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv4:    
      description: 'Gate 4 (Gv4).  Gate Position value for point 4 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv5:    
      description: 'Gate 5 (Gv5).  Gate Position value for point 5 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
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
    kd:    
      description: 'Derivative controller derivative gain (Kd). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ki:    
      description: 'Derivative controller Integral gain (Ki). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kp:    
      description: 'Derivative control gain (Kp). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    pmss1:    
      description: 'Pmss Flow P1 (Pmss1).  Mechanical Power output Pmss for Turbine Flow point 1 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss10:    
      description: 'Pmss Flow P10 (Pmss10).  Mechanical Power output Pmss for Turbine Flow point 10 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss2:    
      description: 'Pmss Flow P2 (Pmss2).  Mechanical Power output Pmss for Turbine Flow point 2 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss3:    
      description: 'Pmss Flow P3 (Pmss3).  Mechanical Power output Pmss for Turbine Flow point 3 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss4:    
      description: 'Pmss Flow P4 (Pmss4).  Mechanical Power output Pmss for Turbine Flow point 4 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss5:    
      description: 'Pmss Flow P5 (Pmss5).  Mechanical Power output Pmss for Turbine Flow point 5 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss6:    
      description: 'Pmss Flow P6 (Pmss6).  Mechanical Power output Pmss for Turbine Flow point 6 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss7:    
      description: 'Pmss Flow P7 (Pmss7).  Mechanical Power output Pmss for Turbine Flow point 7 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss8:    
      description: 'Pmss Flow P8 (Pmss8).  Mechanical Power output Pmss for Turbine Flow point 8 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss9:    
      description: 'Pmss Flow P9 (Pmss9).  Mechanical Power output Pmss for Turbine Flow point 9 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rpg:    
      description: 'Permanent droop for governor output feedback (R-Perm-Gate). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rpp:    
      description: 'Permanent droop for electrical power feedback (R-Perm-Pe). Default: 0.0'    
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
    td:    
      description: 'Derivative controller time constant to limit the derivative characteristic beyond a breakdown frequency to avoid amplification of high-frequency noise (Td). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tdv:    
      description: 'Distributive Valve time lag time constant (Tdv). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tg:    
      description: 'Value to allow the Distribution valve controller to advance beyond the gate movement rate limit (Tg). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tp:    
      description: 'Pilot Valve time lag time constant (Tp). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tpe:    
      description: 'Electrical power droop time constant (Tpe). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tw:    
      description: 'Water inertia time constant (Tw) (>0). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: NGSI type. It has to be GovHydroWEH    
      enum:    
        - GovHydroWEH    
      type: string    
      x-ngsi:    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovHydroWEH/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/GovHydroWEH/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
No disponible el ejemplo de un GovHydroWEH en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No disponible el ejemplo de un GovHydroWEH en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No disponible el ejemplo de un GovHydroWEH en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No disponible el ejemplo de un GovHydroWEH en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
