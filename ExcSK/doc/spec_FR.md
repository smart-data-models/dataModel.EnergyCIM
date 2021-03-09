Entité : ExcSK  
==============  
[Licence ouverte](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExcSK/LICENSE.md)  
Description globale : **Adapté des modèles de données CIM. Modèle de système d'excitation slovaque.  La LIE et le contrôle de la tension secondaire sont inclus dans ce modèle. Lorsque ce modèle est utilisé, il ne peut y avoir de modèle séparé de limiteur de sous-excitation ou de contrôleur de VAR.**  

## Liste des biens  

- `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `efdmax`: Limite d'écrêtage de la tension de champ (Efdmax). Valeur par défaut : 0,0  - `efdmin`: Limite d'écrêtage de la tension de champ (Efdmin). Valeur par défaut : 0.0  - `emax`: Tension de champ maximale de sortie (Emax).  Valeur typique = 20. Valeur par défaut : 0,0  - `emin`: Sortie de tension de champ minimale (Emin).  Valeur typique = -20. Valeur par défaut : 0,0  - `id`: Identifiant unique de l'entité  - `k`: Gain (K).  Valeur typique = 1. Valeur par défaut : 0,0  - `k1`: Paramètre de la limite de sous-excitation (K1).  Valeur typique = 0,1364. Valeur par défaut : 0.0  - `k2`: Paramètre de la limite de sous-excitation (K2).  Valeur typique = -0,3861. Valeur par défaut : 0,0  - `kc`: Gain du contrôleur PI (Kc).  Valeur typique = 70. Valeur par défaut : 0.0  - `kce`: Facteur de régulation du correcteur (Kce).  Valeur typique = 0, par défaut : 0,0  - `kd`: Réaction interne de l'excitateur (Kd).  Valeur typique = 0, par défaut : 0,0  - `kgob`: Gain du contrôleur P (Kgob).  Valeur typique = 10. Valeur par défaut : 0,0  - `kp`: Gain du contrôleur PI (Kp).  Valeur typique = 1. Valeur par défaut : 0.0  - `kqi`: Gain du contrôleur PI de la composante intégrale (Kqi).  Valeur typique = 0, par défaut : 0,0  - `kqob`: Taux d'augmentation de la puissance réactive (Kqob). Valeur par défaut : 0,0  - `kqp`: Gain du contrôleur PI (Kqp).  Valeur typique = 0, par défaut : 0,0  - `location`:   - `name`: Le nom de cet article.  - `nq`: Zone morte de la puissance réactive (nq).  Détermine la plage de sensibilité.  Valeur typique = 0,001. Valeur par défaut : 0,0  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `qconoff`: État du contrôle de la tension secondaire (Qc_on_off). true = le contrôle de la tension secondaire est ON false = le contrôle de la tension secondaire est OFF. Valeur typique = faux. Valeur par défaut : False  - `qz`: Valeur désirée (consigne) de la puissance réactive, réglage manuel (Qz). Valeur par défaut : 0,0  - `remote`: Sélecteur pour appliquer le calcul automatique dans le modèle de contrôleur secondaire. true = le calcul automatique est activé false = le réglage manuel est actif ; l'utilisation de la valeur souhaitée de la puissance réactive (Qz) est nécessaire. Valeur typique = vrai. Par défaut : False  - `sbase`: Puissance apparente de l'unité (Sbase).  Unité = MVA.  Valeur typique = 259. Valeur par défaut : 0,0  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `tc`: Constante de temps d'avance de phase du contrôleur PI (Tc).  Valeur typique = 8. Valeur par défaut : 0  - `te`: Constante de temps du bloc de gain (Te).  Valeur typique = 0,1. Valeur par défaut : 0  - `ti`: Constante de temps d'avance de phase du contrôleur PI (Ti).  Valeur typique = 2. Valeur par défaut : 0  - `tp`: Constante de temps (Tp).  Valeur typique = 0,1. Valeur par défaut : 0  - `tr`: Constante de temps du transducteur de tension (Tr).  Valeur typique = 0,01. Valeur par défaut : 0  - `type`: Type NGSI. Il doit être de type ExcSK  - `uimax`: Erreur maximale (Uimax).  Valeur typique = 10. Valeur par défaut : 0,0  - `uimin`: Erreur minimale (UImin).  Valeur typique = -10. Valeur par défaut : 0,0  - `urmax`: Sortie maximale du contrôleur (URmax).  Valeur typique = 10. Valeur par défaut : 0,0  - `urmin`: Sortie minimale du contrôleur (URmin).  Valeur typique = -10. Valeur par défaut : 0.0  - `vtmax`: Tension d'entrée maximale aux bornes (Vtmax).  Détermine la plage de la zone morte de tension.  Valeur typique = 1,05. Valeur par défaut : 0,0  - `vtmin`: Tension d'entrée minimale aux bornes (Vtmin).  Détermine la plage de la zone morte de tension.  Valeur typique = 0,95. Valeur par défaut : 0,0  - `yp`: Sortie maximale (Yp).  Sortie minimale = 0. Valeur typique = 1. Valeur par défaut : 0.0    
Propriétés requises  
Ce modèle de données est une conversion directe du modèle commun d'information (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un mauvais type. C'est le cas, pelase soulever un problème ou envoyer un mail à alberto.abella@fiware.org  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ExcSK:    
  description: 'Adapted from CIM data models. Slovakian Excitation System Model.  UEL and secondary voltage control are included in this model. When this model is used, there cannot be a separate underexcitation limiter or VAr controller model.'    
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
      description: 'Field voltage clipping limit (Efdmax). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    efdmin:    
      description: 'Field voltage clipping limit (Efdmin). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    emax:    
      description: 'Maximum field voltage output (Emax).  Typical Value = 20. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    emin:    
      description: 'Minimum field voltage output (Emin).  Typical Value = -20. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &excsk_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Gain (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    k1:    
      description: 'Parameter of underexcitation limit (K1).  Typical Value = 0.1364. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    k2:    
      description: 'Parameter of underexcitation limit (K2).  Typical Value = -0.3861. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kc:    
      description: 'PI controller gain (Kc).  Typical Value = 70. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kce:    
      description: 'Rectifier regulation factor (Kce).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kd:    
      description: 'Exciter internal reactance (Kd).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kgob:    
      description: 'P controller gain (Kgob).  Typical Value = 10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kp:    
      description: 'PI controller gain (Kp).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kqi:    
      description: 'PI controller gain of integral component (Kqi).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kqob:    
      description: 'Rate of rise of the reactive power (Kqob). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kqp:    
      description: 'PI controller gain (Kqp).  Typical Value = 0. Default: 0.0'    
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
    nq:    
      description: 'Dead band of reactive power (nq).  Determines the range of sensitivity.  Typical Value = 0.001. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *excsk_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    qconoff:    
      description: 'Secondary voltage control state (Qc_on_off). true = secondary voltage control is ON false = secondary voltage control is OFF. Typical Value = false. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    qz:    
      description: 'Desired value (setpoint) of reactive power, manual setting (Qz). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    remote:    
      description: 'Selector to apply automatic calculation in secondary controller model. true = automatic calculation is activated false = manual set is active; the use of desired value of reactive power (Qz) is required. Typical Value = true. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    sbase:    
      description: 'Apparent power of the unit (Sbase).  Unit = MVA.  Typical Value = 259. Default: 0.0'    
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
    tc:    
      description: 'PI controller phase lead time constant (Tc).  Typical Value = 8. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    te:    
      description: 'Time constant of gain block (Te).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ti:    
      description: 'PI controller phase lead time constant (Ti).  Typical Value = 2. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tp:    
      description: 'Time constant (Tp).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tr:    
      description: 'Voltage transducer time constant (Tr).  Typical Value = 0.01. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be ExcSK'    
      enum:    
        - ExcSK    
      type: Property    
    uimax:    
      description: 'Maximum error (Uimax).  Typical Value = 10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    uimin:    
      description: 'Minimum error (UImin).  Typical Value = -10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    urmax:    
      description: 'Maximum controller output (URmax).  Typical Value = 10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    urmin:    
      description: 'Minimum controller output (URmin).  Typical Value = -10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vtmax:    
      description: 'Maximum terminal voltage input (Vtmax).  Determines the range of voltage dead band.  Typical Value = 1.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vtmin:    
      description: 'Minimum terminal voltage input (Vtmin).  Determines the range of voltage dead band.  Typical Value = 0.95. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    yp:    
      description: 'Maximum output (Yp).  Minimum output = 0.  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un ExcSK en format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un ExcSK en format JSON comme normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un ExcSK en format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un ExcSK en format JSON-LD comme normalisé. Il est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
