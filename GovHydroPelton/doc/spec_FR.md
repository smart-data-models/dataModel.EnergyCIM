<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : GovHydroPelton  
=======================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovHydroPelton/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Adapté des modèles de données CIM. Unité hydroélectrique détaillée - modèle Pelton.  Ce modèle peut être utilisé pour représenter la dynamique liée au tunnel d'eau et à la chambre d'équilibre. Un schéma du système hydraulique des modèles d'unités hydroélectriques détaillées, comme Francis et Pelton, se trouve dans la classe GovHydroFrancis**.  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour cet élément  - `areaServed[string]`: La zone géographique où un service ou un article offert est fourni  . Model: [https://schema.org/Text](https://schema.org/Text)- `av0[number]`: Surface du réservoir d'équilibre (A). Unité = m. Valeur typique = 30. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `av1[number]`: Surface du réservoir de compensation (A). Unité = m. Valeur typique = 700. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bp[number]`: Droop (bp).  Valeur typique = 0.05. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified[string]`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `db1[number]`: Largeur de la bande morte intentionnelle (DB1).  Unité = Hz.  Valeur typique = 0. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `db2[number]`: Largeur de la bande morte intentionnelle de l'erreur d'ouverture de la vanne (DB2). Unité = Hz.  Valeur typique = 0.01. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: Une description de cet article  - `h1[number]`: Hauteur du niveau d'eau de la chambre de compensation par rapport au niveau de la conduite forcée (H).  Unité = m. Valeur typique = 4. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `h2[number]`: Hauteur du niveau d'eau du réservoir d'équilibre par rapport au niveau de la conduite forcée (H).  Unité = m. Valeur typique = 40. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `hn[number]`: Hauteur de chute hydraulique nominale (H).  Unité = m. Valeur typique = 250. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identifiant unique de l'entité  - `kc[number]`: Coefficient de perte de la conduite forcée (due à la friction) (Kc).  Valeur typique = 0,025. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kg[number]`: Coefficient de perte du tunnel d'eau et de la chambre d'équilibre (due à la friction) (Kg).  Valeur typique = -0.025. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément.  - `owner[array]`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `qc0[number]`: Débit de la turbine à vide à la hauteur de chute nominale (Qc0).  Valeur typique = 0.05. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `qn[number]`: Débit nominal (Q). Unité = m/s. Valeur typique = 40. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires sur l'article  - `simplifiedPelton[number]`: Simulation simplifiée du modèle Pelton (Sflag). true = activation de la simulation simplifiée du modèle Pelton false = activation de la simulation complète du modèle Pelton (gain non linéaire). Valeur typique = false. Valeur par défaut : False  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `staticCompensating[number]`: Caractéristique de compensation statique (Cflag). true = activation de la caractéristique de compensation statique false = inhibition de la caractéristique de compensation statique. Valeur typique = false. Valeur par défaut : False  . Model: [https://schema.org/Number](https://schema.org/Number)- `ta[number]`: Gain dérivatif (constante de temps de l'accéléromètre) (Ta).  Valeur typique = 3. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ts[number]`: Constante de temps de l'asservissement de la porte (Ts).  Valeur typique = 0.15. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tv[number]`: Constante de temps de l'intégrateur du servomoteur (TV).  Valeur typique = 0,3. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `twnc[number]`: Constante de temps de l'inertie de l'eau (Twnc).  Valeur typique = 1. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `twng[number]`: Constante de temps d'inertie du tunnel d'eau et de la chambre d'équilibre (Twng). Valeur typique = 3. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tx[number]`: Constante de temps de l'intégrateur électronique (Tx).  Valeur typique = 0,5. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Type de NGSI. Il doit s'agir de GovHydroPelton.  - `va[number]`: Vitesse maximale d'ouverture du portail (Va).  Unité = PU/sec.  Valeur typique = 0.016. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `valvmax[number]`: Ouverture maximale du portail (ValvMax).  Valeur typique = 1. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `valvmin[number]`: Ouverture minimale du portail (ValvMin).  Valeur typique = 0. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vav[number]`: Vitesse maximale d'ouverture de la valve du servomoteur (Vav).  Valeur typique = 0.017. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vc[number]`: Vitesse maximale de fermeture du portail (Vc).  Unité = PU/sec.  Valeur typique = -0.016. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vcv[number]`: Vitesse de fermeture maximale de la valve du servomoteur (Vcv).  Valeur typique = -0.017. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `waterTunnelSurgeChamberSimulation[number]`: Simulation de tunnel d'eau et de chambre d'équilibre (Tflag). true = activer la simulation de tunnel d'eau et de chambre d'équilibre false = inhiber la simulation de tunnel d'eau et de chambre d'équilibre. Valeur typique = false. Valeur par défaut : False  . Model: [https://schema.org/Number](https://schema.org/Number)- `zsfc[number]`: Hauteur du niveau d'eau supérieur par rapport au niveau de la conduite forcée (Zsfc).  Unité = m. Valeur typique = 25. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
<!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Adapté de CIM data models and CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Ce modèle de données est une conversion directe du modèle d'information commun (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un mauvais type. Si tel était le cas, veuillez soulever un problème ou envoyer un courrier à info@smartdatamodels.org.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GovHydroPelton:    
  description: 'Adapted from CIM data models. Detailed hydro unit - Pelton model.  This model can be used to represent the dynamic related to water tunnel and surge chamber. A schematic of the hydraulic system of detailed hydro unit models, like Francis and Pelton, is located under the GovHydroFrancis class.'    
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
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    av0:    
      description: 'Area of the surge tank (A). Unit = m. Typical Value = 30. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    av1:    
      description: 'Area of the compensation tank (A). Unit = m. Typical Value = 700. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bp:    
      description: 'Droop (bp).  Typical Value = 0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    db1:    
      description: 'Intentional dead-band width (DB1).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    db2:    
      description: 'Intentional dead-band width of valve opening error (DB2). Unit = Hz.  Typical Value = 0.01. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    h1:    
      description: 'Head of compensation chamber water level with respect to the level of penstock (H).  Unit = m. Typical Value = 4. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    h2:    
      description: 'Head of surge tank water level with respect to the level of penstock (H).  Unit = m. Typical Value = 40. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    hn:    
      description: 'Rated hydraulic head (H).  Unit = m. Typical Value = 250. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &govhydropelton_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    kc:    
      description: 'Penstock loss coefficient (due to friction) (Kc).  Typical Value = 0.025. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kg:    
      description: 'Water tunnel and surge chamber loss coefficient (due to friction) (Kg).  Typical Value = -0.025. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
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
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *govhydropelton_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    qc0:    
      description: 'No-load turbine flow at nominal head (Qc0).  Typical Value = 0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    qn:    
      description: 'Rated flow (Q). Unit = m/s. Typical Value = 40. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
      x-ngsi:    
        type: Property    
    simplifiedPelton:    
      description: 'Simplified Pelton model simulation (Sflag). true = enable of simplified Pelton model simulation false = enable of complete Pelton model simulation (non linear gain). Typical Value = false. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    staticCompensating:    
      description: 'Static compensating characteristic (Cflag). true = enable of static compensating characteristic  false = inhibit of static compensating characteristic. Typical Value = false. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ta:    
      description: 'Derivative gain (accelerometer time constant) (Ta).  Typical Value = 3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ts:    
      description: 'Gate servo time constant (Ts).  Typical Value = 0.15. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tv:    
      description: 'Servomotor integrator time constant (TV).  Typical Value = 0.3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    twnc:    
      description: 'Water inertia time constant (Twnc).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    twng:    
      description: 'Water tunnel and surge chamber inertia time constant (Twng). Typical Value = 3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tx:    
      description: 'Electronic integrator time constant (Tx).  Typical Value = 0.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be GovHydroPelton'    
      enum:    
        - GovHydroPelton    
      type: string    
      x-ngsi:    
        type: Property    
    va:    
      description: 'Maximum gate opening velocity (Va).  Unit = PU/sec.  Typical Value = 0.016. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    valvmax:    
      description: 'Maximum gate opening (ValvMax).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    valvmin:    
      description: 'Minimum gate opening (ValvMin).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vav:    
      description: 'Maximum servomotor valve opening velocity (Vav).  Typical Value = 0.017. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vc:    
      description: 'Maximum gate closing velocity (Vc).  Unit = PU/sec.  Typical Value = -0.016. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vcv:    
      description: 'Maximum servomotor valve closing velocity (Vcv).  Typical Value = -0.017. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    waterTunnelSurgeChamberSimulation:    
      description: 'Water tunnel and surge chamber simulation (Tflag). true = enable of water tunnel and surge chamber simulation false = inhibit of water tunnel and surge chamber simulation. Typical Value = false. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    zsfc:    
      description: 'Head of upper water level with respect to the level of penstock (Zsfc).  Unit = m. Typical Value = 25. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovHydroPelton/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/GovHydroPelton/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
Non disponible l'exemple d'un GovHydroPelton au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un GovHydroPelton au format JSON-LD tel que normalisé. Ceci est compatible avec la NGSI-v2 lorsqu'elle n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un GovHydroPelton au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un GovHydroPelton au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
