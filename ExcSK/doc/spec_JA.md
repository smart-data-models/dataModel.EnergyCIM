<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティExcSK  
===========<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExcSK/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述。**CIMデータモデルから引用。スロバキアの励磁システムモデル。  UELと二次電圧制御がこのモデルに含まれる。このモデルを使用する場合、別途、不足電圧リミッターやVArコントローラーのモデルを用意することはできない**。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別称  - `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `efdmax[number]`: フィールド電圧のクリッピングリミット（Efdmax）。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `efdmin[number]`: フィールド電圧のクリッピングリミット（Efdmin）。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `emax[number]`: 最大フィールド電圧出力(Emax)。  典型的な値 = 20.初期値：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `emin[number]`: フィールド電圧出力の最小値(Emin)。  典型的な値=-20。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: エンティティの一意な識別子  - `k[number]`: ゲイン(K)。  典型的な値 = 1.デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `k1[number]`: 過小励磁制限パラメータ(K1)。  代表値 = 0.1364。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `k2[number]`: 過小励磁制限パラメータ(K2)。  代表値 = -0.3861。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kc[number]`: PIコントローラーゲイン（Kc）。  典型的な値 = 70.デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kce[number]`: 整流器レギュレーションファクター（Kce）。  代表値＝0 デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kd[number]`: エキサイター内部リアクタンス (Kd)。  代表値 = 0. デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kgob[number]`: Pコントローラーのゲイン（Kgob）。  典型的な値 = 10.デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kp[number]`: PIコントローラーゲイン（Kp）。  典型的な値 = 1.デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kqi[number]`: PIコントローラの積分値のゲイン（Kqi）。  代表値＝0 デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kqob[number]`: 無効電力上昇率（Kqob）。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kqp[number]`: PIコントローラーゲイン（Kqp）。  代表値＝0 デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `name[string]`: このアイテムの名称です。  - `nq[number]`: 無効電力(nq)のデッドバンド。  感度の範囲を決定する。  典型的な値＝0.001。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリストです。  - `qconoff[number]`: 2次電圧制御状態 (Qc_on_off) true = 2次電圧制御がON false = 2次電圧制御がOFF。典型的な値 = false。デフォルトFalse  . Model: [https://schema.org/Number](https://schema.org/Number)- `qz[number]`: 無効電力の希望値（設定値），手動設定（Qz）。初期値：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `remote[number]`: True = 自動計算が有効 false = 手動設定が有効；無効電力（Qz）の希望値を使用する必要がある。典型的な値＝true。デフォルトFalse  . Model: [https://schema.org/Number](https://schema.org/Number)- `sbase[number]`: ユニットの皮相電力（Sbase）。  単位＝MVA。  典型的な値 = 259。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `tc[number]`: PIコントローラ位相リード時定数（Tc）。  典型的な値 = 8.デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `te[number]`: ゲインブロックの時定数（Te）。  代表的な値＝0.1。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti[number]`: PIコントローラ位相リード時定数（Ti）。  代表的な値＝2。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tp[number]`: 時定数(Tp)。  典型的な値 = 0.1。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tr[number]`: 電圧変換器の時定数 (Tr)。  典型的な値 = 0.01。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSIタイプであること。ExcSKでなければならない  - `uimax[number]`: 最大誤差(Uimax)。  典型的な値 = 10。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `uimin[number]`: 最小誤差(UImin)。  典型的な値=-10。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `urmax[number]`: コントローラ最大出力（URmax）。  典型的な値 = 10.デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `urmin[number]`: コントローラ出力の最小値(URmin)。  典型的な値=-10。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vtmax[number]`: 最大端子電圧入力 (Vtmax)。  電圧デッドバンドの範囲を決定する。  代表値＝1.05。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vtmin[number]`: 最小端子電圧入力（Vtmin）。  電圧デッドバンドの範囲を決定します。  代表値＝0.95。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `yp[number]`: 最大出力(Yp)。  最小出力＝0．代表値＝1．初期値：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
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
ExcSK:    
  description: 'Adapted from CIM data models. Slovakian Excitation System Model.  UEL and secondary voltage control are included in this model. When this model is used, there cannot be a separate underexcitation limiter or VAr controller model.'    
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
      anyOf: &excsk_-_properties_-_owner_-_items_-_anyof    
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
    nq:    
      description: 'Dead band of reactive power (nq).  Determines the range of sensitivity.  Typical Value = 0.001. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *excsk_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
      description: 'NGSI type. It has to be ExcSK'    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
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
JSON-LD形式のExcSKの例をkey-valuesとして利用することはできません。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータが返される。  
ExcSK を JSON-LD 形式で正規化した例は利用不可。オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返す。  
JSON-LD形式のExcSKの例をkey-valuesとして利用することはできません。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータが返される。  
ExcSK を JSON-LD 形式で正規化した例は存在しない。オプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
