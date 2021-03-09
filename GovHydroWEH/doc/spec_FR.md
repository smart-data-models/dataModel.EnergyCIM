Entité : GovHydroWEH  
====================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovHydroWEH/LICENSE.md)  
Description globale : **Adapté des modèles de données CIM. Modèle Woodward Electric Hydro Governor.**  

## Liste des biens  

- `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `db`: Bande morte de vitesse (db). Valeur par défaut : 0.0  - `description`: Une description de cet article  - `dicn`: Valeur permettant au contrôleur intégral d'avancer au-delà des limites de la porte (Dicn). Valeur par défaut : 0.0  - `dpv`: Valeur permettant au contrôleur de la vanne pilote d'avancer au-delà des limites de la vanne (Dpv). Valeur par défaut : 0.0  - `dturb`: Facteur d'amortissement des turbines (Dturb).  Unité = delta P (PU de la base MW) / vitesse delta (PU). Valeur par défaut : 0,0  - `feedbackSignal`: Sélection du signal de retour (Sw). true = Sortie PID (si R-Perm-Gate=droop et R-Perm-Pe=0) false = Puissance électrique (si R-Perm-Gate=0 et R-Perm-Pe=droop) ou false = Position de la porte (si R-Perm-Gate=droop et R-Perm-Pe=0). Par défaut : False  - `fl1`: Porte de flux 1 (Fl1).  Valeur de débit pour le point de position de la vanne 1 pour le tableau de référence représentant le débit d'eau à travers la turbine en fonction de la position de la vanne pour produire un débit en régime permanent. Valeur par défaut : 0.0  - `fl2`: Porte de flux 2 (Fl2).  Valeur de débit pour le point de position de la vanne 2 pour le tableau de référence représentant le débit d'eau à travers la turbine en fonction de la position de la vanne pour produire un débit en régime permanent. Valeur par défaut : 0.0  - `fl3`: Porte de flux 3 (Fl3).  Valeur de débit pour le point de position de la vanne 3 pour le tableau de référence représentant le débit d'eau à travers la turbine en fonction de la position de la vanne pour produire un débit en régime permanent. Valeur par défaut : 0.0  - `fl4`: Porte de flux 4 (Fl4).  Valeur de débit pour le point de position de la vanne 4 pour le tableau de référence représentant le débit d'eau à travers la turbine en fonction de la position de la vanne pour produire un débit en régime permanent. Valeur par défaut : 0.0  - `fl5`: Porte de flux 5 (Fl5).  Valeur de débit pour le point de position de la vanne 5 pour le tableau de référence représentant le débit d'eau à travers la turbine en fonction de la position de la vanne pour produire un débit en régime permanent. Valeur par défaut : 0.0  - `fp1`: Flux P1 (Fp1).  Valeur du débit de la turbine pour le point 1 du tableau de recherche représentant par unité de puissance mécanique la puissance nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  - `fp10`: Flux P10 (Fp10).  Valeur du débit de la turbine pour le point 10 pour le tableau de recherche représentant par unité de puissance mécanique la puissance nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  - `fp2`: Débit P2 (Fp2).  Valeur du débit de la turbine pour le point 2 du tableau de recherche représentant par unité de puissance mécanique la puissance nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  - `fp3`: Flux P3 (Fp3).  Valeur du débit de la turbine pour le point 3 du tableau de recherche représentant par unité de puissance mécanique la puissance nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  - `fp4`: Flux P4 (Fp4).  Valeur du débit de la turbine pour le point 4 du tableau de recherche représentant par unité de puissance mécanique la puissance nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  - `fp5`: Flux P5 (Fp5).  Valeur du débit de la turbine pour le point 5 pour le tableau de recherche représentant par unité de puissance mécanique la puissance nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  - `fp6`: Flux P6 (Fp6).  Valeur du débit de la turbine pour le point 6 pour le tableau de recherche représentant par unité de puissance mécanique la puissance nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  - `fp7`: Flux P7 (Fp7).  Valeur du débit de la turbine pour le point 7 pour le tableau de recherche représentant par unité de puissance mécanique la puissance nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  - `fp8`: Flux P8 (Fp8).  Valeur du débit de la turbine pour le point 8 pour le tableau de recherche représentant par unité de puissance mécanique la puissance nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  - `fp9`: Flux P9 (Fp9).  Valeur du débit de la turbine pour le point 9 pour le tableau de recherche représentant par unité de puissance mécanique la puissance nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  - `gmax`: Position maximale de la porte (Gmax). Valeur par défaut : 0,0  - `gmin`: Position minimale de la porte (Gmin). Valeur par défaut : 0.0  - `gtmxcl`: Taux maximal de fermeture des portes (Gtmxcl). Valeur par défaut : 0,0  - `gtmxop`: Taux d'ouverture maximum des portes (Gtmxop). Valeur par défaut : 0,0  - `gv1`: Porte 1 (Gv1).  Valeur de la position de la vanne pour le point 1 de la table de recherche représentant le débit d'eau à travers la turbine en fonction de la position de la vanne pour produire un débit en régime permanent. Valeur par défaut : 0.0  - `gv2`: Porte 2 (Gv2).  Valeur de la position de la vanne pour le point 2 de la table de recherche représentant le débit d'eau à travers la turbine en fonction de la position de la vanne pour produire un débit en régime permanent. Valeur par défaut : 0.0  - `gv3`: Porte 3 (Gv3).  Valeur de la position de la vanne pour le point 3 de la table de recherche représentant le débit d'eau à travers la turbine en fonction de la position de la vanne pour produire un débit en régime permanent. Valeur par défaut : 0.0  - `gv4`: Porte 4 (Gv4).  Valeur de la position de la vanne pour le point 4 pour le tableau de recherche représentant le débit d'eau à travers la turbine en fonction de la position de la vanne pour produire un débit en régime permanent. Valeur par défaut : 0.0  - `gv5`: Porte 5 (Gv5).  Valeur de la position de la vanne pour le point 5 pour le tableau de référence représentant le débit d'eau à travers la turbine en fonction de la position de la vanne pour produire un débit en régime permanent. Valeur par défaut : 0.0  - `id`: Identifiant unique de l'entité  - `kd`: Gain dérivé du contrôleur de dérivés (Kd). Valeur par défaut : 0.0  - `ki`: Contrôleur de dérivation Gain intégral (Ki). Valeur par défaut : 0.0  - `kp`: Gain de contrôle dérivé (Kp). Valeur par défaut : 0,0  - `location`:   - `mwbase`: Base pour les valeurs de puissance (MWbase) (>0).  Unité = MW. Valeur par défaut : 0.0  - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `pmss1`: Flux Pmss P1 (Pmss1).  Puissance mécanique de sortie Pmss pour le débit de la turbine point 1 pour le tableau de recherche représentant par unité de puissance mécanique sur la puissance nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  - `pmss10`: Pmss Flow P10 (Pmss10).  Puissance mécanique Pmss pour le débit de la turbine point 10 pour le tableau de recherche représentant par unité de puissance mécanique sur la puissance nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  - `pmss2`: Flux Pmss P2 (Pmss2).  Puissance mécanique de sortie Pmss pour le débit de la turbine point 2 pour le tableau de recherche représentant par unité de puissance mécanique sur la puissance nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  - `pmss3`: Flux Pmss P3 (Pmss3).  Puissance mécanique de sortie Pmss pour le débit de la turbine point 3 pour le tableau de recherche représentant par unité de puissance mécanique sur la puissance nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  - `pmss4`: Flux Pmss P4 (Pmss4).  Puissance mécanique de sortie Pmss pour le débit de la turbine point 4 pour le tableau de recherche représentant par unité de puissance mécanique sur la puissance nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  - `pmss5`: Flux Pmss P5 (Pmss5).  Puissance mécanique de sortie Pmss pour le débit de la turbine point 5 pour le tableau de recherche représentant par unité de puissance mécanique sur la puissance nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  - `pmss6`: Flux Pmss P6 (Pmss6).  Puissance mécanique Pmss pour le débit de la turbine point 6 pour le tableau de recherche représentant par unité de puissance mécanique sur la puissance nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  - `pmss7`: Flux Pmss P7 (Pmss7).  Puissance mécanique de sortie Pmss pour le débit de la turbine point 7 pour le tableau de recherche représentant par unité de puissance mécanique sur la puissance nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  - `pmss8`: Flux Pmss P8 (Pmss8).  Puissance mécanique de sortie Pmss pour le débit de la turbine point 8 pour le tableau de recherche représentant par unité de puissance mécanique sur la puissance nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  - `pmss9`: Flux Pmss P9 (Pmss9).  Puissance mécanique de sortie Pmss pour le débit de la turbine point 9 pour le tableau de recherche représentant par unité de puissance mécanique sur la puissance nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  - `rpg`: Chute permanente pour le retour d'information sur la sortie du gouverneur (R-Perm-Gate). Valeur par défaut : 0.0  - `rpp`: Chute permanente pour le retour d'énergie électrique (R-Perm-Pe). Valeur par défaut : 0.0  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `td`: Constante de temps du contrôleur dérivé pour limiter la caractéristique dérivée au-delà d'une fréquence de rupture afin d'éviter l'amplification du bruit à haute fréquence (Td). Valeur par défaut : 0  - `tdv`: Constante de temps de décalage de la valve distributive (Tdv). Valeur par défaut : 0  - `tg`: Valeur permettant au contrôleur de la vanne de distribution d'avancer au-delà de la limite de la vitesse de déplacement de la vanne (Tg). Valeur par défaut : 0  - `tp`: Constante de temps de retard de la vanne pilote (Tp). Valeur par défaut : 0  - `tpe`: Constante de temps de chute de l'énergie électrique (Tpe). Valeur par défaut : 0  - `tw`: Constante de temps de l'inertie de l'eau (Tw) (>0). Valeur par défaut : 0  - `type`: Type NGSI. Il doit être de type GovHydroWEH    
Propriétés requises  
Ce modèle de données est une conversion directe du modèle commun d'information (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un mauvais type. C'est le cas, pelase soulever un problème ou envoyer un mail à alberto.abella@fiware.org  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GovHydroWEH:    
  description: 'Adapted from CIM data models. Woodward Electric Hydro Governor Model.'    
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
Non disponible l'exemple d'une GovHydroWEH en format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un GovHydroWEH en format JSON comme normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un GovHydroWEH en format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un GovHydroWEH en format JSON-LD comme normalisé. Il est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
