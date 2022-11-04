<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。GovHydro3  
============<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovHydro3/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述。**改编自CIM数据模型。修改后的IEEE水力调速器-涡轮机模型。  该模型与IEEE建模指导文件中定义的模型不同，对闸门位置和速度的限制不允许对上游信号进行缠绕。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `at[number]`: 涡轮机增益（At）。  典型值=1.2。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `db1[number]`: 有意的死带宽度（db1）。  单位=Hz。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `db2[number]`: 非故意死区（db2）。  单位=MW。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: 对这个项目的描述  - `dturb[number]`: 涡轮机阻尼系数（Dturb）。  典型值=0.2。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `eps[number]`: 有意的db滞后（eps）。  单位=Hz。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `governorControl[number]`: 调速器控制标志（Cflag）。true = PID控制有效 false = 双导数控制有效。典型值=true。默认值。假的  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv1[number]`: 非线性增益点1，PU gv（Gv1）。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv2[number]`: 非线性增益点2，PU gv（Gv2）。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv3[number]`: 非线性增益点3，PU gv（Gv3）。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv4[number]`: 非线性增益点4，PU gv（Gv4）。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv5[number]`: 非线性增益点5，PU gv（Gv5）。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv6[number]`: 非线性增益点6，PU gv（Gv6）。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `h0[number]`: 涡轮机额定水头（H0）。  典型值=1。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: 实体的唯一标识符  - `k1[number]`: 衍生增益（K1）。  典型值=0.01。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `k2[number]`: 双重导数增益，如果Cflag=-1（K2）。  典型值=2.5。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kg[number]`: 门控伺服增益（Kg）。  典型值=2。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ki[number]`: 积分增益（Ki）。  典型值=0.5。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `mwbase[number]`: 功率值的基础（MWbase）（>0）。  单位=MW。默认：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `pgv1[number]`: 非线性增益点1，PU功率（Pgv1）。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pgv2[number]`: 非线性增益点2，PU功率（Pgv2）。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pgv3[number]`: 非线性增益点3，PU功率（Pgv3）。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pgv4[number]`: 非线性增益点4，PU功率（Pgv4）。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pgv5[number]`: 非线性增益点5，PU功率（Pgv5）。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pgv6[number]`: 非线性增益点6，PU功率（Pgv6）。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmax[number]`: 最大闸门开度，MWbase的PU（Pmax）。  典型值=1。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmin[number]`: 最小闸门开度，MWbase的PU（Pmin）。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `qnl[number]`: 标称水头下的空载水轮机流量（Qnl）。  典型值=0.08。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `relec[number]`: 稳态下降，PU，用于电功率反馈（Relec）。  典型值=0.05。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rgate[number]`: 稳态下降，PU，用于调速器输出反馈（Rgate）。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 提供实体数据原始来源的一连串字符，作为一个URL。建议为源提供者的完全合格域名，或源对象的URL。  - `td[number]`: 输入滤波器时间常数（Td）。  典型值=0.05。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tf[number]`: 冲洗时间常数（Tf）。  典型值=0.1。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tp[number]`: 门控伺服时间常数（Tp）。  典型值=0.05。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tt[number]`: 功率反馈时间常数（Tt）。  典型值=0.2。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw[number]`: 水的惯性时间常数（Tw）。  典型值=1。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI类型。它必须是GovHydro3  - `velcl[number]`: 最大闸门关闭速度（Velcl）。  单位=PU/秒。  典型值=-0.2。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `velop[number]`: 最大闸门开启速度（Velop）。  单位=PU/秒。典型值=0.2。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
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
GovHydro3:    
  description: 'Adapted from CIM data models. Modified IEEE Hydro Governor-Turbine Model.  This model differs from that defined in the IEEE modeling guideline paper in that the limits on gate position and velocity do not permit wind up of the upstream signals.'    
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
    at:    
      description: 'Turbine gain (At).  Typical Value = 1.2. Default: 0.0'    
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
      description: 'Intentional dead-band width (db1).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    db2:    
      description: 'Unintentional dead-band (db2).  Unit = MW.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    dturb:    
      description: 'Turbine damping factor (Dturb).  Typical Value = 0.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    eps:    
      description: 'Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    governorControl:    
      description: 'Governor control flag (Cflag). true = PID control is active false = double derivative control is active. Typical Value = true. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv1:    
      description: 'Nonlinear gain point 1, PU gv (Gv1).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv2:    
      description: 'Nonlinear gain point 2, PU gv (Gv2).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv3:    
      description: 'Nonlinear gain point 3, PU gv (Gv3).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv4:    
      description: 'Nonlinear gain point 4, PU gv (Gv4).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv5:    
      description: 'Nonlinear gain point 5, PU gv (Gv5).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv6:    
      description: 'Nonlinear gain point 6, PU gv (Gv6).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    h0:    
      description: 'Turbine nominal head (H0).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &govhydro3_-_properties_-_owner_-_items_-_anyof    
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
    k1:    
      description: 'Derivative gain (K1).  Typical Value = 0.01. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    k2:    
      description: 'Double derivative gain, if Cflag = -1 (K2).  Typical Value = 2.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kg:    
      description: 'Gate servo gain (Kg).  Typical Value = 2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ki:    
      description: 'Integral gain (Ki).  Typical Value = 0.5. Default: 0.0'    
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
        anyOf: *govhydro3_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    pgv1:    
      description: 'Nonlinear gain point 1, PU power (Pgv1).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pgv2:    
      description: 'Nonlinear gain point 2, PU power (Pgv2).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pgv3:    
      description: 'Nonlinear gain point 3, PU power (Pgv3).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pgv4:    
      description: 'Nonlinear gain point 4, PU power (Pgv4).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pgv5:    
      description: 'Nonlinear gain point 5, PU power (Pgv5).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pgv6:    
      description: 'Nonlinear gain point 6, PU power (Pgv6).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmax:    
      description: 'Maximum gate opening, PU of MWbase (Pmax).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmin:    
      description: 'Minimum gate opening, PU of MWbase (Pmin).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    qnl:    
      description: 'No-load turbine flow at nominal head (Qnl).  Typical Value = 0.08. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    relec:    
      description: 'Steady-state droop, PU, for electrical power feedback (Relec).  Typical Value = 0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rgate:    
      description: 'Steady-state droop, PU, for governor output feedback (Rgate).  Typical Value = 0. Default: 0.0'    
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
    td:    
      description: 'Input filter time constant (Td).  Typical Value = 0.05. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tf:    
      description: 'Washout time constant (Tf).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tp:    
      description: 'Gate servo time constant (Tp).  Typical Value = 0.05. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tt:    
      description: 'Power feedback time constant (Tt).  Typical Value = 0.2. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tw:    
      description: 'Water inertia time constant (Tw).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be GovHydro3'    
      enum:    
        - GovHydro3    
      type: string    
      x-ngsi:    
        type: Property    
    velcl:    
      description: 'Maximum gate closing velocity (Velcl).  Unit = PU/sec.  Typical Value = -0.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    velop:    
      description: 'Maximum gate opening velocity (Velop).  Unit = PU/sec. Typical Value = 0.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovHydro3/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/GovHydro3/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
不提供JSON-LD格式的GovHydro3的例子作为关键值。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
不提供规范化的JSON-LD格式的GovHydro3的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
不提供JSON-LD格式的GovHydro3的例子，作为key-values。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
不提供规范化的JSON-LD格式的GovHydro3的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
