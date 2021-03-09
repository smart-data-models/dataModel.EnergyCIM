Entité : Terminal  
=================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/Terminal/LICENSE.md)  
Description globale : **Adapté des modèles de données CIM. Un point de connexion électrique CA à un équipement conducteur. Les terminaux sont connectés à des points de connexion physiques appelés nœuds de connectivité.**  

## Liste des biens  

- `ConductingEquipment`: L'équipement conducteur du terminal.  Les équipements conducteurs ont des terminaux qui peuvent être connectés à d'autres terminaux d'équipements conducteurs via des nœuds de connectivité ou des nœuds topologiques. Par défaut : Aucun  - `ConnectivityNode`: Terminaux interconnectés avec une impédance nulle à ce nœud de connectivité. Par défaut : Aucun  - `ConverterDCSides`: Point de la borne de couplage commune pour ce convertisseur côté courant continu. Il s'agit généralement de la borne du transformateur de puissance (ou interrupteur) la plus proche du réseau CA. La mesure du flux de puissance doit être la somme de tous les flux entrant dans le transformateur. Par défaut : "list".  - `HasFirstMutualCoupling`: Couplages mutuels associés à la branche comme première branche. Valeur par défaut : "list".  - `HasSecondMutualCoupling`: Couplages mutuels avec la branche associée comme première branche. Valeur par défaut : "list".  - `RegulatingControl`: Le terminal associé à ce contrôle de régulation.  Le terminal est associé à la place d'un nœud, puisque le terminal pourrait se connecter soit à un nœud topologique (modèle bus en branche), soit à un nœud de connectivité (modèle détaillé de commutateur).  Il est parfois utile de modéliser la régulation à un terminal d'un objet de barre omnibus, puisque la barre omnibus peut être présente à la fois dans un modèle de branche omnibus ou un modèle avec détail de commutateur. Par défaut : Aucun  - `RemoteInputSignal`: Signal d'entrée provenant de ce terminal. Par défaut : "liste".  - `SvPowerFlow`: La variable d'état du flux d'énergie associée au terminal. Par défaut : Aucune  - `TieFlow`: La zone de contrôle relie les flux auxquels ce terminal est associé. Par défaut : "liste".  - `TopologicalNode`: Les terminaux associés au nœud topologique.   Il peut être utilisé comme alternative au chemin du nœud de connectivité vers le terminal, ce qui rend inutile la modélisation des nœuds de connectivité dans certains cas.   Notez que si les nœuds de connectivité sont dans le modèle, cette association ne sera probablement pas utilisée comme spécification d'entrée. Par défaut : Aucune  - `TransformerEnd`: Toutes les extrémités des transformateurs sont connectées à cette borne. Par défaut : "liste".  - `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `location`:   - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `phases`: Représente la condition de mise en phase normale du réseau. Si l'attribut est manquant, trois phases (ABC ou ABCN) sont supposées. Par défaut : Aucun  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `type`: Type NGSI. Il doit être de type Terminal    
Propriétés requises  
Ce modèle de données est une conversion directe du modèle commun d'information (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un mauvais type. C'est le cas, pelase soulever un problème ou envoyer un mail à alberto.abella@fiware.org  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
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
      description: 'Point of common coupling terminal for this converter DC side. It is typically the terminal on the power transformer (or switch) closest to the AC network. The power flow measurement must be the sum of all flows into the transformer. Default: "list"'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    HasFirstMutualCoupling:    
      description: 'Mutual couplings associated with the branch as the first branch. Default: "list"'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    HasSecondMutualCoupling:    
      description: 'Mutual couplings with the branch associated as the first branch. Default: "list"'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    RegulatingControl:    
      description: 'The terminal associated with this regulating control.  The terminal is associated instead of a node, since the terminal could connect into either a topological node (bus in bus-branch model) or a connectivity node (detailed switch model).  Sometimes it is useful to model regulation at a terminal of a bus bar object since the bus bar can be present in both a bus-branch model or a model with switch detail. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    RemoteInputSignal:    
      description: 'Input signal coming from this terminal. Default: "list"'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    SvPowerFlow:    
      description: 'The power flow state variable associated with the terminal. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    TieFlow:    
      description: 'The control area tie flows to which this terminal associates. Default: "list"'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    TopologicalNode:    
      description: 'The terminals associated with the topological node.   This can be used as an alternative to the connectivity node path to terminal, thus making it unneccesary to model connectivity nodes in some cases.   Note that if connectivity nodes are in the model, this association would probably not be used as an input specification. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    TransformerEnd:    
      description: 'All transformer ends connected at this terminal. Default: "list"'    
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
Non disponible l'exemple d'un terminal au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un terminal en format JSON comme normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un terminal au format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un terminal en format JSON-LD comme normalisé. Il est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
