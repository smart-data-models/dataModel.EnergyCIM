<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: WindContPType3IEC  
=========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/WindContPType3IEC/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Adattato dai modelli di dati CIM. Modello di controllo P Tipo 3.  Riferimento: Norma IEC 61400-27-1 Sezione 6.6.5.3.**  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `WindDynamicsLookupTable[number]`: Il modello di controllo P di tipo 3 a cui è associata questa tabella di ricerca sulla dinamica del vento. Predefinito: "elenco".  . Model: [https://schema.org/Number](https://schema.org/Number)- `WindGenTurbineType3IEC[number]`: Modello di turbina eolica di tipo 3 a cui è associato questo modello Wind control P di tipo 3. Predefinito: Nessuno  . Model: [https://schema.org/Number](https://schema.org/Number)- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated[string]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateModified[string]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `description[string]`: Descrizione dell'articolo  - `dpmax[number]`: Velocità di rampa della potenza massima della turbina eolica (). È un parametro che dipende dal progetto. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dtrisemaxlvrt[number]`: Limitazione del tasso di aumento della coppia durante la LVRT per S (d). È un parametro dipendente dal progetto. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identificatore univoco dell'entità  - `kdtd[number]`: Guadagno per lo smorzamento attivo della trasmissione (). È un parametro dipendente dal tipo. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kip[number]`: Parametro di integrazione del controllore PI (). È un parametro dipendente dal tipo. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kpp[number]`: Guadagno proporzionale del regolatore PI (). È un parametro dipendente dal tipo. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Riferimento Geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `mplvrt[number]`: Abilita la modalità di controllo della potenza LVRT (M true = 1: controllo della tensione false = 0: controllo della potenza reattiva.  È un parametro dipendente dal progetto. Predefinito: Falso  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: Il nome di questo elemento.  - `omegaoffset[number]`: Offset al valore di riferimento che limita l'azione del regolatore durante le variazioni di velocità del rotore (omega). È un parametro dipendente dal caso. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `pdtdmax[number]`: Potenza massima attiva di smorzamento della trasmissione (). È un parametro dipendente dal tipo. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rramp[number]`: Limitazione di rampa della coppia, richiesta in alcuni codici di rete (). È un parametro dipendente dal progetto. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `tdvs[number]`: Ritardo dopo le cadute di tensione profonde (T). È un parametro dipendente dal progetto. Predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `temin[number]`: Coppia minima del generatore elettrico (). È un parametro dipendente dal tipo. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tomegafilt[number]`: Costante di tempo del filtro per la misura della velocità del generatore (). È un parametro dipendente dal tipo. Predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tpfilt[number]`: Costante di tempo del filtro per la misura di potenza (). È un parametro dipendente dal tipo. Predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tpord[number]`: Costante di tempo in ritardo di ordine di potenza (). È un parametro dipendente dal tipo. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tufilt[number]`: Costante di tempo del filtro per la misurazione della tensione (). È un parametro dipendente dal tipo. Predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tuscale[number]`: Fattore di scala della tensione della coppia di ripristino (T). È un parametro dipendente dal progetto. Predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `twref[number]`: Costante di tempo nel filtro di riferimento della velocità (). È un parametro dipendente dal tipo. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Tipo NGSI. Deve essere WindContPType3IEC  - `udvs[number]`: Limite di tensione per il mantenimento dello stato LVRT dopo forti cali di tensione (). È un parametro dipendente dal progetto. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `updip[number]`: Soglia di caduta di tensione per il controllo P ().  Parte del controllo della turbina, spesso diversa (ad esempio 0,8) dalle soglie del convertitore. È un parametro che dipende dal progetto. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `wdtd[number]`: Frequenza di smorzamento attivo della trasmissione (omega). Può essere calcolata da due parametri del modello di massa. È un parametro dipendente dal tipo. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `zeta[number]`: Coefficiente di smorzamento attivo della trasmissione (zeta). È un parametro dipendente dal tipo. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
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
WindContPType3IEC:    
  description: 'Adapted from CIM data models. P control model Type 3.  Reference: IEC Standard 61400-27-1 Section 6.6.5.3.'    
  properties:    
    WindDynamicsLookupTable:    
      description: 'The P control type 3 model with which this wind dynamics lookup table is associated. Default: ''list'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    WindGenTurbineType3IEC:    
      description: 'Wind turbine type 3 model with which this Wind control P type 3 model is associated. Default: None'    
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
    dpmax:    
      description: 'Maximum wind turbine power ramp rate (). It is project dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dtrisemaxlvrt:    
      description: 'Limitation of torque rise rate during LVRT for S (d). It is project dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &windcontptype3iec_-_properties_-_owner_-_items_-_anyof    
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
    kdtd:    
      description: 'Gain for active drive train damping (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kip:    
      description: 'PI controller integration parameter (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kpp:    
      description: 'PI controller proportional gain (). It is type dependent parameter. Default: 0.0'    
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
    mplvrt:    
      description: 'Enable LVRT power control mode (M true = 1: voltage control false = 0: reactive power control.  It is project dependent parameter. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    omegaoffset:    
      description: 'Offset to reference value that limits controller action during rotor speed changes (omega). It is case dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *windcontptype3iec_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    pdtdmax:    
      description: 'Maximum active drive train damping power (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rramp:    
      description: 'Ramp limitation of torque, required in some grid codes (). It is project dependent parameter. Default: 0.0'    
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
    tdvs:    
      description: 'Timedelay after deep voltage sags (T). It is project dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    temin:    
      description: 'Minimum electrical generator torque (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tomegafilt:    
      description: 'Filter time constant for generator speed measurement (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tpfilt:    
      description: 'Filter time constant for power measurement (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tpord:    
      description: 'Time constant in power order lag (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tufilt:    
      description: 'Filter time constant for voltage measurement (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tuscale:    
      description: 'Voltage scaling factor of reset-torque (T). It is project dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    twref:    
      description: 'Time constant in speed reference filter (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be WindContPType3IEC'    
      enum:    
        - WindContPType3IEC    
      type: string    
      x-ngsi:    
        type: Property    
    udvs:    
      description: 'Voltage limit for hold LVRT status after deep voltage sags (). It is project dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    updip:    
      description: 'Voltage dip threshold for P-control ().  Part of turbine control, often different (e.g 0.8) from converter thresholds. It is project dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    wdtd:    
      description: 'Active drive train damping frequency (omega). It can be calculated from two mass model parameters. It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    zeta:    
      description: 'Coefficient for active drive train damping (zeta). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindContPType3IEC/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/WindContPType3IEC/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
Non è disponibile l'esempio di un WindContPType3IEC in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
Non è disponibile l'esempio di un WindContPType3IEC in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
Non è disponibile l'esempio di un WindContPType3IEC in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
Non è disponibile l'esempio di un WindContPType3IEC in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
