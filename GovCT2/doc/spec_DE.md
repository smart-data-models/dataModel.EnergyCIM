Entität: GovCT2  
===============  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovCT2/LICENSE.md)  
Globale Beschreibung: **Abgeleitet aus CIM-Datenmodellen. Allgemeines Reglermodell mit frequenzabhängiger Brennstoffflussgrenze.  Dieses Modell ist eine Modifikation des GovCT1Modells, um die frequenzabhängige Kraftstoffdurchflussgrenze eines bestimmten Gasturbinenherstellers darzustellen.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `aset`: Sollwert des Beschleunigungsbegrenzers (Aset).  Einheit = VE/sec.  Typischer Wert = 10. Voreinstellung: 0.0  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `db`: Totzone des Drehzahlreglers in pro Geschwindigkeitseinheit (db).  In der Mehrzahl der Anwendungen wird empfohlen, diesen Wert auf Null zu setzen.  Typischer Wert = 0. Voreinstellung: 0.0  - `description`: Eine Beschreibung dieses Artikels  - `dm`: Drehzahl-Empfindlichkeitskoeffizient (Dm).  Dm kann entweder die Veränderung der Motorleistung mit der Drehzahl oder die Veränderung der maximalen Leistungsfähigkeit mit der Drehzahl darstellen.  Wenn er positiv ist, beschreibt er die fallende Steigung der Motordrehzahl-Leistungs-Kennlinie bei steigender Drehzahl. Eine leicht fallende Kennlinie ist typisch für Hubkolbenmotoren und einige aero-derivative Turbinen.  Ist sie negativ, wird angenommen, dass die Motorleistung von der Drehzahl unbeeinflusst bleibt, aber der maximal zulässige Kraftstoffdurchsatz mit fallender Drehzahl sinkt. Dies ist charakteristisch für einwellige Industrieturbinen aufgrund von Abgastemperaturgrenzen.  Typischer Wert = 0. Voreinstellung: 0.0  - `flim1`: Frequenzschwelle 1 (Flim1).  Einheit = Hz.  Typischer Wert = 59. Voreinstellung: 0.0  - `flim10`: Frequenzschwelle 10 (Flim10).  Einheit = Hz.  Typischer Wert = 0. Voreinstellung: 0.0  - `flim2`: Frequenzschwelle 2 (Flim2).  Einheit = Hz.  Typischer Wert = 0. Voreinstellung: 0.0  - `flim3`: Frequenzschwelle 3 (Flim3).  Einheit = Hz.  Typischer Wert = 0. Voreinstellung: 0.0  - `flim4`: Frequenzschwelle 4 (Flim4).  Einheit = Hz.  Typischer Wert = 0. Voreinstellung: 0.0  - `flim5`: Frequenzschwelle 5 (Flim5).  Einheit = Hz.  Typischer Wert = 0. Voreinstellung: 0.0  - `flim6`: Frequenzschwelle 6 (Flim6).  Einheit = Hz.  Typischer Wert = 0. Voreinstellung: 0.0  - `flim7`: Frequenzschwelle 7 (Flim7).  Einheit = Hz.  Typischer Wert = 0. Voreinstellung: 0.0  - `flim8`: Frequenzschwelle 8 (Flim8).  Einheit = Hz.  Typischer Wert = 0. Voreinstellung: 0.0  - `flim9`: Frequenzschwelle 9 (Flim9).  Einheit = Hz.  Typischer Wert = 0. Voreinstellung: 0.0  - `id`: Eindeutiger Bezeichner der Entität  - `ka`: Beschleunigungsbegrenzer Verstärkung (Ka).  Typischer Wert = 10. Voreinstellung: 0.0  - `kdgov`: Verstärkung der Reglerableitung (Kdgov).  Typischer Wert = 0. Voreinstellung: 0.0  - `kigov`: Integralverstärkung des Reglers (Kigov).  Typischer Wert = 0,45. Voreinstellung: 0.0  - `kiload`: Lastbegrenzer-Integralverstärkung für PI-Regler (Kiload).  Typischer Wert = 1. Voreinstellung: 0.0  - `kimw`: Verstärkung des Leistungsreglers (Reset) (Kimw).  Der Standardwert von 0,01 entspricht einer Nachstellzeit von 100 Sekunden.  Ein Wert von 0,001 entspricht einem relativ langsam wirkenden Lastregler.  Typischer Wert = 0. Voreinstellung: 0,0  - `kpgov`: Proportionalverstärkung des Reglers (Kpgov).  Typischer Wert = 4. Voreinstellung: 0.0  - `kpload`: Lastbegrenzer-Proportionalverstärkung für PI-Regler (Kpload).  Typischer Wert = 1. Voreinstellung: 0.0  - `kturb`: Turbinenverstärkung (Kturb).  Typischer Wert = 1,9168. Voreinstellung: 0,0  - `ldref`: Lastbegrenzer-Sollwert (Ldref).  Typischer Wert = 1. Voreinstellung: 0.0  - `location`:   - `maxerr`: Maximalwert für Drehzahlfehlersignal (Maxerr).  Typischer Wert = 1. Voreinstellung: 0.0  - `minerr`: Minimaler Wert für das Drehzahlfehlersignal (Minerr).  Typischer Wert = -1. Voreinstellung: 0.0  - `mwbase`: Basis für Leistungswerte (MWbase) (> 0).  Einheit = MW. Voreinstellung: 0,0  - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `plim1`: Leistungsgrenze 1 (Plim1).  Typischer Wert = 0,8325. Voreinstellung: 0,0  - `plim10`: Leistungsgrenze 10 (Plim10).  Typischer Wert = 0. Voreinstellung: 0.0  - `plim2`: Leistungsgrenze 2 (Plim2).  Typischer Wert = 0. Voreinstellung: 0.0  - `plim3`: Leistungsgrenze 3 (Plim3).  Typischer Wert = 0. Voreinstellung: 0.0  - `plim4`: Leistungsgrenze 4 (Plim4).  Typischer Wert = 0. Voreinstellung: 0.0  - `plim5`: Leistungsgrenze 5 (Plim5).  Typischer Wert = 0. Voreinstellung: 0.0  - `plim6`: Leistungsgrenze 6 (Plim6).  Typischer Wert = 0. Voreinstellung: 0.0  - `plim7`: Leistungsgrenze 7 (Plim7).  Typischer Wert = 0. Voreinstellung: 0.0  - `plim8`: Leistungsgrenze 8 (Plim8).  Typischer Wert = 0. Voreinstellung: 0.0  - `plim9`: Leistungsgrenze 9 (Plim9).  Typischer Wert = 0. Voreinstellung: 0.0  - `prate`: Rampenrate für frequenzabhängige Leistungsbegrenzung (Prate).  Typischer Wert = 0,017. Voreinstellung: 0,0  - `r`: Permanenter Durchhang (R).  Typischer Wert = 0,05. Voreinstellung: 0,0  - `rclose`: Minimale Ventilschließrate (Rclose).  Einheit = VE/sec.  Typischer Wert = -99. Voreinstellung: 0.0  - `rdown`: Maximale Rate der Lastgrenzensenkung (Rdown).  Typischer Wert = -99. Voreinstellung: 0,0  - `ropen`: Maximale Ventilöffnungsrate (Ropen).  Einheit = VE/sec.  Typischer Wert = 99. Voreinstellung: 0.0  - `rselect`: Rückführsignal für P-Bereich (Rselect).  Typischer Wert = electricalPower. Voreinstellung: Keine  - `rup`: Maximale Rate der Lastgrenzenerhöhung (Rup).  Typischer Wert = 99. Voreinstellung: 0.0  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `ta`: Zeitkonstante des Beschleunigungsbegrenzers (Ta).  Typischer Wert = 1. Voreinstellung: 0  - `tact`: Aktor-Zeitkonstante (Tact).  Typischer Wert = 0,4. Voreinstellung: 0  - `tb`: Verzögerungszeitkonstante der Turbine (Tb).  Typischer Wert = 0,1. Voreinstellung: 0  - `tc`: Turbinenvorlaufzeitkonstante (Tc).  Typischer Wert = 0. Voreinstellung: 0  - `tdgov`: Zeitkonstante des Reglervorlaufs (Tdgov).  Typischer Wert = 1. Voreinstellung: 0  - `teng`: Transportzeitverzögerung für Dieselmotoren, die bei der Darstellung von Dieselmotoren verwendet wird, bei denen es eine kleine, aber messbare Transportverzögerung zwischen einer Änderung der Kraftstoffdurchflusseinstellung und der Entwicklung des Drehmoments (Teng) gibt.  Teng sollte in allen außer speziellen Fällen, in denen diese Transportverzögerung von besonderer Bedeutung ist, Null sein.  Typischer Wert = 0. Voreinstellung: 0  - `tfload`: Lastbegrenzer-Zeitkonstante (Tfload).  Typischer Wert = 3. Voreinstellung: 0  - `tpelec`: Zeitkonstante des elektrischen Leistungswandlers (Tpelec).  Typischer Wert = 2,5. Voreinstellung: 0  - `tsa`: Vorlaufzeitkonstante der Temperaturerfassung (Tsa).  Typischer Wert = 0. Voreinstellung: 0  - `tsb`: Verzögerungszeitkonstante der Temperaturerfassung (Tsb).  Typischer Wert = 50. Voreinstellung: 0  - `type`: NGSI-Typ. Es muss GovCT2 sein  - `vmax`: Maximale Ventilstellungsgrenze (Vmax).  Typischer Wert = 1. Voreinstellung: 0.0  - `vmin`: Minimale Ventilstellungsgrenze (Vmin).  Typischer Wert = 0,175. Voreinstellung: 0.0  - `wfnl`: Kraftstofffluss ohne Last (Wfnl).  Typischer Wert = 0,187. Voreinstellung: 0,0  - `wfspd`: Schalter für die Kraftstoffquellenkennlinie, um zu erkennen, dass der Kraftstoffdurchfluss bei einem bestimmten Kraftstoffventilhub proportional zur Motordrehzahl sein kann (Wfspd). true = Kraftstoffdurchfluss proportional zur Drehzahl (für einige Gasturbinen und Dieselmotoren mit Verdrängereinspritzdüsen) false = Kraftstoffregelsystem hält den Kraftstoffdurchfluss unabhängig von der Motordrehzahl. Typischer Wert = false. Voreinstellung: False    
Erforderliche Eigenschaften  
Dieses Datenmodell ist eine direkte Umsetzung des Common Information Model (CIM), das durch die Norm IEC61970 spezifiziert ist, in Smart Data Models. Die Python-Klassen, auf denen dieses Modell basiert, wurden von diesen Einrichtungen entwickelt Institut für Automatisierung komplexer Stromversorgungssysteme (ACS), EON Energy Research Center (EONERC) und RWTH Aachen, Deutschland. einige Eigenschaften können einen falschen Typ haben. Dies war der Fall, bitte melden Sie einen Fehler oder senden Sie eine E-Mail an alberto.abella@fiware.org  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GovCT2:    
  description: 'Adapted from CIM data models. General governor model with frequency-dependent fuel flow limit.  This model is a modification of the GovCT1model in order to represent the frequency-dependent fuel flow limit of a specific gas turbine manufacturer.'    
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
    aset:    
      description: 'Acceleration limiter setpoint (Aset).  Unit = PU/sec.  Typical Value = 10. Default: 0.0'    
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
    db:    
      description: 'Speed governor dead band in per unit speed (db).  In the majority of applications, it is recommended that this value be set to zero.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    description:    
      description: 'A description of this item'    
      type: Property    
    dm:    
      description: 'Speed sensitivity coefficient (Dm).  Dm can represent either the variation of the engine power with the shaft speed or the variation of maximum power capability with shaft speed.  If it is positive it describes the falling slope of the engine speed verses power characteristic as speed increases. A slightly falling characteristic is typical for reciprocating engines and some aero-derivative turbines.  If it is negative the engine power is assumed to be unaffected by the shaft speed, but the maximum permissible fuel flow is taken to fall with falling shaft speed. This is characteristic of single-shaft industrial turbines due to exhaust temperature limits.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    flim1:    
      description: 'Frequency threshold 1 (Flim1).  Unit = Hz.  Typical Value = 59. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    flim10:    
      description: 'Frequency threshold 10 (Flim10).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    flim2:    
      description: 'Frequency threshold 2 (Flim2).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    flim3:    
      description: 'Frequency threshold 3 (Flim3).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    flim4:    
      description: 'Frequency threshold 4 (Flim4).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    flim5:    
      description: 'Frequency threshold 5 (Flim5).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    flim6:    
      description: 'Frequency threshold 6 (Flim6).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    flim7:    
      description: 'Frequency threshold 7 (Flim7).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    flim8:    
      description: 'Frequency threshold 8 (Flim8).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    flim9:    
      description: 'Frequency threshold 9 (Flim9).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &govct2_-_properties_-_owner_-_items_-_anyof    
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
    ka:    
      description: 'Acceleration limiter Gain (Ka).  Typical Value = 10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kdgov:    
      description: 'Governor derivative gain (Kdgov).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kigov:    
      description: 'Governor integral gain (Kigov).  Typical Value = 0.45. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kiload:    
      description: 'Load limiter integral gain for PI controller (Kiload).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kimw:    
      description: 'Power controller (reset) gain (Kimw).  The default value of 0.01 corresponds to a reset time of 100 seconds.  A value of 0.001 corresponds to a relatively slow acting load controller.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kpgov:    
      description: 'Governor proportional gain (Kpgov).  Typical Value = 4. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kpload:    
      description: 'Load limiter proportional gain for PI controller (Kpload).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kturb:    
      description: 'Turbine gain (Kturb).  Typical Value = 1.9168. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ldref:    
      description: 'Load limiter reference value (Ldref).  Typical Value = 1. Default: 0.0'    
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
    maxerr:    
      description: 'Maximum value for speed error signal (Maxerr).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    minerr:    
      description: 'Minimum value for speed error signal (Minerr).  Typical Value = -1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
        anyOf: *govct2_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    plim1:    
      description: 'Power limit 1 (Plim1).  Typical Value = 0.8325. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    plim10:    
      description: 'Power limit 10 (Plim10).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    plim2:    
      description: 'Power limit 2 (Plim2).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    plim3:    
      description: 'Power limit 3 (Plim3).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    plim4:    
      description: 'Power limit 4 (Plim4).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    plim5:    
      description: 'Power limit 5 (Plim5).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    plim6:    
      description: 'Power limit 6 (Plim6).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    plim7:    
      description: 'Power limit 7 (Plim7).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    plim8:    
      description: 'Power limit 8 (Plim8).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    plim9:    
      description: 'Power Limit 9 (Plim9).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    prate:    
      description: 'Ramp rate for frequency-dependent power limit (Prate).  Typical Value = 0.017. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    r:    
      description: 'Permanent droop (R).  Typical Value = 0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rclose:    
      description: 'Minimum valve closing rate (Rclose).  Unit = PU/sec.  Typical Value = -99. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rdown:    
      description: 'Maximum rate of load limit decrease (Rdown).  Typical Value = -99. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ropen:    
      description: 'Maximum valve opening rate (Ropen).  Unit = PU/sec.  Typical Value = 99. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rselect:    
      description: 'Feedback signal for droop (Rselect).  Typical Value = electricalPower. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rup:    
      description: 'Maximum rate of load limit increase (Rup).  Typical Value = 99. Default: 0.0'    
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
      description: 'Acceleration limiter time constant (Ta).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tact:    
      description: 'Actuator time constant (Tact).  Typical Value = 0.4. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tb:    
      description: 'Turbine lag time constant (Tb).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tc:    
      description: 'Turbine lead time constant (Tc).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tdgov:    
      description: 'Governor derivative controller time constant (Tdgov).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    teng:    
      description: 'Transport time delay for diesel engine used in representing diesel engines where there is a small but measurable transport delay between a change in fuel flow setting and the development of torque (Teng).  Teng should be zero in all but special cases where this transport delay is of particular concern.  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tfload:    
      description: 'Load Limiter time constant (Tfload).  Typical Value = 3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tpelec:    
      description: 'Electrical power transducer time constant (Tpelec).  Typical Value = 2.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tsa:    
      description: 'Temperature detection lead time constant (Tsa).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tsb:    
      description: 'Temperature detection lag time constant (Tsb).  Typical Value = 50. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be GovCT2'    
      enum:    
        - GovCT2    
      type: Property    
    vmax:    
      description: 'Maximum valve position limit (Vmax).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vmin:    
      description: 'Minimum valve position limit (Vmin).  Typical Value = 0.175. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    wfnl:    
      description: 'No load fuel flow (Wfnl).  Typical Value = 0.187. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    wfspd:    
      description: 'Switch for fuel source characteristic to recognize that fuel flow, for a given fuel valve stroke, can be proportional to engine speed (Wfspd). true = fuel flow proportional to speed (for some gas turbines and diesel engines with positive displacement fuel injectors) false = fuel control system keeps fuel flow independent of engine speed. Typical Value = false. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
Nicht verfügbar das Beispiel eines GovCT2 im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel eines GovCT2 im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel eines GovCT2 im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel eines GovCT2 im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
