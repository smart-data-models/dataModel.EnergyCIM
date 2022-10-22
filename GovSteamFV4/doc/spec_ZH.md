<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。GovSteamFV4  
==============<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovSteamFV4/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述。**改编自CIM数据模型。蒸汽机组的详细电液调速器。**。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `cpsmn[number]`: 压力调节器输出的最小值（Cpsmn）。  典型值=-1。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `cpsmx[number]`: 压力调节器输出的最大值（Cpsmx）。  典型值=1。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `crmn[number]`: 调节器设定点的最小值（Crmn）。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `crmx[number]`: 调节器设定点的最大值（Crmx）。  典型值=1.2。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `id[*]`: 实体的唯一标识符  - `kdc[number]`: 压力调节器的派生增益（Kdc）。  典型值=1。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kf1[number]`: 频率偏置（下降的倒数）（Kf1）。  典型值=20。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kf3[number]`: 频率控制（下垂的倒数）（Kf3）。  典型值=20。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `khp[number]`: 由HP部分产生的涡轮机总输出量的一部分（KHP）。  典型值=0.35。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kic[number]`: 压力调节器的积分增益（Kic）。  典型值=0.0033。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kip[number]`: 压力反馈调节器的积分增益（Kip）。  典型值=0.5。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kit[number]`: 电液调节器的积分增益（套装）。  典型值=0.04。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kmp1[number]`: 截流阀特性的第一个增益系数（Kmp1）。  典型值=0.5。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kmp2[number]`: 截流阀特性的第二个增益系数（Kmp2）。  典型值=3.5。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kpc[number]`: 压力调节器的比例增益（Kpc）。  典型值=0.5。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kpp[number]`: 压力反馈调节器的比例增益（Kpp）。  典型值=1。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kpt[number]`: 电液调节器的比例增益（Kpt）。  典型值=0.3。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `krc[number]`: 燃料流量的最大变化（Krc）。  典型值=0.05。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ksh[number]`: 锅炉管内流动摩擦造成的压力损失（Ksh）。  典型值=0.08。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `lpi[number]`: 最大负功率误差（Lpi）。  典型值=-0.15。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `lps[number]`: 最大正功率误差（Lps）。  典型值=0.03。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `mnef[number]`: 频率校正的下限（MN）。  典型值=-0.05。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `mxef[number]`: 频率校正的上限（MX）。  典型值=0.05。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `pr1[number]`: 压力设定点静态特性的第一个值（Pr1）。  典型值=0.2。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pr2[number]`: 压力设定点静态特性的第二个值，对应Ps0 = 1.0 PU（Pr2）。  典型值=0.75。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `psmn[number]`: 压力设定点静态特性的最小值（Psmn）。  典型值=1。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rsmimn[number]`: 积分调节器的最小值（Rsmimn）。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rsmimx[number]`: 积分调节器的最大值（Rsmimx）。  典型值=1.1。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rvgmn[number]`: 积分调节器的最小值（Rvgmn）。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rvgmx[number]`: 积分调节器的最大值（Rvgmx）。  典型值=1.2。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 提供实体数据原始来源的一连串字符，作为一个URL。建议为源提供者的完全合格域名，或源对象的URL。  - `srmn[number]`: 最小阀门开度（Srmn）。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `srmx[number]`: 最大阀门开度（Srmx）。  典型值=1.1。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `srsmp[number]`: 截距阀特征不连续点（Srsmp）。  典型值=0.43。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `svmn[number]`: 最大调节器门关闭速度（Svmn）。  典型值=-0.0333。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `svmx[number]`: 最大调节器门打开速度（Svmx）。  典型值=0.0333。默认：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ta[number]`: 控制阀速率开启时间（Ta）。  典型值=0.8。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tam[number]`: 截流阀速率开启时间（Tam）。  典型值=0.8。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tc[number]`: 调节阀速率关闭时间（Tc）。  典型值=0.5。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tcm[number]`: 截流阀速率关闭时间（Tcm）。  典型值=0.5。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tdc[number]`: 压力调节器的衍生时间常数（Tdc）。  典型值=90。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tf1[number]`: 燃料调节的时间常数（Tf1）。  典型值=10。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tf2[number]`: 蒸汽箱的时间常数（Tf2）。  典型值=10。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `thp[number]`: 涡轮机的高压（HP）时间常数（Thp）。  典型值=0.15。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tmp[number]`: 涡轮机的低压（LP）时间常数（Tmp）。  典型值=0.4。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `trh[number]`: 涡轮机的再热器时间常数（Trh）。  典型值=10。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tv[number]`: 锅炉时间常数（Tv）。  典型值=60。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ty[number]`: 控制阀伺服时间常数（Ty）。  典型值=0.1。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI类型。它必须是GovSteamFV4  - `y[number]`: 涡轮机的线性化方程的系数（斯托多拉公式）（Y）。  典型值=0.13。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `yhpmn[number]`: 最小控制阀位置（Yhpmn）。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `yhpmx[number]`: 最大控制阀位置（Yhpmx）。  典型值=1.1。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ympmn[number]`: 最小截流阀位置（Ympmn）。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ympmx[number]`: 最大截流阀位置（Ympmx）。  典型值=1.1。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
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
GovSteamFV4:    
  description: 'Adapted from CIM data models. Detailed electro-hydraulic governor for steam unit.'    
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
    cpsmn:    
      description: 'Minimum value of pressure regulator output (Cpsmn).  Typical Value = -1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    cpsmx:    
      description: 'Maximum value of pressure regulator output (Cpsmx).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    crmn:    
      description: 'Minimum value of regulator set-point (Crmn).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    crmx:    
      description: 'Maximum value of regulator set-point (Crmx).  Typical Value = 1.2. Default: 0.0'    
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
    id:    
      anyOf: &govsteamfv4_-_properties_-_owner_-_items_-_anyof    
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
    kdc:    
      description: 'Derivative gain of pressure regulator (Kdc).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kf1:    
      description: 'Frequency bias (reciprocal of droop) (Kf1).  Typical Value = 20. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kf3:    
      description: 'Frequency control (reciprocal of droop) (Kf3).  Typical Value = 20. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    khp:    
      description: 'Fraction  of total turbine output generated by HP part (Khp).  Typical Value = 0.35. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kic:    
      description: 'Integral gain of pressure regulator (Kic).  Typical Value = 0.0033. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kip:    
      description: 'Integral gain of pressure feedback regulator (Kip).  Typical Value = 0.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kit:    
      description: 'Integral gain of electro-hydraulic regulator (Kit).  Typical Value = 0.04. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kmp1:    
      description: 'First gain coefficient of  intercept valves characteristic (Kmp1).  Typical Value = 0.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kmp2:    
      description: 'Second gain coefficient of intercept valves characteristic (Kmp2).  Typical Value = 3.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kpc:    
      description: 'Proportional gain of pressure regulator (Kpc).  Typical Value = 0.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kpp:    
      description: 'Proportional gain of pressure feedback regulator (Kpp).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kpt:    
      description: 'Proportional gain of electro-hydraulic regulator (Kpt).  Typical Value = 0.3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    krc:    
      description: 'Maximum variation of fuel flow (Krc).  Typical Value = 0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ksh:    
      description: 'Pressure loss due to flow friction in the boiler tubes (Ksh).  Typical Value = 0.08. Default: 0.0'    
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
    lpi:    
      description: 'Maximum negative power error (Lpi).  Typical Value = -0.15. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    lps:    
      description: 'Maximum positive power error (Lps).  Typical Value = 0.03. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    mnef:    
      description: 'Lower limit for frequency correction (MN).  Typical Value = -0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    mxef:    
      description: 'Upper limit for frequency correction (MX).  Typical Value = 0.05. Default: 0.0'    
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
        anyOf: *govsteamfv4_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    pr1:    
      description: 'First value of pressure set point static characteristic (Pr1).  Typical Value = 0.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pr2:    
      description: 'Second value of pressure set point static characteristic, corresponding to Ps0 = 1.0 PU (Pr2).  Typical Value = 0.75. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    psmn:    
      description: 'Minimum value of pressure set point static characteristic (Psmn).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rsmimn:    
      description: 'Minimum value of integral regulator (Rsmimn).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rsmimx:    
      description: 'Maximum value of integral regulator (Rsmimx).  Typical Value = 1.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rvgmn:    
      description: 'Minimum value of integral regulator (Rvgmn).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rvgmx:    
      description: 'Maximum value of integral regulator (Rvgmx).  Typical Value = 1.2. Default: 0.0'    
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
    srmn:    
      description: 'Minimum valve opening (Srmn).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    srmx:    
      description: 'Maximum valve opening (Srmx).  Typical Value = 1.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    srsmp:    
      description: 'Intercept valves characteristic discontinuity point (Srsmp).  Typical Value = 0.43. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    svmn:    
      description: 'Maximum regulator gate closing velocity (Svmn).  Typical Value = -0.0333. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    svmx:    
      description: 'Maximum regulator gate opening velocity (Svmx).  Typical Value = 0.0333. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ta:    
      description: 'Control valves rate opening time (Ta).  Typical Value = 0.8. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tam:    
      description: 'Intercept valves rate opening time (Tam).  Typical Value = 0.8. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tc:    
      description: 'Control valves rate closing time (Tc).  Typical Value = 0.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tcm:    
      description: 'Intercept valves rate closing time (Tcm).  Typical Value = 0.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tdc:    
      description: 'Derivative time constant of pressure regulator (Tdc).  Typical Value = 90. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tf1:    
      description: 'Time constant of fuel regulation (Tf1).  Typical Value = 10. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tf2:    
      description: 'Time constant of steam chest (Tf2).  Typical Value = 10. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    thp:    
      description: 'High pressure (HP) time constant of the turbine (Thp).  Typical Value = 0.15. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tmp:    
      description: 'Low pressure (LP) time constant of the turbine (Tmp).  Typical Value = 0.4. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    trh:    
      description: 'Reheater  time constant of the turbine (Trh).  Typical Value = 10. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tv:    
      description: 'Boiler time constant (Tv).  Typical Value = 60. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ty:    
      description: 'Control valves servo time constant (Ty).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be GovSteamFV4'    
      enum:    
        - GovSteamFV4    
      type: string    
      x-ngsi:    
        type: Property    
    y:    
      description: 'Coefficient of linearized equations of turbine (Stodola formulation) (Y).  Typical Value = 0.13. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    yhpmn:    
      description: 'Minimum control valve position (Yhpmn).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    yhpmx:    
      description: 'Maximum control valve position (Yhpmx).  Typical Value = 1.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ympmn:    
      description: 'Minimum intercept valve position (Ympmn).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ympmx:    
      description: 'Maximum intercept valve position (Ympmx).  Typical Value = 1.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovSteamFV4/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/GovSteamFV4/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
不提供JSON-LD格式的GovSteamFV4的例子，作为关键值。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
不提供规范化的JSON-LD格式的GovSteamFV4的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
不提供JSON-LD格式的GovSteamFV4的例子，作为关键值。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
不提供规范化的JSON-LD格式的GovSteamFV4的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
