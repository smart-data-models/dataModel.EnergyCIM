Entité : GovCT2  
===============  
[Licence ouverte](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovCT2/LICENSE.md)  
Description globale : **Adapté des modèles de données CIM. Modèle de régulateur général avec limite de débit de carburant dépendant de la fréquence.  Ce modèle est une modification du modèle GovCT1 afin de représenter la limite de débit de carburant en fonction de la fréquence d'un fabricant de turbines à gaz spécifique.**  

## Liste des biens  

- `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `aset`: Consigne du limiteur d'accélération (Aset).  Unité = PU/sec.  Valeur typique = 10. Valeur par défaut : 0,0  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `db`: Zone morte du régulateur de vitesse par unité de vitesse (db).  Dans la majorité des applications, il est recommandé de fixer cette valeur à zéro.  Valeur typique = 0, valeur par défaut : 0,0  - `description`: Une description de cet article  - `dm`: Coefficient de sensibilité à la vitesse (Dm).  Dm peut représenter soit la variation de la puissance du moteur en fonction de la vitesse de l'arbre, soit la variation de la capacité de puissance maximale en fonction de la vitesse de l'arbre.  S'il est positif, il décrit la pente descendante de la caractéristique de la vitesse du moteur par rapport à la puissance à mesure que la vitesse augmente. Une caractéristique légèrement descendante est typique des moteurs alternatifs et de certaines turbines dérivées de l'aviation.  Si elle est négative, on suppose que la puissance du moteur n'est pas affectée par la vitesse de rotation de l'arbre, mais le débit de carburant maximum autorisé est supposé diminuer avec la baisse de la vitesse de rotation de l'arbre. C'est une caractéristique des turbines industrielles à arbre unique en raison des limites de température des gaz d'échappement.  Valeur typique = 0, par défaut : 0,0  - `flim1`: Seuil de fréquence 1 (Flim1).  Unité = Hz.  Valeur typique = 59. Valeur par défaut : 0,0  - `flim10`: Seuil de fréquence 10 (Flim10).  Unité = Hz.  Valeur typique = 0, par défaut : 0,0  - `flim2`: Seuil de fréquence 2 (Flim2).  Unité = Hz.  Valeur typique = 0, par défaut : 0,0  - `flim3`: Seuil de fréquence 3 (Flim3).  Unité = Hz.  Valeur typique = 0, par défaut : 0,0  - `flim4`: Seuil de fréquence 4 (Flim4).  Unité = Hz.  Valeur typique = 0, par défaut : 0,0  - `flim5`: Seuil de fréquence 5 (Flim5).  Unité = Hz.  Valeur typique = 0, par défaut : 0,0  - `flim6`: Seuil de fréquence 6 (Flim6).  Unité = Hz.  Valeur typique = 0, par défaut : 0,0  - `flim7`: Seuil de fréquence 7 (Flim7).  Unité = Hz.  Valeur typique = 0, par défaut : 0,0  - `flim8`: Seuil de fréquence 8 (Flim8).  Unité = Hz.  Valeur typique = 0, par défaut : 0,0  - `flim9`: Seuil de fréquence 9 (Flim9).  Unité = Hz.  Valeur typique = 0, par défaut : 0,0  - `id`: Identifiant unique de l'entité  - `ka`: Gain du limiteur d'accélération (Ka).  Valeur typique = 10. Valeur par défaut : 0,0  - `kdgov`: Gain dérivé du gouverneur (Kdgov).  Valeur typique = 0, par défaut : 0,0  - `kigov`: Gain intégral du gouverneur (Kigov).  Valeur typique = 0,45. Valeur par défaut : 0,0  - `kiload`: Gain intégral du limiteur de charge pour le contrôleur PI (Kiload).  Valeur typique = 1. Valeur par défaut : 0.0  - `kimw`: Gain (réinitialisation) du contrôleur de puissance (Kimw).  La valeur par défaut de 0,01 correspond à un temps de réinitialisation de 100 secondes.  Une valeur de 0,001 correspond à un contrôleur de charge à action relativement lente.  Valeur typique = 0, valeur par défaut : 0,0  - `kpgov`: Gain proportionnel du gouverneur (Kpgov).  Valeur typique = 4. Valeur par défaut : 0,0  - `kpload`: Limiteur de charge à gain proportionnel pour régulateur PI (Kpload).  Valeur typique = 1. Valeur par défaut : 0.0  - `kturb`: Gain de la turbine (Kturb).  Valeur typique = 1,9168. Valeur par défaut : 0,0  - `ldref`: Valeur de référence du limiteur de charge (Ldref).  Valeur typique = 1. Valeur par défaut : 0,0  - `location`:   - `maxerr`: Valeur maximale pour le signal d'erreur de vitesse (Maxerr).  Valeur typique = 1. Valeur par défaut : 0,0  - `minerr`: Valeur minimale pour le signal d'erreur de vitesse (Minerr).  Valeur typique = -1. Valeur par défaut : 0,0  - `mwbase`: Base pour les valeurs de puissance (MWbase) (> 0).  Unité = MW. Valeur par défaut : 0,0  - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `plim1`: Limite de puissance 1 (Plim1).  Valeur typique = 0,8325. Valeur par défaut : 0,0  - `plim10`: Limite de puissance 10 (Plim10).  Valeur typique = 0, par défaut : 0,0  - `plim2`: Limite de puissance 2 (Plim2).  Valeur typique = 0, par défaut : 0,0  - `plim3`: Limite de puissance 3 (Plim3).  Valeur typique = 0, par défaut : 0,0  - `plim4`: Limite de puissance 4 (Plim4).  Valeur typique = 0, par défaut : 0,0  - `plim5`: Limite de puissance 5 (Plim5).  Valeur typique = 0, par défaut : 0,0  - `plim6`: Limite de puissance 6 (Plim6).  Valeur typique = 0, par défaut : 0,0  - `plim7`: Limite de puissance 7 (Plim7).  Valeur typique = 0, par défaut : 0,0  - `plim8`: Limite de puissance 8 (Plim8).  Valeur typique = 0, par défaut : 0,0  - `plim9`: Limite de puissance 9 (Plim9).  Valeur typique = 0, par défaut : 0,0  - `prate`: Taux de rampe pour la limite de puissance dépendant de la fréquence (Prate).  Valeur typique = 0,017. Valeur par défaut : 0,0  - `r`: Chute permanente (R).  Valeur typique = 0,05. Valeur par défaut : 0,0  - `rclose`: Taux minimum de fermeture de la vanne (Rclose).  Unité = PU/sec.  Valeur typique = -99. Valeur par défaut : 0,0  - `rdown`: Taux maximal de diminution de la limite de charge (Rdown).  Valeur typique = -99. Valeur par défaut : 0,0  - `ropen`: Taux d'ouverture maximum de la vanne (Ropen).  Unité = PU/sec.  Valeur typique = 99. Valeur par défaut : 0,0  - `rselect`: Signal de rétroaction pour le statisme (Rselect).  Valeur typique = puissance électrique. Par défaut : Aucune  - `rup`: Taux maximum d'augmentation de la limite de charge (Rup).  Valeur typique = 99. Valeur par défaut : 0,0  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `ta`: Constante de temps du limiteur d'accélération (Ta).  Valeur typique = 1. Valeur par défaut : 0  - `tact`: Constante de temps de l'actionneur (Tact).  Valeur typique = 0,4. Valeur par défaut : 0  - `tb`: Constante de temps de retard des turbines (Tb).  Valeur typique = 0,1. Valeur par défaut : 0  - `tc`: Constante de temps d'avance de la turbine (Tc).  Valeur typique = 0, par défaut : 0  - `tdgov`: Constante de temps du régulateur dérivé du gouverneur (Tdgov).  Valeur typique = 1. Valeur par défaut : 0  - `teng`: Délai de transport pour les moteurs diesel utilisés dans la représentation des moteurs diesel où il y a un délai de transport faible mais mesurable entre un changement de réglage du débit de carburant et le développement du couple (Teng).  Le Teng devrait être nul dans tous les cas, sauf dans les cas particuliers où ce retard de transport est particulièrement préoccupant.  Valeur typique = 0, valeur par défaut : 0  - `tfload`: Constante de temps du limiteur de charge (Tfload).  Valeur typique = 3. Valeur par défaut : 0  - `tpelec`: Constante de temps du transducteur de puissance électrique (Tpelec).  Valeur typique = 2,5. Valeur par défaut : 0  - `tsa`: Constante de temps de détection de la température (Tsa).  Valeur typique = 0, par défaut : 0  - `tsb`: Constante de temps de retard de la détection de la température (Tsb).  Valeur typique = 50. Valeur par défaut : 0  - `type`: Type NGSI. Il doit être de type GovCT2  - `vmax`: Limite maximale de la position de la vanne (Vmax).  Valeur typique = 1. Valeur par défaut : 0,0  - `vmin`: Limite minimale de position de la vanne (Vmin).  Valeur typique = 0,175. Valeur par défaut : 0,0  - `wfnl`: Débit de carburant à vide (Wfnl).  Valeur typique = 0,187. Valeur par défaut : 0,0  - `wfspd`: Commutateur pour la caractéristique de la source de carburant afin de reconnaître que le débit de carburant, pour une course donnée de la vanne de carburant, peut être proportionnel à la vitesse du moteur (Wfspd). vrai = débit de carburant proportionnel à la vitesse (pour certaines turbines à gaz et moteurs diesel avec injecteurs de carburant à déplacement positif) faux = le système de contrôle du carburant maintient le débit de carburant indépendant de la vitesse du moteur. Valeur typique = faux. Valeur par défaut : False    
Propriétés requises  
Ce modèle de données est une conversion directe du modèle commun d'information (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un mauvais type. C'est le cas, pelase soulever un problème ou envoyer un mail à alberto.abella@fiware.org  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GovCT2:    
  description: 'Adapted from CIM data models. General governor model with frequency-dependent fuel flow limit.  This model is a modification of the GovCT1model in order to represent the frequency-dependent fuel flow limit of a specific gas turbine manufacturer.'    
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
    aset:    
      description: 'Acceleration limiter setpoint (Aset).  Unit = PU/sec.  Typical Value = 10. Default: 0.0'    
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
    db:    
      description: 'Speed governor dead band in per unit speed (db).  In the majority of applications, it is recommended that this value be set to zero.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    description:    
      description: 'A description of this item'    
      type: Property    
    dm:    
      description: 'Speed sensitivity coefficient (Dm).  Dm can represent either the variation of the engine power with the shaft speed or the variation of maximum power capability with shaft speed.  If it is positive it describes the falling slope of the engine speed verses power characteristic as speed increases. A slightly falling characteristic is typical for reciprocating engines and some aero-derivative turbines.  If it is negative the engine power is assumed to be unaffected by the shaft speed, but the maximum permissible fuel flow is taken to fall with falling shaft speed. This is characteristic of single-shaft industrial turbines due to exhaust temperature limits.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    flim1:    
      description: 'Frequency threshold 1 (Flim1).  Unit = Hz.  Typical Value = 59. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    flim10:    
      description: 'Frequency threshold 10 (Flim10).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    flim2:    
      description: 'Frequency threshold 2 (Flim2).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    flim3:    
      description: 'Frequency threshold 3 (Flim3).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    flim4:    
      description: 'Frequency threshold 4 (Flim4).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    flim5:    
      description: 'Frequency threshold 5 (Flim5).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    flim6:    
      description: 'Frequency threshold 6 (Flim6).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    flim7:    
      description: 'Frequency threshold 7 (Flim7).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    flim8:    
      description: 'Frequency threshold 8 (Flim8).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    flim9:    
      description: 'Frequency threshold 9 (Flim9).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &govct2_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Acceleration limiter Gain (Ka).  Typical Value = 10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kdgov:    
      description: 'Governor derivative gain (Kdgov).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kigov:    
      description: 'Governor integral gain (Kigov).  Typical Value = 0.45. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kiload:    
      description: 'Load limiter integral gain for PI controller (Kiload).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kimw:    
      description: 'Power controller (reset) gain (Kimw).  The default value of 0.01 corresponds to a reset time of 100 seconds.  A value of 0.001 corresponds to a relatively slow acting load controller.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kpgov:    
      description: 'Governor proportional gain (Kpgov).  Typical Value = 4. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kpload:    
      description: 'Load limiter proportional gain for PI controller (Kpload).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kturb:    
      description: 'Turbine gain (Kturb).  Typical Value = 1.9168. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ldref:    
      description: 'Load limiter reference value (Ldref).  Typical Value = 1. Default: 0.0'    
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
    maxerr:    
      description: 'Maximum value for speed error signal (Maxerr).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    minerr:    
      description: 'Minimum value for speed error signal (Minerr).  Typical Value = -1. Default: 0.0'    
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
        anyOf: *govct2_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    plim1:    
      description: 'Power limit 1 (Plim1).  Typical Value = 0.8325. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    plim10:    
      description: 'Power limit 10 (Plim10).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    plim2:    
      description: 'Power limit 2 (Plim2).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    plim3:    
      description: 'Power limit 3 (Plim3).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    plim4:    
      description: 'Power limit 4 (Plim4).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    plim5:    
      description: 'Power limit 5 (Plim5).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    plim6:    
      description: 'Power limit 6 (Plim6).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    plim7:    
      description: 'Power limit 7 (Plim7).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    plim8:    
      description: 'Power limit 8 (Plim8).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    plim9:    
      description: 'Power Limit 9 (Plim9).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    prate:    
      description: 'Ramp rate for frequency-dependent power limit (Prate).  Typical Value = 0.017. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    r:    
      description: 'Permanent droop (R).  Typical Value = 0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rclose:    
      description: 'Minimum valve closing rate (Rclose).  Unit = PU/sec.  Typical Value = -99. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rdown:    
      description: 'Maximum rate of load limit decrease (Rdown).  Typical Value = -99. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ropen:    
      description: 'Maximum valve opening rate (Ropen).  Unit = PU/sec.  Typical Value = 99. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rselect:    
      description: 'Feedback signal for droop (Rselect).  Typical Value = electricalPower. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rup:    
      description: 'Maximum rate of load limit increase (Rup).  Typical Value = 99. Default: 0.0'    
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
    ta:    
      description: 'Acceleration limiter time constant (Ta).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tact:    
      description: 'Actuator time constant (Tact).  Typical Value = 0.4. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tb:    
      description: 'Turbine lag time constant (Tb).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tc:    
      description: 'Turbine lead time constant (Tc).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tdgov:    
      description: 'Governor derivative controller time constant (Tdgov).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    teng:    
      description: 'Transport time delay for diesel engine used in representing diesel engines where there is a small but measurable transport delay between a change in fuel flow setting and the development of torque (Teng).  Teng should be zero in all but special cases where this transport delay is of particular concern.  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tfload:    
      description: 'Load Limiter time constant (Tfload).  Typical Value = 3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tpelec:    
      description: 'Electrical power transducer time constant (Tpelec).  Typical Value = 2.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tsa:    
      description: 'Temperature detection lead time constant (Tsa).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tsb:    
      description: 'Temperature detection lag time constant (Tsb).  Typical Value = 50. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be GovCT2'    
      enum:    
        - GovCT2    
      type: Property    
    vmax:    
      description: 'Maximum valve position limit (Vmax).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vmin:    
      description: 'Minimum valve position limit (Vmin).  Typical Value = 0.175. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    wfnl:    
      description: 'No load fuel flow (Wfnl).  Typical Value = 0.187. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    wfspd:    
      description: 'Switch for fuel source characteristic to recognize that fuel flow, for a given fuel valve stroke, can be proportional to engine speed (Wfspd). true = fuel flow proportional to speed (for some gas turbines and diesel engines with positive displacement fuel injectors) false = fuel control system keeps fuel flow independent of engine speed. Typical Value = false. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un GovCT2 en format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un GovCT2 en format JSON comme normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un GovCT2 en format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un GovCT2 en format JSON-LD comme normalisé. Il est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
