Entité : ExcBBC  
===============  
[Licence ouverte](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExcBBC/LICENSE.md)  
Description globale : **Adapté des modèles de données CIM. Système d'excitation statique alimenté par transformateur (statique avec régulateur ABB). Ce modèle représente un système d'excitation statique dans lequel un pont de thyristors à grille alimenté par un transformateur aux bornes du générateur principal alimente directement le générateur principal.**  

## Liste des biens  

- `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `efdmax`: Tension maximale de l'excitateur en circuit ouvert (Efdmax).  Valeur typique = 5. Valeur par défaut : 0,0  - `efdmin`: Tension minimale de l'excitateur en circuit ouvert (Efdmin).  Valeur typique = -5. Valeur par défaut : 0,0  - `id`: Identifiant unique de l'entité  - `k`: Gain d'état stable (K).  Valeur typique = 300. Valeur par défaut : 0,0  - `location`:   - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `switch`: Sélecteur d'acheminement du signal supplémentaire (commutateur). true = Vs connecté au 3ème point de sommation false = Vs connecté au 1er point de sommation (voir schéma). Valeur typique = vrai. Valeur par défaut : False  - `t1`: Constante de temps du contrôleur (T1).  Valeur typique = 6. Valeur par défaut : 0  - `t2`: Constante de temps du contrôleur (T2).  Valeur typique = 1. Valeur par défaut : 0  - `t3`: Constante de temps plomb/retard (T3).  Valeur typique = 0,05. Valeur par défaut : 0  - `t4`: Constante de temps plomb/retard (T4).  Valeur typique = 0,01. Valeur par défaut : 0  - `type`: Type NGSI. Il doit être de type ExcBBC  - `vrmax`: Sortie maximale de l'élément de commande (Vrmax).  Valeur typique = 5. Valeur par défaut : 0,0  - `vrmin`: Sortie minimale de l'élément de contrôle (Vrmin).  Valeur typique = -5. Valeur par défaut : 0.0  - `xe`: Réactance effective du transformateur d'excitation (Xe).  Valeur typique = 0,05. Valeur par défaut : 0,0    
Propriétés requises  
Ce modèle de données est une conversion directe du modèle commun d'information (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un mauvais type. C'est le cas, pelase soulever un problème ou envoyer un mail à alberto.abella@fiware.org  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ExcBBC:    
  description: 'Adapted from CIM data models. Transformer fed static excitation system (static with ABB regulator). This model represents a static excitation system in which a gated thyristor bridge fed by a transformer at the main generator terminals feeds the main generator directly.'    
  properties:    
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
    efdmax:    
      description: 'Maximum open circuit exciter voltage (Efdmax).  Typical Value = 5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    efdmin:    
      description: 'Minimum open circuit exciter voltage (Efdmin).  Typical Value = -5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &excbbc_-_properties_-_owner_-_items_-_anyof    
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
    k:    
      description: 'Steady state gain (K).  Typical Value = 300. Default: 0.0'    
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
        anyOf: *excbbc_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
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
    switch:    
      description: 'Supplementary signal routing selector (switch). true = Vs connected to 3rd summing point false =  Vs connected to 1st summing point (see diagram). Typical Value = true. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t1:    
      description: 'Controller time constant (T1).  Typical Value = 6. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t2:    
      description: 'Controller time constant (T2).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t3:    
      description: 'Lead/lag time constant (T3).  Typical Value = 0.05. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t4:    
      description: 'Lead/lag time constant (T4).  Typical Value = 0.01. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be ExcBBC'    
      enum:    
        - ExcBBC    
      type: Property    
    vrmax:    
      description: 'Maximum control element output (Vrmax).  Typical Value = 5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vrmin:    
      description: 'Minimum control element output (Vrmin).  Typical Value = -5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    xe:    
      description: 'Effective excitation transformer reactance (Xe).  Typical Value = 0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un ExcBBC en format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un ExcBBC en format JSON comme normalisé. Il est compatible avec la version 2 du NGSI lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un ExcBBC en format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un ExcBBC en format JSON-LD comme normalisé. Il est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
