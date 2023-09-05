<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : ExcAC8B  
================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExcAC8B/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Adapté des modèles de données CIM. Système d'excitation redresseur modifié IEEE AC8B alimenté par un alternateur avec entrée de vitesse et limiteur d'entrée**.  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.    
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `id[*]`: Identifiant unique de l'entité  - `inlim[number]`: Indicateur de limiteur d'entrée. true = le limiteur d'entrée Vimax et Vimin est pris en compte false = le limiteur d'entrée Vimax et Vimin n'est pas pris en compte. Valeur typique = vrai. Valeur par défaut : Faux  . Model: [https://schema.org/Number](https://schema.org/Number)- `ka[number]`: Gain du régulateur de tension (Ka).  Valeur typique = 1. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kc[number]`: Facteur de charge du redresseur proportionnel à la réactance de commutation (Kc). Valeur typique = 0,55. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kd[number]`: Facteur de démagnétisation, fonction des réactances de l'excitateur et de l'alternateur (Kd).  Valeur typique = 1,1. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kdr[number]`: Gain dérivé du régulateur de tension (Kdr).  Valeur typique = 10. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ke[number]`: Constante de l'excitateur liée au champ auto-excité (Ke).  Valeur typique = 1. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kir[number]`: Gain intégral du régulateur de tension (Kir).  Valeur typique = 5. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kpr[number]`: Gain proportionnel du régulateur de tension (Kpr).  Valeur typique = 80. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ks[number]`: Coefficient permettant d'utiliser différemment le coefficient de vitesse du modèle (Ks).  Valeur typique = 0. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `pidlim[number]`: Indicateur de limiteur PID. true = le limiteur d'entrée Vpidmax et Vpidmin est pris en compte false = le limiteur d'entrée Vpidmax et Vpidmin n'est pas pris en compte. Valeur typique = true. Valeur par défaut : Faux  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `seve1[number]`: Valeur de la fonction de saturation de l'excitateur à la tension correspondante de l'excitateur, Ve, en arrière de la réactance de commutation (Se[Ve1]).  Valeur typique = 0,3. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seve2[number]`: Valeur de la fonction de saturation de l'excitateur à la tension correspondante de l'excitateur, Ve, en arrière de la réactance de commutation (Se[Ve2]).  Valeur typique = 3. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `ta[number]`: Constante de temps du régulateur de tension (Ta).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tdr[number]`: Constante de temps de retard (Tdr).  Valeur typique = 0,1. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `te[number]`: Constante de temps de l'excitateur, taux d'intégration associé à la commande de l'excitateur (Te).  Valeur typique = 1,2. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `telim[number]`: Sélecteur pour le limiteur du bloc [1/sTe].  Voir le diagramme pour la signification de true et false. Valeur typique = false. Valeur par défaut : Faux  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Type NGSI. Il doit s'agir de ExcAC8B  - `ve1[number]`: Les tensions de sortie de l'alternateur excitateur en arrière de la réactance de commutation à laquelle la saturation est définie (Ve) est égale à V (Ve1).  Valeur typique = 6,5. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ve2[number]`: Tensions de sortie de l'alternateur de l'excitatrice en arrière de la réactance de commutation à laquelle la saturation est définie (Ve).  Valeur typique = 9. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vemin[number]`: Tension minimale de sortie de l'excitateur (Vemin).  Valeur typique = 0. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vfemax[number]`: Référence de la limite de courant de l'excitateur (Vfemax).  Valeur typique = 6. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vimax[number]`: Signal d'entrée maximum (Vimax).  Valeur typique = 35. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vimin[number]`: Signal d'entrée minimum (Vimin).  Valeur typique = -10. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vpidmax[number]`: Sortie maximale du régulateur PID (Vpidmax).  Valeur typique = 35. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vpidmin[number]`: Sortie minimale du contrôleur PID (Vpidmin).  Valeur typique = -10. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vrmax[number]`: Sortie maximale du régulateur de tension (Vrmax). Valeur typique = 35. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vrmin[number]`: Sortie minimale du régulateur de tension (Vrmin).  Valeur typique = 0. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vtmult[number]`: Indicateur de multiplication par la tension terminale du générateur. true = les limites Vrmax et Vrmin sont multipliées par la tension terminale du générateur pour représenter un étage de puissance à thyristor alimenté par les bornes du générateur false = les limites ne sont pas multipliées par la tension terminale du générateur.  Valeur typique = false. Valeur par défaut : Faux  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
<!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Adapté des modèles de données CIM et de CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Ce modèle de données est une conversion directe du modèle d'information commun (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par les entités suivantes : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un type erroné. Si c'est le cas, veuillez soulever un problème ou envoyer un courrier à info@smartdatamodels.org.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ExcAC8B:    
  description: Adapted from CIM data models. Modified IEEE AC8B alternator-supplied rectifier excitation system with speed input and input limiter.    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    inlim:    
      description: 'Input limiter indicator. true = input limiter Vimax and Vimin is considered false = input limiter Vimax and Vimin is not considered. Typical Value = true. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ka:    
      description: 'Voltage regulator gain (Ka).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kc:    
      description: 'Rectifier loading factor proportional to commutating reactance (Kc). Typical Value = 0.55. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kd:    
      description: 'Demagnetizing factor, a function of exciter alternator reactances (Kd).  Typical Value = 1.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kdr:    
      description: 'Voltage regulator derivative gain (Kdr).  Typical Value = 10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ke:    
      description: 'Exciter constant related to self-excited field (Ke).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kir:    
      description: 'Voltage regulator integral gain (Kir).  Typical Value = 5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kpr:    
      description: 'Voltage regulator proportional gain (Kpr).  Typical Value = 80. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ks:    
      description: 'Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
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
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
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
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
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
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
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
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    pidlim:    
      description: 'PID limiter indicator. true = input limiter Vpidmax and Vpidmin is considered false = input limiter Vpidmax and Vpidmin is not considered. Typical Value = true. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    seve1:    
      description: 'Exciter saturation function value at the corresponding exciter voltage, Ve, back of commutating reactance (Se[Ve1]).  Typical Value = 0.3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    seve2:    
      description: 'Exciter saturation function value at the corresponding exciter voltage, Ve, back of commutating reactance (Se[Ve2]).  Typical Value = 3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    ta:    
      description: 'Voltage regulator time constant (Ta).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tdr:    
      description: 'Lag time constant (Tdr).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    te:    
      description: 'Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 1.2. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    telim:    
      description: 'Selector for the limiter on the block [1/sTe].  See diagram for meaning of true and false. Typical Value = false. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: NGSI type. It has to be ExcAC8B    
      enum:    
        - ExcAC8B    
      type: string    
      x-ngsi:    
        type: Property    
    ve1:    
      description: 'Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve) equals V (Ve1).  Typical Value = 6.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ve2:    
      description: 'Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve).  Typical Value = 9. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vemin:    
      description: 'Minimum exciter voltage output (Vemin).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vfemax:    
      description: 'Exciter field current limit reference (Vfemax).  Typical Value = 6. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vimax:    
      description: 'Input signal maximum (Vimax).  Typical Value = 35. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vimin:    
      description: 'Input signal minimum (Vimin).  Typical Value = -10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vpidmax:    
      description: 'PID maximum controller output (Vpidmax).  Typical Value = 35. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vpidmin:    
      description: 'PID minimum controller output (Vpidmin).  Typical Value = -10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vrmax:    
      description: 'Maximum voltage regulator output (Vrmax). Typical Value = 35. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vrmin:    
      description: 'Minimum voltage regulator output (Vrmin).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vtmult:    
      description: 'Multiply by generator`s terminal voltage indicator. true =the limits Vrmax and Vrmin are multiplied by the generator`s terminal voltage to represent a thyristor power stage fed from the generator terminals false = limits are not multiplied by generator`s terminal voltage.  Typical Value = false. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcAC8B/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/ExcAC8B/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
Non disponible l'exemple d'une ExcAC8B en format JSON-LD comme valeurs de clé. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un ExcAC8B au format JSON-LD tel que normalisé. Ce format est compatible avec l'INSG-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'une ExcAC8B au format JSON-LD en tant que valeurs-clé. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un ExcAC8B au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
