Entität: ExcIEEEST5B  
====================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExcIEEEST5B/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Abgeleitet von CIM-Datenmodellen. Die Klasse repräsentiert das Modell IEEE Std 421.5-2005 Typ ST5B. Das Erregungssystem Typ ST5B ist eine Variation des Modells Typ ST1A mit alternativen Übererregungs- und Untererregungseingängen und zusätzlichen Grenzwerten.  Referenz: IEEE Standard 421.5-2005 Abschnitt 7.5.   Hinweis: Das Blockdiagramm im IEEE 421.5-Standard hat das Eingangssignal Vc und zeigt nicht den Summationspunkt mit Vref. Die Implementierung des ExcIEEEST5B muss den Summationspunkt mit Vref berücksichtigen.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `id`: Eindeutiger Bezeichner der Entität  - `kc`: Regelungsfaktor des Gleichrichters (K).  Typischer Wert = 0,004. Voreinstellung: 0,0  - `kr`: Verstärkung des Reglers (K).  Typischer Wert = 200. Voreinstellung: 0,0  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `t1`: Zeitkonstante des Zündkreises (T1).  Typischer Wert = 0,004. Voreinstellung: 0  - `tb1`: Verzögerungszeitkonstante des Reglers (T).  Typischer Wert = 6. Voreinstellung: 0  - `tb2`: Verzögerungszeitkonstante des Reglers (T).  Typischer Wert = 0,01. Voreinstellung: 0  - `tc1`: Reglervorlaufzeitkonstante (T).  Typischer Wert = 0,8. Voreinstellung: 0  - `tc2`: Reglervorlaufzeitkonstante (T).  Typischer Wert = 0,08. Voreinstellung: 0  - `tob1`: OEL Verzögerungszeitkonstante (T).  Typischer Wert = 2. Voreinstellung: 0  - `tob2`: OEL Verzögerungszeitkonstante (T).  Typischer Wert = 0,08. Voreinstellung: 0  - `toc1`: OEL-Vorlaufzeitkonstante (T).  Typischer Wert = 0,1. Voreinstellung: 0  - `toc2`: OEL-Vorlaufzeitkonstante (T).  Typischer Wert = 0,08. Voreinstellung: 0  - `tub1`: UEL-Verzögerungszeitkonstante (T).  Typischer Wert = 10. Voreinstellung: 0  - `tub2`: UEL-Verzögerungszeitkonstante (T).  Typischer Wert = 0,05. Voreinstellung: 0  - `tuc1`: UEL-Durchlaufzeitkonstante (T).  Typischer Wert = 2. Voreinstellung: 0  - `tuc2`: UEL-Vorlaufzeitkonstante (T).  Typischer Wert = 0,1. Voreinstellung: 0  - `type`: NGSI-Typ. Es muss ExcIEEEST5B sein  - `vrmax`: Maximaler Spannungsreglerausgang (V).  Typischer Wert = 5. Voreinstellung: 0,0  - `vrmin`: Minimaler Spannungsreglerausgang (V).  Typischer Wert = -4. Voreinstellung: 0,0    
Erforderliche Eigenschaften  
Angepasst von CIM-Datenmodellen und CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Dieses Datenmodell ist eine direkte Umsetzung des Common Information Model (CIM), das durch den Standard IEC61970 spezifiziert ist, in Smart Data Models. Die Python-Klassen, auf denen dieses Modell basiert, wurden von den genannten Einrichtungen Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) und RWTH Aachen entwickelt. Einige Eigenschaften können einen falschen Typ haben. Dies war der Fall, bitte erheben Sie einen Fehler oder senden Sie eine Mail an info@smartdatamodels.org.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ExcIEEEST5B:    
  description: 'Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type ST5B model. The Type ST5B excitation system is a variation of the Type ST1A model, with alternative overexcitation and underexcitation inputs and additional limits.  Reference: IEEE Standard 421.5-2005 Section 7.5.   Note: the block diagram in the IEEE 421.5 standard has input signal Vc and does not indicate the summation point with Vref. The implementation of the ExcIEEEST5B shall consider summation point with Vref.'    
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
    id:    
      anyOf: &excieeest5b_-_properties_-_owner_-_items_-_anyof    
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
    kc:    
      description: 'Rectifier regulation factor (K).  Typical Value = 0.004. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kr:    
      description: 'Regulator gain (K).  Typical Value = 200. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
      type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *excieeest5b_-_properties_-_owner_-_items_-_anyof    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    t1:    
      description: 'Firing circuit time constant (T1).  Typical Value = 0.004. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tb1:    
      description: 'Regulator lag time constant (T).  Typical Value = 6. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tb2:    
      description: 'Regulator lag time constant (T).  Typical Value = 0.01. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tc1:    
      description: 'Regulator lead time constant (T).  Typical Value = 0.8. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tc2:    
      description: 'Regulator lead time constant (T).  Typical Value = 0.08. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tob1:    
      description: 'OEL lag time constant (T).  Typical Value = 2. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tob2:    
      description: 'OEL lag time constant (T).  Typical Value = 0.08. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    toc1:    
      description: 'OEL lead time constant (T).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    toc2:    
      description: 'OEL lead time constant (T).  Typical Value = 0.08. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tub1:    
      description: 'UEL lag time constant (T).  Typical Value = 10. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tub2:    
      description: 'UEL lag time constant (T).  Typical Value = 0.05. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tuc1:    
      description: 'UEL lead time constant (T).  Typical Value = 2. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tuc2:    
      description: 'UEL lead time constant (T).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be ExcIEEEST5B'    
      enum:    
        - ExcIEEEST5B    
      type: Property    
    vrmax:    
      description: 'Maximum voltage regulator output (V).  Typical Value = 5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vrmin:    
      description: 'Minimum voltage regulator output (V).  Typical Value = -4. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
Nicht verfügbar das Beispiel einer ExcIEEEST5B im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer ExcIEEEST5B im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer ExcIEEEST5B im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer ExcIEEEST5B im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
