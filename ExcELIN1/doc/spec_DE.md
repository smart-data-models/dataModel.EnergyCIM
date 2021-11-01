Entität: ExcELIN1  
=================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExcELIN1/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Angelehnt an die CIM-Datenmodelle. Statisches, durch einen PI-Transformator gespeistes Erregersystem: ELIN (VATECH) - vereinfachtes Modell.  Dieses Modell stellt ein rein statisches Erregersystem dar. Ein PI-Spannungsregler gibt einen gewünschten Feldstrom-Sollwert für einen proportionalen Stromregler vor. Der Integrator des PI-Reglers hat einen Folgeeingang, um sein Signal an den aktuellen Feldstrom anzupassen.  Ein Netzstabilisator mit Leistungseingang ist im Modell enthalten.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `dataProvider`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `dpnf`: Totzone des Nachlaufreglers (Dpnf).  Typischer Wert = 0. Voreinstellung: 0.0  - `efmax`: Maximale Erregerspannung bei offenem Stromkreis (Efmax).  Typischer Wert = 5. Voreinstellung: 0,0  - `efmin`: Minimale Erregerspannung bei offenem Stromkreis (Efmin).  Typischer Wert = -5. Voreinstellung: 0,0  - `id`: Eindeutiger Bezeichner der Entität  - `ks1`: Stabilisatorverstärkung 1 (Ks1).  Typischer Wert = 0. Voreinstellung: 0.0  - `ks2`: Stabilisatorverstärkung 2 (Ks2).  Typischer Wert = 0. Voreinstellung: 0.0  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name`: Der Name dieses Artikels.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `seeAlso`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `smax`: Stabilisator-Grenzwertausgang (smax).  Typischer Wert = 0,1. Voreinstellung: 0,0  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `tfi`: Zeitkonstante des Stromwandlers (Tfi).  Typischer Wert = 0. Voreinstellung: 0  - `tnu`: Zeitkonstante der Reglerrückstellung (Tnu).  Typischer Wert = 2. Voreinstellung: 0  - `ts1`: Stabilisator-Phasenverzögerungszeitkonstante (Ts1).  Typischer Wert = 1. Voreinstellung: 0  - `ts2`: Zeitkonstante des Stabilisierungsfilters (Ts2).  Typischer Wert = 1. Voreinstellung: 0  - `tsw`: Stabilisierungsparameter (Tsw).  Typischer Wert = 3. Voreinstellung: 0  - `type`: NGSI-Typ. Es muss ExcELIN1 sein.  - `vpi`: Verstärkung des Stromreglers (Vpi).  Typischer Wert = 12,45. Voreinstellung: 0.0  - `vpnf`: Regler-Nachlaufverstärkung (Vpnf).  Typischer Wert = 2. Voreinstellung: 0,0  - `vpu`: Spannungsregler Proportionalverstärkung (Vpu).  Typischer Wert = 34,5. Voreinstellung: 0,0  - `xe`: Effektive Reaktanz des Erregertransformators (Xe) (>=0).  Xe steht für die Regelung der Transformator/Gleichrichter-Einheit.  Typischer Wert = 0,06. Voreinstellung: 0,0    
Erforderliche Eigenschaften  
Angepasst von CIM-Datenmodellen und CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Dieses Datenmodell ist eine direkte Umsetzung des Common Information Model (CIM), das durch die Norm IEC61970 spezifiziert ist, in intelligente Datenmodelle. Die Python-Klassen, auf denen dieses Modell basiert, wurden vom Institut für Automatisierung komplexer Stromversorgungssysteme (ACS), dem EON Energy Research Center (EONERC) und der RWTH Aachen, Deutschland, entwickelt. Einige Eigenschaften können einen falschen Typ haben. Sollte dies der Fall sein, melden Sie bitte einen Fehler oder senden Sie eine E-Mail an info@smartdatamodels.org.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ExcELIN1:    
  description: 'Adapted from CIM data models. Static PI transformer fed excitation system: ELIN (VATECH) - simplified model.  This model represents an all-static excitation system. A PI voltage controller establishes a desired field current set point for a proportional current controller. The integrator of the PI controller has a follow-up input to match its signal to the present field current.  A power system stabilizer with power input is included in the model.'    
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
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    dpnf:    
      description: 'Controller follow up dead band (Dpnf).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    efmax:    
      description: 'Maximum open circuit excitation voltage (Efmax).  Typical Value = 5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    efmin:    
      description: 'Minimum open circuit excitation voltage (Efmin).  Typical Value = -5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &excelin1_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    ks1:    
      description: 'Stabilizer Gain 1 (Ks1).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ks2:    
      description: 'Stabilizer Gain 2 (Ks2).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *excelin1_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
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
      x-ngsi:    
        type: Property    
    smax:    
      description: 'Stabilizer Limit Output (smax).  Typical Value = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    tfi:    
      description: 'Current transducer time constant (Tfi).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tnu:    
      description: 'Controller reset time constant (Tnu).  Typical Value = 2. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ts1:    
      description: 'Stabilizer Phase Lag Time Constant (Ts1).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ts2:    
      description: 'Stabilizer Filter Time Constant (Ts2).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tsw:    
      description: 'Stabilizer parameters (Tsw).  Typical Value = 3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be ExcELIN1'    
      enum:    
        - ExcELIN1    
      type: string    
      x-ngsi:    
        type: Property    
    vpi:    
      description: 'Current controller gain (Vpi).  Typical Value = 12.45. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vpnf:    
      description: 'Controller follow up gain (Vpnf).  Typical Value = 2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vpu:    
      description: 'Voltage controller proportional gain (Vpu).  Typical Value = 34.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    xe:    
      description: 'Excitation transformer effective reactance (Xe) (>=0).  Xe represents the regulation of the transformer/rectifier unit.  Typical Value = 0.06. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
Nicht verfügbar ist das Beispiel einer ExcELIN1 im JSON-LD Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar ist das Beispiel einer ExcELIN1 im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar ist das Beispiel einer ExcELIN1 im JSON-LD Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar ist das Beispiel einer ExcELIN1 im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
