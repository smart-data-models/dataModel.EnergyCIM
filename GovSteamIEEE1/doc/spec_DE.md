Entität: GovSteamIEEE1  
======================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovSteamIEEE1/LICENSE.md)  
Globale Beschreibung: **Abgeleitet aus CIM-Datenmodellen. IEEE-Dampfturbinenregler-Modell.  Ref**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `id`: Eindeutiger Bezeichner der Entität  - `k`: Verstärkung des Reglers (Kehrwert des P-Bereichs) (K) (> 0).  Typischer Wert = 25. Voreinstellung: 0.0  - `k1`: Bruchteil der HP-Wellenleistung nach dem ersten Kesseldurchgang (K1).  Typischer Wert = 0,2. Voreinstellung: 0,0  - `k2`: Bruchteil der LP-Wellenleistung nach dem ersten Kesseldurchgang (K2).  Typischer Wert = 0. Voreinstellung: 0.0  - `k3`: Bruchteil der HP-Wellenleistung nach dem zweiten Kesseldurchgang (K3).  Typischer Wert = 0,3. Voreinstellung: 0,0  - `k4`: Bruchteil der LP-Wellenleistung nach dem zweiten Kesseldurchgang (K4).  Typischer Wert = 0. Voreinstellung: 0.0  - `k5`: Bruchteil der HP-Wellenleistung nach dem dritten Kesseldurchgang (K5).  Typischer Wert = 0,5. Voreinstellung: 0,0  - `k6`: Bruchteil der LP-Wellenleistung nach dem dritten Kesseldurchgang (K6).  Typischer Wert = 0. Voreinstellung: 0.0  - `k7`: Bruchteil der HP-Wellenleistung nach dem vierten Kesseldurchgang (K7).  Typischer Wert = 0. Voreinstellung: 0.0  - `k8`: Bruchteil der LP-Wellenleistung nach dem vierten Kesseldurchgang (K8).  Typischer Wert = 0. Voreinstellung: 0.0  - `location`:   - `mwbase`: Basis für Leistungswerte (MWbase) (> 0) Default: 0.0  - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `pmax`: Maximale Ventilöffnung (Pmax) (> Pmin).  Typischer Wert = 1. Voreinstellung: 0,0  - `pmin`: Minimale Ventilöffnung (Pmin) (>= 0).  Typischer Wert = 0. Voreinstellung: 0.0  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `t1`: Verzögerungszeitkonstante des Reglers (T1).  Typischer Wert = 0. Voreinstellung: 0  - `t2`: Reglervorlaufzeitkonstante (T2).  Typischer Wert = 0. Voreinstellung: 0  - `t3`: Zeitkonstante des Ventilstellungsreglers (T3) (> 0).  Typischer Wert = 0,1. Voreinstellung: 0  - `t4`: Zeitkonstante der Einlassleitung/Dampfschale (T4).  Typischer Wert = 0,3. Voreinstellung: 0  - `t5`: Zeitkonstante des zweiten Kesseldurchgangs (T5).  Typischer Wert = 5. Voreinstellung: 0  - `t6`: Zeitkonstante des dritten Kesseldurchgangs (T6).  Typischer Wert = 0,5. Voreinstellung: 0  - `t7`: Zeitkonstante des vierten Kesseldurchgangs (T7).  Typischer Wert = 0. Voreinstellung: 0  - `type`: NGSI-Typ. Es muss GovSteamIEEE1 sein  - `uc`: Maximale Ventilschließgeschwindigkeit (Uc) (< 0).  Einheit = PU/sec.  Typischer Wert = -10. Voreinstellung: 0.0  - `uo`: Maximale Ventilöffnungsgeschwindigkeit (Uo) (> 0).  Einheit = PU/sec.  Typischer Wert = 1. Voreinstellung: 0.0    
Erforderliche Eigenschaften  
Dieses Datenmodell ist eine direkte Umsetzung des Common Information Model (CIM), das durch die Norm IEC61970 spezifiziert ist, in Smart Data Models. Die Python-Klassen, auf denen dieses Modell basiert, wurden von diesen Einrichtungen entwickelt Institut für Automatisierung komplexer Stromversorgungssysteme (ACS), EON Energy Research Center (EONERC) und RWTH Aachen, Deutschland. einige Eigenschaften können einen falschen Typ haben. Dies war der Fall, bitte melden Sie einen Fehler oder senden Sie eine E-Mail an alberto.abella@fiware.org  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GovSteamIEEE1:    
  description: 'Adapted from CIM data models. IEEE steam turbine governor model.  Ref'    
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
      anyOf: &govsteamieee1_-_properties_-_owner_-_items_-_anyof    
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
    k:    
      description: 'Governor gain (reciprocal of droop) (K) (> 0).  Typical Value = 25. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    k1:    
      description: 'Fraction of HP shaft power after first boiler pass (K1).  Typical Value = 0.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    k2:    
      description: 'Fraction of LP shaft power after first boiler pass (K2).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    k3:    
      description: 'Fraction of HP shaft power after second boiler pass (K3).  Typical Value = 0.3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    k4:    
      description: 'Fraction of LP shaft power after second boiler pass (K4).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    k5:    
      description: 'Fraction of HP shaft power after third boiler pass (K5).  Typical Value = 0.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    k6:    
      description: 'Fraction of LP shaft power after third boiler pass (K6).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    k7:    
      description: 'Fraction of HP shaft power after fourth boiler pass (K7).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    k8:    
      description: 'Fraction of LP shaft power after fourth boiler pass (K8).  Typical Value = 0. Default: 0.0'    
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
      description: 'Base for power values (MWbase) (> 0) Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *govsteamieee1_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    pmax:    
      description: 'Maximum valve opening (Pmax) (> Pmin).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmin:    
      description: 'Minimum valve opening (Pmin) (>= 0).  Typical Value = 0. Default: 0.0'    
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
      description: 'Governor lag time constant (T1).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t2:    
      description: 'Governor lead time constant (T2).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t3:    
      description: 'Valve positioner time constant (T3) (> 0).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t4:    
      description: 'Inlet piping/steam bowl time constant (T4).  Typical Value = 0.3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t5:    
      description: 'Time constant of second boiler pass (T5).  Typical Value = 5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t6:    
      description: 'Time constant of third boiler pass (T6).  Typical Value = 0.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t7:    
      description: 'Time constant of fourth boiler pass (T7).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be GovSteamIEEE1'    
      enum:    
        - GovSteamIEEE1    
      type: Property    
    uc:    
      description: 'Maximum valve closing velocity (Uc) (< 0).  Unit = PU/sec.  Typical Value = -10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    uo:    
      description: 'Maximum valve opening velocity (Uo) (> 0).  Unit = PU/sec.  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
Nicht verfügbar ist das Beispiel einer GovSteamIEEE1 im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer GovSteamIEEE1 im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar ist das Beispiel eines GovSteamIEEE1 im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer GovSteamIEEE1 im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
