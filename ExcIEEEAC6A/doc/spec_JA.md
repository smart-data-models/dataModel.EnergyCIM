<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティExcIEEEAC6A  
=================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExcIEEEAC6A/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述。**CIM データモデルから引用した。IEEE Std 421.5-2005 タイプ AC6A モデルを表すクラス。このモデルは、システムが供給する電子電圧レギュレータを備えた、フィールド制御のオルタネーター-整流器励磁システムを表している。  レギュレータの最大出力は、端子電圧の関数である。 元のモデルAC6Aに含まれていた界磁電流リミッタは、2005年の更新版でも残されている。  参考文献IEEE 規格 421.5-2005 第 6.6.** 項  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別称  - `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `id[*]`: エンティティの一意な識別子  - `ka[number]`: 電圧レギュレータのゲイン (K)。  典型的な値 = 536。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kc[number]`: 整流リアクタンス（K）に比例する整流器負荷率。典型的な値＝0.173。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kd[number]`: 消磁率。励磁機のオルタネータリアクタンス（K）の関数である。  典型的な値 = 1.91.デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ke[number]`: 自励磁界に関係する励磁定数（K）。  典型的な値 = 1.6。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kh[number]`: 励磁電流制限器利得 (K)。  典型的な値 = 92.デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `name[string]`: このアイテムの名称です。  - `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリストです。  - `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `seve1[number]`: 励磁機飽和関数値（S[V]） 励磁機電圧Vに対応し，整流リアクタンスの背面にある値。  典型的な値 = 0.214.デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seve2[number]`: 励磁機飽和関数値（S[V]） 励磁機電圧Vに対応し，整流リアクタンスの背面にある値。  典型的な値 = 0.044.デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `ta[number]`: 電圧レギュレータの時定数 (T)。  代表値 = 0.086。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tb[number]`: ボルテージレギュレータの時定数（T）。  典型的な値=9。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tc[number]`: ボルテージレギュレータの時定数（T）。  典型的な値=3。初期値：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `te[number]`: Exciter time constant, Exciter control (T) に関連する積分レート。  典型的な値 = 1.デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th[number]`: 励磁電流制限時定数（T）。  典型的な値 = 0.08。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tj[number]`: 励磁電流制限時定数（T）。  典型的な値 = 0.02。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tk[number]`: 電圧レギュレータの時定数 (T)。  代表値 = 0.18。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSIタイプ。ExcIEEEAC6A である必要があります。  - `vamax[number]`: ボルテージレギュレータ出力の最大値（V）。  代表値＝75。初期値：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vamin[number]`: ボルテージレギュレータ出力の最小値（V）。  代表値＝-75。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ve1[number]`: 飽和が定義される整流リアクタンスの裏側のエキサイターオルタネーター出力電圧（V）＝V（V）。  典型的な値 = 7.4.デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ve2[number]`: エキサイターオルタネーターの出力電圧で，飽和が定義される整流リアクタンスの背面電圧（V）。  典型的な値 = 5.55.デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vfelim[number]`: 励磁電流制限値（V）。  典型的な値 = 19.デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vhmax[number]`: 最大フィールド電流リミッタ信号の基準値（V）。  代表的な値＝75。初期値：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vrmax[number]`: ボルテージレギュレータ出力の最大値（V）。  代表値＝44。初期値：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vrmin[number]`: 電圧レギュレータ出力の最小値（V）。  代表値：-36 デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
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
ExcIEEEAC6A:    
  description: 'Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type AC6A model. The model represents field-controlled alternator-rectifier excitation systems with system-supplied electronic voltage regulators.  The maximum output of the regulator, , is a function of terminal voltage, . The field current limiter included in the original model AC6A remains in the 2005 update.  Reference: IEEE Standard 421.5-2005 Section 6.6.'    
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
    id:    
      anyOf: &excieeeac6a_-_properties_-_owner_-_items_-_anyof    
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
    ka:    
      description: 'Voltage regulator gain (K).  Typical Value = 536. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kc:    
      description: 'Rectifier loading factor proportional to commutating reactance (K). Typical Value = 0.173. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kd:    
      description: 'Demagnetizing factor, a function of exciter alternator reactances (K).  Typical Value = 1.91. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ke:    
      description: 'Exciter constant related to self-excited field (K).  Typical Value = 1.6. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kh:    
      description: 'Exciter field current limiter gain (K).  Typical Value = 92. Default: 0.0'    
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
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *excieeeac6a_-_properties_-_owner_-_items_-_anyof    
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
    seve1:    
      description: 'Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance (S[V]).  Typical Value = 0.214. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    seve2:    
      description: 'Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance (S[V]).  Typical Value = 0.044. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    ta:    
      description: 'Voltage regulator time constant (T).  Typical Value = 0.086. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tb:    
      description: 'Voltage regulator time constant (T).  Typical Value = 9. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tc:    
      description: 'Voltage regulator time constant (T).  Typical Value = 3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    te:    
      description: 'Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th:    
      description: 'Exciter field current limiter time constant (T).  Typical Value = 0.08. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tj:    
      description: 'Exciter field current limiter time constant (T).  Typical Value = 0.02. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tk:    
      description: 'Voltage regulator time constant (T).  Typical Value = 0.18. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be ExcIEEEAC6A'    
      enum:    
        - ExcIEEEAC6A    
      type: string    
      x-ngsi:    
        type: Property    
    vamax:    
      description: 'Maximum voltage regulator output (V).  Typical Value = 75. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vamin:    
      description: 'Minimum voltage regulator output (V).  Typical Value = -75. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ve1:    
      description: 'Exciter alternator output voltages back of commutating reactance at which saturation is defined (V) equals V(V).  Typical Value = 7.4. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ve2:    
      description: 'Exciter alternator output voltages back of commutating reactance at which saturation is defined (V).  Typical Value = 5.55. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vfelim:    
      description: 'Exciter field current limit reference (V).  Typical Value = 19. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vhmax:    
      description: 'Maximum field current limiter signal reference (V).  Typical Value = 75. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vrmax:    
      description: 'Maximum voltage regulator output (V).  Typical Value = 44. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vrmin:    
      description: 'Minimum voltage regulator output (V).  Typical Value = -36. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcIEEEAC6A/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/ExcIEEEAC6A/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
ExcIEEEAC6A の例を JSON-LD 形式で key-value として利用することはできません。これは、`options=keyValues`を使用した場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返す。  
ExcIEEEAC6A の例を JSON-LD 形式で正規化したものは利用できない。オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返す。  
JSON-LD形式のExcIEEEAC6Aの例をkey-valuesとして利用することはできません。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータが返される。  
ExcIEEEAC6A を正規化した JSON-LD 形式の例は利用できません。オプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
