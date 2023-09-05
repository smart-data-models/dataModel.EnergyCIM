<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Branche équivalente  
============================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/EquivalentBranch/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Adapté des modèles de données CIM. La classe représente des branches équivalentes.  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.    
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément  - `negativeR12[number]`: Résistance série de séquence négative de la séquence de bornes 1 à la séquence de bornes 2. Utilisée pour l'échange de données sur les courts-circuits conformément à la norme CEI 60909. La branche équivalente est le résultat d'une réduction du réseau avant l'échange de données.  . Model: [https://schema.org/Number](https://schema.org/Number)- `negativeR21[number]`: Résistance série de séquence négative de la séquence de bornes 2 à la séquence de bornes 1. Utilisée pour l'échange de données sur les courts-circuits conformément à la norme CEI 60909. La branche équivalente est le résultat d'une réduction du réseau avant l'échange de données.  . Model: [https://schema.org/Number](https://schema.org/Number)- `negativeX12[number]`: Réactance série de séquence négative de la séquence de bornes 1 à la séquence de bornes 2. Utilisée pour l'échange de données sur les courts-circuits conformément à la norme CEI 60909 Utilisation : la branche équivalente est le résultat de la réduction du réseau avant l'échange de données Défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `negativeX21[number]`: Réactance série de séquence négative de la séquence de bornes 2 à la séquence de bornes 1. Utilisé pour l'échange de données sur les courts-circuits conformément à la norme IEC 60909. Utilisation : Branche équivalente est un résultat de la réduction du réseau avant l'échange de données Défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `positiveR12[number]`: Résistance en série de séquence positive de la borne de séquence 1 à la borne de séquence 2. Utilisée pour l'échange de données sur les courts-circuits conformément à la norme CEI 60909.  La branche équivalente est le résultat de la réduction du réseau avant l'échange de données. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `positiveR21[number]`: Résistance série de séquence positive de la séquence de bornes 2 à la séquence de bornes 1. Utilisée pour l'échange de données sur les courts-circuits conformément à la norme CEI 60909. La branche équivalente est le résultat d'une réduction du réseau avant l'échange de données.  . Model: [https://schema.org/Number](https://schema.org/Number)- `positiveX12[number]`: Réactance série de séquence positive de la séquence de bornes 1 à la séquence de bornes 2. Utilisée pour l'échange de données sur les courts-circuits conformément à la norme CEI 60909 Utilisation : la branche équivalente est le résultat de la réduction du réseau avant l'échange de données Défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `positiveX21[number]`: Réactance série de séquence positive de la séquence de bornes 2 à la séquence de bornes 1. Utilisé pour l'échange de données sur les courts-circuits conformément à la norme CEI 60909 Utilisation : la branche équivalente est le résultat de la réduction du réseau avant l'échange de données Défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `r[number]`: Résistance série de séquence positive de la branche réduite. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `r21[number]`: Résistance entre la séquence de bornes 2 et la séquence de bornes 1, utilisée pour le flux d'énergie en régime permanent. Cet attribut est facultatif et représente un réseau déséquilibré tel qu'un déphaseur non nominal. Si seul EquivalentBranch.r est indiqué, EquivalentBranch.r21 est supposé égal à EquivalentBranch.r. Règle d'utilisation : EquivalentBranch est le résultat de la réduction du réseau avant l'échange de données. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `type[string]`: Type d'INSG. Il doit s'agir d'une branche équivalente  - `x[number]`: Réactance série de séquence positive de la branche réduite. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `x21[number]`: Réactance entre la séquence terminale 2 et la séquence terminale 1, utilisée pour le flux d'énergie en régime permanent. Cet attribut est facultatif et représente un réseau déséquilibré tel qu'un déphaseur non nominal. Si seule la branche équivalente.x est indiquée, la branche équivalente.x21 est supposée être égale à la branche équivalente.x. Règle d'utilisation : la branche équivalente est le résultat de la réduction du réseau avant l'échange de données. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `zeroR12[number]`: Résistance en série de séquence nulle de la séquence de bornes 1 à la séquence de bornes 2. Utilisée pour l'échange de données sur les courts-circuits conformément à la norme CEI 60909. La branche équivalente est le résultat d'une réduction du réseau avant l'échange de données.  . Model: [https://schema.org/Number](https://schema.org/Number)- `zeroR21[number]`: Résistance en série de séquence nulle de la séquence de bornes 2 à la séquence de bornes 1. Utilisé pour l'échange de données sur les courts-circuits conformément à la norme CEI 60909 Utilisation : la branche équivalente est le résultat de la réduction du réseau avant l'échange de données Défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `zeroX12[number]`: Réactance série homopolaire de la séquence de bornes 1 à la séquence de bornes 2. Utilisé pour l'échange de données sur les courts-circuits conformément à la norme CEI 60909 Utilisation : la branche équivalente est le résultat de la réduction du réseau avant l'échange de données Défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `zeroX21[number]`: Réactance série homopolaire entre la séquence de bornes 2 et la séquence de bornes 1. Utilisé pour l'échange de données sur les courts-circuits conformément à la norme CEI 60909 Utilisation : la branche équivalente est le résultat de la réduction du réseau avant l'échange de données Défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
<!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Adapté des modèles de données CIM et de CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Ce modèle de données est une conversion directe du modèle d'information commun (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par les entités suivantes : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un type erroné. Si c'est le cas, veuillez soulever un problème ou envoyer un courrier à info@smartdatamodels.org.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EquivalentBranch:    
  description: Adapted from CIM data models. The class represents equivalent branches.    
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
      description: NGSI type. It has to be EquivalentBranch    
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
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/EquivalentBranch/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/EquivalentBranch/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
Non disponible l'exemple d'une EquivalentBranch au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'une EquivalentBranch au format JSON-LD tel que normalisé. Ce format est compatible avec l'INSG-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'une EquivalentBranch au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'une EquivalentBranch au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
