<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティトポロジカルノード  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/TopologicalNode/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述。**CIMデータモデルから引用した。詳細な変電所モデルの場合、トポロジカルノードとは、現在のネットワーク状態において、ジャンパーを含む任意のタイプの閉じたスイッチを通して一緒に接続されている接続ノードのセットである。トポロジカルノードは、現在のネットワーク状態が変化すると（つまり、スイッチ、ブレーカーなどの状態が変化すると）変化する。計画モデルでは、トポロジカルノードを形成するためにスイッチのステータスは使用されません。代わりに、モデルビルダーツールで手動で作成または削除されます。このように維持されるトポロジカルノードは「バス」とも呼ばれる**。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `AngleRefTopologicalIsland[number]`: このノードが角度参照となる島を指定します。   通常、各島に1つの角度参照ノードが存在します。デフォルトはなし  . Model: [https://schema.org/Number](https://schema.org/Number)- `BaseVoltage[number]`: トポロジカルノードのベース電圧。デフォルトはなし  . Model: [https://schema.org/Number](https://schema.org/Number)- `ConnectivityNodeContainer[number]`: トップロジカル・ノードが属するコネクティビティ・ノード・コンテナ。デフォルトはなし  . Model: [https://schema.org/Number](https://schema.org/Number)- `ConnectivityNodes[number]`: この接続ノードが割り当てられているトポロジカルノード。  ネットワーク内のスイッチの現在の状態に依存する場合がある。デフォルト: 'list'  . Model: [https://schema.org/Number](https://schema.org/Number)- `ReportingGroup[number]`: 報告グループに属するトポロジカルノード。デフォルトはなし  . Model: [https://schema.org/Number](https://schema.org/Number)- `SvInjection[number]`: フローインジェクション状態変数に関連するトポロジカルノード。デフォルトはなし  . Model: [https://schema.org/Number](https://schema.org/Number)- `SvVoltage[number]`: 電圧状態に関連するトポロジカルノード。デフォルトなし  . Model: [https://schema.org/Number](https://schema.org/Number)- `Terminal[number]`: 端末に関連付けられたトポロジカルノード。   これはトポロジカルノードへの接続性ノードのパスの代わりとして使用することができ、したがって、場合によっては接続性ノードをモデル化する必要がなくなる。   接続ノードがモデル内にある場合、この関連付けはおそらく入力指定として使われないことに注意。デフォルト: 'list'  . Model: [https://schema.org/Number](https://schema.org/Number)- `TopologicalIsland[number]`: トポロジカルノードがトポロジカルアイランドに属するかどうか。デフォルトなし  . Model: [https://schema.org/Number](https://schema.org/Number)- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別称  - `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `boundaryPoint[number]`: ノードが BoundaryPoint であるかどうかを識別する。boundaryPoint=true の場合、ConnectivityNode または TopologicalNode は、BoundaryPoint を表します。デフォルトはFalse  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `fromEndIsoCode[number]`: この属性は、バウンダリポイントの From` 側が属する、または接続される地域の ISO コードを交換するために使用されます。ISOコードはISO3166()で定義された2文字の国コードである。文字列の長さは最大2文字である。この属性は、Boundary Topology プロファイルの TopologicalNode と Boundary Equipment プロファイルの ConnectivityNode にのみ使用される Boundary Model Authority Set で必須となります。デフォルト：''。  . Model: [https://schema.org/Number](https://schema.org/Number)- `fromEndName[number]`: この属性は，最大 32 文字の文字列からなる可読性の高い名前を交換するために使用される。この属性は、2つのケースをカバーしています。  この属性は、Boundary Topology プロファイルの TopologicalNode と Boundary Equipment プロファイルの ConnectivityNode にのみ使用される Boundary Model Authority Set で必要とされます。デフォルト：''。  . Model: [https://schema.org/Number](https://schema.org/Number)- `fromEndNameTso[number]`: この属性は、バウンダリポイントの`From`側が属する、または接続されているTSOの名称を交換するために使用される。文字列の長さは最大32文字です。この属性は、Boundary Topology プロファイルの TopologicalNode と Boundary Equipment プロファイルの ConnectivityNode にのみ使用される Boundary Model Authority Set で必要とされる。デフォルト：''。  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: エンティティの一意な識別子  - `location[*]`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `name[string]`: このアイテムの名称です。  - `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリスト  - `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `toEndIsoCode[number]`: この属性は、バウンダリポイントの `To` 側が属する、または接続される地域の ISO コードを交換するために使用されます。ISOコードはISO3166()で定義された2文字の国コードです。文字列の長さは最大2文字です。この属性は、Boundary Topology プロファイルの TopologicalNode と Boundary Equipment プロファイルの ConnectivityNode にのみ使用される Boundary Model Authority Set で必須となります。デフォルト：''。  . Model: [https://schema.org/Number](https://schema.org/Number)- `toEndName[number]`: この属性は，最大 32 文字の文字列からなる可読性の高い名前を交換するために使用される。この属性は、2つのケースをカバーしています。  この属性は、Boundary Topology プロファイルの TopologicalNode と Boundary Equipment プロファイルの ConnectivityNode にのみ使用される Boundary Model Authority Set で必要とされます。デフォルト：''。  . Model: [https://schema.org/Number](https://schema.org/Number)- `toEndNameTso[number]`: この属性は、バウンダリポイントの`To`側が属する、あるいは接続されるTSOの名称を交換するために使用される。文字列の長さは最大32文字です。この属性は、Boundary Topology プロファイルの TopologicalNode と Boundary Equipment プロファイルの ConnectivityNode にのみ使用される Boundary Model Authority Set で必要とされる。デフォルト：''。  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSIタイプ。TopologicalNodeである必要があります。  <!-- /30-PropertiesList -->  
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
TopologicalNode:    
  description: 'Adapted from CIM data models. For a detailed substation model a topological node is a set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes change as the current network state changes (i.e., switches, breakers, etc. change state). For a planning model, switch statuses are not used to form topological nodes. Instead they are manually created or deleted in a model builder tool. Topological nodes maintained this way are also called ''busses''.'    
  properties:    
    AngleRefTopologicalIsland:    
      description: 'The island for which the node is an angle reference.   Normally there is one angle reference node for each island. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    BaseVoltage:    
      description: 'The base voltage of the topologocial node. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ConnectivityNodeContainer:    
      description: 'The connectivity node container to which the toplogical node belongs. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ConnectivityNodes:    
      description: 'The topological node to which this connectivity node is assigned.  May depend on the current state of switches in the network. Default: ''list'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ReportingGroup:    
      description: 'The topological nodes that belong to the reporting group. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    SvInjection:    
      description: 'The topological node associated with the flow injection state variable. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    SvVoltage:    
      description: 'The topological node associated with the voltage state. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    Terminal:    
      description: 'The topological node associated with the terminal.   This can be used as an alternative to the connectivity node path to topological node, thus making it unneccesary to model connectivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would probably not be used as an input specification. Default: ''list'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    TopologicalIsland:    
      description: 'A topological node belongs to a topological island. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
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
    boundaryPoint:    
      description: 'Identifies if a node is a BoundaryPoint. If boundaryPoint=true the ConnectivityNode or the TopologicalNode represents a BoundaryPoint. Default: False'    
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
    fromEndIsoCode:    
      description: 'The attribute is used for an exchange of the ISO code of the region to which the `From` side of the Boundary point belongs to or it is connected to. The ISO code is two characters country code as defined by ISO 3166 (). The length of the string is 2 characters maximum. The attribute is a required for the Boundary Model Authority Set where this attribute is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: '''''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fromEndName:    
      description: 'The attribute is used for an exchange of a human readable name with length of the string 32 characters maximum. The attribute covers two cases:  The attribute is required for the Boundary Model Authority Set where it is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: '''''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fromEndNameTso:    
      description: 'The attribute is used for an exchange of the name of the TSO to which the `From` side of the Boundary point belongs to or it is connected to. The length of the string is 32 characters maximum. The attribute is required for the Boundary Model Authority Set where it is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: '''''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &topologicalnode_-_properties_-_owner_-_items_-_anyof    
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
        anyOf: *topologicalnode_-_properties_-_owner_-_items_-_anyof    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    toEndIsoCode:    
      description: 'The attribute is used for an exchange of the ISO code of the region to which the `To` side of the Boundary point belongs to or it is connected to. The ISO code is two characters country code as defined by ISO 3166 (). The length of the string is 2 characters maximum. The attribute is a required for the Boundary Model Authority Set where this attribute is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: '''''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    toEndName:    
      description: 'The attribute is used for an exchange of a human readable name with length of the string 32 characters maximum. The attribute covers two cases:  The attribute is required for the Boundary Model Authority Set where it is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: '''''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    toEndNameTso:    
      description: 'The attribute is used for an exchange of the name of the TSO to which the `To` side of the Boundary point belongs to or it is connected to. The length of the string is 32 characters maximum. The attribute is required for the Boundary Model Authority Set where it is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: '''''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be TopologicalNode'    
      enum:    
        - TopologicalNode    
      type: string    
      x-ngsi:    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/TopologicalNode/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/TopologicalNode/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
JSON-LD形式のTopologicalNodeの例をkey-valuesとして利用することはできない。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータが返される。  
JSON-LD 形式で正規化された TopologicalNode の例は利用不可。これはオプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返す。  
JSON-LD形式のTopologicalNodeの例をkey-valuesとして利用することはできない。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータが返される。  
TopologicalNodeのJSON-LD形式での正規化された例は利用不可。これはオプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
