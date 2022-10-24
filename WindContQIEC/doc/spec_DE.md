<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: WindContQIEC  
=====================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/WindContQIEC/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Abgeleitet von CIM-Datenmodellen. Q-Kontrollmodell.  Referenz: IEC-Norm 61400-27-1 Abschnitt 6.6.5.6.**  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, liegt das daran, dass es mehrere Typen oder unterschiedliche Formate/Muster haben kann</sub></sup>.  
- `WindTurbineType3or4IEC[number]`: Modell der Windkraftanlage des Typs 3 oder 4, dem dieser Blindleistungsregelungsmodus zugeordnet ist. Voreinstellung: Keine  . Model: [https://schema.org/Number](https://schema.org/Number)- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated[string]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified[string]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description[string]`: Eine Beschreibung dieses Artikels  - `id[*]`: Eindeutiger Bezeichner der Entität  - `iqh1[number]`: Maximale Blindstromeinspeisung während des Eintauchens (i). Es handelt sich um einen typabhängigen Parameter. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `iqmax[number]`: Maximale Blindstromeinspeisung (i). Es handelt sich um einen typabhängigen Parameter. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `iqmin[number]`: Mindestblindstromeinspeisung (i). Es handelt sich um einen typabhängigen Parameter. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `iqpost[number]`: Blindstromeinspeisung nach einem Fehler (). Es handelt sich um einen projektabhängigen Parameter. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kiq[number]`: Integrationsverstärkung des PI-Reglers für die Blindleistung (). Es handelt sich um einen typabhängigen Parameter. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kiu[number]`: Integrationsverstärkung des Spannungs-PI-Reglers (). Es ist ein typabhängiger Parameter. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kpq[number]`: Proportionale Verstärkung des PI-Reglers für die Blindleistung (). Es handelt sich um einen typabhängigen Parameter. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kpu[number]`: Proportionalverstärkung des Spannungs-PI-Reglers (). Es handelt sich um einen typabhängigen Parameter. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kqv[number]`: Spannungsskalierungsfaktor für LVRT-Strom (). Dies ist ein projektabhängiger Parameter. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels.  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `qmax[number]`: Maximale Blindleistung (q). Es ist ein typabhängiger Parameter. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `qmin[number]`: Mindestblindleistung (q). Es ist ein typabhängiger Parameter. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rdroop[number]`: Resistive Komponente der Spannungsabfallimpedanz (). Dies ist ein projektabhängiger Parameter. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `tiq[number]`: Zeitkonstante der Blindstromverzögerung (T). Es handelt sich um einen typabhängigen Parameter. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tpfilt[number]`: Zeitkonstante des Leistungsmessungsfilters (). Es handelt sich um einen typabhängigen Parameter. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tpost[number]`: Länge des Zeitraums, in dem Nachfehlerblindleistung eingespeist wird (). Dies ist ein projektabhängiger Parameter. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tqord[number]`: Zeitkonstante für die Verzögerung der Blindleistungsordnung (). Es handelt sich um einen typabhängigen Parameter. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tufilt[number]`: Zeitkonstante des Spannungsmessungsfilters (). Es handelt sich um einen typabhängigen Parameter. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI-Typ. Es muss WindContQIEC sein.  - `udb1[number]`: Untere Grenze der Spannungs-Totzone (). Es handelt sich um einen typabhängigen Parameter. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `udb2[number]`: Obere Grenze der Spannungs-Totzone (). Es handelt sich um einen typabhängigen Parameter. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `umax[number]`: Maximale Spannung im Integralanteil des Spannungs-PI-Reglers (u). Es ist ein typabhängiger Parameter. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `umin[number]`: Minimale Spannung im Integralanteil des Spannungs-PI-Reglers (u). Es ist ein typabhängiger Parameter. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `uqdip[number]`: Spannungsschwelle für die LVRT-Erkennung in der q-Steuerung (). Es handelt sich um einen typabhängigen Parameter. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `uref0[number]`: Benutzerdefinierte Vorspannung in der Spannungsreferenz (), die verwendet wird, wenn =. Es ist ein fallabhängiger Parameter. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `windLVRTQcontrolModesType[number]`: Arten von LVRT Q-Steuerungsmodi (). Dies ist ein projektabhängiger Parameter. Voreinstellung: Keine  . Model: [https://schema.org/Number](https://schema.org/Number)- `windQcontrolModesType[number]`: Arten der allgemeinen Q-Steuerungsmodi von Windkraftanlagen ().  Dies ist ein projektabhängiger Parameter. Voreinstellung: Keine  . Model: [https://schema.org/Number](https://schema.org/Number)- `xdroop[number]`: Induktive Komponente der Spannungsabfall-Impedanz (). Dieser Parameter ist projektabhängig. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
<!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Angepasst von CIM-Datenmodellen und CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Dieses Datenmodell ist eine direkte Umsetzung des Common Information Model (CIM), das durch die Norm IEC61970 spezifiziert ist, in intelligente Datenmodelle. Die Python-Klassen, auf denen dieses Modell basiert, wurden vom Institut für Automatisierung komplexer Stromversorgungssysteme (ACS), dem EON Energy Research Center (EONERC) und der RWTH Aachen, Deutschland, entwickelt. Einige Eigenschaften können einen falschen Typ haben. Sollte dies der Fall sein, melden Sie bitte einen Fehler oder senden Sie eine E-Mail an info@smartdatamodels.org.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
Nicht verfügbar ist das Beispiel einer WindContQIEC im JSON-LD Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar ist das Beispiel einer WindContQIEC im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar ist das Beispiel einer WindContQIEC im JSON-LD Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar ist das Beispiel einer WindContQIEC im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
