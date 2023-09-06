<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: GovSteamEU  
===================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovSteamEU/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Adaptiert von CIM-Datenmodellen. Vereinfachtes Modell von Kessel und Dampfturbine mit PID-Regler**.  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.    
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `chc[number]`: Grenzwert für die Schließgeschwindigkeit der Steuerventile (Chc).  Einheit = VE/Sek.  Typischer Wert = -3,3. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `cho[number]`: Grenzwert für die Öffnungsrate der Steuerventile (Cho).  Einheit = VE/Sek.  Typischer Wert = 0,17. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `cic[number]`: Grenzwert für das Schließen des Abschnittsventils (Cic).  Typischer Wert = -2.2. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `cio[number]`: Grenzwert für die Öffnungsrate der Abfangventile (Cio).  Typischer Wert = 0,123. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `db1[number]`: Totzone des Frequenzumrichters (db1).  Typischer Wert = 0. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `db2[number]`: Totzone des Drehzahlreglers (db2).  Typischer Wert = 0,0004. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: Eine Beschreibung dieses Artikels  - `hhpmax[number]`: Maximale Regelventilstellung (Hhpmax).  Typischer Wert = 1. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Eindeutiger Bezeichner der Entität  - `ke[number]`: Verstärkung des Leistungsreglers (Ke).  Typischer Wert = 0,65. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kfcor[number]`: Verstärkung des Frequenzumrichters (Kfcor).  Typischer Wert = 20. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `khp[number]`: Anteil der vom HP-Teil erzeugten Gesamtleistung der Turbine (Khp).  Typischer Wert = 0,277. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `klp[number]`: Anteil der vom Hochdruckteil erzeugten Gesamtleistung der Turbine (Klp).  Typischer Wert = 0,723. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kwcor[number]`: Verstärkung des Drehzahlreglers (Kwcor).  Typischer Wert = 20. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `mwbase[number]`: Basis für Leistungswerte (MWbase) (>0).  Einheit = MW. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: Der Name dieses Artikels  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `pmax[number]`: Maximale Wirkleistung der Turbine (Pmax).  Typischer Wert = 1. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `prhmax[number]`: Maximale Niederdruckgrenze (Prhmax).  Typischer Wert = 1,4. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `simx[number]`: Abfangventil-Übertragungsgrenze (Simx).  Typischer Wert = 0,425. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der vollständig qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `tb[number]`: Zeitkonstante des Kessels (Tb).  Typischer Wert = 100. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tdp[number]`: Vorhaltezeitkonstante des Leistungsreglers (Tdp).  Typischer Wert = 0. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ten[number]`: Elektrohydraulischer Messumformer (Ten).  Typischer Wert = 0,1. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tf[number]`: Zeitkonstante des Frequenzumwandlers (Tf).  Typischer Wert = 0. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tfp[number]`: Zeitkonstante des Leistungsreglers (Tfp).  Typischer Wert = 0. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `thp[number]`: Hochdruck-Zeitkonstante (HP) der Turbine (Thp).  Typischer Wert = 0,31. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tip[number]`: Integrale Zeitkonstante des Leistungsreglers (Tip).  Typischer Wert = 2. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tlp[number]`: Niederdruck(ND)-Zeitkonstante der Turbine (Tlp).  Typischer Wert = 0,45. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tp[number]`: Zeitkonstante des Energiewandlers (Tp).  Typischer Wert = 0,07. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `trh[number]`: Wiedererwärmungszeitkonstante der Turbine (Trh).  Typischer Wert = 8. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tvhp[number]`: Servo-Zeitkonstante der Steuerventile (Tvhp).  Typischer Wert = 0,1. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tvip[number]`: Intercept Ventile Servo Zeitkonstante (Tvip).  Typischer Wert = 0,15. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw[number]`: Zeitkonstante des Geschwindigkeitsaufnehmers (Tw).  Typischer Wert = 0,02. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI-Typ. Es muss GovSteamEU sein  - `wfmax[number]`: Obere Grenze für die Frequenzkorrektur (Wfmax).  Typischer Wert = 0,05. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `wfmin[number]`: Unterer Grenzwert für die Frequenzkorrektur (Wfmin).  Typischer Wert = -0,05. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `wmax1[number]`: Untere Grenze der Notlaufregelung (wmax1).  Typischer Wert = 1,025. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `wmax2[number]`: Obere Grenze der Notlaufregelung (wmax2).  Typischer Wert = 1,05. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `wwmax[number]`: Oberer Grenzwert für den Drehzahlregler (Wwmax).  Typischer Wert = 0,1. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `wwmin[number]`: Unterer Grenzwert für die Frequenzkorrektur des Drehzahlreglers (Wwmin).  Typischer Wert = -1. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
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
GovSteamEU:    
  description: Adapted from CIM data models. Simplified model  of boiler and steam turbine with PID governor.    
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
    chc:    
      description: 'Control valves rate closing limit (Chc).  Unit = PU/sec.  Typical Value = -3.3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    cho:    
      description: 'Control valves rate opening limit (Cho).  Unit = PU/sec.  Typical Value = 0.17. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    cic:    
      description: 'Intercept valves rate closing limit (Cic).  Typical Value = -2.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    cio:    
      description: 'Intercept valves rate opening limit (Cio).  Typical Value = 0.123. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    db1:    
      description: 'Dead band of the frequency corrector (db1).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    db2:    
      description: 'Dead band of the speed governor (db2).  Typical Value = 0.0004. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    hhpmax:    
      description: 'Maximum control valve position (Hhpmax).  Typical Value = 1. Default: 0.0'    
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
    ke:    
      description: 'Gain of the power controller (Ke).  Typical Value = 0.65. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kfcor:    
      description: 'Gain of the frequency corrector (Kfcor).  Typical Value = 20. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    khp:    
      description: 'Fraction of total turbine output generated by HP part (Khp).  Typical Value = 0.277. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    klp:    
      description: 'Fraction of total turbine output generated by HP part (Klp).  Typical Value = 0.723. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kwcor:    
      description: 'Gain of the speed governor (Kwcor).  Typical Value = 20. Default: 0.0'    
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
    pmax:    
      description: 'Maximal active power of the turbine (Pmax).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    prhmax:    
      description: 'Maximum low pressure limit (Prhmax).  Typical Value = 1.4. Default: 0.0'    
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
    simx:    
      description: 'Intercept valves transfer limit (Simx).  Typical Value = 0.425. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    tb:    
      description: 'Boiler time constant (Tb).  Typical Value = 100. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tdp:    
      description: 'Derivative time constant of the power controller (Tdp).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ten:    
      description: 'Electro hydraulic transducer (Ten).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tf:    
      description: 'Frequency transducer time constant (Tf).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tfp:    
      description: 'Time constant of the power controller (Tfp).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    thp:    
      description: 'High pressure (HP) time constant of the turbine (Thp).  Typical Value = 0.31. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tip:    
      description: 'Integral time constant of the power controller (Tip).  Typical Value = 2. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tlp:    
      description: 'Low pressure(LP) time constant of the turbine (Tlp).  Typical Value = 0.45. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tp:    
      description: 'Power transducer time constant (Tp).  Typical Value = 0.07. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    trh:    
      description: 'Reheater  time constant of the turbine (Trh).  Typical Value = 8. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tvhp:    
      description: 'Control valves servo time constant (Tvhp).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tvip:    
      description: 'Intercept valves servo time constant (Tvip).  Typical Value = 0.15. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tw:    
      description: 'Speed transducer time constant (Tw).  Typical Value = 0.02. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: NGSI type. It has to be GovSteamEU    
      enum:    
        - GovSteamEU    
      type: string    
      x-ngsi:    
        type: Property    
    wfmax:    
      description: 'Upper limit for frequency correction (Wfmax).  Typical Value = 0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    wfmin:    
      description: 'Lower limit for frequency correction (Wfmin).  Typical Value = -0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    wmax1:    
      description: 'Emergency speed control lower limit (wmax1).  Typical Value = 1.025. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    wmax2:    
      description: 'Emergency speed control upper limit (wmax2).  Typical Value = 1.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    wwmax:    
      description: 'Upper limit for the speed governor (Wwmax).  Typical Value = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    wwmin:    
      description: 'Lower limit for the speed governor frequency correction (Wwmin).  Typical Value = -1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovSteamEU/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/GovSteamEU/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
Nicht verfügbar ist das Beispiel einer GovSteamEU im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar ist das Beispiel einer GovSteamEU im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar ist das Beispiel einer GovSteamEU im JSON-LD Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar ist das Beispiel einer GovSteamEU im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
