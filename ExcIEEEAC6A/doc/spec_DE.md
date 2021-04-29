Entität: ExcIEEEAC6A  
====================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExcIEEEAC6A/LICENSE.md)  
Globale Beschreibung: **Abgeleitet von CIM-Datenmodellen. Die Klasse repräsentiert das Modell IEEE Std 421.5-2005 Typ AC6A. Das Modell repräsentiert feldgesteuerte Generator-Gleichrichter-Erregungssysteme mit systemgespeisten elektronischen Spannungsreglern.  Die maximale Leistung des Reglers, , ist eine Funktion der Klemmenspannung, . Der im ursprünglichen Modell AC6A enthaltene Feldstrombegrenzer bleibt in der Aktualisierung 2005 erhalten.  Referenz: IEEE Standard 421.5-2005 Abschnitt 6.6.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `id`: Eindeutiger Bezeichner der Entität  - `ka`: Verstärkung des Spannungsreglers (K).  Typischer Wert = 536. Voreinstellung: 0,0  - `kc`: Belastungsfaktor des Gleichrichters proportional zur Kommutierungsreaktanz (K). Typischer Wert = 0,173. Voreinstellung: 0.0  - `kd`: Entmagnetisierungsfaktor, eine Funktion der Reaktanzen des Erregergenerators (K).  Typischer Wert = 1,91. Voreinstellung: 0,0  - `ke`: Erregerkonstante bezogen auf das selbsterregte Feld (K).  Typischer Wert = 1,6. Voreinstellung: 0,0  - `kh`: Verstärkung des Erregerfeldstrombegrenzers (K).  Typischer Wert = 92. Voreinstellung: 0.0  - `location`:   - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `seve1`: Wert der Erregersättigungsfunktion bei der entsprechenden Erregerspannung, V, hinter der Kommutierungsreaktanz (S[V]).  Typischer Wert = 0,214. Voreinstellung: 0.0  - `seve2`: Wert der Erregersättigungsfunktion bei der entsprechenden Erregerspannung, V, hinter der Kommutierungsreaktanz (S[V]).  Typischer Wert = 0,044. Voreinstellung: 0.0  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `ta`: Zeitkonstante des Spannungsreglers (T).  Typischer Wert = 0,086. Voreinstellung: 0  - `tb`: Zeitkonstante des Spannungsreglers (T).  Typischer Wert = 9. Voreinstellung: 0  - `tc`: Zeitkonstante des Spannungsreglers (T).  Typischer Wert = 3. Voreinstellung: 0  - `te`: Erregerzeitkonstante, Integrationsrate in Verbindung mit der Erregersteuerung (T).  Typischer Wert = 1. Voreinstellung: 0  - `th`: Erregerfeldstrombegrenzer-Zeitkonstante (T).  Typischer Wert = 0,08. Voreinstellung: 0  - `tj`: Erregerfeldstrombegrenzer-Zeitkonstante (T).  Typischer Wert = 0,02. Voreinstellung: 0  - `tk`: Zeitkonstante des Spannungsreglers (T).  Typischer Wert = 0,18. Voreinstellung: 0  - `type`: NGSI-Typ. Es muss ExcIEEEAC6A sein  - `vamax`: Maximaler Spannungsreglerausgang (V).  Typischer Wert = 75. Voreinstellung: 0,0  - `vamin`: Minimaler Spannungsreglerausgang (V).  Typischer Wert = -75. Voreinstellung: 0,0  - `ve1`: Die Ausgangsspannung des Erregergenerators hinter der Kommutierungsreaktanz, bei der die Sättigung definiert ist (V), ist gleich V(V).  Typischer Wert = 7,4. Voreinstellung: 0,0  - `ve2`: Ausgangsspannungen des Erregergenerators hinter der Kommutierungsreaktanz, bei denen die Sättigung definiert ist (V).  Typischer Wert = 5,55. Voreinstellung: 0.0  - `vfelim`: Referenz für die Erregerfeldstromgrenze (V).  Typischer Wert = 19. Voreinstellung: 0.0  - `vhmax`: Maximaler Feldstrombegrenzer-Signalsollwert (V).  Typischer Wert = 75. Voreinstellung: 0.0  - `vrmax`: Maximaler Spannungsreglerausgang (V).  Typischer Wert = 44. Voreinstellung: 0,0  - `vrmin`: Minimaler Spannungsreglerausgang (V).  Typischer Wert = -36. Voreinstellung: 0.0    
Erforderliche Eigenschaften  
Dieses Datenmodell ist eine direkte Umsetzung des Common Information Model (CIM), das durch die Norm IEC61970 spezifiziert ist, in Smart Data Models. Die Python-Klassen, auf denen dieses Modell basiert, wurden von diesen Einrichtungen entwickelt Institut für Automatisierung komplexer Stromversorgungssysteme (ACS), EON Energy Research Center (EONERC) und RWTH Aachen, Deutschland. einige Eigenschaften können einen falschen Typ haben. Dies war der Fall, bitte melden Sie einen Fehler oder senden Sie eine E-Mail an alberto.abella@fiware.org  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ExcIEEEAC6A:    
  description: 'Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type AC6A model. The model represents field-controlled alternator-rectifier excitation systems with system-supplied electronic voltage regulators.  The maximum output of the regulator, , is a function of terminal voltage, . The field current limiter included in the original model AC6A remains in the 2005 update.  Reference: IEEE Standard 421.5-2005 Section 6.6.'    
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
    id:    
      anyOf: &excieeeac6a_-_properties_-_owner_-_items_-_anyof    
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
    ka:    
      description: 'Voltage regulator gain (K).  Typical Value = 536. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kc:    
      description: 'Rectifier loading factor proportional to commutating reactance (K). Typical Value = 0.173. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kd:    
      description: 'Demagnetizing factor, a function of exciter alternator reactances (K).  Typical Value = 1.91. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ke:    
      description: 'Exciter constant related to self-excited field (K).  Typical Value = 1.6. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kh:    
      description: 'Exciter field current limiter gain (K).  Typical Value = 92. Default: 0.0'    
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
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *excieeeac6a_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
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
    seve1:    
      description: 'Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance (S[V]).  Typical Value = 0.214. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    seve2:    
      description: 'Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance (S[V]).  Typical Value = 0.044. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    ta:    
      description: 'Voltage regulator time constant (T).  Typical Value = 0.086. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tb:    
      description: 'Voltage regulator time constant (T).  Typical Value = 9. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tc:    
      description: 'Voltage regulator time constant (T).  Typical Value = 3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    te:    
      description: 'Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    th:    
      description: 'Exciter field current limiter time constant (T).  Typical Value = 0.08. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tj:    
      description: 'Exciter field current limiter time constant (T).  Typical Value = 0.02. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tk:    
      description: 'Voltage regulator time constant (T).  Typical Value = 0.18. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be ExcIEEEAC6A'    
      enum:    
        - ExcIEEEAC6A    
      type: Property    
    vamax:    
      description: 'Maximum voltage regulator output (V).  Typical Value = 75. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vamin:    
      description: 'Minimum voltage regulator output (V).  Typical Value = -75. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ve1:    
      description: 'Exciter alternator output voltages back of commutating reactance at which saturation is defined (V) equals V(V).  Typical Value = 7.4. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ve2:    
      description: 'Exciter alternator output voltages back of commutating reactance at which saturation is defined (V).  Typical Value = 5.55. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vfelim:    
      description: 'Exciter field current limit reference (V).  Typical Value = 19. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vhmax:    
      description: 'Maximum field current limiter signal reference (V).  Typical Value = 75. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vrmax:    
      description: 'Maximum voltage regulator output (V).  Typical Value = 44. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vrmin:    
      description: 'Minimum voltage regulator output (V).  Typical Value = -36. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
Nicht verfügbar das Beispiel einer ExcIEEEAC6A im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer ExcIEEEAC6A im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer ExcIEEEAC6A im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer ExcIEEEAC6A im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
