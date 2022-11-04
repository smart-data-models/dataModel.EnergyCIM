<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: GovGASTWD  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovGASTWD/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Angelehnt an die CIM-Datenmodelle. Woodward Gasturbinenregler-Modell.**  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `a[number]`: Ventil-Stellungsregler (). Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)- `af1[number]`: Abgastemperatur Parameter (Af1). Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `af2[number]`: Koeffizient gleich 0,5 (1 Geschwindigkeit) (Af2). Standardwert: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `b[number]`: Ventil-Stellungsregler (). Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bf1[number]`: (Bf1).  Bf1 = E(1-w), wobei E (Geschwindigkeitsempfindlichkeitskoeffizient) 0,55 bis 0,65 x Tr beträgt. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bf2[number]`: Turbinendrehmomentkoeffizient K (hängt vom Heizwert des Brennstoffstroms in der Brennkammer ab) (Bf2). Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `c[number]`: Ventil-Stellungsregler (). Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `cf2[number]`: Koeffizient, der den Kraftstofffluss bei einer Leistung von 0 % definiert (Cf2).  Synchron, aber keine Leistung.  Normalerweise 0,23 x K(23% Brennstoffdurchsatz). Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated[string]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified[string]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description[string]`: Eine Beschreibung dieses Artikels  - `ecr[number]`: Verzögerung der Verbrennungsreaktion (Ecr). Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `etd[number]`: Turbinen- und Abgasverzögerung (Etd). Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Eindeutiger Bezeichner der Entität  - `k3[number]`: Verhältnis der Kraftstoffanpassung (K3). Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `k4[number]`: Verstärkung des Strahlungsschutzes (K4). Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `k5[number]`: Verstärkung des Strahlungsschutzes (K5). Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `k6[number]`: Minimaler Kraftstoffdurchfluss (K6). Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kd[number]`: Verstärkung des Tropfenreglers (Kd). Standard: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kdroop[number]`: (Kdroop). Standardwert: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kf[number]`: Rückmeldung des Kraftstoffsystems (Kf). Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ki[number]`: Isochrone Reglerverstärkung (Ki). Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kp[number]`: PID-Proportionalverstärkung (Kp). Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `mwbase[number]`: Basis für Leistungswerte (MWbase) (> 0).  Einheit = MW. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: Der Name dieses Artikels.  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den voll qualifizierten Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden.  - `t[number]`: Zeitkonstante der Kraftstoffregelung (T). Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t3[number]`: Zeitkonstante des Strahlenschutzes (T3). Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t4[number]`: Thermoelement-Zeitkonstante (T4). Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `t5[number]`: Zeitkonstante der Temperaturregelung (T5). Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tc[number]`: Temperaturregelung (Tc). Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tcd[number]`: Zeitkonstante der Verdichterentladung (Tcd). Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `td[number]`: Zeitkonstante des Energiewandlers (Td). Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tf[number]`: Zeitkonstante des Kraftstoffsystems (Tf). Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tmax[number]`: Maximaler Turbinengrenzwert (Tmax). Standardwert: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tmin[number]`: Minimaler Turbinengrenzwert (Tmin). Standardwert: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tr[number]`: Nenntemperatur (Tr). Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `trate[number]`: Turbinenleistung (Trate).  Einheit = MW. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tt[number]`: Integrationsrate des Temperaturreglers (Tt). Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI-Typ. Es muss GovGASTWD sein.  <!-- /30-PropertiesList -->  
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
GovGASTWD:    
  description: 'Adapted from CIM data models. Woodward Gas turbine governor model.'    
  properties:    
    a:    
      description: 'Valve positioner (). Default: 0.0'    
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
      description: 'Exhaust temperature Parameter (Af1). Default: 0.0'    
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
      description: 'Valve positioner (). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bf1:    
      description: '(Bf1).  Bf1 = E(1-w) where E (speed sensitivity coefficient) is 0.55 to 0.65 x Tr. Default: 0.0'    
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
      description: 'Valve positioner (). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    cf2:    
      description: 'Coefficient defining fuel flow where power output is 0% (Cf2).  Synchronous but no output.  Typically 0.23 x K(23% fuel flow). Default: 0.0'    
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
      anyOf: &govgastwd_-_properties_-_owner_-_items_-_anyof    
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
    kd:    
      description: 'Drop Governor Gain (Kd). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kdroop:    
      description: '(Kdroop). Default: 0.0'    
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
    ki:    
      description: 'Isochronous Governor Gain (Ki). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kp:    
      description: 'PID Proportional gain (Kp). Default: 0.0'    
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
        anyOf: *govgastwd_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Temperature control (Tc). Default: 0.0'    
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
    td:    
      description: 'Power transducer time constant (Td). Default: 0'    
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
      description: 'Rated temperature (Tr). Default: 0.0'    
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
      description: 'NGSI type. It has to be GovGASTWD'    
      enum:    
        - GovGASTWD    
      type: string    
      x-ngsi:    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovGASTWD/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/GovGASTWD/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
Nicht verfügbar ist das Beispiel eines GovGASTWD im JSON-LD Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar ist das Beispiel eines GovGASTWD im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar ist das Beispiel eines GovGASTWD im JSON-LD Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar ist das Beispiel eines GovGASTWD im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
