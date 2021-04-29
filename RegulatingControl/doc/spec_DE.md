Entität: RegulatingControl  
==========================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/RegulatingControl/LICENSE.md)  
Globale Beschreibung: **Abgeleitet aus CIM-Datenmodellen. Gibt eine Gruppe von Geräten an, die zusammenarbeiten, um eine Größe des Stromnetzes, wie z. B. Spannung oder Durchfluss, zu steuern.  Eine Fernsteuerung der Busspannung ist möglich, indem die gesteuerte Klemme an einem von den steuernden Geräten entfernten Ort angegeben wird. Wenn mehrere Geräte, möglicherweise unterschiedlichen Typs, dieselbe Klemme steuern, darf es nur ein RegulatingControl an dieser Klemme geben. Der spezifischste Subtyp von RegulatingControl muss verwendet werden, wenn solche Geräte an der Steuerung teilnehmen, z. B. TapChangerControl für Stufenschalter. Für die Flusssteuerung wird die Lastvorzeichenkonvention verwendet, d. h. ein positives Vorzeichen bedeutet, dass ein Strom von einem TopologicalNode (Bus) in das leitende Gerät fließt.**  

## Liste der Eigenschaften  

- `RegulatingCondEq`: Das Gerät, das an diesem Regelungsschema teilnimmt. Standard: 'Liste'  - `RegulationSchedule`: Zeitplan für diese Regelungssteuerung. Standard: 'Liste'  - `Terminal`: Die Steuerelemente, die diese Klemme regeln. Voreinstellung: Keine  - `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `discrete`: Die Regelung erfolgt in einem diskreten Modus. Dies gilt für Geräte mit diskreter Regelung, z. B. Stufenschalter und Nebenschlusskompensatoren. Voreinstellung: Falsch  - `enabled`: Das Flag gibt an, ob die Regelung aktiviert ist. Voreinstellung: False  - `id`: Eindeutiger Bezeichner der Entität  - `location`:   - `mode`: Die Regelungsart ist derzeit verfügbar.  Mit dieser Angabe kann die Art der Regelung bestimmt werden, ohne dass die Einheiten aus einem Zeitplan entnommen werden müssen. Voreinstellung: Keine  - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `targetDeadband`: Dies ist eine Totzone, die bei diskreter Regelung verwendet wird, um eine übermäßige Aktualisierung von Reglern wie Stufenschaltern und Nebenschlusskompensatorbänken während der Regelung zu vermeiden. Die Einheiten der für den Modus geeigneten. Voreinstellung: 0.0  - `targetValue`: Der für die Falleingabe angegebene Zielwert.   Dieser Wert kann für den Zielwert ohne die Verwendung von Zeitplänen verwendet werden. Der Wert hat die zum Modus-Attribut passenden Einheiten. Voreinstellung: 0.0  - `targetValueUnitMultiplier`: Geben Sie den Multiplikator an, der für den targetValue verwendet wird. Voreinstellung: Keine  - `type`: NGSI-Typ. Es muss RegulatingControl sein    
Erforderliche Eigenschaften  
Dieses Datenmodell ist eine direkte Umsetzung des Common Information Model (CIM), das durch die Norm IEC61970 spezifiziert ist, in Smart Data Models. Die Python-Klassen, auf denen dieses Modell basiert, wurden von diesen Einrichtungen entwickelt Institut für Automatisierung komplexer Stromversorgungssysteme (ACS), EON Energy Research Center (EONERC) und RWTH Aachen, Deutschland. einige Eigenschaften können einen falschen Typ haben. Dies war der Fall, bitte melden Sie einen Fehler oder senden Sie eine E-Mail an alberto.abella@fiware.org  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
RegulatingControl:    
  description: 'Adapted from CIM data models. Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.  Remote bus voltage control is possible by specifying the controlled terminal located at some place remote from the controlling equipment. In case multiple equipment, possibly of different types, control same terminal there must be only one RegulatingControl at that terminal. The most specific subtype of RegulatingControl shall be used in case such equipment participate in the control, e.g. TapChangerControl for tap changers. For flow control  load sign convention is used, i.e. positive sign means flow out from a TopologicalNode (bus) into the conducting equipment.'    
  properties:    
    RegulatingCondEq:    
      description: 'The equipment that participates in this regulating control scheme. Default: ''list'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    RegulationSchedule:    
      description: 'Schedule for this Regulating regulating control. Default: ''list'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    Terminal:    
      description: 'The controls regulating this terminal. Default: None'    
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
    discrete:    
      description: 'The regulation is performed in a discrete mode. This applies to equipment with discrete controls, e.g. tap changers and shunt compensators. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    enabled:    
      description: 'The flag tells if regulation is enabled. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &regulatingcontrol_-_properties_-_owner_-_items_-_anyof    
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
    mode:    
      description: 'The regulating control mode presently available.  This specification allows for determining the kind of regulation without need for obtaining the units from a schedule. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *regulatingcontrol_-_properties_-_owner_-_items_-_anyof    
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
    targetDeadband:    
      description: 'This is a deadband used with discrete control to avoid excessive update of controls like tap changers and shunt compensator banks while regulating. The units of those appropriate for the mode. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    targetValue:    
      description: 'The target value specified for case input.   This value can be used for the target value without the use of schedules. The value has the units appropriate to the mode attribute. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    targetValueUnitMultiplier:    
      description: 'Specify the multiplier for used for the targetValue. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be RegulatingControl'    
      enum:    
        - RegulatingControl    
      type: Property    
  required: []    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
Nicht verfügbar das Beispiel eines RegulatingControls im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel eines RegulatingControls im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel eines RegulatingControls im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel eines RegulatingControls im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
