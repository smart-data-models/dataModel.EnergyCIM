<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。风力类型3IEC  
===========<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/WindContPType3IEC/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述。**改编自CIM数据模型。P控制模型类型3。  参考。IEC标准61400-27-1第6.6.5.3节**。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `WindDynamicsLookupTable[number]`: 与该风动力学查询表有关的P控制类型3模型。默认：'列表  . Model: [https://schema.org/Number](https://schema.org/Number)- `WindGenTurbineType3IEC[number]`: 与该风控P3型模型相关的风轮机3型模型。默认值。无  . Model: [https://schema.org/Number](https://schema.org/Number)- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `dpmax[number]`: 最大风力涡轮机功率斜率（）。它是与项目有关的参数。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dtrisemaxlvrt[number]`: 在LVRT期间对S（d）的扭矩上升率的限制。这是一个取决于项目的参数。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: 实体的唯一标识符  - `kdtd[number]`: 主动传动系统阻尼的增益（）。它是与类型有关的参数。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kip[number]`: PI控制器集成参数（）。它是与类型有关的参数。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kpp[number]`: PI控制器的比例增益（）。它是与类型有关的参数。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `mplvrt[number]`: 启用LVRT功率控制模式（M true = 1：电压控制 false = 0：无功功率控制。  这是一个取决于项目的参数。默认值。假的  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: 这个项目的名称。  - `omegaoffset[number]`: 参考值的偏移，在转子速度变化时限制控制器的动作（欧米茄）。这是一个取决于具体情况的参数。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `pdtdmax[number]`: 最大的主动传动系统阻尼功率（）。它是与类型有关的参数。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rramp[number]`: 扭矩的斜率限制，在一些电网规范中要求（）。这是一个取决于项目的参数。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `tdvs[number]`: 深度电压骤降后的时间延迟（T）。这是一个与项目有关的参数。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `temin[number]`: 最小发电机扭矩（）。它是与类型有关的参数。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tomegafilt[number]`: 用于发电机转速测量的滤波时间常数（）。它是与类型有关的参数。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tpfilt[number]`: 功率测量的过滤时间常数（）。它是与类型有关的参数。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tpord[number]`: 幂级滞后的时间常数（）。它是与类型有关的参数。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tufilt[number]`: 电压测量的滤波时间常数（）。它是与类型有关的参数。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tuscale[number]`: 复位扭矩（T）的电压比例系数。它是一个与项目有关的参数。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `twref[number]`: 速度参考滤波器的时间常数（）。它是一个与类型有关的参数。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI类型。它必须是WindContPType3IEC  - `udvs[number]`: 深度电压骤降后保持LVRT状态的电压限制（）。这是一个与项目有关的参数。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `updip[number]`: P控制的电压跌落阈值（）。  汽轮机控制的一部分，通常与变流器的阈值不同（如0.8）。它是与项目有关的参数。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `wdtd[number]`: 主动传动系统阻尼频率（omega）。它可以从两个质量模型参数计算出来。它是与类型有关的参数。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `zeta[number]`: 主动传动系统阻尼的系数（Zeta）。它是与类型有关的参数。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
<!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
改编自CIM数据模型和CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy)。这个数据模型是将IEC61970标准规定的通用信息模型（CIM）直接转换为智能数据模型。这个模型所基于的python类是由这些实体复杂电力系统自动化研究所（ACS）、EON能源研究中心（EONERC）和德国亚琛工大开发的。一些属性可能有错误的类型。这种情况下，请提出一个问题或发送邮件到 info@smartdatamodels.org。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WindContPType3IEC:    
  description: 'Adapted from CIM data models. P control model Type 3.  Reference: IEC Standard 61400-27-1 Section 6.6.5.3.'    
  properties:    
    WindDynamicsLookupTable:    
      description: 'The P control type 3 model with which this wind dynamics lookup table is associated. Default: ''list'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    WindGenTurbineType3IEC:    
      description: 'Wind turbine type 3 model with which this Wind control P type 3 model is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
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
    dpmax:    
      description: 'Maximum wind turbine power ramp rate (). It is project dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dtrisemaxlvrt:    
      description: 'Limitation of torque rise rate during LVRT for S (d). It is project dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &windcontptype3iec_-_properties_-_owner_-_items_-_anyof    
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
    kdtd:    
      description: 'Gain for active drive train damping (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kip:    
      description: 'PI controller integration parameter (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kpp:    
      description: 'PI controller proportional gain (). It is type dependent parameter. Default: 0.0'    
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
    mplvrt:    
      description: 'Enable LVRT power control mode (M true = 1: voltage control false = 0: reactive power control.  It is project dependent parameter. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    omegaoffset:    
      description: 'Offset to reference value that limits controller action during rotor speed changes (omega). It is case dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *windcontptype3iec_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    pdtdmax:    
      description: 'Maximum active drive train damping power (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rramp:    
      description: 'Ramp limitation of torque, required in some grid codes (). It is project dependent parameter. Default: 0.0'    
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
    tdvs:    
      description: 'Timedelay after deep voltage sags (T). It is project dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    temin:    
      description: 'Minimum electrical generator torque (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tomegafilt:    
      description: 'Filter time constant for generator speed measurement (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tpfilt:    
      description: 'Filter time constant for power measurement (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tpord:    
      description: 'Time constant in power order lag (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tufilt:    
      description: 'Filter time constant for voltage measurement (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tuscale:    
      description: 'Voltage scaling factor of reset-torque (T). It is project dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    twref:    
      description: 'Time constant in speed reference filter (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be WindContPType3IEC'    
      enum:    
        - WindContPType3IEC    
      type: string    
      x-ngsi:    
        type: Property    
    udvs:    
      description: 'Voltage limit for hold LVRT status after deep voltage sags (). It is project dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    updip:    
      description: 'Voltage dip threshold for P-control ().  Part of turbine control, often different (e.g 0.8) from converter thresholds. It is project dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    wdtd:    
      description: 'Active drive train damping frequency (omega). It can be calculated from two mass model parameters. It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    zeta:    
      description: 'Coefficient for active drive train damping (zeta). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindContPType3IEC/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/WindContPType3IEC/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
不提供JSON-LD格式的WindContPType3IEC的例子作为关键值。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
不提供JSON-LD格式的规范化WindContPType3IEC的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
不提供JSON-LD格式的WindContPType3IEC的例子，作为关键值。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
不提供JSON-LD格式的规范化WindContPType3IEC的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
