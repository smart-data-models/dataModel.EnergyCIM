Entité : RemoteInputSignal  
==========================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/RemoteInputSignal/LICENSE.md)  
Description globale : **Adapté des modèles de données CIM. Supporte la connexion à un terminal associé à un bus distant d'où provient un signal d'entrée d'un type spécifique.**  

## Liste des propriétés  

- `DiscontinuousExcitationControlDynamics`: Modèle de commande d'excitation discontinue utilisant ce signal d'entrée à distance. Par défaut : Aucun  - `PFVArControllerType1Dynamics`: Modèle de contrôleur de facteur de puissance ou de VAr de type I utilisant ce signal d'entrée à distance. Par défaut : Aucun  - `PowerSystemStabilizerDynamics`: Modèle de stabilisateur de système d'alimentation utilisant ce signal d'entrée à distance. Par défaut : Aucun  - `Terminal`: Terminal distant auquel ce signal d'entrée est associé. Valeur par défaut : Aucun  - `UnderexcitationLimiterDynamics`: Modèle de limiteur de sous-excitation utilisant ce signal d'entrée à distance. Par défaut : Aucun  - `VoltageCompensatorDynamics`: Modèle de compensateur de tension utilisant ce signal d'entrée à distance. Par défaut : Aucun  - `WindPlantDynamics`: Le signal distant auquel cette centrale est associée. Par défaut : Aucun  - `WindTurbineType1or2Dynamics`: Modèle d'éolienne Type 1 ou Type 2 utilisant ce signal d'entrée à distance. Valeur par défaut : Aucun  - `WindTurbineType3or4Dynamics`: Signal d'entrée à distance utilisé par ces modèles d'éoliennes de type 3 ou 4. Valeur par défaut : Aucun  - `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `location`:   - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `remoteSignalType`: Type de signal d'entrée. Par défaut : Aucun  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type`: Type de NGSI. Il doit s'agir de RemoteInputSignal.    
Propriétés requises  
Ce modèle de données est une conversion directe du modèle d'information commun (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un type incorrect. Si tel était le cas, veuillez soulever un problème ou envoyer un message à alberto.abella@fiware.org.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
RemoteInputSignal:    
  description: 'Adapted from CIM data models. Supports connection to a terminal associated with a remote bus from which an input signal of a specific type is coming.'    
  properties:    
    DiscontinuousExcitationControlDynamics:    
      description: 'Discontinuous excitation control model using this remote input signal. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    PFVArControllerType1Dynamics:    
      description: 'Power Factor or VAr controller Type I model using this remote input signal. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    PowerSystemStabilizerDynamics:    
      description: 'Power system stabilizer model using this remote input signal. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    Terminal:    
      description: 'Remote terminal with which this input signal is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    UnderexcitationLimiterDynamics:    
      description: 'Underexcitation limiter model using this remote input signal. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    VoltageCompensatorDynamics:    
      description: 'Voltage compensator model using this remote input signal. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    WindPlantDynamics:    
      description: 'The remote signal with which this power plant is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    WindTurbineType1or2Dynamics:    
      description: 'Wind generator Type 1 or Type 2 model using this remote input signal. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    WindTurbineType3or4Dynamics:    
      description: 'Remote input signal used by these wind turbine Type 3 or 4 models. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/areaServed'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
    id:    
      anyOf: &remoteinputsignal_-_properties_-_owner_-_items_-_anyof    
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
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *remoteinputsignal_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    remoteSignalType:    
      description: 'Type of input signal. Default: None'    
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
      description: 'NGSI type. It has to be RemoteInputSignal'    
      enum:    
        - RemoteInputSignal    
      type: Property    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un RemoteInputSignal au format JSON comme valeurs-clés. Ceci est compatible avec NGSI V2 en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un RemoteInputSignal au format JSON tel que normalisé. Ceci est compatible avec NGSI V2 lorsqu'on n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un RemoteInputSignal au format JSON-LD en tant que key-values. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un RemoteInputSignal au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
