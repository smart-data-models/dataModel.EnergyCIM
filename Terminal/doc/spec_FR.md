Entité : Terminal  
=================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/Terminal/LICENSE.md)  
Description globale : **Adapté des modèles de données CIM. Un point de connexion électrique en courant alternatif à un équipement conducteur. Les bornes sont connectées à des points de connexion physiques appelés nœuds de connectivité**.  

## Liste des propriétés  

- `ConductingEquipment`: L'équipement conducteur du terminal.  Les équipements conducteurs ont des terminaux qui peuvent être connectés à d'autres terminaux d'équipements conducteurs via des nœuds de connectivité ou des nœuds topologiques. Valeur par défaut : Aucun  - `ConnectivityNode`: Bornes interconnectées avec une impédance nulle à ce nœud de connectivité. Valeur par défaut : Aucun  - `ConverterDCSides`: Borne du point de couplage commun pour le côté CC de ce convertisseur. Il s'agit généralement de la borne du transformateur de puissance (ou du commutateur) la plus proche du réseau CA. La mesure du flux de puissance doit être la somme de tous les flux dans le transformateur. Valeur par défaut : 'list'.  - `HasFirstMutualCoupling`: Couplages mutuels associés à la branche comme première branche. Valeur par défaut : 'list'.  - `HasSecondMutualCoupling`: Couplages mutuels avec la branche associée comme première branche. Valeur par défaut : 'list'.  - `RegulatingControl`: La borne associée à cette commande de régulation.  La borne est associée au lieu d'un nœud, car la borne pourrait se connecter soit à un nœud topologique (bus dans un modèle de bus-branche), soit à un nœud de connectivité (modèle détaillé d'interrupteur).  Il est parfois utile de modéliser la régulation au niveau d'une borne d'un objet de barre omnibus, car la barre omnibus peut être présente à la fois dans un modèle de branche omnibus et dans un modèle détaillé d'interrupteur. Valeur par défaut : Aucun  - `RemoteInputSignal`: Signal d'entrée provenant de ce terminal. Valeur par défaut : 'list'.  - `SvPowerFlow`: La variable d'état du flux de puissance associée au terminal. Valeur par défaut : Aucun  - `TieFlow`: Les flux d'attache de la zone de contrôle auxquels ce terminal s'associe. Valeur par défaut : "list".  - `TopologicalNode`: Les terminaux associés au noeud topologique.   Ceci peut être utilisé comme une alternative au chemin du nœud de connectivité vers le terminal, rendant ainsi inutile la modélisation des nœuds de connectivité dans certains cas.   Notez que si les noeuds de connectivité sont dans le modèle, cette association ne sera probablement pas utilisée comme spécification d'entrée. Par défaut : Aucun  - `TransformerEnd`: Toutes les extrémités du transformateur connectées à cette borne. Valeur par défaut : 'list'.  - `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `location`:   - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `phases`: Représente la condition normale de mise en phase du réseau. Si l'attribut est absent, trois phases (ABC ou ABCN) sont supposées. Valeur par défaut : Aucun  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type`: Type de NGSI. Il doit être Terminal    
Propriétés requises  
Ce modèle de données est une conversion directe du modèle d'information commun (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un type incorrect. Si tel était le cas, veuillez soulever un problème ou envoyer un message à alberto.abella@fiware.org.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Terminal:    
  description: 'Adapted from CIM data models. An AC electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called connectivity nodes.'    
  properties:    
    ConductingEquipment:    
      description: 'The conducting equipment of the terminal.  Conducting equipment have  terminals that may be connected to other conducting equipment terminals via connectivity nodes or topological nodes. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ConnectivityNode:    
      description: 'Terminals interconnected with zero impedance at a this connectivity node. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ConverterDCSides:    
      description: 'Point of common coupling terminal for this converter DC side. It is typically the terminal on the power transformer (or switch) closest to the AC network. The power flow measurement must be the sum of all flows into the transformer. Default: ''list'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    HasFirstMutualCoupling:    
      description: 'Mutual couplings associated with the branch as the first branch. Default: ''list'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    HasSecondMutualCoupling:    
      description: 'Mutual couplings with the branch associated as the first branch. Default: ''list'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    RegulatingControl:    
      description: 'The terminal associated with this regulating control.  The terminal is associated instead of a node, since the terminal could connect into either a topological node (bus in bus-branch model) or a connectivity node (detailed switch model).  Sometimes it is useful to model regulation at a terminal of a bus bar object since the bus bar can be present in both a bus-branch model or a model with switch detail. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    RemoteInputSignal:    
      description: 'Input signal coming from this terminal. Default: ''list'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    SvPowerFlow:    
      description: 'The power flow state variable associated with the terminal. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    TieFlow:    
      description: 'The control area tie flows to which this terminal associates. Default: ''list'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    TopologicalNode:    
      description: 'The terminals associated with the topological node.   This can be used as an alternative to the connectivity node path to terminal, thus making it unneccesary to model connectivity nodes in some cases.   Note that if connectivity nodes are in the model, this association would probably not be used as an input specification. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    TransformerEnd:    
      description: 'All transformer ends connected at this terminal. Default: ''list'''    
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
      anyOf: &terminal_-_properties_-_owner_-_items_-_anyof    
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
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *terminal_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    phases:    
      description: 'Represents the normal network phasing condition. If the attribute is missing three phases (ABC or ABCN) shall be assumed. Default: None'    
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
    type:    
      description: 'NGSI type. It has to be Terminal'    
      enum:    
        - Terminal    
      type: Property    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un Terminal au format JSON comme key-values. Ceci est compatible avec NGSI V2 lorsqu'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un Terminal au format JSON tel que normalisé. Ceci est compatible avec NGSI V2 lorsqu'on n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un Terminal au format JSON-LD en tant que key-values. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un Terminal au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
