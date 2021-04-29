Entität: GovGAST2  
=================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovGAST2/LICENSE.md)  
Globale Beschreibung: **Abgeleitet aus CIM-Datenmodellen. Gasturbinenmodell.**  

## Liste der Eigenschaften  

- `a`: Ventil-Stellungsregler (A). Voreinstellung: 0.0  - `address`: Die Postanschrift  - `af1`: Abgastemperatur Parameter (Af1).  Einheit = pro Einheit Temperatur.  Basierend auf der Temperatur in Grad C. Voreinstellung: 0.0  - `af2`: Koeffizient gleich 0,5(1-Geschwindigkeit) (Af2). Voreinstellung: 0,0  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `b`: Ventil-Stellungsregler (B). Voreinstellung: 0,0  - `bf1`: (Bf1).  Bf1 = E(1-w), wobei E (Geschwindigkeitsempfindlichkeitskoeffizient) 0,55 bis 0,65 x Tr beträgt.  Einheit = pro Temperatureinheit.  Bezogen auf die Temperatur in Grad C. Voreinstellung: 0,0  - `bf2`: Turbinen-Drehmomentkoeffizient K (abhängig vom Heizwert des Brennstoffstroms in der Brennkammer) (Bf2). Voreinstellung: 0,0  - `c`: Ventil-Stellungsregler (C). Voreinstellung: 0,0  - `cf2`: Koeffizient, der den Kraftstofffluss definiert, wenn die Leistung 0 % beträgt (Cf2).  Synchron, aber keine Leistung.  Typischerweise 0,23 x K (23 % Brennstofffluss). Voreinstellung: 0,0  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `ecr`: Zeitverzögerung der Verbrennungsreaktion (Ecr). Voreinstellung: 0  - `etd`: Turbinen- und Abgasverzögerung (Etd). Voreinstellung: 0  - `id`: Eindeutiger Bezeichner der Entität  - `k3`: Verhältnis der Brennstoffanpassung (K3). Voreinstellung: 0,0  - `k4`: Verstärkung des Strahlungsschutzes (K4). Voreinstellung: 0,0  - `k5`: Verstärkung des Strahlungsschutzes (K5). Voreinstellung: 0,0  - `k6`: Minimaler Kraftstoffdurchfluss (K6). Voreinstellung: 0,0  - `kf`: Rückmeldung des Kraftstoffsystems (Kf). Voreinstellung: 0.0  - `location`:   - `mwbase`: Basis für Leistungswerte (MWbase) (> 0).  Einheit = MW. Voreinstellung: 0,0  - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `t`: Zeitkonstante der Brennstoffsteuerung (T). Voreinstellung: 0  - `t3`: Zeitkonstante des Strahlungsschutzes (T3). Voreinstellung: 0  - `t4`: Thermoelement-Zeitkonstante (T4). Voreinstellung: 0  - `t5`: Zeitkonstante der Temperaturregelung (T5). Voreinstellung: 0  - `tc`: Temperaturregelung (Tc).  Einheit = [SYMBOL ENTFERNT]F oder [SYMBOL ENTFERNT]C abhängig von den Konstanten Af1 und Bf1. Voreinstellung: 0,0  - `tcd`: Zeitkonstante der Verdichterentladung (Tcd). Voreinstellung: 0  - `tf`: Zeitkonstante des Kraftstoffsystems (Tf). Voreinstellung: 0  - `tmax`: Maximale Turbinengrenze (Tmax). Voreinstellung: 0,0  - `tmin`: Minimale Turbinengrenze (Tmin). Voreinstellung: 0.0  - `tr`: Nenntemperatur (Tr).  Einheit = [SYMBOL ENTFERNT]C abhängig von den Parametern Af1 und Bf1. Voreinstellung: 0,0  - `trate`: Turbinenleistung (Trate).  Einheit = MW. Voreinstellung: 0,0  - `tt`: Integrationsrate des Temperaturreglers (Tt). Voreinstellung: 0  - `type`: NGSI-Typ. Es muss GovGAST2 sein  - `w`: Reglerverstärkung (1/Droop) bei Turbinenleistung (W). Voreinstellung: 0.0  - `x`: Reglervorlaufzeitkonstante (X). Voreinstellung: 0  - `y`: Verzögerungszeitkonstante des Reglers (Y) (>0). Voreinstellung: 0  - `z`: Reglermodus (Z). true = Droop false = ISO. Voreinstellung: Falsch    
Erforderliche Eigenschaften  
Dieses Datenmodell ist eine direkte Umsetzung des Common Information Model (CIM), das durch die Norm IEC61970 spezifiziert ist, in Smart Data Models. Die Python-Klassen, auf denen dieses Modell basiert, wurden von diesen Einrichtungen entwickelt Institut für Automatisierung komplexer Stromversorgungssysteme (ACS), EON Energy Research Center (EONERC) und RWTH Aachen, Deutschland. einige Eigenschaften können einen falschen Typ haben. Dies war der Fall, bitte melden Sie einen Fehler oder senden Sie eine E-Mail an alberto.abella@fiware.org  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GovGAST2:    
  description: 'Adapted from CIM data models. Gas turbine model.'    
  properties:    
    a:    
      description: 'Valve positioner (A). Default: 0.0'    
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
    af1:    
      description: 'Exhaust temperature Parameter (Af1).  Unit = per unit temperature.  Based on temperature in degrees C. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    af2:    
      description: 'Coefficient equal to 0.5(1-speed) (Af2). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    b:    
      description: 'Valve positioner (B). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    bf1:    
      description: '(Bf1).  Bf1 = E(1-w) where E (speed sensitivity coefficient) is 0.55 to 0.65 x Tr.  Unit = per unit temperature.  Based on temperature in degrees C. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    bf2:    
      description: 'Turbine Torque Coefficient K (depends on heating value of fuel stream in combustion chamber) (Bf2). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    c:    
      description: 'Valve positioner (C). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    cf2:    
      description: 'Coefficient defining fuel flow where power output is 0% (Cf2).  Synchronous but no output.  Typically 0.23 x K (23% fuel flow). Default: 0.0'    
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
    ecr:    
      description: 'Combustion reaction time delay (Ecr). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    etd:    
      description: 'Turbine and exhaust delay (Etd). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &govgast2_-_properties_-_owner_-_items_-_anyof    
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
    k3:    
      description: 'Ratio of Fuel Adjustment (K3). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    k4:    
      description: 'Gain of radiation shield (K4). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    k5:    
      description: 'Gain of radiation shield (K5). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    k6:    
      description: 'Minimum fuel flow (K6). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kf:    
      description: 'Fuel system feedback (Kf). Default: 0.0'    
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
      description: 'Base for power values (MWbase) (> 0).  Unit = MW. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *govgast2_-_properties_-_owner_-_items_-_anyof    
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
    t:    
      description: 'Fuel Control Time Constant (T). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t3:    
      description: 'Radiation shield time constant (T3). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t4:    
      description: 'Thermocouple time constant (T4). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t5:    
      description: 'Temperature control time constant (T5). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tc:    
      description: 'Temperature control (Tc).  Unit = [SYMBOL REMOVED]F or [SYMBOL REMOVED]C depending on constants Af1 and Bf1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tcd:    
      description: 'Compressor discharge time constant (Tcd). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tf:    
      description: 'Fuel system time constant (Tf). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tmax:    
      description: 'Maximum Turbine limit (Tmax). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tmin:    
      description: 'Minimum Turbine limit (Tmin). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tr:    
      description: 'Rated temperature (Tr).  Unit = [SYMBOL REMOVED]C depending on parameters Af1 and Bf1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    trate:    
      description: 'Turbine rating (Trate).  Unit = MW. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tt:    
      description: 'Temperature controller integration rate (Tt). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be GovGAST2'    
      enum:    
        - GovGAST2    
      type: Property    
    w:    
      description: 'Governor gain (1/droop) on turbine rating (W). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    x:    
      description: 'Governor lead time constant (X). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    y:    
      description: 'Governor lag time constant (Y) (>0). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    z:    
      description: 'Governor mode (Z). true = Droop false = ISO. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
Nicht verfügbar das Beispiel eines GovGAST2 im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel eines GovGAST2 im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel eines GovGAST2 im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel eines GovGAST2 im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
