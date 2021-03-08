Entité : AsynchronousMachine  
============================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/AsynchronousMachine/LICENSE.md)  
Description globale : **Adapté des modèles de données CIM. Machine tournante dont l'arbre tourne de manière asynchrone avec le champ électrique.  Aussi appelée machine à induction sans connexion externe aux enroulements du rotor, par exemple une machine à induction à cage d'écureuil.**  

## Liste des biens  

- `AsynchronousMachineDynamics`: Modèle de dynamique de machine asynchrone utilisé pour décrire le comportement dynamique de cette machine asynchrone. Par défaut : Aucun  - `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `asynchronousMachineType`: Indique le type de machine asynchrone (moteur ou générateur). Par défaut : Aucun  - `converterFedDrive`: Indique si la machine est un entraînement alimenté par un convertisseur. Utilisé pour l'échange de données de court-circuit selon la norme IEC 60909 Défaut : Faux :  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `efficiency`: Rendement de la machine asynchrone à son fonctionnement nominal en pourcentage. Indicateur pour les moteurs d'entraînement des convertisseurs. Utilisé pour l'échange de données de court-circuit selon la norme CEI 60909 Valeur par défaut : 0,0  - `iaIrRatio`: Rapport entre le courant du rotor bloqué et le courant nominal du moteur (Ia/Ir). Utilisé pour l'échange de données de court-circuit selon la norme IEC 60909 Défaut : 0,0  - `id`: Identifiant unique de l'entité  - `location`:   - `name`: Le nom de cet article.  - `nominalFrequency`: Les données de la plaque signalétique indiquent si la machine est à 50 ou 60 Hz. Valeur par défaut : 0.0  - `nominalSpeed`: Données de la plaque d'identification.  Dépend du glissement et du nombre de paires de pôles. Valeur par défaut : 0.0  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `polePairNumber`: Nombre de paires de pôles du stator. Utilisé pour l'échange de données de court-circuit selon la norme CEI 60909 Valeur par défaut : 0  - `ratedMechanicalPower`: Puissance mécanique nominale (Pr dans la norme CEI 60909-0). Utilisée pour l'échange de données en court-circuit conformément à la norme IEC 60909. Valeur par défaut : 0,0  - `reversible`: Indique pour les moteurs d'entraînement des convertisseurs si la puissance peut être réversible. Utilisé pour l'échange de données en cas de court-circuit conformément à la norme CEI 60909 Défaut : Faux :  - `rxLockedRotorRatio`: Rapport de rotor bloqué (R/X). Utilisé pour l'échange de données en cas de court-circuit selon la norme IEC 60909 Valeur par défaut : 0,0  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `type`: Type NGSI. Il doit être de type AsynchronousMachine    
Propriétés requises  
Ce modèle de données est une conversion directe du modèle commun d'information (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un mauvais type. C'est le cas, pelase soulever un problème ou envoyer un mail à alberto.abella@fiware.org  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AsynchronousMachine:    
  description: 'Adapted from CIM data models. A rotating machine whose shaft rotates asynchronously with the electrical field.  Also known as an induction machine with no external connection to the rotor windings, e.g squirrel-cage induction machine.'    
  properties:    
    AsynchronousMachineDynamics:    
      description: 'Asynchronous machine dynamics model used to describe dynamic behavior of this asynchronous machine. Default: None'    
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
    asynchronousMachineType:    
      description: 'Indicates the type of Asynchronous Machine (motor or generator). Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    converterFedDrive:    
      description: 'Indicates whether the machine is a converter fed drive. Used for short circuit data exchange according to IEC 60909 Default: False'    
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
    efficiency:    
      description: 'Efficiency of the asynchronous machine at nominal operation in percent. Indicator for converter drive motors. Used for short circuit data exchange according to IEC 60909 Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    iaIrRatio:    
      description: 'Ratio of locked-rotor current to the rated current of the motor (Ia/Ir). Used for short circuit data exchange according to IEC 60909 Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &asynchronousmachine_-_properties_-_owner_-_items_-_anyof    
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
    nominalFrequency:    
      description: 'Nameplate data indicates if the machine is 50 or 60 Hz. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    nominalSpeed:    
      description: 'Nameplate data.  Depends on the slip and number of pole pairs. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *asynchronousmachine_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    polePairNumber:    
      description: 'Number of pole pairs of stator. Used for short circuit data exchange according to IEC 60909 Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ratedMechanicalPower:    
      description: 'Rated mechanical power (Pr in the IEC 60909-0). Used for short circuit data exchange according to IEC 60909. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    reversible:    
      description: 'Indicates for converter drive motors if the power can be reversible. Used for short circuit data exchange according to IEC 60909 Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rxLockedRotorRatio:    
      description: 'Locked rotor ratio (R/X). Used for short circuit data exchange according to IEC 60909 Default: 0.0'    
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
      description: 'NGSI type. It has to be AsynchronousMachine'    
      enum:    
        - AsynchronousMachine    
      type: Property    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'une AsynchronousMachine au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'une AsynchronousMachine en format JSON comme normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'une AsynchronousMachine au format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'une AsynchronousMachine en format JSON-LD comme normalisé. Il est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
