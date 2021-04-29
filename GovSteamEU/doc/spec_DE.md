Entität: GovSteamEU  
===================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovSteamEU/LICENSE.md)  
Globale Beschreibung: **Abgeleitet aus CIM-Datenmodellen. Vereinfachtes Modell von Kessel und Dampfturbine mit PID-Regler.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `chc`: Grenzwert für die Schließgeschwindigkeit der Regelventile (Chc).  Einheit = VE/sec.  Typischer Wert = -3,3. Voreinstellung: 0,0  - `cho`: Grenzwert für die Öffnungsrate der Regelventile (Cho).  Einheit = VE/sec.  Typischer Wert = 0,17. Voreinstellung: 0,0  - `cic`: Intercept Ventile Rate Schließgrenze (Cic).  Typischer Wert = -2,2. Voreinstellung: 0,0  - `cio`: Intercept Ventile Rate Öffnungsgrenze (Cio).  Typischer Wert = 0,123. Voreinstellung: 0.0  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `db1`: Totzone des Frequenzumrichters (db1).  Typischer Wert = 0. Voreinstellung: 0.0  - `db2`: Totzone des Drehzahlreglers (db2).  Typischer Wert = 0,0004. Voreinstellung: 0,0  - `description`: Eine Beschreibung dieses Artikels  - `hhpmax`: Maximale Regelventilposition (Hhpmax).  Typischer Wert = 1. Voreinstellung: 0.0  - `id`: Eindeutiger Bezeichner der Entität  - `ke`: Verstärkung des Leistungsreglers (Ke).  Typischer Wert = 0,65. Voreinstellung: 0,0  - `kfcor`: Verstärkung des Frequenzumrichters (Kfcor).  Typischer Wert = 20. Voreinstellung: 0.0  - `khp`: Anteil der vom HP-Teil erzeugten Gesamtleistung der Turbine (Khp).  Typischer Wert = 0,277. Voreinstellung: 0.0  - `klp`: Anteil der vom HD-Teil erzeugten Gesamtleistung der Turbine (Klp).  Typischer Wert = 0,723. Voreinstellung: 0,0  - `kwcor`: Verstärkung des Drehzahlreglers (Kwcor).  Typischer Wert = 20. Voreinstellung: 0.0  - `location`:   - `mwbase`: Basis für Leistungswerte (MWbase) (>0).  Einheit = MW. Voreinstellung: 0,0  - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `pmax`: Maximale Wirkleistung der Turbine (Pmax).  Typischer Wert = 1. Voreinstellung: 0.0  - `prhmax`: Maximale Niederdruckgrenze (Prhmax).  Typischer Wert = 1,4. Voreinstellung: 0,0  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `simx`: Intercept Ventile Übertragungsgrenze (Simx).  Typischer Wert = 0,425. Voreinstellung: 0,0  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `tb`: Kesselzeitkonstante (Tb).  Typischer Wert = 100. Voreinstellung: 0  - `tdp`: Vorhaltezeitkonstante des Leistungsreglers (Tdp).  Typischer Wert = 0. Voreinstellung: 0  - `ten`: Elektrohydraulischer Messumformer (Ten).  Typischer Wert = 0,1. Voreinstellung: 0  - `tf`: Zeitkonstante des Frequenzumwandlers (Tf).  Typischer Wert = 0. Voreinstellung: 0  - `tfp`: Zeitkonstante des Leistungsreglers (Tfp).  Typischer Wert = 0. Voreinstellung: 0  - `thp`: Hochdruck (HP) Zeitkonstante der Turbine (Thp).  Typischer Wert = 0,31. Voreinstellung: 0  - `tip`: Integrale Zeitkonstante des Leistungsreglers (Tip).  Typischer Wert = 2. Voreinstellung: 0  - `tlp`: Niederdruck(ND)-Zeitkonstante der Turbine (Tlp).  Typischer Wert = 0,45. Voreinstellung: 0  - `tp`: Zeitkonstante des Leistungsmesswandlers (Tp).  Typischer Wert = 0,07. Voreinstellung: 0  - `trh`: Nachheizzeitkonstante der Turbine (Trh).  Typischer Wert = 8. Voreinstellung: 0  - `tvhp`: Regelventile Servo-Zeitkonstante (Tvhp).  Typischer Wert = 0,1. Voreinstellung: 0  - `tvip`: Intercept Ventile Servo-Zeitkonstante (Tvip).  Typischer Wert = 0,15. Voreinstellung: 0  - `tw`: Zeitkonstante des Geschwindigkeitsaufnehmers (Tw).  Typischer Wert = 0,02. Voreinstellung: 0  - `type`: NGSI-Typ. Es muss GovSteamEU sein  - `wfmax`: Obere Grenze für die Frequenzkorrektur (Wfmax).  Typischer Wert = 0,05. Voreinstellung: 0,0  - `wfmin`: Untere Grenze für die Frequenzkorrektur (Wfmin).  Typischer Wert = -0,05. Voreinstellung: 0,0  - `wmax1`: Untere Grenze der Notdrehzahlregelung (wmax1).  Typischer Wert = 1,025. Voreinstellung: 0,0  - `wmax2`: Obere Grenze der Notdrehzahlregelung (wmax2).  Typischer Wert = 1,05. Voreinstellung: 0,0  - `wwmax`: Obere Grenze für den Drehzahlregler (Wwmax).  Typischer Wert = 0,1. Voreinstellung: 0,0  - `wwmin`: Unterer Grenzwert für die Frequenzkorrektur des Drehzahlreglers (Wwmin).  Typischer Wert = -1. Voreinstellung: 0.0    
Erforderliche Eigenschaften  
Dieses Datenmodell ist eine direkte Umsetzung des Common Information Model (CIM), das durch die Norm IEC61970 spezifiziert ist, in Smart Data Models. Die Python-Klassen, auf denen dieses Modell basiert, wurden von diesen Einrichtungen entwickelt Institut für Automatisierung komplexer Stromversorgungssysteme (ACS), EON Energy Research Center (EONERC) und RWTH Aachen, Deutschland. einige Eigenschaften können einen falschen Typ haben. Dies war der Fall, bitte melden Sie einen Fehler oder senden Sie eine E-Mail an alberto.abella@fiware.org  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GovSteamEU:    
  description: 'Adapted from CIM data models. Simplified model  of boiler and steam turbine with PID governor.'    
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
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/areaServed'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    chc:    
      description: 'Control valves rate closing limit (Chc).  Unit = PU/sec.  Typical Value = -3.3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    cho:    
      description: 'Control valves rate opening limit (Cho).  Unit = PU/sec.  Typical Value = 0.17. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    cic:    
      description: 'Intercept valves rate closing limit (Cic).  Typical Value = -2.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    cio:    
      description: 'Intercept valves rate opening limit (Cio).  Typical Value = 0.123. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    db1:    
      description: 'Dead band of the frequency corrector (db1).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    db2:    
      description: 'Dead band of the speed governor (db2).  Typical Value = 0.0004. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    description:    
      description: 'A description of this item'    
      type: Property    
    hhpmax:    
      description: 'Maximum control valve position (Hhpmax).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &govsteameu_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      type: Property    
    ke:    
      description: 'Gain of the power controller (Ke).  Typical Value = 0.65. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kfcor:    
      description: 'Gain of the frequency corrector (Kfcor).  Typical Value = 20. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    khp:    
      description: 'Fraction of total turbine output generated by HP part (Khp).  Typical Value = 0.277. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    klp:    
      description: 'Fraction of total turbine output generated by HP part (Klp).  Typical Value = 0.723. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kwcor:    
      description: 'Gain of the speed governor (Kwcor).  Typical Value = 20. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
      title: 'GeoJSON Geometry'    
    mwbase:    
      description: 'Base for power values (MWbase) (>0).  Unit = MW. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *govsteameu_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    pmax:    
      description: 'Maximal active power of the turbine (Pmax).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    prhmax:    
      description: 'Maximum low pressure limit (Prhmax).  Typical Value = 1.4. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    simx:    
      description: 'Intercept valves transfer limit (Simx).  Typical Value = 0.425. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    tb:    
      description: 'Boiler time constant (Tb).  Typical Value = 100. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tdp:    
      description: 'Derivative time constant of the power controller (Tdp).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ten:    
      description: 'Electro hydraulic transducer (Ten).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tf:    
      description: 'Frequency transducer time constant (Tf).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tfp:    
      description: 'Time constant of the power controller (Tfp).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    thp:    
      description: 'High pressure (HP) time constant of the turbine (Thp).  Typical Value = 0.31. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tip:    
      description: 'Integral time constant of the power controller (Tip).  Typical Value = 2. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tlp:    
      description: 'Low pressure(LP) time constant of the turbine (Tlp).  Typical Value = 0.45. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tp:    
      description: 'Power transducer time constant (Tp).  Typical Value = 0.07. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    trh:    
      description: 'Reheater  time constant of the turbine (Trh).  Typical Value = 8. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tvhp:    
      description: 'Control valves servo time constant (Tvhp).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tvip:    
      description: 'Intercept valves servo time constant (Tvip).  Typical Value = 0.15. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tw:    
      description: 'Speed transducer time constant (Tw).  Typical Value = 0.02. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be GovSteamEU'    
      enum:    
        - GovSteamEU    
      type: Property    
    wfmax:    
      description: 'Upper limit for frequency correction (Wfmax).  Typical Value = 0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    wfmin:    
      description: 'Lower limit for frequency correction (Wfmin).  Typical Value = -0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    wmax1:    
      description: 'Emergency speed control lower limit (wmax1).  Typical Value = 1.025. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    wmax2:    
      description: 'Emergency speed control upper limit (wmax2).  Typical Value = 1.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    wwmax:    
      description: 'Upper limit for the speed governor (Wwmax).  Typical Value = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    wwmin:    
      description: 'Lower limit for the speed governor frequency correction (Wwmin).  Typical Value = -1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
Nicht verfügbar das Beispiel einer GovSteamEU im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer GovSteamEU im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer GovSteamEU im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer GovSteamEU im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
