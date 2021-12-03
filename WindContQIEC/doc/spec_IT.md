Entità: WindContQIEC  
====================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/WindContQIEC/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Adattato dai modelli di dati CIM. Modello di controllo Q.  Riferimento: Norma IEC 61400-27-1 Sezione 6.6.5.6.**  

## Elenco delle proprietà  

- `WindTurbineType3or4IEC`: Modello di turbina eolica di tipo 3 o 4 a cui è associato questo modo di controllo reattivo. Predefinito: Nessuno  - `address`: L'indirizzo postale  - `alternateName`: Un nome alternativo per questa voce  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `description`: Una descrizione di questo articolo  - `id`: Identificatore unico dell'entità  - `iqh1`: Massima iniezione di corrente reattiva durante il dip (i). È un parametro dipendente dal tipo. Predefinito: 0,0  - `iqmax`: Massima iniezione di corrente reattiva (i). È un parametro dipendente dal tipo. Predefinito: 0,0  - `iqmin`: Iniezione minima di corrente reattiva (i). È un parametro dipendente dal tipo. Predefinito: 0,0  - `iqpost`: Iniezione di corrente reattiva post-guasto (). È un parametro dipendente dal progetto. Predefinito: 0,0  - `kiq`: Guadagno di integrazione del controllore PI di potenza reattiva (). È un parametro dipendente dal tipo. Predefinito: 0.0  - `kiu`: Guadagno di integrazione del regolatore PI di tensione (). È un parametro dipendente dal tipo. Predefinito: 0.0  - `kpq`: Guadagno proporzionale del regolatore PI di potenza reattiva (). È un parametro dipendente dal tipo. Predefinito: 0.0  - `kpu`: Guadagno proporzionale del regolatore PI di tensione (). È un parametro dipendente dal tipo. Predefinito: 0.0  - `kqv`: Fattore di scala della tensione per la corrente LVRT (). È un parametro dipendente dal progetto. Predefinito: 0.0  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: Il nome di questo articolo.  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `qmax`: Potenza reattiva massima (q). È un parametro dipendente dal tipo. Predefinito: 0,0  - `qmin`: Potenza reattiva minima (q). È un parametro dipendente dal tipo. Predefinito: 0,0  - `rdroop`: Componente resistivo dell'impedenza di caduta di tensione (). È un parametro dipendente dal progetto. Predefinito: 0.0  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `tiq`: Costante di tempo nel ritardo della corrente reattiva (T). È un parametro dipendente dal tipo. Predefinito: 0  - `tpfilt`: Costante di tempo del filtro di misurazione della potenza (). È un parametro dipendente dal tipo. Predefinito: 0  - `tpost`: Durata del periodo di tempo in cui viene iniettata potenza reattiva dopo il guasto (). È un parametro dipendente dal progetto. Predefinito: 0  - `tqord`: Costante di tempo nell'ordine di potenza reattiva (). È un parametro dipendente dal tipo. Predefinito: 0  - `tufilt`: Costante di tempo del filtro di misura della tensione (). È un parametro dipendente dal tipo. Predefinito: 0  - `type`: Tipo di NGSI. Deve essere WindContQIEC  - `udb1`: Limite inferiore della banda morta di tensione (). È un parametro dipendente dal tipo. Predefinito: 0.0  - `udb2`: Limite superiore della banda morta di tensione (). È un parametro dipendente dal tipo. Predefinito: 0.0  - `umax`: Tensione massima nel termine integrale del regolatore PI di tensione (u). È un parametro dipendente dal tipo. Predefinito: 0.0  - `umin`: Tensione minima nel termine integrale del regolatore PI di tensione (u). È un parametro dipendente dal tipo. Predefinito: 0,0  - `uqdip`: Soglia di tensione per il rilevamento di LVRT nel controllo q (). È un parametro dipendente dal tipo. Predefinito: 0,0  - `uref0`: Bias definito dall'utente nel riferimento di tensione (), usato quando =. È un parametro dipendente dal caso. Predefinito: 0.0  - `windLVRTQcontrolModesType`: Tipi di modalità di controllo LVRT Q (). È un parametro dipendente dal progetto. Predefinito: Nessuno  - `windQcontrolModesType`: Tipi di modalità di controllo Q delle turbine eoliche in generale ().  È un parametro dipendente dal progetto. Predefinito: Nessuno  - `xdroop`: Componente induttivo dell'impedenza di caduta di tensione (). È un parametro dipendente dal progetto. Predefinito: 0.0    
Proprietà richieste  
Adattato dai modelli di dati CIM e CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Questo modello di dati è una conversione diretta del Common Information Model (CIM) specificato dallo standard IEC61970 in modelli di dati intelligenti. Le classi python su cui si basa questo modello sono state sviluppate da queste entità Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) e RWTH University Aachen, Germania. Alcune proprietà possono avere un tipo sbagliato. Questo è stato il caso, si prega di sollevare un problema o inviare una mail a info@smartdatamodels.org.  
## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WindContQIEC:    
  description: 'Adapted from CIM data models. Q control model.  Reference: IEC Standard 61400-27-1 Section 6.6.5.6.'    
  properties:    
    WindTurbineType3or4IEC:    
      description: 'Wind turbine type 3 or 4 model with which this reactive control mode is associated. Default: None'    
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
    id:    
      anyOf: &windcontqiec_-_properties_-_owner_-_items_-_anyof    
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
    iqh1:    
      description: 'Maximum reactive current injection during dip (i). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    iqmax:    
      description: 'Maximum reactive current injection (i). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    iqmin:    
      description: 'Minimum reactive current injection (i). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    iqpost:    
      description: 'Post fault reactive current injection (). It is project dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kiq:    
      description: 'Reactive power PI controller integration gain (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kiu:    
      description: 'Voltage PI controller integration gain (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kpq:    
      description: 'Reactive power PI controller proportional gain (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kpu:    
      description: 'Voltage PI controller proportional gain (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kqv:    
      description: 'Voltage scaling factor for LVRT current (). It is project dependent parameter. Default: 0.0'    
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
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *windcontqiec_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    qmax:    
      description: 'Maximum reactive power (q). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    qmin:    
      description: 'Minimum reactive power (q). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rdroop:    
      description: 'Resistive component of voltage drop impedance (). It is project dependent parameter. Default: 0.0'    
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
    tiq:    
      description: 'Time constant in reactive current lag (T). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tpfilt:    
      description: 'Power measurement filter time constant (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tpost:    
      description: 'Length of time period where post fault reactive power is injected (). It is project dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tqord:    
      description: 'Time constant in reactive power order lag (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tufilt:    
      description: 'Voltage measurement filter time constant (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be WindContQIEC'    
      enum:    
        - WindContQIEC    
      type: string    
      x-ngsi:    
        type: Property    
    udb1:    
      description: 'Voltage dead band lower limit (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    udb2:    
      description: 'Voltage dead band upper limit (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    umax:    
      description: 'Maximum voltage in voltage PI controller integral term (u). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    umin:    
      description: 'Minimum voltage in voltage PI controller integral term (u). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    uqdip:    
      description: 'Voltage threshold for LVRT detection in q control (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    uref0:    
      description: 'User defined bias in voltage reference (), used when  =. It is case dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    windLVRTQcontrolModesType:    
      description: 'Types of LVRT Q control modes (). It is project dependent parameter. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    windQcontrolModesType:    
      description: 'Types of general wind turbine Q control modes ().  It is project dependent parameter. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    xdroop:    
      description: 'Inductive component of voltage drop impedance (). It is project dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindContQIEC/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/WindContQIEC/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## Esempio di payloads  
Non è disponibile l'esempio di un WindContQIEC in formato JSON-LD come key-values. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
Non disponibile l'esempio di un WindContQIEC in formato JSON-LD come normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
Non è disponibile l'esempio di un WindContQIEC in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
Non disponibile l'esempio di un WindContQIEC in formato JSON-LD come normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per avere una risposta su come trattare le unità di grandezza