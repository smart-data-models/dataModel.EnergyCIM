<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティGovHydroPID2  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovHydroPID2/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述。**CIMデータモデルから引用しています。水力タービンおよびガバナー。直線的なペンストック構成と三項電動油圧ガバナー（例：Woodard electronic）を持つプラントを表す**。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別称  - `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `atw[number]`: Tw (Atw)を乗じる係数。  代表値＝0 デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `d[number]`: タービンのダンピングファクター（D）。  単位＝デルタP／デルタスピード。  典型的な値 = 0. デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `feedbackSignal[number]`: フィードバック信号タイプフラグ(Flag) true = ゲート位置フィードバック信号を使用 false = Peを使用。デフォルトFalse  . Model: [https://schema.org/Number](https://schema.org/Number)- `g0[number]`: 速度無負荷時のゲート開度 (G0)。  代表値＝0 デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `g1[number]`: 中間ゲート開度(G1)。  代表値＝0。デフォルト：0.0。  . Model: [https://schema.org/Number](https://schema.org/Number)- `g2[number]`: 中間ゲート開度(G2)。  代表値 = 0. デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gmax[number]`: 最大ゲート開度 (Gmax)。  代表値 = 0. デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gmin[number]`: 最小ゲート開度 (Gmin)。  代表値 = 0. デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: エンティティの一意な識別子  - `kd[number]`: 微分ゲイン（Kd）。  代表値 = 0. デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ki[number]`: リセットゲイン（Ki）。  単位：PU/sec.  代表値 = 0. 初期値: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kp[number]`: 比例ゲイン（Kp）。  代表値＝0 デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `mwbase[number]`: 電力値のベース（MWbase）（>0）。  単位＝MW。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: このアイテムの名称です。  - `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリストです。  - `p1[number]`: ゲートオープン時の電力G1 (P1)。  代表値＝0 デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `p2[number]`: ゲート開放時電力 G2 (P2)。  代表値＝0 デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `p3[number]`: ゲート全開時の電力 (P3)。  代表値＝0 デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rperm[number]`: パーマネントドロップ(Rperm)。  代表値＝0 デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `ta[number]`: コントローラ時定数 (Ta)(>0)。  代表値＝0 デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tb[number]`: ゲートサーボ時定数(Tb) (>0).  代表値＝0 デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `treg[number]`: 速度検出器の時定数（Treg）。  代表値＝0 デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw[number]`: 水の慣性時定数(Tw) (>0).  代表値 = 0. デフォルト: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSIタイプ。GovHydroPID2である必要があります。  - `velmax[number]`: 最大ゲート開閉速度（Velmax）。  単位：PU/sec。  代表値 = 0. デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `velmin[number]`: ゲート最大閉速度（Velmin）。  単位：PU/sec。  代表値 = 0. デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
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
GovHydroPID2:    
  description: 'Adapted from CIM data models. Hydro turbine and governor. Represents plants with straight forward penstock configurations and three term electro-hydraulic governors (i.e. Woodard electronic).'    
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
    atw:    
      description: 'Factor multiplying Tw (Atw).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    d:    
      description: 'Turbine damping factor (D).  Unit = delta P / delta speed.  Typical Value = 0. Default: 0.0'    
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
    feedbackSignal:    
      description: 'Feedback signal type flag (Flag). true = use gate position feedback signal false = use Pe. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    g0:    
      description: 'Gate opening at speed no load (G0).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    g1:    
      description: 'Intermediate gate opening (G1).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    g2:    
      description: 'Intermediate gate opening (G2).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gmax:    
      description: 'Maximum gate opening (Gmax).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gmin:    
      description: 'Minimum gate opening (Gmin).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &govhydropid2_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Derivative gain (Kd).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ki:    
      description: 'Reset gain (Ki).  Unit = PU/ sec.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kp:    
      description: 'Proportional gain (Kp).  Typical Value = 0. Default: 0.0'    
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
        anyOf: *govhydropid2_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    p1:    
      description: 'Power at gate opening G1 (P1).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    p2:    
      description: 'Power at gate opening G2 (P2).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    p3:    
      description: 'Power at full opened gate (P3).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rperm:    
      description: 'Permanent drop (Rperm).  Typical Value = 0. Default: 0.0'    
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
    ta:    
      description: 'Controller time constant (Ta) (>0).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tb:    
      description: 'Gate servo time constant (Tb) (>0).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    treg:    
      description: 'Speed detector time constant (Treg).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tw:    
      description: 'Water inertia time constant (Tw) (>0).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be GovHydroPID2'    
      enum:    
        - GovHydroPID2    
      type: string    
      x-ngsi:    
        type: Property    
    velmax:    
      description: 'Maximum gate opening velocity (Velmax).  Unit = PU/sec.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    velmin:    
      description: 'Maximum gate closing velocity (Velmin).  Unit = PU/sec.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovHydroPID2/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/GovHydroPID2/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
GovHydroPID2のJSON-LD形式のkey-valuesの例は利用できません。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返す。  
GovHydroPID2のJSON-LD形式を正規化した例はありません。オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返す。  
GovHydroPID2のJSON-LD形式のkey-valuesの例は利用できません。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータが返される。  
GovHydroPID2 を JSON-LD 形式で正規化した例はありません。オプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータが返される。  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
