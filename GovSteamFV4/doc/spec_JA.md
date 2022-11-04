エンティティGovSteamFV4  
=================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovSteamFV4/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述です。**CIMデータモデルから採用。蒸気ユニットの詳細な電気油圧式ガバナー。  

## プロパティのリスト  

- `address`: 郵送先住所  - `alternateName`: このアイテムの別称  - `areaServed`: サービスや提供されるアイテムが提供される地理的なエリア  - `cpsmn`: 圧力調整器の出力の最小値（Cpsmn）。  代表値＝-1。初期値：0.0  - `cpsmx`: 圧力調整器の出力の最大値（Cpsmx）。  代表値＝1。初期値：0.0  - `crmn`: レギュレータ設定値（Crumn）の最小値。  代表値＝0、デフォルト：0.0  - `crmx`: レギュレータの設定値（Crmx）の最大値。  代表値＝1.2。デフォルト：0.0  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `description`: このアイテムの説明  - `id`: エンティティのユニークな識別子  - `kdc`: 圧力調整器の微分ゲイン（Kdc）。  代表値＝1。初期値：0.0  - `kf1`: 周波数バイアス（垂下量の逆数）（Kf1）。  代表値＝20初期値：0.0  - `kf3`: 周波数制御（垂下量の逆数）（Kf3）。  代表値＝20。初期値：0.0  - `khp`: タービンの総出力のうち、HP部の出力が占める割合（Khp）。  代表値＝0.35。初期値：0.0  - `kic`: 圧力調整器の積分ゲイン（Kic）。  代表値＝0.0033。初期値：0.0  - `kip`: 圧力フィードバック調整器の積分ゲイン（Kip）。  代表値＝0.5。初期値：0.0  - `kit`: 電子油圧式レギュレータの積分ゲイン（Kit）。  代表値＝0.04。初期値：0.0  - `kmp1`: インターセプトバルブ特性（Kmp1）の第1ゲイン係数。  代表値＝0.5初期値：0.0  - `kmp2`: インターセプトバルブ特性の第2ゲイン係数（Kmp2）。  代表値＝3.5初期値：0.0  - `kpc`: 圧力調整器の比例ゲイン（Kpc）。  代表値＝0.5。初期値：0.0  - `kpp`: 圧力フィードバック・レギュレータの比例ゲイン（Kpp）。  代表値＝1。初期値：0.0  - `kpt`: 電子油圧式レギュレータの比例ゲイン（Kpt）です。  代表値＝0.3です。初期値：0.0  - `krc`: 燃料流量（Krc）の最大変動幅。  代表値＝0.05。デフォルト：0.0  - `ksh`: ボイラー管内の流動摩擦による圧力損失（Ksh）。  代表値＝0.08。デフォルト：0.0  - `location`: アイテムへのGeojson参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygonのいずれかです。  - `lpi`: 最大負のパワーエラー（Lpi）。  代表値＝-0.15。初期値：0.0  - `lps`: 最大正のパワーエラー（Lps）。  代表値＝0.03。初期値：0.0  - `mnef`: 周波数補正（MN）の下限値です。  代表値＝-0.05。初期値：0.0  - `mxef`: 周波数補正（MX）の上限値です。  代表値＝0.05初期値：0.0  - `name`: このアイテムの名前です。  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `pr1`: 圧力設定値静的特性（Pr1）の最初の値。  代表値＝0.2。初期値：0.0  - `pr2`: Ps0 = 1.0 PU (Pr2)に対応する圧力設定点静特性の2番目の値。  代表値＝0.75。初期値：0.0  - `psmn`: 圧力設定点静特性（Psmn）の最小値。  代表値＝1。初期値：0.0  - `rsmimn`: 積分レギュレータの最小値（Rsmimn）。  代表値＝0、初期値＝0.0  - `rsmimx`: 整流器の最大値（Rsmimx）。  代表値＝1.1。初期値：0.0  - `rvgmn`: 積分レギュレーターの最小値（Rvgmn）。  代表値＝0、初期値＝0.0  - `rvgmx`: インテグラルレギュレーター（Rvgmx）の最大値です。  代表値＝1.2。初期値：0.0  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `srmn`: 最小バルブ開度（Srmn）。  代表値＝0、初期値＝0.0  - `srmx`: 最大バルブ開度（Srmx）。  代表値＝1.1。デフォルト：0.0  - `srsmp`: インターセプトバルブ特性不連続点（Srsmp）。  代表値＝0.43。デフォルト：0.0  - `svmn`: レギュレーターの最大ゲート閉鎖速度（Svmn）。  代表値＝-0.0333。初期値：0.0  - `svmx`: レギュレーターの最大ゲート開速度（Svmx）。  代表値＝0.0333。デフォルト：0.0  - `ta`: コントロールバルブのレート開放時間（Ta）。  代表値＝0.8。デフォルト：0  - `tam`: インターセプトバルブのレートオープン時間（Tam）。  代表値＝0.8。デフォルト：0  - `tc`: コントロールバルブのレートクロージングタイム（Tc）。  代表値＝0.5。デフォルト：0  - `tcm`: インターセプトバルブレートの閉鎖時間（Tcm）。  代表値＝0.5。デフォルト：0  - `tdc`: 圧力調整器の微分時定数（Tdc）。  代表値＝90デフォルト：0  - `tf1`: 燃料調整の時定数（Tf1）。  代表値＝10。デフォルト：0  - `tf2`: スチームチェストの時定数（Tf2）。  代表値＝10。デフォルト：0  - `thp`: タービンの高圧（HP）時定数（Thp）。  代表値＝0.15。デフォルト：0  - `tmp`: タービンの低圧（LP）時定数（Tmp）。  代表値＝0.4。デフォルト：0  - `trh`: タービンの再熱時定数（Trh）。  代表値＝10。デフォルト：0  - `tv`: ボイラー時定数（Tv）。  代表値＝60。デフォルト：0  - `ty`: コントロールバルブのサーボ時定数（Ty）。  代表値＝0.1です。初期値：0  - `type`: NGSIタイプです。GovSteamFV4である必要があります。  - `y`: タービンの線形化方程式（ストドラ式）の係数（Y）。  代表値＝0.13。初期値：0.0  - `yhpmn`: コントロールバルブの最小位置（Yhpmn）。  代表値＝0.0 既定値＝0.0  - `yhpmx`: コントロールバルブの最大位置（Yhpmx）。  代表値＝1.1。初期値：0.0  - `ympmn`: インターセプトバルブの最小位置（Ympmn）。  代表値＝0.0 既定値＝0.0  - `ympmx`: インターセプトバルブの最大位置（Ympmx）。  代表値＝1.1。デフォルト：0.0    
必須項目  
CIMデータモデルとCIMpyからの採用 - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy)。このデータモデルは、IEC61970規格で規定されたCommon Information Model (CIM)をスマートデータモデルに直接変換したものです。このモデルがベースとしているpythonクラスは、Institute for Automation of Complex Power Systems (ACS)、EON Energy Research Center (EONERC)、RWTH University Aachen (ドイツ) の3団体によって開発されました。一部のプロパティのタイプが間違っている場合があります。このような場合には、問題を提起するか、info@smartdatamodels.org にメールを送ってください。  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます）  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GovSteamFV4:    
  description: 'Adapted from CIM data models. Detailed electro-hydraulic governor for steam unit.'    
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
    cpsmn:    
      description: 'Minimum value of pressure regulator output (Cpsmn).  Typical Value = -1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    cpsmx:    
      description: 'Maximum value of pressure regulator output (Cpsmx).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    crmn:    
      description: 'Minimum value of regulator set-point (Crmn).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    crmx:    
      description: 'Maximum value of regulator set-point (Crmx).  Typical Value = 1.2. Default: 0.0'    
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
    id:    
      anyOf: &govsteamfv4_-_properties_-_owner_-_items_-_anyof    
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
    kdc:    
      description: 'Derivative gain of pressure regulator (Kdc).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kf1:    
      description: 'Frequency bias (reciprocal of droop) (Kf1).  Typical Value = 20. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kf3:    
      description: 'Frequency control (reciprocal of droop) (Kf3).  Typical Value = 20. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    khp:    
      description: 'Fraction  of total turbine output generated by HP part (Khp).  Typical Value = 0.35. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kic:    
      description: 'Integral gain of pressure regulator (Kic).  Typical Value = 0.0033. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kip:    
      description: 'Integral gain of pressure feedback regulator (Kip).  Typical Value = 0.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kit:    
      description: 'Integral gain of electro-hydraulic regulator (Kit).  Typical Value = 0.04. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kmp1:    
      description: 'First gain coefficient of  intercept valves characteristic (Kmp1).  Typical Value = 0.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kmp2:    
      description: 'Second gain coefficient of intercept valves characteristic (Kmp2).  Typical Value = 3.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kpc:    
      description: 'Proportional gain of pressure regulator (Kpc).  Typical Value = 0.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kpp:    
      description: 'Proportional gain of pressure feedback regulator (Kpp).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kpt:    
      description: 'Proportional gain of electro-hydraulic regulator (Kpt).  Typical Value = 0.3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    krc:    
      description: 'Maximum variation of fuel flow (Krc).  Typical Value = 0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ksh:    
      description: 'Pressure loss due to flow friction in the boiler tubes (Ksh).  Typical Value = 0.08. Default: 0.0'    
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
    lpi:    
      description: 'Maximum negative power error (Lpi).  Typical Value = -0.15. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    lps:    
      description: 'Maximum positive power error (Lps).  Typical Value = 0.03. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    mnef:    
      description: 'Lower limit for frequency correction (MN).  Typical Value = -0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    mxef:    
      description: 'Upper limit for frequency correction (MX).  Typical Value = 0.05. Default: 0.0'    
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
        anyOf: *govsteamfv4_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    pr1:    
      description: 'First value of pressure set point static characteristic (Pr1).  Typical Value = 0.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pr2:    
      description: 'Second value of pressure set point static characteristic, corresponding to Ps0 = 1.0 PU (Pr2).  Typical Value = 0.75. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    psmn:    
      description: 'Minimum value of pressure set point static characteristic (Psmn).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rsmimn:    
      description: 'Minimum value of integral regulator (Rsmimn).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rsmimx:    
      description: 'Maximum value of integral regulator (Rsmimx).  Typical Value = 1.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rvgmn:    
      description: 'Minimum value of integral regulator (Rvgmn).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rvgmx:    
      description: 'Maximum value of integral regulator (Rvgmx).  Typical Value = 1.2. Default: 0.0'    
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
    srmn:    
      description: 'Minimum valve opening (Srmn).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    srmx:    
      description: 'Maximum valve opening (Srmx).  Typical Value = 1.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    srsmp:    
      description: 'Intercept valves characteristic discontinuity point (Srsmp).  Typical Value = 0.43. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    svmn:    
      description: 'Maximum regulator gate closing velocity (Svmn).  Typical Value = -0.0333. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    svmx:    
      description: 'Maximum regulator gate opening velocity (Svmx).  Typical Value = 0.0333. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ta:    
      description: 'Control valves rate opening time (Ta).  Typical Value = 0.8. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tam:    
      description: 'Intercept valves rate opening time (Tam).  Typical Value = 0.8. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tc:    
      description: 'Control valves rate closing time (Tc).  Typical Value = 0.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tcm:    
      description: 'Intercept valves rate closing time (Tcm).  Typical Value = 0.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tdc:    
      description: 'Derivative time constant of pressure regulator (Tdc).  Typical Value = 90. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tf1:    
      description: 'Time constant of fuel regulation (Tf1).  Typical Value = 10. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tf2:    
      description: 'Time constant of steam chest (Tf2).  Typical Value = 10. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    thp:    
      description: 'High pressure (HP) time constant of the turbine (Thp).  Typical Value = 0.15. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tmp:    
      description: 'Low pressure (LP) time constant of the turbine (Tmp).  Typical Value = 0.4. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    trh:    
      description: 'Reheater  time constant of the turbine (Trh).  Typical Value = 10. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tv:    
      description: 'Boiler time constant (Tv).  Typical Value = 60. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ty:    
      description: 'Control valves servo time constant (Ty).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be GovSteamFV4'    
      enum:    
        - GovSteamFV4    
      type: string    
      x-ngsi:    
        type: Property    
    y:    
      description: 'Coefficient of linearized equations of turbine (Stodola formulation) (Y).  Typical Value = 0.13. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    yhpmn:    
      description: 'Minimum control valve position (Yhpmn).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    yhpmx:    
      description: 'Maximum control valve position (Yhpmx).  Typical Value = 1.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ympmn:    
      description: 'Minimum intercept valve position (Ympmn).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ympmx:    
      description: 'Maximum intercept valve position (Ympmx).  Typical Value = 1.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovSteamFV4/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/GovSteamFV4/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## ペイロードの例  
JSON-LD形式のGovSteamFV4の例をkey-valuesとして利用できません。これは、`options=keyValues`を使用した場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
GovSteamFV4をJSON-LD形式で正規化した例はありません。オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
JSON-LD形式のGovSteamFV4の例をkey-valuesとして利用できません。これは、`options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
GovSteamFV4をJSON-LD形式で正規化した例はありません。オプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。