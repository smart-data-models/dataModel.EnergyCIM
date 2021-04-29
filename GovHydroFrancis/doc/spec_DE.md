Entität: GovHydroFrancis  
========================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovHydroFrancis/LICENSE.md)  
Globale Beschreibung: **Abgeleitet aus CIM-Datenmodellen. Detaillierte Hydroeinheit - Francis-Modell.  Mit diesem Modell lassen sich drei Arten von Reglern darstellen. Eine schematische Darstellung des hydraulischen Systems von detaillierten Hydroaggregat-Modellen, wie Francis und Pelton, wird im Diagramm DetailedHydroModelHydraulicSystem bereitgestellt.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `am`: Öffnungsquerschnitt S bei maximalem Wirkungsgrad (Am).  Typischer Wert = 0,7. Voreinstellung: 0,0  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `av0`: Fläche des Wasserschlosses (A). Einheit = m. Typischer Wert = 30. Voreinstellung: 0.0  - `av1`: Fläche des Ausgleichsbehälters (A). Einheit = m. Typischer Wert = 700. Voreinstellung: 0.0  - `bp`: Droop (Bp).  Typischer Wert = 0,05. Voreinstellung: 0,0  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `db1`: Beabsichtigte Totbandbreite (DB1).  Einheit = Hz.  Typischer Wert = 0. Voreinstellung: 0.0  - `description`: Eine Beschreibung dieses Artikels  - `etamax`: Maximaler Wirkungsgrad (EtaMax).  Typischer Wert = 1,05. Voreinstellung: 0,0  - `governorControl`: Reglersteuerungs-Flag (Cflag).  Typischer Wert = mechanicHydrolicTachoAccelerator. Voreinstellung: Keine  - `h1`: Höhe des Wasserspiegels der Ausgleichskammer in Bezug auf die Höhe der Druckleitung (H).  Einheit = m. Typischer Wert = 4. Voreinstellung: 0.0  - `h2`: Wasserspiegelhöhe des Wasserschlosses in Bezug auf die Höhe der Druckleitung (H).  Einheit = m. Typischer Wert = 40. Voreinstellung: 0.0  - `hn`: Hydraulische Nennförderhöhe (H).  Einheit = m. Typischer Wert = 250. Voreinstellung: 0.0  - `id`: Eindeutiger Bezeichner der Entität  - `kc`: Verlustkoeffizient der Druckleitung (aufgrund von Reibung) (Kc).  Typischer Wert = 0,025. Standard: 0,0  - `kg`: Verlustkoeffizient von Wassertunnel und Wasserschloss (aufgrund von Reibung) (Kg).  Typischer Wert = 0,025. Voreinstellung: 0,0  - `kt`: Auswaschverstärkung (Kt).  Typischer Wert = 0,25. Voreinstellung: 0,0  - `location`:   - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `qc0`: Leerlaufdurchfluss der Turbine bei Nennhöhe (Qc0).  Typischer Wert = 0,21. Voreinstellung: 0,0  - `qn`: Nenndurchfluss (Q). Einheit = m/s. Typischer Wert = 40. Voreinstellung: 0,0  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `ta`: Abgeleitete Verstärkung (Ta).  Typischer Wert = 3. Voreinstellung: 0  - `td`: Auswaschzeitkonstante (Td).  Typischer Wert = 3. Voreinstellung: 0  - `ts`: Gate-Servo-Zeitkonstante (Ts).  Typischer Wert = 0,5. Voreinstellung: 0  - `twnc`: Wasserträgheitszeitkonstante (Twnc).  Typischer Wert = 1. Voreinstellung: 0  - `twng`: Wassertunnel und Wasserschloss Trägheitszeitkonstante (Twng). Typischer Wert = 3. Voreinstellung: 0  - `tx`: Abgeleitete Rückkopplungsverstärkung (Tx).  Typischer Wert = 1. Voreinstellung: 0  - `type`: NGSI-Typ. Es muss GovHydroFrancis sein  - `va`: Maximale Toröffnungsgeschwindigkeit (Va).  Einheit = VE/sec.  Typischer Wert = 0,011. Voreinstellung: 0,0  - `valvmax`: Maximale Toröffnung (ValvMax).  Typischer Wert = 1. Voreinstellung: 0.0  - `valvmin`: Minimale Toröffnung (ValvMin).  Typischer Wert = 0. Voreinstellung: 0.0  - `vc`: Maximale Torschließgeschwindigkeit (Vc).  Einheit = VE/sec.  Typischer Wert = -0,011. Voreinstellung: 0.0  - `waterTunnelSurgeChamberSimulation`: Wassertunnel- und Wasserschloss-Simulation (Tflag). true = Freigabe der Wassertunnel- und Wasserschloss-Simulation false = Sperrung der Wassertunnel- und Wasserschloss-Simulation. Typischer Wert = false. Voreinstellung: False  - `zsfc`: Höhe des oberen Wasserspiegels in Bezug auf die Höhe der Druckleitung (Zsfc).  Einheit = m. Typischer Wert = 25. Voreinstellung: 0.0    
Erforderliche Eigenschaften  
Dieses Datenmodell ist eine direkte Umsetzung des Common Information Model (CIM), das durch die Norm IEC61970 spezifiziert ist, in Smart Data Models. Die Python-Klassen, auf denen dieses Modell basiert, wurden von diesen Einrichtungen entwickelt Institut für Automatisierung komplexer Stromversorgungssysteme (ACS), EON Energy Research Center (EONERC) und RWTH Aachen, Deutschland. einige Eigenschaften können einen falschen Typ haben. Dies war der Fall, bitte melden Sie einen Fehler oder senden Sie eine E-Mail an alberto.abella@fiware.org  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GovHydroFrancis:    
  description: 'Adapted from CIM data models. Detailed hydro unit - Francis model.  This model can be used to represent three types of governors. A schematic of the hydraulic system of detailed hydro unit models, like Francis and Pelton, is provided in the DetailedHydroModelHydraulicSystem diagram.'    
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
    am:    
      description: 'Opening section S at the maximum efficiency (Am).  Typical Value = 0.7. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    av0:    
      description: 'Area of the surge tank (A). Unit = m. Typical Value = 30. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    av1:    
      description: 'Area of the compensation tank (A). Unit = m. Typical Value = 700. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    bp:    
      description: 'Droop (Bp).  Typical Value = 0.05. Default: 0.0'    
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
      description: 'Intentional dead-band width (DB1).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    description:    
      description: 'A description of this item'    
      type: Property    
    etamax:    
      description: 'Maximum efficiency (EtaMax).  Typical Value = 1.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    governorControl:    
      description: 'Governor control flag (Cflag).  Typical Value = mechanicHydrolicTachoAccelerator. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    h1:    
      description: 'Head of compensation chamber water level with respect to the level of penstock (H).  Unit = m. Typical Value = 4. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    h2:    
      description: 'Head of surge tank water level with respect to the level of penstock (H).  Unit = m. Typical Value = 40. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    hn:    
      description: 'Rated hydraulic head (H).  Unit = m. Typical Value = 250. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &govhydrofrancis_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Penstock loss coefficient (due to friction) (Kc).  Typical Value = 0.025. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kg:    
      description: 'Water tunnel and surge chamber loss coefficient (due to friction) (Kg).  Typical Value = 0.025. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kt:    
      description: 'Washout gain (Kt).  Typical Value = 0.25. Default: 0.0'    
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
        anyOf: *govhydrofrancis_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    qc0:    
      description: 'No-load turbine flow at nominal head (Qc0).  Typical Value = 0.21. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    qn:    
      description: 'Rated flow (Q). Unit = m/s. Typical Value = 40. Default: 0.0'    
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
    ta:    
      description: 'Derivative gain (Ta).  Typical Value = 3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    td:    
      description: 'Washout time constant (Td).  Typical Value = 3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ts:    
      description: 'Gate servo time constant (Ts).  Typical Value = 0.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    twnc:    
      description: 'Water inertia time constant (Twnc).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    twng:    
      description: 'Water tunnel and surge chamber inertia time constant (Twng). Typical Value = 3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tx:    
      description: 'Derivative feedback gain (Tx).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be GovHydroFrancis'    
      enum:    
        - GovHydroFrancis    
      type: Property    
    va:    
      description: 'Maximum gate opening velocity (Va).  Unit = PU/sec.  Typical Value = 0.011. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    valvmax:    
      description: 'Maximum gate opening (ValvMax).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    valvmin:    
      description: 'Minimum gate opening (ValvMin).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vc:    
      description: 'Maximum gate closing velocity (Vc).  Unit = PU/sec.  Typical Value = -0.011. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    waterTunnelSurgeChamberSimulation:    
      description: 'Water tunnel and surge chamber simulation (Tflag). true = enable of water tunnel and surge chamber simulation false = inhibit of water tunnel and surge chamber simulation. Typical Value = false. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    zsfc:    
      description: 'Head of upper water level with respect to the level of penstock (Zsfc).  Unit = m.  Typical Value = 25. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
Nicht verfügbar das Beispiel eines GovHydroFrancis im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel eines GovHydroFrancis im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel eines GovHydroFrancis im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel eines GovHydroFrancis im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
