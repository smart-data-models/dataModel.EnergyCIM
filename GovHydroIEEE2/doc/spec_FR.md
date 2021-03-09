Entité : GovHydroIEEE2  
======================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovHydroIEEE2/LICENSE.md)  
Description globale : **Adapté des modèles de données CIM. Le modèle de régulateur de turbine hydraulique de l'IEEE représente les centrales avec des configurations simples de conduites forcées et des régulateurs de points d'écoulement hydrauliques.  Réf**  

## Liste des biens  

- `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `aturb`: Multiplicateur du numérateur de la turbine (Aturb).  Valeur typique = -1. Valeur par défaut : 0,0  - `bturb`: Multiplicateur du dénominateur de la turbine (Bturb).  Valeur typique = 0,5. Valeur par défaut : 0,0  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `gv1`: Gain non linéaire point 1, PU gv (Gv1).  Valeur typique = 0, par défaut : 0,0  - `gv2`: Gain non linéaire point 2, PU gv (Gv2).  Valeur typique = 0, par défaut : 0,0  - `gv3`: Gain non linéaire point 3, PU gv (Gv3).  Valeur typique = 0, par défaut : 0,0  - `gv4`: Gain non linéaire point 4, PU gv (Gv4).  Valeur typique = 0, par défaut : 0,0  - `gv5`: Gain non linéaire point 5, PU gv (Gv5).  Valeur typique = 0, par défaut : 0,0  - `gv6`: Gain non linéaire point 6, PU gv (Gv6).  Valeur typique = 0, par défaut : 0,0  - `id`: Identifiant unique de l'entité  - `kturb`: Gain de la turbine (Kturb).  Valeur typique = 1. Valeur par défaut : 0,0  - `location`:   - `mwbase`: Base pour les valeurs de puissance (MWbase) (> 0).  Unité = MW. Valeur par défaut : 0,0  - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `pgv1`: Gain non linéaire point 1, puissance PU (Pgv1).  Valeur typique = 0, par défaut : 0,0  - `pgv2`: Gain non linéaire point 2, puissance PU (Pgv2).  Valeur typique = 0, par défaut : 0,0  - `pgv3`: Gain non linéaire point 3, puissance PU (Pgv3).  Valeur typique = 0, par défaut : 0,0  - `pgv4`: Gain non linéaire point 4, puissance PU (Pgv4).  Valeur typique = 0, par défaut : 0,0  - `pgv5`: Gain non linéaire point 5, puissance PU (Pgv5).  Valeur typique = 0, par défaut : 0,0  - `pgv6`: Gain non linéaire point 6, puissance PU (Pgv6).  Valeur typique = 0, par défaut : 0,0  - `pmax`: Ouverture maximale des portes (Pmax).  Valeur typique = 1. Valeur par défaut : 0,0  - `pmin`: Ouverture minimale de la porte (Pmin).  Valeur typique = 0, par défaut : 0,0  - `rperm`: Chute permanente (Rperm).  Valeur typique = 0,05. Valeur par défaut : 0.0  - `rtemp`: Abattement temporaire (Rtemp).  Valeur typique = 0,5. Valeur par défaut : 0,0  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `tg`: Constante de temps de l'asservissement de la porte (Tg).  Valeur typique = 0,5. Valeur par défaut : 0  - `tp`: Constante de temps de la servovanne du pilote (Tp).  Valeur typique = 0,03. Valeur par défaut : 0  - `tr`: Constante de temps du Dashpot (Tr).  Valeur typique = 12. Valeur par défaut : 0  - `tw`: Constante de temps de l'inertie de l'eau (Tw).  Valeur typique = 2. Valeur par défaut : 0  - `type`: Type NGSI. Il doit être de type GovHydroIEEE2  - `uc`: Vitesse maximale de fermeture de la porte (Uc) (<0).  Valeur typique = -0,1. Valeur par défaut : 0,0  - `uo`: Vitesse maximale d'ouverture de la porte (Uo). Unité = PU/sec.  Valeur typique = 0,1. Valeur par défaut : 0,0    
Propriétés requises  
Ce modèle de données est une conversion directe du modèle commun d'information (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un mauvais type. C'est le cas, pelase soulever un problème ou envoyer un mail à alberto.abella@fiware.org  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GovHydroIEEE2:    
  description: 'Adapted from CIM data models. IEEE hydro turbine governor model represents plants with straightforward penstock configurations and hydraulic-dashpot governors.  Ref'    
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
    aturb:    
      description: 'Turbine numerator multiplier (Aturb).  Typical Value = -1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    bturb:    
      description: 'Turbine denominator multiplier (Bturb).  Typical Value = 0.5. Default: 0.0'    
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
    gv1:    
      description: 'Nonlinear gain point 1, PU gv (Gv1).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv2:    
      description: 'Nonlinear gain point 2, PU gv (Gv2).  Typical Value = 0. Default: 0.0'    
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
      anyOf: &govhydroieee2_-_properties_-_owner_-_items_-_anyof    
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
    kturb:    
      description: 'Turbine gain (Kturb).  Typical Value = 1. Default: 0.0'    
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
        anyOf: *govhydroieee2_-_properties_-_owner_-_items_-_anyof    
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
    pmax:    
      description: 'Maximum gate opening (Pmax).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmin:    
      description: 'Minimum gate opening (Pmin).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rperm:    
      description: 'Permanent droop (Rperm).  Typical Value = 0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rtemp:    
      description: 'Temporary droop (Rtemp).  Typical Value = 0.5. Default: 0.0'    
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
    tg:    
      description: 'Gate servo time constant (Tg).  Typical Value = 0.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tp:    
      description: 'Pilot servo valve time constant (Tp).  Typical Value = 0.03. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tr:    
      description: 'Dashpot time constant (Tr).  Typical Value = 12. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tw:    
      description: 'Water inertia time constant (Tw).  Typical Value = 2. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be GovHydroIEEE2'    
      enum:    
        - GovHydroIEEE2    
      type: Property    
    uc:    
      description: 'Maximum gate closing velocity (Uc) (<0).  Typical Value = -0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    uo:    
      description: 'Maximum gate opening velocity (Uo). Unit = PU/sec.  Typical Value = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un GovHydroIEEE2 au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un GovHydroIEEE2 au format JSON tel que normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un GovHydroIEEE2 en format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un GovHydroIEEE2 au format JSON-LD tel que normalisé. Il est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
