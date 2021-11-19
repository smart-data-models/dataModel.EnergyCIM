Entità: GovGAST2  
================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovGAST2/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Adattato dai modelli di dati CIM. Modello di turbina a gas.**  

## Elenco delle proprietà  

- `a`: Posizionatore della valvola (A). Predefinito: 0,0  - `address`: L'indirizzo postale  - `af1`: Temperatura di scarico Parametro (Af1).  Unità = per unità di temperatura.  Basato sulla temperatura in gradi C. Default: 0.0  - `af2`: Coefficiente uguale a 0,5 (1 velocità) (Af2). Predefinito: 0,0  - `alternateName`: Un nome alternativo per questa voce  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `b`: Posizionatore della valvola (B). Predefinito: 0,0  - `bf1`: (Bf1).  Bf1 = E(1-w) dove E (coefficiente di sensibilità alla velocità) è da 0,55 a 0,65 x Tr.  Unità = per unità di temperatura.  Basato sulla temperatura in gradi C. Default: 0.0  - `bf2`: Coefficiente di coppia della turbina K (dipende dal valore di riscaldamento del flusso di combustibile nella camera di combustione) (Bf2). Predefinito: 0,0  - `c`: Posizionatore della valvola (C). Predefinito: 0,0  - `cf2`: Coefficiente che definisce il flusso di carburante quando l'uscita di potenza è 0% (Cf2).  Sincrono ma senza potenza.  Tipicamente 0,23 x K (23% di flusso di carburante). Predefinito: 0,0  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `description`: Una descrizione di questo articolo  - `ecr`: Ritardo della reazione di combustione (Ecr). Predefinito: 0  - `etd`: Ritardo della turbina e dello scarico (Etd). Predefinito: 0  - `id`: Identificatore unico dell'entità  - `k3`: Rapporto di regolazione del carburante (K3). Predefinito: 0.0  - `k4`: Guadagno dello scudo antiradiazioni (K4). Predefinito: 0,0  - `k5`: Guadagno dello scudo antiradiazioni (K5). Predefinito: 0,0  - `k6`: Flusso minimo di carburante (K6). Predefinito: 0,0  - `kf`: Feedback del sistema di alimentazione (Kf). Predefinito: 0,0  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `mwbase`: Base per i valori di potenza (MWbase) (> 0).  Unità = MW. Predefinito: 0,0  - `name`: Il nome di questo articolo.  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `t`: Costante di tempo del controllo del carburante (T). Predefinito: 0  - `t3`: Costante di tempo dello scudo antiradiazioni (T3). Predefinito: 0  - `t4`: Costante di tempo della termocoppia (T4). Predefinito: 0  - `t5`: Costante di tempo di controllo della temperatura (T5). Predefinito: 0  - `tc`: Controllo della temperatura (Tc).  Unità = [SYMBOL REMOVED]F o [SYMBOL REMOVED]C a seconda delle costanti Af1 e Bf1. Predefinito: 0.0  - `tcd`: Costante di tempo di scarico del compressore (Tcd). Predefinito: 0  - `tf`: Costante di tempo del sistema di alimentazione (Tf). Predefinito: 0  - `tmax`: Limite massimo della turbina (Tmax). Predefinito: 0.0  - `tmin`: Limite minimo della turbina (Tmin). Predefinito: 0.0  - `tr`: Temperatura nominale (Tr).  Unità = [SYMBOL REMOVED]C a seconda dei parametri Af1 e Bf1. Predefinito: 0,0  - `trate`: Potenza della turbina (Trate).  Unità = MW. Predefinito: 0,0  - `tt`: Tasso di integrazione del controllore di temperatura (Tt). Predefinito: 0  - `type`: Tipo di NGSI. Deve essere GovGAST2  - `w`: Guadagno del governatore (1/droop) sulla potenza della turbina (W). Predefinito: 0,0  - `x`: Costante di tempo del governatore (X). Predefinito: 0  - `y`: Costante di tempo di ritardo del governatore (Y) (>0). Predefinito: 0  - `z`: Modalità del governatore (Z). true = Droop false = ISO. Predefinito: Falso    
Proprietà richieste  
Adattato dai modelli di dati CIM e CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Questo modello di dati è una conversione diretta del Common Information Model (CIM) specificato dallo standard IEC61970 in modelli di dati intelligenti. Le classi python su cui si basa questo modello sono state sviluppate da queste entità Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) e RWTH University Aachen, Germania. Alcune proprietà possono avere un tipo sbagliato. Questo è stato il caso, si prega di sollevare un problema o inviare una mail a info@smartdatamodels.org.  
## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GovGAST2:    
  description: 'Adapted from CIM data models. Gas turbine model.'    
  properties:    
    a:    
      description: 'Valve positioner (A). Default: 0.0'    
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
    af1:    
      description: 'Exhaust temperature Parameter (Af1).  Unit = per unit temperature.  Based on temperature in degrees C. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    af2:    
      description: 'Coefficient equal to 0.5(1-speed) (Af2). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
      description: 'Valve positioner (B). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bf1:    
      description: '(Bf1).  Bf1 = E(1-w) where E (speed sensitivity coefficient) is 0.55 to 0.65 x Tr.  Unit = per unit temperature.  Based on temperature in degrees C. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bf2:    
      description: 'Turbine Torque Coefficient K (depends on heating value of fuel stream in combustion chamber) (Bf2). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    c:    
      description: 'Valve positioner (C). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    cf2:    
      description: 'Coefficient defining fuel flow where power output is 0% (Cf2).  Synchronous but no output.  Typically 0.23 x K (23% fuel flow). Default: 0.0'    
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
    ecr:    
      description: 'Combustion reaction time delay (Ecr). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    etd:    
      description: 'Turbine and exhaust delay (Etd). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &govgast2_-_properties_-_owner_-_items_-_anyof    
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
    k3:    
      description: 'Ratio of Fuel Adjustment (K3). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    k4:    
      description: 'Gain of radiation shield (K4). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    k5:    
      description: 'Gain of radiation shield (K5). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    k6:    
      description: 'Minimum fuel flow (K6). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kf:    
      description: 'Fuel system feedback (Kf). Default: 0.0'    
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
    mwbase:    
      description: 'Base for power values (MWbase) (> 0).  Unit = MW. Default: 0.0'    
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
        anyOf: *govgast2_-_properties_-_owner_-_items_-_anyof    
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
    t:    
      description: 'Fuel Control Time Constant (T). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t3:    
      description: 'Radiation shield time constant (T3). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t4:    
      description: 'Thermocouple time constant (T4). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    t5:    
      description: 'Temperature control time constant (T5). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tc:    
      description: 'Temperature control (Tc).  Unit = [SYMBOL REMOVED]F or [SYMBOL REMOVED]C depending on constants Af1 and Bf1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tcd:    
      description: 'Compressor discharge time constant (Tcd). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tf:    
      description: 'Fuel system time constant (Tf). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tmax:    
      description: 'Maximum Turbine limit (Tmax). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tmin:    
      description: 'Minimum Turbine limit (Tmin). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tr:    
      description: 'Rated temperature (Tr).  Unit = [SYMBOL REMOVED]C depending on parameters Af1 and Bf1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    trate:    
      description: 'Turbine rating (Trate).  Unit = MW. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tt:    
      description: 'Temperature controller integration rate (Tt). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be GovGAST2'    
      enum:    
        - GovGAST2    
      type: string    
      x-ngsi:    
        type: Property    
    w:    
      description: 'Governor gain (1/droop) on turbine rating (W). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    x:    
      description: 'Governor lead time constant (X). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    y:    
      description: 'Governor lag time constant (Y) (>0). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    z:    
      description: 'Governor mode (Z). true = Droop false = ISO. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovGAST2/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/GovGAST2/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## Esempio di payloads  
Non è disponibile l'esempio di un GovGAST2 in formato JSON-LD come key-values. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
Non disponibile l'esempio di un GovGAST2 in formato JSON-LD come normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
Non è disponibile l'esempio di un GovGAST2 in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
Non è disponibile l'esempio di un GovGAST2 in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
