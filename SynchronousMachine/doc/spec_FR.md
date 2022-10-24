<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : SynchronousMachine  
===========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/SynchronousMachine/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Adapté des modèles de données CIM. Un dispositif électromécanique qui fonctionne avec un arbre tournant de manière synchrone avec le réseau. Il s'agit d'une machine unique fonctionnant soit comme un générateur, soit comme un condensateur ou une pompe synchrone.**  
version : 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `InitialReactiveCapabilityCurve[number]`: Les machines synchrones utilisent cette courbe par défaut. Par défaut : Aucun  . Model: [https://schema.org/Number](https://schema.org/Number)- `SynchronousMachineDynamics[number]`: Modèle de dynamique de la machine synchrone utilisé pour décrire le comportement dynamique de cette machine synchrone. Valeur par défaut : Aucun  . Model: [https://schema.org/Number](https://schema.org/Number)- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour cet élément  - `areaServed[string]`: La zone géographique où un service ou un article offert est fourni  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified[string]`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description[string]`: Une description de cet article  - `earthing[number]`: Indique si le générateur est mis à la terre ou non. Utilisé pour l'échange de données sur les courts-circuits selon la norme CEI 60909 Par défaut : Faux  . Model: [https://schema.org/Number](https://schema.org/Number)- `earthingStarPointR[number]`: Résistance de mise à la terre du point étoile du générateur (Re). Utilisée pour l'échange de données sur les courts-circuits selon la norme CEI 60909 Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `earthingStarPointX[number]`: Réactance de mise à la terre du point étoile du générateur (Xe). Utilisée pour l'échange de données sur les courts-circuits selon la norme IEC 60909 Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identifiant unique de l'entité  - `ikk[number]`: Courant de court-circuit en régime permanent (en A pour le profil) du générateur avec excitation composée pendant un court-circuit triphasé. - Ikk=0 : Générateur sans excitation composée. - Ikk?0 : Générateur avec excitation composée. Ikk est utilisé pour calculer le courant de court-circuit minimum en régime permanent pour les générateurs avec excitation composée (Section 4.6.1.2 de la CEI 60909-0). Utilisé uniquement pour un court-circuit à alimentation unique sur un générateur. (Section 4.3.4.2. de la norme CEI 60909-0) Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `maxQ[number]`: Limite maximale de la puissance réactive. Il s'agit de la limite maximale (plaque signalétique) de l'unité. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `minQ[number]`: Limite de puissance réactive minimale pour l'unité. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `mu[number]`: Facteur permettant de calculer le courant de rupture (Section 4.5.2.1 de la CEI 60909-0). Utilisé uniquement pour un court-circuit à alimentation unique sur un générateur (section 4.3.4.2. de la norme CEI 60909-0). Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: Le nom de cet élément.  - `operatingMode[number]`: Mode de fonctionnement actuel. Par défaut : Aucun  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `qPercent[number]`: Pourcentage de la commande réactive coordonnée qui provient de cette machine. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `r[number]`: Résistance équivalente (RG) du générateur. La RG est prise en compte pour le calcul de tous les courants, sauf pour le calcul du courant de pointe ip. Utilisée pour l'échange de données sur les courts-circuits selon la norme IEC 60909 Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `r0[number]`: Résistance de séquence zéro de la machine synchrone. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `r2[number]`: Résistance de séquence négative. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `referencePriority[number]`: Priorité de l'unité pour l'utilisation en tant que sélection de bus de référence d'angle de phase de tension de flux de puissance. 0 = indifférent (par défaut) 1 = priorité la plus élevée. 2 est inférieur à 1 et ainsi de suite. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `satDirectSubtransX[number]`: Réactance subtransitoire à axe direct saturée, également connue sous le nom de Xd`sat. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `satDirectSyncX[number]`: Réactance synchrone saturée à axe direct (xdsat) ; réciproque du rapport de court-circuit. Utilisé pour l'échange de données sur les courts-circuits, uniquement pour les courts-circuits à alimentation unique sur un générateur. (Section 4.3.4.2. de la norme IEC 60909-0). Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `satDirectTransX[number]`: Réactance transitoire saturée à axe direct. Cet attribut est principalement utilisé pour les calculs de court-circuit selon l'ANSI. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires sur l'article  - `shortCircuitRotorType[number]`: Type de rotor, utilisé par les applications de court-circuit, uniquement pour un court-circuit à alimentation unique selon la norme IEC 60909. Par défaut : Aucun  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type[string]`: Modes dans lesquels cette machine synchrone peut fonctionner. Par défaut : None. Type d'entité NGSI. Il doit être SynchronousMachine.  . Model: [https://schema.org/Number](https://schema.org/Number)- `voltageRegulationRange[number]`: Plage de régulation de la tension du générateur (PG dans la CEI 60909-0) utilisée pour le calcul du facteur de correction d'impédance KG défini dans la CEI 60909-0 Cet attribut est utilisé pour décrire la tension de fonctionnement de l'unité de production. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `x0[number]`: Réactance homopolaire de la machine synchrone. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `x2[number]`: Réactance de séquence négative. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
<!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Adapté de CIM data models and CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Ce modèle de données est une conversion directe du modèle d'information commun (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un mauvais type. Si tel était le cas, veuillez soulever un problème ou envoyer un courrier à info@smartdatamodels.org.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
SynchronousMachine:    
  description: 'Adapted from CIM data models. An electromechanical device that operates with shaft rotating synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.'    
  properties:    
    InitialReactiveCapabilityCurve:    
      description: 'Synchronous machines using this curve as default. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    SynchronousMachineDynamics:    
      description: 'Synchronous machine dynamics model used to describe dynamic behavior of this synchronous machine. Default: None'    
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
    earthing:    
      description: 'Indicates whether or not the generator is earthed. Used for short circuit data exchange according to IEC 60909 Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    earthingStarPointR:    
      description: 'Generator star point earthing resistance (Re). Used for short circuit data exchange according to IEC 60909 Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    earthingStarPointX:    
      description: 'Generator star point earthing reactance (Xe). Used for short circuit data exchange according to IEC 60909 Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &synchronousmachine_-_properties_-_owner_-_items_-_anyof    
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
    ikk:    
      description: 'Steady-state short-circuit current (in A for the profile) of generator with compound excitation during 3-phase short circuit. - Ikk=0: Generator with no compound excitation. - Ikk?0: Generator with compound excitation. Ikk is used to calculate the minimum steady-state short-circuit current for generators with compound excitation (Section 4.6.1.2 in the IEC 60909-0) Used only for single fed short circuit on a generator. (Section 4.3.4.2. in the IEC 60909-0) Default: 0.0'    
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
    maxQ:    
      description: 'Maximum reactive power limit. This is the maximum (nameplate) limit for the unit. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    minQ:    
      description: 'Minimum reactive power limit for the unit. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    mu:    
      description: 'Factor to calculate the breaking current (Section 4.5.2.1 in the IEC 60909-0). Used only for single fed short circuit on a generator (Section 4.3.4.2. in the IEC 60909-0). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    operatingMode:    
      description: 'Current mode of operation. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *synchronousmachine_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    qPercent:    
      description: 'Percent of the coordinated reactive control that comes from this machine. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    r:    
      description: 'Equivalent resistance (RG) of generator. RG is considered for the calculation of all currents, except for the calculation of the peak current ip. Used for short circuit data exchange according to IEC 60909 Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    r0:    
      description: 'Zero sequence resistance of the synchronous machine. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    r2:    
      description: 'Negative sequence resistance. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    referencePriority:    
      description: 'Priority of unit for use as powerflow voltage phase angle reference bus selection. 0 = don t care (default) 1 = highest priority. 2 is less than 1 and so on. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    satDirectSubtransX:    
      description: 'Direct-axis subtransient reactance saturated, also known as Xd`sat. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    satDirectSyncX:    
      description: 'Direct-axes saturated synchronous reactance (xdsat); reciprocal of short-circuit ration. Used for short circuit data exchange, only for single fed short circuit on a generator. (Section 4.3.4.2. in the IEC 60909-0). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    satDirectTransX:    
      description: 'Saturated Direct-axis transient reactance. The attribute is primarily used for short circuit calculations according to ANSI. Default: 0.0'    
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
    shortCircuitRotorType:    
      description: 'Type of rotor, used by short circuit applications, only for single fed short circuit according to IEC 60909. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'Modes that this synchronous machine can operate in. Default: None. NGSI entity type. it has to be SynchronousMachine'    
      enum:    
        - SynchronousMachine    
      type: string    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    voltageRegulationRange:    
      description: 'Range of generator voltage regulation (PG in the IEC 60909-0) used for calculation of the impedance correction factor KG defined in IEC 60909-0 This attribute is used to describe the operating voltage of the generating unit. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    x0:    
      description: 'Zero sequence reactance of the synchronous machine. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    x2:    
      description: 'Negative sequence reactance. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/SynchronousMachine/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/SynchronousMachine/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
Non disponible l'exemple d'une SynchronousMachine au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'une SynchronousMachine au format JSON-LD tel que normalisé. Ceci est compatible avec la NGSI-v2 lorsqu'elle n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'une SynchronousMachine au format JSON-LD comme key-values. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'une SynchronousMachine au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
