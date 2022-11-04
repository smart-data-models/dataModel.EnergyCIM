Entité : GovHydro4  
==================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovHydro4/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Adapté des modèles de données CIM. Turbine hydraulique et régulateur. Représente les usines avec des configurations de conduites forcées simples et des régulateurs hydrauliques de type traditionnel "dashpot".  Ce modèle peut être utilisé pour représenter des turbines simples, Francis, Pelton ou Kaplan**.  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `at`: Gain de la turbine (At).  Valeur typique = 1.2. Valeur par défaut : 0.0  - `bgv0`: Point d'asservissement 0 de la pale Kaplan (Bgv0).  Valeur typique = 0. Valeur par défaut : 0.0  - `bgv1`: Point d'asservissement 1 de la pale Kaplan (Bgv1).  Valeur typique = 0. Valeur par défaut : 0.0  - `bgv2`: Point d'asservissement des pales Kaplan 2 (Bgv2). Valeur typique = 0. Valeur typique Francis = 0, Kaplan = 0.1. Valeur par défaut : 0.0  - `bgv3`: Point d'asservissement 3 de la pale Kaplan (Bgv3). Valeur typique = 0. Valeur typique Francis = 0, Kaplan = 0.667. Valeur par défaut : 0.0  - `bgv4`: Point d'asservissement de la pale Kaplan 4 (Bgv4).  Valeur typique = 0. Valeur typique Francis = 0, Kaplan = 0.9. Valeur par défaut : 0.0  - `bgv5`: Point d'asservissement de la pale Kaplan 5 (Bgv5). Valeur typique = 0. Valeur typique Francis = 0, Kaplan = 1. Valeur par défaut : 0.0  - `bmax`: Facteur d'ajustement maximal des pales (Bmax). Valeur typique = 0. Valeur typique Francis = 0, Kaplan = 1.1276. Valeur par défaut : 0.0  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `db1`: Largeur de la bande morte intentionnelle (db1).  Unité = Hz.  Valeur typique = 0. Valeur par défaut : 0.0  - `db2`: Bande morte involontaire (db2).  Unité = MW.  Valeur typique = 0. Valeur par défaut : 0.0  - `description`: Une description de cet article  - `dturb`: Facteur d'amortissement de la turbine (Dturb).  Unité = delta P (PU de MWbase) / delta vitesse (PU). Valeur typique = 0,5.  Valeur typique Francis = 1,1, Kaplan = 1,1. Valeur par défaut : 0.0  - `eps`: Hystérésis db intentionnelle (eps).  Unité = Hz.  Valeur typique = 0. Valeur par défaut : 0.0  - `gmax`: Ouverture maximale du portail, PU de MWbase (Gmax).  Valeur typique = 1. Valeur par défaut : 0.0  - `gmin`: Ouverture minimale du portail, PU de MWbase (Gmin).  Valeur typique = 0. Valeur par défaut : 0.0  - `gv0`: Point de gain non linéaire 0, PU gv (Gv0). Valeur typique = 0. Valeur typique Francis = 0,1, Kaplan = 0,1. Valeur par défaut : 0.0  - `gv1`: Point de gain non linéaire 1, PU gv (Gv1). Valeur typique = 0. Valeur typique Francis = 0,4, Kaplan = 0,4. Valeur par défaut : 0.0  - `gv2`: Point de gain non linéaire 2, PU gv (Gv2). Valeur typique = 0. Valeur typique Francis = 0,5, Kaplan = 0,5. Valeur par défaut : 0.0  - `gv3`: Point de gain non linéaire 3, PU gv (Gv3). Valeur typique = 0. Valeur typique Francis = 0,7, Kaplan = 0,7. Valeur par défaut : 0.0  - `gv4`: Point de gain non linéaire 4, PU gv (Gv4). Valeur typique = 0. Valeur typique Francis = 0,8, Kaplan = 0,8. Valeur par défaut : 0.0  - `gv5`: Point de gain non linéaire 5, PU gv (Gv5). Valeur typique = 0. Valeur typique Francis = 0,9, Kaplan = 0,9. Valeur par défaut : 0.0  - `hdam`: Hauteur de chute disponible au barrage (hdam).  Valeur typique = 1. Valeur par défaut : 0.0  - `id`: Identifiant unique de l'entité  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `mwbase`: Base pour les valeurs de puissance (MWbase) (>0).  Unité = MW. Valeur par défaut : 0.0  - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `pgv0`: Point de gain non linéaire 0, puissance du PU (Pgv0).  Valeur typique = 0. Valeur par défaut : 0.0  - `pgv1`: Point de gain non linéaire 1, puissance PU (Pgv1). Valeur typique = 0. Valeur typique Francis = 0.42, Kaplan = 0.35. Valeur par défaut : 0.0  - `pgv2`: Point de gain non linéaire 2, puissance PU (Pgv2). Valeur typique = 0. Valeur typique Francis = 0.56, Kaplan = 0.468. Valeur par défaut : 0.0  - `pgv3`: Point de gain non linéaire 3, puissance PU (Pgv3). Valeur typique = 0. Valeur typique Francis = 0.8, Kaplan = 0.796. Valeur par défaut : 0.0  - `pgv4`: Point de gain non linéaire 4, puissance PU (Pgv4). Valeur typique = 0. Valeur typique Francis = 0.9, Kaplan = 0.917. Valeur par défaut : 0.0  - `pgv5`: Point de gain non linéaire 5, puissance PU (Pgv5).  Valeur typique = 0. Valeur typique Francis = 0.97, Kaplan = 0.99. Valeur par défaut : 0.0  - `qn1`: Débit à vide à la hauteur de chute nominale (Qnl). Valeur typique = 0.08.  Valeur typique Francis = 0, Kaplan = 0. Valeur par défaut : 0.0  - `rperm`: Chute permanente (Rperm).  Valeur typique = 0.05. Valeur par défaut : 0  - `rtemp`: Chute temporaire (Rtemp).  Valeur typique = 0.3. Valeur par défaut : 0  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `tblade`: Constante de temps de l'asservissement de la lame (Tblade).  Valeur typique = 100. Valeur par défaut : 0  - `tg`: Constante de temps de l'asservissement de la porte (Tg) (>0).  Valeur typique = 0,5. Valeur par défaut : 0  - `tp`: Constante de temps de l'asservissement du pilote (Tp).  Valeur typique = 0,1. Valeur par défaut : 0  - `tr`: Constante de temps du Dashpot (Tr) (>0).  Valeur typique = 5. Valeur par défaut : 0  - `tw`: Constante de temps de l'inertie de l'eau (Tw) (>0).  Valeur typique = 1. Valeur par défaut : 0  - `type`: Type de NGSI. Il doit s'agir de GovHydro4.  - `uc`: Vitesse maximale de fermeture du portail (Uc).  Valeur typique = 0.2. Valeur par défaut : 0.0  - `uo`: Vitesse maximale d'ouverture du portail (Uo).  Typique Vlaue = 0.2. Valeur par défaut : 0.0    
Propriétés requises  
Adapté de CIM data models and CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Ce modèle de données est une conversion directe du modèle d'information commun (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un mauvais type. Si tel était le cas, veuillez soulever un problème ou envoyer un courrier à info@smartdatamodels.org.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GovHydro4:    
  description: 'Adapted from CIM data models. Hydro turbine and governor. Represents plants with straight-forward penstock configurations and hydraulic governors of traditional ''dashpot'' type.  This model can be used to represent simple, Francis, Pelton or Kaplan turbines.'    
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
    at:    
      description: 'Turbine gain (At).  Typical Value = 1.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    bgv0:    
      description: 'Kaplan blade servo point 0 (Bgv0).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    bgv1:    
      description: 'Kaplan blade servo point 1 (Bgv1).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    bgv2:    
      description: 'Kaplan blade servo point 2 (Bgv2). Typical Value = 0.  Typical Value Francis = 0, Kaplan = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    bgv3:    
      description: 'Kaplan blade servo point 3 (Bgv3). Typical Value = 0.  Typical Value Francis = 0, Kaplan = 0.667. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    bgv4:    
      description: 'Kaplan blade servo point 4 (Bgv4).  Typical Value = 0.  Typical Value Francis = 0, Kaplan = 0.9. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    bgv5:    
      description: 'Kaplan blade servo point 5 (Bgv5). Typical Value = 0.  Typical Value Francis = 0, Kaplan = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    bmax:    
      description: 'Maximum blade adjustment factor (Bmax). Typical Value = 0.  Typical Value Francis = 0, Kaplan = 1.1276. Default: 0.0'    
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
      description: 'Intentional deadband width (db1).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
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
    dturb:    
      description: 'Turbine damping factor (Dturb).  Unit = delta P (PU of MWbase) / delta speed (PU). Typical Value = 0.5.  Typical Value Francis = 1.1, Kaplan = 1.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    eps:    
      description: 'Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gmax:    
      description: 'Maximum gate opening, PU of MWbase (Gmax).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gmin:    
      description: 'Minimum gate opening, PU of MWbase (Gmin).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv0:    
      description: 'Nonlinear gain point 0, PU gv (Gv0). Typical Value = 0.  Typical Value Francis = 0.1, Kaplan = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv1:    
      description: 'Nonlinear gain point 1, PU gv (Gv1). Typical Value = 0.  Typical Value Francis = 0.4, Kaplan = 0.4. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv2:    
      description: 'Nonlinear gain point 2, PU gv (Gv2). Typical Value = 0.  Typical Value Francis = 0.5, Kaplan = 0.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv3:    
      description: 'Nonlinear gain point 3, PU gv (Gv3). Typical Value = 0.  Typical Value Francis = 0.7, Kaplan = 0.7. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv4:    
      description: 'Nonlinear gain point 4, PU gv (Gv4). Typical Value = 0.  Typical Value Francis = 0.8, Kaplan = 0.8. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv5:    
      description: 'Nonlinear gain point 5, PU gv (Gv5). Typical Value = 0.  Typical Value Francis = 0.9, Kaplan = 0.9. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    hdam:    
      description: 'Head available at dam (hdam).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &govhydro4_-_properties_-_owner_-_items_-_anyof    
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
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
      type: GeoProperty    
    mwbase:    
      description: 'Base for power values (MWbase) (>0).  Unit = MW. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *govhydro4_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    pgv0:    
      description: 'Nonlinear gain point 0, PU power (Pgv0).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pgv1:    
      description: 'Nonlinear gain point 1, PU power (Pgv1). Typical Value = 0.  Typical Value Francis = 0.42, Kaplan = 0.35. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pgv2:    
      description: 'Nonlinear gain point 2, PU power (Pgv2). Typical Value = 0.  Typical Value Francis = 0.56, Kaplan = 0.468. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pgv3:    
      description: 'Nonlinear gain point 3, PU power (Pgv3). Typical Value = 0.  Typical Value Francis = 0.8, Kaplan = 0.796. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pgv4:    
      description: 'Nonlinear gain point 4, PU power (Pgv4). Typical Value = 0.  Typical Value Francis = 0.9, Kaplan = 0.917. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pgv5:    
      description: 'Nonlinear gain point 5, PU power (Pgv5).  Typical Value = 0.  Typical Value Francis = 0.97, Kaplan = 0.99. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    qn1:    
      description: 'No-load flow at nominal head (Qnl). Typical Value = 0.08.  Typical Value Francis = 0, Kaplan = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rperm:    
      description: 'Permanent droop (Rperm).  Typical Value = 0.05. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rtemp:    
      description: 'Temporary droop (Rtemp).  Typical Value = 0.3. Default: 0'    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    tblade:    
      description: 'Blade servo time constant (Tblade).  Typical Value = 100. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tg:    
      description: 'Gate servo time constant (Tg) (>0).  Typical Value = 0.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tp:    
      description: 'Pilot servo time constant (Tp).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tr:    
      description: 'Dashpot time constant (Tr) (>0).  Typical Value = 5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tw:    
      description: 'Water inertia time constant (Tw) (>0).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be GovHydro4'    
      enum:    
        - GovHydro4    
      type: Property    
    uc:    
      description: 'Max gate closing velocity (Uc).  Typical Value = 0.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    uo:    
      description: 'Max gate opening velocity (Uo).  Typical Vlaue = 0.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un GovHydro4 au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-v2 en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un GovHydro4 au format JSON-LD tel que normalisé. Ceci est compatible avec la NGSI-v2 lorsqu'elle n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un GovHydro4 au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un GovHydro4 au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude