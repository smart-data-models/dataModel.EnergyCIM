<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティACDCConverter  
===================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ACDCConverter/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述。**CIM データモデルから引用。三相のバルブを持つユニットで、ユニット制御装置、必須の保護装置およびスイッチング装置、DC 蓄積コンデンサ、相リアクトル、変換に使用される場合は補助装置も含む **。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `DCTerminals[number]`: デフォルト：'list'  . Model: [https://schema.org/Number](https://schema.org/Number)- `PccTerminal[number]`: すべてのコンバーターのDC側をこの共通結合端子にリンクさせる。デフォルトなし  . Model: [https://schema.org/Number](https://schema.org/Number)- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別称  - `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `baseS[number]`: コンバータ極の基本皮相電力。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `id[*]`: エンティティの一意な識別子  - `idc[number]`: コンバータの直流電流で、Id とも呼ばれる。コンバータの状態変数で，パワーフローから得られる。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `idleLoss[number]`: 電力転送がない場合の極の有効電力損失。パワーフローで使用されるコンバータ設定データ。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `maxUdc[number]`: コンバータが動作すべきDC側の最大電圧。パワーフローで使用されるコンバータ設定データ。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `minUdc[number]`: コンバータの最小許容直流電圧。パワーフローで使用されるコンバータ構成データ。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: このアイテムの名称です。  - `numberOfValves[number]`: コンバータの弁の数。損失計算で使用される。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリストです。  - `p[number]`: 共通結合点での有効電力。負荷符号を使用し，正符号はノードから流出することを意味する。簡略化されたパワーフローモデルが使用される場合の定常解の開始値。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `poleLossP[number]`: 直流極の有効電力損失 = idleLoss + switchingLoss*|Idc| + resitiveLoss*Idc^2 ロスレス動作の場合 Pdc=Pac 整流器動作で損失を伴う場合 Pdc=Pac-lossP インバータ動作で損失を伴う場合 Pdc=Pac+lossP パワーフローで使用するコンバータ状態変数です。デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `q[number]`: 共通結合点での無効電力。負荷の符号は、正符号はノードから流出することを意味する。簡略化されたパワーフローモデルが使用される場合の定常解の開始値。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ratedUdc[number]`: コンバータの定格直流電圧。UdNとも呼ばれる。パワーフローで使用されるコンバーターのコンフィギュレーションデータ。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `resistiveLoss[number]`: パワーフローで使用されるコンバータ設定データ。poleLossPを参照。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `switchingLoss[number]`: スイッチング損失。ベース皮相電力 `baseS` に対する相対値。poleLossPを参照。デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `targetPpcc[number]`: 共通結合点における，ACグリッドの実電力注入目標値。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `targetUdc[number]`: DC電圧の大きさの目標値。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSIタイプ。ACDCConverterでなければならない。  - `uc[number]`: コンバータ電圧、ブリッジのAC側での電圧。コンバーター状態変数、パワーフローからの結果。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `udc[number]`: DC側のコンバータ電圧，Udとも呼ばれる。コンバータの状態変数で，電力フローから得られる。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `valveU0[number]`: バルブのしきい値電圧。バルブが導通しているときの順方向電圧降下。損失計算で使用される。つまり、switchLossはnumberOfValves * valveU0に依存する。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
<!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
CIMデータモデルとCIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy) から引用した。このデータモデルは、IEC61970規格で規定されたCommon Information Model (CIM)をスマートデータモデルに直接変換したものです。このモデルのベースとなっているpythonクラスは、これらのエンティティInstitute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) and RWTH University Aachen, Germanyによって開発されたものである。一部のプロパティは間違ったタイプを持つことがあります。このような場合は、問題を提起するか、info@smartdatamodels.org にメールを送ってください。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ACDCConverter:    
  description: 'Adapted from CIM data models. A unit with valves for three phases, together with unit control equipment, essential protective and switching devices, DC storage capacitors, phase reactors and auxiliaries, if any, used for conversion.'    
  properties:    
    DCTerminals:    
      description: ' Default: ''list'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    PccTerminal:    
      description: 'All converters` DC sides linked to this point of common coupling terminal. Default: None'    
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
    baseS:    
      description: 'Base apparent power of the converter pole. Default: 0.0'    
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
      anyOf: &acdcconverter_-_properties_-_owner_-_items_-_anyof    
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
    idc:    
      description: 'Converter DC current, also called Id. Converter state variable, result from power flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    idleLoss:    
      description: 'Active power loss in pole at no power transfer. Converter configuration data used in power flow. Default: 0.0'    
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
    maxUdc:    
      description: 'The maximum voltage on the DC side at which the converter should operate. Converter configuration data used in power flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    minUdc:    
      description: 'Min allowed converter DC voltage. Converter configuration data used in power flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    numberOfValves:    
      description: 'Number of valves in the converter. Used in loss calculations. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *acdcconverter_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    p:    
      description: 'Active power at the point of common coupling. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution in the case a simplified power flow model is used. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    poleLossP:    
      description: 'The active power loss at a DC Pole  = idleLoss + switchingLoss*|Idc| + resitiveLoss*Idc^2 For lossless operation Pdc=Pac For rectifier operation with losses Pdc=Pac-lossP For inverter operation with losses Pdc=Pac+lossP Converter state variable used in power flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    q:    
      description: 'Reactive power at the point of common coupling. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution in the case a simplified power flow model is used. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ratedUdc:    
      description: 'Rated converter DC voltage, also called UdN. Converter configuration data used in power flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    resistiveLoss:    
      description: 'Converter configuration data used in power flow. Refer to poleLossP. Default: 0.0'    
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
    switchingLoss:    
      description: 'Switching losses, relative to the base apparent power `baseS`. Refer to poleLossP. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    targetPpcc:    
      description: 'Real power injection target in AC grid, at point of common coupling. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    targetUdc:    
      description: 'Target value for DC voltage magnitude. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be ACDCConverter'    
      enum:    
        - ACDCConverter    
      type: string    
      x-ngsi:    
        type: Property    
    uc:    
      description: 'Converter voltage, the voltage at the AC side of the bridge. Converter state variable, result from power flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    udc:    
      description: 'Converter voltage at the DC side, also called Ud. Converter state variable, result from power flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    valveU0:    
      description: 'Valve threshold voltage. Forward voltage drop when the valve is conducting. Used in loss calculations, i.e. the switchLoss depend on numberOfValves * valveU0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ACDCConverter/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/ACDCConverter/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
ACDCConverterのJSON-LD形式のkey-valuesの例は利用できない。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータが返される。  
ACDCConverter を JSON-LD 形式で正規化した例はない。オプションを使用しない場合はNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返す。  
ACDCConverterのJSON-LD形式のkey-valuesの例は利用できない。これは `options=keyValues` を使ったときに NGSI-LD と互換性があり、個々のエンティティのコンテキストデータが返される。  
ACDCConverter を JSON-LD 形式で正規化した例はない。オプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
