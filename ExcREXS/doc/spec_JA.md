<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティExcREXS  
=============<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExcREXS/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述。**CIMデータモデルから引用。汎用回転励磁システムモデル。  このモデルは、直流電源がACまたはDC発電機である広範囲の励磁システムを表現するために使用することができる。IEEEタイプAC1、AC2、DC1、DC2励磁システムモデルを包含している。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別称  - `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `e1[number]`: フィールド電圧値1(E1)。  典型的な値=3。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `e2[number]`: フィールド電圧値2(E2)。  典型的な値=4。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fbf[number]`: レートフィードバック信号フラグ(Fbf)。典型的な値 = fieldCurrent。デフォルト。なし  . Model: [https://schema.org/Number](https://schema.org/Number)- `flimf[number]`: リミットタイプフラグ(Flimf)。  代表値＝0 デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: エンティティの一意な識別子  - `kc[number]`: 整流器レギュレーションファクター (Kc)。  典型的な値=0.05。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kd[number]`: 励磁制御係数(Kd)。  典型的な値 = 2.デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ke[number]`: 励磁磁界比例定数（Ke）。  典型的な値 = 1.デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kefd[number]`: フィールド電圧フィードバックゲイン (Kefd)。  典型的な値 = 0. デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kf[number]`: レートフィードバックゲイン(Kf)。  典型的な値 = 0.05.デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kh[number]`: フィールド電圧コントローラフィードバックゲイン（Kh）。  典型的な値 = 0. デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kii[number]`: フィールド電流レギュレータ積分ゲイン (Kii)。  代表値=0.デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kip[number]`: フィールドカレントレギュレータの比例ゲイン (Kip)。  典型的な値 = 1.デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ks[number]`: モデル速度係数(Ks)の使い分けを可能にする係数。  代表的な値＝0 デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kvi[number]`: 電圧レギュレータ積分ゲイン (Kvi)。  代表値 = 0. デフォルト値: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kvp[number]`: 電圧レギュレータの比例ゲイン (Kvp)。  典型的な値 = 2800.デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kvphz[number]`: V/Hzリミッターのゲイン（Kvphz）。  代表値＝0 デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `name[string]`: このアイテムの名称です。  - `nvphz[number]`: V/Hzリミッタのピックアップ速度(Nvphz)。  代表値＝0 デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリスト  - `se1[number]`: E1(Se1)での飽和係数。  典型的な値=0.0001。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `se2[number]`: E2(Se2)における飽和係数。  典型的な値=0.001。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `ta[number]`: ボルテージレギュレータの時定数（Ta）。  代表値＝0.01。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tb1[number]`: ラグ時定数 (Tb1)。  代表値＝0 デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tb2[number]`: ラグ時定数 (Tb2)。  代表値＝0 デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tc1[number]`: リードタイム定数 (Tc1)。  代表値＝0 デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tc2[number]`: リードタイム定数 (Tc2)。  代表値＝0 デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `te[number]`: エキサイターフィールド時定数 (Te)。  典型的な値 = 1.2。デフォルト: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tf[number]`: レートフィードバック時定数（Tf）。  典型的な値 = 1.デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tf1[number]`: フィードバックリードタイム定数 (Tf1)。  代表値 = 0. デフォルト: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tf2[number]`: フィードバックラグ時定数（Tf2）。  代表値＝0 デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tp[number]`: フィールド電流ブリッジ時定数(Tp)。  代表値＝0 デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSIタイプ。ExcREXSでなければならない  - `vcmax[number]`: 最大化合物電圧 (Vcmax)。  代表値＝0 デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vfmax[number]`: 最大励磁電流(Vfmax)。  典型的な値 = 47.デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vfmin[number]`: 最小励磁電流(Vfmin)。  典型的な値 = -20。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vimax[number]`: 電圧レギュレータ入力制限（Vimax）。  典型的な値= 0.1。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vrmax[number]`: コントローラ最大出力（Vrmax）。  典型的な値 = 47.デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vrmin[number]`: コントローラ出力の最小値（Vrmin）。  典型的な値=-20。初期値：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `xc[number]`: エキサイタ複合リアクタンス (Xc)。  代表値＝0 デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
<!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
CIMデータモデルとCIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy) から引用した。このデータモデルは、IEC61970規格で規定されたCommon Information Model (CIM)をスマートデータモデルに直接変換したものです。このモデルのベースとなっているpythonクラスは、これらのエンティティInstitute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) and RWTH University Aachen, Germanyによって開発されたものである。一部のプロパティが間違ったタイプを持つことがあります。このような場合は、問題を提起するか、info@smartdatamodels.org にメールを送ってください。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ExcREXS:    
  description: 'Adapted from CIM data models. General Purpose Rotating Excitation System Model.  This model can be used to represent a wide range of excitation systems whose DC power source is an AC or DC generator. It encompasses IEEE type AC1, AC2, DC1, and DC2 excitation system models.'    
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
    e1:    
      description: 'Field voltage value 1 (E1).  Typical Value = 3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    e2:    
      description: 'Field voltage value 2 (E2).  Typical Value = 4. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fbf:    
      description: 'Rate feedback signal flag (Fbf). Typical Value = fieldCurrent. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    flimf:    
      description: 'Limit type flag (Flimf).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &excrexs_-_properties_-_owner_-_items_-_anyof    
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
    kc:    
      description: 'Rectifier regulation factor (Kc).  Typical Value = 0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kd:    
      description: 'Exciter regulation factor (Kd).  Typical Value = 2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ke:    
      description: 'Exciter field proportional constant (Ke).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kefd:    
      description: 'Field voltage feedback gain (Kefd).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kf:    
      description: 'Rate feedback gain (Kf).  Typical Value = 0.05. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kh:    
      description: 'Field voltage controller feedback gain (Kh).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kii:    
      description: 'Field Current Regulator Integral Gain (Kii).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kip:    
      description: 'Field Current Regulator Proportional Gain (Kip).  Typical Value = 1. Default: 0.0'    
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
    kvi:    
      description: 'Voltage Regulator Integral Gain (Kvi).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kvp:    
      description: 'Voltage Regulator Proportional Gain (Kvp).  Typical Value = 2800. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kvphz:    
      description: 'V/Hz limiter gain (Kvphz).  Typical Value = 0. Default: 0.0'    
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
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    nvphz:    
      description: 'Pickup speed of V/Hz limiter (Nvphz).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *excrexs_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    se1:    
      description: 'Saturation factor at E1 (Se1).  Typical Value = 0.0001. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    se2:    
      description: 'Saturation factor at E2 (Se2).  Typical Value = 0.001. Default: 0.0'    
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
    ta:    
      description: 'Voltage Regulator time constant (Ta).  Typical Value = 0.01. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tb1:    
      description: 'Lag time constant (Tb1).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tb2:    
      description: 'Lag time constant (Tb2).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tc1:    
      description: 'Lead time constant (Tc1).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tc2:    
      description: 'Lead time constant (Tc2).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    te:    
      description: 'Exciter field time constant (Te).  Typical Value = 1.2. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tf:    
      description: 'Rate feedback time constant (Tf).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tf1:    
      description: 'Feedback lead time constant (Tf1).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tf2:    
      description: 'Feedback lag time constant (Tf2).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tp:    
      description: 'Field current Bridge time constant (Tp).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be ExcREXS'    
      enum:    
        - ExcREXS    
      type: string    
      x-ngsi:    
        type: Property    
    vcmax:    
      description: 'Maximum compounding voltage (Vcmax).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vfmax:    
      description: 'Maximum Exciter Field Current (Vfmax).  Typical Value = 47. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vfmin:    
      description: 'Minimum Exciter Field Current (Vfmin).  Typical Value = -20. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vimax:    
      description: 'Voltage Regulator Input Limit (Vimax).  Typical Value = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vrmax:    
      description: 'Maximum controller output (Vrmax).  Typical Value = 47. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vrmin:    
      description: 'Minimum controller output (Vrmin).  Typical Value = -20. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    xc:    
      description: 'Exciter compounding reactance (Xc).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcREXS/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/ExcREXS/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
JSON-LD形式のExcREXSをkey-valueとする例は利用できない。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータが返される。  
ExcREXS を JSON-LD 形式で正規化した例は利用不可。これはオプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
JSON-LD形式のExcREXSをkey-valuesとする例は利用できません。これは `options=keyValues` を使用した場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータが返される。  
ExcREXS を JSON-LD 形式で正規化した例は存在しない。これはオプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
