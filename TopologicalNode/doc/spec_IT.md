Entità: TopologicalNode  
=======================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/TopologicalNode/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Adattato dai modelli di dati CIM. Per un modello dettagliato di sottostazione, un nodo topologico è un insieme di nodi di connettività che, nello stato corrente della rete, sono collegati insieme attraverso qualsiasi tipo di interruttori chiusi, compresi i ponticelli. I nodi topologici cambiano quando cambia lo stato corrente della rete (cioè, interruttori, interruttori, ecc.). Per un modello di pianificazione, gli stati degli interruttori non sono usati per formare i nodi topologici. Invece sono creati o cancellati manualmente in uno strumento di costruzione del modello. I nodi topologici mantenuti in questo modo sono anche chiamati 'bus'.**  

## Elenco delle proprietà  

- `AngleRefTopologicalIsland`: L'isola per la quale il nodo è un riferimento angolare.   Normalmente c'è un nodo di riferimento angolare per ogni isola. Predefinito: Nessuno  - `BaseVoltage`: La tensione di base del nodo topologico. Predefinito: Nessuno  - `ConnectivityNodeContainer`: Il contenitore di nodi di connettività a cui appartiene il nodo toplogico. Predefinito: Nessuno  - `ConnectivityNodes`: Il nodo topologico a cui è assegnato questo nodo di connettività.  Può dipendere dallo stato corrente degli switch nella rete. Predefinito: "elenco".  - `ReportingGroup`: I nodi topologici che appartengono al gruppo di segnalazione. Predefinito: Nessuno  - `SvInjection`: Il nodo topologico associato alla variabile di stato dell'iniezione di flusso. Predefinito: Nessuno  - `SvVoltage`: Il nodo topologico associato allo stato di tensione. Predefinito: Nessuno  - `Terminal`: Il nodo topologico associato al terminale.   Questo può essere usato come alternativa al percorso del nodo di connettività al nodo topologico, rendendo così non necessario modellare i nodi di connettività in alcuni casi.   Si noti che se i nodi di connettività sono nel modello, questa associazione probabilmente non verrebbe usata come specifica di input. Predefinito: "lista".  - `TopologicalIsland`: Un nodo topologico appartiene a un'isola topologica. Predefinito: Nessuno  - `address`: L'indirizzo postale  - `alternateName`: Un nome alternativo per questa voce  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `boundaryPoint`: Identifica se un nodo è un BoundaryPoint. Se boundaryPoint=true il ConnectivityNode o il TopologicalNode rappresenta un BoundaryPoint. Predefinito: False  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `description`: Una descrizione di questo articolo  - `fromEndIsoCode`: Questo attributo è usato per uno scambio del codice ISO della regione a cui il lato `Da` del punto di confine appartiene o a cui è collegato. Il codice ISO è un codice paese a due caratteri come definito da ISO 3166 (). La lunghezza della stringa è di massimo 2 caratteri. L'attributo è richiesto per il Boundary Model Authority Set dove questo attributo è usato solo per il TopologicalNode nel profilo Boundary Topology e ConnectivityNode nel profilo Boundary Equipment. Predefinito: ''  - `fromEndName`: L'attributo è utilizzato per uno scambio di un nome leggibile dall'uomo con lunghezza della stringa di 32 caratteri al massimo. L'attributo copre due casi:  L'attributo è richiesto per il Boundary Model Authority Set dove è usato solo per il TopologicalNode nel profilo Boundary Topology e ConnectivityNode nel profilo Boundary Equipment. Predefinito: ''  - `fromEndNameTso`: L'attributo è usato per uno scambio del nome del TSO a cui il lato `From` del punto di confine appartiene o a cui è collegato. La lunghezza della stringa è di 32 caratteri al massimo. L'attributo è richiesto per il Boundary Model Authority Set dove è usato solo per il TopologicalNode nel profilo Boundary Topology e il ConnectivityNode nel profilo Boundary Equipment. Predefinito: ''  - `id`: Identificatore unico dell'entità  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: Il nome di questo articolo.  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `toEndIsoCode`: L'attributo è usato per uno scambio del codice ISO della regione a cui il lato `A` del punto di confine appartiene o a cui è collegato. Il codice ISO è un codice paese a due caratteri come definito da ISO 3166 (). La lunghezza della stringa è di massimo 2 caratteri. L'attributo è richiesto per il Boundary Model Authority Set dove questo attributo è usato solo per il TopologicalNode nel profilo Boundary Topology e ConnectivityNode nel profilo Boundary Equipment. Predefinito: ''  - `toEndName`: L'attributo è utilizzato per uno scambio di un nome leggibile dall'uomo con lunghezza della stringa di 32 caratteri al massimo. L'attributo copre due casi:  L'attributo è richiesto per il Boundary Model Authority Set dove è usato solo per il TopologicalNode nel profilo Boundary Topology e ConnectivityNode nel profilo Boundary Equipment. Predefinito: ''  - `toEndNameTso`: L'attributo è usato per uno scambio del nome del TSO a cui il lato `To` del punto di confine appartiene o a cui è collegato. La lunghezza della stringa è di 32 caratteri al massimo. L'attributo è richiesto per il Boundary Model Authority Set dove è usato solo per il TopologicalNode nel profilo Boundary Topology e il ConnectivityNode nel profilo Boundary Equipment. Predefinito: ''  - `type`: Tipo NGSI. Deve essere TopologicalNode    
Proprietà richieste  
Adattato dai modelli di dati CIM e CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Questo modello di dati è una conversione diretta del Common Information Model (CIM) specificato dallo standard IEC61970 in modelli di dati intelligenti. Le classi python su cui si basa questo modello sono state sviluppate da queste entità Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) e RWTH University Aachen, Germania. Alcune proprietà possono avere un tipo sbagliato. Questo è stato il caso, si prega di sollevare un problema o inviare una mail a info@smartdatamodels.org.  
## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
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
        type: Property    
    BaseVoltage:    
      description: 'The base voltage of the topologocial node. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ConnectivityNodeContainer:    
      description: 'The connectivity node container to which the toplogical node belongs. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ConnectivityNodes:    
      description: 'The topological node to which this connectivity node is assigned.  May depend on the current state of switches in the network. Default: ''list'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ReportingGroup:    
      description: 'The topological nodes that belong to the reporting group. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    SvInjection:    
      description: 'The topological node associated with the flow injection state variable. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    SvVoltage:    
      description: 'The topological node associated with the voltage state. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    Terminal:    
      description: 'The topological node associated with the terminal.   This can be used as an alternative to the connectivity node path to topological node, thus making it unneccesary to model connectivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would probably not be used as an input specification. Default: ''list'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    TopologicalIsland:    
      description: 'A topological node belongs to a topological island. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
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
    boundaryPoint:    
      description: 'Identifies if a node is a BoundaryPoint. If boundaryPoint=true the ConnectivityNode or the TopologicalNode represents a BoundaryPoint. Default: False'    
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
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    fromEndIsoCode:    
      description: 'The attribute is used for an exchange of the ISO code of the region to which the `From` side of the Boundary point belongs to or it is connected to. The ISO code is two characters country code as defined by ISO 3166 (). The length of the string is 2 characters maximum. The attribute is a required for the Boundary Model Authority Set where this attribute is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: '''''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fromEndName:    
      description: 'The attribute is used for an exchange of a human readable name with length of the string 32 characters maximum. The attribute covers two cases:  The attribute is required for the Boundary Model Authority Set where it is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: '''''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fromEndNameTso:    
      description: 'The attribute is used for an exchange of the name of the TSO to which the `From` side of the Boundary point belongs to or it is connected to. The length of the string is 32 characters maximum. The attribute is required for the Boundary Model Authority Set where it is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: '''''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
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
      x-ngsi:    
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
        anyOf: *topologicalnode_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    toEndIsoCode:    
      description: 'The attribute is used for an exchange of the ISO code of the region to which the `To` side of the Boundary point belongs to or it is connected to. The ISO code is two characters country code as defined by ISO 3166 (). The length of the string is 2 characters maximum. The attribute is a required for the Boundary Model Authority Set where this attribute is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: '''''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    toEndName:    
      description: 'The attribute is used for an exchange of a human readable name with length of the string 32 characters maximum. The attribute covers two cases:  The attribute is required for the Boundary Model Authority Set where it is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: '''''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    toEndNameTso:    
      description: 'The attribute is used for an exchange of the name of the TSO to which the `To` side of the Boundary point belongs to or it is connected to. The length of the string is 32 characters maximum. The attribute is required for the Boundary Model Authority Set where it is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: '''''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be TopologicalNode'    
      enum:    
        - TopologicalNode    
      type: string    
      x-ngsi:    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/TopologicalNode/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/TopologicalNode/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## Esempio di payloads  
Non è disponibile l'esempio di un TopologicalNode in formato JSON-LD come key-values. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
Non disponibile l'esempio di un TopologicalNode in formato JSON-LD come normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
Non è disponibile l'esempio di un TopologicalNode in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
Non disponibile l'esempio di un TopologicalNode in formato JSON-LD come normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per avere una risposta su come trattare le unità di grandezza