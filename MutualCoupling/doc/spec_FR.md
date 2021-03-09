Entité : MutualCoupling  
=======================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/MutualCoupling/LICENSE.md)  
Description globale : **Adapté des modèles de données CIM. Cette classe représente le couplage mutuel des lignes de séquence zéro.**  

## Liste des biens  

- `First_Terminal`: La borne de départ pour le calcul des distances le long de la première branche du couplage mutuel.  Normalement, le couplage mutuel ne devrait être utilisé que pour les bornes des segments de ligne CA.  Les première et deuxième bornes d'un couplage mutuel doivent pointer vers des segments de ligne CA différents. Par défaut : Aucune  - `Second_Terminal`: La borne de départ pour le calcul des distances le long de la deuxième branche du couplage mutuel. Par défaut : Aucune  - `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `b0ch`: Susceptance de shunt (charge) de couplage mutuel de séquence zéro, uniformément répartie, de toute la section de ligne. Valeur par défaut : 0,0  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `distance11`: Distance au début de la région couplée par rapport au terminal de la première ligne dont le numéro de séquence est égal à 1. Valeur par défaut : 0.0  - `distance12`: Distance à l'extrémité de la région couplée par rapport au terminal de la première ligne avec un numéro de séquence égal à 1. Valeur par défaut : 0.0  - `distance21`: Distance du début de la région couplée par rapport au terminal de la deuxième ligne avec un numéro de séquence égal à 1. Valeur par défaut : 0.0  - `distance22`: Distance à la fin de la région couplée par rapport au terminal de la deuxième ligne avec un numéro de séquence égal à 1. Valeur par défaut : 0.0  - `g0ch`: Conductance de shunt (charge) de couplage mutuel de séquence zéro, uniformément répartie, de toute la section de ligne. Valeur par défaut : 0,0  - `id`: Identifiant unique de l'entité  - `location`:   - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `r0`: Couplage d'impédance mutuelle de branche à branche de séquence zéro, résistance. Valeur par défaut : 0,0  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `type`: Type NGSI. Il doit être de type MutualCoupling  - `x0`: Couplage d'impédance mutuelle de branche à branche de séquence zéro, réactance. Valeur par défaut : 0,0    
Propriétés requises  
Ce modèle de données est une conversion directe du modèle commun d'information (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un mauvais type. C'est le cas, pelase soulever un problème ou envoyer un mail à alberto.abella@fiware.org  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
MutualCoupling:    
  description: 'Adapted from CIM data models. This class represents the zero sequence line mutual coupling.'    
  properties:    
    First_Terminal:    
      description: 'The starting terminal for the calculation of distances along the first branch of the mutual coupling.  Normally MutualCoupling would only be used for terminals of AC line segments.  The first and second terminals of a mutual coupling should point to different AC line segments. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    Second_Terminal:    
      description: 'The starting terminal for the calculation of distances along the second branch of the mutual coupling. Default: None'    
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
    b0ch:    
      description: 'Zero sequence mutual coupling shunt (charging) susceptance, uniformly distributed, of the entire line section. Default: 0.0'    
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
    distance11:    
      description: 'Distance to the start of the coupled region from the first line`s terminal having sequence number equal to 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    distance12:    
      description: 'Distance to the end of the coupled region from the first line`s terminal with sequence number equal to 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    distance21:    
      description: 'Distance to the start of coupled region from the second line`s terminal with sequence number equal to 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    distance22:    
      description: 'Distance to the end of coupled region from the second line`s terminal with sequence number equal to 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    g0ch:    
      description: 'Zero sequence mutual coupling shunt (charging) conductance, uniformly distributed, of the entire line section. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &mutualcoupling_-_properties_-_owner_-_items_-_anyof    
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
        anyOf: *mutualcoupling_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    r0:    
      description: 'Zero sequence branch-to-branch mutual impedance coupling, resistance. Default: 0.0'    
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
      description: 'NGSI type. It has to be MutualCoupling'    
      enum:    
        - MutualCoupling    
      type: Property    
    x0:    
      description: 'Zero sequence branch-to-branch mutual impedance coupling, reactance. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un MutualCoupling en format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un MutualCoupling en format JSON comme normalisé. Il est compatible avec la version 2 du NGSI lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un MutualCoupling en format JSON-LD comme valeurs clés. Il est compatible avec le format JSON-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un MutualCoupling en format JSON-LD comme normalisé. Il est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
