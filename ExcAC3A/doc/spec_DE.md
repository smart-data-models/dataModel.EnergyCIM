Entität: ExcAC3A  
================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExcAC3A/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Abgeleitet aus CIM-Datenmodellen. Modifiziertes IEEE AC3A-Gleichrichter-Erregersystem mit unterschiedlicher Feldstromgrenze.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `efdn`: Wert, bei dem sich die Rückkopplungsverstärkung ändert (Efdn).  Typischer Wert = 2,36. Voreinstellung: 0.0  - `id`: Eindeutiger Bezeichner der Entität  - `ka`: Spannungsregler-Verstärkung (Ka).  Typischer Wert = 45,62. Voreinstellung: 0  - `kc`: Belastungsfaktor des Gleichrichters proportional zur Kommutierungsreaktanz (Kc).  Typischer Wert = 0,104. Voreinstellung: 0,0  - `kd`: Entmagnetisierungsfaktor, eine Funktion der Reaktanzen des Erregergenerators (Kd).  Typischer Wert = 0,499. Voreinstellung: 0,0  - `ke`: Erregerkonstante bezogen auf das selbsterregte Feld (Ke).  Typischer Wert = 1. Voreinstellung: 0,0  - `kf`: Erregungssteuerungssystem Stabilisatorverstärkungen (Kf).  Typischer Wert = 0,143. Voreinstellung: 0.0  - `kf1`: Koeffizient, um eine unterschiedliche Verwendung des Modells zu ermöglichen (Kf1).  Typischer Wert = 1. Voreinstellung: 0.0  - `kf2`: Koeffizient, um eine unterschiedliche Nutzung des Modells zu ermöglichen (Kf2).  Typischer Wert = 0. Voreinstellung: 0.0  - `klv`: Verstärkung, die in der Begrenzerschleife für die minimale Feldspannung verwendet wird (Klv).  Typischer Wert = 0,194. Voreinstellung: 0.0  - `kn`: Verstärkung des Stabilisators der Erregungssteuerung (Kn).  Typischer Wert =0,05. Voreinstellung: 0.0  - `kr`: Konstante, die dem Regler und der Feldstromversorgung des Generators zugeordnet ist (Kr).  Typischer Wert =3,77. Voreinstellung: 0,0  - `ks`: Koeffizient, um eine unterschiedliche Verwendung des Modell-Geschwindigkeitskoeffizienten (Ks) zu ermöglichen.  Typischer Wert = 0. Voreinstellung: 0.0  - `location`:   - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `seve1`: Wert der Erregersättigungsfunktion bei der entsprechenden Erregerspannung, Ve, Rückseite der Kommutierungsreaktanz (Se[Ve]).  Typischer Wert = 1.143. Voreinstellung: 0.0  - `seve2`: Wert der Erregersättigungsfunktion bei der entsprechenden Erregerspannung, Ve, hinter der Kommutierungsreaktanz (Se[Ve]).  Typischer Wert = 0,1. Voreinstellung: 0,0  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `ta`: Zeitkonstante des Spannungsreglers (Ta).  Typischer Wert = 0,013. Voreinstellung: 0,0  - `tb`: Zeitkonstante des Spannungsreglers (Tb).  Typischer Wert = 0. Voreinstellung: 0  - `tc`: Zeitkonstante des Spannungsreglers (T).  Typischer Wert = 0. Voreinstellung: 0  - `te`: Erregerzeitkonstante, Integrationsrate in Verbindung mit der Erregersteuerung (Te).  Typischer Wert = 1,17. Voreinstellung: 0  - `tf`: Zeitkonstante des Stabilisators des Erregungssteuerungssystems (Tf).  Typischer Wert = 1. Voreinstellung: 0  - `type`: NGSI-Typ. Es muss ExcAC3A sein  - `vamax`: Maximaler Spannungsreglerausgang (V).  Typischer Wert = 1. Voreinstellung: 0.0  - `vamin`: Minimaler Spannungsreglerausgang (V).  Typischer Wert = -0,95. Voreinstellung: 0,0  - `ve1`: Die Ausgangsspannung des Erregergenerators hinter der Kommutierungsreaktanz, bei der die Sättigung definiert ist (Ve1), ist gleich Vemax (Ve1).  Typischer Wert = 6,24. Voreinstellung: 0,0  - `ve2`: Ausgangsspannungen des Erregergenerators hinter der Kommutierungsreaktanz, bei der die Sättigung definiert ist (Ve).  Typischer Wert = 4,68. Voreinstellung: 0.0  - `vemin`: Minimaler Erregerspannungsausgang (Vemin).  Typischer Wert = 0,1. Voreinstellung: 0,0  - `vfemax`: Erregerfeldstrom-Grenzsollwert (Vfemax).  Typischer Wert = 16. Voreinstellung: 0.0  - `vlv`: Feldspannung, die in der minimalen Feldspannungsbegrenzerschleife (Vlv) verwendet wird.  Typischer Wert = 0,79. Voreinstellung: 0,0    
Erforderliche Eigenschaften  
Angepasst von CIM-Datenmodellen und CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Dieses Datenmodell ist eine direkte Umsetzung des Common Information Model (CIM), das durch den Standard IEC61970 spezifiziert ist, in Smart Data Models. Die Python-Klassen, auf denen dieses Modell basiert, wurden von den genannten Einrichtungen Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) und RWTH Aachen entwickelt. Einige Eigenschaften können einen falschen Typ haben. Dies war der Fall, bitte erheben Sie einen Fehler oder senden Sie eine Mail an info@smartdatamodels.org.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ExcAC3A:    
  description: 'Adapted from CIM data models. Modified IEEE AC3A alternator-supplied rectifier excitation system with different field current limit.'    
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
    efdn:    
      description: 'Value of at which feedback gain changes (Efdn).  Typical Value = 2.36. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &excac3a_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Voltage regulator gain (Ka).  Typical Value = 45.62. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kc:    
      description: 'Rectifier loading factor proportional to commutating reactance (Kc).  Typical Value = 0.104. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kd:    
      description: 'Demagnetizing factor, a function of exciter alternator reactances (Kd).  Typical Value = 0.499. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ke:    
      description: 'Exciter constant related to self-excited field (Ke).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kf:    
      description: 'Excitation control system stabilizer gains (Kf).  Typical Value = 0.143. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kf1:    
      description: 'Coefficient to allow different usage of the model (Kf1).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kf2:    
      description: 'Coefficient to allow different usage of the model (Kf2).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    klv:    
      description: 'Gain used in the minimum field voltage limiter loop (Klv).  Typical Value = 0.194. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kn:    
      description: 'Excitation control system stabilizer gain (Kn).  Typical Value =0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kr:    
      description: 'Constant associated with regulator and alternator field power supply (Kr).  Typical Value =3.77. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ks:    
      description: 'Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0. Default: 0.0'    
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
        anyOf: *excac3a_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
      type: Property    
    seve1:    
      description: 'Exciter saturation function value at the corresponding exciter voltage, Ve, back of commutating reactance (Se[Ve]).  Typical Value = 1.143. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    seve2:    
      description: 'Exciter saturation function value at the corresponding exciter voltage, Ve, back of commutating reactance (Se[Ve]).  Typical Value = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    ta:    
      description: 'Voltage regulator time constant (Ta).  Typical Value = 0.013. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tb:    
      description: 'Voltage regulator time constant (Tb).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tc:    
      description: 'Voltage regulator time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    te:    
      description: 'Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 1.17. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tf:    
      description: 'Excitation control system stabilizer time constant (Tf).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be ExcAC3A'    
      enum:    
        - ExcAC3A    
      type: Property    
    vamax:    
      description: 'Maximum voltage regulator output (V).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vamin:    
      description: 'Minimum voltage regulator output (V).  Typical Value = -0.95. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ve1:    
      description: 'Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1) equals Vemax (Ve1).  Typical Value = 6.24. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ve2:    
      description: 'Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve).  Typical Value = 4.68. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vemin:    
      description: 'Minimum exciter voltage output (Vemin).  Typical Value = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vfemax:    
      description: 'Exciter field current limit reference (Vfemax).  Typical Value = 16. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vlv:    
      description: 'Field voltage used in the minimum field voltage limiter loop (Vlv).  Typical Value = 0.79. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
Nicht verfügbar das Beispiel einer ExcAC3A im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer ExcAC3A im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer ExcAC3A im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer ExcAC3A im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
