<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : GovHydroWEH  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovHydroWEH/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Adapté des modèles de données CIM. Modèle du gouverneur hydroélectrique de Woodward Electric**.  
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
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `db[number]`: Bande morte de la vitesse (db). Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: Une description de l'article  - `dicn[number]`: Valeur permettant au régulateur intégral d'avancer au-delà des limites de la porte (Dicn). Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dpv[number]`: Valeur permettant au contrôleur de la vanne pilote d'avancer au-delà des limites de la vanne (Dpv). Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dturb[number]`: Facteur d'amortissement de la turbine (Dturb).  Unité = delta P (PU de MWbase) / delta vitesse (PU). Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `feedbackSignal[number]`: Sélection du signal de retour (Sw). true = Sortie PID (si R-Perm-Gate=droop et R-Perm-Pe=0) false = Alimentation électrique (si R-Perm-Gate=0 et R-Perm-Pe=droop) ou false = Position de la porte (si R-Perm-Gate=droop et R-Perm-Pe=0). Valeur par défaut : Faux  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl1[number]`: Porte de débit 1 (Fl1).  Valeur de débit pour le point 1 de la position de la vanne pour le tableau de consultation représentant le débit d'eau dans la turbine en fonction de la position de la vanne pour produire un débit stable. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl2[number]`: Porte de débit 2 (Fl2).  Valeur de débit pour le point 2 de la position de la vanne pour le tableau de consultation représentant le débit d'eau à travers la turbine en fonction de la position de la vanne pour produire un débit en régime permanent. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl3[number]`: Porte de débit 3 (Fl3).  Valeur de débit pour le point 3 de la position de la vanne pour le tableau de consultation représentant le débit d'eau à travers la turbine en fonction de la position de la vanne pour produire un débit en régime permanent. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl4[number]`: Porte de débit 4 (Fl4).  Valeur de débit pour le point 4 de la position de la vanne pour le tableau de consultation représentant le débit d'eau à travers la turbine en fonction de la position de la vanne pour produire un débit en régime permanent. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl5[number]`: Porte de débit 5 (Fl5).  Valeur de débit pour le point 5 de la position de la vanne pour le tableau de consultation représentant le débit d'eau dans la turbine en fonction de la position de la vanne pour produire un débit stable. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp1[number]`: Débit P1 (Fp1).  Valeur du débit de la turbine pour le point 1 de la table de correspondance représentant la puissance mécanique par unité sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp10[number]`: Débit P10 (Fp10).  Valeur du débit de la turbine pour le point 10 de la table de correspondance représentant la puissance mécanique par unité sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp2[number]`: Débit P2 (Fp2).  Valeur du débit de la turbine pour le point 2 de la table de correspondance représentant la puissance mécanique par unité sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp3[number]`: Débit P3 (Fp3).  Valeur du débit de la turbine pour le point 3 de la table de correspondance représentant la puissance mécanique par unité sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp4[number]`: Débit P4 (Fp4).  Valeur du débit de la turbine pour le point 4 de la table de correspondance représentant la puissance mécanique par unité sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp5[number]`: Débit P5 (Fp5).  Valeur du débit de la turbine pour le point 5 de la table de correspondance représentant la puissance mécanique par unité sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp6[number]`: Débit P6 (Fp6).  Valeur du débit de la turbine pour le point 6 de la table de correspondance représentant la puissance mécanique par unité sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp7[number]`: Débit P7 (Fp7).  Valeur du débit de la turbine pour le point 7 de la table de correspondance représentant la puissance mécanique par unité sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp8[number]`: Débit P8 (Fp8).  Valeur du débit de la turbine pour le point 8 de la table de correspondance représentant la puissance mécanique par unité sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp9[number]`: Débit P9 (Fp9).  Valeur du débit de la turbine pour le point 9 de la table de correspondance représentant la puissance mécanique par unité sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gmax[number]`: Position maximale de la porte (Gmax). Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gmin[number]`: Position minimale de la porte (Gmin). Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gtmxcl[number]`: Vitesse maximale de fermeture de la porte (Gtmxcl). Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gtmxop[number]`: Taux d'ouverture maximal de la porte (Gtmxop). Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv1[number]`: Porte 1 (Gv1).  Valeur de la position de la vanne pour le point 1 de la table de correspondance représentant le débit d'eau dans la turbine en fonction de la position de la vanne pour produire un débit stable. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv2[number]`: Porte 2 (Gv2).  Valeur de la position de la vanne pour le point 2 de la table de correspondance représentant le débit d'eau dans la turbine en fonction de la position de la vanne pour produire un débit stable. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv3[number]`: Porte 3 (Gv3).  Valeur de la position de la vanne pour le point 3 de la table de correspondance représentant le débit d'eau dans la turbine en fonction de la position de la vanne pour produire un débit stable. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv4[number]`: Porte 4 (Gv4).  Valeur de la position de la vanne pour le point 4 de la table de correspondance représentant le débit d'eau dans la turbine en fonction de la position de la vanne pour produire un débit en régime permanent. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv5[number]`: Porte 5 (Gv5).  Valeur de la position de la vanne pour le point 5 de la table de correspondance représentant le débit d'eau dans la turbine en fonction de la position de la vanne pour produire un débit en régime permanent. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identifiant unique de l'entité  - `kd[number]`: Gain dérivé du contrôleur de dérivée (Kd). Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ki[number]`: Gain intégral du contrôleur dérivatif (Ki). Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kp[number]`: Gain de contrôle dérivatif (Kp). Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `mwbase[number]`: Base pour les valeurs de puissance (MWbase) (>0).  Unité = MW. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `pmss1[number]`: Pmss Flow P1 (Pmss1).  Puissance mécanique de sortie Pmss pour le point de débit 1 de la turbine pour la table de correspondance représentant la puissance mécanique par unité sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss10[number]`: Pmss Flow P10 (Pmss10).  Puissance mécanique de sortie Pmss pour le point de débit 10 de la turbine pour la table de correspondance représentant la puissance mécanique par unité sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss2[number]`: Pmss Flow P2 (Pmss2).  Sortie de puissance mécanique Pmss pour le point 2 du débit de la turbine pour la table de correspondance représentant la puissance mécanique par unité sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss3[number]`: Pmss Flow P3 (Pmss3).  Puissance mécanique de sortie Pmss pour le point 3 du débit de la turbine pour la table de correspondance représentant la puissance mécanique par unité sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss4[number]`: Pmss Flow P4 (Pmss4).  Puissance mécanique de sortie Pmss pour le point de débit 4 de la turbine pour la table de correspondance représentant la puissance mécanique par unité sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss5[number]`: Pmss Flow P5 (Pmss5).  Puissance mécanique de sortie Pmss pour le point 5 du débit de la turbine pour la table de correspondance représentant la puissance mécanique par unité sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss6[number]`: Pmss Flow P6 (Pmss6).  Puissance mécanique de sortie Pmss pour le point 6 du débit de la turbine pour la table de correspondance représentant la puissance mécanique par unité sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss7[number]`: Pmss Flow P7 (Pmss7).  Puissance mécanique de sortie Pmss pour le point 7 du débit de la turbine pour la table de correspondance représentant la puissance mécanique par unité sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss8[number]`: Pmss Flow P8 (Pmss8).  Puissance mécanique de sortie Pmss pour le point 8 du débit de la turbine pour la table de correspondance représentant la puissance mécanique par unité sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss9[number]`: Pmss Flow P9 (Pmss9).  Puissance mécanique de sortie Pmss pour le point 9 du débit de la turbine pour la table de correspondance représentant la puissance mécanique par unité sur la valeur nominale MVA de la machine en fonction du débit de la turbine. Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rpg[number]`: Statisme permanent pour le retour de sortie du régulateur (R-Perm-Gate). Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rpp[number]`: Statisme permanent pour le retour de puissance électrique (R-Perm-Pe). Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `td[number]`: Constante de temps du contrôleur de dérivée pour limiter la caractéristique de dérivée au-delà d'une fréquence de rupture afin d'éviter l'amplification du bruit à haute fréquence (Td). Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tdv[number]`: Constante de temps de décalage de la vanne distributive (Tdv). Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tg[number]`: Valeur permettant au contrôleur de la vanne de distribution d'avancer au-delà de la limite de vitesse de mouvement de la vanne (Tg). Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tp[number]`: Constante de temps du retard de la vanne pilote (Tp). Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tpe[number]`: Constante de temps du statisme de la puissance électrique (Tpe). Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw[number]`: Constante de temps de l'inertie de l'eau (Tw) (>0). Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Type d'INSG. Il doit s'agir de GovHydroWEH  <!-- /30-PropertiesList -->  
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
GovHydroWEH:    
  description: Adapted from CIM data models. Woodward Electric Hydro Governor Model.    
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
    db:    
      description: 'Speed Dead Band (db). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    dicn:    
      description: 'Value to allow the integral controller to advance beyond the gate limits (Dicn). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dpv:    
      description: 'Value to allow the Pilot valve controller to advance beyond the gate limits (Dpv). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dturb:    
      description: 'Turbine damping factor (Dturb).  Unit = delta P (PU of MWbase) / delta speed (PU). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    feedbackSignal:    
      description: 'Feedback signal selection (Sw). true = PID Output (if R-Perm-Gate=droop and R-Perm-Pe=0) false = Electrical Power (if R-Perm-Gate=0 and R-Perm-Pe=droop) or false = Gate Position (if R-Perm-Gate=droop and R-Perm-Pe=0). Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fl1:    
      description: 'Flow Gate 1 (Fl1).  Flow value for gate position point 1 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fl2:    
      description: 'Flow Gate 2 (Fl2).  Flow value for gate position point 2 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fl3:    
      description: 'Flow Gate 3 (Fl3).  Flow value for gate position point 3 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fl4:    
      description: 'Flow Gate 4 (Fl4).  Flow value for gate position point 4 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fl5:    
      description: 'Flow Gate 5 (Fl5).  Flow value for gate position point 5 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp1:    
      description: 'Flow P1 (Fp1).  Turbine Flow value for point 1 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp10:    
      description: 'Flow P10 (Fp10).  Turbine Flow value for point 10 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp2:    
      description: 'Flow P2 (Fp2).  Turbine Flow value for point 2 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp3:    
      description: 'Flow P3 (Fp3).  Turbine Flow value for point 3 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp4:    
      description: 'Flow P4 (Fp4).  Turbine Flow value for point 4 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp5:    
      description: 'Flow P5 (Fp5).  Turbine Flow value for point 5 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp6:    
      description: 'Flow P6 (Fp6).  Turbine Flow value for point 6 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp7:    
      description: 'Flow P7 (Fp7).  Turbine Flow value for point 7 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp8:    
      description: 'Flow P8 (Fp8).  Turbine Flow value for point 8 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp9:    
      description: 'Flow P9 (Fp9).  Turbine Flow value for point 9 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gmax:    
      description: 'Maximum Gate Position (Gmax). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gmin:    
      description: 'Minimum Gate Position (Gmin). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gtmxcl:    
      description: 'Maximum gate closing rate (Gtmxcl). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gtmxop:    
      description: 'Maximum gate opening rate (Gtmxop). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv1:    
      description: 'Gate 1 (Gv1).  Gate Position value for point 1 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv2:    
      description: 'Gate 2 (Gv2).  Gate Position value for point 2 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv3:    
      description: 'Gate 3 (Gv3).  Gate Position value for point 3 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv4:    
      description: 'Gate 4 (Gv4).  Gate Position value for point 4 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv5:    
      description: 'Gate 5 (Gv5).  Gate Position value for point 5 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    kd:    
      description: 'Derivative controller derivative gain (Kd). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ki:    
      description: 'Derivative controller Integral gain (Ki). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kp:    
      description: 'Derivative control gain (Kp). Default: 0.0'    
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
    mwbase:    
      description: 'Base for power values (MWbase) (>0).  Unit = MW. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
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
    pmss1:    
      description: 'Pmss Flow P1 (Pmss1).  Mechanical Power output Pmss for Turbine Flow point 1 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss10:    
      description: 'Pmss Flow P10 (Pmss10).  Mechanical Power output Pmss for Turbine Flow point 10 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss2:    
      description: 'Pmss Flow P2 (Pmss2).  Mechanical Power output Pmss for Turbine Flow point 2 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss3:    
      description: 'Pmss Flow P3 (Pmss3).  Mechanical Power output Pmss for Turbine Flow point 3 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss4:    
      description: 'Pmss Flow P4 (Pmss4).  Mechanical Power output Pmss for Turbine Flow point 4 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss5:    
      description: 'Pmss Flow P5 (Pmss5).  Mechanical Power output Pmss for Turbine Flow point 5 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss6:    
      description: 'Pmss Flow P6 (Pmss6).  Mechanical Power output Pmss for Turbine Flow point 6 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss7:    
      description: 'Pmss Flow P7 (Pmss7).  Mechanical Power output Pmss for Turbine Flow point 7 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss8:    
      description: 'Pmss Flow P8 (Pmss8).  Mechanical Power output Pmss for Turbine Flow point 8 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss9:    
      description: 'Pmss Flow P9 (Pmss9).  Mechanical Power output Pmss for Turbine Flow point 9 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rpg:    
      description: 'Permanent droop for governor output feedback (R-Perm-Gate). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rpp:    
      description: 'Permanent droop for electrical power feedback (R-Perm-Pe). Default: 0.0'    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    td:    
      description: 'Derivative controller time constant to limit the derivative characteristic beyond a breakdown frequency to avoid amplification of high-frequency noise (Td). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tdv:    
      description: 'Distributive Valve time lag time constant (Tdv). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tg:    
      description: 'Value to allow the Distribution valve controller to advance beyond the gate movement rate limit (Tg). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tp:    
      description: 'Pilot Valve time lag time constant (Tp). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tpe:    
      description: 'Electrical power droop time constant (Tpe). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tw:    
      description: 'Water inertia time constant (Tw) (>0). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: NGSI type. It has to be GovHydroWEH    
      enum:    
        - GovHydroWEH    
      type: string    
      x-ngsi:    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovHydroWEH/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/GovHydroWEH/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
Non disponible l'exemple d'un GovHydroWEH au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un GovHydroWEH au format JSON-LD tel que normalisé. Ce format est compatible avec les NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un GovHydroWEH au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un GovHydroWEH au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
