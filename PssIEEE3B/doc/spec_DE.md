Entität: PssIEEE3B  
==================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/PssIEEE3B/LICENSE.md)  
Globale Beschreibung: **Abgeleitet von CIM-Datenmodellen. Die Klasse repräsentiert das Leistungssystemstabilisatormodell IEEE Std 421.5-2005 vom Typ PSS3B. Das PSS-Modell PSS3B hat zwei Eingänge für elektrische Leistung und Rotorwinkelfrequenzabweichung. Die Signale werden zur Ableitung eines äquivalenten mechanischen Leistungssignals verwendet.  Referenz: IEEE 3B 421.5-2005 Abschnitt 8.3.**  

## Liste der Eigenschaften  

- `a1`: Kerbfilter-Parameter (A1).  Typischer Wert = 0,359. Voreinstellung: 0.0  - `a2`: Kerbfilter-Parameter (A2).  Typischer Wert = 0,586. Voreinstellung: 0.0  - `a3`: Kerbfilter-Parameter (A3).  Typischer Wert = 0,429. Voreinstellung: 0.0  - `a4`: Kerbfilter-Parameter (A4).  Typischer Wert = 0,564. Voreinstellung: 0.0  - `a5`: Kerbfilter-Parameter (A5).  Typischer Wert = 0,001. Voreinstellung: 0.0  - `a6`: Kerbfilter-Parameter (A6).  Typischer Wert = 0. Voreinstellung: 0.0  - `a7`: Kerbfilter-Parameter (A7).  Typischer Wert = 0,031. Voreinstellung: 0.0  - `a8`: Kerbfilter-Parameter (A8).  Typischer Wert = 0. Voreinstellung: 0.0  - `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `id`: Eindeutiger Bezeichner der Entität  - `inputSignal1Type`: Typ des Eingangssignals #1.  Typischer Wert = generatorElectricalPower. Voreinstellung: Keine  - `inputSignal2Type`: Typ des Eingangssignals #2.  Typischer Wert = rotorSpeed. Voreinstellung: Keine  - `ks1`: Verstärkung auf Signal # 1 (Ks1).  Typischer Wert = -0,602. Voreinstellung: 0.0  - `ks2`: Verstärkung auf Signal # 2 (Ks2).  Typischer Wert = 30,12. Voreinstellung: 0.0  - `location`:   - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `t1`: Wandler-Zeitkonstante (T1).  Typischer Wert = 0,012. Voreinstellung: 0  - `t2`: Wandler-Zeitkonstante (T2).  Typischer Wert = 0,012. Voreinstellung: 0  - `tw1`: Auswaschzeitkonstante (Tw1).  Typischer Wert = 0,3. Voreinstellung: 0  - `tw2`: Auswaschzeitkonstante (Tw2).  Typischer Wert = 0,3. Voreinstellung: 0  - `tw3`: Auswaschzeitkonstante (Tw3).  Typischer Wert = 0,6. Voreinstellung: 0  - `type`: NGSI-Typ. Es muss PssIEEE3B sein  - `vstmax`: Maximalgrenze des Stabilisatorausgangs (Vstmax).  Typischer Wert = 0,1. Voreinstellung: 0,0  - `vstmin`: Minimalgrenze des Stabilisatorausgangs (Vstmin).  Typischer Wert = -0,1. Voreinstellung: 0,0    
Erforderliche Eigenschaften  
Dieses Datenmodell ist eine direkte Umsetzung des Common Information Model (CIM), das durch die Norm IEC61970 spezifiziert ist, in Smart Data Models. Die Python-Klassen, auf denen dieses Modell basiert, wurden von diesen Einrichtungen entwickelt Institut für Automatisierung komplexer Stromversorgungssysteme (ACS), EON Energy Research Center (EONERC) und RWTH Aachen, Deutschland. einige Eigenschaften können einen falschen Typ haben. Dies war der Fall, bitte melden Sie einen Fehler oder senden Sie eine E-Mail an alberto.abella@fiware.org  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PssIEEE3B:    
  description: 'Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type PSS3B power system stabilizer model. The PSS model PSS3B has dual inputs of electrical power and rotor angular frequency deviation. The signals are used to derive an equivalent mechanical power signal.  Reference: IEEE 3B 421.5-2005 Section 8.3.'    
  properties:    
    a1:    
      description: 'Notch filter parameter (A1).  Typical Value = 0.359. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    a2:    
      description: 'Notch filter parameter (A2).  Typical Value = 0.586. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    a3:    
      description: 'Notch filter parameter (A3).  Typical Value = 0.429. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    a4:    
      description: 'Notch filter parameter (A4).  Typical Value = 0.564. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    a5:    
      description: 'Notch filter parameter (A5).  Typical Value = 0.001. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    a6:    
      description: 'Notch filter parameter (A6).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    a7:    
      description: 'Notch filter parameter (A7).  Typical Value = 0.031. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    a8:    
      description: 'Notch filter parameter (A8).  Typical Value = 0. Default: 0.0'    
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
    id:    
      anyOf: &pssieee3b_-_properties_-_owner_-_items_-_anyof    
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
    inputSignal1Type:    
      description: "Type of input signal #1.  Typical Value = generatorElectricalPower. Default: None"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    inputSignal2Type:    
      description: "Type of input signal #2.  Typical Value = rotorSpeed. Default: None"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ks1:    
      description: "Gain on signal # 1 (Ks1).  Typical Value = -0.602. Default: 0.0"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ks2:    
      description: "Gain on signal # 2 (Ks2).  Typical Value = 30.12. Default: 0.0"    
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
        anyOf: *pssieee3b_-_properties_-_owner_-_items_-_anyof    
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
    t1:    
      description: 'Transducer time constant (T1).  Typical Value = 0.012. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t2:    
      description: 'Transducer time constant (T2).  Typical Value = 0.012. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tw1:    
      description: 'Washout time constant (Tw1).  Typical Value = 0.3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tw2:    
      description: 'Washout time constant (Tw2).  Typical Value = 0.3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tw3:    
      description: 'Washout time constant (Tw3).  Typical Value = 0.6. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be PssIEEE3B'    
      enum:    
        - PssIEEE3B    
      type: Property    
    vstmax:    
      description: 'Stabilizer output max limit (Vstmax).  Typical Value = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vstmin:    
      description: 'Stabilizer output min limit (Vstmin).  Typical Value = -0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
Nicht verfügbar das Beispiel einer PssIEEE3B im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer PssIEEE3B im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer PssIEEE3B im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer PssIEEE3B im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
