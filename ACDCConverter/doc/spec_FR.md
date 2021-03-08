Entité : ACDCConverter  
======================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ACDCConverter/LICENSE.md)  
Description globale : **Adapté des modèles de données CIM. Une unité avec des vannes pour trois phases, ainsi que l'équipement de commande de l'unité, les dispositifs de protection et de commutation essentiels, les condensateurs de stockage de courant continu, les réacteurs de phase et les auxiliaires, le cas échéant, utilisés pour la conversion.**  

## Liste des biens  

- `DCTerminals`:  Par défaut : "liste".  - `PccTerminal`: Tous les côtés CC des convertisseurs sont reliés à ce point de la borne de couplage commune. Par défaut : Aucun  - `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `baseS`: Puissance apparente de base du pôle de conversion. Valeur par défaut : 0,0  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `idc`: Convertisseur de courant continu, également appelé Id. Variable d'état du convertisseur, résultant du flux de puissance. Valeur par défaut : 0.0  - `idleLoss`: Perte de puissance active dans le pôle sans transfert de puissance. Données de configuration du convertisseur utilisées dans le flux de puissance. Valeur par défaut : 0,0  - `location`:   - `maxUdc`: La tension maximale du côté du courant continu à laquelle le convertisseur doit fonctionner. Données de configuration du convertisseur utilisées dans le flux de puissance. Valeur par défaut : 0,0  - `minUdc`: Tension continue minimale autorisée du convertisseur. Données de configuration du convertisseur utilisées dans le flux de puissance. Valeur par défaut : 0,0  - `name`: Le nom de cet article.  - `numberOfValves`: Nombre de valves dans le convertisseur. Utilisé dans le calcul des pertes. Valeur par défaut : 0  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `p`: Puissance active au point de couplage commun. La convention de signe de charge est utilisée, c'est-à-dire que le signe positif signifie que l'énergie sort d'un nœud. Valeur de départ pour une solution en régime permanent dans le cas où un modèle simplifié de flux de puissance est utilisé. Valeur par défaut : 0.0  - `poleLossP`: La perte de puissance active à un pôle DC = idleLoss + switchingLoss*|Idc| + resitiveLoss*Idc^2 Pour un fonctionnement sans perte Pdc=Pac Pour un fonctionnement avec pertes Pdc=Pac-lossP Pour un fonctionnement avec pertes Pdc=Pac+lossP Variable d'état du convertisseur utilisée dans le flux de puissance. Valeur par défaut : 0,0  - `q`: Puissance réactive au point de couplage commun. La convention de signe de charge est utilisée, c'est-à-dire que le signe positif signifie le flux sortant d'un nœud. Valeur de départ pour une solution en régime permanent dans le cas où un modèle simplifié de flux de puissance est utilisé. Valeur par défaut : 0,0  - `ratedUdc`: Tension continue nominale du convertisseur, également appelée UdN. Données de configuration du convertisseur utilisées dans le flux de puissance. Valeur par défaut : 0,0  - `resistiveLoss`: Données de configuration du convertisseur utilisées dans le flux d'énergie. Se référer à poleLossP. Valeur par défaut : 0.0  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `switchingLoss`: Pertes de commutation, par rapport à la puissance apparente de base "baseS". Se référer à la perte de pôleP. Valeur par défaut : 0.0  - `targetPpcc`: Cible réelle d'injection de puissance dans le réseau CA, au point de couplage commun. Valeur par défaut : 0,0  - `targetUdc`: Valeur cible pour l'amplitude de la tension continue. Valeur par défaut : 0,0  - `type`: Type NGSI. Il doit être de type ACDCConverter  - `uc`: Tension du convertisseur, c'est-à-dire la tension du côté CA du pont. Variable d'état du convertisseur, résultat du flux de puissance. Valeur par défaut : 0,0  - `udc`: La tension du convertisseur côté courant continu, également appelée Ud. La variable d'état du convertisseur, résulte du flux de puissance. Valeur par défaut : 0,0  - `valveU0`: Tension de seuil de la vanne. Chute de tension en avant lorsque la vanne est conductrice. Utilisée dans les calculs de perte, c'est-à-dire que la perte de commutation dépend du nombre de soupapes * soupapeU0. Valeur par défaut : 0,0    
Propriétés requises  
Ce modèle de données est une conversion directe du modèle commun d'information (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un mauvais type. C'est le cas, pelase soulever un problème ou envoyer un mail à alberto.abella@fiware.org  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ACDCConverter:    
  description: 'Adapted from CIM data models. A unit with valves for three phases, together with unit control equipment, essential protective and switching devices, DC storage capacitors, phase reactors and auxiliaries, if any, used for conversion.'    
  properties:    
    DCTerminals:    
      description: ' Default: "list"'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    PccTerminal:    
      description: 'All converters` DC sides linked to this point of common coupling terminal. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    baseS:    
      description: 'Base apparent power of the converter pole. Default: 0.0'    
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
    id:    
      anyOf: &acdcconverter_-_properties_-_owner_-_items_-_anyof    
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
    idc:    
      description: 'Converter DC current, also called Id. Converter state variable, result from power flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    idleLoss:    
      description: 'Active power loss in pole at no power transfer. Converter configuration data used in power flow. Default: 0.0'    
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
    maxUdc:    
      description: 'The maximum voltage on the DC side at which the converter should operate. Converter configuration data used in power flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    minUdc:    
      description: 'Min allowed converter DC voltage. Converter configuration data used in power flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    name:    
      description: 'The name of this item.'    
      type: Property    
    numberOfValves:    
      description: 'Number of valves in the converter. Used in loss calculations. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *acdcconverter_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    p:    
      description: 'Active power at the point of common coupling. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution in the case a simplified power flow model is used. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    poleLossP:    
      description: 'The active power loss at a DC Pole  = idleLoss + switchingLoss*|Idc| + resitiveLoss*Idc^2 For lossless operation Pdc=Pac For rectifier operation with losses Pdc=Pac-lossP For inverter operation with losses Pdc=Pac+lossP Converter state variable used in power flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    q:    
      description: 'Reactive power at the point of common coupling. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution in the case a simplified power flow model is used. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ratedUdc:    
      description: 'Rated converter DC voltage, also called UdN. Converter configuration data used in power flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    resistiveLoss:    
      description: 'Converter configuration data used in power flow. Refer to poleLossP. Default: 0.0'    
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
    switchingLoss:    
      description: 'Switching losses, relative to the base apparent power `baseS`. Refer to poleLossP. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    targetPpcc:    
      description: 'Real power injection target in AC grid, at point of common coupling. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    targetUdc:    
      description: 'Target value for DC voltage magnitude. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be ACDCConverter'    
      enum:    
        - ACDCConverter    
      type: Property    
    uc:    
      description: 'Converter voltage, the voltage at the AC side of the bridge. Converter state variable, result from power flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    udc:    
      description: 'Converter voltage at the DC side, also called Ud. Converter state variable, result from power flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    valveU0:    
      description: 'Valve threshold voltage. Forward voltage drop when the valve is conducting. Used in loss calculations, i.e. the switchLoss depend on numberOfValves * valveU0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un ACDCConverter au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un ACDCConverter au format JSON comme normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un ACDCConverter au format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un ACDCConverter au format JSON-LD comme normalisé. Il est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
