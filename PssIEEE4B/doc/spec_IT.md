<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: PssIEEE4B  
=================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/PssIEEE4B/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Adattato dai modelli di dati CIM. La classe rappresenta il modello di stabilizzatore del sistema di alimentazione PSS2B di tipo IEEE Std 421.5-2005. Il modello PSS4B rappresenta una struttura basata su bande di frequenza multiple. In questo PSS delta-omega (ingresso di velocità) vengono utilizzate tre bande separate, rispettivamente dedicate ai modi di oscillazione a bassa, media e alta frequenza.  Riferimento: IEEE 4B 421.5-2005 Sezione 8.4.**  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `bwh1[number]`: Filtro notch 1 (banda ad alta frequenza): Larghezza di banda di tre dB (B). Predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bwh2[number]`: Filtro notch 2 (banda ad alta frequenza): Larghezza di banda di tre dB (B). Predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bwl1[number]`: Filtro notch 1 (banda a bassa frequenza): Larghezza di banda di tre dB (B). Predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bwl2[number]`: Filtro notch 2 (banda a bassa frequenza): Larghezza di banda di tre dB (B). Predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated[string]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateModified[string]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `description[string]`: Descrizione dell'articolo  - `id[*]`: Identificatore univoco dell'entità  - `kh[number]`: Guadagno in banda alta (K).  Valore tipico = 120. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kh1[number]`: Guadagno del filtro differenziale ad alta banda (K).  Valore tipico = 66. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kh11[number]`: Coefficiente di blocco del primo lead-lag in banda alta (K).  Valore tipico = 1. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kh17[number]`: Coefficiente di blocco del primo lead-lag in banda alta (K).  Valore tipico = 1. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kh2[number]`: Guadagno del filtro differenziale ad alta banda (K).  Valore tipico = 66. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ki[number]`: Guadagno della banda intermedia (K).  Valore tipico = 30. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ki1[number]`: Guadagno del filtro differenziale a banda intermedia (K).  Valore tipico = 66. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ki11[number]`: Coefficiente di blocco della prima banda intermedia (K).  Valore tipico = 1. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ki17[number]`: Coefficiente di blocco della prima banda intermedia (K).  Valore tipico = 1. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ki2[number]`: Guadagno del filtro differenziale a banda intermedia (K).  Valore tipico = 66. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kl[number]`: Guadagno in banda bassa (K).  Valore tipico = 7,5. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kl1[number]`: Guadagno del filtro differenziale a bassa banda (K).  Valore tipico = 66. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kl11[number]`: Coefficiente di blocco del primo lead-lag in banda bassa (K).  Valore tipico = 1. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kl17[number]`: Coefficiente di blocco del primo lead-lag in banda bassa (K).  Valore tipico = 1. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kl2[number]`: Guadagno del filtro differenziale a bassa banda (K).  Valore tipico = 66. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Riferimento Geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento.  - `omeganh1[number]`: Filtro notch 1 (banda ad alta frequenza): frequenza del filtro (omega). Predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `omeganh2[number]`: Filtro notch 2 (banda ad alta frequenza): frequenza del filtro (omega). Predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `omeganl1[number]`: Filtro notch 1 (banda a bassa frequenza): frequenza del filtro (omega). Predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `omeganl2[number]`: Filtro notch 2 (banda a bassa frequenza): frequenza del filtro (omega). Predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `th1[number]`: Costante di tempo della banda alta (T).  Valore tipico = 0,01513. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th10[number]`: Costante di tempo della banda alta (T).  Valore tipico = 0. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th11[number]`: Costante di tempo della banda alta (T).  Valore tipico = 0. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th12[number]`: Costante di tempo della banda alta (T).  Valore tipico = 0. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th2[number]`: Costante di tempo della banda alta (T).  Valore tipico = 0,01816. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th3[number]`: Costante di tempo della banda alta (T).  Valore tipico = 0. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th4[number]`: Costante di tempo della banda alta (T).  Valore tipico = 0. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th5[number]`: Costante di tempo della banda alta (T).  Valore tipico = 0. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th6[number]`: Costante di tempo della banda alta (T).  Valore tipico = 0. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th7[number]`: Costante di tempo della banda alta (T).  Valore tipico = 0,01816. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th8[number]`: Costante di tempo della banda alta (T).  Valore tipico = 0,02179. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th9[number]`: Costante di tempo della banda alta (T).  Valore tipico = 0. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti1[number]`: Costante di tempo della banda intermedia (T).  Valore tipico = 0,173. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti10[number]`: Costante di tempo della banda intermedia (T).  Valore tipico = 0. Predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti11[number]`: Costante di tempo della banda intermedia (T).  Valore tipico = 0. Predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti12[number]`: Costante di tempo della banda intermedia (T).  Valore tipico = 0. Predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti2[number]`: Costante di tempo della banda intermedia (T).  Valore tipico = 0,2075. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti3[number]`: Costante di tempo della banda intermedia (T).  Valore tipico = 0. Predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti4[number]`: Costante di tempo della banda intermedia (T).  Valore tipico = 0. Predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti5[number]`: Costante di tempo della banda intermedia (T).  Valore tipico = 0. Predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti6[number]`: Costante di tempo della banda intermedia (T).  Valore tipico = 0. Predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti7[number]`: Costante di tempo della banda intermedia (T).  Valore tipico = 0,2075. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti8[number]`: Costante di tempo della banda intermedia (T).  Valore tipico = 0,2491. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti9[number]`: Costante di tempo della banda intermedia (T).  Valore tipico = 0. Predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl1[number]`: Costante di tempo della banda bassa (T).  Valore tipico = 1,73. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl10[number]`: Costante di tempo della banda bassa (T).  Valore tipico = 0. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl11[number]`: Costante di tempo della banda bassa (T).  Valore tipico = 0. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl12[number]`: Costante di tempo della banda bassa (T).  Valore tipico = 0. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl2[number]`: Costante di tempo della banda bassa (T).  Valore tipico = 2,075. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl3[number]`: Costante di tempo della banda bassa (T).  Valore tipico = 0. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl4[number]`: Costante di tempo della banda bassa (T).  Valore tipico = 0. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl5[number]`: Costante di tempo della banda bassa (T).  Valore tipico = 0. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl6[number]`: Costante di tempo della banda bassa (T).  Valore tipico = 0. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl7[number]`: Costante di tempo della banda bassa (T).  Valore tipico = 2,075. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl8[number]`: Costante di tempo della banda bassa (T).  Valore tipico = 2,491. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl9[number]`: Costante di tempo della banda bassa (T).  Valore tipico = 0. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Tipo NGSI. Deve essere PssIEEE4B  - `vhmax[number]`: Limite massimo di uscita in banda alta (V).  Valore tipico = 0,6. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vhmin[number]`: Limite minimo di uscita in banda alta (V).  Valore tipico = -0,6. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vimax[number]`: Limite massimo di uscita della banda intermedia (V).  Valore tipico = 0,6. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vimin[number]`: Limite minimo di uscita della banda intermedia (V).  Valore tipico = -0,6. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vlmax[number]`: Limite massimo di uscita in banda bassa (V).  Valore tipico = 0,075. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vlmin[number]`: Limite minimo di uscita in banda bassa (V).  Valore tipico = -0,075. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vstmax[number]`: Limite massimo dell'uscita PSS (V).  Valore tipico = 0,15. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vstmin[number]`: Limite minimo dell'uscita PSS (V).  Valore tipico = -0,15. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
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
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
Non è disponibile l'esempio di un PssIEEE4B in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
Non è disponibile l'esempio di un PssIEEE4B in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
Non è disponibile l'esempio di un PssIEEE4B in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
Non è disponibile l'esempio di un PssIEEE4B in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
