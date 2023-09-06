<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティターミナル  
===========<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/Terminal/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述：**CIM データモデルからの引用。CIMデータモデルからの引用。端子は、接続ノードと呼ばれる物理的な接続点で接続される。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `ConductingEquipment[number]`: 端末の導電機器。  導電機器は、接続ノードまたはトポロジカルノードを介して他の導電機器端末に接続される可能性のある端末を持つ。デフォルト：なし  . Model: [https://schema.org/Number](https://schema.org/Number)- `ConnectivityNode[number]`: この接続ノードでゼロインピーダンスで相互接続されている端子。デフォルト：なし  . Model: [https://schema.org/Number](https://schema.org/Number)- `ConverterDCSides[number]`: このコンバータDC側の共通結合端子。通常、AC ネットワークに最も近い電力変圧器（またはスイッチ）の端子である。電力フローの測定は、変圧器に流入するすべてのフローの合計でなければならない。デフォルト：'list'  . Model: [https://schema.org/Number](https://schema.org/Number)- `HasFirstMutualCoupling[number]`: 最初のブランチとしてのブランチに関連する相互カップリング。デフォルト: 'list'  . Model: [https://schema.org/Number](https://schema.org/Number)- `HasSecondMutualCoupling[number]`: 関連するブランチを最初のブランチとする相互カップリング。デフォルト: 'list'  . Model: [https://schema.org/Number](https://schema.org/Number)- `RegulatingControl[number]`: この調整制御に関連する端末。  ターミナルは、トポロジカルノード（バス分岐モデルのバス）または接続性ノード（スイッチ詳細モデル）のいずれかに接続できるため、ノードの代わりにターミナルが関連付けられます。  バスバーがバス分岐モデルとスイッチ詳細モデルの両方に存在できるため、バスバーオブジェクトのターミナルで規制をモデル化することが有用な場合があります。デフォルトなし  . Model: [https://schema.org/Number](https://schema.org/Number)- `RemoteInputSignal[number]`: この端子からの入力信号。デフォルト：'list'  . Model: [https://schema.org/Number](https://schema.org/Number)- `SvPowerFlow[number]`: 端末に関連付けられたパワーフロー状態変数。デフォルト：なし  . Model: [https://schema.org/Number](https://schema.org/Number)- `TieFlow[number]`: この端末が関連付ける制御領域のタイフロー。デフォルト: 'list'  . Model: [https://schema.org/Number](https://schema.org/Number)- `TopologicalNode[number]`: トポロジカル・ノードに関連付けられた端末。   これは、接続性ノードのパスから端末への代用として使用することができるため、場合によっては接続性ノードをモデル化する必要がなくなる。   接続性ノードがモデル内にある場合、この関連付けはおそらく入力仕様として使用されないことに注意してください。デフォルトなし  . Model: [https://schema.org/Number](https://schema.org/Number)- `TransformerEnd[number]`: この端子に接続されているすべてのトランス端。デフォルト：'list'  . Model: [https://schema.org/Number](https://schema.org/Number)- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。    
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `id[*]`: エンティティの一意識別子  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `phases[number]`: 通常のネットワークの位相条件を表す。この属性がない場合、3つの位相(ABCまたはABCN)が仮定される。デフォルト：なし  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `type[string]`: NGSIタイプ。ターミナル  <!-- /30-PropertiesList -->  
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
Terminal:    
  description: Adapted from CIM data models. An AC electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called connectivity nodes.    
  properties:    
    ConductingEquipment:    
      description: 'The conducting equipment of the terminal.  Conducting equipment have  terminals that may be connected to other conducting equipment terminals via connectivity nodes or topological nodes. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ConnectivityNode:    
      description: 'Terminals interconnected with zero impedance at a this connectivity node. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ConverterDCSides:    
      description: 'Point of common coupling terminal for this converter DC side. It is typically the terminal on the power transformer (or switch) closest to the AC network. The power flow measurement must be the sum of all flows into the transformer. Default: ''list'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    HasFirstMutualCoupling:    
      description: 'Mutual couplings associated with the branch as the first branch. Default: ''list'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    HasSecondMutualCoupling:    
      description: 'Mutual couplings with the branch associated as the first branch. Default: ''list'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    RegulatingControl:    
      description: 'The terminal associated with this regulating control.  The terminal is associated instead of a node, since the terminal could connect into either a topological node (bus in bus-branch model) or a connectivity node (detailed switch model).  Sometimes it is useful to model regulation at a terminal of a bus bar object since the bus bar can be present in both a bus-branch model or a model with switch detail. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    RemoteInputSignal:    
      description: 'Input signal coming from this terminal. Default: ''list'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    SvPowerFlow:    
      description: 'The power flow state variable associated with the terminal. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    TieFlow:    
      description: 'The control area tie flows to which this terminal associates. Default: ''list'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    TopologicalNode:    
      description: 'The terminals associated with the topological node.   This can be used as an alternative to the connectivity node path to terminal, thus making it unneccesary to model connectivity nodes in some cases.   Note that if connectivity nodes are in the model, this association would probably not be used as an input specification. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    TransformerEnd:    
      description: 'All transformer ends connected at this terminal. Default: ''list'''    
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
    phases:    
      description: 'Represents the normal network phasing condition. If the attribute is missing three phases (ABC or ABCN) shall be assumed. Default: None'    
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
    type:    
      description: NGSI type. It has to be Terminal    
      enum:    
        - Terminal    
      type: string    
      x-ngsi:    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Terminal/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/Terminal/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
JSON-LD形式のTerminalの例をkey-valuesとして利用することはできない。これは NGSI-v2 と互換性があり、`options=keyValues` を使用すると個々のエンティティのコンテキストデータを返す。  
正規化された JSON-LD 形式の Terminal の例は利用できません。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
JSON-LD形式のTerminalの例をkey-valuesとして利用することはできない。これは NGSI-LD と互換性があり、`options=keyValues` を使用すると個々のエンティティのコンテキストデータを返す。  
正規化された JSON-LD 形式の Terminal の例は利用できません。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
