<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。PssPTIST3  
============<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/PssPTIST3/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述。**改编自CIM数据模型。PTI基于微处理器的稳定器3.**型  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `a0[number]`: 滤波系数（A0）。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `a1[number]`: 限制器（Al）。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `a2[number]`: 滤波系数（A2）。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `a3[number]`: 滤波系数（A3）。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `a4[number]`: 滤波系数（A4）。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `a5[number]`: 滤波系数（A5）。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `al[number]`: 限制器（Al）。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `athres[number]`: 阈值，超过此值将绕过输出平均化（Athres）。  典型值=0.005。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `b0[number]`: 滤波系数（B0）。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `b1[number]`: 滤波系数（B1）。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `b2[number]`: 滤波系数（B2）。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `b3[number]`: 滤波系数（B3）。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `b4[number]`: 滤波系数（B4）。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `b5[number]`: 滤波系数（B5）。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `dl[number]`: 限制器（Dl）。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dtc[number]`: 与激活控制有关的时间步长（50赫兹为0.03）（Dtc）。  典型值=0.025。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dtf[number]`: 时间步长频率计算（50赫兹为0.03）（Dtf）。  典型值=0.025。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dtp[number]`: 时间步长的有功功率计算（50赫兹为0.015）（Dtp）。  典型值=0.0125。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: 实体的唯一标识符  - `isw[number]`: 数字/模拟输出开关（Isw）。true = 产生模拟输出 false = 转换为数字输出，使用分接选择表。默认值。False（假）。  . Model: [https://schema.org/Number](https://schema.org/Number)- `k[number]`: 增益（K）。  典型值=9。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `lthres[number]`: 阈值（Lthres）。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `m[number]`: (M).  M=2*H。  典型值=5。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: 这个项目的名称。  - `nav[number]`: 平均控制输出的数量（Nav）（1 <= Nav <= 16）。  典型值=4。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ncl[number]`: 激活极限功能时的计数（Ncl）（>0）。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ncr[number]`: 触发极限功能后直到复位的计数数（Ncr）。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `pmin[number]`: (Pmin)。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `t1[number]`: 时间常数（T1）。  典型值=0.3。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t2[number]`: 时间常数（T2）。  典型值=1。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t3[number]`: 时间常数（T3）。  典型值=0.2。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t4[number]`: 时间常数（T4）。  典型值=0.05。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t5[number]`: 时间常数（T5）。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t6[number]`: 时间常数（T6）。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tf[number]`: 时间常数（Tf）。  典型值=0.2。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tp[number]`: 时间常数（Tp）。  典型值=0.2。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI类型。它必须是PssPTIST3  <!-- /30-PropertiesList -->  
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
PssPTIST3:    
  description: 'Adapted from CIM data models. PTI Microprocessor-Based Stabilizer type 3.'    
  properties:    
    a0:    
      description: 'Filter coefficient (A0). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    a1:    
      description: 'Limiter (Al). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    a2:    
      description: 'Filter coefficient (A2). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    a3:    
      description: 'Filter coefficient (A3). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    a4:    
      description: 'Filter coefficient (A4). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    a5:    
      description: 'Filter coefficient (A5). Default: 0.0'    
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
    al:    
      description: 'Limiter (Al). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    athres:    
      description: 'Threshold value above which output averaging will be bypassed (Athres).  Typical Value = 0.005. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    b0:    
      description: 'Filter coefficient (B0). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    b1:    
      description: 'Filter coefficient (B1). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    b2:    
      description: 'Filter coefficient (B2). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    b3:    
      description: 'Filter coefficient (B3). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    b4:    
      description: 'Filter coefficient (B4). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    b5:    
      description: 'Filter coefficient (B5). Default: 0.0'    
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
    dl:    
      description: 'Limiter (Dl). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dtc:    
      description: 'Time step related to activation of controls (0.03 for 50 Hz) (Dtc).  Typical Value = 0.025. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dtf:    
      description: 'Time step frequency calculation (0.03 for 50 Hz) (Dtf).  Typical Value = 0.025. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dtp:    
      description: 'Time step active power calculation (0.015 for 50 Hz) (Dtp).  Typical Value = 0.0125. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &pssptist3_-_properties_-_owner_-_items_-_anyof    
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
    isw:    
      description: 'Digital/analog output switch (Isw). true = produce analog output false = convert to digital output, using tap selection table. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    k:    
      description: 'Gain (K).  Typical Value = 9. Default: 0.0'    
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
    lthres:    
      description: 'Threshold value (Lthres). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    m:    
      description: '(M).  M=2*H.  Typical Value = 5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    nav:    
      description: 'Number of control outputs to average (Nav) (1 <= Nav <= 16).  Typical Value = 4. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ncl:    
      description: 'Number of counts at limit to active limit function (Ncl) (>0). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ncr:    
      description: 'Number of counts until reset after limit function is triggered (Ncr). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *pssptist3_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    pmin:    
      description: '(Pmin). Default: 0.0'    
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
    t1:    
      description: 'Time constant (T1).  Typical Value = 0.3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t2:    
      description: 'Time constant (T2).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t3:    
      description: 'Time constant (T3).  Typical Value = 0.2. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t4:    
      description: 'Time constant (T4).  Typical Value = 0.05. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t5:    
      description: 'Time constant (T5). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t6:    
      description: 'Time constant (T6). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tf:    
      description: 'Time constant (Tf).  Typical Value = 0.2. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tp:    
      description: 'Time constant (Tp).  Typical Value = 0.2. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be PssPTIST3'    
      enum:    
        - PssPTIST3    
      type: string    
      x-ngsi:    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PssPTIST3/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/PssPTIST3/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
不提供JSON-LD格式的PssPTIST3的例子，作为key-values。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
不提供规范化的JSON-LD格式的PssPTIST3的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
不提供JSON-LD格式的PssPTIST3的例子，作为key-values。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
不提供规范化的JSON-LD格式的PssPTIST3的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
