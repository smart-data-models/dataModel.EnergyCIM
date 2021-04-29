Entität: LoadStatic  
===================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/LoadStatic/LICENSE.md)  
Globale Beschreibung: **Abgeleitet aus CIM-Datenmodellen. Allgemeines statisches Lastmodell, das die Empfindlichkeit der von der Last aufgenommenen Wirk- und Blindleistung gegenüber der Amplitude und Frequenz der Busspannung darstellt.**  

## Liste der Eigenschaften  

- `LoadAggregate`: Aggregatlast, zu der diese statische Aggregatlast gehört. Voreinstellung: Keine  - `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `ep1`: Spannungsexponent des ersten Terms für die Wirkleistung (Ep1).  Wird nur verwendet, wenn .staticLoadModelType = exponential. Voreinstellung: 0,0  - `ep2`: Spannungsexponent des zweiten Terms für die Wirkleistung (Ep2).  Wird nur verwendet, wenn .staticLoadModelType = exponential. Voreinstellung: 0,0  - `ep3`: Spannungsexponent des dritten Terms für die Wirkleistung (Ep3).  Wird nur verwendet, wenn .staticLoadModelType = exponential. Voreinstellung: 0,0  - `eq1`: Spannungsexponent des ersten Terms für die Blindleistung (Eq1).  Wird nur verwendet, wenn .staticLoadModelType = exponential. Voreinstellung: 0,0  - `eq2`: Spannungsexponent des zweiten Terms für die Blindleistung (Eq2).  Wird nur verwendet, wenn .staticLoadModelType = exponential. Voreinstellung: 0,0  - `eq3`: Spannungsexponent des dritten Terms für die Blindleistung (Eq3).  Wird nur verwendet, wenn .staticLoadModelType = exponential. Voreinstellung: 0,0  - `id`: Eindeutiger Bezeichner der Entität  - `kp1`: Spannungskoeffizient des ersten Terms für die Wirkleistung (Kp1).  Wird nicht verwendet, wenn .staticLoadModelType = constantZ. Voreinstellung: 0.0  - `kp2`: Spannungskoeffizient des zweiten Terms für die Wirkleistung (Kp2).  Wird nicht verwendet, wenn .staticLoadModelType = constantZ. Voreinstellung: 0.0  - `kp3`: Spannungskoeffizient des dritten Terms für die Wirkleistung (Kp3).  Wird nicht verwendet, wenn .staticLoadModelType = constantZ. Voreinstellung: 0.0  - `kp4`: Frequenzkoeffizient für die Wirkleistung (Kp4).  Muss ungleich Null sein, wenn .staticLoadModelType = ZIP2.  Nicht verwendet für alle anderen Werte von .staticLoadModelType. Voreinstellung: 0.0  - `kpf`: Frequenzabweichungskoeffizient für die Wirkleistung (Kpf).  Wird nicht verwendet, wenn .staticLoadModelType = constantZ. Voreinstellung: 0.0  - `kq1`: Spannungskoeffizient des ersten Terms für Blindleistung (Kq1).  Wird nicht verwendet, wenn .staticLoadModelType = constantZ. Voreinstellung: 0.0  - `kq2`: Spannungskoeffizient des zweiten Terms für Blindleistung (Kq2).  Wird nicht verwendet, wenn .staticLoadModelType = constantZ. Voreinstellung: 0.0  - `kq3`: Dritter Term Spannungskoeffizient für Blindleistung (Kq3).  Wird nicht verwendet, wenn .staticLoadModelType = constantZ. Voreinstellung: 0.0  - `kq4`: Frequenzkoeffizient für Blindleistung (Kq4).  Muss ungleich Null sein, wenn .staticLoadModelType = ZIP2.  Nicht verwendet für alle anderen Werte von .staticLoadModelType. Voreinstellung: 0.0  - `kqf`: Frequenzabweichungskoeffizient für Blindleistung (Kqf).  Wird nicht verwendet, wenn .staticLoadModelType = constantZ. Voreinstellung: 0.0  - `location`:   - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `staticLoadModelType`: Typ des statischen Lastmodells.  Typischer Wert = konstantZ. Voreinstellung: Keine  - `type`: NGSI-Typ. Es muss LoadStatic sein    
Erforderliche Eigenschaften  
Dieses Datenmodell ist eine direkte Umsetzung des Common Information Model (CIM), das durch die Norm IEC61970 spezifiziert ist, in Smart Data Models. Die Python-Klassen, auf denen dieses Modell basiert, wurden von diesen Einrichtungen entwickelt Institut für Automatisierung komplexer Stromversorgungssysteme (ACS), EON Energy Research Center (EONERC) und RWTH Aachen, Deutschland. einige Eigenschaften können einen falschen Typ haben. Dies war der Fall, bitte melden Sie einen Fehler oder senden Sie eine E-Mail an alberto.abella@fiware.org  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
LoadStatic:    
  description: 'Adapted from CIM data models. General static load model representing the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage.'    
  properties:    
    LoadAggregate:    
      description: 'Aggregate load to which this aggregate static load belongs. Default: None'    
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
    ep1:    
      description: 'First term voltage exponent for active power (Ep1).  Used only when .staticLoadModelType = exponential. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ep2:    
      description: 'Second term voltage exponent for active power (Ep2).  Used only when .staticLoadModelType = exponential. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ep3:    
      description: 'Third term voltage exponent for active power (Ep3).  Used only when .staticLoadModelType = exponential. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    eq1:    
      description: 'First term voltage exponent for reactive power (Eq1).  Used only when .staticLoadModelType = exponential. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    eq2:    
      description: 'Second term voltage exponent for reactive power (Eq2).  Used only when .staticLoadModelType = exponential. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    eq3:    
      description: 'Third term voltage exponent for reactive power (Eq3).  Used only when .staticLoadModelType = exponential. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &loadstatic_-_properties_-_owner_-_items_-_anyof    
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
    kp1:    
      description: 'First term voltage coefficient for active power (Kp1).  Not used when .staticLoadModelType = constantZ. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kp2:    
      description: 'Second term voltage coefficient for active power (Kp2).  Not used when .staticLoadModelType = constantZ. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kp3:    
      description: 'Third term voltage coefficient for active power (Kp3).  Not used when .staticLoadModelType = constantZ. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kp4:    
      description: 'Frequency coefficient for active power (Kp4).  Must be non-zero when .staticLoadModelType = ZIP2.  Not used for all other values of .staticLoadModelType. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kpf:    
      description: 'Frequency deviation coefficient for active power (Kpf).  Not used when .staticLoadModelType = constantZ. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kq1:    
      description: 'First term voltage coefficient for reactive power (Kq1).  Not used when .staticLoadModelType = constantZ. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kq2:    
      description: 'Second term voltage coefficient for reactive power (Kq2).  Not used when .staticLoadModelType = constantZ. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kq3:    
      description: 'Third term voltage coefficient for reactive power (Kq3).  Not used when .staticLoadModelType = constantZ. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kq4:    
      description: 'Frequency coefficient for reactive power (Kq4).  Must be non-zero when .staticLoadModelType = ZIP2.  Not used for all other values of .staticLoadModelType. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kqf:    
      description: 'Frequency deviation coefficient for reactive power (Kqf).  Not used when .staticLoadModelType = constantZ. Default: 0.0'    
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
        anyOf: *loadstatic_-_properties_-_owner_-_items_-_anyof    
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
    staticLoadModelType:    
      description: 'Type of static load model.  Typical Value = constantZ. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be LoadStatic'    
      enum:    
        - LoadStatic    
      type: Property    
  required: []    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
Nicht verfügbar ist das Beispiel einer LoadStatic im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar ist das Beispiel einer LoadStatic im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar ist das Beispiel einer LoadStatic im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar ist das Beispiel einer LoadStatic im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
