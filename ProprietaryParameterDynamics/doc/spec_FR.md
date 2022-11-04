<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : ProprietaryParameterDynamics  
=====================================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ProprietaryParameterDynamics/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Adapté des modèles de données CIM. Supporte la définition d'un ou plusieurs paramètres de plusieurs types de données différents pour une utilisation par des modèles propriétaires définis par l'utilisateur.  NOTE : Cette classe n'hérite pas de IdentifiedObject car il n'est pas prévu qu'une seule instance de cette classe soit référencée par plus d'une instance de modèle propriétaire défini par l'utilisateur**.  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `AsynchronousMachineUserDefined[number]`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Valeur par défaut : Aucun  . Model: [https://schema.org/Number](https://schema.org/Number)- `DiscontinuousExcitationControlUserDefined[number]`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Valeur par défaut : Aucun  . Model: [https://schema.org/Number](https://schema.org/Number)- `ExcitationSystemUserDefined[number]`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Valeur par défaut : Aucun  . Model: [https://schema.org/Number](https://schema.org/Number)- `LoadUserDefined[number]`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Valeur par défaut : Aucun  . Model: [https://schema.org/Number](https://schema.org/Number)- `MechanicalLoadUserDefined[number]`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Valeur par défaut : Aucun  . Model: [https://schema.org/Number](https://schema.org/Number)- `OverexcitationLimiterUserDefined[number]`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Valeur par défaut : Aucun  . Model: [https://schema.org/Number](https://schema.org/Number)- `PFVArControllerType1UserDefined[number]`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Valeur par défaut : Aucun  . Model: [https://schema.org/Number](https://schema.org/Number)- `PFVArControllerType2UserDefined[number]`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Valeur par défaut : Aucun  . Model: [https://schema.org/Number](https://schema.org/Number)- `PowerSystemStabilizerUserDefined[number]`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Valeur par défaut : Aucun  . Model: [https://schema.org/Number](https://schema.org/Number)- `SynchronousMachineUserDefined[number]`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Valeur par défaut : Aucun  . Model: [https://schema.org/Number](https://schema.org/Number)- `TurbineGovernorUserDefined[number]`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Valeur par défaut : Aucun  . Model: [https://schema.org/Number](https://schema.org/Number)- `TurbineLoadControllerUserDefined[number]`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Valeur par défaut : Aucun  . Model: [https://schema.org/Number](https://schema.org/Number)- `UnderexcitationLimiterUserDefined[number]`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Valeur par défaut : Aucun  . Model: [https://schema.org/Number](https://schema.org/Number)- `VoltageAdjusterUserDefined[number]`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Valeur par défaut : Aucun  . Model: [https://schema.org/Number](https://schema.org/Number)- `VoltageCompensatorUserDefined[number]`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Valeur par défaut : Aucun  . Model: [https://schema.org/Number](https://schema.org/Number)- `WindPlantUserDefined[number]`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Valeur par défaut : Aucun  . Model: [https://schema.org/Number](https://schema.org/Number)- `WindType1or2UserDefined[number]`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Valeur par défaut : Aucun  . Model: [https://schema.org/Number](https://schema.org/Number)- `WindType3or4UserDefined[number]`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Valeur par défaut : Aucun  . Model: [https://schema.org/Number](https://schema.org/Number)- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour cet élément  - `areaServed[string]`: La zone géographique où un service ou un article offert est fourni  . Model: [https://schema.org/Text](https://schema.org/Text)- `booleanParameterValue[number]`: Utilisé pour la valeur du paramètre booléen. Si cet attribut est renseigné, integerParameterValue et floatParameterValue ne le seront pas. Valeur par défaut : False  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified[string]`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description[string]`: Une description de cet article  - `floatParameterValue[number]`: Utilisé pour la valeur du paramètre en virgule flottante.  Si cet attribut est renseigné, booleanParameterValue et integerParameterValue ne le seront pas. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identifiant unique de l'entité  - `integerParameterValue[number]`: Utilisé pour la valeur entière du paramètre.  Si cet attribut est renseigné, booleanParameterValue et floatParameterValue ne le seront pas. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément.  - `owner[array]`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `parameterNumber[number]`: Numéro de séquence du paramètre parmi l'ensemble des paramètres associés au modèle propriétaire défini par l'utilisateur. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires sur l'article  - `source[string]`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type[string]`: Type NGSI. Il doit être ProprietaryParameterDynamics.  <!-- /30-PropertiesList -->  
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
ProprietaryParameterDynamics:    
  description: 'Adapted from CIM data models. Supports definition of one or more parameters of several different datatypes for use by proprietary user-defined models.  NOTE: This class does not inherit from IdentifiedObject since it is not intended that a single instance of it be referenced by more than one proprietary user-defined model instance.'    
  properties:    
    AsynchronousMachineUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    DiscontinuousExcitationControlUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ExcitationSystemUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    LoadUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    MechanicalLoadUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    OverexcitationLimiterUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    PFVArControllerType1UserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    PFVArControllerType2UserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    PowerSystemStabilizerUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    SynchronousMachineUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    TurbineGovernorUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    TurbineLoadControllerUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    UnderexcitationLimiterUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    VoltageAdjusterUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    VoltageCompensatorUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    WindPlantUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    WindType1or2UserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    WindType3or4UserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
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
    booleanParameterValue:    
      description: 'Used for boolean parameter value. If this attribute is populated, integerParameterValue and floatParameterValue will not be. Default: False'    
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
    floatParameterValue:    
      description: 'Used for floating point parameter value.  If this attribute is populated, booleanParameterValue and integerParameterValue will not be. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &proprietaryparameterdynamics_-_properties_-_owner_-_items_-_anyof    
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
    integerParameterValue:    
      description: 'Used for integer parameter value.  If this attribute is populated, booleanParameterValue and floatParameterValue will not be. Default: 0'    
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
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *proprietaryparameterdynamics_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    parameterNumber:    
      description: 'Sequence number of the parameter among the set of parameters associated with the related proprietary user-defined model. Default: 0'    
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
      description: 'NGSI type. It has to be ProprietaryParameterDynamics'    
      enum:    
        - ProprietaryParameterDynamics    
      type: string    
      x-ngsi:    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ProprietaryParameterDynamics/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/ProprietaryParameterDynamics/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
Non disponible l'exemple d'un ProprietaryParameterDynamics au format JSON-LD comme key-values. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un ProprietaryParameterDynamics au format JSON-LD tel que normalisé. Ceci est compatible avec la NGSI-v2 lorsqu'elle n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un ProprietaryParameterDynamics au format JSON-LD comme key-values. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un ProprietaryParameterDynamics au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
