Entität: Pss1A  
==============  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/Pss1A/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Abgeleitet aus CIM-Datenmodellen. Leistungssystemstabilisator mit einem Eingang. Es handelt sich um eine modifizierte Version, um die Darstellung von Implementierungen verschiedener Hersteller auf PSS Typ 1A zu ermöglichen.  

## Liste der Eigenschaften  

- `a1`: Kerbfilter-Parameter (A1). Voreinstellung: 0.0  - `a2`: Kerbfilter-Parameter (A2). Voreinstellung: 0.0  - `a3`: Kerbfilter-Parameter (A3). Voreinstellung: 0.0  - `a4`: Kerbfilter-Parameter (A4). Voreinstellung: 0.0  - `a5`: Kerbfilter-Parameter (A5). Voreinstellung: 0.0  - `a6`: Kerbfilter-Parameter (A6). Voreinstellung: 0.0  - `a7`: Kerbfilter-Parameter (A7). Voreinstellung: 0.0  - `a8`: Kerbfilter-Parameter (A8). Voreinstellung: 0.0  - `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `id`: Eindeutiger Bezeichner der Entität  - `inputSignalType`: Typ des Eingangssignals. Voreinstellung: Keine  - `kd`: Selektor (Kd). true = e verwendet false = e nicht verwendet. Voreinstellung: False  - `ks`: Stabilisator-Verstärkung (Ks). Voreinstellung: 0,0  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `t1`: Vorlauf-/Verzögerungszeitkonstante (T1). Voreinstellung: 0  - `t2`: Vorlauf-/Verzögerungszeitkonstante (T2). Voreinstellung: 0  - `t3`: Vorlauf-/Verzögerungszeitkonstante (T3). Voreinstellung: 0  - `t4`: Vorlauf-/Verzögerungszeitkonstante (T4). Voreinstellung: 0  - `t5`: Auswaschzeitkonstante (T5). Voreinstellung: 0  - `t6`: Wandler-Zeitkonstante (T6). Voreinstellung: 0  - `tdelay`: Zeitkonstante (Tdelay). Voreinstellung: 0  - `type`: NGSI-Typ. Es muss Pss1A sein  - `vcl`: Schwellenwert für die Eingangsabschaltung des Stabilisators (Vcl). Voreinstellung: 0,0  - `vcu`: Schwellenwert für die Eingangsabschaltung des Stabilisators (Vcu). Voreinstellung: 0,0  - `vrmax`: Maximaler Stabilisatorausgang (Vrmax). Voreinstellung: 0,0  - `vrmin`: Minimaler Stabilisatorausgang (Vrmin). Voreinstellung: 0,0    
Erforderliche Eigenschaften  
Angepasst von CIM-Datenmodellen und CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Dieses Datenmodell ist eine direkte Umsetzung des Common Information Model (CIM), das durch den Standard IEC61970 spezifiziert ist, in Smart Data Models. Die Python-Klassen, auf denen dieses Modell basiert, wurden von den genannten Einrichtungen Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) und RWTH Aachen entwickelt. Einige Eigenschaften können einen falschen Typ haben. Dies war der Fall, bitte erheben Sie einen Fehler oder senden Sie eine Mail an info@smartdatamodels.org.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Pss1A:    
  description: 'Adapted from CIM data models. Single input power system stabilizer. It is a modified version in order to allow representation of various vendors'' implementations on PSS type 1A.'    
  properties:    
    a1:    
      description: 'Notch filter parameter (A1). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    a2:    
      description: 'Notch filter parameter (A2). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    a3:    
      description: 'Notch filter parameter (A3). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    a4:    
      description: 'Notch filter parameter (A4). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    a5:    
      description: 'Notch filter parameter (A5). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    a6:    
      description: 'Notch filter parameter (A6). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    a7:    
      description: 'Notch filter parameter (A7). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    a8:    
      description: 'Notch filter parameter (A8). Default: 0.0'    
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
      anyOf: &pss1a_-_properties_-_owner_-_items_-_anyof    
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
    inputSignalType:    
      description: 'Type of input signal. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kd:    
      description: 'Selector (Kd).  true = e used false = e not used. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ks:    
      description: 'Stabilizer gain (Ks). Default: 0.0'    
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
        anyOf: *pss1a_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Lead/lag time constant (T1). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t2:    
      description: 'Lead/lag time constant (T2). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t3:    
      description: 'Lead/lag time constant (T3). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t4:    
      description: 'Lead/lag time constant (T4). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t5:    
      description: 'Washout time constant (T5). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t6:    
      description: 'Transducer time constant (T6). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tdelay:    
      description: 'Time constant (Tdelay). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be Pss1A'    
      enum:    
        - Pss1A    
      type: Property    
    vcl:    
      description: 'Stabilizer input cutoff threshold (Vcl). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vcu:    
      description: 'Stabilizer input cutoff threshold (Vcu). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vrmax:    
      description: 'Maximum stabilizer output (Vrmax). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vrmin:    
      description: 'Minimum stabilizer output (Vrmin). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
Nicht verfügbar das Beispiel einer Pss1A im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer Pss1A im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer Pss1A im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer Pss1A im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
