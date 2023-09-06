<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: GovHydroWEH  
===================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovHydroWEH/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Adattato dai modelli di dati CIM. Modello governatore idroelettrico Woodward Electric.**  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale.    
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `db[number]`: Banda morta della velocità (db). Predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: Descrizione dell'articolo  - `dicn[number]`: Valore che consente al regolatore integrale di avanzare oltre i limiti del gate (Dicn). Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dpv[number]`: Valore che consente al controllore della valvola pilota di avanzare oltre i limiti della porta (Dpv). Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dturb[number]`: Fattore di smorzamento della turbina (Dturb).  Unità = delta P (PU di MWbase) / delta velocità (PU). Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `feedbackSignal[number]`: Selezione del segnale di retroazione (Sw). true = Uscita PID (se R-Perm-Gate=droop e R-Perm-Pe=0) false = Potenza elettrica (se R-Perm-Gate=0 e R-Perm-Pe=droop) o false = Posizione gate (se R-Perm-Gate=droop e R-Perm-Pe=0). Predefinito: Falso  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl1[number]`: Porta di flusso 1 (Fl1).  Valore del flusso per il punto di posizione 1 della paratoia per la tabella di lookup che rappresenta il flusso dell'acqua attraverso la turbina in funzione della posizione della paratoia per produrre un flusso a regime. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl2[number]`: Porta di flusso 2 (Fl2).  Valore del flusso per il punto 2 della posizione della paratoia per la tabella di lookup che rappresenta il flusso dell'acqua attraverso la turbina in funzione della posizione della paratoia per produrre un flusso a regime. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl3[number]`: Porta di flusso 3 (Fl3).  Valore del flusso per il punto 3 della posizione della paratoia per la tabella di lookup che rappresenta il flusso dell'acqua attraverso la turbina in funzione della posizione della paratoia per produrre un flusso a regime. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl4[number]`: Porta di flusso 4 (Fl4).  Valore del flusso per il punto 4 della posizione della paratoia per la tabella di lookup che rappresenta il flusso dell'acqua attraverso la turbina in funzione della posizione della paratoia per produrre un flusso a regime. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl5[number]`: Porta di flusso 5 (Fl5).  Valore del flusso per il punto 5 della posizione della paratoia per la tabella di lookup che rappresenta il flusso dell'acqua attraverso la turbina in funzione della posizione della paratoia per produrre un flusso a regime. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp1[number]`: Flusso P1 (Fp1).  Valore del flusso della turbina per il punto 1 della tabella di ricerca che rappresenta la potenza meccanica unitaria sul valore nominale MVA della macchina in funzione del flusso della turbina. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp10[number]`: Flusso P10 (Fp10).  Valore del flusso della turbina per il punto 10 della tabella di ricerca che rappresenta la potenza meccanica unitaria sul rating MVA della macchina in funzione del flusso della turbina. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp2[number]`: Flusso P2 (Fp2).  Valore del flusso della turbina per il punto 2 della tabella di ricerca che rappresenta la potenza meccanica unitaria sulla potenza nominale MVA della macchina in funzione del flusso della turbina. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp3[number]`: Flusso P3 (Fp3).  Valore del flusso della turbina per il punto 3 della tabella di ricerca che rappresenta la potenza meccanica unitaria sulla potenza nominale MVA della macchina in funzione del flusso della turbina. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp4[number]`: Flusso P4 (Fp4).  Valore del flusso della turbina per il punto 4 della tabella di ricerca che rappresenta la potenza meccanica unitaria sulla potenza nominale MVA della macchina in funzione del flusso della turbina. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp5[number]`: Flusso P5 (Fp5).  Valore del flusso della turbina per il punto 5 della tabella di ricerca che rappresenta la potenza meccanica unitaria sul rating MVA della macchina in funzione del flusso della turbina. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp6[number]`: Flusso P6 (Fp6).  Valore del flusso della turbina per il punto 6 della tabella di ricerca che rappresenta la potenza meccanica unitaria sul rating MVA della macchina in funzione del flusso della turbina. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp7[number]`: Flusso P7 (Fp7).  Valore del flusso della turbina per il punto 7 della tabella di ricerca che rappresenta la potenza meccanica unitaria sul rating MVA della macchina in funzione del flusso della turbina. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp8[number]`: Flusso P8 (Fp8).  Valore del flusso della turbina per il punto 8 della tabella di ricerca che rappresenta la potenza meccanica unitaria sul rating MVA della macchina in funzione del flusso della turbina. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp9[number]`: Flusso P9 (Fp9).  Valore del flusso della turbina per il punto 9 della tabella di ricerca che rappresenta la potenza meccanica unitaria sulla potenza nominale MVA della macchina in funzione del flusso della turbina. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gmax[number]`: Posizione massima del cancello (Gmax). Predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gmin[number]`: Posizione minima del gate (Gmin). Predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gtmxcl[number]`: Velocità massima di chiusura del cancello (Gtmxcl). Predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gtmxop[number]`: Velocità massima di apertura del gate (Gtmxop). Predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv1[number]`: Porta 1 (Gv1).  Valore della posizione della paratoia per il punto 1 della tabella di ricerca che rappresenta il flusso dell'acqua attraverso la turbina in funzione della posizione della paratoia per produrre un flusso a regime. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv2[number]`: Porta 2 (Gv2).  Valore della posizione della paratoia per il punto 2 della tabella di ricerca che rappresenta il flusso dell'acqua attraverso la turbina in funzione della posizione della paratoia per produrre un flusso a regime. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv3[number]`: Gate 3 (Gv3).  Valore della posizione della paratoia per il punto 3 della tabella di ricerca che rappresenta il flusso dell'acqua attraverso la turbina in funzione della posizione della paratoia per produrre un flusso a regime. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv4[number]`: Gate 4 (Gv4).  Valore della posizione della paratoia per il punto 4 della tabella di ricerca che rappresenta il flusso dell'acqua attraverso la turbina in funzione della posizione della paratoia per produrre un flusso a regime. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv5[number]`: Porta 5 (Gv5).  Valore della posizione della paratoia per il punto 5 della tabella di lookup che rappresenta il flusso dell'acqua attraverso la turbina in funzione della posizione della paratoia per produrre un flusso a regime. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identificatore univoco dell'entità  - `kd[number]`: Guadagno derivato del regolatore (Kd). Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ki[number]`: Regolatore derivativo Guadagno integrale (Ki). Predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kp[number]`: Guadagno del controllo derivativo (Kp). Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `mwbase[number]`: Base per i valori di potenza (MWbase) (>0).  Unità = MW. Predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: Il nome di questo elemento  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `pmss1[number]`: Flusso Pmss P1 (Pmss1).  Potenza meccanica in uscita Pmss per il punto 1 del flusso della turbina per la tabella di ricerca che rappresenta la potenza meccanica unitaria sulla potenza nominale MVA della macchina in funzione del flusso della turbina. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss10[number]`: Flusso Pmss P10 (Pmss10).  Potenza meccanica in uscita Pmss per il punto 10 del flusso della turbina per la tabella di ricerca che rappresenta la potenza meccanica unitaria sul rating MVA della macchina in funzione del flusso della turbina. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss2[number]`: Flusso Pmss P2 (Pmss2).  Potenza meccanica in uscita Pmss per il punto 2 del flusso della turbina per la tabella di ricerca che rappresenta la potenza meccanica unitaria sul rating MVA della macchina in funzione del flusso della turbina. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss3[number]`: Flusso Pmss P3 (Pmss3).  Potenza meccanica in uscita Pmss per il punto 3 del flusso della turbina per la tabella di ricerca che rappresenta la potenza meccanica unitaria sulla potenza nominale MVA della macchina in funzione del flusso della turbina. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss4[number]`: Flusso Pmss P4 (Pmss4).  Potenza meccanica in uscita Pmss per il punto 4 del flusso della turbina per la tabella di ricerca che rappresenta la potenza meccanica unitaria sul rating MVA della macchina in funzione del flusso della turbina. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss5[number]`: Flusso Pmss P5 (Pmss5).  Potenza meccanica in uscita Pmss per il punto 5 del flusso della turbina per la tabella di ricerca che rappresenta la potenza meccanica unitaria sulla potenza nominale MVA della macchina in funzione del flusso della turbina. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss6[number]`: Flusso Pmss P6 (Pmss6).  Potenza meccanica in uscita Pmss per il punto 6 del flusso della turbina per la tabella di ricerca che rappresenta la potenza meccanica unitaria sul rating MVA della macchina in funzione del flusso della turbina. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss7[number]`: Flusso Pmss P7 (Pmss7).  Potenza meccanica in uscita Pmss per il punto 7 del flusso della turbina per la tabella di ricerca che rappresenta la potenza meccanica unitaria sul rating MVA della macchina in funzione del flusso della turbina. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss8[number]`: Flusso Pmss P8 (Pmss8).  Potenza meccanica in uscita Pmss per il punto 8 del flusso della turbina per la tabella di ricerca che rappresenta la potenza meccanica unitaria sul rating MVA della macchina in funzione del flusso della turbina. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss9[number]`: Flusso Pmss P9 (Pmss9).  Potenza meccanica in uscita Pmss per il punto 9 del flusso della turbina per la tabella di ricerca che rappresenta la potenza meccanica unitaria sul rating MVA della macchina in funzione del flusso della turbina. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rpg[number]`: Droop permanente per la retroazione dell'uscita del regolatore (R-Perm-Gate). Predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rpp[number]`: Droop permanente per il feedback di potenza elettrica (R-Perm-Pe). Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `td[number]`: Costante di tempo del controllore della derivata per limitare la caratteristica della derivata oltre una frequenza di breakdown per evitare l'amplificazione del rumore ad alta frequenza (Td). Predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tdv[number]`: Costante di tempo di ritardo della valvola distributrice (Tdv). Predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tg[number]`: Valore che consente al controller della valvola di distribuzione di avanzare oltre il limite della velocità di movimento della paratoia (Tg). Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tp[number]`: Costante di tempo di ritardo della valvola pilota (Tp). Predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tpe[number]`: Costante di tempo di droop della potenza elettrica (Tpe). Predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw[number]`: Costante di tempo di inerzia dell'acqua (Tw) (>0). Predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Tipo NGSI. Deve essere GovHydroWEH  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
<!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Adattato dai modelli di dati CIM e CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Questo modello di dati è una conversione diretta del Common Information Model (CIM) specificato dallo standard IEC61970 in modelli di dati intelligenti. Le classi python su cui si basa questo modello sono state sviluppate da questi enti Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) e RWTH University Aachen, Germania. Alcune proprietà possono avere un tipo sbagliato. In questo caso, si prega di segnalare un problema o di inviare una mail a info@smartdatamodels.org.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GovHydroWEH:    
  description: Adapted from CIM data models. Woodward Electric Hydro Governor Model.    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
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
      description: A description of this item    
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
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
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
        - description: Geojson reference to the item. Point    
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
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
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
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
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
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
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
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    mwbase:    
      description: 'Base for power values (MWbase) (>0).  Unit = MW. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
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
      description: list of uri pointing to additional resources about the item    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
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
      description: NGSI type. It has to be GovHydroWEH    
      enum:    
        - GovHydroWEH    
      type: string    
      x-ngsi:    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovHydroWEH/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/GovHydroWEH/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
Non è disponibile l'esempio di un GovHydroWEH in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
Non è disponibile l'esempio di un GovHydroWEH in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
Non è disponibile l'esempio di un GovHydroWEH in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
Non è disponibile l'esempio di un GovHydroWEH in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
