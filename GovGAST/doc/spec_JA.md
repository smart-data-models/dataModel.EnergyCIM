エンティティGovGAST  
=============  
[オープンライセンス](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovGAST/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述です。**CIMデータモデルから採用。単軸ガスタービン。  

## プロパティのリスト  

- `address`: 郵送先住所  - `alternateName`: このアイテムの別称  - `areaServed`: サービスや提供されるアイテムが提供される地理的なエリア  - `at`: Ambient Temperature Load Limit (Load Limit)の略。  代表値＝1。初期値：0.0  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `description`: このアイテムの説明  - `dturb`: タービンのダンピングファクター（Dturb）。  代表値＝0.18。デフォルト：0.0  - `id`: エンティティのユニークな識別子  - `kt`: 温度リミッタゲイン（Kt）。  代表値＝3。初期値：0.0  - `location`: アイテムへのGeojson参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygonのいずれかです。  - `mwbase`: パワー値のベース（MWbase）（＞0）。デフォルト：0.0  - `name`: このアイテムの名前です。  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `r`: 永久垂下（R）。  代表値＝0.04。初期値：0.0  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `t1`: ガバナー機構時定数（T1）。  T1は、レートリミッターが作動していないときに見られる、小さな外乱に対するガバナーの自然なバルブ位置決め時定数を表します。  典型的な値は0.5です。デフォルト：0  - `t2`: タービン出力時定数（T2）。  T2は、ガスタービンエンジンの内部エネルギー蓄積による遅延を表しています。T2は、多軸エンジンの圧縮機スプールの加速や、空力発電装置のフリーパワータービンのプレナム内のガスの圧縮性などに伴う遅延を大まかに表すために使用することができる。  典型的な値は0.5です。デフォルト：0  - `t3`: タービン排気温度時定数（T3）。  代表値＝3。デフォルト：0  - `type`: NGSIタイプです。GovGASTでなければならない  - `vmax`: 最大タービン出力、MWbaseのPU（Vmax）。  代表値＝1。デフォルト：0.0  - `vmin`: 最小タービン出力、MWbaseのPU（Vmin）。  代表値＝0、デフォルト：0.0    
必須項目  
CIMデータモデルとCIMpyからの採用 - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy)。このデータモデルは、IEC61970規格で規定されたCommon Information Model (CIM)をスマートデータモデルに直接変換したものです。このモデルがベースとしているpythonクラスは、Institute for Automation of Complex Power Systems (ACS)、EON Energy Research Center (EONERC)、RWTH University Aachen (ドイツ) の3団体によって開発されました。一部のプロパティのタイプが間違っている場合があります。このような場合には、問題を提起するか、info@smartdatamodels.org にメールを送ってください。  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます）  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GovGAST:    
  description: 'Adapted from CIM data models. Single shaft gas turbine.'    
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
      description: 'Ambient temperature load limit (Load Limit).  Typical Value = 1. Default: 0.0'    
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
    dturb:    
      description: 'Turbine damping factor (Dturb).  Typical Value = 0.18. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &govgast_-_properties_-_owner_-_items_-_anyof    
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
    kt:    
      description: 'Temperature limiter gain (Kt).  Typical Value = 3. Default: 0.0'    
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
      description: 'Base for power values (MWbase) (> 0). Default: 0.0'    
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
        anyOf: *govgast_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    r:    
      description: 'Permanent droop (R).  Typical Value = 0.04. Default: 0.0'    
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
    t1:    
      description: 'Governor mechanism time constant (T1).  T1 represents the natural valve positioning time constant of the governor for small disturbances, as seen when rate limiting is not in effect.  Typical Value = 0.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t2:    
      description: 'Turbine power time constant (T2).  T2 represents delay due to internal energy storage of the gas turbine engine. T2 can be used to give a rough approximation to the delay associated with acceleration of the compressor spool of a multi-shaft engine, or with the compressibility of gas in the plenum of a the free power turbine of an aero-derivative unit, for example.  Typical Value = 0.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t3:    
      description: 'Turbine exhaust temperature time constant (T3).  Typical Value = 3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be GovGAST'    
      enum:    
        - GovGAST    
      type: string    
      x-ngsi:    
        type: Property    
    vmax:    
      description: 'Maximum turbine power, PU of MWbase (Vmax).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vmin:    
      description: 'Minimum turbine power, PU of MWbase (Vmin).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovGAST/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/GovGAST/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## ペイロードの例  
key-valuesとしてJSON-LD形式のGovGASTの例を利用できません。これは、`options=keyValues`を使用した場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
正規化されたJSON-LD形式のGovGASTの例はありません。オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
JSON-LD形式のGovGASTの例をkey-valuesとして利用できません。これは`options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
正規化されたJSON-LD形式のGovGASTの例はありません。オプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。