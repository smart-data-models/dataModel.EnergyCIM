<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: Pss2B  
=============<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/Pss2B/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Adattato dai modelli di dati CIM. Modello IEEE PSS2B modificato.  Blocco lead/lag (o tasso) aggiuntivo aggiunto alla fine (fino a 4 lead/lag in totale)**.  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `a[number]`: Costante del numeratore (a).  Valore tipico = 1. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated[string]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateModified[string]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `description[string]`: Descrizione dell'articolo  - `id[*]`: Identificatore univoco dell'entità  - `inputSignal1Type[number]`: Tipo di segnale di ingresso #1.  Valore tipico = rotorSpeed. Predefinito: Nessuno  . Model: [https://schema.org/Number](https://schema.org/Number)- `inputSignal2Type[number]`: Tipo di segnale di ingresso #2.  Valore tipico = generatorePotenza elettrica. Predefinito: Nessuno  . Model: [https://schema.org/Number](https://schema.org/Number)- `ks1[number]`: Guadagno dello stabilizzatore (Ks1).  Valore tipico = 12. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ks2[number]`: Guadagno sul segnale #2 (Ks2).  Valore tipico = 0,2. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ks3[number]`: Guadagno sull'ingresso del segnale #2 prima del filtro di inseguimento della rampa (Ks3).  Valore tipico = 1. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ks4[number]`: Guadagno sull'ingresso del segnale #2 dopo il filtro di inseguimento della rampa (Ks4).  Valore tipico = 1. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Riferimento Geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `m[number]`: Ordine del denominatore del filtro di inseguimento della rampa (M).  Valore tipico = 5. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `n[number]`: Ordine del filtro di inseguimento della rampa (N).  Valore tipico = 1. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: Il nome di questo elemento.  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `t1[number]`: Costante di tempo di ritardo (T1).  Valore tipico = 0,12. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t10[number]`: Costante di tempo di ritardo/ritardo (T10).  Valore tipico = 0. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t11[number]`: Costante di tempo di ritardo/ritardo (T11).  Valore tipico = 0. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t2[number]`: Costante di tempo lead/lag (T2).  Valore tipico = 0,02. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t3[number]`: Costante di tempo lead/lag (T3).  Valore tipico = 0,3. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t4[number]`: Costante di tempo di ritardo (T4).  Valore tipico = 0,02. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t6[number]`: Costante di tempo sul segnale #1 (T6).  Valore tipico = 0. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t7[number]`: Costante di tempo sul segnale #2 (T7).  Valore tipico = 2. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t8[number]`: Piombo del filtro di inseguimento della rampa (T8).  Valore tipico = 0,2. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t9[number]`: Ritardo del filtro di inseguimento della rampa (T9).  Valore tipico = 0,1. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ta[number]`: Costante di piombo (Ta).  Valore tipico = 0. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tb[number]`: Costante di tempo di ritardo (Tb).  Valore tipico = 0. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw1[number]`: Primo washout sul segnale #1 (Tw1).  Valore tipico = 2. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw2[number]`: Secondo washout sul segnale #1 (Tw2).  Valore tipico = 2. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw3[number]`: Primo washout sul segnale #2 (Tw3).  Valore tipico = 2. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw4[number]`: Secondo washout sul segnale #2 (Tw4).  Valore tipico = 0. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Tipo NGSI. Deve essere Pss2B  - `vsi1max[number]`: Limite massimo del segnale d'ingresso #1 (Vsi1max).  Valore tipico = 2. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vsi1min[number]`: Segnale di ingresso #1 limite minimo (Vsi1min).  Valore tipico = -2. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vsi2max[number]`: Limite massimo del segnale d'ingresso #2 (Vsi2max).  Valore tipico = 2. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vsi2min[number]`: Segnale di ingresso #2 limite minimo (Vsi2min).  Valore tipico = -2. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vstmax[number]`: Limite massimo dell'uscita dello stabilizzatore (Vstmax).  Valore tipico = 0,1. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vstmin[number]`: Limite minimo di uscita dello stabilizzatore (Vstmin).  Valore tipico = -0,1. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
<!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Adattato dai modelli di dati CIM e CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Questo modello di dati è una conversione diretta del Common Information Model (CIM) specificato dallo standard IEC61970 in modelli di dati intelligenti. Le classi python su cui si basa questo modello sono state sviluppate da questi enti Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) e RWTH University Aachen, Germania. Alcune proprietà possono avere un tipo sbagliato. In questo caso, si prega di sollevare un problema o di inviare una mail a info@smartdatamodels.org.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Pss2B:    
  description: 'Adapted from CIM data models. Modified IEEE PSS2B Model.  Extra lead/lag (or rate) block added at end (up to 4 lead/lags total).'    
  properties:    
    a:    
      description: 'Numerator constant (a).  Typical Value = 1. Default: 0.0'    
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
      anyOf: &pss2b_-_properties_-_owner_-_items_-_anyof    
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
    inputSignal1Type:    
      description: "Type of input signal #1.  Typical Value = rotorSpeed. Default: None"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    inputSignal2Type:    
      description: "Type of input signal #2.  Typical Value = generatorElectricalPower. Default: None"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ks1:    
      description: 'Stabilizer gain (Ks1).  Typical Value = 12. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ks2:    
      description: "Gain on signal #2 (Ks2).  Typical Value = 0.2. Default: 0.0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ks3:    
      description: "Gain on signal #2 input before ramp-tracking filter (Ks3).  Typical Value = 1. Default: 0.0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ks4:    
      description: "Gain on signal #2 input after ramp-tracking filter (Ks4).  Typical Value = 1. Default: 0.0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        type: GeoProperty    
    m:    
      description: 'Denominator order of ramp tracking filter (M).  Typical Value = 5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    n:    
      description: 'Order of ramp tracking filter (N).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *pss2b_-_properties_-_owner_-_items_-_anyof    
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
    t1:    
      description: 'Lead/lag time constant (T1).  Typical Value = 0.12. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t10:    
      description: 'Lead/lag time constant (T10).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t11:    
      description: 'Lead/lag time constant (T11).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t2:    
      description: 'Lead/lag time constant (T2).  Typical Value = 0.02. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t3:    
      description: 'Lead/lag time constant (T3).  Typical Value = 0.3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t4:    
      description: 'Lead/lag time constant (T4).  Typical Value = 0.02. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t6:    
      description: "Time constant on signal #1 (T6).  Typical Value = 0. Default: 0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t7:    
      description: "Time constant on signal #2 (T7).  Typical Value = 2. Default: 0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t8:    
      description: 'Lead of ramp tracking filter (T8).  Typical Value = 0.2. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t9:    
      description: 'Lag of ramp tracking filter (T9).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ta:    
      description: 'Lead constant (Ta).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tb:    
      description: 'Lag time constant (Tb).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tw1:    
      description: "First washout on signal #1 (Tw1).  Typical Value = 2. Default: 0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tw2:    
      description: "Second washout on signal #1 (Tw2).  Typical Value = 2. Default: 0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tw3:    
      description: "First washout on signal #2 (Tw3).  Typical Value = 2. Default: 0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tw4:    
      description: "Second washout on signal #2 (Tw4).  Typical Value = 0. Default: 0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be Pss2B'    
      enum:    
        - Pss2B    
      type: string    
      x-ngsi:    
        type: Property    
    vsi1max:    
      description: "Input signal #1 max limit (Vsi1max).  Typical Value = 2. Default: 0.0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vsi1min:    
      description: "Input signal #1 min limit (Vsi1min).  Typical Value = -2. Default: 0.0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vsi2max:    
      description: "Input signal #2 max limit (Vsi2max).  Typical Value = 2. Default: 0.0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vsi2min:    
      description: "Input signal #2 min limit (Vsi2min).  Typical Value = -2. Default: 0.0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vstmax:    
      description: 'Stabilizer output max limit (Vstmax).  Typical Value = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vstmin:    
      description: 'Stabilizer output min limit (Vstmin).  Typical Value = -0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Pss2B/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/Pss2B/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
Non è disponibile l'esempio di un Pss2B in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
Non è disponibile l'esempio di un Pss2B in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
Non è disponibile l'esempio di un Pss2B in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
Non è disponibile l'esempio di un Pss2B in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
