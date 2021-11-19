Entità: PowerTransformerEnd  
===========================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/PowerTransformerEnd/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Adattato dai modelli di dati CIM. Un PowerTransformerEnd è associato ad ogni terminale di un PowerTransformer. I valori di impedenza r, r0, x, e x0 di un PowerTransformerEnd rappresentano una stella equivalente come segue 1) per un PowerTransformer a due terminali il PowerTransformerEnd ad alta tensione ha valori non nulli su r, r0, x, e x0 mentre il PowerTransformerEnd a bassa tensione ha valori nulli per r, r0, x, e x0. 2) per un PowerTransformer a tre terminali i tre PowerTransformerEnds rappresentano una stella equivalente con ogni gamba nella stella rappresentata dai valori r, r0, x, e x0. 3) per un PowerTransformer con più di tre terminali i valori di impedenza di PowerTransformerEnd non possono essere usati. Usare invece l'impedenza TransformerMeshImpedance o dividere il trasformatore in più PowerTransformer.**  

## Elenco delle proprietà  

- `PowerTransformer`: Le estremità di questo trasformatore di potenza. Predefinito: Nessuno  - `address`: L'indirizzo postale  - `alternateName`: Un nome alternativo per questa voce  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `b`: Suscettività del ramo magnetizzante (B mag).  Il valore può essere positivo o negativo. Predefinito: 0,0  - `b0`: Suscettibilità del ramo magnetizzante a sequenza zero. Predefinito: 0.0  - `connectionKind`: Tipo di connessione. Predefinito: Nessuno  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `description`: Una descrizione di questo articolo  - `g`: Conduttanza del ramo magnetizzante. Predefinito: 0.0  - `g0`: Conduttanza del ramo magnetizzante a sequenza zero (modello a stella). Predefinito: 0,0  - `id`: Identificatore unico dell'entità  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: Il nome di questo articolo.  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `phaseAngleClock`: Spostamento dell'angolo di fase della tensione terminale dove 360 gradi sono rappresentati con ore di orologio. I valori validi sono da 0 a 11. Per esempio, per l'estremità secondaria di un trasformatore con il codice del gruppo vettoriale `Dyn11`, specificate il tipo di connessione come wye con neutro e specificate l'angolo di fase dell'orologio come 11.  Il valore dell'orologio del numero dell'estremità del trasformatore specificato come 1, è assunto come zero.  Si noti che il numero finale del trasformatore non si presume sia lo stesso del numero di sequenza del terminale. Predefinito: 0  - `r`: Resistenza (modello a stella) dell'estremità del trasformatore. L'attributo deve essere uguale o maggiore di zero per i trasformatori non equivalenti. Predefinito: 0.0  - `r0`: Resistenza serie a sequenza zero (modello a stella) dell'estremità del trasformatore. Predefinito: 0,0  - `ratedS`: Potenza apparente normale. L'attributo deve essere un valore positivo. Per un trasformatore a due avvolgimenti i valori per il lato alta e bassa tensione devono essere identici. Predefinito: 0.0  - `ratedU`: Tensione nominale: fase-fase per avvolgimenti trifase, e fase-fase o fase-neutro per avvolgimenti monofase. Un lato ad alta tensione, come dato da TransformerEnd.endNumber, deve avere un U nominale che è maggiore o uguale a U nominale per i lati a tensione inferiore. Predefinito: 0.0  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `type`: Tipo NGSI. Deve essere PowerTransformerEnd  - `x`: Reattanza serie in sequenza positiva (modello a stella) dell'estremità del trasformatore. Predefinito: 0,0  - `x0`: Reattanza serie a sequenza zero dell'estremità del trasformatore. Predefinito: 0,0    
Proprietà richieste  
Adattato dai modelli di dati CIM e CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Questo modello di dati è una conversione diretta del Common Information Model (CIM) specificato dallo standard IEC61970 in modelli di dati intelligenti. Le classi python su cui si basa questo modello sono state sviluppate da queste entità Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) e RWTH University Aachen, Germania. Alcune proprietà possono avere un tipo sbagliato. Questo è stato il caso, si prega di sollevare un problema o inviare una mail a info@smartdatamodels.org.  
## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PowerTransformerEnd:    
  description: 'Adapted from CIM data models. A PowerTransformerEnd is associated with each Terminal of a PowerTransformer. The impedance values r, r0, x, and x0 of a PowerTransformerEnd represents a star equivalent as follows 1) for a two Terminal PowerTransformer the high voltage PowerTransformerEnd has non zero values on r, r0, x, and x0 while the low voltage PowerTransformerEnd has zero values for r, r0, x, and x0. 2) for a three Terminal PowerTransformer the three PowerTransformerEnds represents a star equivalent with each leg in the star represented by r, r0, x, and x0 values. 3) for a PowerTransformer with more than three Terminals the PowerTransformerEnd impedance values cannot be used. Instead use the TransformerMeshImpedance or split the transformer into multiple PowerTransformers.'    
  properties:    
    PowerTransformer:    
      description: 'The ends of this power transformer. Default: None'    
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
    b:    
      description: 'Magnetizing branch susceptance (B mag).  The value can be positive or negative. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    b0:    
      description: 'Zero sequence magnetizing branch susceptance. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    connectionKind:    
      description: 'Kind of connection. Default: None'    
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
    g:    
      description: 'Magnetizing branch conductance. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    g0:    
      description: 'Zero sequence magnetizing branch conductance (star-model). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &powertransformerend_-_properties_-_owner_-_items_-_anyof    
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
        anyOf: *powertransformerend_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    phaseAngleClock:    
      description: 'Terminal voltage phase angle displacement where 360 degrees are represented with clock hours. The valid values are 0 to 11. For example, for the secondary side end of a transformer with vector group code of `Dyn11`, specify the connection kind as wye with neutral and specify the phase angle of the clock as 11.  The clock value of the transformer end number specified as 1, is assumed to be zero.  Note the transformer end number is not assumed to be the same as the terminal sequence number. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    r:    
      description: 'Resistance (star-model) of the transformer end. The attribute shall be equal or greater than zero for non-equivalent transformers. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    r0:    
      description: 'Zero sequence series resistance (star-model) of the transformer end. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ratedS:    
      description: 'Normal apparent power rating. The attribute shall be a positive value. For a two-winding transformer the values for the high and low voltage sides shall be identical. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ratedU:    
      description: 'Rated voltage: phase-phase for three-phase windings, and either phase-phase or phase-neutral for single-phase windings. A high voltage side, as given by TransformerEnd.endNumber, shall have a ratedU that is greater or equal than ratedU for the lower voltage sides. Default: 0.0'    
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
      description: 'NGSI type. It has to be PowerTransformerEnd'    
      enum:    
        - PowerTransformerEnd    
      type: string    
      x-ngsi:    
        type: Property    
    x:    
      description: 'Positive sequence series reactance (star-model) of the transformer end. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    x0:    
      description: 'Zero sequence series reactance of the transformer end. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PowerTransformerEnd/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/PowerTransformerEnd/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## Esempio di payloads  
Non è disponibile l'esempio di un PowerTransformerEnd in formato JSON-LD come valori chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
Non disponibile l'esempio di un PowerTransformerEnd in formato JSON-LD come normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
Non è disponibile l'esempio di un PowerTransformerEnd in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
Non disponibile l'esempio di un PowerTransformerEnd in formato JSON-LD come normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
