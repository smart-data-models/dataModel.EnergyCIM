<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: GovHydroWPID  
=====================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovHydroWPID/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Angelehnt an die CIM-Datenmodelle. Woodward PID Hydro Governor.**  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `d[number]`: Dämpfungsfaktor der Turbine (D).  Einheit = delta P / delta Geschwindigkeit. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated[string]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified[string]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description[string]`: Eine Beschreibung dieses Artikels  - `gatmax[number]`: Grenzwert für die maximale Toröffnung (Gatmax). Standard: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gatmin[number]`: Toröffnungsgrenze Minimum (Gatmin). Standard: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv1[number]`: Torstellung 1 (Gv1). Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv2[number]`: Torstellung 2 (Gv2). Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv3[number]`: Torstellung 3 (Gv3). Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Eindeutiger Bezeichner der Entität  - `kd[number]`: Ableitungsverstärkung (Kd).  Typischer Wert = 1,11. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ki[number]`: Rückstellverstärkung (Ki).  Typischer Wert = 0,36. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kp[number]`: Proportionalverstärkung (Kp).  Typischer Wert = 0,1. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `mwbase[number]`: Basis für Leistungswerte (MWbase) (>0).  Einheit = MW. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: Der Name dieses Artikels.  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `pgv1[number]`: Ausgang an Gv1 PU der MW-Basis (Pgv1). Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pgv2[number]`: Ausgang an Gv2 PU der MW-Basis (Pgv2). Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pgv3[number]`: Ausgang an Gv3 PU der MWbase (Pgv3). Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmax[number]`: Maximale Ausgangsleistung (Pmax). Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmin[number]`: Minimale Ausgangsleistung (Pmin). Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `reg[number]`: Permanenter Abfall (Reg). Standardwert: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den voll qualifizierten Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden.  - `ta[number]`: Zeitkonstante des Reglers (Ta) (>0).  Typischer Wert = 0. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tb[number]`: Gate-Servo-Zeitkonstante (Tb) (>0).  Typischer Wert = 0. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `treg[number]`: Zeitkonstante des Geschwindigkeitsdetektors (Treg). Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw[number]`: Wasserträgheitszeitkonstante (Tw) (>0).  Typischer Wert = 0. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI-Typ. Es muss GovHydroWPID sein.  - `velmax[number]`: Maximale Öffnungsgeschwindigkeit des Tores (Velmax).  Einheit = PU/sec.  Typischer Wert = 0. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `velmin[number]`: Maximale Schließgeschwindigkeit des Tores (Velmin).  Einheit = PU/sec.  Typischer Wert = 0. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
<!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Angepasst von CIM-Datenmodellen und CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Dieses Datenmodell ist eine direkte Umsetzung des Common Information Model (CIM), das durch die Norm IEC61970 spezifiziert ist, in intelligente Datenmodelle. Die Python-Klassen, auf denen dieses Modell basiert, wurden vom Institut für Automatisierung komplexer Stromversorgungssysteme (ACS), dem EON Energy Research Center (EONERC) und der RWTH Aachen, Deutschland, entwickelt. Einige Eigenschaften können den falschen Typ haben. Sollte dies der Fall sein, melden Sie bitte einen Fehler oder senden Sie eine E-Mail an info@smartdatamodels.org.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GovHydroWPID:    
  description: 'Adapted from CIM data models. Woodward PID Hydro Governor.'    
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
    d:    
      description: 'Turbine damping factor (D).  Unit = delta P / delta speed. Default: 0.0'    
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
    gatmax:    
      description: 'Gate opening Limit Maximum (Gatmax). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gatmin:    
      description: 'Gate opening Limit Minimum (Gatmin). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv1:    
      description: 'Gate position 1 (Gv1). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv2:    
      description: 'Gate position 2 (Gv2). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv3:    
      description: 'Gate position 3 (Gv3). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &govhydrowpid_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Derivative gain (Kd).  Typical Value = 1.11. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ki:    
      description: 'Reset gain (Ki).  Typical Value = 0.36. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kp:    
      description: 'Proportional gain (Kp).  Typical Value = 0.1. Default: 0.0'    
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
      description: 'Base for power values  (MWbase) (>0).  Unit = MW. Default: 0.0'    
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
        anyOf: *govhydrowpid_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    pgv1:    
      description: 'Output at Gv1 PU of MWbase (Pgv1). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pgv2:    
      description: 'Output at Gv2 PU of MWbase (Pgv2). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pgv3:    
      description: 'Output at Gv3 PU of MWbase (Pgv3). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmax:    
      description: 'Maximum Power Output (Pmax). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmin:    
      description: 'Minimum Power Output (Pmin). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    reg:    
      description: 'Permanent drop (Reg). Default: 0.0'    
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
      description: 'Controller time constant (Ta) (>0).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tb:    
      description: 'Gate servo time constant (Tb) (>0).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    treg:    
      description: 'Speed detector time constant (Treg). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tw:    
      description: 'Water inertia time constant (Tw) (>0).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be GovHydroWPID'    
      enum:    
        - GovHydroWPID    
      type: string    
      x-ngsi:    
        type: Property    
    velmax:    
      description: 'Maximum gate opening velocity (Velmax).  Unit = PU/sec.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    velmin:    
      description: 'Maximum gate closing velocity (Velmin).  Unit = PU/sec.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovHydroWPID/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/GovHydroWPID/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
Nicht verfügbar ist das Beispiel einer GovHydroWPID im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar ist das Beispiel einer GovHydroWPID im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar ist das Beispiel einer GovHydroWPID im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar ist das Beispiel einer GovHydroWPID im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
