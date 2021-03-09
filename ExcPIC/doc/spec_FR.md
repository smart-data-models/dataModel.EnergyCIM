Entité : ExcPIC  
===============  
[Licence ouverte](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExcPIC/LICENSE.md)  
Description globale : **Adapté des modèles de données CIM. Modèle proportionnel/intégral du système d'excitation du régulateur.  Ce modèle peut être utilisé pour représenter les systèmes d'excitation avec un régulateur de tension proportionnel/intégral (PI).**  

## Liste des biens  

- `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `e1`: Valeur de la tension de champ 1 (E1).  Valeur typique = 0, valeur par défaut : 0,0  - `e2`: Valeur de la tension de champ 2 (E2).  Valeur typique = 0, valeur par défaut : 0,0  - `efdmax`: Limite maximale de l'excitateur (Efdmax).  Valeur typique = 8. Valeur par défaut : 0,0  - `efdmin`: Limite minimale de l'excitateur (Efdmin).  Valeur typique = -0,87. Valeur par défaut : 0,0  - `id`: Identifiant unique de l'entité  - `ka`: Gain du contrôleur PI (Ka).  Valeur typique = 3,15. Valeur par défaut : 0,0  - `kc`: Facteur de régulation de l'excitateur (Kc).  Valeur typique = 0,08. Valeur par défaut : 0,0  - `ke`: Constante d'excitation (Ke).  Valeur typique = 0, par défaut : 0,0  - `kf`: Gain de retour d'information sur les taux (Kf).  Valeur typique = 0, par défaut : 0,0  - `ki`: Gain de la source actuelle (Ki).  Valeur typique = 0, par défaut : 0,0  - `kp`: Gain potentiel de la source (Kp).  Valeur typique = 6,5. Valeur par défaut : 0,0  - `location`:   - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `se1`: Facteur de saturation à E1 (Se1).  Valeur typique = 0, par défaut : 0,0  - `se2`: Facteur de saturation à E2 (Se2).  Valeur typique = 0, par défaut : 0,0  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `ta1`: Constante de temps du contrôleur PI (Ta1).  Valeur typique = 1. Valeur par défaut : 0  - `ta2`: Constante de temps du régulateur de tension (Ta2).  Valeur typique = 0,01. Valeur par défaut : 0  - `ta3`: Constante de temps d'avance (Ta3).  Valeur typique = 0, par défaut : 0  - `ta4`: Constante de temps de retard (Ta4).  Valeur typique = 0, par défaut : 0  - `te`: Constante de temps de l'excitateur (Te).  Valeur typique = 0, par défaut : 0  - `tf1`: Constante de temps de rétroaction du taux (Tf1).  Valeur typique = 0, par défaut : 0  - `tf2`: Constante de temps de retard de la rétroaction du taux (Tf2).  Valeur typique = 0, par défaut : 0  - `type`: Type NGSI. Il doit être de type ExcPIC  - `vr1`: Limite maximale de l'IP (Vr1).  Valeur typique = 1. Valeur par défaut : 0,0  - `vr2`: Limite minimale de l'IP (Vr2).  Valeur typique = -0,87. Valeur par défaut : 0,0  - `vrmax`: Limite maximale du régulateur de tension (Vrmax).  Valeur typique = 1. Valeur par défaut : 0,0  - `vrmin`: Limite minimale du régulateur de tension (Vrmin).  Valeur typique = -0,87. Valeur par défaut : 0,0    
Propriétés requises  
Ce modèle de données est une conversion directe du modèle commun d'information (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un mauvais type. C'est le cas, pelase soulever un problème ou envoyer un mail à alberto.abella@fiware.org  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ExcPIC:    
  description: 'Adapted from CIM data models. Proportional/Integral Regulator Excitation System Model.  This model can be used to represent excitation systems with a proportional-integral (PI) voltage regulator controller.'    
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
    e1:    
      description: 'Field voltage value 1 (E1).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    e2:    
      description: 'Field voltage value 2 (E2).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    efdmax:    
      description: 'Exciter maximum limit (Efdmax).  Typical Value = 8. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    efdmin:    
      description: 'Exciter minimum limit (Efdmin).  Typical Value = -0.87. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &excpic_-_properties_-_owner_-_items_-_anyof    
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
    ka:    
      description: 'PI controller gain (Ka).  Typical Value = 3.15. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kc:    
      description: 'Exciter regulation factor (Kc).  Typical Value = 0.08. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ke:    
      description: 'Exciter constant (Ke).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kf:    
      description: 'Rate feedback gain (Kf).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ki:    
      description: 'Current source gain (Ki).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kp:    
      description: 'Potential source gain (Kp).  Typical Value = 6.5. Default: 0.0'    
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
        anyOf: *excpic_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    se1:    
      description: 'Saturation factor at E1 (Se1).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    se2:    
      description: 'Saturation factor at E2 (Se2).  Typical Value = 0. Default: 0.0'    
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
    ta1:    
      description: 'PI controller time constant (Ta1).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ta2:    
      description: 'Voltage regulator time constant (Ta2).  Typical Value = 0.01. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ta3:    
      description: 'Lead time constant (Ta3).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ta4:    
      description: 'Lag time constant (Ta4).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    te:    
      description: 'Exciter time constant (Te).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tf1:    
      description: 'Rate feedback time constant (Tf1).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tf2:    
      description: 'Rate feedback lag time constant (Tf2).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be ExcPIC'    
      enum:    
        - ExcPIC    
      type: Property    
    vr1:    
      description: 'PI maximum limit (Vr1).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vr2:    
      description: 'PI minimum limit (Vr2).  Typical Value = -0.87. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vrmax:    
      description: 'Voltage regulator maximum limit (Vrmax).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vrmin:    
      description: 'Voltage regulator minimum limit (Vrmin).  Typical Value = -0.87. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un ExcPIC en format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un ExcPIC en format JSON comme normalisé. Il est compatible avec la version 2 du NGSI lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un ExcPIC au format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un ExcPIC en format JSON-LD comme normalisé. Il est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
