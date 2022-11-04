<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。GovHydroWEH  
==============<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovHydroWEH/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述。**改编自CIM数据模型。伍德沃德水电调速器模型.**  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `db[number]`: 速度死区（db）。默认：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: 对这个项目的描述  - `dicn[number]`: 允许积分控制器超过门限值前进的数值（Dicn）。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dpv[number]`: 允许先导阀控制器前进超过闸门限制的数值（Dpv）。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dturb[number]`: 涡轮机阻尼系数（Dturb）。  单位=delta P（MWbase的PU）/delta速度（PU）。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `feedbackSignal[number]`: 反馈信号选择（Sw）。true = PID输出（如果R-Perm-Gate=droop和R-Perm-Pe=0）false = 电力（如果R-Perm-Gate=0和R-Perm-Pe=droop）或false = 闸门位置（如果R-Perm-Gate=droop和R-Perm-Pe=0）。默认值。假的  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl1[number]`: 流量门1（Fl1）。  闸门位置点1的流量值，用于查询表，代表通过水轮机的水流量与闸门位置的函数关系，以产生稳定状态的流量。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl2[number]`: 流量门2（Fl2）。  闸门位置点2的流量值，用于查询表，代表通过水轮机的水流量与闸门位置的函数关系，以产生稳定状态的流量。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl3[number]`: 流量门3（Fl3）。  闸门位置点3的流量值，用于查询表，代表通过水轮机的水流量与闸门位置的函数关系，以产生稳定状态的流量。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl4[number]`: 流量门4（Fl4）。  闸门位置点4的流量值，用于查询表，代表通过水轮机的水流量与闸门位置的函数关系，以产生稳定状态的流量。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl5[number]`: 流量门5（Fl5）。  闸门位置点5的流量值，用于查询表，代表通过水轮机的水流量与闸门位置的函数关系，以产生稳定状态的流量。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp1[number]`: 流量P1（Fp1）。  用于查找表的第1点的涡轮机流量值，代表机器MVA额定值上的单位机械功率与涡轮机流量的关系。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp10[number]`: 流量P10（Fp10）。  用于查找表的第10点的涡轮机流量值，代表机器MVA额定值上的单位机械功率与涡轮机流量的关系。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp2[number]`: 流量P2（Fp2）。  查询表第2点的涡轮流量值，代表机器MVA额定值上的单位机械功率与涡轮流量的关系。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp3[number]`: 流量P3（Fp3）。  查询表第3点的涡轮流量值，代表机器MVA额定值上的单位机械功率与涡轮流量的关系。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp4[number]`: 流量P4（Fp4）。  查询表第4点的涡轮流量值，代表机器MVA额定值上的单位机械功率与涡轮流量的关系。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp5[number]`: 流量P5（Fp5）。  用于查找表的第5点的涡轮机流量值，代表机器MVA额定值上的单位机械功率与涡轮机流量的关系。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp6[number]`: 流量P6（Fp6）。  用于查找表的第6点的涡轮机流量值，代表机器MVA额定值上的单位机械功率与涡轮机流量的关系。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp7[number]`: 流量P7（Fp7）。  用于查找表的第7点的涡轮机流量值，代表机器MVA额定值上的单位机械功率与涡轮机流量的关系。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp8[number]`: 流量P8（Fp8）。  查询表第8点的涡轮流量值，代表机器MVA额定值上的单位机械功率与涡轮流量的关系。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp9[number]`: 流量P9（Fp9）。  用于查找表的第9点的涡轮机流量值，代表机器MVA额定值上的单位机械功率与涡轮机流量的关系。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gmax[number]`: 最大闸门位置（Gmax）。默认：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gmin[number]`: 最小闸门位置（Gmin）。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gtmxcl[number]`: 最大闸门关闭率（Gtmxcl）。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gtmxop[number]`: 最大闸门打开率（Gtmxop）。默认：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv1[number]`: 闸门1（Gv1）。  用于查找表的第1点的闸门位置值，代表通过水轮机的水流与闸门位置的函数关系，以产生稳态流量。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv2[number]`: 闸门2（Gv2）。  用于查找表的第2点的闸门位置值，代表通过水轮机的水流与闸门位置的函数关系，以产生稳态流量。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv3[number]`: 闸门3（Gv3）。  用于查找表的第3点的闸门位置值，表示通过水轮机的水流与闸门位置的函数关系，以产生稳态流量。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv4[number]`: 闸门4（Gv4）。  用于查找表的第4点的闸门位置值，表示通过水轮机的水流与闸门位置的函数关系，以产生稳态流量。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv5[number]`: 闸门5（Gv5）。  用于查找表的第5点的闸门位置值，表示通过水轮机的水流与闸门位置的函数关系，以产生稳态流量。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: 实体的唯一标识符  - `kd[number]`: 衍生控制器的衍生增益（Kd）。默认：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ki[number]`: 衍生控制器积分增益（Ki）。默认：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kp[number]`: 衍生控制增益（Kp）。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `mwbase[number]`: 功率值的基础（MWbase）（>0）。  单位=MW。默认：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `pmss1[number]`: Pmss流量P1（Pmss1）。  涡轮机流量点1的机械功率输出Pmss，用于查询表，代表机器MVA额定值上的单位机械功率与涡轮机流量的关系。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss10[number]`: Pmss流量P10（Pmss10）。  涡轮机流量点10的机械功率输出Pmss，用于查询表，代表机器MVA额定值上的单位机械功率与涡轮机流量的关系。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss2[number]`: Pmss流量P2（Pmss2）。  涡轮机流量点2的机械功率输出Pmss，用于查询表，代表机器MVA额定值上的单位机械功率与涡轮机流量的关系。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss3[number]`: Pmss流量P3（Pmss3）。  涡轮机流量点3的机械功率输出Pmss，用于查询表，代表机器MVA额定值上的单位机械功率与涡轮机流量的关系。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss4[number]`: Pmss流量P4（Pmss4）。  涡轮机流量点4的机械功率输出Pmss，用于查询表，代表机器MVA额定值上的单位机械功率与涡轮机流量的关系。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss5[number]`: Pmss流量P5（Pmss5）。  涡轮机流量点5的机械功率输出Pmss，用于查询表，代表机器MVA额定值上的单位机械功率与涡轮机流量的关系。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss6[number]`: Pmss流量P6（Pmss6）。  涡轮机流量点6的机械功率输出Pmss，用于查询表，代表机器MVA额定值上的单位机械功率与涡轮机流量的关系。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss7[number]`: Pmss流量P7（Pmss7）。  涡轮机流量点7的机械功率输出Pmss，用于查询表，代表机器MVA额定值上的单位机械功率与涡轮机流量的关系。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss8[number]`: Pmss流量P8（Pmss8）。  涡轮机流量点8的机械功率输出Pmss，用于查询表，代表机器MVA额定值上的单位机械功率与涡轮机流量的关系。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss9[number]`: Pmss流量P9（Pmss9）。  涡轮机流量点9的机械功率输出Pmss，用于查询表，代表机器MVA额定值上的单位机械功率与涡轮机流量的关系。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rpg[number]`: 调速器输出反馈的永久下降（R-Perm-Gate）。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rpp[number]`: 电功率反馈的永久下降（R-Perm-Pe）。默认值：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `td[number]`: 衍生控制器的时间常数，用于限制超出击穿频率的衍生特性，以避免高频噪声的放大（Td）。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tdv[number]`: 分配阀时滞时间常数（Tdv）。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tg[number]`: 允许分配阀控制器前进到超过闸门移动速率限制（Tg）的数值。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tp[number]`: 先导阀时滞时间常数（Tp）。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tpe[number]`: 电功率下降时间常数（Tpe）。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw[number]`: 水的惯性时间常数（Tw）（>0）。默认值：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI类型。它必须是GovHydroWEH  <!-- /30-PropertiesList -->  
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
GovHydroWEH:    
  description: 'Adapted from CIM data models. Woodward Electric Hydro Governor Model.'    
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
    db:    
      description: 'Speed Dead Band (db). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    description:    
      description: 'A description of this item'    
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
      anyOf: &govhydroweh_-_properties_-_owner_-_items_-_anyof    
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
        anyOf: *govhydroweh_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
      description: 'NGSI type. It has to be GovHydroWEH'    
      enum:    
        - GovHydroWEH    
      type: string    
      x-ngsi:    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
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
## ＃＃＃＃有效载荷的例子  
不提供JSON-LD格式的GovHydroWEH的例子，作为关键值。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
不提供规范化的JSON-LD格式的GovHydroWEH的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
不提供JSON-LD格式的GovHydroWEH的例子，作为关键值。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
不提供规范化的JSON-LD格式的GovHydroWEH的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
