Entität: ExcIEEEAC8B  
====================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExcIEEEAC8B/LICENSE.md)  
Globale Beschreibung: **Abgeleitet von CIM-Datenmodellen. Die Klasse repräsentiert das Modell IEEE Std 421.5-2005 Typ AC8B. Dieses Modell repräsentiert einen PID-Spannungsregler mit entweder einem bürstenlosen Erreger oder einem Gleichstromerreger. Der Spannungsregler in diesem Modell besteht aus einer PID-Regelung mit separaten Konstanten für die proportionale (), integrale () und derivative () Verstärkung. Die Darstellung des bürstenlosen Erregers (, , , , ) ist ähnlich wie beim Modell Typ AC2A. Das Modell Typ AC8B kann zur Darstellung von statischen Spannungsreglern verwendet werden, die bei bürstenlosen Erregersystemen eingesetzt werden. Digital basierte Spannungsregler, die gleichstrombetriebene rotierende Haupterreger speisen, können mit dem Modell Typ AC8B dargestellt werden, wobei die Parameter und auf 0 gesetzt werden. Für Thyristor-Leistungsstufen, die von den Generatorklemmen gespeist werden, sollten die Grenzen und eine Funktion der Klemmenspannung sein:  * und * .     Referenz: IEEE Standard 421.5-2005 Abschnitt 6.8.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `id`: Eindeutiger Bezeichner der Entität  - `ka`: Verstärkung des Spannungsreglers (K).  Typischer Wert = 1. Voreinstellung: 0,0  - `kc`: Belastungsfaktor des Gleichrichters proportional zur Kommutierungsreaktanz (K). Typischer Wert = 0,55. Voreinstellung: 0,0  - `kd`: Entmagnetisierungsfaktor, eine Funktion der Reaktanzen des Erregergenerators (K).    Typischer Wert = 1,1. Voreinstellung: 0,0  - `kdr`: Ableitungsverstärkung des Spannungsreglers (K).  Typischer Wert = 10. Voreinstellung: 0.0  - `ke`: Erregerkonstante bezogen auf das selbsterregte Feld (K).  Typischer Wert = 1. Voreinstellung: 0,0  - `kir`: Integrale Verstärkung des Spannungsreglers (K).  Typischer Wert = 5. Voreinstellung: 0,0  - `kpr`: Spannungsregler Proportionalverstärkung (K).  Typischer Wert = 80. Voreinstellung: 0,0  - `location`:   - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `seve1`: Wert der Erregersättigungsfunktion bei der entsprechenden Erregerspannung, V, hinter der Kommutierungsreaktanz (S[V]).  Typischer Wert = 0,3. Voreinstellung: 0,0  - `seve2`: Wert der Erregersättigungsfunktion bei der entsprechenden Erregerspannung, V, hinter der Kommutierungsreaktanz (S[V]).  Typischer Wert = 3. Voreinstellung: 0.0  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `ta`: Zeitkonstante des Spannungsreglers (T).  Typischer Wert = 0. Voreinstellung: 0  - `tdr`: Nachlaufzeitkonstante (T).  Typischer Wert = 0,1. Voreinstellung: 0  - `te`: Erregerzeitkonstante, Integrationsrate in Verbindung mit der Erregersteuerung (T).  Typischer Wert = 1,2. Voreinstellung: 0  - `type`: NGSI-Typ. Es muss ExcIEEEAC8B sein  - `ve1`: Die Ausgangsspannungen des Erregergenerators hinter der Kommutierungsreaktanz, bei der die Sättigung definiert ist (V), sind gleich V (V).  Typischer Wert = 6,5. Voreinstellung: 0,0  - `ve2`: Ausgangsspannungen des Erregergenerators hinter der Kommutierungsreaktanz, bei denen die Sättigung definiert ist (V).  Typischer Wert = 9. Voreinstellung: 0.0  - `vemin`: Minimaler Erregerspannungsausgang (V).  Typischer Wert = 0. Voreinstellung: 0.0  - `vfemax`: Referenz für die Erregerfeldstromgrenze (V).  Typischer Wert = 6. Voreinstellung: 0.0  - `vrmax`: Maximaler Spannungsreglerausgang (V).  Typischer Wert = 35. Voreinstellung: 0,0  - `vrmin`: Minimaler Spannungsreglerausgang (V).  Typischer Wert = 0. Voreinstellung: 0.0    
Erforderliche Eigenschaften  
Dieses Datenmodell ist eine direkte Umsetzung des Common Information Model (CIM), das durch die Norm IEC61970 spezifiziert ist, in Smart Data Models. Die Python-Klassen, auf denen dieses Modell basiert, wurden von diesen Einrichtungen entwickelt Institut für Automatisierung komplexer Stromversorgungssysteme (ACS), EON Energy Research Center (EONERC) und RWTH Aachen, Deutschland. einige Eigenschaften können einen falschen Typ haben. Dies war der Fall, bitte melden Sie einen Fehler oder senden Sie eine E-Mail an alberto.abella@fiware.org  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ExcIEEEAC8B:    
  description: 'Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type AC8B model. This model represents a PID voltage regulator with either a brushless exciter or dc exciter. The AVR in this model consists of PID control, with separate constants for the proportional (), integral (), and derivative () gains. The representation of the brushless exciter (, , , , ) is similar to the model Type AC2A. The Type AC8B model can be used to represent static voltage regulators applied to brushless excitation systems. Digitally based voltage regulators feeding dc rotating main exciters can be represented with the AC Type AC8B model with the parameters  and  set to 0.  For thyristor power stages fed from the generator terminals, the limits  and  should be a function of terminal voltage:  * and  * .     Reference: IEEE Standard 421.5-2005 Section 6.8.'    
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
      anyOf: &excieeeac8b_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Voltage regulator gain (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kc:    
      description: 'Rectifier loading factor proportional to commutating reactance (K). Typical Value = 0.55. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kd:    
      description: 'Demagnetizing factor, a function of exciter alternator reactances (K).    Typical Value = 1.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kdr:    
      description: 'Voltage regulator derivative gain (K).  Typical Value = 10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ke:    
      description: 'Exciter constant related to self-excited field (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kir:    
      description: 'Voltage regulator integral gain (K).  Typical Value = 5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kpr:    
      description: 'Voltage regulator proportional gain (K).  Typical Value = 80. Default: 0.0'    
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
        anyOf: *excieeeac8b_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance (S[V]).  Typical Value = 0.3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    seve2:    
      description: 'Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance (S[V]).  Typical Value = 3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    ta:    
      description: 'Voltage regulator time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tdr:    
      description: 'Lag time constant (T).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    te:    
      description: 'Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 1.2. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be ExcIEEEAC8B'    
      enum:    
        - ExcIEEEAC8B    
      type: Property    
    ve1:    
      description: 'Exciter alternator output voltages back of commutating reactance at which saturation is defined (V) equals V (V).  Typical Value = 6.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ve2:    
      description: 'Exciter alternator output voltages back of commutating reactance at which saturation is defined (V).  Typical Value = 9. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vemin:    
      description: 'Minimum exciter voltage output (V).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vfemax:    
      description: 'Exciter field current limit reference (V).  Typical Value = 6. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vrmax:    
      description: 'Maximum voltage regulator output (V).  Typical Value = 35. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vrmin:    
      description: 'Minimum voltage regulator output (V).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
Nicht verfügbar das Beispiel einer ExcIEEEAC8B im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer ExcIEEEAC8B im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer ExcIEEEAC8B im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer ExcIEEEAC8B im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
