Entità: ExternalNetworkInjection  
================================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExternalNetworkInjection/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Adattato dai modelli di dati CIM. Questa classe rappresenta la rete esterna ed è usata per i calcoli IEC 60909.  

## Elenco delle proprietà  

- `address`: L'indirizzo postale  - `alternateName`: Un nome alternativo per questa voce  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `description`: Una descrizione di questo articolo  - `governorSCD`: Bias di frequenza della potenza. Questo è il cambiamento nell'iniezione di potenza diviso per il cambiamento di frequenza e negato.  Un valore positivo del power frequency bias fornisce un'iniezione di potenza aggiuntiva su un calo di frequenza. Predefinito: 0.0  - `id`: Identificatore unico dell'entità  - `ikSecond`: Indica se la corrente di cortocircuito simmetrica iniziale e la potenza sono state calcolate secondo la norma IEC (Ik`). Predefinito: Falso  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `maxInitialSymShCCurrent`: Correnti di cortocircuito simmetriche iniziali massime (Ik` max) in A (Ik` = Sk`/(SQRT(3) Un)). Utilizzato per lo scambio di dati sul cortocircuito secondo IEC 60909 Default: 0.0  - `maxP`: Potenza attiva massima dell'iniezione. Predefinito: 0,0  - `maxQ`: Non per la modellazione del cortocircuito; è usato per la modellazione dell'alimentazione per lo scambio di flussi di carico. Se maxQ e minQ non sono utilizzati può essere utilizzato ReactiveCapabilityCurve Default: 0.0  - `maxR0ToX0Ratio`: Rapporto massimo tra la resistenza di sequenza zero dell'alimentatore di rete e la sua reattanza di sequenza zero (R(0)/X(0) max). Utilizzato per lo scambio di dati di corto circuito secondo IEC 60909 Default: 0.0  - `maxR1ToX1Ratio`: Rapporto massimo tra la resistenza di sequenza positiva dell'alimentatore di rete e la sua reattanza di sequenza positiva (R(1)/X(1) max). Utilizzato per lo scambio di dati di corto circuito secondo IEC 60909 Default: 0.0  - `maxZ0ToZ1Ratio`: Rapporto massimo tra l'impedenza di sequenza zero e la sua impedenza di sequenza positiva (Z(0)/Z(1) max). Utilizzato per lo scambio di dati sul cortocircuito secondo IEC 60909 Default: 0.0  - `minInitialSymShCCurrent`: Correnti di cortocircuito simmetriche iniziali minime (Ik` min) in A (Ik` = Sk`/(SQRT(3) Un)). Utilizzato per lo scambio di dati sul cortocircuito secondo IEC 60909 Default: 0.0  - `minP`: Potenza attiva minima dell'iniezione. Predefinito: 0,0  - `minQ`: Non per la modellazione del cortocircuito; è usato per la modellazione dell'alimentazione per lo scambio di flussi di carico. Se maxQ e minQ non sono utilizzati può essere utilizzato ReactiveCapabilityCurve Default: 0.0  - `minR0ToX0Ratio`: Indica se la corrente di cortocircuito simmetrica iniziale e la potenza sono state calcolate secondo la norma IEC (Ik`). Utilizzato per lo scambio di dati sul cortocircuito secondo IEC 6090 Default: 0.0  - `minR1ToX1Ratio`: Rapporto minimo tra la resistenza di sequenza positiva dell'alimentatore di rete e la sua reattanza di sequenza positiva (R(1)/X(1) min). Utilizzato per lo scambio di dati di corto circuito secondo IEC 60909 Default: 0.0  - `minZ0ToZ1Ratio`: Rapporto minimo tra l'impedenza di sequenza zero e la sua impedenza di sequenza positiva (Z(0)/Z(1) min). Utilizzato per lo scambio di dati sul cortocircuito secondo IEC 60909 Default: 0.0  - `name`: Il nome di questo articolo.  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `p`: Iniezione di potenza attiva. Viene usata la convenzione del segno del carico, cioè il segno positivo significa flusso in uscita da un nodo. Valore di partenza per le soluzioni a stato stazionario. Predefinito: 0,0  - `q`: Iniezione di potenza reattiva. Viene usata la convenzione del segno del carico, cioè il segno positivo significa flusso in uscita da un nodo. Valore di partenza per soluzioni a stato stazionario. Predefinito: 0,0  - `referencePriority`: Priorità dell'unità per l'uso come selezione del bus di riferimento dell'angolo di fase della tensione del flusso di potenza. 0 = don t care (default) 1 = massima priorità. 2 è inferiore a 1 e così via. Predefinito: 0  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `type`: Tipo NGSI. Deve essere ExternalNetworkInjection  - `voltageFactor`: Fattore di tensione in pu, usato per calcolare la corrente di cortocircuito Ik` e la potenza Sk`. Predefinito: 0.0    
Proprietà richieste  
Adattato dai modelli di dati CIM e CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Questo modello di dati è una conversione diretta del Common Information Model (CIM) specificato dallo standard IEC61970 in modelli di dati intelligenti. Le classi python su cui si basa questo modello sono state sviluppate da queste entità Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) e RWTH University Aachen, Germania. Alcune proprietà possono avere un tipo sbagliato. Questo è stato il caso, si prega di sollevare un problema o inviare una mail a info@smartdatamodels.org.  
## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ExternalNetworkInjection:    
  description: 'Adapted from CIM data models. This class represents external network and it is used for IEC 60909 calculations.'    
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
    governorSCD:    
      description: 'Power Frequency Bias. This is the change in power injection divided by the change in frequency and negated.  A positive value of the power frequency bias provides additional power injection upon a drop in frequency. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &externalnetworkinjection_-_properties_-_owner_-_items_-_anyof    
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
    ikSecond:    
      description: 'Indicates whether initial symmetrical short-circuit current and power have been calculated according to IEC (Ik`). Default: False'    
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
    maxInitialSymShCCurrent:    
      description: 'Maximum initial symmetrical short-circuit currents (Ik` max) in A (Ik` = Sk`/(SQRT(3) Un)). Used for short circuit data exchange according to IEC 60909 Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    maxP:    
      description: 'Maximum active power of the injection. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    maxQ:    
      description: 'Not for short circuit modelling; It is used for modelling of infeed for load flow exchange. If maxQ and minQ are not used ReactiveCapabilityCurve can be used Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    maxR0ToX0Ratio:    
      description: 'Maximum ratio of zero sequence resistance of Network Feeder to its zero sequence reactance (R(0)/X(0) max). Used for short circuit data exchange according to IEC 60909 Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    maxR1ToX1Ratio:    
      description: 'Maximum ratio of positive sequence resistance of Network Feeder to its positive sequence reactance (R(1)/X(1) max). Used for short circuit data exchange according to IEC 60909 Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    maxZ0ToZ1Ratio:    
      description: 'Maximum ratio of zero sequence impedance to its positive sequence impedance (Z(0)/Z(1) max). Used for short circuit data exchange according to IEC 60909 Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    minInitialSymShCCurrent:    
      description: 'Minimum initial symmetrical short-circuit currents (Ik` min) in A (Ik` = Sk`/(SQRT(3) Un)). Used for short circuit data exchange according to IEC 60909 Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    minP:    
      description: 'Minimum active power of the injection. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    minQ:    
      description: 'Not for short circuit modelling; It is used for modelling of infeed for load flow exchange. If maxQ and minQ are not used ReactiveCapabilityCurve can be used Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    minR0ToX0Ratio:    
      description: 'Indicates whether initial symmetrical short-circuit current and power have been calculated according to IEC (Ik`). Used for short circuit data exchange according to IEC 6090 Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    minR1ToX1Ratio:    
      description: 'Minimum ratio of positive sequence resistance of Network Feeder to its positive sequence reactance (R(1)/X(1) min). Used for short circuit data exchange according to IEC 60909 Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    minZ0ToZ1Ratio:    
      description: 'Minimum ratio of zero sequence impedance to its positive sequence impedance (Z(0)/Z(1) min). Used for short circuit data exchange according to IEC 60909 Default: 0.0'    
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
        anyOf: *externalnetworkinjection_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    p:    
      description: 'Active power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for steady state solutions. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    q:    
      description: 'Reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for steady state solutions. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    referencePriority:    
      description: 'Priority of unit for use as powerflow voltage phase angle reference bus selection. 0 = don t care (default) 1 = highest priority. 2 is less than 1 and so on. Default: 0'    
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
      description: 'NGSI type. It has to be ExternalNetworkInjection'    
      enum:    
        - ExternalNetworkInjection    
      type: string    
      x-ngsi:    
        type: Property    
    voltageFactor:    
      description: 'Voltage factor in pu, which was used to calculate short-circuit current Ik` and power Sk`. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExternalNetworkInjection/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/ExternalNetworkInjection/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## Esempio di payloads  
Non è disponibile l'esempio di una ExternalNetworkInjection in formato JSON-LD come key-values. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
Non è disponibile l'esempio di una ExternalNetworkInjection in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
Non è disponibile l'esempio di una ExternalNetworkInjection in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
Non è disponibile l'esempio di una ExternalNetworkInjection in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
