Entité : GovGAST1  
=================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovGAST1/LICENSE.md)  
Description globale : **Adapté des modèles de données CIM. Turbine à gaz modifiée à arbre unique.**  

## Liste des propriétés  

- `a`: Facteur d'échelle du numérateur de la constante de temps de la puissance de la turbine (a).  Valeur typique = 0.8. Valeur par défaut : 0.0  - `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `b`: Facteur d'échelle du dénominateur de la constante de temps de la puissance de la turbine (b).  Valeur typique = 1. Valeur par défaut : 0.0  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `db1`: Largeur de la bande morte intentionnelle (db1).  Unité = Hz.  Valeur typique = 0. Valeur par défaut : 0.0  - `db2`: Bande morte involontaire (db2).  Unité = MW.  Valeur typique = 0. Valeur par défaut : 0.0  - `description`: Une description de cet article  - `eps`: Hystérésis db intentionnelle (eps).  Unité = Hz.  Valeur typique = 0. Valeur par défaut : 0.0  - `fidle`: Débit de carburant à puissance nulle (Fidle).  Valeur typique = 0.18. Valeur par défaut : 0.0  - `gv1`: Point de gain non linéaire 1, PU gv (Gv1).  Valeur typique = 0. Valeur par défaut : 0.0  - `gv2`: Point de gain non linéaire 2,PU gv (Gv2).  Valeur typique = 0. Valeur par défaut : 0.0  - `gv3`: Point de gain non linéaire 3, PU gv (Gv3).  Valeur typique = 0. Valeur par défaut : 0.0  - `gv4`: Point de gain non linéaire 4, PU gv (Gv4).  Valeur typique = 0. Valeur par défaut : 0.0  - `gv5`: Point de gain non linéaire 5, PU gv (Gv5).  Valeur typique = 0. Valeur par défaut : 0.0  - `gv6`: Point de gain non linéaire 6, PU gv (Gv6).  Valeur typique = 0. Valeur par défaut : 0.0  - `id`: Identifiant unique de l'entité  - `ka`: Gain du gouverneur (Ka).  Valeur typique = 0. Valeur par défaut : 0.0  - `kt`: Gain du limiteur de température (Kt).  Valeur typique = 3. Valeur par défaut : 0.0  - `lmax`: Limite de charge à température ambiante (Lmax).  Lmax est la puissance de sortie de la turbine correspondant à la température limite des gaz d'échappement.  Valeur typique = 1. Valeur par défaut : 0.0  - `loadinc`: Changement de position de la vanne autorisé à un rythme rapide (Loadinc).  Valeur typique = 0.05. Valeur par défaut : 0.0  - `location`:   - `ltrate`: Taux d'ouverture maximal à long terme du robinet de carburant (Ltrate).  Valeur typique = 0.02. Valeur par défaut : 0.0  - `mwbase`: Base pour les valeurs de puissance (MWbase) (> 0).  Unité = MW. Valeur par défaut : 0.0  - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `pgv1`: Point de gain non linéaire 1, puissance du PU (Pgv1).  Valeur typique = 0. Valeur par défaut : 0.0  - `pgv2`: Point de gain non linéaire 2, puissance du PU (Pgv2).  Valeur typique = 0. Valeur par défaut : 0.0  - `pgv3`: Point de gain non linéaire 3, puissance du PU (Pgv3).  Valeur typique = 0. Valeur par défaut : 0.0  - `pgv4`: Point de gain non linéaire 4, puissance du PU (Pgv4).  Valeur typique = 0. Valeur par défaut : 0.0  - `pgv5`: Point de gain non linéaire 5, puissance du PU (Pgv5).  Valeur typique = 0. Valeur par défaut : 0.0  - `pgv6`: Point de gain non linéaire 6, puissance du PU (Pgv6).  Valeur typique = 0. Valeur par défaut : 0.0  - `r`: Chute permanente (R).  Valeur typique = 0.04. Valeur par défaut : 0.0  - `rmax`: Taux d'ouverture maximal de la vanne de carburant (Rmax).  Unité = PU/sec.  Valeur typique = 1. Valeur par défaut : 0.0  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `t1`: Constante de temps du mécanisme du régulateur (T1).  T1 représente la constante de temps de positionnement naturel de la vanne du régulateur pour de petites perturbations, comme cela se produit lorsque la limitation de débit n'est pas en vigueur.  Valeur typique = 0,5. Valeur par défaut : 0  - `t2`: Constante de temps de la puissance de la turbine (T2).  T2 représente le retard dû au stockage interne de l'énergie du moteur à turbine à gaz. T2 peut être utilisée pour donner une approximation du retard associé à l'accélération de la bobine du compresseur d'un moteur à plusieurs arbres, ou à la compressibilité du gaz dans le plénum de la turbine de puissance libre d'une unité aérodérivée, par exemple.  Valeur typique = 0,5. Valeur par défaut : 0  - `t3`: Constante de temps de la température d'échappement de la turbine (T3).  T3 représente le retard du système de limitation de la température d'échappement et de la charge. Valeur typique = 3. Valeur par défaut : 0  - `t4`: Constante de temps du gouverneur (T4).  Valeur typique = 0. Valeur par défaut : 0  - `t5`: Constante de temps de retard du gouverneur (T5).  Valeur typique = 0. Valeur par défaut : 0  - `tltr`: Constante de temps de la moyenne de la position de la vanne (Tltr).  Valeur typique = 10. Valeur par défaut : 0  - `type`: Type de NGSI. Il doit s'agir de GovGAST1  - `vmax`: Puissance maximale de la turbine, PU du MWbase (Vmax).  Valeur typique = 1. Valeur par défaut : 0.0  - `vmin`: Puissance minimale de la turbine, PU de MWbase (Vmin).  Valeur typique = 0. Valeur par défaut : 0.0    
Propriétés requises  
Ce modèle de données est une conversion directe du modèle d'information commun (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un type incorrect. Si tel était le cas, veuillez soulever un problème ou envoyer un message à alberto.abella@fiware.org.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GovGAST1:    
  description: 'Adapted from CIM data models. Modified single shaft gas turbine.'    
  properties:    
    a:    
      description: 'Turbine power time constant numerator scale factor (a).  Typical Value = 0.8. Default: 0.0'    
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
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/areaServed'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/https://schema.org/postalCode'''    
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
    b:    
      description: 'Turbine power time constant denominator scale factor (b).  Typical Value = 1. Default: 0.0'    
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
    db1:    
      description: 'Intentional dead-band width (db1).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    db2:    
      description: 'Unintentional dead-band (db2).  Unit = MW.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    description:    
      description: 'A description of this item'    
      type: Property    
    eps:    
      description: 'Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fidle:    
      description: 'Fuel flow at zero power output (Fidle).  Typical Value = 0.18. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv1:    
      description: 'Nonlinear gain point 1, PU gv (Gv1).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv2:    
      description: 'Nonlinear gain point 2,PU gv (Gv2).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv3:    
      description: 'Nonlinear gain point 3, PU gv (Gv3).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv4:    
      description: 'Nonlinear gain point 4, PU gv (Gv4).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv5:    
      description: 'Nonlinear gain point 5, PU gv (Gv5).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv6:    
      description: 'Nonlinear gain point 6, PU gv (Gv6).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &govgast1_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Governor gain (Ka).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kt:    
      description: 'Temperature limiter gain (Kt).  Typical Value = 3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    lmax:    
      description: 'Ambient temperature load limit (Lmax).  Lmax is the turbine power output corresponding to the limiting exhaust gas temperature.  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    loadinc:    
      description: 'Valve position change allowed at fast rate (Loadinc).  Typical Value = 0.05. Default: 0.0'    
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
    ltrate:    
      description: 'Maximum long term fuel valve opening rate (Ltrate).  Typical Value = 0.02. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    mwbase:    
      description: 'Base for power values (MWbase) (> 0).  Unit = MW. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *govgast1_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    pgv1:    
      description: 'Nonlinear gain point 1, PU power (Pgv1).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pgv2:    
      description: 'Nonlinear gain point 2, PU power (Pgv2).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pgv3:    
      description: 'Nonlinear gain point 3, PU power (Pgv3).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pgv4:    
      description: 'Nonlinear gain point 4, PU power (Pgv4).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pgv5:    
      description: 'Nonlinear gain point 5, PU power (Pgv5).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pgv6:    
      description: 'Nonlinear gain point 6, PU power (Pgv6).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    r:    
      description: 'Permanent droop (R).  Typical Value = 0.04. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rmax:    
      description: 'Maximum fuel valve opening rate (Rmax).  Unit = PU/sec.  Typical Value = 1. Default: 0.0'    
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
    t1:    
      description: 'Governor mechanism time constant (T1).  T1 represents the natural valve positioning time constant of the governor for small disturbances, as seen when rate limiting is not in effect.  Typical Value = 0.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t2:    
      description: 'Turbine power time constant (T2).  T2 represents delay due to internal energy storage of the gas turbine engine. T2 can be used to give a rough approximation to the delay associated with acceleration of the compressor spool of a multi-shaft engine, or with the compressibility of gas in the plenum of the free power turbine of an aero-derivative unit, for example.  Typical Value = 0.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t3:    
      description: 'Turbine exhaust temperature time constant (T3).  T3 represents delay in the exhaust temperature and load limiting system. Typical Value = 3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t4:    
      description: 'Governor lead time constant (T4).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t5:    
      description: 'Governor lag time constant (T5).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tltr:    
      description: 'Valve position averaging time constant (Tltr).  Typical Value = 10. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be GovGAST1'    
      enum:    
        - GovGAST1    
      type: Property    
    vmax:    
      description: 'Maximum turbine power, PU of MWbase (Vmax).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vmin:    
      description: 'Minimum turbine power, PU of MWbase (Vmin).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un GovGAST1 au format JSON comme valeurs-clés. Ceci est compatible avec NGSI V2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un GovGAST1 au format JSON tel que normalisé. Ceci est compatible avec la NGSI V2 lorsqu'elle n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un GovGAST1 au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et retourne les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un GovGAST1 au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
