<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。GovSteamEU  
=============<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovSteamEU/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述。**改编自CIM数据模型。带有PID调节器的锅炉和汽轮机的简化模型。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `chc[number]`: 控制阀速率关闭限制（Chc）。  单位=PU/秒。  典型值=-3.3。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `cho[number]`: 控制阀速率开度限制（Cho）。  单位=PU/秒。  典型值=0.17。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `cic[number]`: 截流阀速率关闭极限（Cic）。  典型值=-2.2。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `cio[number]`: 截流阀率开限（Cio）。  典型值=0.123。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `db1[number]`: 频率校正器的死区（db1）。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `db2[number]`: 调速器的死区（db2）。  典型值=0.0004。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: 对这个项目的描述  - `hhpmax[number]`: 最大控制阀位置（Hhpmax）。  典型值=1。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: 实体的唯一标识符  - `ke[number]`: 功率控制器的增益（Ke）。  典型值=0.65。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kfcor[number]`: 频率校正器的增益（Kfcor）。  典型值=20。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `khp[number]`: 由HP部分产生的涡轮机总输出量的一部分（KHP）。  典型值=0.277。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `klp[number]`: HP部分产生的涡轮机总输出量的一部分（Klp）。  典型值=0.723。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kwcor[number]`: 调速器的增益（Kwcor）。  典型值=20。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `mwbase[number]`: 功率值的基础（MWbase）（>0）。  单位=MW。默认：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `pmax[number]`: 涡轮机的最大有功功率（Pmax）。  典型值=1。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `prhmax[number]`: 最大低压限制（Prhmax）。  典型值=1.4。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `simx[number]`: 截流阀传输极限（Simx）。  典型值=0.425。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `tb[number]`: 锅炉时间常数（Tb）。  典型值=100。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tdp[number]`: 功率控制器的衍生时间常数（Tdp）。  典型值=0。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ten[number]`: 电子液压传感器（十）。  典型值=0.1。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tf[number]`: 频率传感器时间常数（Tf）。  典型值=0。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tfp[number]`: 功率控制器的时间常数（Tfp）。  典型值=0。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `thp[number]`: 涡轮机的高压（HP）时间常数（Thp）。  典型值=0.31。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tip[number]`: 功率控制器的积分时间常数（提示）。  典型值=2。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tlp[number]`: 涡轮机的低压（LP）时间常数（Tlp）。  典型值=0.45。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tp[number]`: 功率传感器时间常数（Tp）。  典型值=0.07。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `trh[number]`: 涡轮机的再热器时间常数（Trh）。  典型值=8。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tvhp[number]`: 控制阀伺服时间常数（Tvhp）。  典型值=0.1。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tvip[number]`: 截流阀伺服时间常数（Tvip）。  典型值=0.15。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw[number]`: 速度传感器时间常数（Tw）。  典型值=0.02。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI类型。它必须是GovSteamEU  - `wfmax[number]`: 频率校正的上限（Wfmax）。  典型值=0.05。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `wfmin[number]`: 频率校正的下限（Wfmin）。  典型值=-0.05。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `wmax1[number]`: 紧急速度控制下限（wmax1）。  典型值=1.025。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `wmax2[number]`: 紧急速度控制上限（wmax2）。  典型值=1.05。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `wwmax[number]`: 调速器的上限（Wwmax）。  典型值=0.1。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `wwmin[number]`: 调速器频率修正的下限（Wwmin）。  典型值=-1。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
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
GovSteamEU:    
  description: 'Adapted from CIM data models. Simplified model  of boiler and steam turbine with PID governor.'    
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
    chc:    
      description: 'Control valves rate closing limit (Chc).  Unit = PU/sec.  Typical Value = -3.3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    cho:    
      description: 'Control valves rate opening limit (Cho).  Unit = PU/sec.  Typical Value = 0.17. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    cic:    
      description: 'Intercept valves rate closing limit (Cic).  Typical Value = -2.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    cio:    
      description: 'Intercept valves rate opening limit (Cio).  Typical Value = 0.123. Default: 0.0'    
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
    db1:    
      description: 'Dead band of the frequency corrector (db1).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    db2:    
      description: 'Dead band of the speed governor (db2).  Typical Value = 0.0004. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    hhpmax:    
      description: 'Maximum control valve position (Hhpmax).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &govsteameu_-_properties_-_owner_-_items_-_anyof    
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
    ke:    
      description: 'Gain of the power controller (Ke).  Typical Value = 0.65. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kfcor:    
      description: 'Gain of the frequency corrector (Kfcor).  Typical Value = 20. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    khp:    
      description: 'Fraction of total turbine output generated by HP part (Khp).  Typical Value = 0.277. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    klp:    
      description: 'Fraction of total turbine output generated by HP part (Klp).  Typical Value = 0.723. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kwcor:    
      description: 'Gain of the speed governor (Kwcor).  Typical Value = 20. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
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
      x-ngsi:    
        type: GeoProperty    
    mwbase:    
      description: 'Base for power values (MWbase) (>0).  Unit = MW. Default: 0.0'    
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
        anyOf: *govsteameu_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    pmax:    
      description: 'Maximal active power of the turbine (Pmax).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    prhmax:    
      description: 'Maximum low pressure limit (Prhmax).  Typical Value = 1.4. Default: 0.0'    
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
    simx:    
      description: 'Intercept valves transfer limit (Simx).  Typical Value = 0.425. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    tb:    
      description: 'Boiler time constant (Tb).  Typical Value = 100. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tdp:    
      description: 'Derivative time constant of the power controller (Tdp).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ten:    
      description: 'Electro hydraulic transducer (Ten).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tf:    
      description: 'Frequency transducer time constant (Tf).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tfp:    
      description: 'Time constant of the power controller (Tfp).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    thp:    
      description: 'High pressure (HP) time constant of the turbine (Thp).  Typical Value = 0.31. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tip:    
      description: 'Integral time constant of the power controller (Tip).  Typical Value = 2. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tlp:    
      description: 'Low pressure(LP) time constant of the turbine (Tlp).  Typical Value = 0.45. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tp:    
      description: 'Power transducer time constant (Tp).  Typical Value = 0.07. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    trh:    
      description: 'Reheater  time constant of the turbine (Trh).  Typical Value = 8. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tvhp:    
      description: 'Control valves servo time constant (Tvhp).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tvip:    
      description: 'Intercept valves servo time constant (Tvip).  Typical Value = 0.15. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tw:    
      description: 'Speed transducer time constant (Tw).  Typical Value = 0.02. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be GovSteamEU'    
      enum:    
        - GovSteamEU    
      type: string    
      x-ngsi:    
        type: Property    
    wfmax:    
      description: 'Upper limit for frequency correction (Wfmax).  Typical Value = 0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    wfmin:    
      description: 'Lower limit for frequency correction (Wfmin).  Typical Value = -0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    wmax1:    
      description: 'Emergency speed control lower limit (wmax1).  Typical Value = 1.025. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    wmax2:    
      description: 'Emergency speed control upper limit (wmax2).  Typical Value = 1.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    wwmax:    
      description: 'Upper limit for the speed governor (Wwmax).  Typical Value = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    wwmin:    
      description: 'Lower limit for the speed governor frequency correction (Wwmin).  Typical Value = -1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovSteamEU/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/GovSteamEU/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
不可用JSON-LD格式的GovSteamEU的例子作为key-values。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
不提供规范化的JSON-LD格式的GovSteamEU的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
不可用JSON-LD格式的GovSteamEU的例子作为key-values。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
不提供规范化的JSON-LD格式的GovSteamEU的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
