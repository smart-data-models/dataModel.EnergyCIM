Entität: TapChanger  
===================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/TapChanger/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Abgeleitet aus CIM-Datenmodellen. Mechanismus zum Ändern von Transformatorwicklungs-Stufenstellungen.**  

## Liste der Eigenschaften  

- `SvTapStep`: Der dem Stufenschalter zugeordnete Stufenschaltzustand. Voreinstellung: Keine  - `TapChangerControl`: Der Stufenschalter, der an diesem Regelstufenschema teilnimmt. Voreinstellung: Keine  - `TapSchedules`: Ein TapSchedule ist mit einem TapChanger verbunden. Standard: 'Liste'  - `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `controlEnabled`: Gibt den Regelungsstatus des Geräts an.  True ist regulierend, false ist nicht regulierend. Voreinstellung: False  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `highStep`: Höchste mögliche Stufenstellung, Vorlauf aus der Neutralstellung. Das Attribut muss größer als lowStep sein. Voreinstellung: 0  - `id`: Eindeutiger Bezeichner der Entität  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `lowStep`: Kleinstmögliche Stufenstellung, verzögert aus der Neutralstellung Default: 0  - `ltcFlag`: Gibt an, ob ein TapChanger über Laststufenwechsel-Fähigkeiten verfügt oder nicht. Voreinstellung: False  - `name`: Der Name dieses Elements.  - `neutralStep`: Die neutrale Stufenstellung für diese Wicklung. Das Attribut muss gleich oder größer als lowStep und gleich oder kleiner als highStep sein. Voreinstellung: 0  - `neutralU`: Spannung, bei der die Wicklung bei der neutralen Anzapfungseinstellung arbeitet. Voreinstellung: 0,0  - `normalStep`: Die im `normalen` Netzbetrieb verwendete Stufenstellung für diese Wicklung. Bei einem `Fixed` Stufenschalter wird die aktuelle physikalische Stufenstellung angegeben. Das Attribut muss gleich oder größer als lowStep und gleich oder kleiner als highStep sein. Voreinstellung: 0  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `step`: Stufenschalterposition. Startschritt für eine stationäre Lösung. Nicht-ganzzahlige Werte sind erlaubt, um kontinuierliche Stufenschaltervariablen zu unterstützen. Die Gründe für kontinuierliche Werte sind die Unterstützung von Studienfällen, in denen noch keine diskreten Stufenschalter entworfen wurden, eine Lösung, bei der ein schmales Spannungsband den Stufenschalter zum Schwingen zwingt, oder die Anpassung an eine kontinuierliche Lösung als Eingabe. Das Attribut muss gleich oder größer als lowStep und gleich oder kleiner als highStep sein. Voreinstellung: 0.0  - `type`: NGSI-Typ. Es muss TapChanger sein    
Erforderliche Eigenschaften  
Angepasst von CIM-Datenmodellen und CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Dieses Datenmodell ist eine direkte Umsetzung des Common Information Model (CIM), das durch den Standard IEC61970 spezifiziert ist, in Smart Data Models. Die Python-Klassen, auf denen dieses Modell basiert, wurden von den genannten Einrichtungen Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) und RWTH Aachen entwickelt. Einige Eigenschaften können einen falschen Typ haben. Dies war der Fall, bitte erheben Sie einen Fehler oder senden Sie eine Mail an info@smartdatamodels.org.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
TapChanger:    
  description: 'Adapted from CIM data models. Mechanism for changing transformer winding tap positions.'    
  properties:    
    SvTapStep:    
      description: 'The tap step state associated with the tap changer. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    TapChangerControl:    
      description: 'The tap changers that participates in this regulating tap control scheme. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    TapSchedules:    
      description: 'A TapSchedule is associated with a TapChanger. Default: ''list'''    
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
    controlEnabled:    
      description: 'Specifies the regulation status of the equipment.  True is regulating, false is not regulating. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    highStep:    
      description: 'Highest possible tap step position, advance from neutral. The attribute shall be greater than lowStep. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &tapchanger_-_properties_-_owner_-_items_-_anyof    
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
    lowStep:    
      description: 'Lowest possible tap step position, retard from neutral Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ltcFlag:    
      description: 'Specifies whether or not a TapChanger has load tap changing capabilities. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    name:    
      description: 'The name of this item.'    
      type: Property    
    neutralStep:    
      description: 'The neutral tap step position for this winding. The attribute shall be equal or greater than lowStep and equal or less than highStep. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    neutralU:    
      description: 'Voltage at which the winding operates at the neutral tap setting. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    normalStep:    
      description: 'The tap step position used in `normal` network operation for this winding. For a `Fixed` tap changer indicates the current physical tap setting. The attribute shall be equal or greater than lowStep and equal or less than highStep. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *tapchanger_-_properties_-_owner_-_items_-_anyof    
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
    step:    
      description: 'Tap changer position. Starting step for a steady state solution. Non integer values are allowed to support continuous tap variables. The reasons for continuous value are to support study cases where no discrete tap changers has yet been designed, a solutions where a narrow voltage band force the tap step to oscillate or accommodate for a continuous solution as input. The attribute shall be equal or greater than lowStep and equal or less than highStep. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be TapChanger'    
      enum:    
        - TapChanger    
      type: Property    
  required: []    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
Nicht verfügbar das Beispiel eines TapChangers im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel eines TapChangers im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel eines TapChangers im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel eines TapChangers im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
