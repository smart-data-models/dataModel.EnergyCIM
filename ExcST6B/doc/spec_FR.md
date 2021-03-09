Entité : ExcST6B  
================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExcST6B/LICENSE.md)  
Description globale : **Adapté des modèles de données CIM. Système d'excitation statique IEEE ST6B modifié avec contrôleur PID et boucle de rétroaction interne en option.**  

## Liste des biens  

- `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `ilr`: Référence de la limite de courant de sortie de l'excitateur (Ilr).  Valeur typique = 4,164. Valeur par défaut : 0,0  - `k1`: Sélecteur (K1). true = le retour est de Ifd false = le retour n'est pas de Ifd. Valeur typique = vrai. Valeur par défaut : False  - `kcl`: Réglage de la limite de courant de sortie de l'excitateur (Kcl).  Valeur typique = 1,0577. Valeur par défaut : 0,0  - `kff`: Constante de gain de pré-commande du régulateur de champ de la boucle interne (Kff).  Valeur typique = 1. Valeur par défaut : 0,0  - `kg`: Constante de gain de rétroaction du régulateur de champ de la boucle interne (Kg).  Valeur typique = 1. Valeur par défaut : 0,0  - `kia`: Gain intégral du régulateur de tension (Kia).  Valeur typique = 45,094. Valeur par défaut : 0,0  - `klr`: Réglage de la limite de courant de sortie de l'excitateur (Kcl).  Valeur typique = 17,33. Valeur par défaut : 0,0  - `km`: Constante de gain avant du régulateur de champ de la boucle intérieure (Km).  Valeur typique = 1. Valeur par défaut : 0,0  - `kpa`: Gain proportionnel du régulateur de tension (Kpa).  Valeur typique = 18,038. Valeur par défaut : 0,0  - `kvd`: Gain dérivé du régulateur de tension (Kvd).  Valeur typique = 0, par défaut : 0,0  - `location`:   - `name`: Le nom de cet article.  - `oelin`: Sélecteur d'entrée OEL (OELin). Valeur typique = aucune entrée OEL. Valeur par défaut : Aucune  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `tg`: Constante de temps de rétroaction du régulateur de tension du champ de la boucle interne (Tg).  Valeur typique = 0,02. Valeur par défaut : 0  - `ts`: Constante de temps d'allumage du redresseur (Ts).  Valeur typique = 0, par défaut : 0  - `tvd`: Gain dérivé du régulateur de tension (Tvd).  Valeur typique = 0, par défaut : 0  - `type`: Type NGSI. Il doit être de type ExcST6B  - `vamax`: Sortie maximale du régulateur de tension (Vamax).  Valeur typique = 4,81. Valeur par défaut : 0,0  - `vamin`: Sortie minimale du régulateur de tension (Vamin).  Valeur typique = -3,85. Valeur par défaut : 0,0  - `vilim`: Sélecteur (Vilim). true = le limiteur Vimin-Vimax est actif false = le limiteur Vimin-Vimax n'est pas actif. Valeur typique = vrai. Valeur par défaut : False  - `vimax`: Limite maximale d'entrée du régulateur de tension (Vimax).  Valeur typique = 10. Valeur par défaut : 0,0  - `vimin`: Limite minimale d'entrée du régulateur de tension (Vimin).  Valeur typique = -10. Valeur par défaut : 0,0  - `vmult`: Sélecteur (Vmult). true = multiplier la sortie du régulateur par la tension aux bornes false = ne pas multiplier la sortie du régulateur par la tension aux bornes.  Valeur typique = vrai. Par défaut : False  - `vrmax`: Sortie maximale du régulateur de tension (Vrmax).  Valeur typique = 4,81. Valeur par défaut : 0,0  - `vrmin`: Sortie minimale du régulateur de tension (Vrmin).  Valeur typique = -3,85. Valeur par défaut : 0,0  - `xc`: Réactivité de la source d'excitation (Xc).  Valeur typique = 0,05. Valeur par défaut : 0,0    
Propriétés requises  
Ce modèle de données est une conversion directe du modèle commun d'information (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un mauvais type. C'est le cas, pelase soulever un problème ou envoyer un mail à alberto.abella@fiware.org  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ExcST6B:    
  description: 'Adapted from CIM data models. Modified IEEE ST6B static excitation system with PID controller and optional inner feedbacks loop.'    
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
    id:    
      anyOf: &excst6b_-_properties_-_owner_-_items_-_anyof    
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
    ilr:    
      description: 'Exciter output current limit reference (Ilr).  Typical Value = 4.164. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    k1:    
      description: 'Selector (K1). true = feedback is from Ifd false = feedback is not from Ifd. Typical Value = true. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kcl:    
      description: 'Exciter output current limit adjustment (Kcl).  Typical Value = 1.0577. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kff:    
      description: 'Pre-control gain constant of the inner loop field regulator (Kff).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kg:    
      description: 'Feedback gain constant of the inner loop field regulator (Kg).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kia:    
      description: 'Voltage regulator integral gain (Kia).  Typical Value = 45.094. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    klr:    
      description: 'Exciter output current limit adjustment (Kcl).  Typical Value = 17.33. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    km:    
      description: 'Forward gain constant of the inner loop field regulator (Km).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kpa:    
      description: 'Voltage regulator proportional gain (Kpa).  Typical Value = 18.038. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kvd:    
      description: 'Voltage regulator derivative gain (Kvd).  Typical Value = 0. Default: 0.0'    
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
    oelin:    
      description: 'OEL input selector (OELin). Typical Value = noOELinput. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *excst6b_-_properties_-_owner_-_items_-_anyof    
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
    tg:    
      description: 'Feedback time constant of inner loop field voltage regulator (Tg).  Typical Value = 0.02. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ts:    
      description: 'Rectifier firing time constant (Ts).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tvd:    
      description: 'Voltage regulator derivative gain (Tvd).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be ExcST6B'    
      enum:    
        - ExcST6B    
      type: Property    
    vamax:    
      description: 'Maximum voltage regulator output (Vamax).  Typical Value = 4.81. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vamin:    
      description: 'Minimum voltage regulator output (Vamin).  Typical Value = -3.85. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vilim:    
      description: 'Selector (Vilim). true = Vimin-Vimax limiter is active false = Vimin-Vimax limiter is not active. Typical Value = true. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vimax:    
      description: 'Maximum voltage regulator input limit (Vimax).  Typical Value = 10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vimin:    
      description: 'Minimum voltage regulator input limit (Vimin).  Typical Value = -10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vmult:    
      description: 'Selector (Vmult). true = multiply regulator output by terminal voltage false = do not multiply regulator output by terminal voltage.  Typical Value = true. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vrmax:    
      description: 'Maximum voltage regulator output (Vrmax).  Typical Value = 4.81. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vrmin:    
      description: 'Minimum voltage regulator output (Vrmin).  Typical Value = -3.85. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    xc:    
      description: 'Excitation source reactance (Xc).  Typical Value = 0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un ExcST6B au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsque l'on utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un ExcST6B en format JSON comme normalisé. Ce format est compatible avec la version 2 de l'INSG lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un ExcST6B au format JSON-LD comme valeurs clés. Il est compatible avec le format JSON-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un ExcST6B au format JSON-LD comme normalisé. Il est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
