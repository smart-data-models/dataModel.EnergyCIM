Entité : GovCT1  
===============  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovCT1/LICENSE.md)  
Description globale : **Adapté des modèles de données du CIM. Modèle général pour tout moteur d'entraînement avec un régulateur PID, utilisé principalement pour les turbines à combustion et les unités à cycle combiné. Ce modèle peut être utilisé pour représenter une variété de moteurs d'entraînement contrôlés par des régulateurs PID.  Il convient, par exemple, pour la représentation de Des informations supplémentaires sur ce modèle sont disponibles dans le rapport 2012 de l'IEEE, section 3.1.2.3 page 3-4 (GGOV1).  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `aset`: Point de consigne du limiteur d'accélération (Aset).  Unité = PU/sec.  Valeur typique = 0.01. Valeur par défaut : 0.0  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `db`: Bande morte du régulateur de vitesse par unité de vitesse (db).  Dans la majorité des applications, il est recommandé de régler cette valeur sur zéro.  Valeur typique = 0. Valeur par défaut : 0.0  - `description`: Une description de cet article  - `dm`: Coefficient de sensibilité à la vitesse (Dm).  Dm peut représenter soit la variation de la puissance du moteur en fonction de la vitesse de l'arbre, soit la variation de la capacité de puissance maximale en fonction de la vitesse de l'arbre.  S'il est positif, il décrit la pente descendante de la caractéristique vitesse/puissance du moteur lorsque la vitesse augmente. Une caractéristique légèrement descendante est typique des moteurs alternatifs et de certaines turbines aérodérivatives.  Si elle est négative, la puissance du moteur est supposée ne pas être affectée par la vitesse de l'arbre, mais le débit maximal de carburant admissible est supposé diminuer avec la vitesse de l'arbre. Ceci est caractéristique des turbines industrielles à arbre unique en raison des limites de température d'échappement.  Valeur typique = 0. Valeur par défaut : 0.0  - `id`: Identifiant unique de l'entité  - `ka`: Gain du limiteur d'accélération (Ka).  Valeur typique = 10. Valeur par défaut : 0.0  - `kdgov`: Gain de la dérivation du gouverneur (Kdgov).  Valeur typique = 0. Valeur par défaut : 0.0  - `kigov`: Gain intégral du gouverneur (Kigov).  Valeur typique = 2. Valeur par défaut : 0.0  - `kiload`: Gain intégral du limiteur de charge pour le contrôleur PI (Kiload).  Valeur typique = 0.67. Valeur par défaut : 0.0  - `kimw`: Gain du contrôleur de puissance (réinitialisation) (Kimw).  La valeur par défaut de 0,01 correspond à un temps de réinitialisation de 100 secondes.  Une valeur de 0,001 correspond à un contrôleur de puissance à action relativement lente.  Valeur typique = 0,01. Valeur par défaut : 0.0  - `kpgov`: Gain proportionnel du gouverneur (Kpgov).  Valeur typique = 10. Valeur par défaut : 0.0  - `kpload`: Gain proportionnel du limiteur de charge pour le contrôleur PI (Kpload).  Valeur typique = 2. Valeur par défaut : 0.0  - `kturb`: Gain de la turbine (Kturb) (>0).  Valeur typique = 1,5. Valeur par défaut : 0,0  - `ldref`: Valeur de référence du limiteur de charge (Ldref).  Valeur typique = 1. Valeur par défaut : 0.0  - `location`:   - `maxerr`: Valeur maximale du signal d'erreur de vitesse (maxerr).  Valeur typique = 0,05. Valeur par défaut : 0.0  - `minerr`: Valeur minimale du signal d'erreur de vitesse (minerr).  Valeur typique = -0.05. Valeur par défaut : 0.0  - `mwbase`: Base pour les valeurs de puissance (MWbase) (> 0).  Unité = MW. Valeur par défaut : 0.0  - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `r`: Chute permanente (R).  Valeur typique = 0.04. Valeur par défaut : 0.0  - `rclose`: Taux de fermeture minimum de la vanne (Rclose).  Unité = PU/sec.  Valeur typique = -0.1. Valeur par défaut : 0.0  - `rdown`: Taux maximal de diminution de la limite de charge (Rdown).  Valeur typique = -99. Valeur par défaut : 0.0  - `ropen`: Taux d'ouverture maximal de la vanne (Ropen).  Unité = PU/sec.  Valeur typique = 0.10. Valeur par défaut : 0.0  - `rselect`: Signal de retour pour le droop (Rselect).  Valeur typique = electricPower. Valeur par défaut : Aucun  - `rup`: Taux maximal d'augmentation de la limite de charge (Rup).  Valeur typique = 99. Valeur par défaut : 0.0  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `ta`: Constante de temps du limiteur d'accélération (Ta) (>0).  Valeur typique = 0,1. Valeur par défaut : 0  - `tact`: Constante de temps de l'actionneur (Tact).  Valeur typique = 0,5. Valeur par défaut : 0  - `tb`: Constante de temps de retard de la turbine (Tb) (>0).  Valeur typique = 0,5. Valeur par défaut : 0  - `tc`: Constante de temps d'avance de la turbine (Tc).  Valeur typique = 0. Valeur par défaut : 0  - `tdgov`: Constante de temps du contrôleur de dérivation du gouverneur (Tdgov).  Valeur typique = 1. Valeur par défaut : 0  - `teng`: Retard de transport pour moteur diesel utilisé dans la représentation des moteurs diesel où il existe un retard de transport faible mais mesurable entre une modification du réglage du débit de carburant et le développement du couple (Teng).  Teng doit être égal à zéro dans tous les cas, sauf les cas particuliers où ce délai de transport est particulièrement important.  Valeur typique = 0. Valeur par défaut : 0  - `tfload`: Constante de temps du limiteur de charge (Tfload) (>0).  Valeur typique = 3. Valeur par défaut : 0  - `tpelec`: Constante de temps du transducteur de puissance électrique (Tpelec) (>0).  Valeur typique = 1. Valeur par défaut : 0  - `tsa`: Constante de temps de la détection de la température (Tsa).  Valeur typique = 4. Valeur par défaut : 0  - `tsb`: Constante de temps de retard de la détection de la température (Tsb).  Valeur typique = 5. Valeur par défaut : 0  - `type`: Type de NGSI. Il doit être GovCT1  - `vmax`: Limite de position maximale de la vanne (Vmax).  Valeur typique = 1. Valeur par défaut : 0.0  - `vmin`: Limite de position minimale de la vanne (Vmin).  Valeur typique = 0.15. Valeur par défaut : 0.0  - `wfnl`: Débit de carburant à vide (Wfnl).  Valeur typique = 0,2. Valeur par défaut : 0.0  - `wfspd`: Commutateur pour la caractéristique de la source de carburant afin de reconnaître que le débit de carburant, pour une course de soupape de carburant donnée, peut être proportionnel à la vitesse du moteur (Wfspd). true = débit de carburant proportionnel à la vitesse (pour certaines turbines à gaz et moteurs diesel avec injecteurs de carburant à déplacement positif) false = le système de contrôle du carburant maintient le débit de carburant indépendant de la vitesse du moteur. Valeur typique = true. Valeur par défaut : False    
Propriétés requises  
Ce modèle de données est une conversion directe du modèle d'information commun (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un type incorrect. Si tel était le cas, veuillez soulever un problème ou envoyer un message à alberto.abella@fiware.org.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GovCT1:    
  description: 'Adapted from CIM data models. General model for any prime mover with a PID governor, used primarily for combustion turbine and combined cycle units. This model can be used to represent a variety of prime movers controlled by PID governors.  It is suitable, for example, for representation of     Additional information on this model is available in the 2012 IEEE report, , section 3.1.2.3 page 3-4 (GGOV1).'    
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
    aset:    
      description: 'Acceleration limiter setpoint (Aset).  Unit = PU/sec.  Typical Value = 0.01. Default: 0.0'    
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
    id:    
      anyOf: &govct1_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Acceleration limiter gain (Ka).  Typical Value = 10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kdgov:    
      description: 'Governor derivative gain (Kdgov).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kigov:    
      description: 'Governor integral gain (Kigov).  Typical Value = 2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kiload:    
      description: 'Load limiter integral gain for PI controller (Kiload).  Typical Value = 0.67. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kimw:    
      description: 'Power controller (reset) gain (Kimw).  The default value of 0.01 corresponds to a reset time of 100 seconds.  A value of 0.001 corresponds to a relatively slow acting load controller.  Typical Value = 0.01. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kpgov:    
      description: 'Governor proportional gain (Kpgov).  Typical Value = 10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kpload:    
      description: 'Load limiter proportional gain for PI controller (Kpload).  Typical Value = 2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kturb:    
      description: 'Turbine gain (Kturb) (>0).  Typical Value = 1.5. Default: 0.0'    
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
      description: 'Maximum value for speed error signal (maxerr).  Typical Value = 0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    minerr:    
      description: 'Minimum value for speed error signal (minerr).  Typical Value = -0.05. Default: 0.0'    
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
        anyOf: *govct1_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    r:    
      description: 'Permanent droop (R).  Typical Value = 0.04. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rclose:    
      description: 'Minimum valve closing rate (Rclose).  Unit = PU/sec.  Typical Value = -0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rdown:    
      description: 'Maximum rate of load limit decrease (Rdown).  Typical Value = -99. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ropen:    
      description: 'Maximum valve opening rate (Ropen).  Unit = PU/sec.  Typical Value = 0.10. Default: 0.0'    
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
      description: 'Acceleration limiter time constant (Ta) (>0).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tact:    
      description: 'Actuator time constant (Tact).  Typical Value = 0.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tb:    
      description: 'Turbine lag time constant (Tb) (>0).  Typical Value = 0.5. Default: 0'    
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
      description: 'Load Limiter time constant (Tfload) (>0).  Typical Value = 3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tpelec:    
      description: 'Electrical power transducer time constant (Tpelec) (>0).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tsa:    
      description: 'Temperature detection lead time constant (Tsa).  Typical Value = 4. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tsb:    
      description: 'Temperature detection lag time constant (Tsb).  Typical Value = 5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be GovCT1'    
      enum:    
        - GovCT1    
      type: Property    
    vmax:    
      description: 'Maximum valve position limit (Vmax).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vmin:    
      description: 'Minimum valve position limit (Vmin).  Typical Value = 0.15. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    wfnl:    
      description: 'No load fuel flow (Wfnl).  Typical Value = 0.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    wfspd:    
      description: 'Switch for fuel source characteristic to recognize that fuel flow, for a given fuel valve stroke, can be proportional to engine speed (Wfspd). true = fuel flow proportional to speed (for some gas turbines and diesel engines with positive displacement fuel injectors) false = fuel control system keeps fuel flow independent of engine speed. Typical Value = true. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un GovCT1 au format JSON comme valeurs-clés. Ceci est compatible avec la NGSI V2 lorsqu'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un GovCT1 au format JSON tel que normalisé. Ceci est compatible avec la NGSI V2 lorsqu'elle n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un GovCT1 au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et retourne les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un GovCT1 au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
