<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：GovHydroWEH  
==============<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovHydroWEH/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：** 改编自 CIM 数据模型。伍德沃德电力公司水电调速器模型。  
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
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `db[number]`: 速度死区 (db)。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: 项目描述  - `dicn[number]`: 允许积分控制器超越门限值 (Dicn) 前进的值。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dpv[number]`: 允许先导阀控制器前进到闸门限值 (Dpv) 以外的值。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dturb[number]`: 涡轮机阻尼系数 (Dturb)。  单位 = delta P（MWbase 的 PU）/delta speed (PU)。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `feedbackSignal[number]`: true = PID 输出（如果 R-Perm-Gate=droop 和 R-Perm-Pe=0）false = 电源（如果 R-Perm-Gate=0 和 R-Perm-Pe=hydroop）或 false = 门位置（如果 R-Perm-Gate=droop 和 R-Perm-Pe=0）。默认值：假  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl1[number]`: 流量闸门 1 (Fl1)。  闸门位置点 1 的流量值，用于查找表，表示水流通过水轮机时与闸门位置的函数关系，以产生稳态流量。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl2[number]`: 流量闸门 2 (Fl2)。  闸门位置点 2 的流量值，用于查找表，表示水流通过水轮机时与闸门位置的函数关系，以产生稳态流量。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl3[number]`: 流量闸门 3 (Fl3)。  闸门位置点 3 的流量值，用于查找表，表示水流通过水轮机时与闸门位置的函数关系，以产生稳态流量。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl4[number]`: 流量闸门 4 (Fl4)。  闸门位置点 4 的流量值，用于查找表，表示水流通过水轮机时与闸门位置的函数关系，以产生稳态流量。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl5[number]`: 流量闸门 5 (Fl5)。  闸门位置点 5 的流量值，用于查找表，表示水流通过水轮机时与闸门位置的函数关系，以产生稳态流量。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp1[number]`: 流量 P1 (Fp1)。  查找表中第 1 点的涡轮流量值，代表机器 MVA 额定值上的单位机械功率与涡轮流量的函数关系。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp10[number]`: 流量 P10 (Fp10)。  查找表中第 10 点的涡轮流量值，表示机器 MVA 额定值上的单位机械功率与涡轮流量的函数关系。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp2[number]`: 流量 P2 (Fp2)。  查找表中第 2 点的涡轮流量值，代表机器 MVA 额定值上的单位机械功率与涡轮流量的函数关系。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp3[number]`: 流量 P3 (Fp3)。  查找表中第 3 点的涡轮流量值，代表机器 MVA 额定值上的单位机械功率与涡轮流量的函数关系。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp4[number]`: 流量 P4 (Fp4)。  查找表中第 4 点的涡轮流量值，代表机器 MVA 额定值上的单位机械功率与涡轮流量的函数关系。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp5[number]`: 流量 P5 (Fp5)。  查找表中第 5 点的涡轮流量值，代表机器 MVA 额定值上的单位机械功率与涡轮流量的函数关系。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp6[number]`: 流量 P6 (Fp6)。  查找表中第 6 点的涡轮流量值，代表机器 MVA 额定值上的单位机械功率与涡轮流量的函数关系。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp7[number]`: 流量 P7 (Fp7)。  查找表中第 7 点的涡轮流量值，代表机器 MVA 额定值上的单位机械功率与涡轮流量的函数关系。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp8[number]`: 流量 P8 (Fp8)。  查找表中第 8 点的涡轮流量值，表示机器 MVA 额定值上的单位机械功率与涡轮流量的函数关系。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp9[number]`: 流量 P9 (Fp9)。  查找表中第 9 点的涡轮流量值，代表机器 MVA 额定值上的单位机械功率与涡轮流量的函数关系。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gmax[number]`: 最大闸门位置 (Gmax)。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gmin[number]`: 最小闸门位置 (Gmin)。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gtmxcl[number]`: 最大闸门关闭速率 (Gtmxcl)。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gtmxop[number]`: 最大闸门开度 (Gtmxop)。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv1[number]`: 闸门 1 (Gv1)。  查找表中 1 号点的闸门位置值，表示水流通过水轮机时与闸门位置的函数关系，以产生稳态流量。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv2[number]`: 2 号闸门 (Gv2)。  表示水流通过水轮机与闸门位置的函数关系，以产生稳态流量的查找表中第 2 点的闸门位置值。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv3[number]`: 闸门 3 (Gv3)。  查找表中 3 号点的闸门位置值，表示水流通过水轮机时与闸门位置的函数关系，以产生稳态流量。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv4[number]`: 4 号闸门 (Gv4)。  4 号闸门的闸门位置值，用于查找表，表示水流通过水轮机时与闸门位置的函数关系，以产生稳态流量。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv5[number]`: 闸门 5 (Gv5)。  查找表中第 5 点的闸门位置值，表示水流通过水轮机时与闸门位置的函数关系，以产生稳态流量。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: 实体的唯一标识符  - `kd[number]`: 导数控制器导数增益 (Kd)。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ki[number]`: 微分控制器积分增益 (Ki)。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kp[number]`: 偏差控制增益 (Kp)。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `mwbase[number]`: 功率值基准 (MWbase) (>0)。  单位 = MW。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `pmss1[number]`: Pmss 流量 P1 (Pmss1)。  用于查找表的涡轮机流量点 1 的机械功率输出 Pmss，表示机器 MVA 额定值上的单位机械功率与涡轮机流量的函数关系。默认值： 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss10[number]`: Pmss 流量 P10 (Pmss10)。  用于查找表的涡轮机流量点 10 的机械功率输出 Pmss，表示机器 MVA 额定值上的单位机械功率与涡轮机流量的函数关系。默认值： 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss2[number]`: Pmss 流量 P2 (Pmss2)。  用于查找表的涡轮机流量点 2 的机械功率输出 Pmss，表示机器 MVA 额定值上的单位机械功率与涡轮机流量的函数关系。默认值： 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss3[number]`: Pmss 流量 P3 (Pmss3)。  用于查找表的涡轮机流量点 3 的机械功率输出 Pmss，表示机器 MVA 额定值上的单位机械功率与涡轮机流量的函数关系。默认值： 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss4[number]`: Pmss 流量 P4 (Pmss4)。  用于查找表的涡轮机流量点 4 的机械功率输出 Pmss，表示机器 MVA 额定值上的单位机械功率与涡轮机流量的函数关系。默认值： 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss5[number]`: Pmss 流量 P5 (Pmss5)。  用于查找表的涡轮机流量点 5 的机械功率输出 Pmss，表示机器 MVA 额定值上的单位机械功率与涡轮机流量的函数关系。默认值： 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss6[number]`: Pmss 流量 P6 (Pmss6)。  用于查找表的涡轮机流量点 6 的机械功率输出 Pmss，表示机器 MVA 额定值上的单位机械功率与涡轮机流量的函数关系。默认值： 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss7[number]`: Pmss 流量 P7 (Pmss7)。  用于查找表的涡轮机流量点 7 的机械功率输出 Pmss，表示机器 MVA 额定值上的单位机械功率与涡轮机流量的函数关系。默认值： 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss8[number]`: Pmss 流量 P8 (Pmss8)。  用于查找表的涡轮机流量点 8 的机械功率输出 Pmss，表示机器 MVA 额定值上的单位机械功率与涡轮机流量的函数关系。默认值： 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss9[number]`: Pmss 流量 P9 (Pmss9)。  用于查找表的涡轮机流量点 9 的机械功率输出 Pmss，表示机器 MVA 额定值上的单位机械功率与涡轮机流量的函数关系。默认值： 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rpg[number]`: 调速器输出反馈的永久下垂（R-Perm-Gate）。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rpp[number]`: 电能反馈永久下垂 (R-Perm-Pe)。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `td[number]`: 导数控制器时间常数，用于限制超出击穿频率的导数特性，以避免高频噪声 (Td) 放大。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tdv[number]`: 分配阀时滞时间常数 (Tdv)。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tg[number]`: 允许分配阀控制器前进超过闸门移动速率限制 (Tg) 的值。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tp[number]`: 先导阀时滞时间常数 (Tp)。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tpe[number]`: 电功率下降时间常数 (Tpe)。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw[number]`: 水惯性时间常数 (Tw) (>0)。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI 类型。必须是 GovHydroWEH  <!-- /30-PropertiesList -->  
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
## 有效载荷示例  
以 JSON-LD 格式作为键值的 GovHydroWEH 示例不可用。当使用 "options=keyValues "时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
未提供规范化 JSON-LD 格式的 GovHydroWEH 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
以 JSON-LD 格式作为键值的 GovHydroWEH 示例不可用。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
未提供规范化 JSON-LD 格式的 GovHydroWEH 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
