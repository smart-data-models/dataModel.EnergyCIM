Entité : TurbLCFB1  
==================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/TurbLCFB1/LICENSE.md)  
Description globale : **Adapté des modèles de données du CIM. Modèle de contrôleur de charge de turbine développé dans le WECC.  Ce modèle représente un contrôleur de charge de turbine de supervision qui agit pour maintenir la puissance de la turbine à une valeur définie par un ajustement continu de la référence vitesse-charge du régulateur de turbine. Ce modèle est destiné à représenter les contrôleurs à réinitialisation lente de la "boucle extérieure" qui gèrent l'action du régulateur de turbine.  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `db`: Bande morte du contrôleur (db).  Valeur typique = 0. Valeur par défaut : 0.0  - `description`: Une description de cet article  - `emax`: Erreur de contrôle maximale (Emax) (note 4).  Valeur typique = 0,02. Valeur par défaut : 0,0  - `fb`: Gain du biais de fréquence (Fb).  Valeur typique = 0. Valeur par défaut : 0.0  - `fbf`: Indicateur de biais de fréquence (Fbf). true = activer le biais de fréquence false = désactiver le biais de fréquence. Valeur typique = false. Valeur par défaut : False  - `id`: Identifiant unique de l'entité  - `irmax`: Biais de référence maximum de la vitesse/charge de la turbine (Irmax) (note 3).  Valeur typique = 0. Valeur par défaut : 0.0  - `ki`: Gain intégral (Ki).  Valeur typique = 0. Valeur par défaut : 0.0  - `kp`: Gain proportionnel (Kp).  Valeur typique = 0. Valeur par défaut : 0.0  - `location`:   - `mwbase`: Base pour les valeurs de puissance (MWbase) (>0).  Unité = MW. Valeur par défaut : 0.0  - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `pbf`: Drapeau du contrôleur de charge (Pbf). true = activer le contrôleur de charge false = désactiver le contrôleur de charge. Valeur typique = false. Valeur par défaut : False  - `pmwset`: Point de consigne du régulateur de puissance (Pmwset) (note 1).  Unité = MW. Valeur typique = 0. Valeur par défaut : 0.0  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `speedReferenceGovernor`: Type de référence du régulateur de turbine (Type). true = régulateur de référence de vitesse false = régulateur de référence de charge. Valeur typique = true. Valeur par défaut : False  - `tpelec`: Constante de temps du transducteur de puissance (Tpelec).  Valeur typique = 0. Valeur par défaut : 0  - `type`: Type de NGSI. Il doit s'agir de TurbLCFB1.    
Propriétés requises  
Ce modèle de données est une conversion directe du modèle d'information commun (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un type incorrect. Si tel était le cas, veuillez soulever un problème ou envoyer un message à alberto.abella@fiware.org.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
TurbLCFB1:    
  description: 'Adapted from CIM data models. Turbine Load Controller model developed in the WECC.  This model represents a supervisory turbine load controller that acts to maintain turbine power at a set value by continuous adjustment of the turbine governor speed-load reference. This model is intended to represent slow reset ''outer loop'' controllers managing the action of the turbine governor.'    
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
    db:    
      description: 'Controller dead band (db).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    description:    
      description: 'A description of this item'    
      type: Property    
    emax:    
      description: 'Maximum control error (Emax) (note 4).  Typical Value = 0.02. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fb:    
      description: 'Frequency bias gain (Fb).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fbf:    
      description: 'Frequency bias flag (Fbf). true = enable frequency bias false = disable frequency bias. Typical Value = false. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &turblcfb1_-_properties_-_owner_-_items_-_anyof    
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
    irmax:    
      description: 'Maximum turbine speed/load reference bias (Irmax) (note 3).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ki:    
      description: 'Integral gain (Ki).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kp:    
      description: 'Proportional gain (Kp).  Typical Value = 0. Default: 0.0'    
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
    mwbase:    
      description: 'Base for power values (MWbase) (>0).  Unit = MW. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *turblcfb1_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    pbf:    
      description: 'Power controller flag (Pbf). true = enable load controller false = disable load controller. Typical Value = false. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmwset:    
      description: 'Power controller setpoint (Pmwset) (note 1).  Unit = MW. Typical Value = 0. Default: 0.0'    
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
    speedReferenceGovernor:    
      description: 'Type of turbine governor reference (Type). true = speed reference governor false = load reference governor. Typical Value = true. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tpelec:    
      description: 'Power transducer time constant (Tpelec).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be TurbLCFB1'    
      enum:    
        - TurbLCFB1    
      type: Property    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un TurbLCFB1 au format JSON comme valeurs-clés. Ceci est compatible avec NGSI V2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un TurbLCFB1 au format JSON tel que normalisé. Ceci est compatible avec la NGSI V2 lorsqu'elle n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un TurbLCFB1 au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un TurbLCFB1 au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
