Entità: GovHydroWEH  
===================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovHydroWEH/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Adattato dai modelli di dati CIM. Woodward Electric Hydro Governor Model.**  

## Elenco delle proprietà  

- `address`: L'indirizzo postale  - `alternateName`: Un nome alternativo per questa voce  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `db`: Banda morta della velocità (db). Predefinito: 0.0  - `description`: Una descrizione di questo articolo  - `dicn`: Valore che permette al regolatore integrale di avanzare oltre i limiti del gate (Dicn). Predefinito: 0.0  - `dpv`: Valore per permettere al controllore della valvola pilota di avanzare oltre i limiti del cancello (Dpv). Predefinito: 0,0  - `dturb`: Fattore di smorzamento della turbina (Dturb).  Unità = delta P (PU di MWbase) / delta velocità (PU). Predefinito: 0,0  - `feedbackSignal`: Selezione del segnale di feedback (Sw). true = Uscita PID (se R-Perm-Gate=droop e R-Perm-Pe=0) false = Potenza elettrica (se R-Perm-Gate=0 e R-Perm-Pe=droop) o false = Posizione Gate (se R-Perm-Gate=droop e R-Perm-Pe=0). Predefinito: Falso  - `fl1`: Portata del gate 1 (Fl1).  Valore di flusso per il punto 1 della posizione del gate per la tabella di ricerca che rappresenta il flusso d'acqua attraverso la turbina in funzione della posizione del gate per produrre un flusso costante. Predefinito: 0.0  - `fl2`: Portata del gate 2 (Fl2).  Valore di flusso per il punto 2 della posizione del gate per la tabella di ricerca che rappresenta il flusso d'acqua attraverso la turbina in funzione della posizione del gate per produrre un flusso costante. Predefinito: 0.0  - `fl3`: Portata del gate 3 (Fl3).  Valore di flusso per il punto 3 della posizione del gate per la tabella di ricerca che rappresenta il flusso d'acqua attraverso la turbina in funzione della posizione del gate per produrre un flusso costante. Predefinito: 0.0  - `fl4`: Portata del gate 4 (Fl4).  Valore di flusso per il punto 4 della posizione del gate per la tabella di ricerca che rappresenta il flusso d'acqua attraverso la turbina in funzione della posizione del gate per produrre un flusso costante. Predefinito: 0.0  - `fl5`: Portata del gate 5 (Fl5).  Valore di flusso per il punto 5 della posizione del gate per la tabella di ricerca che rappresenta il flusso d'acqua attraverso la turbina in funzione della posizione del gate per produrre un flusso costante. Predefinito: 0.0  - `fp1`: Flusso P1 (Fp1).  Valore del flusso della turbina per il punto 1 della tabella di ricerca che rappresenta la potenza meccanica per unità sulla potenza nominale MVA della macchina in funzione del flusso della turbina. Predefinito: 0.0  - `fp10`: Flusso P10 (Fp10).  Valore del flusso della turbina per il punto 10 per la tabella di ricerca che rappresenta la potenza meccanica per unità sul valore nominale MVA della macchina in funzione del flusso della turbina. Predefinito: 0.0  - `fp2`: Flusso P2 (Fp2).  Valore del flusso della turbina per il punto 2 della tabella di ricerca che rappresenta la potenza meccanica per unità sul valore nominale MVA della macchina in funzione del flusso della turbina. Predefinito: 0.0  - `fp3`: Flusso P3 (Fp3).  Valore del flusso della turbina per il punto 3 della tabella di ricerca che rappresenta la potenza meccanica per unità sulla potenza nominale MVA della macchina in funzione del flusso della turbina. Predefinito: 0.0  - `fp4`: Flusso P4 (Fp4).  Valore del flusso della turbina per il punto 4 della tabella di ricerca che rappresenta la potenza meccanica per unità sul valore nominale MVA della macchina in funzione del flusso della turbina. Predefinito: 0.0  - `fp5`: Flusso P5 (Fp5).  Valore del flusso della turbina per il punto 5 della tabella di ricerca che rappresenta la potenza meccanica per unità sul valore nominale MVA della macchina in funzione del flusso della turbina. Predefinito: 0.0  - `fp6`: Flusso P6 (Fp6).  Valore del flusso della turbina per il punto 6 della tabella di ricerca che rappresenta la potenza meccanica per unità sul valore nominale MVA della macchina in funzione del flusso della turbina. Predefinito: 0.0  - `fp7`: Flusso P7 (Fp7).  Valore del flusso della turbina per il punto 7 della tabella di ricerca che rappresenta la potenza meccanica per unità sul valore nominale MVA della macchina in funzione del flusso della turbina. Predefinito: 0.0  - `fp8`: Flusso P8 (Fp8).  Valore del flusso della turbina per il punto 8 della tabella di ricerca che rappresenta la potenza meccanica per unità sul valore nominale MVA della macchina in funzione del flusso della turbina. Predefinito: 0.0  - `fp9`: Flusso P9 (Fp9).  Valore del flusso della turbina per il punto 9 della tabella di ricerca che rappresenta la potenza meccanica per unità sul valore nominale MVA della macchina in funzione del flusso della turbina. Predefinito: 0.0  - `gmax`: Posizione massima del cancello (Gmax). Predefinito: 0.0  - `gmin`: Posizione minima del cancello (Gmin). Predefinito: 0.0  - `gtmxcl`: Tasso massimo di chiusura del cancello (Gtmxcl). Predefinito: 0,0  - `gtmxop`: Tasso massimo di apertura del cancello (Gtmxop). Predefinito: 0,0  - `gv1`: Cancello 1 (Gv1).  Valore di posizione del cancello per il punto 1 per la tabella di ricerca che rappresenta il flusso d'acqua attraverso la turbina in funzione della posizione del cancello per produrre un flusso costante. Predefinito: 0.0  - `gv2`: Cancello 2 (Gv2).  Valore di posizione del cancello per il punto 2 per la tabella di ricerca che rappresenta il flusso d'acqua attraverso la turbina in funzione della posizione del cancello per produrre un flusso costante. Predefinito: 0.0  - `gv3`: Gate 3 (Gv3).  Valore di posizione del cancello per il punto 3 per la tabella di ricerca che rappresenta il flusso d'acqua attraverso la turbina in funzione della posizione del cancello per produrre un flusso costante. Predefinito: 0.0  - `gv4`: Cancello 4 (Gv4).  Valore di posizione del cancello per il punto 4 per la tabella di ricerca che rappresenta il flusso d'acqua attraverso la turbina in funzione della posizione del cancello per produrre un flusso costante. Predefinito: 0.0  - `gv5`: Gate 5 (Gv5).  Valore di posizione del cancello per il punto 5 per la tabella di ricerca che rappresenta il flusso d'acqua attraverso la turbina in funzione della posizione del cancello per produrre un flusso costante. Predefinito: 0.0  - `id`: Identificatore unico dell'entità  - `kd`: Guadagno derivato del regolatore di derivazione (Kd). Predefinito: 0.0  - `ki`: Regolatore di derivazione Guadagno integrale (Ki). Predefinito: 0.0  - `kp`: Guadagno di controllo della derivata (Kp). Predefinito: 0,0  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `mwbase`: Base per i valori di potenza (MWbase) (>0).  Unità = MW. Predefinito: 0,0  - `name`: Il nome di questo articolo.  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `pmss1`: Flusso Pmss P1 (Pmss1).  Potenza meccanica in uscita Pmss per il punto 1 del flusso della turbina per la tabella di ricerca che rappresenta la potenza meccanica per unità sulla potenza MVA della macchina in funzione del flusso della turbina. Predefinito: 0,0  - `pmss10`: Flusso Pmss P10 (Pmss10).  Potenza meccanica in uscita Pmss per il punto 10 del flusso della turbina per la tabella di ricerca che rappresenta la potenza meccanica per unità sul valore nominale MVA della macchina in funzione del flusso della turbina. Predefinito: 0.0  - `pmss2`: Flusso Pmss P2 (Pmss2).  Potenza meccanica in uscita Pmss per il punto 2 del flusso della turbina per la tabella di ricerca che rappresenta la potenza meccanica per unità sul valore nominale MVA della macchina in funzione del flusso della turbina. Predefinito: 0.0  - `pmss3`: Flusso Pmss P3 (Pmss3).  Potenza meccanica in uscita Pmss per il punto 3 del flusso della turbina per la tabella di ricerca che rappresenta la potenza meccanica per unità sul valore nominale MVA della macchina in funzione del flusso della turbina. Predefinito: 0,0  - `pmss4`: Flusso Pmss P4 (Pmss4).  Potenza meccanica in uscita Pmss per il punto 4 del flusso della turbina per la tabella di ricerca che rappresenta la potenza meccanica per unità sul valore nominale MVA della macchina in funzione del flusso della turbina. Predefinito: 0,0  - `pmss5`: Flusso Pmss P5 (Pmss5).  Potenza meccanica in uscita Pmss per il punto 5 del flusso della turbina per la tabella di ricerca che rappresenta la potenza meccanica per unità sul valore nominale MVA della macchina in funzione del flusso della turbina. Predefinito: 0,0  - `pmss6`: Pmss Flow P6 (Pmss6).  Potenza meccanica in uscita Pmss per il punto 6 del flusso della turbina per la tabella di ricerca che rappresenta la potenza meccanica per unità sul valore nominale MVA della macchina in funzione del flusso della turbina. Predefinito: 0.0  - `pmss7`: Flusso Pmss P7 (Pmss7).  Potenza meccanica in uscita Pmss per il punto 7 del flusso della turbina per la tabella di ricerca che rappresenta la potenza meccanica per unità sul valore nominale MVA della macchina in funzione del flusso della turbina. Predefinito: 0,0  - `pmss8`: Flusso Pmss P8 (Pmss8).  Potenza meccanica in uscita Pmss per il punto 8 del flusso della turbina per la tabella di ricerca che rappresenta la potenza meccanica per unità sul valore nominale MVA della macchina in funzione del flusso della turbina. Predefinito: 0.0  - `pmss9`: Flusso Pmss P9 (Pmss9).  Potenza meccanica in uscita Pmss per il punto 9 del flusso della turbina per la tabella di ricerca che rappresenta la potenza meccanica per unità sul valore nominale MVA della macchina in funzione del flusso della turbina. Predefinito: 0.0  - `rpg`: Statismo permanente per il feedback dell'uscita del regolatore (R-Perm-Gate). Predefinito: 0,0  - `rpp`: Statismo permanente per il feedback di potenza elettrica (R-Perm-Pe). Predefinito: 0,0  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `td`: Costante di tempo del controllore della derivata per limitare la caratteristica della derivata oltre una frequenza di breakdown per evitare l'amplificazione del rumore ad alta frequenza (Td). Predefinito: 0  - `tdv`: Costante di tempo di ritardo della valvola distributiva (Tdv). Predefinito: 0  - `tg`: Valore che permette al controllore della valvola di distribuzione di avanzare oltre il limite di velocità di movimento del cancello (Tg). Predefinito: 0  - `tp`: Costante di tempo di ritardo della valvola pilota (Tp). Predefinito: 0  - `tpe`: Costante di tempo dello statismo della potenza elettrica (Tpe). Predefinito: 0  - `tw`: Costante di tempo di inerzia dell'acqua (Tw) (>0). Predefinito: 0  - `type`: Tipo di NGSI. Deve essere GovHydroWEH    
Proprietà richieste  
Adattato dai modelli di dati CIM e CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Questo modello di dati è una conversione diretta del Common Information Model (CIM) specificato dallo standard IEC61970 in modelli di dati intelligenti. Le classi python su cui si basa questo modello sono state sviluppate da queste entità Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) e RWTH University Aachen, Germania. Alcune proprietà possono avere un tipo sbagliato. Questo è stato il caso, si prega di sollevare un problema o inviare una mail a info@smartdatamodels.org.  
## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GovHydroWEH:    
  description: 'Adapted from CIM data models. Woodward Electric Hydro Governor Model.'    
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
    db:    
      description: 'Speed Dead Band (db). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    dicn:    
      description: 'Value to allow the integral controller to advance beyond the gate limits (Dicn). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dpv:    
      description: 'Value to allow the Pilot valve controller to advance beyond the gate limits (Dpv). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dturb:    
      description: 'Turbine damping factor (Dturb).  Unit = delta P (PU of MWbase) / delta speed (PU). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    feedbackSignal:    
      description: 'Feedback signal selection (Sw). true = PID Output (if R-Perm-Gate=droop and R-Perm-Pe=0) false = Electrical Power (if R-Perm-Gate=0 and R-Perm-Pe=droop) or false = Gate Position (if R-Perm-Gate=droop and R-Perm-Pe=0). Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fl1:    
      description: 'Flow Gate 1 (Fl1).  Flow value for gate position point 1 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fl2:    
      description: 'Flow Gate 2 (Fl2).  Flow value for gate position point 2 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fl3:    
      description: 'Flow Gate 3 (Fl3).  Flow value for gate position point 3 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fl4:    
      description: 'Flow Gate 4 (Fl4).  Flow value for gate position point 4 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fl5:    
      description: 'Flow Gate 5 (Fl5).  Flow value for gate position point 5 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp1:    
      description: 'Flow P1 (Fp1).  Turbine Flow value for point 1 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp10:    
      description: 'Flow P10 (Fp10).  Turbine Flow value for point 10 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp2:    
      description: 'Flow P2 (Fp2).  Turbine Flow value for point 2 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp3:    
      description: 'Flow P3 (Fp3).  Turbine Flow value for point 3 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp4:    
      description: 'Flow P4 (Fp4).  Turbine Flow value for point 4 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp5:    
      description: 'Flow P5 (Fp5).  Turbine Flow value for point 5 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp6:    
      description: 'Flow P6 (Fp6).  Turbine Flow value for point 6 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp7:    
      description: 'Flow P7 (Fp7).  Turbine Flow value for point 7 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp8:    
      description: 'Flow P8 (Fp8).  Turbine Flow value for point 8 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp9:    
      description: 'Flow P9 (Fp9).  Turbine Flow value for point 9 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gmax:    
      description: 'Maximum Gate Position (Gmax). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gmin:    
      description: 'Minimum Gate Position (Gmin). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gtmxcl:    
      description: 'Maximum gate closing rate (Gtmxcl). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gtmxop:    
      description: 'Maximum gate opening rate (Gtmxop). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv1:    
      description: 'Gate 1 (Gv1).  Gate Position value for point 1 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv2:    
      description: 'Gate 2 (Gv2).  Gate Position value for point 2 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv3:    
      description: 'Gate 3 (Gv3).  Gate Position value for point 3 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv4:    
      description: 'Gate 4 (Gv4).  Gate Position value for point 4 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv5:    
      description: 'Gate 5 (Gv5).  Gate Position value for point 5 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &govhydroweh_-_properties_-_owner_-_items_-_anyof    
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
    kd:    
      description: 'Derivative controller derivative gain (Kd). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ki:    
      description: 'Derivative controller Integral gain (Ki). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kp:    
      description: 'Derivative control gain (Kp). Default: 0.0'    
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
    mwbase:    
      description: 'Base for power values (MWbase) (>0).  Unit = MW. Default: 0.0'    
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
        anyOf: *govhydroweh_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    pmss1:    
      description: 'Pmss Flow P1 (Pmss1).  Mechanical Power output Pmss for Turbine Flow point 1 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss10:    
      description: 'Pmss Flow P10 (Pmss10).  Mechanical Power output Pmss for Turbine Flow point 10 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss2:    
      description: 'Pmss Flow P2 (Pmss2).  Mechanical Power output Pmss for Turbine Flow point 2 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss3:    
      description: 'Pmss Flow P3 (Pmss3).  Mechanical Power output Pmss for Turbine Flow point 3 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss4:    
      description: 'Pmss Flow P4 (Pmss4).  Mechanical Power output Pmss for Turbine Flow point 4 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss5:    
      description: 'Pmss Flow P5 (Pmss5).  Mechanical Power output Pmss for Turbine Flow point 5 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss6:    
      description: 'Pmss Flow P6 (Pmss6).  Mechanical Power output Pmss for Turbine Flow point 6 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss7:    
      description: 'Pmss Flow P7 (Pmss7).  Mechanical Power output Pmss for Turbine Flow point 7 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss8:    
      description: 'Pmss Flow P8 (Pmss8).  Mechanical Power output Pmss for Turbine Flow point 8 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss9:    
      description: 'Pmss Flow P9 (Pmss9).  Mechanical Power output Pmss for Turbine Flow point 9 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rpg:    
      description: 'Permanent droop for governor output feedback (R-Perm-Gate). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rpp:    
      description: 'Permanent droop for electrical power feedback (R-Perm-Pe). Default: 0.0'    
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
    td:    
      description: 'Derivative controller time constant to limit the derivative characteristic beyond a breakdown frequency to avoid amplification of high-frequency noise (Td). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tdv:    
      description: 'Distributive Valve time lag time constant (Tdv). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tg:    
      description: 'Value to allow the Distribution valve controller to advance beyond the gate movement rate limit (Tg). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tp:    
      description: 'Pilot Valve time lag time constant (Tp). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tpe:    
      description: 'Electrical power droop time constant (Tpe). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tw:    
      description: 'Water inertia time constant (Tw) (>0). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be GovHydroWEH'    
      enum:    
        - GovHydroWEH    
      type: string    
      x-ngsi:    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovHydroWEH/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/GovHydroWEH/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## Esempio di payloads  
Non è disponibile l'esempio di un GovHydroWEH in formato JSON-LD come key-values. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
Non disponibile l'esempio di un GovHydroWEH in formato JSON-LD come normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
Non è disponibile l'esempio di un GovHydroWEH in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
Non disponibile l'esempio di un GovHydroWEH in formato JSON-LD come normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per avere una risposta su come trattare le unità di grandezza