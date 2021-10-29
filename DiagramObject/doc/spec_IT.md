Entità: DiagramObject  
=====================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/DiagramObject/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Adattato dai modelli di dati CIM. Un oggetto che definisce uno o più punti in un dato spazio. Questo oggetto può essere associato a qualsiasi cosa che specializza IdentifiedObject. Per i diagrammi a linea singola tali oggetti includono tipicamente elementi come valori analogici, interruttori, sezionatori, trasformatori di potenza e linee di trasmissione.  

## Elenco delle proprietà  

- `Diagram`: Un oggetto diagramma è parte di un diagramma. Predefinito: Nessuno  - `DiagramObjectPoints`: Un oggetto diagramma può avere 0 o più punti per riflettere la sua posizione di layout, il percorso (per le polilinee) o il confine (per i poligoni). Predefinito: "elenco".  - `DiagramObjectStyle`: Un oggetto diagramma ha uno stile associato che fornisce un riferimento per lo stile usato nel sistema di origine. Predefinito: Nessuno  - `IdentifiedObject`: Gli oggetti del diagramma che sono associati all'oggetto dominio. Predefinito: Nessuno  - `VisibilityLayers`: Un oggetto diagramma può essere parte di più livelli di visibilità. Predefinito: "elenco".  - `address`: L'indirizzo postale  - `alternateName`: Un nome alternativo per questa voce  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `description`: Una descrizione di questo articolo  - `drawingOrder`: L'ordine di disegno di questo elemento. Più alto è il numero, più tardi viene disegnato l'elemento in sequenza. Questo è usato per assicurare che gli elementi che si sovrappongono siano resi nell'ordine corretto. Predefinito: 0  - `id`: Identificatore unico dell'entità  - `isPolygon`: Definisce se i punti degli oggetti diagramma definiscono o meno i confini di un poligono o il percorso di una polilinea. Se questo valore è true, allora un'applicazione ricevente dovrebbe considerare il primo e l'ultimo punto come collegati. Predefinito: False  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: Il nome di questo articolo.  - `offsetX`: L'offset nella direzione X. Questo è usato per definire l'offset dal centro per il rendering di un'icona (l'impostazione predefinita è che un singolo punto specifichi il centro dell'icona).  L'offset è in unità con 0 che indica che non c'è alcun offset dal centro orizzontale dell'icona.  -0.5 indica che c'è un offset del 50% a sinistra e 0.5 indica un offset del 50% a destra. Predefinito: 0.0  - `offsetY`: L'offset nella direzione Y. Questo è usato per definire l'offset dal centro per il rendering di un'icona (l'impostazione predefinita è che un singolo punto specifichi il centro dell'icona).  L'offset è in per-unità con 0 che indica che non c'è alcun offset dal centro verticale dell'icona.  La direzione dell'offset dipende dall'orientamento del diagramma, con -0,5 e 0,5 che indicano un offset di +/- 50% sull'asse verticale. Predefinito: 0.0  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `rotation`: Imposta l'angolo di rotazione dell'oggetto diagramma.  Zero gradi punta alla parte superiore del diagramma.  La rotazione è in senso orario. Predefinito: 0,0  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `type`: Tipo NGSI. Deve essere DiagramObject    
Proprietà richieste  
Adattato dai modelli di dati CIM e CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Questo modello di dati è una conversione diretta del Common Information Model (CIM) specificato dallo standard IEC61970 in modelli di dati intelligenti. Le classi python su cui si basa questo modello sono state sviluppate da queste entità Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) e RWTH University Aachen, Germania. Alcune proprietà possono avere un tipo sbagliato. Questo è stato il caso, si prega di sollevare un problema o inviare una mail a info@smartdatamodels.org.  
## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
DiagramObject:    
  description: 'Adapted from CIM data models. An object that defines one or more points in a given space. This object can be associated with anything that specializes IdentifiedObject. For single line diagrams such objects typically include such items as analog values, breakers, disconnectors, power transformers, and transmission lines.'    
  properties:    
    Diagram:    
      description: 'A diagram object is part of a diagram. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    DiagramObjectPoints:    
      description: 'A diagram object can have 0 or more points to reflect its layout position, routing (for polylines) or boundary (for polygons). Default: ''list'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    DiagramObjectStyle:    
      description: 'A diagram object has a style associated that provides a reference for the style used in the originating system. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    IdentifiedObject:    
      description: 'The diagram objects that are associated with the domain object. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    VisibilityLayers:    
      description: 'A diagram object can be part of multiple visibility layers. Default: ''list'''    
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
    drawingOrder:    
      description: 'The drawing order of this element. The higher the number, the later the element is drawn in sequence. This is used to ensure that elements that overlap are rendered in the correct order. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &diagramobject_-_properties_-_owner_-_items_-_anyof    
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
    isPolygon:    
      description: 'Defines whether or not the diagram objects points define the boundaries of a polygon or the routing of a polyline. If this value is true then a receiving application should consider the first and last points to be connected. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    offsetX:    
      description: 'The offset in the X direction. This is used for defining the offset from centre for rendering an icon (the default is that a single point specifies the centre of the icon).  The offset is in per-unit with 0 indicating there is no offset from the horizontal centre of the icon.  -0.5 indicates it is offset by 50% to the left and 0.5 indicates an offset of 50% to the right. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    offsetY:    
      description: 'The offset in the Y direction. This is used for defining the offset from centre for rendering an icon (the default is that a single point specifies the centre of the icon).  The offset is in per-unit with 0 indicating there is no offset from the vertical centre of the icon.  The offset direction is dependent on the orientation of the diagram, with -0.5 and 0.5 indicating an offset of +/- 50% on the vertical axis. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *diagramobject_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    rotation:    
      description: 'Sets the angle of rotation of the diagram object.  Zero degrees is pointing to the top of the diagram.  Rotation is clockwise. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    type:    
      description: 'NGSI type. It has to be DiagramObject'    
      enum:    
        - DiagramObject    
      type: string    
      x-ngsi:    
        type: Property    
  required: []    
  type: object    
```  
</details>    
## Esempio di payloads  
Non è disponibile l'esempio di un DiagramObject in formato JSON-LD come key-values. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
Non è disponibile l'esempio di un DiagramObject in formato JSON-LD come normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
Non è disponibile l'esempio di un DiagramObject in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
Non è disponibile l'esempio di un DiagramObject in formato JSON-LD come normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
