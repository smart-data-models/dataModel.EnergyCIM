エンティティPss2B  
===========  
[オープンライセンス](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/Pss2B/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述です。**CIMデータモデルからの採用。IEEE PSS2Bモデルを修正。  最後に追加のリード/ラグ(またはレート)ブロックを追加(最大4つのリード/ラグの合計)**。  

## プロパティのリスト  

- `a`: 分子の定数（a）。  典型的な値は1です。既定値：0.0  - `address`: 郵送先住所  - `alternateName`: このアイテムの別称  - `areaServed`: サービスや提供されるアイテムが提供される地理的なエリア  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `description`: このアイテムの説明  - `id`: エンティティのユニークな識別子  - `inputSignal1Type`: 入力信号#1の種類。  代表値＝rotorSpeed。デフォルトなし  - `inputSignal2Type`: 入力信号#2の種類。  代表値＝generatorElectricalPower。デフォルト。なし  - `ks1`: スタビライザーゲイン（Ks1）。  代表値＝12。初期値：0.0  - `ks2`: 信号2のゲイン（Ks2）。  代表値＝0.2。初期値：0.0  - `ks3`: 信号#2入力のランプトラッキングフィルタ(Ks3)前のゲイン。  典型的な値は1です。初期値：0.0  - `ks4`: ランプトラッキング・フィルター（Ks4）後の信号＃2入力のゲイン。  典型的な値は1です。初期値：0.0  - `location`: アイテムへのGeojson参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygonのいずれかです。  - `m`: ランプ・トラッキング・フィルター（M）の分母の次数。  典型的な値は5です。初期値：0  - `n`: ランプ・トラッキング・フィルターの次数（N）。  典型的な値は1です。初期値：0  - `name`: このアイテムの名前です。  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `t1`: リード／ラグ時定数（T1）。  代表値＝0.12。デフォルト：0  - `t10`: リード／ラグ時定数（T10）。  代表値＝0、初期値＝0  - `t11`: リード／ラグ時定数（T11）。  代表値＝0、初期値＝0  - `t2`: リード／ラグ時定数（T2）。  代表値＝0.02。デフォルト：0  - `t3`: リード／ラグ時定数（T3）。  代表値＝0.3です。デフォルト：0  - `t4`: リード／ラグ時定数（T4）。  代表値＝0.02。デフォルト：0  - `t6`: 信号#1の時定数(T6)。  代表値＝0、デフォルト：0  - `t7`: 信号2（T7）の時定数。  代表値＝2。デフォルト：0  - `t8`: ランプトラッキングフィルタ（T8）のリード。  典型的な値＝0.2です。デフォルト：0  - `t9`: ランプ・トラッキング・フィルター（T9）のラグ。  代表値＝0.1。初期値：0  - `ta`: リード定数（Ta）。  代表値＝0、初期値＝0  - `tb`: ラグ時定数（Tb）。  代表値＝0、デフォルト：0  - `tw1`: 信号#1(Tw1)の最初のウォッシュアウト。  典型的な値は2です。デフォルト：0  - `tw2`: 信号#1(Tw2)の2回目のウォッシュアウト。  典型的な値は2です。デフォルト：0  - `tw3`: 信号2（Tw3）の最初のウォッシュアウト。  典型的な値は2です。デフォルト：0  - `tw4`: 信号#2(Tw4)の2回目のウォッシュアウト。  代表値＝0、デフォルト：0  - `type`: NGSIタイプであること。Pss2Bでなければならない  - `vsi1max`: 入力信号#1のマックスリミット（Vsi1max）。  典型的な値 = 2.デフォルト：0.0  - `vsi1min`: 入力信号#1の下限値(Vsi1min)。  典型的な値 = -2.デフォルト：0.0  - `vsi2max`: 入力信号#2のマックスリミット（Vsi2max）。  典型的な値 = 2.デフォルト：0.0  - `vsi2min`: 入力信号#2の下限値（Vsi2min）。  典型的な値 = -2.デフォルト：0.0  - `vstmax`: スタビライザー出力の最大リミット（Vstmax）。  代表値＝0.1初期値：0.0  - `vstmin`: スタビライザー出力の下限値（Vstmin）。  代表値＝-0.1初期値：0.0    
必須項目  
CIMデータモデルとCIMpyからの採用 - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy)。このデータモデルは、IEC61970規格で規定されたCommon Information Model (CIM)をスマートデータモデルに直接変換したものです。このモデルがベースとしているpythonクラスは、Institute for Automation of Complex Power Systems (ACS)、EON Energy Research Center (EONERC)、RWTH University Aachen (ドイツ) の3団体によって開発されました。一部のプロパティのタイプが間違っている場合があります。このような場合には、問題を提起するか、info@smartdatamodels.org にメールを送ってください。  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます）  
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
## ペイロードの例  
key-valuesとしてJSON-LD形式のPss2Bの例を利用できません。これは、`options=keyValues`を使用した場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
Pss2BをJSON-LD形式で正規化した例はありません。オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
Pss2Bの例をkey-valuesとしてJSON-LD形式で利用できない。これは、`options=keyValues`を使用した場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
Pss2BをJSON-LD形式で正規化した例はありません。オプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
