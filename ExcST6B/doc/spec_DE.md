Entität: ExcST6B  
================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExcST6B/LICENSE.md)  
Globale Beschreibung: **Abgeleitet aus CIM-Datenmodellen. Modifiziertes statisches Erregersystem IEEE ST6B mit PID-Regler und optionaler innerer Rückkopplungsschleife.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `id`: Eindeutiger Bezeichner der Entität  - `ilr`: Referenz der Erregerausgangsstromgrenze (Ilr).  Typischer Wert = 4.164. Voreinstellung: 0.0  - `k1`: Selektor (K1). true = Rückmeldung ist von Ifd false = Rückmeldung ist nicht von Ifd. Typischer Wert = true. Voreinstellung: Falsch  - `kcl`: Einstellung der Erregerausgangsstromgrenze (Kcl).  Typischer Wert = 1,0577. Voreinstellung: 0,0  - `kff`: Vorsteuerungs-Verstärkungskonstante des Feldreglers der inneren Schleife (Kff).  Typischer Wert = 1. Voreinstellung: 0,0  - `kg`: Rückkopplungsverstärkungskonstante des Feldreglers der inneren Schleife (Kg).  Typischer Wert = 1. Voreinstellung: 0.0  - `kia`: Spannungsregler integrale Verstärkung (Kia).  Typischer Wert = 45,094. Voreinstellung: 0.0  - `klr`: Einstellung der Erregerausgangsstromgrenze (Kcl).  Typischer Wert = 17,33. Voreinstellung: 0.0  - `km`: Vorwärtsverstärkungskonstante des Feldreglers der inneren Schleife (Km).  Typischer Wert = 1. Voreinstellung: 0.0  - `kpa`: Spannungsregler Proportionalverstärkung (Kpa).  Typischer Wert = 18.038. Voreinstellung: 0.0  - `kvd`: Ableitungsverstärkung des Spannungsreglers (Kvd).  Typischer Wert = 0. Voreinstellung: 0.0  - `location`:   - `name`: Der Name dieses Elements.  - `oelin`: OEL-Eingangswahlschalter (OELin). Typischer Wert = noOELinput. Voreinstellung: Keine  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `tg`: Rückführzeitkonstante des Feldspannungsreglers der inneren Schleife (Tg).  Typischer Wert = 0,02. Voreinstellung: 0  - `ts`: Gleichrichter-Zündzeitkonstante (Ts).  Typischer Wert = 0. Voreinstellung: 0  - `tvd`: Ableitungsverstärkung des Spannungsreglers (Tvd).  Typischer Wert = 0. Voreinstellung: 0  - `type`: NGSI-Typ. Es muss ExcST6B sein  - `vamax`: Maximaler Spannungsreglerausgang (Vamax).  Typischer Wert = 4,81. Voreinstellung: 0,0  - `vamin`: Minimaler Spannungsreglerausgang (Vamin).  Typischer Wert = -3,85. Voreinstellung: 0,0  - `vilim`: Selektor (Vilim). true = Vimin-Vimax-Begrenzer ist aktiv false = Vimin-Vimax-Begrenzer ist nicht aktiv. Typischer Wert = true. Voreinstellung: Falsch  - `vimax`: Maximale Eingangsgrenze des Spannungsreglers (Vimax).  Typischer Wert = 10. Voreinstellung: 0.0  - `vimin`: Minimale Eingangsgrenze des Spannungsreglers (Vimin).  Typischer Wert = -10. Voreinstellung: 0,0  - `vmult`: Wahlschalter (Vmult). true = Reglerausgang mit Klemmenspannung multiplizieren false = Reglerausgang nicht mit Klemmenspannung multiplizieren.  Typischer Wert = true. Voreinstellung: False  - `vrmax`: Maximaler Spannungsreglerausgang (Vrmax).  Typischer Wert = 4,81. Voreinstellung: 0,0  - `vrmin`: Minimaler Spannungsreglerausgang (Vrmin).  Typischer Wert = -3,85. Voreinstellung: 0,0  - `xc`: Reaktanz der Erregungsquelle (Xc).  Typischer Wert = 0,05. Voreinstellung: 0,0    
Erforderliche Eigenschaften  
Dieses Datenmodell ist eine direkte Umsetzung des Common Information Model (CIM), das durch die Norm IEC61970 spezifiziert ist, in Smart Data Models. Die Python-Klassen, auf denen dieses Modell basiert, wurden von diesen Einrichtungen entwickelt Institut für Automatisierung komplexer Stromversorgungssysteme (ACS), EON Energy Research Center (EONERC) und RWTH Aachen, Deutschland. einige Eigenschaften können einen falschen Typ haben. Dies war der Fall, bitte melden Sie einen Fehler oder senden Sie eine E-Mail an alberto.abella@fiware.org  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ExcST6B:    
  description: 'Adapted from CIM data models. Modified IEEE ST6B static excitation system with PID controller and optional inner feedbacks loop.'    
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
      anyOf: &excst6b_-_properties_-_owner_-_items_-_anyof    
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
    ilr:    
      description: 'Exciter output current limit reference (Ilr).  Typical Value = 4.164. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    k1:    
      description: 'Selector (K1). true = feedback is from Ifd false = feedback is not from Ifd. Typical Value = true. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kcl:    
      description: 'Exciter output current limit adjustment (Kcl).  Typical Value = 1.0577. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kff:    
      description: 'Pre-control gain constant of the inner loop field regulator (Kff).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kg:    
      description: 'Feedback gain constant of the inner loop field regulator (Kg).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kia:    
      description: 'Voltage regulator integral gain (Kia).  Typical Value = 45.094. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    klr:    
      description: 'Exciter output current limit adjustment (Kcl).  Typical Value = 17.33. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    km:    
      description: 'Forward gain constant of the inner loop field regulator (Km).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kpa:    
      description: 'Voltage regulator proportional gain (Kpa).  Typical Value = 18.038. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kvd:    
      description: 'Voltage regulator derivative gain (Kvd).  Typical Value = 0. Default: 0.0'    
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
    oelin:    
      description: 'OEL input selector (OELin). Typical Value = noOELinput. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *excst6b_-_properties_-_owner_-_items_-_anyof    
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
    tg:    
      description: 'Feedback time constant of inner loop field voltage regulator (Tg).  Typical Value = 0.02. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ts:    
      description: 'Rectifier firing time constant (Ts).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tvd:    
      description: 'Voltage regulator derivative gain (Tvd).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be ExcST6B'    
      enum:    
        - ExcST6B    
      type: Property    
    vamax:    
      description: 'Maximum voltage regulator output (Vamax).  Typical Value = 4.81. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vamin:    
      description: 'Minimum voltage regulator output (Vamin).  Typical Value = -3.85. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vilim:    
      description: 'Selector (Vilim). true = Vimin-Vimax limiter is active false = Vimin-Vimax limiter is not active. Typical Value = true. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vimax:    
      description: 'Maximum voltage regulator input limit (Vimax).  Typical Value = 10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vimin:    
      description: 'Minimum voltage regulator input limit (Vimin).  Typical Value = -10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vmult:    
      description: 'Selector (Vmult). true = multiply regulator output by terminal voltage false = do not multiply regulator output by terminal voltage.  Typical Value = true. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vrmax:    
      description: 'Maximum voltage regulator output (Vrmax).  Typical Value = 4.81. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vrmin:    
      description: 'Minimum voltage regulator output (Vrmin).  Typical Value = -3.85. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    xc:    
      description: 'Excitation source reactance (Xc).  Typical Value = 0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
Nicht verfügbar das Beispiel einer ExcST6B im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer ExcST6B im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer ExcST6B im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer ExcST6B im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
