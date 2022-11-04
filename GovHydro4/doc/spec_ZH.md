<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。GovHydro4  
============<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovHydro4/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述。**改编自CIM数据模型。水轮机和调速器。代表具有直截了当的笔架结构和传统 "冲床 "类型的水力调节器的工厂。  该模型可用于表示简单、混流式、佩尔顿或卡普兰水轮机。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `at[number]`: 涡轮机增益（At）。  典型值=1.2。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bgv0[number]`: 卡普兰叶片伺服点0（Bgv0）。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bgv1[number]`: 卡普兰叶片伺服点1（Bgv1）。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bgv2[number]`: 卡普兰叶片伺服点2（Bgv2）。典型值=0。典型值弗朗西斯=0，卡普兰=0.1。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bgv3[number]`: 卡普兰叶片伺服点3（Bgv3）。典型值=0。典型值弗朗西斯=0，卡普兰=0.667。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bgv4[number]`: 卡普兰叶片伺服点4（Bgv4）。  典型值=0。典型值弗朗西斯=0，卡普兰=0.9。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bgv5[number]`: 卡普兰叶片伺服点5（Bgv5）。典型值=0。典型值弗朗西斯=0，卡普兰=1。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bmax[number]`: 最大叶片调整系数（Bmax）。典型值=0。典型值弗朗西斯=0，卡普兰=1.1276。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `db1[number]`: 有意的死区宽度（db1）。  单位=Hz。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `db2[number]`: 非故意死区（db2）。  单位=MW。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: 对这个项目的描述  - `dturb[number]`: 涡轮机阻尼系数（Dturb）。  单位=delta P（MWbase的PU）/delta速度（PU）。典型值=0.5。  典型值 混流=1.1，卡普兰=1.1。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `eps[number]`: 有意的db滞后（eps）。  单位=Hz。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gmax[number]`: 最大闸门开度，MWbase的PU（Gmax）。  典型值=1。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gmin[number]`: 最小闸门开度，MWbase的PU（Gmin）。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv0[number]`: 非线性增益点0，PU gv（Gv0）。典型值 = 0.典型值 Francis = 0.1, Kaplan = 0.1.默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv1[number]`: 非线性增益点1，PU gv（Gv1）。典型值 = 0.典型值 Francis = 0.4, Kaplan = 0.4.默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv2[number]`: 非线性增益点2，PU gv（Gv2）。典型值 = 0.典型值 Francis = 0.5, Kaplan = 0.5.默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv3[number]`: 非线性增益点3，PU gv（Gv3）。典型值 = 0.典型值 Francis = 0.7, Kaplan = 0.7.默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv4[number]`: 非线性增益点4，PU gv（Gv4）。典型值 = 0.典型值 Francis = 0.8, Kaplan = 0.8.默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv5[number]`: 非线性增益点5，PU gv（Gv5）。典型值 = 0.典型值 Francis = 0.9, Kaplan = 0.9.默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `hdam[number]`: 大坝上的可用水头（hdam）。  典型值=1。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: 实体的唯一标识符  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `mwbase[number]`: 功率值的基础（MWbase）（>0）。  单位=MW。默认：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `pgv0[number]`: 非线性增益点0，PU功率（Pgv0）。  典型值=0。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pgv1[number]`: 非线性增益点1，PU功率（Pgv1）。典型值 = 0.典型值 Francis = 0.42, Kaplan = 0.35.默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pgv2[number]`: 非线性增益点2，PU功率（Pgv2）。典型值 = 0.典型值 Francis = 0.56, Kaplan = 0.468.默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pgv3[number]`: 非线性增益点3，PU功率（Pgv3）。典型值 = 0.典型值 Francis = 0.8, Kaplan = 0.796.默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pgv4[number]`: 非线性增益点4，PU功率（Pgv4）。典型值 = 0.典型值 Francis = 0.9, Kaplan = 0.917.默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pgv5[number]`: 非线性增益点5，PU功率（Pgv5）。  典型值 = 0。典型值 Francis = 0.97，Kaplan = 0.99。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `qn1[number]`: 额定扬程下的空载流量（Qnl）。典型值=0.08。  典型值 Francis = 0, Kaplan = 0. 默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rperm[number]`: 永久下降（Rperm）。  典型值=0.05。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rtemp[number]`: 临时下降（Rtemp）。  典型值=0.3。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `tblade[number]`: 叶片伺服时间常数（Tblade）。  典型值=100。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tg[number]`: 门控伺服时间常数（Tg）（>0）。  典型值=0.5。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tp[number]`: 先导伺服时间常数（Tp）。  典型值=0.1。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tr[number]`: Dashpot时间常数（Tr）（>0）。  典型值=5。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw[number]`: 水的惯性时间常数（Tw）（>0）。  典型值=1。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI类型。它必须是GovHydro4  - `uc[number]`: 最大闸门关闭速度（Uc）。  典型值=0.2。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `uo[number]`: 最大闸门开启速度（Uo）。  典型的Vlaue = 0.2。默认：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
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
GovHydro4:    
  description: 'Adapted from CIM data models. Hydro turbine and governor. Represents plants with straight-forward penstock configurations and hydraulic governors of traditional ''dashpot'' type.  This model can be used to represent simple, Francis, Pelton or Kaplan turbines.'    
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
    bgv0:    
      description: 'Kaplan blade servo point 0 (Bgv0).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bgv1:    
      description: 'Kaplan blade servo point 1 (Bgv1).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bgv2:    
      description: 'Kaplan blade servo point 2 (Bgv2). Typical Value = 0.  Typical Value Francis = 0, Kaplan = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bgv3:    
      description: 'Kaplan blade servo point 3 (Bgv3). Typical Value = 0.  Typical Value Francis = 0, Kaplan = 0.667. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bgv4:    
      description: 'Kaplan blade servo point 4 (Bgv4).  Typical Value = 0.  Typical Value Francis = 0, Kaplan = 0.9. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bgv5:    
      description: 'Kaplan blade servo point 5 (Bgv5). Typical Value = 0.  Typical Value Francis = 0, Kaplan = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bmax:    
      description: 'Maximum blade adjustment factor (Bmax). Typical Value = 0.  Typical Value Francis = 0, Kaplan = 1.1276. Default: 0.0'    
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
      description: 'Intentional deadband width (db1).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
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
      description: 'Turbine damping factor (Dturb).  Unit = delta P (PU of MWbase) / delta speed (PU). Typical Value = 0.5.  Typical Value Francis = 1.1, Kaplan = 1.1. Default: 0.0'    
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
    gmax:    
      description: 'Maximum gate opening, PU of MWbase (Gmax).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gmin:    
      description: 'Minimum gate opening, PU of MWbase (Gmin).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv0:    
      description: 'Nonlinear gain point 0, PU gv (Gv0). Typical Value = 0.  Typical Value Francis = 0.1, Kaplan = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv1:    
      description: 'Nonlinear gain point 1, PU gv (Gv1). Typical Value = 0.  Typical Value Francis = 0.4, Kaplan = 0.4. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv2:    
      description: 'Nonlinear gain point 2, PU gv (Gv2). Typical Value = 0.  Typical Value Francis = 0.5, Kaplan = 0.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv3:    
      description: 'Nonlinear gain point 3, PU gv (Gv3). Typical Value = 0.  Typical Value Francis = 0.7, Kaplan = 0.7. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv4:    
      description: 'Nonlinear gain point 4, PU gv (Gv4). Typical Value = 0.  Typical Value Francis = 0.8, Kaplan = 0.8. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv5:    
      description: 'Nonlinear gain point 5, PU gv (Gv5). Typical Value = 0.  Typical Value Francis = 0.9, Kaplan = 0.9. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    hdam:    
      description: 'Head available at dam (hdam).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &govhydro4_-_properties_-_owner_-_items_-_anyof    
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
        anyOf: *govhydro4_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    pgv0:    
      description: 'Nonlinear gain point 0, PU power (Pgv0).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pgv1:    
      description: 'Nonlinear gain point 1, PU power (Pgv1). Typical Value = 0.  Typical Value Francis = 0.42, Kaplan = 0.35. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pgv2:    
      description: 'Nonlinear gain point 2, PU power (Pgv2). Typical Value = 0.  Typical Value Francis = 0.56, Kaplan = 0.468. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pgv3:    
      description: 'Nonlinear gain point 3, PU power (Pgv3). Typical Value = 0.  Typical Value Francis = 0.8, Kaplan = 0.796. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pgv4:    
      description: 'Nonlinear gain point 4, PU power (Pgv4). Typical Value = 0.  Typical Value Francis = 0.9, Kaplan = 0.917. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pgv5:    
      description: 'Nonlinear gain point 5, PU power (Pgv5).  Typical Value = 0.  Typical Value Francis = 0.97, Kaplan = 0.99. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    qn1:    
      description: 'No-load flow at nominal head (Qnl). Typical Value = 0.08.  Typical Value Francis = 0, Kaplan = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rperm:    
      description: 'Permanent droop (Rperm).  Typical Value = 0.05. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rtemp:    
      description: 'Temporary droop (Rtemp).  Typical Value = 0.3. Default: 0'    
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
    tblade:    
      description: 'Blade servo time constant (Tblade).  Typical Value = 100. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tg:    
      description: 'Gate servo time constant (Tg) (>0).  Typical Value = 0.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tp:    
      description: 'Pilot servo time constant (Tp).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tr:    
      description: 'Dashpot time constant (Tr) (>0).  Typical Value = 5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tw:    
      description: 'Water inertia time constant (Tw) (>0).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be GovHydro4'    
      enum:    
        - GovHydro4    
      type: string    
      x-ngsi:    
        type: Property    
    uc:    
      description: 'Max gate closing velocity (Uc).  Typical Value = 0.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    uo:    
      description: 'Max gate opening velocity (Uo).  Typical Vlaue = 0.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovHydro4/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/GovHydro4/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
不提供JSON-LD格式的GovHydro4的例子作为关键值。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
不提供规范化的JSON-LD格式的GovHydro4的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
不提供JSON-LD格式的GovHydro4的例子，作为key-values。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
不提供规范化的JSON-LD格式的GovHydro4的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
