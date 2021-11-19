エンティティGeneratingUnit  
====================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GeneratingUnit/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述です。**CIMデータモデルからの採用。機械的な動力を交流電力に変換するための、単一または一連の同期機のこと。例えば、セット内の個々の機械はスケジューリングのために定義されるが、セットに対しては単一の制御信号が生成される。この場合、セットの各メンバーのGeneratingUnitと、セットに対応する追加のGeneratingUnitが存在することになる。  

## プロパティのリスト  

- `ControlAreaGeneratingUnit`: この発電ユニットのControlAreaの仕様。デフォルト：'list'  - `GrossToNetActivePowerCurves`: 発電ユニットは、ユニットの損失および補助電力要件を記述する総有効電力／正味有効電力曲線を持つことができる。デフォルト：'list'  - `RotatingMachine`: 同期機は発電機として動作することがあり、その場合は発電ユニットのメンバーとなる。デフォルトは「リスト」。  - `address`: 郵送先住所  - `alternateName`: このアイテムの別称  - `areaServed`: サービスや提供されるアイテムが提供される地理的なエリア  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `description`: このアイテムの説明  - `genControlSource`: 発電ユニットのコントロールのソース。デフォルトです。なし  - `governorSCD`: Governor Speed Changer Droopの略。   これは、発電機の出力の変化を、発電機の公称出力と公称周波数で正規化した周波数の変化で割ったもので、単位はパーセント、負の値で表される。速度変更ドロップの値が正であれば、周波数が低下したときに追加の発電機出力が得られます。デフォルト：0.0  - `id`: エンティティのユニークな識別子  - `initialP`: 本ネットワーク構成における本機の初期有効電力のパワーフロー結果を保存するために使用されるデフォルトの初期有効電力。デフォルト：0.0  - `location`: アイテムへのGeojson参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygonのいずれかです。  - `longPF`: 発電ユニットの長期経済参加係数。デフォルト：0.0  - `maxOperatingP`: ディスパッチャーが本機に入力できる動作有効電力の上限値です。デフォルト：0.0  - `maximumAllowableSpinningReserve`: スピニングリザーブの最大許容値。現在の動作点に関わらず、スピニングリザーブがこの値より大きいと判断されることはありません。デフォルト：0.0  - `minOperatingP`: ディスパッチャーが本機に入力できる動作有効電力の最小値を示します。デフォルト：0.0  - `name`: このアイテムの名前です。  - `nominalP`: 発電ユニットの公称電力。  governorSCD 属性）のようなパーセンテージベースの属性に正確な意味を与えるために使用される。この属性は、RotatingMachine.resatedS と同等またはそれ以下の正の値でなければならない。デフォルト：0.0  - `normalPF`: 発電ユニットの経済参加係数。デフォルト：0.0  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `ratedGrossMaxP`: ユニットの総定格最大容量（簿価）。デフォルト：0.0  - `ratedGrossMinP`: 送電網に電力を供給している間、ユニットが安全に運転できる総定格最小発電量。デフォルト：0.0  - `ratedNetMaxP`: 定格総容量から、工場内の機械を動かすための補助動力を差し引いた正味の定格総容量。デフォルト：0.0  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `shortPF`: 発電ユニットの短期経済参加係数。デフォルト：0.0  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `startupCost`: GeneratingUnitが起動するたびに発生する初期起動コスト。デフォルト：0.0  - `totalEfficiency`: 燃料を電気エネルギーに変換する際のユニットの効率。デフォルト：0.0  - `type`: NGSIタイプ。GeneratingUnitでなければならない。  - `variableCost`: ActivePowerの1ユニットあたりの生産にかかる変動費成分です。デフォルト：0.0    
必須項目  
CIMデータモデルとCIMpyからの採用 - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy)。このデータモデルは、IEC61970規格で規定されたCommon Information Model (CIM)をスマートデータモデルに直接変換したものです。このモデルがベースとしているpythonクラスは、Institute for Automation of Complex Power Systems (ACS)、EON Energy Research Center (EONERC)、RWTH University Aachen (ドイツ) の3団体によって開発されました。一部のプロパティのタイプが間違っている場合があります。このような場合には、問題を提起するか、info@smartdatamodels.org にメールを送ってください。  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます）  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GeneratingUnit:    
  description: 'Adapted from CIM data models. A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.'    
  properties:    
    ControlAreaGeneratingUnit:    
      description: 'ControlArea specifications for this generating unit. Default: ''list'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    GrossToNetActivePowerCurves:    
      description: 'A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit. Default: ''list'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    RotatingMachine:    
      description: 'A synchronous machine may operate as a generator and as such becomes a member of a generating unit. Default: ''list'''    
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
    genControlSource:    
      description: 'The source of controls for a generating unit. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    governorSCD:    
      description: 'Governor Speed Changer Droop.   This is the change in generator power output divided by the change in frequency normalized by the nominal power of the generator and the nominal frequency and expressed in percent and negated. A positive value of speed change droop provides additional generator output upon a drop in frequency. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &generatingunit_-_properties_-_owner_-_items_-_anyof    
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
    initialP:    
      description: 'Default initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration. Default: 0.0'    
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
    longPF:    
      description: 'Generating unit long term economic participation factor. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    maxOperatingP:    
      description: 'This is the maximum operating active power limit the dispatcher can enter for this unit. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    maximumAllowableSpinningReserve:    
      description: 'Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    minOperatingP:    
      description: 'This is the minimum operating active power limit the dispatcher can enter for this unit. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    nominalP:    
      description: 'The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes such as the governor speed change droop (governorSCD attribute). The attribute shall be a positive value equal or less than RotatingMachine.ratedS. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    normalPF:    
      description: 'Generating unit economic participation factor. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *generatingunit_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    ratedGrossMaxP:    
      description: 'The unit`s gross rated maximum capacity (book value). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ratedGrossMinP:    
      description: 'The gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission grid. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ratedNetMaxP:    
      description: 'The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity. Default: 0.0'    
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
    shortPF:    
      description: 'Generating unit short term economic participation factor. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    startupCost:    
      description: 'The initial startup cost incurred for each start of the GeneratingUnit. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    totalEfficiency:    
      description: 'The efficiency of the unit in converting the fuel into electrical energy. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be GeneratingUnit'    
      enum:    
        - GeneratingUnit    
      type: string    
      x-ngsi:    
        type: Property    
    variableCost:    
      description: 'The variable cost component of production per unit of ActivePower. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GeneratingUnit/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/GeneratingUnit/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## ペイロードの例  
GeneratingUnitの例をJSON-LD形式のkey-valuesにしたものは利用できません。これはNGSI-v2の`options=keyValues`との互換性があり、個々のエンティティのコンテキストデータを返します。  
GeneratingUnitの例をJSON-LD形式で正規化したものはありません。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
GeneratingUnitの例をJSON-LD形式のkey-valuesにしたものは利用できません。これは、`options=keyValues`を使った場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
GeneratingUnitの例をJSON-LD形式で正規化したものはありません。オプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
