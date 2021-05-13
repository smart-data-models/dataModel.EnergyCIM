Entité : ExcANS  
===============  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExcANS/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Adapté des modèles de données du CIM. Système d'excitation italien. Il représente la tension de champ statique ou le système d'excitation à retour de courant d'excitation**.  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `blint`: Drapeau de contrôle du régulateur (BLINT).  0 = régulateur plomb-lag 1 = régulateur proportionnel intégral. Valeur typique = 0. Valeur par défaut : 0  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `ifmn`: Courant minimum d'excitation (I).  Valeur typique = -5.2. Valeur par défaut : 0.0  - `ifmx`: Courant maximal de l'excitatrice (I).  Valeur typique = 6.5. Valeur par défaut : 0.0  - `k2`: Gain de l'excitateur (K).  Valeur typique = 20. Valeur par défaut : 0.0  - `k3`: Gain AVR (K).  Valeur typique = 1000. Valeur par défaut : 0.0  - `kce`: Facteur de plafond (K).  Valeur typique = 1. Valeur par défaut : 0.0  - `krvecc`: Activation de la rétroaction (K).  0 = Contrôle en boucle ouverte 1 = Contrôle en boucle fermée. Valeur typique = 1. Valeur par défaut : 0  - `kvfif`: Indicateur de signal de retour de taux (K).  0 = tension de sortie de l'excitatrice 1 = courant de champ de l'excitatrice. Valeur typique = 0. Valeur par défaut : 0  - `location`:   - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `t1`: Constante de temps (T).  Valeur typique = 20. Valeur par défaut : 0  - `t2`: Constante de temps (T).  Valeur typique = 0,05. Valeur par défaut : 0  - `t3`: Constante de temps (T).  Valeur typique = 1,6. Valeur par défaut : 0  - `tb`: Constante de temps de l'excitateur (T).  Valeur typique = 0.04. Valeur par défaut : 0  - `type`: Type NGSI. Il doit s'agir d'ExcANS  - `vrmn`: Sortie maximale de l'AVR (V).  Valeur typique = -5.2. Valeur par défaut : 0.0  - `vrmx`: Sortie minimale de l'AVR (V).  Valeur typique = 6.5. Valeur par défaut : 0.0    
Propriétés requises  
Adapté de CIM data models and CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Ce modèle de données est une conversion directe du modèle d'information commun (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un mauvais type. Si tel était le cas, veuillez soulever un problème ou envoyer un courrier à info@smartdatamodels.org.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ExcANS:    
  description: 'Adapted from CIM data models. Italian excitation system. It represents static field voltage or excitation current feedback excitation system.'    
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
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
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
    blint:    
      description: 'Governor Control Flag (BLINT).  0 = lead-lag regulator 1 = proportional integral regulator. Typical Value = 0. Default: 0'    
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
    id:    
      anyOf: &excans_-_properties_-_owner_-_items_-_anyof    
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
    ifmn:    
      description: 'Minimum exciter current (I).  Typical Value = -5.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ifmx:    
      description: 'Maximum exciter current (I).  Typical Value = 6.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    k2:    
      description: 'Exciter gain (K).  Typical Value = 20. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    k3:    
      description: 'AVR gain (K).  Typical Value = 1000. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kce:    
      description: 'Ceiling factor (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    krvecc:    
      description: 'Feedback enabling (K).  0 = Open loop control 1 = Closed loop control. Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kvfif:    
      description: 'Rate feedback signal flag (K).  0 = output voltage of the exciter 1 = exciter field current. Typical Value = 0. Default: 0'    
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
        anyOf: *excans_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    t1:    
      description: 'Time constant (T).  Typical Value = 20. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t2:    
      description: 'Time constant (T).  Typical Value = 0.05. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t3:    
      description: 'Time constant (T).  Typical Value = 1.6. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tb:    
      description: 'Exciter time constant (T).  Typical Value = 0.04. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be ExcANS'    
      enum:    
        - ExcANS    
      type: Property    
    vrmn:    
      description: 'Maximum AVR output (V).  Typical Value = -5.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vrmx:    
      description: 'Minimum AVR output (V).  Typical Value = 6.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un ExcANS au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-v2 quand on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un ExcANS au format JSON-LD tel que normalisé. Ceci est compatible avec NGSI-v2 lorsqu'on n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un ExcANS au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-LD quand on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un ExcANS au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
