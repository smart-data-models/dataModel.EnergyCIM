<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: ExcREXS  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExcREXS/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Adattato dai modelli di dati CIM. Modello di sistema di eccitazione rotante di uso generale.  Questo modello può essere utilizzato per rappresentare un'ampia gamma di sistemi di eccitazione la cui fonte di alimentazione CC è un generatore CA o CC. Comprende i modelli di sistemi di eccitazione di tipo IEEE AC1, AC2, DC1 e DC2.  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated[string]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateModified[string]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `description[string]`: Descrizione dell'articolo  - `e1[number]`: Valore della tensione di campo 1 (E1).  Valore tipico = 3. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `e2[number]`: Valore della tensione di campo 2 (E2).  Valore tipico = 4. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fbf[number]`: Flag del segnale di retroazione della velocità (Fbf). Valore tipico = fieldCurrent. Predefinito: Nessuno  . Model: [https://schema.org/Number](https://schema.org/Number)- `flimf[number]`: Flag del tipo di limite (Flimf).  Valore tipico = 0. Predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identificatore univoco dell'entità  - `kc[number]`: Fattore di regolazione del raddrizzatore (Kc).  Valore tipico = 0,05. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kd[number]`: Fattore di regolazione dell'eccitatore (Kd).  Valore tipico = 2. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ke[number]`: Costante proporzionale di campo dell'eccitatore (Ke).  Valore tipico = 1. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kefd[number]`: Guadagno di retroazione della tensione di campo (Kefd).  Valore tipico = 0. Default: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kf[number]`: Guadagno di retroazione della velocità (Kf).  Valore tipico = 0,05. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kh[number]`: Guadagno di feedback del regolatore di tensione di campo (Kh).  Valore tipico = 0. Default: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kii[number]`: Guadagno integrale del regolatore di corrente di campo (Kii).  Valore tipico = 0. Predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kip[number]`: Guadagno proporzionale del regolatore di corrente di campo (Kip).  Valore tipico = 1. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ks[number]`: Coefficiente per consentire un uso diverso del coefficiente di velocità del modello (Ks).  Valore tipico = 0. Predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kvi[number]`: Guadagno integrale del regolatore di tensione (Kvi).  Valore tipico = 0. Predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kvp[number]`: Guadagno proporzionale del regolatore di tensione (Kvp).  Valore tipico = 2800. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kvphz[number]`: Guadagno del limitatore V/Hz (Kvphz).  Valore tipico = 0. Predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Riferimento Geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento.  - `nvphz[number]`: Velocità di pickup del limitatore V/Hz (Nvphz).  Valore tipico = 0. Predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `se1[number]`: Fattore di saturazione a E1 (Se1).  Valore tipico = 0,0001. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `se2[number]`: Fattore di saturazione a E2 (Se2).  Valore tipico = 0,001. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `ta[number]`: Costante di tempo del regolatore di tensione (Ta).  Valore tipico = 0,01. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tb1[number]`: Costante di tempo di ritardo (Tb1).  Valore tipico = 0. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tb2[number]`: Costante di tempo di ritardo (Tb2).  Valore tipico = 0. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tc1[number]`: Costante del tempo di esecuzione (Tc1).  Valore tipico = 0. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tc2[number]`: Costante del tempo di esecuzione (Tc2).  Valore tipico = 0. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `te[number]`: Costante di tempo del campo dell'eccitatore (Te).  Valore tipico = 1,2. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tf[number]`: Costante di tempo di retroazione della velocità (Tf).  Valore tipico = 1. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tf1[number]`: Costante di tempo di retroazione (Tf1).  Valore tipico = 0. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tf2[number]`: Costante di tempo di ritardo della retroazione (Tf2).  Valore tipico = 0. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tp[number]`: Costante di tempo del ponte della corrente di campo (Tp).  Valore tipico = 0. Valore predefinito: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Tipo NGSI. Deve essere ExcREXS  - `vcmax[number]`: Tensione massima di compoundazione (Vcmax).  Valore tipico = 0. Predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vfmax[number]`: Corrente massima di campo dell'eccitatore (Vfmax).  Valore tipico = 47. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vfmin[number]`: Corrente minima di campo dell'eccitatore (Vfmin).  Valore tipico = -20. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vimax[number]`: Limite di ingresso del regolatore di tensione (Vimax).  Valore tipico = 0,1. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vrmax[number]`: Uscita massima del regolatore (Vrmax).  Valore tipico = 47. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vrmin[number]`: Uscita minima del controllore (Vrmin).  Valore tipico = -20. Valore predefinito: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `xc[number]`: Reattanza di composizione dell'eccitatore (Xc).  Valore tipico = 0. Default: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
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
ExcREXS:    
  description: 'Adapted from CIM data models. General Purpose Rotating Excitation System Model.  This model can be used to represent a wide range of excitation systems whose DC power source is an AC or DC generator. It encompasses IEEE type AC1, AC2, DC1, and DC2 excitation system models.'    
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
    e1:    
      description: 'Field voltage value 1 (E1).  Typical Value = 3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    e2:    
      description: 'Field voltage value 2 (E2).  Typical Value = 4. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fbf:    
      description: 'Rate feedback signal flag (Fbf). Typical Value = fieldCurrent. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    flimf:    
      description: 'Limit type flag (Flimf).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &excrexs_-_properties_-_owner_-_items_-_anyof    
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
    kc:    
      description: 'Rectifier regulation factor (Kc).  Typical Value = 0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kd:    
      description: 'Exciter regulation factor (Kd).  Typical Value = 2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ke:    
      description: 'Exciter field proportional constant (Ke).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kefd:    
      description: 'Field voltage feedback gain (Kefd).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kf:    
      description: 'Rate feedback gain (Kf).  Typical Value = 0.05. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kh:    
      description: 'Field voltage controller feedback gain (Kh).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kii:    
      description: 'Field Current Regulator Integral Gain (Kii).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kip:    
      description: 'Field Current Regulator Proportional Gain (Kip).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ks:    
      description: 'Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kvi:    
      description: 'Voltage Regulator Integral Gain (Kvi).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kvp:    
      description: 'Voltage Regulator Proportional Gain (Kvp).  Typical Value = 2800. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kvphz:    
      description: 'V/Hz limiter gain (Kvphz).  Typical Value = 0. Default: 0.0'    
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
    nvphz:    
      description: 'Pickup speed of V/Hz limiter (Nvphz).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *excrexs_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    se1:    
      description: 'Saturation factor at E1 (Se1).  Typical Value = 0.0001. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    se2:    
      description: 'Saturation factor at E2 (Se2).  Typical Value = 0.001. Default: 0.0'    
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
    ta:    
      description: 'Voltage Regulator time constant (Ta).  Typical Value = 0.01. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tb1:    
      description: 'Lag time constant (Tb1).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tb2:    
      description: 'Lag time constant (Tb2).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tc1:    
      description: 'Lead time constant (Tc1).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tc2:    
      description: 'Lead time constant (Tc2).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    te:    
      description: 'Exciter field time constant (Te).  Typical Value = 1.2. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tf:    
      description: 'Rate feedback time constant (Tf).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tf1:    
      description: 'Feedback lead time constant (Tf1).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tf2:    
      description: 'Feedback lag time constant (Tf2).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tp:    
      description: 'Field current Bridge time constant (Tp).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be ExcREXS'    
      enum:    
        - ExcREXS    
      type: string    
      x-ngsi:    
        type: Property    
    vcmax:    
      description: 'Maximum compounding voltage (Vcmax).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vfmax:    
      description: 'Maximum Exciter Field Current (Vfmax).  Typical Value = 47. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vfmin:    
      description: 'Minimum Exciter Field Current (Vfmin).  Typical Value = -20. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vimax:    
      description: 'Voltage Regulator Input Limit (Vimax).  Typical Value = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vrmax:    
      description: 'Maximum controller output (Vrmax).  Typical Value = 47. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vrmin:    
      description: 'Minimum controller output (Vrmin).  Typical Value = -20. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    xc:    
      description: 'Exciter compounding reactance (Xc).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcREXS/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/ExcREXS/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
Non è disponibile l'esempio di un ExcREXS in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
Non è disponibile l'esempio di un ExcREXS in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
Non è disponibile l'esempio di un ExcREXS in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
Non è disponibile l'esempio di un ExcREXS in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
