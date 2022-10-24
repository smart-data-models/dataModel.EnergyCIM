<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティGovCT2  
============<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovCT2/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述。**CIMデータモデルから引用。周波数依存の燃料流量制限を持つ一般的なガバナモデル。  GovCT1model を、特定のガスタービンメーカーの周波数依存の燃料流量制限を表現するために改良したモデルです**。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別称  - `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `aset[number]`: 加速度リミッタ設定値（Aset）。  単位＝PU/sec.  典型的な値 = 10.デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `db[number]`: スピードガバナーのデッドバンドを単位速度あたりで表した値（db）。  大半のアプリケーションでは、この値をゼロに設定することが推奨されます。  代表値＝0 デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: このアイテムの説明  - `dm[number]`: 速度感度係数（Dm）。  Dmは，軸回転数に対するエンジン出力の変化，または軸回転数に対する最大出力能力の変化のいずれかを表すことができる。  Dmが正の場合は、速度が上昇するにつれてエンジン速度対出力特性の勾配が下がることを表します。レシプロエンジンや一部の航空転用型タービンでは、わずかに下降する特性が一般的である。  負の場合は、エンジン出力は軸回転数の影響を受けないが、最大許容燃料流量は軸回転数の低下とともに減少すると仮定する。これは、排気温度制限のため、1軸の産業用タービンに特徴的である。  典型的な値＝0 デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `flim1[number]`: 周波数閾値1 (Flim1)。  単位＝Hz。  典型的な値＝59。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `flim10[number]`: 周波数閾値10（Flim10）。  単位：Hz。  典型的な値 = 0. デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `flim2[number]`: 周波数閾値2 (Flim2)。  単位：Hz。  典型的な値 = 0. デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `flim3[number]`: 周波数閾値3 (Flim3)。  単位：Hz。  典型的な値 = 0. デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `flim4[number]`: 周波数閾値4 (Flim4)。  単位：Hz。  典型的な値 = 0. デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `flim5[number]`: 周波数閾値5 (Flim5)。  単位：Hz。  典型的な値 = 0. デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `flim6[number]`: 周波数閾値6 (Flim6)。  単位：Hz。  典型的な値 = 0. デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `flim7[number]`: 周波数閾値7 (Flim7)。  単位：Hz。  典型的な値 = 0. デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `flim8[number]`: 周波数閾値8 (Flim8)。  単位：Hz。  典型的な値 = 0. デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `flim9[number]`: 周波数閾値9 (Flim9)。  単位：Hz。  典型的な値 = 0. デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: エンティティの一意な識別子  - `ka[number]`: 加速度リミッタのゲイン（Ka）。  典型的な値 = 10.デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kdgov[number]`: ガバナー微分ゲイン（Kdgov）。  代表値＝0 デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kigov[number]`: ガバナー積分ゲイン（Kigov）。  代表値 = 0.45.デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kiload[number]`: PIコントローラ（Kiload）用ロードリミッタ積分ゲインです。  代表的な値＝1。初期値：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kimw[number]`: パワーコントローラ（リセット）ゲイン（Kimw）。  デフォルト値の0.01は、リセット時間100秒に対応する。  0.001の値は、比較的遅い動作の負荷コントローラに対応する。  代表値＝0 デフォルト値：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kpgov[number]`: ガバナー比例ゲイン（Kpgov）。  代表値＝4。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kpload[number]`: PIコントローラのロードリミッタ比例ゲイン（Kpload）。  代表的な値＝1。初期値：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kturb[number]`: タービンゲイン (Kturb)。  典型的な値 = 1.9168.デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ldref[number]`: ロードリミッター基準値(Ldref)。  代表的な値＝1。初期値：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `maxerr[number]`: 速度誤差信号(Maxerr)の最大値。  代表的な値＝1。初期値：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `minerr[number]`: 速度誤差信号(Minerr)の最小値。  典型的な値=-1。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `mwbase[number]`: 電力値のベース（MWbase）（> 0）。  単位＝MW。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: このアイテムの名称です。  - `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリスト  - `plim1[number]`: パワーリミット1 (Plim1)。  典型的な値=0.8325。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `plim10[number]`: パワーリミット10 (Plim10)。  代表値＝0 デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `plim2[number]`: パワーリミット2 (Plim2)。  代表値＝0 デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `plim3[number]`: パワーリミット3 (Plim3)。  代表値＝0 デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `plim4[number]`: パワーリミット4 (Plim4)。  代表値＝0 デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `plim5[number]`: パワーリミット5 (Plim5)。  代表値＝0 デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `plim6[number]`: パワーリミット6 (Plim6)。  代表値＝0 デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `plim7[number]`: パワーリミット7 (Plim7)。  代表値＝0 デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `plim8[number]`: パワーリミット8 (Plim8)。  代表値＝0 デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `plim9[number]`: Power Limit 9 (Plim9)。  典型的な値= 0. デフォルト: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `prate[number]`: 周波数依存の電力制限のランプ率（Prate）。  典型的な値 = 0.017。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `r[number]`: パーマネントドループ (R)。  典型的な値 = 0.05。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rclose[number]`: 最小弁閉速度（Rclose）。  単位：PU/sec.  典型的な値 = -99.初期値：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rdown[number]`: 荷重制限減少率（Rdown）の最大値。  典型的な値=-99。初期値：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ropen[number]`: 最大バルブ開度（Ropen）。  単位＝PU/sec.  典型的な値 = 99.初期値：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rselect[number]`: ドループ用フィードバック信号(Rselect)。  典型的な値：electricalPower。デフォルトなし  . Model: [https://schema.org/Number](https://schema.org/Number)- `rup[number]`: 負荷制限の最大増加率(Rup)。  典型的な値=99。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `ta[number]`: 加速度リミッタ時定数（Ta）。  代表的な値＝1。初期値：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tact[number]`: アクチュエータ時定数 (タクト)。  典型的な値 = 0.4。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tb[number]`: タービン・ラグ時定数（Tb）。  典型的な値 = 0.1.デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tc[number]`: タービンリードタイム定数(Tc)。  代表値 = 0. デフォルト: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tdgov[number]`: ガバナー微分コントローラの時定数（Tdgov）。  代表値 = 1.デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `teng[number]`: ディーゼルエンジンの輸送時間遅れは、燃料流量設定の変更とトルク（Teng）の発現の間にわずかではあるが測定可能な輸送遅れがあるディーゼルエンジンを表現するために使用される。  この輸送遅延が特に問題となる特殊なケースを除き、Tengはゼロであるべきである。  典型的な値=0 デフォルト: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tfload[number]`: ロードリミッター時定数（Tfload）。  代表的な値＝3。初期値：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tpelec[number]`: 電力変換器の時定数 (Tpelec)。  典型的な値 = 2.5。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tsa[number]`: 温度検出リード時定数（Tsa）。  代表値＝0 デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tsb[number]`: 温度検出遅れ時間定数（Tsb）。  代表値＝50。初期値：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSIタイプ。GovCT2である必要があります。  - `vmax[number]`: バルブ位置の最大リミット値(Vmax)。  典型的な値=1。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vmin[number]`: バルブ位置の下限値（Vmin）。  代表値＝0.175。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `wfnl[number]`: 無負荷時燃料流量（Wfnl）。  典型的な値=0.187。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `wfspd[number]`: 燃料源特性のスイッチで、与えられた燃料バルブストロークに対する燃料流量がエンジン速度（Wfspd）に比例し得ることを認識する。 true = 燃料流量が速度に比例する（ポジティブディスプレイスメント燃料インジェクタを備えた一部のガスタービンおよびディーゼルエンジン用） false = 燃料制御システムが燃料流量をエンジン速度から独立させる。典型的な値=false。デフォルトFalse  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
<!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
CIMデータモデルとCIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy)から引用。このデータモデルは、IEC61970規格で規定されたCommon Information Model (CIM)をスマートデータモデルに直接変換したものです。このモデルのベースとなっているpythonクラスは、これらのエンティティInstitute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) and RWTH University Aachen, Germanyによって開発されたものである。一部のプロパティは間違ったタイプを持つことがあります。このような場合は、問題を提起するか、info@smartdatamodels.org にメールを送ってください。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GovCT2:    
  description: 'Adapted from CIM data models. General governor model with frequency-dependent fuel flow limit.  This model is a modification of the GovCT1model in order to represent the frequency-dependent fuel flow limit of a specific gas turbine manufacturer.'    
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
    aset:    
      description: 'Acceleration limiter setpoint (Aset).  Unit = PU/sec.  Typical Value = 10. Default: 0.0'    
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
    db:    
      description: 'Speed governor dead band in per unit speed (db).  In the majority of applications, it is recommended that this value be set to zero.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    dm:    
      description: 'Speed sensitivity coefficient (Dm).  Dm can represent either the variation of the engine power with the shaft speed or the variation of maximum power capability with shaft speed.  If it is positive it describes the falling slope of the engine speed verses power characteristic as speed increases. A slightly falling characteristic is typical for reciprocating engines and some aero-derivative turbines.  If it is negative the engine power is assumed to be unaffected by the shaft speed, but the maximum permissible fuel flow is taken to fall with falling shaft speed. This is characteristic of single-shaft industrial turbines due to exhaust temperature limits.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    flim1:    
      description: 'Frequency threshold 1 (Flim1).  Unit = Hz.  Typical Value = 59. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    flim10:    
      description: 'Frequency threshold 10 (Flim10).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    flim2:    
      description: 'Frequency threshold 2 (Flim2).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    flim3:    
      description: 'Frequency threshold 3 (Flim3).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    flim4:    
      description: 'Frequency threshold 4 (Flim4).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    flim5:    
      description: 'Frequency threshold 5 (Flim5).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    flim6:    
      description: 'Frequency threshold 6 (Flim6).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    flim7:    
      description: 'Frequency threshold 7 (Flim7).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    flim8:    
      description: 'Frequency threshold 8 (Flim8).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    flim9:    
      description: 'Frequency threshold 9 (Flim9).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &govct2_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Acceleration limiter Gain (Ka).  Typical Value = 10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kdgov:    
      description: 'Governor derivative gain (Kdgov).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kigov:    
      description: 'Governor integral gain (Kigov).  Typical Value = 0.45. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kiload:    
      description: 'Load limiter integral gain for PI controller (Kiload).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kimw:    
      description: 'Power controller (reset) gain (Kimw).  The default value of 0.01 corresponds to a reset time of 100 seconds.  A value of 0.001 corresponds to a relatively slow acting load controller.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kpgov:    
      description: 'Governor proportional gain (Kpgov).  Typical Value = 4. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kpload:    
      description: 'Load limiter proportional gain for PI controller (Kpload).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kturb:    
      description: 'Turbine gain (Kturb).  Typical Value = 1.9168. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ldref:    
      description: 'Load limiter reference value (Ldref).  Typical Value = 1. Default: 0.0'    
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
    maxerr:    
      description: 'Maximum value for speed error signal (Maxerr).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    minerr:    
      description: 'Minimum value for speed error signal (Minerr).  Typical Value = -1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    mwbase:    
      description: 'Base for power values (MWbase) (> 0).  Unit = MW. Default: 0.0'    
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
        anyOf: *govct2_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    plim1:    
      description: 'Power limit 1 (Plim1).  Typical Value = 0.8325. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    plim10:    
      description: 'Power limit 10 (Plim10).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    plim2:    
      description: 'Power limit 2 (Plim2).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    plim3:    
      description: 'Power limit 3 (Plim3).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    plim4:    
      description: 'Power limit 4 (Plim4).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    plim5:    
      description: 'Power limit 5 (Plim5).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    plim6:    
      description: 'Power limit 6 (Plim6).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    plim7:    
      description: 'Power limit 7 (Plim7).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    plim8:    
      description: 'Power limit 8 (Plim8).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    plim9:    
      description: 'Power Limit 9 (Plim9).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    prate:    
      description: 'Ramp rate for frequency-dependent power limit (Prate).  Typical Value = 0.017. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    r:    
      description: 'Permanent droop (R).  Typical Value = 0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rclose:    
      description: 'Minimum valve closing rate (Rclose).  Unit = PU/sec.  Typical Value = -99. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rdown:    
      description: 'Maximum rate of load limit decrease (Rdown).  Typical Value = -99. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ropen:    
      description: 'Maximum valve opening rate (Ropen).  Unit = PU/sec.  Typical Value = 99. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rselect:    
      description: 'Feedback signal for droop (Rselect).  Typical Value = electricalPower. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rup:    
      description: 'Maximum rate of load limit increase (Rup).  Typical Value = 99. Default: 0.0'    
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
      description: 'Acceleration limiter time constant (Ta).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tact:    
      description: 'Actuator time constant (Tact).  Typical Value = 0.4. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tb:    
      description: 'Turbine lag time constant (Tb).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tc:    
      description: 'Turbine lead time constant (Tc).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tdgov:    
      description: 'Governor derivative controller time constant (Tdgov).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    teng:    
      description: 'Transport time delay for diesel engine used in representing diesel engines where there is a small but measurable transport delay between a change in fuel flow setting and the development of torque (Teng).  Teng should be zero in all but special cases where this transport delay is of particular concern.  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tfload:    
      description: 'Load Limiter time constant (Tfload).  Typical Value = 3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tpelec:    
      description: 'Electrical power transducer time constant (Tpelec).  Typical Value = 2.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tsa:    
      description: 'Temperature detection lead time constant (Tsa).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tsb:    
      description: 'Temperature detection lag time constant (Tsb).  Typical Value = 50. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be GovCT2'    
      enum:    
        - GovCT2    
      type: string    
      x-ngsi:    
        type: Property    
    vmax:    
      description: 'Maximum valve position limit (Vmax).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vmin:    
      description: 'Minimum valve position limit (Vmin).  Typical Value = 0.175. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    wfnl:    
      description: 'No load fuel flow (Wfnl).  Typical Value = 0.187. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    wfspd:    
      description: 'Switch for fuel source characteristic to recognize that fuel flow, for a given fuel valve stroke, can be proportional to engine speed (Wfspd). true = fuel flow proportional to speed (for some gas turbines and diesel engines with positive displacement fuel injectors) false = fuel control system keeps fuel flow independent of engine speed. Typical Value = false. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovCT2/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/GovCT2/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
GovCT2のJSON-LD形式のkey-valuesの例は利用できません。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータが返される。  
GovCT2のJSON-LD形式を正規化した例はありません。オプションを使用しない場合のNGSI-v2と互換性があり、個々のエンティティのコンテキストデータが返される。  
GovCT2のJSON-LD形式でのkey-valuesの例は利用できません。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータが返される。  
GovCT2 を JSON-LD 形式で正規化した例はありません。オプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータが返される。  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
