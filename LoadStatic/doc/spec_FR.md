Entité : LoadStatic  
===================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/LoadStatic/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Adapté des modèles de données CIM. Modèle général de charge statique représentant la sensibilité de la puissance réelle et réactive consommée par la charge à l'amplitude et à la fréquence de la tension du bus**.  

## Liste des propriétés  

- `LoadAggregate`: Charge agrégée à laquelle appartient cette charge statique agrégée. Valeur par défaut : Aucun  - `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `ep1`: Exposant de tension du premier terme pour la puissance active (Ep1).  Utilisé uniquement lorsque .staticLoadModelType = exponentiel. Valeur par défaut : 0,0  - `ep2`: Exposant de tension du second terme pour la puissance active (Ep2).  Utilisé uniquement lorsque .staticLoadModelType = exponentiel. Valeur par défaut : 0,0  - `ep3`: Exposant de tension du troisième terme pour la puissance active (Ep3).  Utilisé uniquement lorsque .staticLoadModelType = exponentiel. Valeur par défaut : 0,0  - `eq1`: Exposant de tension du premier terme pour la puissance réactive (Eq1).  Utilisé uniquement lorsque .staticLoadModelType = exponentiel. Valeur par défaut : 0,0  - `eq2`: Exposant de tension du second terme pour la puissance réactive (Eq2).  Utilisé uniquement lorsque .staticLoadModelType = exponentiel. Valeur par défaut : 0,0  - `eq3`: Exposant de tension du troisième terme pour la puissance réactive (Eq3).  Utilisé uniquement lorsque .staticLoadModelType = exponentiel. Valeur par défaut : 0,0  - `id`: Identifiant unique de l'entité  - `kp1`: Coefficient de tension de premier terme pour la puissance active (Kp1).  Non utilisé lorsque .staticLoadModelType = constantZ. Valeur par défaut : 0,0  - `kp2`: Coefficient de tension de second terme pour la puissance active (Kp2).  Non utilisé lorsque .staticLoadModelType = constantZ. Valeur par défaut : 0,0  - `kp3`: Coefficient de tension de troisième terme pour la puissance active (Kp3).  Non utilisé lorsque .staticLoadModelType = constantZ. Valeur par défaut : 0,0  - `kp4`: Coefficient de fréquence pour la puissance active (Kp4).  Doit être différent de zéro lorsque .staticLoadModelType = ZIP2.  Non utilisé pour toutes les autres valeurs de .staticLoadModelType. Valeur par défaut : 0,0  - `kpf`: Coefficient de déviation de fréquence pour la puissance active (Kpf).  Non utilisé lorsque .staticLoadModelType = constantZ. Valeur par défaut : 0,0  - `kq1`: Coefficient de tension de premier terme pour la puissance réactive (Kq1).  Non utilisé lorsque .staticLoadModelType = constantZ. Valeur par défaut : 0,0  - `kq2`: Coefficient de tension de second terme pour la puissance réactive (Kq2).  Non utilisé lorsque .staticLoadModelType = constantZ. Valeur par défaut : 0,0  - `kq3`: Coefficient de tension de troisième terme pour la puissance réactive (Kq3).  Non utilisé lorsque .staticLoadModelType = constantZ. Valeur par défaut : 0,0  - `kq4`: Coefficient de fréquence pour la puissance réactive (Kq4).  Doit être différent de zéro lorsque .staticLoadModelType = ZIP2.  Non utilisé pour toutes les autres valeurs de .staticLoadModelType. Valeur par défaut : 0,0  - `kqf`: Coefficient de déviation de fréquence pour la puissance réactive (Kqf).  Non utilisé lorsque .staticLoadModelType = constantZ. Valeur par défaut : 0,0  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `staticLoadModelType`: Type de modèle de charge statique.  Valeur typique = constantZ. Valeur par défaut : Aucun  - `type`: Type de NGSI. Il doit être LoadStatic    
Propriétés requises  
Adapté de CIM data models and CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Ce modèle de données est une conversion directe du modèle d'information commun (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un mauvais type. Si tel était le cas, veuillez soulever un problème ou envoyer un courrier à info@smartdatamodels.org.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
LoadStatic:    
  description: 'Adapted from CIM data models. General static load model representing the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage.'    
  properties:    
    LoadAggregate:    
      description: 'Aggregate load to which this aggregate static load belongs. Default: None'    
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
    ep1:    
      description: 'First term voltage exponent for active power (Ep1).  Used only when .staticLoadModelType = exponential. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ep2:    
      description: 'Second term voltage exponent for active power (Ep2).  Used only when .staticLoadModelType = exponential. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ep3:    
      description: 'Third term voltage exponent for active power (Ep3).  Used only when .staticLoadModelType = exponential. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    eq1:    
      description: 'First term voltage exponent for reactive power (Eq1).  Used only when .staticLoadModelType = exponential. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    eq2:    
      description: 'Second term voltage exponent for reactive power (Eq2).  Used only when .staticLoadModelType = exponential. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    eq3:    
      description: 'Third term voltage exponent for reactive power (Eq3).  Used only when .staticLoadModelType = exponential. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &loadstatic_-_properties_-_owner_-_items_-_anyof    
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
    kp1:    
      description: 'First term voltage coefficient for active power (Kp1).  Not used when .staticLoadModelType = constantZ. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kp2:    
      description: 'Second term voltage coefficient for active power (Kp2).  Not used when .staticLoadModelType = constantZ. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kp3:    
      description: 'Third term voltage coefficient for active power (Kp3).  Not used when .staticLoadModelType = constantZ. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kp4:    
      description: 'Frequency coefficient for active power (Kp4).  Must be non-zero when .staticLoadModelType = ZIP2.  Not used for all other values of .staticLoadModelType. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kpf:    
      description: 'Frequency deviation coefficient for active power (Kpf).  Not used when .staticLoadModelType = constantZ. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kq1:    
      description: 'First term voltage coefficient for reactive power (Kq1).  Not used when .staticLoadModelType = constantZ. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kq2:    
      description: 'Second term voltage coefficient for reactive power (Kq2).  Not used when .staticLoadModelType = constantZ. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kq3:    
      description: 'Third term voltage coefficient for reactive power (Kq3).  Not used when .staticLoadModelType = constantZ. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kq4:    
      description: 'Frequency coefficient for reactive power (Kq4).  Must be non-zero when .staticLoadModelType = ZIP2.  Not used for all other values of .staticLoadModelType. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kqf:    
      description: 'Frequency deviation coefficient for reactive power (Kqf).  Not used when .staticLoadModelType = constantZ. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
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
      type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *loadstatic_-_properties_-_owner_-_items_-_anyof    
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
    staticLoadModelType:    
      description: 'Type of static load model.  Typical Value = constantZ. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be LoadStatic'    
      enum:    
        - LoadStatic    
      type: Property    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un LoadStatic au format JSON-LD comme key-values. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un LoadStatic au format JSON-LD tel que normalisé. Ceci est compatible avec NGSI-v2 lorsqu'on n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un LoadStatic au format JSON-LD comme key-values. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un LoadStatic au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
