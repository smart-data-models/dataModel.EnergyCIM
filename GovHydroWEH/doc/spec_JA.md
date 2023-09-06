<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティゴブハイドロWEH  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovHydroWEH/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述：**CIM データモデルからの引用。ウッドワード電気水力ガバナーモデル.**.  
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
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `db[number]`: 速度不感帯（db）。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: この商品の説明  - `dicn[number]`: 積分コントローラがゲートリミット（Dicn）を超えて前進することを許可する値。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dpv[number]`: パイロットバルブコントローラがゲートリミット（Dpv）を超えて前進することを許可する値。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dturb[number]`: タービンの減衰係数（Dturb）。  単位 = デルタ P (MWbase の PU) / デルタ速度(PU)。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `feedbackSignal[number]`: フィードバック信号選択(Sw) true = PID出力(R-Perm-Gate=droopかつR-Perm-Pe=0の場合) false = 電力(R-Perm-Gate=0かつR-Perm-Pe=droopの場合) またはfalse = ゲート位置(R-Perm-Gate=droopかつR-Perm-Pe=0の場合)。デフォルト：偽  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl1[number]`: フローゲート 1（Fl1）。  定常流を生成するゲート位置の関数としてタービンを通過する水流を表すルックアップテーブルのゲート位置ポイント1の流量値。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl2[number]`: フローゲート 2（Fl2）。  定常流を生成するためのゲート位置の関数としてタービンを通過する水流を表すルックアップテーブルのゲート位置ポイント2の流量値。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl3[number]`: フローゲート 3（Fl3）。  定常流を生成するためのゲート位置の関数としてタービンを通過する水流を表すルックアップテーブルのゲート位置ポイント3の流量値。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl4[number]`: フローゲート 4（Fl4）。  定常流を生成するためのゲート位置の関数としてタービンを通過する水流を表すルックアップテーブルのゲート位置ポイント4の流量値。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl5[number]`: フローゲート 5（Fl5）。  定常流を生成するためのゲート位置の関数としてタービンを通過する水流を表すルックアップテーブルのゲート位置ポイント5の流量値。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp1[number]`: フロー P1 (Fp1)。  ルックアップテーブルのポイント 1 のタービン流量値。タービン流量の関数として、機械定格 MVA の単位機械出力当たりを表す。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp10[number]`: フロー P10 (Fp10)。  機械定格 MVA の単位機械出力当たりのタービン流量をタービン流量の関数として表したルックアップテーブルのポイント 10 のタービン流量値。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp2[number]`: フロー P2 (Fp2)。  ルックアップテーブルのポイント 2 のタービン流量値。タービン流量の関数として、機械定格 MVA の単位機械出力当たりを表す。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp3[number]`: フロー P3 (Fp3)。  ルックアップテーブルのポイント 3 のタービン流量値。タービン流量の関数として、機械定格 MVA の単位機械出力当たりを表す。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp4[number]`: フロー P4 (Fp4)。  タービン流量の関数として機械定格 MVA の単位機械出力当たりを表すルックアップテーブルのポイント 4 のタービン流量値。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp5[number]`: フロー P5 (Fp5)。  機械定格 MVA の単位機械出力当たりのタービン流量をタービン流量の関数として表したルックアップテーブルのポイント 5 のタービン流量値。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp6[number]`: フロー P6 (Fp6)。  タービン流量の関数として機械定格 MVA の単位機械出力当たりを表すルックアップテーブルのポイント 6 のタービン流量値。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp7[number]`: フロー P7 (Fp7)。  機械定格 MVA の単位機械出力当たりのタービン流量をタービン流量の関数として表したルックアップテーブルのポイント 7 のタービン流量値。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp8[number]`: フロー P8 (Fp8)。  ルックアップテーブルのポイント 8 のタービン流量値。タービン流量の関数として、機械定格 MVA の単位機械出力当たりを表す。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp9[number]`: フロー P9 (Fp9)。  機械定格 MVA の単位機械出力当たりのタービン流量をタービン流量の関数として表したルックアップテーブルのポイント 9 のタービン流量値。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gmax[number]`: 最大ゲート位置（Gmax）。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gmin[number]`: 最小ゲート位置（Gmin）。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gtmxcl[number]`: 最大ゲート閉鎖率（Gtmxcl）。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gtmxop[number]`: 最大ゲート開口率（Gtmxop）。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv1[number]`: ゲート 1（Gv1）。  定常流を生成するためのゲート位置の関数としてタービンを通過する水流を表すルックアップテーブルのポイント1のゲート位置値。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv2[number]`: ゲート 2 (Gv2)。  定常流を生成するためのゲート位置の関数としてタービンを通過する水流を表すルックアップテーブルのポイント2のゲート位置値。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv3[number]`: ゲート 3 (Gv3)。  定常流を生成するためのゲート位置の関数としてタービンを通過する水流を表すルックアップテーブルのポイント3のゲート位置値。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv4[number]`: ゲート 4 (Gv4)。  定常流を生成するためのゲート位置の関数としてタービンを通過する水流を表すルックアップテーブルのポイント4のゲート位置値。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv5[number]`: ゲート 5 (Gv5)。  定常流を生成するためのゲート位置の関数としてタービンを通過する水流を表すルックアップテーブルのポイント5のゲート位置値。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: エンティティの一意識別子  - `kd[number]`: 微分コントローラの微分ゲイン（Kd）。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ki[number]`: 微分コントローラ積分ゲイン（Ki）。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kp[number]`: 微分制御ゲイン（Kp）。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `mwbase[number]`: 電力値のベース（MWbase）（>0）。  単位 = MW。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: このアイテムの名前  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `pmss1[number]`: Pmss フロー P1 (Pmss1)。  タービン流量の関数として機械定格 MVA の単位機械出力当たりを表すルックアップテーブルのタービン流量ポイント 1 の機械出力 Pmss。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss10[number]`: Pmss Flow P10 (Pmss10)。  タービン流量の関数として機械 MVA 定格の単位機械出力当たりを表すルックアップテーブルのタービン流量ポイント 10 の機械出力 Pmss。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss2[number]`: Pmss フロー P2 (Pmss2)。  タービン流量の関数として機械定格 MVA の単位機械出力当たりを表すルックアップテーブルのタービン流量ポイント 2 の機械出力 Pmss。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss3[number]`: Pmss Flow P3 (Pmss3)。  タービン流量の関数として機械 MVA 定格の単位機械出力当たりを表すルックアップテーブルのタービン流量ポイント 3 の機械出力 Pmss。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss4[number]`: Pmss フロー P4 (Pmss4)。  タービン流量の関数として機械 MVA 定格の単位機械出力当たりを表すルックアップテーブルのタービン流量ポイント 4 の機械出力 Pmss。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss5[number]`: Pmss Flow P5 (Pmss5)。  タービン流量の関数として機械 MVA 定格の単位機械出力当たりを表すルックアップテーブルのタービン流量ポイント 5 の機械出力 Pmss。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss6[number]`: Pmss Flow P6 (Pmss6)。  タービン流量の関数として機械 MVA 定格の単位機械出力当たりを表すルックアップテーブルのタービン流量ポイント 6 の機械出力 Pmss。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss7[number]`: Pmss Flow P7 (Pmss7)。  タービン流量の関数として機械定格 MVA の単位機械出力当たりを表すルックアップテーブルのタービン流量ポイント 7 の機械出力 Pmss。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss8[number]`: Pmss Flow P8 (Pmss8)。  タービン流量の関数として機械定格 MVA の単位機械出力当たりを表すルックアップテーブルのタービン流量ポイント 8 の機械出力 Pmss。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss9[number]`: Pmss フロー P9 (Pmss9).  タービン流量の関数として機械 MVA 定格の単位機械出力当たりを表すルックアップテーブルのタービン流量ポイント 9 の機械出力 Pmss。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rpg[number]`: ガバナー出力フィードバック（R-Perm-Gate）の永久ドループ。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rpp[number]`: 電力フィードバック (R-Perm-Pe) の永久ドループ。デフォルト：0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `td[number]`: 高周波ノイズ（Td）の増幅を避けるために、ブレークダウン周波数を超えて微分特性を制限するための微分コントローラ時定数。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tdv[number]`: 分配弁タイムラグ時定数（Tdv）。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tg[number]`: 分流弁コントローラがゲート移動速度制限 (Tg) を超えて前進することを許可する値。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tp[number]`: パイロットバルブのタイムラグ時定数（Tp）。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tpe[number]`: 電力垂下時定数 (Tpe)。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw[number]`: 水の慣性時定数（Tw）（>0）。デフォルト：0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSIタイプ。GovHydroWEHでなければならない。  <!-- /30-PropertiesList -->  
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
GovHydroWEH:    
  description: Adapted from CIM data models. Woodward Electric Hydro Governor Model.    
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
    db:    
      description: 'Speed Dead Band (db). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    dicn:    
      description: 'Value to allow the integral controller to advance beyond the gate limits (Dicn). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dpv:    
      description: 'Value to allow the Pilot valve controller to advance beyond the gate limits (Dpv). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dturb:    
      description: 'Turbine damping factor (Dturb).  Unit = delta P (PU of MWbase) / delta speed (PU). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    feedbackSignal:    
      description: 'Feedback signal selection (Sw). true = PID Output (if R-Perm-Gate=droop and R-Perm-Pe=0) false = Electrical Power (if R-Perm-Gate=0 and R-Perm-Pe=droop) or false = Gate Position (if R-Perm-Gate=droop and R-Perm-Pe=0). Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fl1:    
      description: 'Flow Gate 1 (Fl1).  Flow value for gate position point 1 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fl2:    
      description: 'Flow Gate 2 (Fl2).  Flow value for gate position point 2 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fl3:    
      description: 'Flow Gate 3 (Fl3).  Flow value for gate position point 3 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fl4:    
      description: 'Flow Gate 4 (Fl4).  Flow value for gate position point 4 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fl5:    
      description: 'Flow Gate 5 (Fl5).  Flow value for gate position point 5 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp1:    
      description: 'Flow P1 (Fp1).  Turbine Flow value for point 1 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp10:    
      description: 'Flow P10 (Fp10).  Turbine Flow value for point 10 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp2:    
      description: 'Flow P2 (Fp2).  Turbine Flow value for point 2 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp3:    
      description: 'Flow P3 (Fp3).  Turbine Flow value for point 3 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp4:    
      description: 'Flow P4 (Fp4).  Turbine Flow value for point 4 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp5:    
      description: 'Flow P5 (Fp5).  Turbine Flow value for point 5 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp6:    
      description: 'Flow P6 (Fp6).  Turbine Flow value for point 6 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp7:    
      description: 'Flow P7 (Fp7).  Turbine Flow value for point 7 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp8:    
      description: 'Flow P8 (Fp8).  Turbine Flow value for point 8 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp9:    
      description: 'Flow P9 (Fp9).  Turbine Flow value for point 9 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gmax:    
      description: 'Maximum Gate Position (Gmax). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gmin:    
      description: 'Minimum Gate Position (Gmin). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gtmxcl:    
      description: 'Maximum gate closing rate (Gtmxcl). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gtmxop:    
      description: 'Maximum gate opening rate (Gtmxop). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv1:    
      description: 'Gate 1 (Gv1).  Gate Position value for point 1 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv2:    
      description: 'Gate 2 (Gv2).  Gate Position value for point 2 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv3:    
      description: 'Gate 3 (Gv3).  Gate Position value for point 3 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv4:    
      description: 'Gate 4 (Gv4).  Gate Position value for point 4 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv5:    
      description: 'Gate 5 (Gv5).  Gate Position value for point 5 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
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
    kd:    
      description: 'Derivative controller derivative gain (Kd). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ki:    
      description: 'Derivative controller Integral gain (Ki). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kp:    
      description: 'Derivative control gain (Kp). Default: 0.0'    
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
    mwbase:    
      description: 'Base for power values (MWbase) (>0).  Unit = MW. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
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
    pmss1:    
      description: 'Pmss Flow P1 (Pmss1).  Mechanical Power output Pmss for Turbine Flow point 1 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss10:    
      description: 'Pmss Flow P10 (Pmss10).  Mechanical Power output Pmss for Turbine Flow point 10 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss2:    
      description: 'Pmss Flow P2 (Pmss2).  Mechanical Power output Pmss for Turbine Flow point 2 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss3:    
      description: 'Pmss Flow P3 (Pmss3).  Mechanical Power output Pmss for Turbine Flow point 3 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss4:    
      description: 'Pmss Flow P4 (Pmss4).  Mechanical Power output Pmss for Turbine Flow point 4 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss5:    
      description: 'Pmss Flow P5 (Pmss5).  Mechanical Power output Pmss for Turbine Flow point 5 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss6:    
      description: 'Pmss Flow P6 (Pmss6).  Mechanical Power output Pmss for Turbine Flow point 6 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss7:    
      description: 'Pmss Flow P7 (Pmss7).  Mechanical Power output Pmss for Turbine Flow point 7 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss8:    
      description: 'Pmss Flow P8 (Pmss8).  Mechanical Power output Pmss for Turbine Flow point 8 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss9:    
      description: 'Pmss Flow P9 (Pmss9).  Mechanical Power output Pmss for Turbine Flow point 9 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rpg:    
      description: 'Permanent droop for governor output feedback (R-Perm-Gate). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rpp:    
      description: 'Permanent droop for electrical power feedback (R-Perm-Pe). Default: 0.0'    
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
    td:    
      description: 'Derivative controller time constant to limit the derivative characteristic beyond a breakdown frequency to avoid amplification of high-frequency noise (Td). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tdv:    
      description: 'Distributive Valve time lag time constant (Tdv). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tg:    
      description: 'Value to allow the Distribution valve controller to advance beyond the gate movement rate limit (Tg). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tp:    
      description: 'Pilot Valve time lag time constant (Tp). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tpe:    
      description: 'Electrical power droop time constant (Tpe). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tw:    
      description: 'Water inertia time constant (Tw) (>0). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: NGSI type. It has to be GovHydroWEH    
      enum:    
        - GovHydroWEH    
      type: string    
      x-ngsi:    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovHydroWEH/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/GovHydroWEH/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
JSON-LD形式のGovHydroWEHの例をkey-valuesとして利用することはできない。これは NGSI-v2 と互換性があり、`options=keyValues` を使用すると個々のエンティティのコンテキストデータを返す。  
正規化された JSON-LD 形式の GovHydroWEH の例は利用できない。これは、オプションを使用しない場合は NGSI-v2 と互換性があり、個々のエンティティのコンテキスト・データを返します。  
JSON-LD形式のGovHydroWEHの例をkey-valuesとして利用することはできない。これは NGSI-LD と互換性があり、`options=keyValues` を使うと個々のエンティティのコンテキストデータを返す。  
正規化された JSON-LD 形式の GovHydroWEH の例は利用できない。これは、オプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
