<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティExcDC3A  
=============<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExcDC3A/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述：**CIM データモデルからの引用。IEEE DC3A 直流整流子励磁機の速度入力、デスバンドを変更したもの。  DC旧タイプ4.**。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。    
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `edfmax[number]`: 最大電圧エキサイタ出力リミッタ（Efdmax）。  代表値=99。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `efd1[number]`: エキサイタ飽和電圧（Efd1）。  代表値 = 2.6。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `efd2[number]`: エキサイタ飽和電圧（Efd2）。  代表値 = 3.45。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `efdlim[number]`: (Efdlim)。true = エキサイタ出力リミッタが有効 false = エキサイタ出力リミッタが無効。代表値 = true。デフォルト：偽  . Model: [https://schema.org/Number](https://schema.org/Number)- `efdmin[number]`: 最低電圧エキサイタ出力リミッタ（Efdmin）。  代表値 = -99。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `exclim[number]`: (exclim)。  IEEE規格は、励磁出力の下限について曖昧である。true = 積分器出力にゼロの下限が適用される false = 積分器出力にゼロの下限が適用されない。代表値 = true。デフォルト：偽  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: エンティティの一意識別子  - `ke[number]`: 自励磁界に関連する励磁定数（Ke）。  代表値 = 1。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kr[number]`: デスバンド（Kr）。  Krがゼロでない場合、IEEE(1968)Type4モデルのようにVerr > KrまたはVerr < -Krであれば、電圧レギュレータ入力は一定の割合で変化する。Krがゼロの場合、IEEE (1980) DC3およびIEEE (1992, 2005) DC3Aモデルに従い、エラー信号が電圧レギュレータを連続的に駆動する。  代表値 = 0. デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ks[number]`: モデル速度係数（Ks）の使い分けを可能にする係数。  代表値 = 0 デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kv[number]`: 高速昇降接点設定（Kv）。  代表値 = 0.05。デフォルト：0.0。  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `seefd1[number]`: 対応するエキサイタ電圧Efd1におけるエキサイタ飽和関数値（Se[Eefd1]）。  代表値 = 0.1。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seefd2[number]`: 対応するエキサイタ電圧Efd2におけるエキサイタ飽和関数値（Se[Efd2]）。  代表値 = 0.35。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `te[number]`: エキサイタ時定数、エキサイタ制御（Te）に関連する積分レート。  代表値 = 1.83。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `trh[number]`: レオスタット移動時間（Trh）。  代表値 = 20。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSIタイプ。ExcDC3Aでなければならない。  - `vrmax[number]`: 最大電圧レギュレータ出力 (Vrmax).  代表値 = 5。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vrmin[number]`: 電圧レギュレータ出力の最小値（Vrmin）。  代表値=0 デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
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
ExcDC3A:    
  description: 'Adapted from CIM data models. This is modified IEEE DC3A direct current commutator exciters with speed input, and death band.  DC old type 4.'    
  properties:    
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
    edfmax:    
      description: 'Maximum voltage exciter output limiter (Efdmax).  Typical Value = 99. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    efd1:    
      description: 'Exciter voltage at which exciter saturation is defined (Efd1).  Typical Value = 2.6. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    efd2:    
      description: 'Exciter voltage at which exciter saturation is defined (Efd2).  Typical Value = 3.45. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    efdlim:    
      description: '(Efdlim). true = exciter output limiter is active false = exciter output limiter not active. Typical Value = true. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    efdmin:    
      description: 'Minimum voltage exciter output limiter (Efdmin).  Typical Value = -99. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    exclim:    
      description: '(exclim).  IEEE standard is ambiguous about lower limit on exciter output. true = a lower limit of zero is applied to integrator output false = a lower limit of zero not applied to integrator output. Typical Value = true. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    ke:    
      description: 'Exciter constant related to self-excited field (Ke).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kr:    
      description: 'Death band (Kr).  If Kr is not zero, the voltage regulator input changes at a constant rate if Verr > Kr or Verr < -Kr as per the IEEE (1968) Type 4 model. If Kr is zero, the error signal drives the voltage regulator continuously as per the IEEE (1980) DC3 and IEEE (1992, 2005) DC3A models.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ks:    
      description: 'Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kv:    
      description: 'Fast raise/lower contact setting (Kv).  Typical Value = 0.05. Default: 0.0'    
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
    seefd1:    
      description: 'Exciter saturation function value at the corresponding exciter voltage, Efd1 (Se[Eefd1]).  Typical Value = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    seefd2:    
      description: 'Exciter saturation function value at the corresponding exciter voltage, Efd2 (Se[Efd2]).  Typical Value = 0.35. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    te:    
      description: 'Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 1.83. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    trh:    
      description: 'Rheostat travel time (Trh).  Typical Value = 20. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: NGSI type. It has to be ExcDC3A    
      enum:    
        - ExcDC3A    
      type: string    
      x-ngsi:    
        type: Property    
    vrmax:    
      description: 'Maximum voltage regulator output (Vrmax).  Typical Value = 5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vrmin:    
      description: 'Minimum voltage regulator output (Vrmin).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcDC3A/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/ExcDC3A/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
JSON-LD形式のExcDC3Aの例をkey-valuesとして利用することはできない。options=keyValues`を使用した場合はNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返す。  
正規化されたJSON-LD形式のExcDC3Aの例は利用できない。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
ExcDC3Aの例をJSON-LD形式でkey-valuesとして利用することはできない。options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。  
ExcDC3AをJSON-LD形式で正規化した例はない。オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
