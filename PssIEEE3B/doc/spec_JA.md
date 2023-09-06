<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティPssIEEE3B  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/PssIEEE3B/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述：**CIM データモデルからの引用。このクラスは、IEEE Std 421.5-2005 タイプの PSS3B 電力系統安定化モデルを表す。PSS モデル PSS3B には、電力とロータ角周波数偏差のデュアル入力があります。これらの信号は、等価機械電力信号を導出するために使用されます。  参考文献IEEE 3B 421.5-2005 8.3.** 節  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `a1[number]`: ノッチフィルターパラメーター(A1)。  代表値 = 0.359。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `a2[number]`: ノッチフィルターパラメーター(A2)。  代表値 = 0.586。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `a3[number]`: ノッチフィルターパラメーター(A3)。  代表値 = 0.429。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `a4[number]`: ノッチフィルターパラメーター(A4)。  代表値 = 0.564。デフォルト：0.0。  . Model: [https://schema.org/Number](https://schema.org/Number)- `a5[number]`: ノッチフィルターパラメーター(A5)。  代表値 = 0.001。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `a6[number]`: ノッチ・フィルター・パラメーター (A6)。  代表値 = 0 デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `a7[number]`: ノッチフィルターパラメーター(A7)。  代表値 = 0.031。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `a8[number]`: ノッチ・フィルター・パラメーター (A8)。  代表値 = 0 デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。    
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `id[*]`: エンティティの一意識別子  - `inputSignal1Type[number]`: 入力信号#1のタイプ。  代表値 = generatorElectricalPower。デフォルト：なし  . Model: [https://schema.org/Number](https://schema.org/Number)- `inputSignal2Type[number]`: 入力信号#2のタイプ。  代表値 = rotorSpeed。デフォルト：なし  . Model: [https://schema.org/Number](https://schema.org/Number)- `ks1[number]`: 信号#1のゲイン（Ks1）。  標準値：-0.602。デフォルト：0.0。  . Model: [https://schema.org/Number](https://schema.org/Number)- `ks2[number]`: 信号#2のゲイン（Ks2）。  代表値：30.12。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `t1[number]`: トランスデューサ時定数 (T1)。  代表値 = 0.012。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t2[number]`: トランスデューサ時定数 (T2)。  代表値 = 0.012。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw1[number]`: ウォッシュアウト時定数 (Tw1).  代表値 = 0.3。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw2[number]`: ウォッシュアウト時定数 (Tw2).  代表値 = 0.3。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw3[number]`: ウォッシュアウト時定数 (Tw3).  代表値 = 0.6。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSIタイプ。PssIEEE3Bでなければならない。  - `vstmax[number]`: スタビライザー出力の最大リミット値（Vstmax）。  代表値 = 0.1。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vstmin[number]`: スタビライザー出力最小リミット（Vstmin）。  代表値 = -0.1。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
<!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
CIMデータモデルとCIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy)からの引用。このデータモデルは、IEC61970標準によって規定された共通情報モデル（CIM）をスマートデータモデルに直接変換したものです。このモデルに基づくPythonクラスは、Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) and RWTH University Aachen, Germanyによって開発されました。プロパティによっては、間違ったタイプを持つことがあります。このような場合は、問題を提起するか、info@smartdatamodels.org までメールをお送りください。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PssIEEE3B:    
  description: 'Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type PSS3B power system stabilizer model. The PSS model PSS3B has dual inputs of electrical power and rotor angular frequency deviation. The signals are used to derive an equivalent mechanical power signal.  Reference: IEEE 3B 421.5-2005 Section 8.3.'    
  properties:    
    a1:    
      description: 'Notch filter parameter (A1).  Typical Value = 0.359. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    a2:    
      description: 'Notch filter parameter (A2).  Typical Value = 0.586. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    a3:    
      description: 'Notch filter parameter (A3).  Typical Value = 0.429. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    a4:    
      description: 'Notch filter parameter (A4).  Typical Value = 0.564. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    a5:    
      description: 'Notch filter parameter (A5).  Typical Value = 0.001. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    a6:    
      description: 'Notch filter parameter (A6).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    a7:    
      description: 'Notch filter parameter (A7).  Typical Value = 0.031. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    a8:    
      description: 'Notch filter parameter (A8).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
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
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
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
    inputSignal1Type:    
      description: "Type of input signal #1.  Typical Value = generatorElectricalPower. Default: None"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    inputSignal2Type:    
      description: "Type of input signal #2.  Typical Value = rotorSpeed. Default: None"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ks1:    
      description: "Gain on signal # 1 (Ks1).  Typical Value = -0.602. Default: 0.0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ks2:    
      description: "Gain on signal # 2 (Ks2).  Typical Value = 30.12. Default: 0.0"    
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
    t1:    
      description: 'Transducer time constant (T1).  Typical Value = 0.012. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t2:    
      description: 'Transducer time constant (T2).  Typical Value = 0.012. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tw1:    
      description: 'Washout time constant (Tw1).  Typical Value = 0.3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tw2:    
      description: 'Washout time constant (Tw2).  Typical Value = 0.3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tw3:    
      description: 'Washout time constant (Tw3).  Typical Value = 0.6. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: NGSI type. It has to be PssIEEE3B    
      enum:    
        - PssIEEE3B    
      type: string    
      x-ngsi:    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PssIEEE3B/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/PssIEEE3B/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
JSON-LD フォーマットの PssIEEE3B のキー値の例は利用できない。これは NGSI-v2 と互換性があり、`options=keyValues` を使用すると個々のエンティティのコンテキストデータを返す。  
正規化された JSON-LD 形式の PssIEEE3B の例は利用できない。これは、オプションを使用しない場合、NGSI-v2 と互換性があり、個々のエンティティのコンテキストデータを返す。  
JSON-LD フォーマットの PssIEEE3B のキー値の例は利用できない。これは、`options=keyValues` を使用した場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータを返す。  
正規化された JSON-LD 形式の PssIEEE3B の例は利用できません。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
