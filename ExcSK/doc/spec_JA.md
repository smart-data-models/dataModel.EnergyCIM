<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティExcSK  
===========<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExcSK/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述：**CIMデータモデルからの引用。スロバキアの励磁システムモデル。  UELおよび二次電圧制御はこのモデルに含まれる。このモデルを使用する場合、別の不足励磁リミッタまたはVAr制御器モデルを使用することはできません。  
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
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `efdmax[number]`: フィールド電圧クリッピング限界 (Efdmax)。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `efdmin[number]`: フィールド電圧クリッピング制限 (Efdmin)。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `emax[number]`: 最大フィールド電圧出力（Emax）。  代表値 = 20。デフォルト：0.0。  . Model: [https://schema.org/Number](https://schema.org/Number)- `emin[number]`: 最小フィールド電圧出力（Emin）。  代表値 = -20。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: エンティティの一意識別子  - `k[number]`: ゲイン（K）。  代表値 = 1。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `k1[number]`: 過励磁制限パラメータ(K1)。  代表値 = 0.1364。デフォルト：0.0。  . Model: [https://schema.org/Number](https://schema.org/Number)- `k2[number]`: 過励磁制限パラメータ(K2)。  代表値 = -0.3861。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kc[number]`: PIコントローラーゲイン（Kc）。  代表値 = 70。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kce[number]`: 整流器調整係数（Kce）。  代表値 = 0. デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kd[number]`: 励磁機内部リアクタンス（Kd）。  代表値 = 0 デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kgob[number]`: Pコントローラーのゲイン（Kgob）。  代表値 = 10。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kp[number]`: PIコントローラゲイン（Kp）。  代表値 = 1。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kqi[number]`: 積分成分のPIコントローラゲイン（Kqi）。  代表値＝0 デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kqob[number]`: 無効電力の上昇率（Kqob）。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kqp[number]`: PIコントローラーゲイン（Kqp）。  代表値 = 0. デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `nq[number]`: 無効電力（nq）のデッドバンド。  感度の範囲を決定する。  代表値 = 0.001。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `qconoff[number]`: 二次電圧制御状態 (Qc_on_off) true = 二次電圧制御がオン false = 二次電圧制御がオフ。代表値 = false。デフォルト：偽  . Model: [https://schema.org/Number](https://schema.org/Number)- `qz[number]`: 無効電力の希望値（設定値），手動設定（Qz）。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `remote[number]`: true = 自動計算が有効 false = 手動設定が有効；無効電力（Qz）の希望値の使用が必要。代表値 = true。デフォルト偽  . Model: [https://schema.org/Number](https://schema.org/Number)- `sbase[number]`: ユニットの皮相電力（Sbase）。  単位はMVA。  代表値 = 259。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `tc[number]`: PIコントローラー位相リード時定数(Tc)。  代表値 = 8。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `te[number]`: ゲインブロックの時定数（Te）。  代表値 = 0.1。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti[number]`: PIコントローラー位相リード時定数（Ti）。  代表値 = 2。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tp[number]`: 時定数（Tp）。  代表値 = 0.1。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tr[number]`: 電圧変換器の時定数（Tr）。  代表値 = 0.01。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSIタイプ。ExcSKでなければならない。  - `uimax[number]`: 最大誤差（Uimax）。  代表値 = 10。デフォルト：0.0。  . Model: [https://schema.org/Number](https://schema.org/Number)- `uimin[number]`: 最小誤差（UImin）。  代表値 = -10。デフォルト：0.0。  . Model: [https://schema.org/Number](https://schema.org/Number)- `urmax[number]`: コントローラーの最大出力（URmax）。  代表値 = 10。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `urmin[number]`: コントローラ出力の最小値（URmin）。  代表値 = -10。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vtmax[number]`: 最大端子電圧入力 (Vtmax).  電圧デッドバンドの範囲を決定する。  代表値 = 1.05。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vtmin[number]`: 最低端子電圧入力（Vtmin）。  電圧デッドバンドの範囲を決定する。  代表値 = 0.95。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `yp[number]`: 最大出力（Yp）。  最小出力 = 0. 標準値 = 1.デフォルト：0.0。  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
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
ExcSK:    
  description: 'Adapted from CIM data models. Slovakian Excitation System Model.  UEL and secondary voltage control are included in this model. When this model is used, there cannot be a separate underexcitation limiter or VAr controller model.'    
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
    efdmax:    
      description: 'Field voltage clipping limit (Efdmax). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    efdmin:    
      description: 'Field voltage clipping limit (Efdmin). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    emax:    
      description: 'Maximum field voltage output (Emax).  Typical Value = 20. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    emin:    
      description: 'Minimum field voltage output (Emin).  Typical Value = -20. Default: 0.0'    
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
    k:    
      description: 'Gain (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    k1:    
      description: 'Parameter of underexcitation limit (K1).  Typical Value = 0.1364. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    k2:    
      description: 'Parameter of underexcitation limit (K2).  Typical Value = -0.3861. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kc:    
      description: 'PI controller gain (Kc).  Typical Value = 70. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kce:    
      description: 'Rectifier regulation factor (Kce).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kd:    
      description: 'Exciter internal reactance (Kd).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kgob:    
      description: 'P controller gain (Kgob).  Typical Value = 10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kp:    
      description: 'PI controller gain (Kp).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kqi:    
      description: 'PI controller gain of integral component (Kqi).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kqob:    
      description: 'Rate of rise of the reactive power (Kqob). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kqp:    
      description: 'PI controller gain (Kqp).  Typical Value = 0. Default: 0.0'    
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
    nq:    
      description: 'Dead band of reactive power (nq).  Determines the range of sensitivity.  Typical Value = 0.001. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    qconoff:    
      description: 'Secondary voltage control state (Qc_on_off). true = secondary voltage control is ON false = secondary voltage control is OFF. Typical Value = false. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    qz:    
      description: 'Desired value (setpoint) of reactive power, manual setting (Qz). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    remote:    
      description: 'Selector to apply automatic calculation in secondary controller model. true = automatic calculation is activated false = manual set is active; the use of desired value of reactive power (Qz) is required. Typical Value = true. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    sbase:    
      description: 'Apparent power of the unit (Sbase).  Unit = MVA.  Typical Value = 259. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    tc:    
      description: 'PI controller phase lead time constant (Tc).  Typical Value = 8. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    te:    
      description: 'Time constant of gain block (Te).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti:    
      description: 'PI controller phase lead time constant (Ti).  Typical Value = 2. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tp:    
      description: 'Time constant (Tp).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tr:    
      description: 'Voltage transducer time constant (Tr).  Typical Value = 0.01. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: NGSI type. It has to be ExcSK    
      enum:    
        - ExcSK    
      type: string    
      x-ngsi:    
        type: Property    
    uimax:    
      description: 'Maximum error (Uimax).  Typical Value = 10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    uimin:    
      description: 'Minimum error (UImin).  Typical Value = -10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    urmax:    
      description: 'Maximum controller output (URmax).  Typical Value = 10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    urmin:    
      description: 'Minimum controller output (URmin).  Typical Value = -10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vtmax:    
      description: 'Maximum terminal voltage input (Vtmax).  Determines the range of voltage dead band.  Typical Value = 1.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vtmin:    
      description: 'Minimum terminal voltage input (Vtmin).  Determines the range of voltage dead band.  Typical Value = 0.95. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    yp:    
      description: 'Maximum output (Yp).  Minimum output = 0.  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcSK/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/ExcSK/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
JSON-LD形式のExcSKの例をkey-valuesとして利用することはできない。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると個々のエンティティのコンテキストデータを返す。  
正規化された JSON-LD 形式の ExcSK の例は利用できない。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返す。  
ExcSKをJSON-LD形式でkey-valuesとした例は利用できない。options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。  
正規化された JSON-LD 形式の ExcSK の例は利用できない。これは、オプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
