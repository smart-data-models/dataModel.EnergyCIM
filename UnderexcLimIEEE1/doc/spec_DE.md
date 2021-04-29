Entität: UnderexcLimIEEE1  
=========================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/UnderexcLimIEEE1/LICENSE.md)  
Globale Beschreibung: **Abgeleitet aus CIM-Datenmodellen. Die Klasse repräsentiert das Modell vom Typ UEL1, das eine kreisförmige Begrenzung aufweist, wenn es in Bezug auf die Maschinenblindleistung gegenüber der Wirkleistungsabgabe aufgetragen wird.  Referenz: IEEE UEL1 421.5-2005 Abschnitt 10.1.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `id`: Eindeutiger Bezeichner der Entität  - `kuc`: UEL-Mitteleinstellung (K).  Typischer Wert = 1,38. Voreinstellung: 0,0  - `kuf`: UEL Erregersystem Stabilisatorverstärkung (K).  Typischer Wert = 3,3. Voreinstellung: 0.0  - `kui`: UEL-Integralverstärkung (K).  Typischer Wert = 0. Voreinstellung: 0.0  - `kul`: UEL-Proportionalverstärkung (K).  Typischer Wert = 100. Voreinstellung: 0,0  - `kur`: Einstellung des UEL-Radius (K).  Typischer Wert = 1,95. Voreinstellung: 0,0  - `location`:   - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `tu1`: UEL-Vorlaufzeitkonstante (T).  Typischer Wert = 0. Voreinstellung: 0  - `tu2`: UEL-Verzögerungszeitkonstante (T).  Typischer Wert = 0,05. Voreinstellung: 0  - `tu3`: UEL-Vorlaufzeitkonstante (T).  Typischer Wert = 0. Voreinstellung: 0  - `tu4`: UEL-Verzögerungszeitkonstante (T).  Typischer Wert = 0. Voreinstellung: 0  - `type`: NGSI-Typ. Es muss UnderexcLimIEEE1 sein  - `vucmax`: UEL-Höchstgrenze für Arbeitspunkt-Phasorgröße (V).  Typischer Wert = 5,8. Voreinstellung: 0,0  - `vuimax`: Maximaler Grenzwert für den UEL-Integratorausgang (V). Voreinstellung: 0,0  - `vuimin`: Minimaler Grenzwert für den UEL-Integratorausgang (V). Voreinstellung: 0,0  - `vulmax`: Maximaler Grenzwert des UEL-Ausgangs (V).  Typischer Wert = 18. Voreinstellung: 0.0  - `vulmin`: Minimaler Grenzwert des UEL-Ausgangs (V).  Typischer Wert = -18. Voreinstellung: 0,0  - `vurmax`: UEL-Höchstgrenze für Radius-Phasorgröße (V).  Typischer Wert = 5,8. Voreinstellung: 0.0    
Erforderliche Eigenschaften  
Dieses Datenmodell ist eine direkte Umsetzung des Common Information Model (CIM), das durch die Norm IEC61970 spezifiziert ist, in Smart Data Models. Die Python-Klassen, auf denen dieses Modell basiert, wurden von diesen Einrichtungen entwickelt Institut für Automatisierung komplexer Stromversorgungssysteme (ACS), EON Energy Research Center (EONERC) und RWTH Aachen, Deutschland. einige Eigenschaften können einen falschen Typ haben. Dies war der Fall, bitte melden Sie einen Fehler oder senden Sie eine E-Mail an alberto.abella@fiware.org  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
UnderexcLimIEEE1:    
  description: 'Adapted from CIM data models. The class represents the Type UEL1 model which has a circular limit boundary when plotted in terms of machine reactive power vs. real power output.  Reference: IEEE UEL1 421.5-2005 Section 10.1.'    
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
      anyOf: &underexclimieee1_-_properties_-_owner_-_items_-_anyof    
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
    kuc:    
      description: 'UEL center setting (K).  Typical Value = 1.38. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kuf:    
      description: 'UEL excitation system stabilizer gain (K).  Typical Value = 3.3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kui:    
      description: 'UEL integral gain (K).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kul:    
      description: 'UEL proportional gain (K).  Typical Value = 100. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kur:    
      description: 'UEL radius setting (K).  Typical Value = 1.95. Default: 0.0'    
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
        anyOf: *underexclimieee1_-_properties_-_owner_-_items_-_anyof    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    tu1:    
      description: 'UEL lead time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tu2:    
      description: 'UEL lag time constant (T).  Typical Value = 0.05. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tu3:    
      description: 'UEL lead time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tu4:    
      description: 'UEL lag time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be UnderexcLimIEEE1'    
      enum:    
        - UnderexcLimIEEE1    
      type: Property    
    vucmax:    
      description: 'UEL maximum limit for operating point phasor magnitude (V).  Typical Value = 5.8. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vuimax:    
      description: 'UEL integrator output maximum limit (V). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vuimin:    
      description: 'UEL integrator output minimum limit (V). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vulmax:    
      description: 'UEL output maximum limit (V).  Typical Value = 18. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vulmin:    
      description: 'UEL output minimum limit (V).  Typical Value = -18. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vurmax:    
      description: 'UEL maximum limit for radius phasor magnitude (V).  Typical Value = 5.8. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
Nicht verfügbar das Beispiel einer UnderexcLimIEEE1 im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer UnderexcLimIEEE1 im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar ist das Beispiel einer UnderexcLimIEEE1 im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer UnderexcLimIEEE1 im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
