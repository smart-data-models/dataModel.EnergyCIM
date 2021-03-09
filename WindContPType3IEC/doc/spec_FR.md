Entité : WindContPType3IEC  
==========================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/WindContPType3IEC/LICENSE.md)  
Description globale : **Adapté des modèles de données CIM. Modèle de contrôle P de type 3.  Référence : Norme CEI 61400-27-1, section 6.6.5.3.**  

## Liste des biens  

- `WindDynamicsLookupTable`: Le modèle de contrôle P de type 3 auquel est associée cette table de recherche sur la dynamique du vent. Par défaut : "list".  - `WindGenTurbineType3IEC`: Modèle d'éolienne de type 3 auquel est associé ce modèle de contrôle du vent P de type 3. Par défaut : Aucun  - `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `dpmax`: Taux de rampe de puissance maximale des éoliennes (). Il s'agit d'un paramètre dépendant du projet. Valeur par défaut : 0.0  - `dtrisemaxlvrt`: Limitation du taux d'augmentation du couple pendant la TRMV pour S (d). Il s'agit d'un paramètre dépendant du projet. Valeur par défaut : 0,0  - `id`: Identifiant unique de l'entité  - `kdtd`: Gain pour l'amortissement actif du groupe motopropulseur (). Il s'agit d'un paramètre dépendant du type. Valeur par défaut : 0.0  - `kip`: Paramètre d'intégration du contrôleur PI (). Il s'agit d'un paramètre dépendant du type. Valeur par défaut : 0.0  - `kpp`: Gain proportionnel du contrôleur PI (). Il s'agit d'un paramètre dépendant du type. Valeur par défaut : 0.0  - `location`:   - `mplvrt`: Activer le mode de contrôle de la puissance de la LVRT (M vrai = 1 : contrôle de la tension faux = 0 : contrôle de la puissance réactive.  Il s'agit d'un paramètre dépendant du projet. Par défaut : False  - `name`: Le nom de cet article.  - `omegaoffset`: Décalage par rapport à la valeur de référence qui limite l'action du contrôleur lors des changements de vitesse du rotor (oméga). Il s'agit d'un paramètre dépendant du cas. Valeur par défaut : 0.0  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `pdtdmax`: Puissance maximale d'amortissement active du groupe motopropulseur (). Il s'agit d'un paramètre dépendant du type. Valeur par défaut : 0.0  - `rramp`: Limitation du couple de la rampe, requise dans certains codes de grille (). Il s'agit d'un paramètre dépendant du projet. Valeur par défaut : 0.0  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `tdvs`: Délai après les chutes de tension profondes (T). Il s'agit d'un paramètre dépendant du projet. Valeur par défaut : 0  - `temin`: Couple minimum du générateur électrique (). Il s'agit d'un paramètre dépendant du type. Valeur par défaut : 0.0  - `tomegafilt`: Constante de temps du filtre pour la mesure de la vitesse du générateur (). Il s'agit d'un paramètre dépendant du type. Valeur par défaut : 0  - `tpfilt`: Constante de temps du filtre pour la mesure de la puissance (). Il s'agit d'un paramètre dépendant du type. Valeur par défaut : 0  - `tpord`: Constante de temps dans le décalage de l'ordre de puissance (). Il s'agit d'un paramètre dépendant du type. Valeur par défaut : 0.0  - `tufilt`: Constante de temps du filtre pour la mesure de la tension (). Il s'agit d'un paramètre dépendant du type. Valeur par défaut : 0  - `tuscale`: Facteur d'échelle de tension du couple de réenclenchement (T). Il s'agit d'un paramètre dépendant du projet. Valeur par défaut : 0,0  - `twref`: Constante de temps dans le filtre de référence de vitesse (). Il s'agit d'un paramètre dépendant du type. Valeur par défaut : 0  - `type`: Type NGSI. Il doit être de type WindContPType3IEC  - `udvs`: Limite de tension pour le maintien du statut de LVRT après des chutes de tension importantes (). Il s'agit d'un paramètre dépendant du projet. Valeur par défaut : 0,0  - `updip`: Seuil de chute de tension pour la commande P ().  Partie de la régulation de la turbine, souvent différente (par exemple 0,8) des seuils du convertisseur. Il s'agit d'un paramètre dépendant du projet. Valeur par défaut : 0,0  - `wdtd`: Fréquence d'amortissement active du groupe motopropulseur (oméga). Elle peut être calculée à partir de deux paramètres du modèle de masse. Il s'agit d'un paramètre dépendant du type. Valeur par défaut : 0.0  - `zeta`: Coefficient d'amortissement actif du groupe motopropulseur (zeta). Il s'agit d'un paramètre dépendant du type. Valeur par défaut : 0.0    
Propriétés requises  
Ce modèle de données est une conversion directe du modèle commun d'information (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un mauvais type. C'est le cas, pelase soulever un problème ou envoyer un mail à alberto.abella@fiware.org  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WindContPType3IEC:    
  description: 'Adapted from CIM data models. P control model Type 3.  Reference: IEC Standard 61400-27-1 Section 6.6.5.3.'    
  properties:    
    WindDynamicsLookupTable:    
      description: 'The P control type 3 model with which this wind dynamics lookup table is associated. Default: "list"'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    WindGenTurbineType3IEC:    
      description: 'Wind turbine type 3 model with which this Wind control P type 3 model is associated. Default: None'    
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
    dpmax:    
      description: 'Maximum wind turbine power ramp rate (). It is project dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    dtrisemaxlvrt:    
      description: 'Limitation of torque rise rate during LVRT for S (d). It is project dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &windcontptype3iec_-_properties_-_owner_-_items_-_anyof    
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
    kdtd:    
      description: 'Gain for active drive train damping (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kip:    
      description: 'PI controller integration parameter (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kpp:    
      description: 'PI controller proportional gain (). It is type dependent parameter. Default: 0.0'    
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
    mplvrt:    
      description: 'Enable LVRT power control mode (M true = 1: voltage control false = 0: reactive power control.  It is project dependent parameter. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    name:    
      description: 'The name of this item.'    
      type: Property    
    omegaoffset:    
      description: 'Offset to reference value that limits controller action during rotor speed changes (omega). It is case dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *windcontptype3iec_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    pdtdmax:    
      description: 'Maximum active drive train damping power (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rramp:    
      description: 'Ramp limitation of torque, required in some grid codes (). It is project dependent parameter. Default: 0.0'    
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
    tdvs:    
      description: 'Timedelay after deep voltage sags (T). It is project dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    temin:    
      description: 'Minimum electrical generator torque (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tomegafilt:    
      description: 'Filter time constant for generator speed measurement (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tpfilt:    
      description: 'Filter time constant for power measurement (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tpord:    
      description: 'Time constant in power order lag (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tufilt:    
      description: 'Filter time constant for voltage measurement (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tuscale:    
      description: 'Voltage scaling factor of reset-torque (T). It is project dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    twref:    
      description: 'Time constant in speed reference filter (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be WindContPType3IEC'    
      enum:    
        - WindContPType3IEC    
      type: Property    
    udvs:    
      description: 'Voltage limit for hold LVRT status after deep voltage sags (). It is project dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    updip:    
      description: 'Voltage dip threshold for P-control ().  Part of turbine control, often different (e.g 0.8) from converter thresholds. It is project dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    wdtd:    
      description: 'Active drive train damping frequency (omega). It can be calculated from two mass model parameters. It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    zeta:    
      description: 'Coefficient for active drive train damping (zeta). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un WindContPType3IEC en format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un WindContPType3IEC en format JSON comme normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un WindContPType3IEC en format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un WindContPType3IEC en format JSON-LD comme normalisé. Il est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
