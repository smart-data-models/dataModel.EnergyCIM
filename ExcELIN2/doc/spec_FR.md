Entité : ExcELIN2  
=================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExcELIN2/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Adapté des modèles de données du CIM. Modèle détaillé du système d'excitation - ELIN (VATECH).  Ce modèle représente un système d'excitation entièrement statique. Un contrôleur de tension PI établit un point de consigne de courant de champ souhaité pour un contrôleur de courant proportionnel. L'intégrateur du contrôleur PI a une entrée de suivi pour adapter son signal au courant d'excitation actuel.  Modèles de stabilisateurs de système d'alimentation utilisés en conjonction avec ce modèle de système d'excitation : PssELIN2, PssIEEE2B, Pss2B.**  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `efdbas`: Gain (Efdbas).  Valeur typique = 0.1. Valeur par défaut : 0.0  - `id`: Identifiant unique de l'entité  - `iefmax`: Limiteur (Iefmax).  Valeur typique = 1. Valeur par défaut : 0.0  - `iefmax2`: Tension minimale d'excitation en circuit ouvert (Iefmax2).  Valeur typique = -5. Valeur par défaut : 0.0  - `iefmin`: Limiteur (Iefmin).  Valeur typique = 1. Valeur par défaut : 0.0  - `k1`: Gain d'entrée du régulateur de tension (K1).  Valeur typique = 0. Valeur par défaut : 0.0  - `k1ec`: Limite d'entrée du régulateur de tension (K1ec).  Valeur typique = 2. Valeur par défaut : 0.0  - `k2`: Gain (K2).  Valeur typique = 5. Valeur par défaut : 0.0  - `k3`: Gain (K3).  Valeur typique = 0.1. Valeur par défaut : 0.0  - `k4`: Gain (K4).  Valeur typique = 0. Valeur par défaut : 0.0  - `kd1`: Gain dérivé du contrôleur de tension (Kd1).  Valeur typique = 34.5. Valeur par défaut : 0.0  - `ke2`: Gain (Ke2).  Valeur typique = 0.1. Valeur par défaut : 0.0  - `ketb`: Gain (Ketb).  Valeur typique = 0.06. Valeur par défaut : 0.0  - `location`:   - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `pid1max`: Gain de suivi du contrôleur (PID1max).  Valeur typique = 2. Valeur par défaut : 0.0  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `seve1`: Valeur de la fonction de saturation de l'excitatrice à la tension d'excitation correspondante, Ve1, en arrière de la réactance de commutation (Se[Ve1]).  Valeur typique = 0. Valeur par défaut : 0.0  - `seve2`: Valeur de la fonction de saturation de l'excitatrice à la tension correspondante de l'excitatrice, Ve2, en arrière de la réactance de commutation (Se[Ve2]).  Valeur typique = 1. Valeur par défaut : 0.0  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `tb1`: Constante de temps du lavage de la dérivation du contrôleur de tension (Tb1).  Valeur typique = 12,45. Valeur par défaut : 0  - `te`: Constante de temps (Te).  Valeur typique = 0. Valeur par défaut : 0  - `te2`: Constante de temps (Te2).  Valeur typique = 1. Valeur par défaut : 0  - `ti1`: Bande morte de suivi du contrôleur (Ti1).  Valeur typique = 0. Valeur par défaut : 0.0  - `ti3`: Constante de temps (Ti3).  Valeur typique = 3. Valeur par défaut : 0  - `ti4`: Constante de temps (Ti4).  Valeur typique = 0. Valeur par défaut : 0  - `tr4`: Constante de temps (Tr4).  Valeur typique = 1. Valeur par défaut : 0  - `type`: Type NGSI. Il faut que ce soit ExcELIN2  - `upmax`: Limiteur (Upmax).  Valeur typique = 3. Valeur par défaut : 0.0  - `upmin`: Limiteur (Upmin).  Valeur typique = 0. Par défaut : 0.0  - `ve1`: Tensions de sortie de l'alternateur d'excitation en arrière de la réactance de commutation à laquelle la saturation est définie (Ve1).  Valeur typique = 3. Valeur par défaut : 0.0  - `ve2`: Tensions de sortie de l'alternateur d'excitation en arrière de la réactance de commutation à laquelle la saturation est définie (Ve2).  Valeur typique = 0. Valeur par défaut : 0.0  - `xp`: Réactance effective du transformateur d'excitation (Xp).  Valeur typique = 1. Valeur par défaut : 0.0    
Propriétés requises  
Adapté de CIM data models and CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Ce modèle de données est une conversion directe du modèle d'information commun (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un mauvais type. Si tel était le cas, veuillez soulever un problème ou envoyer un courrier à info@smartdatamodels.org.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ExcELIN2:    
  description: 'Adapted from CIM data models. Detailed Excitation System Model - ELIN (VATECH).  This model represents an all-static excitation system. A PI voltage controller establishes a desired field current set point for a proportional current controller. The integrator of the PI controller has a follow-up input to match its signal to the present field current.  Power system stabilizer models used in conjunction with this excitation system model: PssELIN2, PssIEEE2B, Pss2B.'    
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
    efdbas:    
      description: 'Gain (Efdbas).  Typical Value = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &excelin2_-_properties_-_owner_-_items_-_anyof    
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
    iefmax:    
      description: 'Limiter (Iefmax).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    iefmax2:    
      description: 'Minimum open circuit excitation voltage (Iefmax2).  Typical Value = -5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    iefmin:    
      description: 'Limiter (Iefmin).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    k1:    
      description: 'Voltage regulator input gain (K1).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    k1ec:    
      description: 'Voltage regulator input limit (K1ec).  Typical Value = 2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    k2:    
      description: 'Gain (K2).  Typical Value = 5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    k3:    
      description: 'Gain (K3).  Typical Value = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    k4:    
      description: 'Gain (K4).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kd1:    
      description: 'Voltage controller derivative gain (Kd1).  Typical Value = 34.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ke2:    
      description: 'Gain (Ke2).  Typical Value = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ketb:    
      description: 'Gain (Ketb).  Typical Value = 0.06. Default: 0.0'    
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
        anyOf: *excelin2_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    pid1max:    
      description: 'Controller follow up gain (PID1max).  Typical Value = 2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    seve1:    
      description: 'Exciter saturation function value at the corresponding exciter voltage, Ve1, back of commutating reactance (Se[Ve1]).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    seve2:    
      description: 'Exciter saturation function value at the corresponding exciter voltage, Ve2, back of commutating reactance (Se[Ve2]).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    tb1:    
      description: 'Voltage controller derivative washout time constant (Tb1).  Typical Value = 12.45. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    te:    
      description: 'Time constant (Te).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    te2:    
      description: 'Time Constant (Te2).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ti1:    
      description: 'Controller follow up dead band (Ti1).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ti3:    
      description: 'Time constant (Ti3).  Typical Value = 3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ti4:    
      description: 'Time constant (Ti4).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tr4:    
      description: 'Time constant (Tr4).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be ExcELIN2'    
      enum:    
        - ExcELIN2    
      type: Property    
    upmax:    
      description: 'Limiter (Upmax).  Typical Value = 3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    upmin:    
      description: 'Limiter (Upmin).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ve1:    
      description: 'Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1).  Typical Value = 3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ve2:    
      description: 'Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve2).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    xp:    
      description: 'Excitation transformer effective reactance (Xp).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un ExcELIN2 au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-v2 en utilisant `options=keyValues` et retourne les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un ExcELIN2 au format JSON-LD tel que normalisé. Ceci est compatible avec NGSI-v2 lorsqu'on n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un ExcELIN2 au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et retourne les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un ExcELIN2 au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
