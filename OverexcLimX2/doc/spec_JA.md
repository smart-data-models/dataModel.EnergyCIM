エンティティオーバーエクスクライムX2  
===================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/OverexcLimX2/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述です。**CIMデータモデルから採用。フィールド電圧または電流の過励磁リミッタで、自動励磁制御のACマシンの発電機フィールドを、長時間の過励磁による過熱から保護するために設計されている。  

## プロパティのリスト  

- `address`: 郵送先住所  - `alternateName`: このアイテムの別称  - `areaServed`: サービスや提供されるアイテムが提供される地理的なエリア  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `description`: このアイテムの説明  - `efd1`: 逆時間特性（EFD）の低電圧または電流ポイント。  代表値＝1.1。初期値：0.0  - `efd2`: 逆時間特性（EFD）の中間電圧または電流ポイント。  代表値＝1.2。初期値：0.0  - `efd3`: 逆時間特性（EFD）上の高電圧または高電流ポイント。  代表値＝1.5です。初期値：0.0  - `efddes`: m=Fの場合は希望するフィールド電圧、m=Tの場合は希望するフィールド電流(EFD)。  典型的な値は1です。初期値：0.0  - `efdrated`: m=Fの場合は定格フィールド電圧、m=Tの場合はフィールド電流(EFD)。  代表値＝1.05初期値：0.0  - `id`: エンティティのユニークな識別子  - `kmx`: ゲイン（K）。  代表値＝0.002。初期値：0.0  - `location`: アイテムへのGeojson参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygonのいずれかです。  - `m`: (m). true = IFD制限 false = EFD制限。デフォルトはFalse  - `name`: このアイテムの名前です。  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `t1`: 逆時間特性(TIME)上の低電圧または低電流ポイントでエキサイターをトリップさせる時間。  代表値＝120。デフォルト：0  - `t2`: 逆時間特性(TIME)上の電圧または電流の中間点でエキサイターをトリップさせる時間。  代表値＝40。デフォルト：0  - `t3`: 逆時間特性(TIME)上の高電圧または高電流ポイントでエキサイターをトリップさせる時間。  代表値＝15。デフォルト：0  - `type`: NGSIタイプです。OverexcLimX2である必要があります。  - `vlow`: 低電圧制限（V）（>0）。デフォルト：0.0    
必須項目  
CIMデータモデルとCIMpyからの採用 - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy)。このデータモデルは、IEC61970規格で規定されたCommon Information Model (CIM)をスマートデータモデルに直接変換したものです。このモデルがベースとしているpythonクラスは、Institute for Automation of Complex Power Systems (ACS)、EON Energy Research Center (EONERC)、RWTH University Aachen (ドイツ) の3団体によって開発されました。一部のプロパティのタイプが間違っている場合があります。このような場合には、問題を提起するか、info@smartdatamodels.org にメールを送ってください。  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます）  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
OverexcLimX2:    
  description: 'Adapted from CIM data models. Field Voltage or Current overexcitation limiter designed to protect the generator field of an AC machine with automatic excitation control from overheating due to prolonged overexcitation.'    
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
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    efd1:    
      description: 'Low voltage or current point on the inverse time characteristic (EFD).  Typical Value = 1.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    efd2:    
      description: 'Mid voltage or current point on the inverse time characteristic (EFD).  Typical Value = 1.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    efd3:    
      description: 'High voltage or current point on the inverse time characteristic (EFD).  Typical Value = 1.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    efddes:    
      description: 'Desired field voltage if m=F or field current if m=T (EFD).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    efdrated:    
      description: 'Rated field voltage if m=F or field current if m=T (EFD).  Typical Value = 1.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &overexclimx2_-_properties_-_owner_-_items_-_anyof    
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
    kmx:    
      description: 'Gain (K).  Typical Value = 0.002. Default: 0.0'    
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
      description: '(m). true = IFD limiting false = EFD limiting. Default: False'    
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
        anyOf: *overexclimx2_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Time to trip the exciter at the low voltage or current point on the inverse time characteristic (TIME).  Typical Value = 120. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t2:    
      description: 'Time to trip the exciter at the mid voltage or current point on the inverse time characteristic (TIME).  Typical Value = 40. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t3:    
      description: 'Time to trip the exciter at the high voltage or current point on the inverse time characteristic (TIME).  Typical Value = 15. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be OverexcLimX2'    
      enum:    
        - OverexcLimX2    
      type: string    
      x-ngsi:    
        type: Property    
    vlow:    
      description: 'Low voltage limit (V) (>0). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/OverexcLimX2/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/OverexcLimX2/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## ペイロードの例  
JSON-LD形式のOverexcLimX2の例をkey-valuesとして利用できません。これは、`options=keyValues`を使用した場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
正規化されたJSON-LD形式のOverexcLimX2の例はありません。オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
JSON-LD形式のOverexcLimX2の例をkey-valuesとして利用できません。これは`options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
正規化されたJSON-LD形式のOverexcLimX2の例はありません。オプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。