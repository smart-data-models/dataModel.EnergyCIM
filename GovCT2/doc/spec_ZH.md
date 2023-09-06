<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：GovCT2  
=========<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovCT2/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**改编自 CIM 数据模型。具有频率相关燃料流量限制的通用调速器模型。  该模型是对 GovCT1model 的修改，以表示特定燃气轮机制造商的随频率变化的燃料流量限制。  
版本： 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理    
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `aset[number]`: 加速度限制器设定点 (Aset)。  单位 = PU/秒。  典型值 = 10。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `db[number]`: 调速器的单位速度死区 (db)。  在大多数应用中，建议将该值设置为零。  典型值 = 0 默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: 项目描述  - `dm[number]`: 转速灵敏系数 (Dm)。  Dm 既可以表示发动机功率随轴速的变化，也可以表示最大功率能力随轴速的变化。  如果它是正值，则表示发动机速度与功率特性随速度增加而下降的斜率。轻微下降特性是往复式发动机和某些航空衍生涡轮机的典型特征。  如果为负值，则假定发动机功率不受轴转速的影响，但最大允许燃油流量会随着轴转速的下降而下降。由于排气温度限制，这是单轴工业汽轮机的特点。  典型值 = 0 默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `flim1[number]`: 频率阈值 1 (Flim1)。  单位 = 赫兹。  典型值 = 59。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `flim10[number]`: 频率阈值 10 (Flim10)。  单位 = 赫兹。  典型值 = 0 默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `flim2[number]`: 频率阈值 2 (Flim2)。  单位 = 赫兹。  典型值 = 0 默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `flim3[number]`: 频率阈值 3 (Flim3)。  单位 = 赫兹。  典型值 = 0 默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `flim4[number]`: 频率阈值 4 (Flim4)。  单位 = 赫兹。  典型值 = 0 默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `flim5[number]`: 频率阈值 5 (Flim5)。  单位 = 赫兹。  典型值 = 0 默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `flim6[number]`: 频率阈值 6 (Flim6)。  单位 = 赫兹。  典型值 = 0 默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `flim7[number]`: 频率阈值 7 (Flim7)。  单位 = 赫兹。  典型值 = 0 默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `flim8[number]`: 频率阈值 8 (Flim8)。  单位 = 赫兹。  典型值 = 0 默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `flim9[number]`: 频率阈值 9 (Flim9)。  单位 = 赫兹。  典型值 = 0 默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: 实体的唯一标识符  - `ka[number]`: 加速度限制器增益 (Ka)。  典型值 = 10。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kdgov[number]`: 调速器导数增益 (Kdgov)。  典型值 = 0 默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kigov[number]`: 调速器积分增益（基戈夫）。  典型值 = 0.45。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kiload[number]`: PI 控制器的负载限制器积分增益（Kiload）。  典型值 = 1。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kimw[number]`: 功率控制器（复位）增益（Kimw）。  默认值 0.01 相当于复位时间为 100 秒。  0.001 的值对应相对较慢的负载控制器。  典型值 = 0 默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kpgov[number]`: 调速器比例增益 (Kpgov)。  典型值 = 4。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kpload[number]`: PI 控制器的负载限制器比例增益（Kpload）。  典型值 = 1。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kturb[number]`: 涡轮增益 (Kturb)。  典型值 = 1.9168。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ldref[number]`: 负载限制器参考值 (Ldref)。  典型值 = 1。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `maxerr[number]`: 速度误差信号 (Maxerr) 的最大值。  典型值 = 1。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `minerr[number]`: 速度误差信号 (Minerr) 的最小值。  典型值 =-1。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `mwbase[number]`: 功率值基准 (MWbase) (> 0)。  单位 = MW。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `plim1[number]`: 功率极限 1 (Plim1)。  典型值 = 0.8325。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `plim10[number]`: 功率极限 10 (Plim10)。  典型值 = 0 默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `plim2[number]`: 功率极限 2 (Plim2)。  典型值 = 0 默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `plim3[number]`: 功率极限 3 (Plim3)。  典型值 = 0 默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `plim4[number]`: 功率极限 4 (Plim4)。  典型值 = 0 默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `plim5[number]`: 功率极限 5 (Plim5)。  典型值 = 0 默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `plim6[number]`: 功率极限 6 (Plim6)。  典型值 = 0 默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `plim7[number]`: 功率极限 7 (Plim7)。  典型值 = 0 默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `plim8[number]`: 功率极限 8 (Plim8)。  典型值 = 0 默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `plim9[number]`: 功率极限 9 (Plim9)。  典型值 = 0 默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `prate[number]`: 频率相关功率限制的斜率 (Prate)。  典型值 = 0.017。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `r[number]`: 永久下垂 (R)。  典型值 = 0.05。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rclose[number]`: 最小阀门关闭速率 (Rclose)。  单位 = PU/秒。  典型值 = -99。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rdown[number]`: 最大负载极限下降率 (Rdown)。  典型值 = -99。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ropen[number]`: 最大阀门开启率 (Ropen)。  单位 = PU/秒。  典型值 = 99。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rselect[number]`: 用于下垂的反馈信号 (Rselect)。  典型值 = 电功率。默认值：无  . Model: [https://schema.org/Number](https://schema.org/Number)- `rup[number]`: 负载极限的最大增长率（Rup）。  典型值 = 99。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `ta[number]`: 加速度限制器时间常数 (Ta)。  典型值 = 1。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tact[number]`: 致动器时间常数 (Tact)。  典型值 = 0.4。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tb[number]`: 涡轮滞后时间常数 (Tb)。  典型值 = 0.1。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tc[number]`: 涡轮前置时间常数 (Tc)。  典型值 = 0 默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tdgov[number]`: 调速器导数控制器时间常数 (Tdgov)。  典型值 = 1。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `teng[number]`: 用于表示柴油发动机的传输时间延迟，在柴油发动机中，燃料流量设定的变化与扭矩（Teng）的产生之间存在微小但可测量的传输延迟。  除特别关注传输延迟的特殊情况外，Teng 值均应为零。  典型值 = 0 默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tfload[number]`: 负载限制器时间常数 (Tfload)。  典型值 = 3。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tpelec[number]`: 电力传感器时间常数 (Tpelec)。  典型值 = 2.5。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tsa[number]`: 温度检测前置时间常数 (Tsa)。  典型值 = 0 默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tsb[number]`: 温度检测滞后时间常数 (Tsb)。  典型值 = 50。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI 类型。必须是 GovCT2  - `vmax[number]`: 最大阀门位置限值 (Vmax)。  典型值 = 1。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vmin[number]`: 最小阀门位置限值 (Vmin)。  典型值 = 0.175。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `wfnl[number]`: 空载燃油流量 (Wfnl)。  典型值 = 0.187。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `wfspd[number]`: true = 燃油流量与转速成正比（适用于某些燃气轮机和带正排量喷油器的柴油发动机） false = 燃油控制系统保持燃油流量与发动机转速无关。典型值 = false。默认值：假  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
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
GovCT2:    
  description: Adapted from CIM data models. General governor model with frequency-dependent fuel flow limit.  This model is a modification of the GovCT1model in order to represent the frequency-dependent fuel flow limit of a specific gas turbine manufacturer.    
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
    aset:    
      description: 'Acceleration limiter setpoint (Aset).  Unit = PU/sec.  Typical Value = 10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
      description: 'Speed governor dead band in per unit speed (db).  In the majority of applications, it is recommended that this value be set to zero.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    description:    
      description: A description of this item    
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
      description: NGSI type. It has to be GovCT2    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
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
## 有效载荷示例  
以 JSON-LD 格式作为键值的 GovCT2 示例不可用。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
没有规范化 JSON-LD 格式的 GovCT2 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
以 JSON-LD 格式作为键值的 GovCT2 示例不可用。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
没有规范化 JSON-LD 格式的 GovCT2 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
