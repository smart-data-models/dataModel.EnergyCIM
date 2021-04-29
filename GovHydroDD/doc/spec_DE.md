Entität: GovHydroDD  
===================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovHydroDD/LICENSE.md)  
Globale Beschreibung: **Abgeleitet aus CIM-Datenmodellen. Doppelt abgeleiteter Hydroregler und Turbine.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `aturb`: Turbinenzähler-Multiplikator (Aturb) (Hinweis 3).  Typischer Wert = -1. Standard: 0.0  - `bturb`: Turbinen-Nenner-Multiplikator (Bturb) (Hinweis 3).  Typischer Wert = 0,5. Standard: 0,0  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `db1`: Beabsichtigte Totbandbreite (db1).  Einheit = Hz.  Typischer Wert = 0. Voreinstellung: 0.0  - `db2`: Ungewolltes Totband (db2).  Einheit = MW.  Typischer Wert = 0. Voreinstellung: 0.0  - `description`: Eine Beschreibung dieses Artikels  - `eps`: Beabsichtigte db-Hysterese (eps).  Einheit = Hz.  Typischer Wert = 0. Voreinstellung: 0.0  - `gmax`: Maximale Toröffnung (Gmax).  Typischer Wert = 0. Voreinstellung: 0.0  - `gmin`: Minimale Toröffnung (Gmin).  Typischer Wert = 0. Voreinstellung: 0.0  - `gv1`: Nichtlinearer Verstärkungspunkt 1, PU gv (Gv1).  Typischer Wert = 0. Voreinstellung: 0.0  - `gv2`: Nichtlinearer Verstärkungspunkt 2, PU gv (Gv2).  Typischer Wert = 0. Voreinstellung: 0.0  - `gv3`: Nichtlinearer Verstärkungspunkt 3, PU gv (Gv3).  Typischer Wert = 0. Voreinstellung: 0.0  - `gv4`: Nichtlinearer Verstärkungspunkt 4, PU gv (Gv4).  Typischer Wert = 0. Voreinstellung: 0.0  - `gv5`: Nichtlinearer Verstärkungspunkt 5, PU gv (Gv5).  Typischer Wert = 0. Voreinstellung: 0.0  - `gv6`: Nichtlinearer Verstärkungspunkt 6, PU gv (Gv6).  Typischer Wert = 0. Voreinstellung: 0.0  - `id`: Eindeutiger Bezeichner der Entität  - `inputSignal`: Eingangssignalschalter (Flag). true = Pe-Eingang wird verwendet false = Rückmeldung wird von CV empfangen. Flag ist normalerweise abhängig von Tt.  Wenn Tf Null ist, wird Flag auf false gesetzt. Wenn Tf nicht Null ist, wird Flag auf true gesetzt.   Typischer Wert = true. Voreinstellung: Falsch  - `k1`: Einzelne Ableitungsverstärkung (K1).  Typischer Wert = 3,6. Voreinstellung: 0,0  - `k2`: Doppelte Ableitungsverstärkung (K2).  Typischer Wert = 0,2. Voreinstellung: 0,0  - `kg`: Gate-Servo-Verstärkung (Kg).  Typischer Wert = 3. Voreinstellung: 0.0  - `ki`: Integrale Verstärkung (Ki).  Typischer Wert = 1. Voreinstellung: 0,0  - `location`:   - `mwbase`: Basis für Leistungswerte (MWbase) (>0).  Einheit = MW. Voreinstellung: 0,0  - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `pgv1`: Nichtlinearer Verstärkungspunkt 1, PU-Leistung (Pgv1).  Typischer Wert = 0. Voreinstellung: 0.0  - `pgv2`: Nichtlinearer Verstärkungspunkt 2, PU-Leistung (Pgv2).  Typischer Wert = 0. Voreinstellung: 0.0  - `pgv3`: Nichtlinearer Verstärkungspunkt 3, PU-Leistung (Pgv3).  Typischer Wert = 0. Voreinstellung: 0.0  - `pgv4`: Nichtlinearer Verstärkungspunkt 4, PU-Leistung (Pgv4).  Typischer Wert = 0. Voreinstellung: 0.0  - `pgv5`: Nichtlinearer Verstärkungspunkt 5, PU-Leistung (Pgv5).  Typischer Wert = 0. Voreinstellung: 0.0  - `pgv6`: Nichtlinearer Verstärkungspunkt 6, PU-Leistung (Pgv6).  Typischer Wert = 0. Voreinstellung: 0.0  - `pmax`: Maximale Toröffnung, VE der MW-Basis (Pmax).  Typischer Wert = 1. Voreinstellung: 0,0  - `pmin`: Minimale Toröffnung, PU der MW-Basis (Pmin).  Typischer Wert = 0. Voreinstellung: 0.0  - `r`: Steady State Droop (R).  Typischer Wert = 0,05. Voreinstellung: 0,0  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `td`: Eingangsfilter-Zeitkonstante (Td).  Typischer Wert = 0. Voreinstellung: 0  - `tf`: Auswaschzeitkonstante (Tf).  Typischer Wert = 0,1. Voreinstellung: 0  - `tp`: Gate-Servo-Zeitkonstante (Tp).  Typischer Wert = 0,35. Voreinstellung: 0  - `tt`: Zeitkonstante der Leistungsrückführung (Tt).  Typischer Wert = 0,02. Voreinstellung: 0  - `tturb`: Turbinenzeitkonstante (Tturb) (Hinweis 3).  Typischer Wert = 0,8. Voreinstellung: 0  - `type`: NGSI-Typ. Es muss GovHydroDD sein  - `velcl`: Maximale Torschließgeschwindigkeit (Velcl).  Einheit = VE/sec.  Typischer Wert = -0,14. Voreinstellung: 0.0  - `velop`: Maximale Toröffnungsgeschwindigkeit (Velop).  Einheit = VE/sec.  Typischer Wert = 0,09. Voreinstellung: 0.0    
Erforderliche Eigenschaften  
Dieses Datenmodell ist eine direkte Umsetzung des Common Information Model (CIM), das durch die Norm IEC61970 spezifiziert ist, in Smart Data Models. Die Python-Klassen, auf denen dieses Modell basiert, wurden von diesen Einrichtungen entwickelt Institut für Automatisierung komplexer Stromversorgungssysteme (ACS), EON Energy Research Center (EONERC) und RWTH Aachen, Deutschland. einige Eigenschaften können einen falschen Typ haben. Dies war der Fall, bitte melden Sie einen Fehler oder senden Sie eine E-Mail an alberto.abella@fiware.org  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GovHydroDD:    
  description: 'Adapted from CIM data models. Double derivative hydro governor and turbine.'    
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
    aturb:    
      description: 'Turbine numerator multiplier (Aturb) (note 3).  Typical Value = -1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    bturb:    
      description: 'Turbine denominator multiplier (Bturb) (note 3).  Typical Value = 0.5. Default: 0.0'    
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
    db1:    
      description: 'Intentional dead-band width (db1).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    db2:    
      description: 'Unintentional dead-band (db2).  Unit = MW.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    description:    
      description: 'A description of this item'    
      type: Property    
    eps:    
      description: 'Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gmax:    
      description: 'Maximum gate opening (Gmax).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gmin:    
      description: 'Minimum gate opening (Gmin).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv1:    
      description: 'Nonlinear gain point 1, PU gv (Gv1).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv2:    
      description: 'Nonlinear gain point 2, PU gv (Gv2).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv3:    
      description: 'Nonlinear gain point 3, PU gv (Gv3).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv4:    
      description: 'Nonlinear gain point 4, PU gv (Gv4).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv5:    
      description: 'Nonlinear gain point 5, PU gv (Gv5).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv6:    
      description: 'Nonlinear gain point 6, PU gv (Gv6).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &govhydrodd_-_properties_-_owner_-_items_-_anyof    
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
    inputSignal:    
      description: 'Input signal switch (Flag).  true = Pe input is used false = feedback is received from CV. Flag is normally dependent on Tt.  If Tf is zero, Flag is set to false. If Tf is not zero, Flag is set to true.   Typical Value = true. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    k1:    
      description: 'Single derivative gain (K1).  Typical Value = 3.6. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    k2:    
      description: 'Double derivative gain (K2).  Typical Value = 0.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kg:    
      description: 'Gate servo gain (Kg).  Typical Value = 3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ki:    
      description: 'Integral gain (Ki).  Typical Value = 1. Default: 0.0'    
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
      description: 'Base for power values (MWbase) (>0).  Unit = MW. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *govhydrodd_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    pgv1:    
      description: 'Nonlinear gain point 1, PU power (Pgv1).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pgv2:    
      description: 'Nonlinear gain point 2, PU power (Pgv2).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pgv3:    
      description: 'Nonlinear gain point 3, PU power (Pgv3).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pgv4:    
      description: 'Nonlinear gain point 4, PU power (Pgv4).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pgv5:    
      description: 'Nonlinear gain point 5, PU power (Pgv5).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pgv6:    
      description: 'Nonlinear gain point 6, PU power (Pgv6).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmax:    
      description: 'Maximum gate opening, PU of MWbase (Pmax).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmin:    
      description: 'Minimum gate opening, PU of MWbase (Pmin).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    r:    
      description: 'Steady state droop (R).  Typical Value = 0.05. Default: 0.0'    
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
    td:    
      description: 'Input filter time constant (Td).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tf:    
      description: 'Washout time constant (Tf).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tp:    
      description: 'Gate servo time constant (Tp).  Typical Value = 0.35. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tt:    
      description: 'Power feedback time constant (Tt).  Typical Value = 0.02. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tturb:    
      description: 'Turbine time constant (Tturb) (note 3).  Typical Value = 0.8. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be GovHydroDD'    
      enum:    
        - GovHydroDD    
      type: Property    
    velcl:    
      description: 'Maximum gate closing velocity (Velcl).  Unit = PU/sec.  Typical Value = -0.14. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    velop:    
      description: 'Maximum gate opening velocity (Velop).  Unit = PU/sec.  Typical Value = 0.09. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
Nicht verfügbar das Beispiel einer GovHydroDD im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer GovHydroDD im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer GovHydroDD im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer GovHydroDD im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
