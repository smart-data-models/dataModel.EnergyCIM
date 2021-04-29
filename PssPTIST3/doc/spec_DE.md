Entität: PssPTIST3  
==================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/PssPTIST3/LICENSE.md)  
Globale Beschreibung: **Abgeleitet aus CIM-Datenmodellen. PTI Mikroprozessorgestützter Stabilisator Typ 3.**  

## Liste der Eigenschaften  

- `a0`: Filterkoeffizient (A0). Voreinstellung: 0,0  - `a1`: Begrenzer (Al). Voreinstellung: 0,0  - `a2`: Filterkoeffizient (A2). Voreinstellung: 0,0  - `a3`: Filterkoeffizient (A3). Voreinstellung: 0,0  - `a4`: Filterkoeffizient (A4). Voreinstellung: 0,0  - `a5`: Filterkoeffizient (A5). Voreinstellung: 0,0  - `address`: Die Postanschrift  - `al`: Begrenzer (Al). Voreinstellung: 0,0  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `athres`: Schwellenwert, über dem die Ausgangsmittelwertbildung umgangen wird (Athres).  Typischer Wert = 0,005. Voreinstellung: 0,0  - `b0`: Filterkoeffizient (B0). Voreinstellung: 0,0  - `b1`: Filterkoeffizient (B1). Voreinstellung: 0,0  - `b2`: Filterkoeffizient (B2). Voreinstellung: 0,0  - `b3`: Filterkoeffizient (B3). Voreinstellung: 0,0  - `b4`: Filterkoeffizient (B4). Voreinstellung: 0,0  - `b5`: Filterkoeffizient (B5). Voreinstellung: 0,0  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `dl`: Begrenzer (Dl). Voreinstellung: 0.0  - `dtc`: Zeitschritt bezogen auf die Aktivierung der Steuerung (0,03 für 50 Hz) (Dtc).  Typischer Wert = 0,025. Voreinstellung: 0  - `dtf`: Berechnung der Zeitschrittfrequenz (0,03 für 50 Hz) (Dtf).  Typischer Wert = 0,025. Voreinstellung: 0  - `dtp`: Zeitschritt Wirkleistungsberechnung (0,015 für 50 Hz) (Dtp).  Typischer Wert = 0,0125. Voreinstellung: 0  - `id`: Eindeutiger Bezeichner der Entität  - `isw`: Schalter für digitalen/analogen Ausgang (Isw). true = analogen Ausgang erzeugen false = in digitalen Ausgang umwandeln, unter Verwendung der Stufenauswahltabelle. Voreinstellung: Falsch  - `k`: Verstärkung (K).  Typischer Wert = 9. Voreinstellung: 0.0  - `location`:   - `lthres`: Schwellwert (Lthres). Voreinstellung: 0,0  - `m`: (M).  M=2*H.  Typischer Wert = 5. Voreinstellung: 0,0  - `name`: Der Name dieses Elements.  - `nav`: Anzahl der zu mittelnden Steuerausgänge (Nav) (1 <= Nav <= 16).  Typischer Wert = 4. Voreinstellung: 0.0  - `ncl`: Anzahl der Zählungen am Limit zur aktiven Limitfunktion (Ncl) (>0). Voreinstellung: 0.0  - `ncr`: Anzahl der Zählungen bis zum Reset nach Auslösen der Grenzwertfunktion (Ncr). Voreinstellung: 0.0  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `pmin`: (Pmin). Voreinstellung: 0,0  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `t1`: Zeitkonstante (T1).  Typischer Wert = 0,3. Voreinstellung: 0  - `t2`: Zeitkonstante (T2).  Typischer Wert = 1. Voreinstellung: 0  - `t3`: Zeitkonstante (T3).  Typischer Wert = 0,2. Voreinstellung: 0  - `t4`: Zeitkonstante (T4).  Typischer Wert = 0,05. Voreinstellung: 0  - `t5`: Zeitkonstante (T5). Voreinstellung: 0  - `t6`: Zeitkonstante (T6). Voreinstellung: 0  - `tf`: Zeitkonstante (Tf).  Typischer Wert = 0,2. Voreinstellung: 0  - `tp`: Zeitkonstante (Tp).  Typischer Wert = 0,2. Voreinstellung: 0  - `type`: NGSI-Typ. Es muss PssPTIST3 sein    
Erforderliche Eigenschaften  
Dieses Datenmodell ist eine direkte Umsetzung des Common Information Model (CIM), das durch die Norm IEC61970 spezifiziert ist, in Smart Data Models. Die Python-Klassen, auf denen dieses Modell basiert, wurden von diesen Einrichtungen entwickelt Institut für Automatisierung komplexer Stromversorgungssysteme (ACS), EON Energy Research Center (EONERC) und RWTH Aachen, Deutschland. einige Eigenschaften können einen falschen Typ haben. Dies war der Fall, bitte melden Sie einen Fehler oder senden Sie eine E-Mail an alberto.abella@fiware.org  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PssPTIST3:    
  description: 'Adapted from CIM data models. PTI Microprocessor-Based Stabilizer type 3.'    
  properties:    
    a0:    
      description: 'Filter coefficient (A0). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    a1:    
      description: 'Limiter (Al). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    a2:    
      description: 'Filter coefficient (A2). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    a3:    
      description: 'Filter coefficient (A3). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    a4:    
      description: 'Filter coefficient (A4). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    a5:    
      description: 'Filter coefficient (A5). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    al:    
      description: 'Limiter (Al). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    athres:    
      description: 'Threshold value above which output averaging will be bypassed (Athres).  Typical Value = 0.005. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    b0:    
      description: 'Filter coefficient (B0). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    b1:    
      description: 'Filter coefficient (B1). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    b2:    
      description: 'Filter coefficient (B2). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    b3:    
      description: 'Filter coefficient (B3). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    b4:    
      description: 'Filter coefficient (B4). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    b5:    
      description: 'Filter coefficient (B5). Default: 0.0'    
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
    description:    
      description: 'A description of this item'    
      type: Property    
    dl:    
      description: 'Limiter (Dl). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    dtc:    
      description: 'Time step related to activation of controls (0.03 for 50 Hz) (Dtc).  Typical Value = 0.025. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    dtf:    
      description: 'Time step frequency calculation (0.03 for 50 Hz) (Dtf).  Typical Value = 0.025. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    dtp:    
      description: 'Time step active power calculation (0.015 for 50 Hz) (Dtp).  Typical Value = 0.0125. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &pssptist3_-_properties_-_owner_-_items_-_anyof    
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
    isw:    
      description: 'Digital/analog output switch (Isw). true = produce analog output false = convert to digital output, using tap selection table. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    k:    
      description: 'Gain (K).  Typical Value = 9. Default: 0.0'    
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
    lthres:    
      description: 'Threshold value (Lthres). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    m:    
      description: '(M).  M=2*H.  Typical Value = 5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    name:    
      description: 'The name of this item.'    
      type: Property    
    nav:    
      description: 'Number of control outputs to average (Nav) (1 <= Nav <= 16).  Typical Value = 4. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ncl:    
      description: 'Number of counts at limit to active limit function (Ncl) (>0). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ncr:    
      description: 'Number of counts until reset after limit function is triggered (Ncr). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *pssptist3_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    pmin:    
      description: '(Pmin). Default: 0.0'    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    t1:    
      description: 'Time constant (T1).  Typical Value = 0.3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t2:    
      description: 'Time constant (T2).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t3:    
      description: 'Time constant (T3).  Typical Value = 0.2. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t4:    
      description: 'Time constant (T4).  Typical Value = 0.05. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t5:    
      description: 'Time constant (T5). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t6:    
      description: 'Time constant (T6). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tf:    
      description: 'Time constant (Tf).  Typical Value = 0.2. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tp:    
      description: 'Time constant (Tp).  Typical Value = 0.2. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be PssPTIST3'    
      enum:    
        - PssPTIST3    
      type: Property    
  required: []    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
Nicht verfügbar das Beispiel eines PssPTIST3 im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel eines PssPTIST3 im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel eines PssPTIST3 im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel eines PssPTIST3 im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
