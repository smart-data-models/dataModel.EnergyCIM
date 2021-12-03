Entità: PssIEEE4B  
=================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/PssIEEE4B/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Adattato dai modelli di dati CIM. La classe rappresenta il modello di stabilizzatore di sistema di potenza IEEE Std 421.5-2005 tipo PSS2B. Il modello PSS4B rappresenta una struttura basata su più bande di frequenza di lavoro. Tre bande separate, rispettivamente dedicate ai modi di oscillazione a bassa, intermedia e alta frequenza, sono utilizzate in questo PSS delta-omega (ingresso velocità).  Riferimento: IEEE 4B 421.5-2005 Sezione 8.4.**  

## Elenco delle proprietà  

- `address`: L'indirizzo postale  - `alternateName`: Un nome alternativo per questa voce  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `bwh1`: Filtro Notch 1 (banda ad alta frequenza): Larghezza di banda di tre dB (B). Predefinito: 0.0  - `bwh2`: Filtro Notch 2 (banda ad alta frequenza): Larghezza di banda di tre dB (B). Predefinito: 0.0  - `bwl1`: Filtro Notch 1 (banda a bassa frequenza): Larghezza di banda di tre dB (B). Predefinito: 0.0  - `bwl2`: Filtro Notch 2 (banda a bassa frequenza): Larghezza di banda di tre dB (B). Predefinito: 0.0  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `description`: Una descrizione di questo articolo  - `id`: Identificatore unico dell'entità  - `kh`: Guadagno di banda alta (K).  Valore tipico = 120. Predefinito: 0.0  - `kh1`: Guadagno del filtro differenziale ad alta banda (K).  Valore tipico = 66. Predefinito: 0.0  - `kh11`: Coefficiente dei primi blocchi lead-lag della banda alta (K).  Valore tipico = 1. Predefinito: 0.0  - `kh17`: Coefficiente dei primi blocchi lead-lag della banda alta (K).  Valore tipico = 1. Predefinito: 0.0  - `kh2`: Guadagno del filtro differenziale ad alta banda (K).  Valore tipico = 66. Predefinito: 0.0  - `ki`: Guadagno della banda intermedia (K).  Valore tipico = 30. Predefinito: 0.0  - `ki1`: Guadagno del filtro differenziale a banda intermedia (K).  Valore tipico = 66. Predefinito: 0.0  - `ki11`: Coefficiente del primo blocco lead-lag della banda intermedia (K).  Valore tipico = 1. Predefinito: 0.0  - `ki17`: Coefficiente del primo blocco lead-lag della banda intermedia (K).  Valore tipico = 1. Predefinito: 0.0  - `ki2`: Guadagno del filtro differenziale a banda intermedia (K).  Valore tipico = 66. Predefinito: 0.0  - `kl`: Guadagno di banda bassa (K).  Valore tipico = 7.5. Predefinito: 0.0  - `kl1`: Guadagno del filtro differenziale a banda bassa (K).  Valore tipico = 66. Predefinito: 0.0  - `kl11`: Coefficiente del primo blocco lead-lag della banda bassa (K).  Valore tipico = 1. Predefinito: 0.0  - `kl17`: Coefficiente del primo blocco lead-lag della banda bassa (K).  Valore tipico = 1. Predefinito: 0.0  - `kl2`: Guadagno del filtro differenziale a banda bassa (K).  Valore tipico = 66. Predefinito: 0.0  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: Il nome di questo articolo.  - `omeganh1`: Filtro Notch 1 (banda ad alta frequenza): frequenza del filtro (omega). Predefinito: 0.0  - `omeganh2`: Filtro Notch 2 (banda ad alta frequenza): frequenza del filtro (omega). Predefinito: 0.0  - `omeganl1`: Filtro Notch 1 (banda di bassa frequenza): frequenza del filtro (omega). Predefinito: 0.0  - `omeganl2`: Filtro Notch 2 (banda di bassa frequenza): frequenza del filtro (omega). Predefinito: 0.0  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `th1`: Costante di tempo della banda alta (T).  Valore tipico = 0.01513. Predefinito: 0  - `th10`: Costante di tempo della banda alta (T).  Valore tipico = 0. Predefinito: 0  - `th11`: Costante di tempo della banda alta (T).  Valore tipico = 0. Predefinito: 0  - `th12`: Costante di tempo della banda alta (T).  Valore tipico = 0. Predefinito: 0  - `th2`: Costante di tempo della banda alta (T).  Valore tipico = 0.01816. Predefinito: 0  - `th3`: Costante di tempo della banda alta (T).  Valore tipico = 0. Predefinito: 0  - `th4`: Costante di tempo della banda alta (T).  Valore tipico = 0. Predefinito: 0  - `th5`: Costante di tempo della banda alta (T).  Valore tipico = 0. Predefinito: 0  - `th6`: Costante di tempo della banda alta (T).  Valore tipico = 0. Predefinito: 0  - `th7`: Costante di tempo della banda alta (T).  Valore tipico = 0.01816. Predefinito: 0  - `th8`: Costante di tempo della banda alta (T).  Valore tipico = 0.02179. Predefinito: 0  - `th9`: Costante di tempo della banda alta (T).  Valore tipico = 0. Predefinito: 0  - `ti1`: Costante di tempo della banda intermedia (T).  Valore tipico = 0,173. Predefinito: 0  - `ti10`: Costante di tempo della banda intermedia (T).  Valore tipico = 0. Predefinito: 0  - `ti11`: Costante di tempo della banda intermedia (T).  Valore tipico = 0. Predefinito: 0  - `ti12`: Costante di tempo della banda intermedia (T).  Valore tipico = 0. Predefinito: 0  - `ti2`: Costante di tempo della banda intermedia (T).  Valore tipico = 0,2075. Predefinito: 0  - `ti3`: Costante di tempo della banda intermedia (T).  Valore tipico = 0. Predefinito: 0  - `ti4`: Costante di tempo della banda intermedia (T).  Valore tipico = 0. Predefinito: 0  - `ti5`: Costante di tempo della banda intermedia (T).  Valore tipico = 0. Predefinito: 0  - `ti6`: Costante di tempo della banda intermedia (T).  Valore tipico = 0. Predefinito: 0  - `ti7`: Costante di tempo della banda intermedia (T).  Valore tipico = 0,2075. Predefinito: 0  - `ti8`: Costante di tempo della banda intermedia (T).  Valore tipico = 0,2491. Predefinito: 0  - `ti9`: Costante di tempo della banda intermedia (T).  Valore tipico = 0. Predefinito: 0  - `tl1`: Costante di tempo della banda bassa (T).  Valore tipico = 1,73. Predefinito: 0  - `tl10`: Costante di tempo della banda bassa (T).  Valore tipico = 0. Predefinito: 0  - `tl11`: Costante di tempo della banda bassa (T).  Valore tipico = 0. Predefinito: 0  - `tl12`: Costante di tempo della banda bassa (T).  Valore tipico = 0. Predefinito: 0  - `tl2`: Costante di tempo della banda bassa (T).  Valore tipico = 2.075. Predefinito: 0  - `tl3`: Costante di tempo della banda bassa (T).  Valore tipico = 0. Predefinito: 0  - `tl4`: Costante di tempo della banda bassa (T).  Valore tipico = 0. Predefinito: 0  - `tl5`: Costante di tempo della banda bassa (T).  Valore tipico = 0. Predefinito: 0  - `tl6`: Costante di tempo della banda bassa (T).  Valore tipico = 0. Predefinito: 0  - `tl7`: Costante di tempo della banda bassa (T).  Valore tipico = 2.075. Predefinito: 0  - `tl8`: Costante di tempo della banda bassa (T).  Valore tipico = 2.491. Predefinito: 0  - `tl9`: Costante di tempo della banda bassa (T).  Valore tipico = 0. Predefinito: 0  - `type`: Tipo NGSI. Deve essere PssIEEE4B  - `vhmax`: Limite massimo di uscita in banda alta (V).  Valore tipico = 0.6. Predefinito: 0.0  - `vhmin`: Limite minimo di uscita in banda alta (V).  Valore tipico = -0.6. Predefinito: 0.0  - `vimax`: Limite massimo di uscita a banda intermedia (V).  Valore tipico = 0.6. Predefinito: 0.0  - `vimin`: Limite minimo di uscita della banda intermedia (V).  Valore tipico = -0.6. Predefinito: 0.0  - `vlmax`: Limite massimo di uscita a banda bassa (V).  Valore tipico = 0.075. Predefinito: 0.0  - `vlmin`: Limite minimo di uscita a banda bassa (V).  Valore tipico = -0.075. Predefinito: 0.0  - `vstmax`: Limite massimo dell'uscita PSS (V).  Valore tipico = 0,15. Predefinito: 0,0  - `vstmin`: Limite minimo dell'uscita PSS (V).  Valore tipico = -0,15. Predefinito: 0,0    
Proprietà richieste  
Adattato dai modelli di dati CIM e CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Questo modello di dati è una conversione diretta del Common Information Model (CIM) specificato dallo standard IEC61970 in modelli di dati intelligenti. Le classi python su cui si basa questo modello sono state sviluppate da queste entità Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) e RWTH University Aachen, Germania. Alcune proprietà possono avere un tipo sbagliato. Questo è stato il caso, si prega di sollevare un problema o inviare una mail a info@smartdatamodels.org.  
## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PssIEEE4B:    
  description: 'Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type PSS2B power system stabilizer model. The PSS4B model represents a structure based on multiple working frequency bands. Three separate bands, respectively dedicated to the low-, intermediate- and high-frequency modes of oscillations, are used in this delta-omega (speed input) PSS.  Reference: IEEE 4B 421.5-2005 Section 8.4.'    
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
    bwh1:    
      description: 'Notch filter 1 (high-frequency band): Three dB bandwidth (B). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bwh2:    
      description: 'Notch filter 2 (high-frequency band): Three dB bandwidth (B). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bwl1:    
      description: 'Notch filter 1 (low-frequency band): Three dB bandwidth (B). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bwl2:    
      description: 'Notch filter 2 (low-frequency band): Three dB bandwidth (B). Default: 0.0'    
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
    id:    
      anyOf: &pssieee4b_-_properties_-_owner_-_items_-_anyof    
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
    kh:    
      description: 'High band gain (K).  Typical Value = 120. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kh1:    
      description: 'High band differential filter gain (K).  Typical Value = 66. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kh11:    
      description: 'High band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kh17:    
      description: 'High band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kh2:    
      description: 'High band differential filter gain (K).  Typical Value = 66. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ki:    
      description: 'Intermediate band gain (K).  Typical Value = 30. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ki1:    
      description: 'Intermediate band differential filter gain (K).  Typical Value = 66. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ki11:    
      description: 'Intermediate band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ki17:    
      description: 'Intermediate band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ki2:    
      description: 'Intermediate band differential filter gain (K).  Typical Value = 66. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kl:    
      description: 'Low band gain (K).  Typical Value = 7.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kl1:    
      description: 'Low band differential filter gain (K).  Typical Value = 66. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kl11:    
      description: 'Low band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kl17:    
      description: 'Low band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kl2:    
      description: 'Low band differential filter gain (K).  Typical Value = 66. Default: 0.0'    
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
    omeganh1:    
      description: 'Notch filter 1 (high-frequency band): filter frequency (omega). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    omeganh2:    
      description: 'Notch filter 2 (high-frequency band): filter frequency (omega). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    omeganl1:    
      description: 'Notch filter 1 (low-frequency band): filter frequency (omega). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    omeganl2:    
      description: 'Notch filter 2 (low-frequency band): filter frequency (omega). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *pssieee4b_-_properties_-_owner_-_items_-_anyof    
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
    th1:    
      description: 'High band time constant (T).  Typical Value = 0.01513. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th10:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th11:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th12:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th2:    
      description: 'High band time constant (T).  Typical Value = 0.01816. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th3:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th4:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th5:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th6:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th7:    
      description: 'High band time constant (T).  Typical Value = 0.01816. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th8:    
      description: 'High band time constant (T).  Typical Value = 0.02179. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th9:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti1:    
      description: 'Intermediate band time constant (T).  Typical Value = 0.173. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti10:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti11:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti12:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti2:    
      description: 'Intermediate band time constant (T).  Typical Value = 0.2075. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti3:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti4:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti5:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti6:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti7:    
      description: 'Intermediate band time constant (T).  Typical Value = 0.2075. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti8:    
      description: 'Intermediate band time constant (T).  Typical Value = 0.2491. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti9:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl1:    
      description: 'Low band time constant (T).  Typical Value = 1.73. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl10:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl11:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl12:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl2:    
      description: 'Low band time constant (T).  Typical Value = 2.075. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl3:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl4:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl5:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl6:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl7:    
      description: 'Low band time constant (T).  Typical Value = 2.075. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl8:    
      description: 'Low band time constant (T).  Typical Value = 2.491. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl9:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be PssIEEE4B'    
      enum:    
        - PssIEEE4B    
      type: string    
      x-ngsi:    
        type: Property    
    vhmax:    
      description: 'High band output maximum limit (V).  Typical Value = 0.6. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vhmin:    
      description: 'High band output minimum limit (V).  Typical Value = -0.6. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vimax:    
      description: 'Intermediate band output maximum limit (V).  Typical Value = 0.6. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vimin:    
      description: 'Intermediate band output minimum limit (V).  Typical Value = -0.6. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vlmax:    
      description: 'Low band output maximum limit (V).  Typical Value = 0.075. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vlmin:    
      description: 'Low band output minimum limit (V).  Typical Value = -0.075. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vstmax:    
      description: 'PSS output maximum limit (V).  Typical Value = 0.15. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vstmin:    
      description: 'PSS output minimum limit (V).  Typical Value = -0.15. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PssIEEE4B/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/PssIEEE4B/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## Esempio di payloads  
Non è disponibile l'esempio di un PssIEEE4B in formato JSON-LD come key-values. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
Non disponibile l'esempio di un PssIEEE4B in formato JSON-LD come normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
Non è disponibile l'esempio di un PssIEEE4B in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
Non disponibile l'esempio di un PssIEEE4B in formato JSON-LD come normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per avere una risposta su come trattare le unità di grandezza