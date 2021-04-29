Entität: GovHydroWEH  
====================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovHydroWEH/LICENSE.md)  
Globale Beschreibung: **Abgeleitet aus CIM-Datenmodellen. Woodward Electric Hydro Governor Model.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `db`: Geschwindigkeit Totzone (db). Standard: 0.0  - `description`: Eine Beschreibung dieses Artikels  - `dicn`: Wert, der es dem Integralregler erlaubt, über die Gate-Grenzen hinaus zu fahren (Dicn). Voreinstellung: 0.0  - `dpv`: Wert, der es der Pilotventilsteuerung erlaubt, über die Schiebergrenzen hinaus zu fahren (Dpv). Voreinstellung: 0.0  - `dturb`: Dämpfungsfaktor der Turbine (Dturb).  Einheit = Delta P (PU der MW-Basis) / Delta Drehzahl (PU). Voreinstellung: 0,0  - `feedbackSignal`: Auswahl des Rückmeldesignals (Sw). true = PID-Ausgang (wenn R-Perm-Gate=droop und R-Perm-Pe=0) false = Elektrische Leistung (wenn R-Perm-Gate=0 und R-Perm-Pe=droop) oder false = Torposition (wenn R-Perm-Gate=droop und R-Perm-Pe=0). Voreinstellung: False  - `fl1`: Durchfluss Tor 1 (Fl1).  Durchflusswert für Gate-Positionspunkt 1 für die Lookup-Tabelle, die den Wasserdurchfluss durch die Turbine in Abhängigkeit von der Gate-Position darstellt, um einen stationären Durchfluss zu erzeugen. Voreinstellung: 0.0  - `fl2`: Durchfluss Tor 2 (Fl2).  Durchflusswert für Gate-Positionspunkt 2 für die Lookup-Tabelle, die den Wasserdurchfluss durch die Turbine in Abhängigkeit von der Gate-Position darstellt, um einen stationären Durchfluss zu erzeugen. Voreinstellung: 0.0  - `fl3`: Durchfluss Tor 3 (Fl3).  Durchflusswert für Gate-Positionspunkt 3 für die Lookup-Tabelle, die den Wasserdurchfluss durch die Turbine als Funktion der Gate-Position darstellt, um einen stationären Durchfluss zu erzeugen. Voreinstellung: 0.0  - `fl4`: Durchfluss Tor 4 (Fl4).  Durchflusswert für Gate-Positionspunkt 4 für die Lookup-Tabelle, die den Wasserdurchfluss durch die Turbine in Abhängigkeit von der Gate-Position darstellt, um einen stationären Durchfluss zu erzeugen. Voreinstellung: 0.0  - `fl5`: Durchfluss Tor 5 (Fl5).  Durchflusswert für Gate-Positionspunkt 5 für die Lookup-Tabelle, die den Wasserdurchfluss durch die Turbine in Abhängigkeit von der Gate-Position darstellt, um einen stationären Durchfluss zu erzeugen. Voreinstellung: 0.0  - `fp1`: Durchfluss P1 (Fp1).  Turbinen-Durchflusswert für Punkt 1 der Lookup-Tabelle, der die mechanische Leistung pro Einheit auf die MVA-Leistung der Maschine als Funktion des Turbinen-Durchflusses darstellt. Voreinstellung: 0,0  - `fp10`: Durchfluss P10 (Fp10).  Turbinen-Durchflusswert für Punkt 10 der Lookup-Tabelle, der die mechanische Leistung pro Einheit der Maschinenleistung MVA in Abhängigkeit vom Turbinen-Durchfluss darstellt. Voreinstellung: 0,0  - `fp2`: Durchfluss P2 (Fp2).  Turbinen-Durchflusswert für Punkt 2 der Lookup-Tabelle, der die mechanische Leistung pro Einheit auf die MVA-Leistung der Maschine als Funktion des Turbinen-Durchflusses darstellt. Voreinstellung: 0,0  - `fp3`: Durchfluss P3 (Fp3).  Turbinendurchflusswert für Punkt 3 der Nachschlagetabelle, der die mechanische Leistung pro Einheit auf die MVA-Leistung der Maschine als Funktion des Turbinendurchflusses darstellt. Voreinstellung: 0,0  - `fp4`: Durchfluss P4 (Fp4).  Turbinendurchflusswert für Punkt 4 der Nachschlagetabelle, der die mechanische Leistung pro Einheit auf die MVA-Leistung der Maschine als Funktion des Turbinendurchflusses darstellt. Voreinstellung: 0,0  - `fp5`: Durchfluss P5 (Fp5).  Turbinendurchflusswert für Punkt 5 der Nachschlagetabelle, der die mechanische Leistung pro Einheit der Maschinenleistung MVA in Abhängigkeit vom Turbinendurchfluss darstellt. Voreinstellung: 0,0  - `fp6`: Durchfluss P6 (Fp6).  Turbinen-Durchflusswert für Punkt 6 der Lookup-Tabelle, der die mechanische Leistung pro Einheit auf die MVA-Leistung der Maschine als Funktion des Turbinen-Durchflusses darstellt. Voreinstellung: 0,0  - `fp7`: Durchfluss P7 (Fp7).  Turbinendurchflusswert für Punkt 7 der Nachschlagetabelle, der die mechanische Leistung pro Einheit auf die MVA-Leistung der Maschine als Funktion des Turbinendurchflusses darstellt. Voreinstellung: 0,0  - `fp8`: Durchfluss P8 (Fp8).  Turbinen-Durchflusswert für Punkt 8 der Lookup-Tabelle, der die mechanische Leistung pro Einheit auf die MVA-Leistung der Maschine als Funktion des Turbinen-Durchflusses darstellt. Voreinstellung: 0,0  - `fp9`: Durchfluss P9 (Fp9).  Turbinen-Durchflusswert für Punkt 9 der Lookup-Tabelle, der die mechanische Leistung pro Einheit auf die MVA-Leistung der Maschine als Funktion des Turbinen-Durchflusses darstellt. Voreinstellung: 0,0  - `gmax`: Maximale Torposition (Gmax). Standard: 0.0  - `gmin`: Minimale Gate-Position (Gmin). Standard: 0.0  - `gtmxcl`: Maximale Torschließrate (Gtmxcl). Voreinstellung: 0.0  - `gtmxop`: Maximale Toröffnungsrate (Gtmxop). Voreinstellung: 0.0  - `gv1`: Tor 1 (Gv1).  Gate-Positionswert für Punkt 1 für die Lookup-Tabelle, die den Wasserdurchfluss durch die Turbine in Abhängigkeit von der Gate-Position darstellt, um einen stationären Durchfluss zu erzeugen. Standard: 0.0  - `gv2`: Tor 2 (Gv2).  Gate-Positionswert für Punkt 2 für die Lookup-Tabelle, die den Wasserdurchfluss durch die Turbine in Abhängigkeit von der Gate-Position darstellt, um einen stationären Durchfluss zu erzeugen. Standard: 0.0  - `gv3`: Tor 3 (Gv3).  Gate-Positionswert für Punkt 3 für die Lookup-Tabelle, die den Wasserdurchfluss durch die Turbine in Abhängigkeit von der Gate-Position darstellt, um einen stationären Durchfluss zu erzeugen. Standard: 0.0  - `gv4`: Tor 4 (Gv4).  Gate-Positionswert für Punkt 4 für die Lookup-Tabelle, die den Wasserdurchfluss durch die Turbine in Abhängigkeit von der Gate-Position darstellt, um einen stationären Durchfluss zu erzeugen. Standard: 0.0  - `gv5`: Tor 5 (Gv5).  Gate-Positionswert für Punkt 5 für die Lookup-Tabelle, die den Wasserdurchfluss durch die Turbine in Abhängigkeit von der Gate-Position darstellt, um einen stationären Durchfluss zu erzeugen. Standard: 0.0  - `id`: Eindeutiger Bezeichner der Entität  - `kd`: Ableitungsverstärkung des Reglers (Kd). Voreinstellung: 0.0  - `ki`: Derivativer Regler Integralverstärkung (Ki). Voreinstellung: 0,0  - `kp`: Derivative Regelverstärkung (Kp). Voreinstellung: 0,0  - `location`:   - `mwbase`: Basis für Leistungswerte (MWbase) (>0).  Einheit = MW. Voreinstellung: 0,0  - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `pmss1`: Pmss Durchfluss P1 (Pmss1).  Mechanische Leistungsabgabe Pmss für Turbinendurchfluss Punkt 1 für die Lookup-Tabelle, die die mechanische Leistung pro Einheit bei der Maschinenleistung MVA in Abhängigkeit vom Turbinendurchfluss darstellt. Voreinstellung: 0,0  - `pmss10`: Pmss Durchfluss P10 (Pmss10).  Mechanische Leistungsabgabe Pmss für den Turbinendurchfluss Punkt 10 für die Lookup-Tabelle, die die mechanische Leistung pro Einheit bei der Maschinenleistung MVA als Funktion des Turbinendurchflusses darstellt. Voreinstellung: 0,0  - `pmss2`: Pmss Durchfluss P2 (Pmss2).  Mechanische Leistungsabgabe Pmss für Turbinendurchfluss Punkt 2 für die Lookup-Tabelle, die die mechanische Leistung pro Einheit auf die MVA-Nennleistung der Maschine in Abhängigkeit vom Turbinendurchfluss darstellt. Voreinstellung: 0,0  - `pmss3`: Pmss Durchfluss P3 (Pmss3).  Mechanische Leistungsabgabe Pmss für Turbinendurchfluss Punkt 3 für die Lookup-Tabelle, die die mechanische Leistung pro Einheit auf die MVA-Nennleistung der Maschine als Funktion des Turbinendurchflusses darstellt. Voreinstellung: 0,0  - `pmss4`: Pmss Durchfluss P4 (Pmss4).  Mechanische Leistungsabgabe Pmss für Turbinendurchfluss Punkt 4 für die Lookup-Tabelle, die die mechanische Leistung pro Einheit auf die MVA-Nennleistung der Maschine als Funktion des Turbinendurchflusses darstellt. Voreinstellung: 0,0  - `pmss5`: Pmss Durchfluss P5 (Pmss5).  Mechanische Leistungsabgabe Pmss für Turbinendurchfluss Punkt 5 für die Lookup-Tabelle, die die mechanische Leistung pro Einheit auf die MVA-Nennleistung der Maschine als Funktion des Turbinendurchflusses darstellt. Voreinstellung: 0,0  - `pmss6`: Pmss Durchfluss P6 (Pmss6).  Mechanische Leistungsabgabe Pmss für Turbinendurchfluss Punkt 6 für die Lookup-Tabelle, die die mechanische Leistung pro Einheit auf die MVA-Nennleistung der Maschine als Funktion des Turbinendurchflusses darstellt. Voreinstellung: 0,0  - `pmss7`: Pmss Durchfluss P7 (Pmss7).  Mechanische Leistungsabgabe Pmss für Turbinendurchfluss Punkt 7 für die Lookup-Tabelle, die die mechanische Leistung pro Einheit auf die MVA-Nennleistung der Maschine in Abhängigkeit vom Turbinendurchfluss darstellt. Voreinstellung: 0,0  - `pmss8`: Pmss Durchfluss P8 (Pmss8).  Mechanische Leistungsabgabe Pmss für Turbinendurchfluss Punkt 8 für die Lookup-Tabelle, die die mechanische Leistung pro Einheit auf die MVA-Nennleistung der Maschine als Funktion des Turbinendurchflusses darstellt. Voreinstellung: 0,0  - `pmss9`: Pmss Durchfluss P9 (Pmss9).  Mechanische Leistungsabgabe Pmss für Turbinendurchfluss Punkt 9 für die Lookup-Tabelle, die die mechanische Leistung pro Einheit auf die MVA-Nennleistung der Maschine als Funktion des Turbinendurchflusses darstellt. Voreinstellung: 0,0  - `rpg`: Permanenter P-Bereich für die Ausgangsrückführung des Reglers (R-Perm-Gate). Voreinstellung: 0,0  - `rpp`: Permanenter P-Bereich für die elektrische Leistungsrückführung (R-Perm-Pe). Voreinstellung: 0,0  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `td`: Zeitkonstante des Ableitungsreglers zur Begrenzung der Ableitungskennlinie jenseits einer Durchbruchsfrequenz, um eine Verstärkung des hochfrequenten Rauschens zu vermeiden (Td). Voreinstellung: 0  - `tdv`: Zeitkonstante für die Verzögerung des Verteilerventils (Tdv). Voreinstellung: 0  - `tg`: Wert, der es der Verteilerventilsteuerung erlaubt, über den Grenzwert für die Torbewegungsrate (Tg) hinaus zu fahren. Voreinstellung: 0  - `tp`: Zeitkonstante des Pilotventils für die Zeitverzögerung (Tp). Voreinstellung: 0  - `tpe`: Zeitkonstante für den elektrischen Leistungsabfall (Tpe). Voreinstellung: 0  - `tw`: Wasserträgheitszeitkonstante (Tw) (>0). Voreinstellung: 0  - `type`: NGSI-Typ. Es muss GovHydroWEH sein    
Erforderliche Eigenschaften  
Dieses Datenmodell ist eine direkte Umsetzung des Common Information Model (CIM), das durch die Norm IEC61970 spezifiziert ist, in Smart Data Models. Die Python-Klassen, auf denen dieses Modell basiert, wurden von diesen Einrichtungen entwickelt Institut für Automatisierung komplexer Stromversorgungssysteme (ACS), EON Energy Research Center (EONERC) und RWTH Aachen, Deutschland. einige Eigenschaften können einen falschen Typ haben. Dies war der Fall, bitte melden Sie einen Fehler oder senden Sie eine E-Mail an alberto.abella@fiware.org  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GovHydroWEH:    
  description: 'Adapted from CIM data models. Woodward Electric Hydro Governor Model.'    
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
    db:    
      description: 'Speed Dead Band (db). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    description:    
      description: 'A description of this item'    
      type: Property    
    dicn:    
      description: 'Value to allow the integral controller to advance beyond the gate limits (Dicn). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    dpv:    
      description: 'Value to allow the Pilot valve controller to advance beyond the gate limits (Dpv). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    dturb:    
      description: 'Turbine damping factor (Dturb).  Unit = delta P (PU of MWbase) / delta speed (PU). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    feedbackSignal:    
      description: 'Feedback signal selection (Sw). true = PID Output (if R-Perm-Gate=droop and R-Perm-Pe=0) false = Electrical Power (if R-Perm-Gate=0 and R-Perm-Pe=droop) or false = Gate Position (if R-Perm-Gate=droop and R-Perm-Pe=0). Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fl1:    
      description: 'Flow Gate 1 (Fl1).  Flow value for gate position point 1 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fl2:    
      description: 'Flow Gate 2 (Fl2).  Flow value for gate position point 2 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fl3:    
      description: 'Flow Gate 3 (Fl3).  Flow value for gate position point 3 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fl4:    
      description: 'Flow Gate 4 (Fl4).  Flow value for gate position point 4 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fl5:    
      description: 'Flow Gate 5 (Fl5).  Flow value for gate position point 5 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fp1:    
      description: 'Flow P1 (Fp1).  Turbine Flow value for point 1 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fp10:    
      description: 'Flow P10 (Fp10).  Turbine Flow value for point 10 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fp2:    
      description: 'Flow P2 (Fp2).  Turbine Flow value for point 2 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fp3:    
      description: 'Flow P3 (Fp3).  Turbine Flow value for point 3 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fp4:    
      description: 'Flow P4 (Fp4).  Turbine Flow value for point 4 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fp5:    
      description: 'Flow P5 (Fp5).  Turbine Flow value for point 5 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fp6:    
      description: 'Flow P6 (Fp6).  Turbine Flow value for point 6 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fp7:    
      description: 'Flow P7 (Fp7).  Turbine Flow value for point 7 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fp8:    
      description: 'Flow P8 (Fp8).  Turbine Flow value for point 8 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    fp9:    
      description: 'Flow P9 (Fp9).  Turbine Flow value for point 9 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gmax:    
      description: 'Maximum Gate Position (Gmax). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gmin:    
      description: 'Minimum Gate Position (Gmin). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gtmxcl:    
      description: 'Maximum gate closing rate (Gtmxcl). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gtmxop:    
      description: 'Maximum gate opening rate (Gtmxop). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv1:    
      description: 'Gate 1 (Gv1).  Gate Position value for point 1 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv2:    
      description: 'Gate 2 (Gv2).  Gate Position value for point 2 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv3:    
      description: 'Gate 3 (Gv3).  Gate Position value for point 3 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv4:    
      description: 'Gate 4 (Gv4).  Gate Position value for point 4 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    gv5:    
      description: 'Gate 5 (Gv5).  Gate Position value for point 5 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &govhydroweh_-_properties_-_owner_-_items_-_anyof    
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
    kd:    
      description: 'Derivative controller derivative gain (Kd). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ki:    
      description: 'Derivative controller Integral gain (Ki). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kp:    
      description: 'Derivative control gain (Kp). Default: 0.0'    
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
        anyOf: *govhydroweh_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    pmss1:    
      description: 'Pmss Flow P1 (Pmss1).  Mechanical Power output Pmss for Turbine Flow point 1 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmss10:    
      description: 'Pmss Flow P10 (Pmss10).  Mechanical Power output Pmss for Turbine Flow point 10 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmss2:    
      description: 'Pmss Flow P2 (Pmss2).  Mechanical Power output Pmss for Turbine Flow point 2 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmss3:    
      description: 'Pmss Flow P3 (Pmss3).  Mechanical Power output Pmss for Turbine Flow point 3 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmss4:    
      description: 'Pmss Flow P4 (Pmss4).  Mechanical Power output Pmss for Turbine Flow point 4 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmss5:    
      description: 'Pmss Flow P5 (Pmss5).  Mechanical Power output Pmss for Turbine Flow point 5 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmss6:    
      description: 'Pmss Flow P6 (Pmss6).  Mechanical Power output Pmss for Turbine Flow point 6 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmss7:    
      description: 'Pmss Flow P7 (Pmss7).  Mechanical Power output Pmss for Turbine Flow point 7 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmss8:    
      description: 'Pmss Flow P8 (Pmss8).  Mechanical Power output Pmss for Turbine Flow point 8 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pmss9:    
      description: 'Pmss Flow P9 (Pmss9).  Mechanical Power output Pmss for Turbine Flow point 9 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rpg:    
      description: 'Permanent droop for governor output feedback (R-Perm-Gate). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rpp:    
      description: 'Permanent droop for electrical power feedback (R-Perm-Pe). Default: 0.0'    
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
      description: 'Derivative controller time constant to limit the derivative characteristic beyond a breakdown frequency to avoid amplification of high-frequency noise (Td). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tdv:    
      description: 'Distributive Valve time lag time constant (Tdv). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tg:    
      description: 'Value to allow the Distribution valve controller to advance beyond the gate movement rate limit (Tg). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tp:    
      description: 'Pilot Valve time lag time constant (Tp). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tpe:    
      description: 'Electrical power droop time constant (Tpe). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tw:    
      description: 'Water inertia time constant (Tw) (>0). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be GovHydroWEH'    
      enum:    
        - GovHydroWEH    
      type: Property    
  required: []    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
Nicht verfügbar das Beispiel eines GovHydroWEH im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel eines GovHydroWEH im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel eines GovHydroWEH im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel eines GovHydroWEH im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
