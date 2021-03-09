Entité : ProprietaryParameterDynamics  
=====================================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ProprietaryParameterDynamics/LICENSE.md)  
Description globale : **Adapté des modèles de données CIM. Prend en charge la définition d'un ou plusieurs paramètres de plusieurs types de données différents pour une utilisation par des modèles propriétaires définis par l'utilisateur.  NOTE : Cette classe n'hérite pas de IdentifiedObject car il n'est pas prévu qu'une seule de ses instances soit référencée par plus d'une instance de modèle propriétaire définie par l'utilisateur.**  

## Liste des biens  

- `AsynchronousMachineUserDefined`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Par défaut : Aucun  - `DiscontinuousExcitationControlUserDefined`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Par défaut : Aucun  - `ExcitationSystemUserDefined`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Par défaut : Aucun  - `LoadUserDefined`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Par défaut : Aucun  - `MechanicalLoadUserDefined`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Par défaut : Aucun  - `OverexcitationLimiterUserDefined`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Par défaut : Aucun  - `PFVArControllerType1UserDefined`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Par défaut : Aucun  - `PFVArControllerType2UserDefined`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Par défaut : Aucun  - `PowerSystemStabilizerUserDefined`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Par défaut : Aucun  - `SynchronousMachineUserDefined`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Par défaut : Aucun  - `TurbineGovernorUserDefined`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Par défaut : Aucun  - `TurbineLoadControllerUserDefined`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Par défaut : Aucun  - `UnderexcitationLimiterUserDefined`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Par défaut : Aucun  - `VoltageAdjusterUserDefined`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Par défaut : Aucun  - `VoltageCompensatorUserDefined`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Par défaut : Aucun  - `WindPlantUserDefined`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Par défaut : Aucun  - `WindType1or2UserDefined`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Par défaut : Aucun  - `WindType3or4UserDefined`: Modèle propriétaire défini par l'utilisateur auquel ce paramètre est associé. Par défaut : Aucun  - `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `booleanParameterValue`: Utilisé pour la valeur du paramètre booléen. Si cet attribut est renseigné, integerParameterValue et floatParameterValue ne le seront pas. Par défaut : False  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `floatParameterValue`: Utilisé pour la valeur du paramètre à virgule flottante.  Si cet attribut est renseigné, booleanParameterValue et integerParameterValue ne le seront pas. Valeur par défaut : 0.0  - `id`: Identifiant unique de l'entité  - `integerParameterValue`: Utilisé pour la valeur d'un paramètre entier.  Si cet attribut est renseigné, booleanParameterValue et floatParameterValue ne le seront pas. Valeur par défaut : 0  - `location`:   - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `parameterNumber`: Numéro de séquence du paramètre parmi l'ensemble des paramètres associés au modèle propriétaire correspondant défini par l'utilisateur. Valeur par défaut : 0  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `type`: Type NGSI. Il doit être de type ProprietaryParameterDynamics    
Propriétés requises  
Ce modèle de données est une conversion directe du modèle commun d'information (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un mauvais type. C'est le cas, pelase soulever un problème ou envoyer un mail à alberto.abella@fiware.org  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
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
    DiscontinuousExcitationControlUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ExcitationSystemUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    LoadUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    MechanicalLoadUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    OverexcitationLimiterUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    PFVArControllerType1UserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    PFVArControllerType2UserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    PowerSystemStabilizerUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    SynchronousMachineUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    TurbineGovernorUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    TurbineLoadControllerUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    UnderexcitationLimiterUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    VoltageAdjusterUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    VoltageCompensatorUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    WindPlantUserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    WindType1or2UserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    WindType3or4UserDefined:    
      description: 'Proprietary user-defined model with which this parameter is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/Text'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/Text'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/Text'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/Text'''    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    booleanParameterValue:    
      description: 'Used for boolean parameter value. If this attribute is populated, integerParameterValue and floatParameterValue will not be. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    floatParameterValue:    
      description: 'Used for floating point parameter value.  If this attribute is populated, booleanParameterValue and integerParameterValue will not be. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
      type: Property    
    integerParameterValue:    
      description: 'Used for integer parameter value.  If this attribute is populated, booleanParameterValue and floatParameterValue will not be. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
      title: 'GeoJSON Geometry'    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *proprietaryparameterdynamics_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    parameterNumber:    
      description: 'Sequence number of the parameter among the set of parameters associated with the related proprietary user-defined model. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI type. It has to be ProprietaryParameterDynamics'    
      enum:    
        - ProprietaryParameterDynamics    
      type: Property    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un ProprietaryParameterDynamics au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsque l'on utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un ProprietaryParameterDynamics en format JSON comme normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un ProprietaryParameterDynamics au format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un ProprietaryParameterDynamics en format JSON-LD comme normalisé. Il est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
