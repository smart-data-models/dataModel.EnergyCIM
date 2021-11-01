エンティティEquivalentBranch  
======================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/EquivalentBranch/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述です。**CIMのデータモデルからの引用です。このクラスは同等のブランチを表します。  

## プロパティのリスト  

- `address`: 郵送先住所  - `alternateName`: このアイテムの別称  - `areaServed`: サービスや提供されるアイテムが提供される地理的なエリア  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `description`: このアイテムの説明  - `id`: エンティティのユニークな識別子  - `location`: アイテムへのGeojson参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygonのいずれかです。  - `name`: このアイテムの名前です。  - `negativeR12`: 端子配列1から端子配列2への負の配列直列抵抗。IEC 60909 に基づく短絡データ交換に使用される。  - `negativeR21`: 端子配列2から端子配列1への負の配列直列抵抗。IEC 60909 に基づく短絡データ交換に使用される。  - `negativeX12`: 端子配列1から端子配列2への負の直列リアクタンス。IEC 60909に基づく短絡データ交換に使用される 使用法：EquivalentBranchはデータ交換前のネットワーク縮小の結果 デフォルト：0.0  - `negativeX21`: 端子配列2から端子配列1への負の直列リアクタンス。IEC 60909に基づく短絡データ交換に使用される。使用方法。EquivalentBranchはデータ交換前のネットワーク縮小の結果 デフォルト：0.0  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `positiveR12`: 端子配列1から端子配列2への正の直列抵抗。IEC 60909に基づく短絡データ交換に使用されます。  EquivalentBranchは、データ交換の前にネットワークを縮小した結果である。デフォルト：0.0  - `positiveR21`: 端子配列2から端子配列1への正順直列抵抗。IEC 60909に準拠した短絡データ交換に使用される 等価分岐はデータ交換前のネットワーク縮小の結果 デフォルト：0.0  - `positiveX12`: 端子配列1から端子配列2への正順直列リアクタンス。IEC 60909による短絡データ交換に使用される 使用法：EquivalentBranchはデータ交換前のネットワーク縮小の結果 デフォルト：0.0  - `positiveX21`: 端子配列2から端子配列1への正順直列リアクタンス。IEC 60909に基づく短絡データ交換に使用される 使用法：EquivalentBranchはデータ交換前のネットワーク縮小の結果 デフォルト：0.0  - `r`: 還元ブランチの正方向の直列抵抗デフォルト：0.0  - `r21`: 端子配列2から端子配列1への抵抗。定常的なパワーフローに使用される。この属性はオプションであり、オフノミナルなフェイズシフターのようなアンバランスなネットワークを表す。EquivalentBranch.rのみが指定された場合、EquivalentBranch.r21はEquivalentBranch.rと等しいと仮定される。使用規則：EquivalentBranchは、データ交換の前にネットワークを縮小した結果である。デフォルト：0.0  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `type`: NGSIタイプです。EquivalentBranchである必要があります。  - `x`: リダクションブランチの正順直列リアクタンスデフォルト：0.0  - `x21`: ターミナル・シーケンス2からターミナル・シーケンス1へのリアクタンスで、定常的なパワーフローに使用される。この属性はオプションであり、オフノミナル・フェイズ・シフターのようなアンバランスなネットワークを表す。EquivalentBranch.xのみが与えられた場合、EquivalentBranch.x21はEquivalentBranch.xと等しいと仮定される。使用規則：EquivalentBranchは、データ交換の前にネットワークを縮小した結果である。デフォルト：0.0  - `zeroR12`: 端子配列1から端子配列2へのゼロシーケンス直列抵抗。IEC 60909に基づく短絡データ交換に使用される 等価分岐はデータ交換前のネットワーク縮小の結果 デフォルト：0.0  - `zeroR21`: 端子配列2から端子配列1へのゼロ配列直列抵抗。IEC 60909に基づく短絡データ交換に使用される 使用法：EquivalentBranchはデータ交換前のネットワーク縮小の結果 デフォルト：0.0  - `zeroX12`: 端子配列1から端子配列2へのゼロシーケンス直列リアクタンス。IEC 60909に基づく短絡データ交換に使用される 使用法：EquivalentBranchはデータ交換前のネットワーク縮小の結果 デフォルト：0.0  - `zeroX21`: 端子配列2から端子配列1への零相直列リアクタンス。IEC 60909による短絡データ交換に使用 使用方法：EquivalentBranchはデータ交換前のネットワーク縮小の結果 デフォルト：0.0    
必須項目  
CIMデータモデルとCIMpyからの採用 - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy)。このデータモデルは、IEC61970規格で規定されたCommon Information Model (CIM)をスマートデータモデルに直接変換したものです。このモデルがベースとしているpythonクラスは、Institute for Automation of Complex Power Systems (ACS)、EON Energy Research Center (EONERC)、RWTH University Aachen (ドイツ) の3団体によって開発されました。一部のプロパティのタイプが間違っている場合があります。このような場合には、問題を提起するか、info@smartdatamodels.org にメールを送ってください。  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EquivalentBranch:    
  description: 'Adapted from CIM data models. The class represents equivalent branches.'    
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
    id:    
      anyOf: &equivalentbranch_-_properties_-_owner_-_items_-_anyof    
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
    negativeR12:    
      description: 'Negative sequence series resistance from terminal sequence  1 to terminal sequence 2. Used for short circuit data exchange according to IEC 60909 EquivalentBranch is a result of network reduction prior to the data exchange Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    negativeR21:    
      description: 'Negative sequence series resistance from terminal sequence 2 to terminal sequence 1. Used for short circuit data exchange according to IEC 60909 EquivalentBranch is a result of network reduction prior to the data exchange Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    negativeX12:    
      description: 'Negative sequence series reactance from terminal sequence  1 to terminal sequence 2. Used for short circuit data exchange according to IEC 60909 Usage : EquivalentBranch is a result of network reduction prior to the data exchange Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    negativeX21:    
      description: 'Negative sequence series reactance from terminal sequence 2 to terminal sequence 1. Used for short circuit data exchange according to IEC 60909. Usage: EquivalentBranch is a result of network reduction prior to the data exchange Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *equivalentbranch_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    positiveR12:    
      description: 'Positive sequence series resistance from terminal sequence  1 to terminal sequence 2 . Used for short circuit data exchange according to IEC 60909.  EquivalentBranch is a result of network reduction prior to the data exchange. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    positiveR21:    
      description: 'Positive sequence series resistance from terminal sequence 2 to terminal sequence 1. Used for short circuit data exchange according to IEC 60909 EquivalentBranch is a result of network reduction prior to the data exchange Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    positiveX12:    
      description: 'Positive sequence series reactance from terminal sequence  1 to terminal sequence 2. Used for short circuit data exchange according to IEC 60909 Usage : EquivalentBranch is a result of network reduction prior to the data exchange Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    positiveX21:    
      description: 'Positive sequence series reactance from terminal sequence 2 to terminal sequence 1. Used for short circuit data exchange according to IEC 60909 Usage : EquivalentBranch is a result of network reduction prior to the data exchange Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    r:    
      description: 'Positive sequence series resistance of the reduced branch. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    r21:    
      description: 'Resistance from terminal sequence 2 to terminal sequence 1 .Used for steady state power flow. This attribute is optional and represent unbalanced network such as off-nominal phase shifter. If only EquivalentBranch.r is given, then EquivalentBranch.r21 is assumed equal to EquivalentBranch.r. Usage rule : EquivalentBranch is a result of network reduction prior to the data exchange. Default: 0.0'    
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
    type:    
      description: 'NGSI type. It has to be EquivalentBranch'    
      enum:    
        - EquivalentBranch    
      type: string    
      x-ngsi:    
        type: Property    
    x:    
      description: 'Positive sequence series reactance of the reduced branch. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    x21:    
      description: 'Reactance from terminal sequence 2 to terminal sequence 1 .Used for steady state power flow. This attribute is optional and represent unbalanced network such as off-nominal phase shifter. If only EquivalentBranch.x is given, then EquivalentBranch.x21 is assumed equal to EquivalentBranch.x. Usage rule : EquivalentBranch is a result of network reduction prior to the data exchange. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    zeroR12:    
      description: 'Zero sequence series resistance from terminal sequence  1 to terminal sequence 2. Used for short circuit data exchange according to IEC 60909 EquivalentBranch is a result of network reduction prior to the data exchange Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    zeroR21:    
      description: 'Zero sequence series resistance from terminal sequence  2 to terminal sequence 1. Used for short circuit data exchange according to IEC 60909 Usage : EquivalentBranch is a result of network reduction prior to the data exchange Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    zeroX12:    
      description: 'Zero sequence series reactance from terminal sequence  1 to terminal sequence 2. Used for short circuit data exchange according to IEC 60909 Usage : EquivalentBranch is a result of network reduction prior to the data exchange Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    zeroX21:    
      description: 'Zero sequence series reactance from terminal sequence 2 to terminal sequence 1. Used for short circuit data exchange according to IEC 60909 Usage : EquivalentBranch is a result of network reduction prior to the data exchange Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
```  
</details>    
## ペイロードの例  
JSON-LD形式のEquivalentBranchの例をkey-valuesとして利用できません。これは、`options=keyValues`を使用した場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
JSON-LD形式のEquivalentBranchの例を正規化したものはありません。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
JSON-LD形式のEquivalentBranchの例をkey-valuesとして利用できません。これは、`options=keyValues`を使用した場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
JSON-LD形式のEquivalentBranchの例を正規化したものはありません。オプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
