Entité : GovHydroWEH  
====================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovHydroWEH/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Adapté des modèles de données CIM. Modèle de gouverneur hydroélectrique de Woodward Electric.**  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `db`: Bande morte de la vitesse (db). Valeur par défaut : 0.0  - `description`: Une description de cet article  - `dicn`: Valeur permettant au contrôleur intégral d'avancer au-delà des limites de la porte (Dicn). Valeur par défaut : 0.0  - `dpv`: Valeur permettant au contrôleur de la vanne pilote d'avancer au-delà des limites de la vanne (Dpv). Valeur par défaut : 0.0  - `dturb`: Facteur d'amortissement de la turbine (Dturb).  Unité = delta P (PU de MWbase) / delta vitesse (PU). Valeur par défaut : 0,0  - `feedbackSignal`: Sélection du signal de rétroaction (Sw). true = Sortie PID (si R-Perm-Gate=droop et R-Perm-Pe=0) false = Puissance électrique (si R-Perm-Gate=0 et R-Perm-Pe=droop) ou false = Position de la porte (si R-Perm-Gate=droop et R-Perm-Pe=0). Par défaut : Faux  - `fl1`: Débit de la vanne 1 (Fl1).  Valeur de débit pour le point de position de la vanne 1 pour la table de consultation représentant le débit d'eau à travers la turbine en fonction de la position de la vanne pour produire un débit stable. Valeur par défaut : 0.0  - `fl2`: Débit de la vanne 2 (Fl2).  Valeur de débit pour le point de position de la vanne 2 pour la table de consultation représentant le débit d'eau à travers la turbine en fonction de la position de la vanne pour produire un débit stable. Valeur par défaut : 0.0  - `fl3`: Débit de la vanne 3 (Fl3).  Valeur de débit pour le point de position de la vanne 3 pour la table de consultation représentant le débit d'eau à travers la turbine en fonction de la position de la vanne pour produire un débit stable. Valeur par défaut : 0.0  - `fl4`: Débit de la vanne 4 (Fl4).  Valeur de débit pour le point de position de la vanne 4 pour la table de consultation représentant le débit d'eau à travers la turbine en fonction de la position de la vanne pour produire un débit stable. Valeur par défaut : 0.0  - `fl5`: Débit de la vanne 5 (Fl5).  Valeur de débit pour le point de position de la vanne 5 pour la table de consultation représentant le débit d'eau à travers la turbine en fonction de la position de la vanne pour produire un débit stable. Valeur par défaut : 0.0  - `fp1`: Débit P1 (Fp1).  Valeur du débit de la turbine pour le point 1 de la table de consultation représentant la puissance mécanique unitaire sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0.0  - `fp10`: Débit P10 (Fp10).  Valeur du débit de la turbine pour le point 10 de la table de consultation représentant la puissance mécanique unitaire sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0.0  - `fp2`: Débit P2 (Fp2).  Valeur du débit de la turbine pour le point 2 de la table de consultation représentant la puissance mécanique unitaire sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0.0  - `fp3`: Débit P3 (Fp3).  Valeur du débit de la turbine pour le point 3 de la table de consultation représentant la puissance mécanique unitaire sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0.0  - `fp4`: Débit P4 (Fp4).  Valeur du débit de la turbine pour le point 4 de la table de consultation représentant la puissance mécanique unitaire sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0.0  - `fp5`: Débit P5 (Fp5).  Valeur du débit de la turbine pour le point 5 de la table de consultation représentant la puissance mécanique unitaire sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0.0  - `fp6`: Débit P6 (Fp6).  Valeur du débit de la turbine pour le point 6 de la table de consultation représentant la puissance mécanique unitaire sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0.0  - `fp7`: Débit P7 (Fp7).  Valeur du débit de la turbine pour le point 7 de la table de consultation représentant la puissance mécanique unitaire sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0.0  - `fp8`: Débit P8 (Fp8).  Valeur du débit de la turbine pour le point 8 de la table de consultation représentant la puissance mécanique unitaire sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0.0  - `fp9`: Débit P9 (Fp9).  Valeur du débit de la turbine pour le point 9 de la table de consultation représentant la puissance mécanique unitaire sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0.0  - `gmax`: Position maximale de la porte (Gmax). Valeur par défaut : 0.0  - `gmin`: Position minimale de la porte (Gmin). Valeur par défaut : 0.0  - `gtmxcl`: Taux de fermeture maximal de la porte (Gtmxcl). Valeur par défaut : 0,0  - `gtmxop`: Taux d'ouverture maximal de la porte (Gtmxop). Valeur par défaut : 0.0  - `gv1`: Porte 1 (Gv1).  Valeur de la position de la vanne pour le point 1 de la table de consultation représentant le débit d'eau à travers la turbine en fonction de la position de la vanne pour produire un débit stable. Valeur par défaut : 0.0  - `gv2`: Porte 2 (Gv2).  Valeur de la position de la vanne pour le point 2 de la table de consultation représentant le débit d'eau à travers la turbine en fonction de la position de la vanne pour produire un débit stable. Valeur par défaut : 0.0  - `gv3`: Porte 3 (Gv3).  Valeur de la position de la vanne pour le point 3 de la table de consultation représentant le débit d'eau à travers la turbine en fonction de la position de la vanne pour produire un débit stable. Valeur par défaut : 0.0  - `gv4`: Porte 4 (Gv4).  Valeur de la position de la porte pour le point 4 de la table de consultation représentant le débit d'eau à travers la turbine en fonction de la position de la porte pour produire un débit stable. Valeur par défaut : 0.0  - `gv5`: Porte 5 (Gv5).  Valeur de la position de la vanne pour le point 5 de la table de consultation représentant le débit d'eau à travers la turbine en fonction de la position de la vanne pour produire un débit stable. Valeur par défaut : 0.0  - `id`: Identifiant unique de l'entité  - `kd`: Gain dérivé du régulateur de dérivation (Kd). Valeur par défaut : 0.0  - `ki`: Contrôleur dérivatif Gain intégral (Ki). Valeur par défaut : 0.0  - `kp`: Gain de contrôle de la dérivation (Kp). Valeur par défaut : 0.0  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `mwbase`: Base pour les valeurs de puissance (MWbase) (>0).  Unité = MW. Valeur par défaut : 0.0  - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `pmss1`: Pmss Débit P1 (Pmss1).  Pmss de sortie de puissance mécanique pour le point de débit de la turbine 1 pour la table de consultation représentant la puissance mécanique unitaire sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0.0  - `pmss10`: Pmss Débit P10 (Pmss10).  Pmss de sortie de puissance mécanique pour le point 10 du débit de la turbine pour la table de consultation représentant la puissance mécanique unitaire sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0.0  - `pmss2`: Pmss Débit P2 (Pmss2).  Sortie de la puissance mécanique Pmss pour le point 2 du débit de la turbine pour la table de consultation représentant la puissance mécanique unitaire sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0.0  - `pmss3`: Pmss Débit P3 (Pmss3).  Pmss de sortie de la puissance mécanique pour le point 3 du débit de la turbine pour la table de consultation représentant la puissance mécanique unitaire sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0.0  - `pmss4`: Pmss Débit P4 (Pmss4).  Pmss de sortie de puissance mécanique pour le point 4 du débit de la turbine pour la table de consultation représentant la puissance mécanique unitaire sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0.0  - `pmss5`: Pmss Débit P5 (Pmss5).  Pmss de sortie de puissance mécanique pour le point 5 du débit de la turbine pour la table de consultation représentant la puissance mécanique unitaire sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0.0  - `pmss6`: Pmss Débit P6 (Pmss6).  Puissance mécanique de sortie Pmss pour le point 6 du débit de la turbine pour la table de consultation représentant la puissance mécanique unitaire sur le MVA nominal de la machine en fonction du débit de la turbine. Valeur par défaut : 0.0  - `pmss7`: Pmss Débit P7 (Pmss7).  Puissance mécanique de sortie Pmss pour le point 7 du débit de la turbine pour la table de consultation représentant la puissance mécanique unitaire sur le MVA nominal de la machine en fonction du débit de la turbine. Valeur par défaut : 0.0  - `pmss8`: Pmss Débit P8 (Pmss8).  Pmss de sortie de puissance mécanique pour le point 8 du débit de la turbine pour la table de consultation représentant la puissance mécanique unitaire sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0.0  - `pmss9`: Pmss Débit P9 (Pmss9).  Pmss de sortie de puissance mécanique pour le point 9 du débit de la turbine pour la table de consultation représentant la puissance mécanique unitaire sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0.0  - `rpg`: Statisme permanent pour le retour de la sortie du régulateur (R-Perm-Gate). Valeur par défaut : 0.0  - `rpp`: Statisme permanent pour le retour de puissance électrique (R-Perm-Pe). Valeur par défaut : 0.0  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `td`: Constante de temps du contrôleur de dérivation pour limiter la caractéristique de dérivation au-delà d'une fréquence de rupture afin d'éviter l'amplification du bruit haute fréquence (Td). Valeur par défaut : 0  - `tdv`: Constante de temps du retard de la vanne distributive (Tdv). Valeur par défaut : 0  - `tg`: Valeur permettant au contrôleur de la vanne de distribution d'avancer au-delà de la limite du taux de mouvement de la vanne (Tg). Valeur par défaut : 0  - `tp`: Constante de temps de retard de la vanne pilote (Tp). Valeur par défaut : 0  - `tpe`: Constante de temps du statisme de la puissance électrique (Tpe). Valeur par défaut : 0  - `tw`: Constante de temps de l'inertie de l'eau (Tw) (>0). Valeur par défaut : 0  - `type`: Type de NGSI. Il s'agit de GovHydroWEH.    
Propriétés requises  
Adapté de CIM data models and CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Ce modèle de données est une conversion directe du modèle d'information commun (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un mauvais type. Si tel était le cas, veuillez soulever un problème ou envoyer un courrier à info@smartdatamodels.org.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GovHydroWEH:    
  description: 'Adapted from CIM data models. Woodward Electric Hydro Governor Model.'    
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
    db:    
      description: 'Speed Dead Band (db). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    description:    
      description: 'A description of this item'    
      type: Property    
    dicn:    
      description: 'Value to allow the integral controller to advance beyond the gate limits (Dicn). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    dpv:    
      description: 'Value to allow the Pilot valve controller to advance beyond the gate limits (Dpv). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    dturb:    
      description: 'Turbine damping factor (Dturb).  Unit = delta P (PU of MWbase) / delta speed (PU). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    feedbackSignal:    
      description: 'Feedback signal selection (Sw). true = PID Output (if R-Perm-Gate=droop and R-Perm-Pe=0) false = Electrical Power (if R-Perm-Gate=0 and R-Perm-Pe=droop) or false = Gate Position (if R-Perm-Gate=droop and R-Perm-Pe=0). Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fl1:    
      description: 'Flow Gate 1 (Fl1).  Flow value for gate position point 1 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fl2:    
      description: 'Flow Gate 2 (Fl2).  Flow value for gate position point 2 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fl3:    
      description: 'Flow Gate 3 (Fl3).  Flow value for gate position point 3 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fl4:    
      description: 'Flow Gate 4 (Fl4).  Flow value for gate position point 4 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fl5:    
      description: 'Flow Gate 5 (Fl5).  Flow value for gate position point 5 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fp1:    
      description: 'Flow P1 (Fp1).  Turbine Flow value for point 1 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fp10:    
      description: 'Flow P10 (Fp10).  Turbine Flow value for point 10 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fp2:    
      description: 'Flow P2 (Fp2).  Turbine Flow value for point 2 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fp3:    
      description: 'Flow P3 (Fp3).  Turbine Flow value for point 3 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fp4:    
      description: 'Flow P4 (Fp4).  Turbine Flow value for point 4 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fp5:    
      description: 'Flow P5 (Fp5).  Turbine Flow value for point 5 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fp6:    
      description: 'Flow P6 (Fp6).  Turbine Flow value for point 6 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fp7:    
      description: 'Flow P7 (Fp7).  Turbine Flow value for point 7 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fp8:    
      description: 'Flow P8 (Fp8).  Turbine Flow value for point 8 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fp9:    
      description: 'Flow P9 (Fp9).  Turbine Flow value for point 9 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gmax:    
      description: 'Maximum Gate Position (Gmax). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gmin:    
      description: 'Minimum Gate Position (Gmin). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gtmxcl:    
      description: 'Maximum gate closing rate (Gtmxcl). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gtmxop:    
      description: 'Maximum gate opening rate (Gtmxop). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv1:    
      description: 'Gate 1 (Gv1).  Gate Position value for point 1 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv2:    
      description: 'Gate 2 (Gv2).  Gate Position value for point 2 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv3:    
      description: 'Gate 3 (Gv3).  Gate Position value for point 3 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv4:    
      description: 'Gate 4 (Gv4).  Gate Position value for point 4 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv5:    
      description: 'Gate 5 (Gv5).  Gate Position value for point 5 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &govhydroweh_-_properties_-_owner_-_items_-_anyof    
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
    kd:    
      description: 'Derivative controller derivative gain (Kd). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ki:    
      description: 'Derivative controller Integral gain (Ki). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kp:    
      description: 'Derivative control gain (Kp). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
        anyOf: *govhydroweh_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    pmss1:    
      description: 'Pmss Flow P1 (Pmss1).  Mechanical Power output Pmss for Turbine Flow point 1 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmss10:    
      description: 'Pmss Flow P10 (Pmss10).  Mechanical Power output Pmss for Turbine Flow point 10 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmss2:    
      description: 'Pmss Flow P2 (Pmss2).  Mechanical Power output Pmss for Turbine Flow point 2 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmss3:    
      description: 'Pmss Flow P3 (Pmss3).  Mechanical Power output Pmss for Turbine Flow point 3 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmss4:    
      description: 'Pmss Flow P4 (Pmss4).  Mechanical Power output Pmss for Turbine Flow point 4 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmss5:    
      description: 'Pmss Flow P5 (Pmss5).  Mechanical Power output Pmss for Turbine Flow point 5 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmss6:    
      description: 'Pmss Flow P6 (Pmss6).  Mechanical Power output Pmss for Turbine Flow point 6 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmss7:    
      description: 'Pmss Flow P7 (Pmss7).  Mechanical Power output Pmss for Turbine Flow point 7 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmss8:    
      description: 'Pmss Flow P8 (Pmss8).  Mechanical Power output Pmss for Turbine Flow point 8 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmss9:    
      description: 'Pmss Flow P9 (Pmss9).  Mechanical Power output Pmss for Turbine Flow point 9 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rpg:    
      description: 'Permanent droop for governor output feedback (R-Perm-Gate). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rpp:    
      description: 'Permanent droop for electrical power feedback (R-Perm-Pe). Default: 0.0'    
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
    td:    
      description: 'Derivative controller time constant to limit the derivative characteristic beyond a breakdown frequency to avoid amplification of high-frequency noise (Td). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tdv:    
      description: 'Distributive Valve time lag time constant (Tdv). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tg:    
      description: 'Value to allow the Distribution valve controller to advance beyond the gate movement rate limit (Tg). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tp:    
      description: 'Pilot Valve time lag time constant (Tp). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tpe:    
      description: 'Electrical power droop time constant (Tpe). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tw:    
      description: 'Water inertia time constant (Tw) (>0). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be GovHydroWEH'    
      enum:    
        - GovHydroWEH    
      type: Property    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un GovHydroWEH au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un GovHydroWEH au format JSON-LD tel que normalisé. Ceci est compatible avec la NGSI-v2 lorsqu'elle n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un GovHydroWEH au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un GovHydroWEH au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude