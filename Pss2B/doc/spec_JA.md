<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティPss2B  
===========<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/Pss2B/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述。**CIM データモデルからの引用。IEEE PSS2Bモデルを変更。  最後にリード/ラグ（またはレート）ブロックを追加（合計4つまで）。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `a[number]`: 分子定数(a)。  典型的な値 = 1.デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別称  - `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `id[*]`: エンティティの一意な識別子  - `inputSignal1Type[number]`: 入力信号の種類#1。  典型的な値 = rotorSpeed.デフォルトなし  . Model: [https://schema.org/Number](https://schema.org/Number)- `inputSignal2Type[number]`: 入力信号の種類 #2。  典型的な値 = generatorElectricalPower。デフォルトなし  . Model: [https://schema.org/Number](https://schema.org/Number)- `ks1[number]`: スタビライザーのゲイン（Ks1）。  代表的な値＝12。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ks2[number]`: 信号2に対するゲイン（Ks2）。  典型的な値=0.2。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ks3[number]`: ランプトラッキングフィルタ（Ks3）前の信号＃2入力時のゲイン。  典型的な値=1。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ks4[number]`: ランプトラッキングフィルタ（Ks4）後の信号＃2入力時のゲイン。  典型的な値=1。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `m[number]`: ランプトラッキングフィルタの分母オーダー(M)。  典型的な値 = 5.デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `n[number]`: ランプトラッキングフィルタの次数（N）。  典型的な値 = 1.デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: このアイテムの名称です。  - `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリストです。  - `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `t1[number]`: リード/ラグ時定数 (T1)。  典型的な値 = 0.12。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t10[number]`: リード／ラグ時定数（T10）。  代表値＝0 デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t11[number]`: リード/ラグ時定数 (T11)。  代表値＝0 デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t2[number]`: リード/ラグ時定数 (T2)。  典型的な値 = 0.02。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t3[number]`: リード/ラグ時定数 (T3)。  典型的な値 = 0.3。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t4[number]`: リード/ラグ時定数 (T4)。  代表値＝0.02。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t6[number]`: 信号#1 の時定数（T6）。  代表値＝0 デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t7[number]`: 信号番号2（T7）の時定数。  代表的な値＝2。初期値：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t8[number]`: ランプトラッキングフィルタ(T8)のリード。  典型的な値 = 0.2。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t9[number]`: ランプトラッキングフィルタ(T9)のラグ。  典型的な値 = 0.1。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ta[number]`: リード定数(Ta)。  代表値＝0 デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tb[number]`: 遅延時定数 (Tb)。  代表値＝0 デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw1[number]`: 信号1(Tw1)の1回目のウォッシュアウト。  典型的な値=2。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw2[number]`: 信号1(Tw2)の2回目のウォッシュアウト。  典型的な値=2。初期値：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw3[number]`: 信号番号2(Tw3)の最初のウォッシュアウト。  典型的な値=2。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw4[number]`: 信号#2 (Tw4)の2回目のウォッシュアウト。  典型的な値=0 デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSIタイプ。Pss2Bでなければならない  - `vsi1max[number]`: 入力信号＃1の最大リミット値（Vsi1max）。  典型的な値=2。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vsi1min[number]`: 入力信号＃1の最小リミット（Vsi1min）。  典型的な値=-2。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vsi2max[number]`: 入力信号＃2の最大リミット値（Vsi2max）。  典型的な値=2。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vsi2min[number]`: 入力信号＃2の最小リミット値（Vsi2min）。  典型的な値=-2。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vstmax[number]`: スタビライザー出力最大リミット値（Vstmax）。  代表値＝0.1。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vstmin[number]`: スタビライザー出力最小リミット値（Vstmin）。  代表値 = -0.1。初期値：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
<!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
CIMデータモデルとCIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy)から引用。このデータモデルは、IEC61970規格で規定されたCommon Information Model (CIM)をスマートデータモデルに直接変換したものです。このモデルのベースとなっているpythonクラスは、これらのエンティティInstitute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) and RWTH University Aachen, Germanyによって開発されたものである。一部のプロパティが間違ったタイプを持つことがあります。このような場合は、問題を提起するか、info@smartdatamodels.org にメールを送ってください。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Pss2B:    
  description: 'Adapted from CIM data models. Modified IEEE PSS2B Model.  Extra lead/lag (or rate) block added at end (up to 4 lead/lags total).'    
  properties:    
    a:    
      description: 'Numerator constant (a).  Typical Value = 1. Default: 0.0'    
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
      anyOf: &pss2b_-_properties_-_owner_-_items_-_anyof    
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
    inputSignal1Type:    
      description: "Type of input signal #1.  Typical Value = rotorSpeed. Default: None"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    inputSignal2Type:    
      description: "Type of input signal #2.  Typical Value = generatorElectricalPower. Default: None"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ks1:    
      description: 'Stabilizer gain (Ks1).  Typical Value = 12. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ks2:    
      description: "Gain on signal #2 (Ks2).  Typical Value = 0.2. Default: 0.0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ks3:    
      description: "Gain on signal #2 input before ramp-tracking filter (Ks3).  Typical Value = 1. Default: 0.0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ks4:    
      description: "Gain on signal #2 input after ramp-tracking filter (Ks4).  Typical Value = 1. Default: 0.0"    
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
    m:    
      description: 'Denominator order of ramp tracking filter (M).  Typical Value = 5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    n:    
      description: 'Order of ramp tracking filter (N).  Typical Value = 1. Default: 0'    
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
        anyOf: *pss2b_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
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
      description: 'Lead/lag time constant (T1).  Typical Value = 0.12. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t10:    
      description: 'Lead/lag time constant (T10).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t11:    
      description: 'Lead/lag time constant (T11).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t2:    
      description: 'Lead/lag time constant (T2).  Typical Value = 0.02. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t3:    
      description: 'Lead/lag time constant (T3).  Typical Value = 0.3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t4:    
      description: 'Lead/lag time constant (T4).  Typical Value = 0.02. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t6:    
      description: "Time constant on signal #1 (T6).  Typical Value = 0. Default: 0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t7:    
      description: "Time constant on signal #2 (T7).  Typical Value = 2. Default: 0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t8:    
      description: 'Lead of ramp tracking filter (T8).  Typical Value = 0.2. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t9:    
      description: 'Lag of ramp tracking filter (T9).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ta:    
      description: 'Lead constant (Ta).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tb:    
      description: 'Lag time constant (Tb).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tw1:    
      description: "First washout on signal #1 (Tw1).  Typical Value = 2. Default: 0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tw2:    
      description: "Second washout on signal #1 (Tw2).  Typical Value = 2. Default: 0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tw3:    
      description: "First washout on signal #2 (Tw3).  Typical Value = 2. Default: 0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tw4:    
      description: "Second washout on signal #2 (Tw4).  Typical Value = 0. Default: 0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be Pss2B'    
      enum:    
        - Pss2B    
      type: string    
      x-ngsi:    
        type: Property    
    vsi1max:    
      description: "Input signal #1 max limit (Vsi1max).  Typical Value = 2. Default: 0.0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vsi1min:    
      description: "Input signal #1 min limit (Vsi1min).  Typical Value = -2. Default: 0.0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vsi2max:    
      description: "Input signal #2 max limit (Vsi2max).  Typical Value = 2. Default: 0.0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vsi2min:    
      description: "Input signal #2 min limit (Vsi2min).  Typical Value = -2. Default: 0.0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vstmax:    
      description: 'Stabilizer output max limit (Vstmax).  Typical Value = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vstmin:    
      description: 'Stabilizer output min limit (Vstmin).  Typical Value = -0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Pss2B/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/Pss2B/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
Pss2BをJSON-LD形式でkey-valuesにした例は利用できません。これは `options=keyValues` を使った場合に NGSI-v2 と互換性があり、個々のエンティティのコンテキストデータが返される。  
Pss2BをJSON-LD形式で正規化した例はありません。オプションを使用しない場合のNGSI-v2と互換性があり、個々のエンティティのコンテキストデータが返される。  
Pss2BをJSON-LD形式でkey-valuesにした例は利用できません。これは `options=keyValues` を使った場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータが返される。  
Pss2BをJSON-LD形式で正規化した例はありません。オプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータが返される。  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
