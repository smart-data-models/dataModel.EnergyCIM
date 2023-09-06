<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：WindContQIEC  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/WindContQIEC/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：** 改编自 CIM 数据模型。Q 控制模型。  参考：IEC 标准 61400-27-1 第 6.6.5.6.** 节  
版本： 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。  
- `WindTurbineType3or4IEC[number]`: 与此无功控制模式相关联的 3 或 4 型风力发电机型号。默认值：无  . Model: [https://schema.org/Number](https://schema.org/Number)- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理    
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `id[*]`: 实体的唯一标识符  - `iqh1[number]`: 浸没期间注入的最大无功电流 (i)。该参数取决于类型。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `iqmax[number]`: 最大无功电流注入 (i)。该参数取决于类型。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `iqmin[number]`: 最小无功电流注入 (i)。该参数取决于类型。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `iqpost[number]`: 故障后无功电流注入（）。该参数取决于项目。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kiq[number]`: 无功功率 PI 控制器积分增益（）。该参数取决于类型。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kiu[number]`: 电压 PI 控制器积分增益（）。该参数取决于类型。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kpq[number]`: 无功功率 PI 控制器比例增益（）。该参数取决于类型。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kpu[number]`: 电压 PI 控制器比例增益（）。该参数取决于类型。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kqv[number]`: LVRT 电流的电压比例系数（）。该参数取决于项目。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `qmax[number]`: 最大无功功率 (q)。该参数取决于类型。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `qmin[number]`: 最小无功功率 (q)。该参数取决于类型。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rdroop[number]`: 压降阻抗的电阻分量（）。该参数取决于项目。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `tiq[number]`: 无功电流滞后时间常数 (T)。该参数取决于类型。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tpfilt[number]`: 功率测量滤波器时间常数（）。该参数取决于类型。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tpost[number]`: 故障后注入无功功率的时间长度（）。该参数取决于项目。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tqord[number]`: 无功功率阶次滞后时间常数（）。该参数取决于类型。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tufilt[number]`: 电压测量滤波器时间常数（）。该参数取决于类型。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI 类型。必须是 WindContQIEC  - `udb1[number]`: 电压死区下限（）。该参数取决于类型。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `udb2[number]`: 电压死区上限（）。该参数取决于类型。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `umax[number]`: 电压 PI 控制器积分项 (u) 中的最大电压。该参数取决于类型。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `umin[number]`: 电压 PI 控制器积分项 (u) 中的最小电压。该参数取决于类型。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `uqdip[number]`: 在 q 控制（）中用于检测 LVRT 的电压阈值。该参数取决于类型。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `uref0[number]`: 用户自定义的电压基准偏置（），在 = 时使用。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `windLVRTQcontrolModesType[number]`: LVRT Q 控制模式的类型（）。该参数取决于项目。默认值：无  . Model: [https://schema.org/Number](https://schema.org/Number)- `windQcontrolModesType[number]`: 一般风力发电机 Q 控制模式的类型（）。  这是一个取决于项目的参数。默认值：无  . Model: [https://schema.org/Number](https://schema.org/Number)- `xdroop[number]`: 压降阻抗的电感分量（）。该参数取决于项目。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
<!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
改编自 CIM 数据模型和 CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy)。该数据模型将 IEC61970 标准规定的通用信息模型（CIM）直接转换为智能数据模型。该模型所基于的 python 类由德国复杂电力系统自动化研究所 (ACS)、EON 能源研究中心 (EONERC) 和亚琛工业大学 (RWTH University Aachen) 开发。某些属性的类型可能有误。如果出现这种情况，请提出问题或发送邮件至 info@smartdatamodels.org。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排列（点击查看详情）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WindContQIEC:    
  description: 'Adapted from CIM data models. Q control model.  Reference: IEC Standard 61400-27-1 Section 6.6.5.6.'    
  properties:    
    WindTurbineType3or4IEC:    
      description: 'Wind turbine type 3 or 4 model with which this reactive control mode is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
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
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
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
    iqh1:    
      description: 'Maximum reactive current injection during dip (i). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    iqmax:    
      description: 'Maximum reactive current injection (i). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    iqmin:    
      description: 'Minimum reactive current injection (i). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    iqpost:    
      description: 'Post fault reactive current injection (). It is project dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kiq:    
      description: 'Reactive power PI controller integration gain (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kiu:    
      description: 'Voltage PI controller integration gain (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kpq:    
      description: 'Reactive power PI controller proportional gain (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kpu:    
      description: 'Voltage PI controller proportional gain (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kqv:    
      description: 'Voltage scaling factor for LVRT current (). It is project dependent parameter. Default: 0.0'    
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
    qmax:    
      description: 'Maximum reactive power (q). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    qmin:    
      description: 'Minimum reactive power (q). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rdroop:    
      description: 'Resistive component of voltage drop impedance (). It is project dependent parameter. Default: 0.0'    
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
    tiq:    
      description: 'Time constant in reactive current lag (T). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tpfilt:    
      description: 'Power measurement filter time constant (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tpost:    
      description: 'Length of time period where post fault reactive power is injected (). It is project dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tqord:    
      description: 'Time constant in reactive power order lag (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tufilt:    
      description: 'Voltage measurement filter time constant (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: NGSI type. It has to be WindContQIEC    
      enum:    
        - WindContQIEC    
      type: string    
      x-ngsi:    
        type: Property    
    udb1:    
      description: 'Voltage dead band lower limit (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    udb2:    
      description: 'Voltage dead band upper limit (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    umax:    
      description: 'Maximum voltage in voltage PI controller integral term (u). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    umin:    
      description: 'Minimum voltage in voltage PI controller integral term (u). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    uqdip:    
      description: 'Voltage threshold for LVRT detection in q control (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    uref0:    
      description: 'User defined bias in voltage reference (), used when  =. It is case dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    windLVRTQcontrolModesType:    
      description: 'Types of LVRT Q control modes (). It is project dependent parameter. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    windQcontrolModesType:    
      description: 'Types of general wind turbine Q control modes ().  It is project dependent parameter. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    xdroop:    
      description: 'Inductive component of voltage drop impedance (). It is project dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindContQIEC/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/WindContQIEC/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
不可用 JSON-LD 格式的 WindContQIEC 示例作为键值。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
没有正常化的 JSON-LD 格式 WindContQIEC 示例。在不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
不可用 JSON-LD 格式的 WindContQIEC 示例作为键值。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
没有正常化的 JSON-LD 格式 WindContQIEC 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
