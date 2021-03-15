Entité : TopologicalNode  
========================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/TopologicalNode/LICENSE.md)  
Description globale : **Adapté des modèles de données CIM. Pour un modèle de poste détaillé, un nœud topologique est un ensemble de nœuds de connectivité qui, dans l'état actuel du réseau, sont reliés entre eux par tout type de commutateurs fermés, y compris les cavaliers. Les nœuds topologiques changent lorsque l'état actuel du réseau change (c'est-à-dire lorsque les commutateurs, les disjoncteurs, etc. changent d'état). Pour un modèle de planification, les états des commutateurs ne sont pas utilisés pour former les nœuds topologiques. Ils sont plutôt créés ou supprimés manuellement dans un outil de construction de modèle. Les nœuds topologiques gérés de cette manière sont également appelés "bus".  

## Liste des propriétés  

- `AngleRefTopologicalIsland`: L'île pour laquelle le nœud est une référence d'angle.   Normalement, il y a un nœud de référence angulaire pour chaque île. Valeur par défaut : Aucun  - `BaseVoltage`: La tension de base du noeud topologique. Par défaut : Aucun  - `ConnectivityNodeContainer`: Le conteneur de nœuds de connectivité auquel appartient le nœud toplogique. Valeur par défaut : Aucun  - `ConnectivityNodes`: Le nœud topologique auquel ce nœud de connectivité est affecté.  Peut dépendre de l'état actuel des commutateurs du réseau. Valeur par défaut : "list".  - `ReportingGroup`: Les noeuds topologiques qui appartiennent au groupe de rapport. Valeur par défaut : Aucun  - `SvInjection`: Le noeud topologique associé à la variable d'état d'injection de flux. Valeur par défaut : Aucun  - `SvVoltage`: Le nœud topologique associé à l'état de tension. Par défaut : Aucun  - `Terminal`: Le nœud topologique associé au terminal.   Il peut être utilisé comme alternative au chemin du noeud de connectivité vers le noeud topologique, rendant ainsi inutile la modélisation des noeuds de connectivité dans certains cas.   Notez que si les noeuds de connectivité sont dans le modèle, cette association ne sera probablement pas utilisée comme spécification d'entrée. Valeur par défaut : 'list'.  - `TopologicalIsland`: Un nœud topologique appartient à un îlot topologique. Valeur par défaut : Aucun  - `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `boundaryPoint`: Identifie si un noeud est un BoundaryPoint. Si boundaryPoint=true, le ConnectivityNode ou le TopologicalNode représente un BoundaryPoint. Valeur par défaut : False  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `fromEndIsoCode`: Cet attribut est utilisé pour l'échange du code ISO de la région à laquelle le côté "From" du point de frontière appartient ou à laquelle il est connecté. Le code ISO est un code pays à deux caractères tel que défini par la norme ISO 3166 (). La longueur de la chaîne est de 2 caractères maximum. Cet attribut est obligatoire pour l'ensemble d'autorités du modèle Boundary où il n'est utilisé que pour le TopologicalNode du profil Boundary Topology et le ConnectivityNode du profil Boundary Equipment. Valeur par défaut : ''.  - `fromEndName`: L'attribut est utilisé pour l'échange d'un nom lisible par l'homme avec une longueur de la chaîne de 32 caractères maximum. L'attribut couvre deux cas :  L'attribut est requis pour l'ensemble d'autorités du modèle frontalier où il est utilisé uniquement pour le TopologicalNode dans le profil de topologie frontalier et le ConnectivityNode dans le profil d'équipement frontalier. Valeur par défaut : "  - `fromEndNameTso`: Cet attribut est utilisé pour l'échange du nom du TSO auquel le côté "From" du point de frontière appartient ou auquel il est connecté. La longueur de la chaîne est de 32 caractères maximum. Cet attribut est requis pour l'ensemble d'autorités du modèle Boundary où il est utilisé uniquement pour le TopologicalNode dans le profil Boundary Topology et le ConnectivityNode dans le profil Boundary Equipment. Valeur par défaut : "  - `id`: Identifiant unique de l'entité  - `location`:   - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `toEndIsoCode`: Cet attribut est utilisé pour l'échange du code ISO de la région à laquelle le côté "à" du point de délimitation appartient ou à laquelle il est connecté. Le code ISO est un code pays à deux caractères tel que défini par la norme ISO 3166 (). La longueur de la chaîne est de 2 caractères maximum. Cet attribut est obligatoire pour l'ensemble d'autorités du modèle Boundary où il n'est utilisé que pour le TopologicalNode du profil Boundary Topology et le ConnectivityNode du profil Boundary Equipment. Valeur par défaut : ''.  - `toEndName`: L'attribut est utilisé pour l'échange d'un nom lisible par l'homme avec une longueur de la chaîne de 32 caractères maximum. L'attribut couvre deux cas :  L'attribut est requis pour l'ensemble d'autorités du modèle frontalier où il est utilisé uniquement pour le TopologicalNode dans le profil de topologie frontalier et le ConnectivityNode dans le profil d'équipement frontalier. Valeur par défaut : "  - `toEndNameTso`: Cet attribut est utilisé pour l'échange du nom du TSO auquel appartient ou auquel est connecté le côté "à" du point de frontière. La longueur de la chaîne est de 32 caractères maximum. Cet attribut est requis pour l'ensemble d'autorités du modèle Boundary où il est utilisé uniquement pour le TopologicalNode dans le profil Boundary Topology et le ConnectivityNode dans le profil Boundary Equipment. Valeur par défaut : "  - `type`: Type de NGSI. Il doit être TopologicalNode    
Propriétés requises  
Ce modèle de données est une conversion directe du modèle d'information commun (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un type incorrect. Si tel était le cas, veuillez soulever un problème ou envoyer un message à alberto.abella@fiware.org.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
TopologicalNode:    
  description: 'Adapted from CIM data models. For a detailed substation model a topological node is a set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes change as the current network state changes (i.e., switches, breakers, etc. change state). For a planning model, switch statuses are not used to form topological nodes. Instead they are manually created or deleted in a model builder tool. Topological nodes maintained this way are also called ''busses''.'    
  properties:    
    AngleRefTopologicalIsland:    
      description: 'The island for which the node is an angle reference.   Normally there is one angle reference node for each island. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    BaseVoltage:    
      description: 'The base voltage of the topologocial node. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ConnectivityNodeContainer:    
      description: 'The connectivity node container to which the toplogical node belongs. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ConnectivityNodes:    
      description: 'The topological node to which this connectivity node is assigned.  May depend on the current state of switches in the network. Default: ''list'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ReportingGroup:    
      description: 'The topological nodes that belong to the reporting group. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    SvInjection:    
      description: 'The topological node associated with the flow injection state variable. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    SvVoltage:    
      description: 'The topological node associated with the voltage state. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    Terminal:    
      description: 'The topological node associated with the terminal.   This can be used as an alternative to the connectivity node path to topological node, thus making it unneccesary to model connectivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would probably not be used as an input specification. Default: ''list'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    TopologicalIsland:    
      description: 'A topological node belongs to a topological island. Default: None'    
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
    boundaryPoint:    
      description: 'Identifies if a node is a BoundaryPoint. If boundaryPoint=true the ConnectivityNode or the TopologicalNode represents a BoundaryPoint. Default: False'    
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
    fromEndIsoCode:    
      description: 'The attribute is used for an exchange of the ISO code of the region to which the `From` side of the Boundary point belongs to or it is connected to. The ISO code is two characters country code as defined by ISO 3166 (). The length of the string is 2 characters maximum. The attribute is a required for the Boundary Model Authority Set where this attribute is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: '''''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fromEndName:    
      description: 'The attribute is used for an exchange of a human readable name with length of the string 32 characters maximum. The attribute covers two cases:  The attribute is required for the Boundary Model Authority Set where it is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: '''''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fromEndNameTso:    
      description: 'The attribute is used for an exchange of the name of the TSO to which the `From` side of the Boundary point belongs to or it is connected to. The length of the string is 32 characters maximum. The attribute is required for the Boundary Model Authority Set where it is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: '''''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &topologicalnode_-_properties_-_owner_-_items_-_anyof    
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
        anyOf: *topologicalnode_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
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
    toEndIsoCode:    
      description: 'The attribute is used for an exchange of the ISO code of the region to which the `To` side of the Boundary point belongs to or it is connected to. The ISO code is two characters country code as defined by ISO 3166 (). The length of the string is 2 characters maximum. The attribute is a required for the Boundary Model Authority Set where this attribute is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: '''''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    toEndName:    
      description: 'The attribute is used for an exchange of a human readable name with length of the string 32 characters maximum. The attribute covers two cases:  The attribute is required for the Boundary Model Authority Set where it is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: '''''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    toEndNameTso:    
      description: 'The attribute is used for an exchange of the name of the TSO to which the `To` side of the Boundary point belongs to or it is connected to. The length of the string is 32 characters maximum. The attribute is required for the Boundary Model Authority Set where it is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: '''''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be TopologicalNode'    
      enum:    
        - TopologicalNode    
      type: Property    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un TopologicalNode au format JSON comme key-values. Ceci est compatible avec NGSI V2 quand on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un TopologicalNode au format JSON tel que normalisé. Ceci est compatible avec la NGSI V2 lorsqu'elle n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un TopologicalNode au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-LD quand on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un TopologicalNode au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
