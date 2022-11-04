<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: GovHydroWEH  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovHydroWEH/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Abgeleitet von CIM-Datenmodellen. Woodward Electric Hydro Governor Model.**  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, liegt das daran, dass es mehrere Typen oder unterschiedliche Formate/Muster haben kann</sub></sup>.  
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated[string]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified[string]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `db[number]`: Geschwindigkeit Totzone (db). Standard: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: Eine Beschreibung dieses Artikels  - `dicn[number]`: Wert, der es dem Integralregler erlaubt, über die Gate-Grenzen hinaus zu fahren (Dicn). Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dpv[number]`: Wert, der es dem Pilotventilregler erlaubt, über die Schiebergrenzen hinaus zu fahren (Dpv). Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dturb[number]`: Dämpfungsfaktor der Turbine (Dturb).  Einheit = Delta P (PU der MW-Basis) / Delta Geschwindigkeit (PU). Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `feedbackSignal[number]`: Auswahl des Rückkopplungssignals (Sw). true = PID-Ausgang (wenn R-Perm-Gate=droop und R-Perm-Pe=0) false = Elektrische Leistung (wenn R-Perm-Gate=0 und R-Perm-Pe=droop) oder false = Gate Position (wenn R-Perm-Gate=droop und R-Perm-Pe=0). Voreinstellung: Falsch  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl1[number]`: Durchfluss Tor 1 (Fl1).  Durchflusswert für Gate-Positionspunkt 1 für die Nachschlagetabelle, die den Wasserdurchfluss durch die Turbine als Funktion der Gate-Position darstellt, um einen stationären Durchfluss zu erzeugen. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl2[number]`: Durchfluss Tor 2 (Fl2).  Durchflusswert für Gate-Positionspunkt 2 für die Nachschlagetabelle, die den Wasserdurchfluss durch die Turbine als Funktion der Gate-Position darstellt, um einen stationären Durchfluss zu erzeugen. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl3[number]`: Durchfluss Tor 3 (Fl3).  Durchflusswert für Gate-Positionspunkt 3 für die Lookup-Tabelle, die den Wasserdurchfluss durch die Turbine als Funktion der Gate-Position darstellt, um einen stationären Durchfluss zu erzeugen. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl4[number]`: Durchfluss Tor 4 (Fl4).  Durchflusswert für Gate-Positionspunkt 4 für die Nachschlagetabelle, die den Wasserdurchfluss durch die Turbine als Funktion der Gate-Position darstellt, um einen stationären Durchfluss zu erzeugen. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl5[number]`: Durchfluss Tor 5 (Fl5).  Durchflusswert für Gate-Positionspunkt 5 für die Nachschlagetabelle, die den Wasserdurchfluss durch die Turbine als Funktion der Gate-Position darstellt, um einen stationären Durchfluss zu erzeugen. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp1[number]`: Durchfluss P1 (Fp1).  Turbinendurchflusswert für Punkt 1 der Nachschlagetabelle, der die mechanische Leistung pro Einheit der Maschinenleistung MVA in Abhängigkeit vom Turbinendurchfluss darstellt. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp10[number]`: Durchfluss P10 (Fp10).  Turbinendurchflusswert für Punkt 10 der Nachschlagetabelle, der die mechanische Leistung pro Einheit der Maschinenleistung MVA in Abhängigkeit vom Turbinendurchfluss darstellt. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp2[number]`: Durchfluss P2 (Fp2).  Turbinendurchflusswert für Punkt 2 der Nachschlagetabelle, der die mechanische Leistung pro Einheit der Maschinenleistung MVA in Abhängigkeit vom Turbinendurchfluss darstellt. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp3[number]`: Durchfluss P3 (Fp3).  Turbinendurchflusswert für Punkt 3 der Nachschlagetabelle, der die mechanische Leistung pro Einheit der Maschinenleistung MVA in Abhängigkeit vom Turbinendurchfluss darstellt. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp4[number]`: Durchfluss P4 (Fp4).  Turbinendurchflusswert für Punkt 4 der Nachschlagetabelle, der die mechanische Leistung pro Einheit der Maschinenleistung MVA in Abhängigkeit vom Turbinendurchfluss darstellt. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp5[number]`: Durchfluss P5 (Fp5).  Turbinendurchflusswert für Punkt 5 der Nachschlagetabelle, der die mechanische Leistung pro Einheit der Maschinenleistung MVA in Abhängigkeit vom Turbinendurchfluss darstellt. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp6[number]`: Durchfluss P6 (Fp6).  Turbinendurchflusswert für Punkt 6 der Nachschlagetabelle, der die mechanische Leistung pro Einheit der Maschinenleistung MVA in Abhängigkeit vom Turbinendurchfluss darstellt. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp7[number]`: Durchfluss P7 (Fp7).  Turbinendurchflusswert für Punkt 7 der Nachschlagetabelle, der die mechanische Leistung pro Einheit der Maschinenleistung MVA in Abhängigkeit vom Turbinendurchfluss darstellt. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp8[number]`: Durchfluss P8 (Fp8).  Turbinendurchflusswert für Punkt 8 der Nachschlagetabelle, der die mechanische Leistung pro Einheit der Maschinenleistung MVA in Abhängigkeit vom Turbinendurchfluss darstellt. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp9[number]`: Durchfluss P9 (Fp9).  Turbinendurchflusswert für Punkt 9 der Nachschlagetabelle, der die mechanische Leistung pro Einheit der Maschinenleistung MVA in Abhängigkeit vom Turbinendurchfluss darstellt. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gmax[number]`: Maximale Gate-Position (Gmax). Standardwert: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gmin[number]`: Minimale Gate-Position (Gmin). Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gtmxcl[number]`: Maximale Schließgeschwindigkeit des Tores (Gtmxcl). Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gtmxop[number]`: Maximale Toröffnungsrate (Gtmxop). Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv1[number]`: Schieber 1 (Gv1).  Gate-Positionswert für Punkt 1 der Nachschlagetabelle, die den Wasserdurchfluss durch die Turbine in Abhängigkeit von der Gate-Position darstellt, um einen gleichmäßigen Durchfluss zu erzeugen. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv2[number]`: Schieber 2 (Gv2).  Gate-Positionswert für Punkt 2 der Lookup-Tabelle, die den Wasserdurchfluss durch die Turbine in Abhängigkeit von der Gate-Position darstellt, um einen stationären Durchfluss zu erzeugen. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv3[number]`: Schieber 3 (Gv3).  Gate-Positionswert für Punkt 3 der Lookup-Tabelle, die den Wasserdurchfluss durch die Turbine in Abhängigkeit von der Gate-Position darstellt, um einen stationären Durchfluss zu erzeugen. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv4[number]`: Schieber 4 (Gv4).  Gate-Positionswert für Punkt 4 der Lookup-Tabelle, die den Wasserdurchfluss durch die Turbine in Abhängigkeit von der Gate-Position darstellt, um einen stationären Durchfluss zu erzeugen. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv5[number]`: Tor 5 (Gv5).  Gate-Positionswert für Punkt 5 der Lookup-Tabelle, die den Wasserdurchfluss durch die Turbine in Abhängigkeit von der Gate-Position darstellt, um einen stationären Durchfluss zu erzeugen. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Eindeutiger Bezeichner der Entität  - `kd[number]`: Ableitungsverstärkung des Reglers (Kd). Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ki[number]`: Derivativer Regler Integralverstärkung (Ki). Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kp[number]`: Ableitungsverstärkung (Kp). Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `mwbase[number]`: Basis für Leistungswerte (MWbase) (>0).  Einheit = MW. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: Der Name dieses Artikels.  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `pmss1[number]`: Pmss Durchfluss P1 (Pmss1).  Mechanische Ausgangsleistung Pmss für Turbinendurchfluss Punkt 1 für die Nachschlagetabelle, die die mechanische Leistung pro Einheit bei der Maschinenleistung MVA in Abhängigkeit vom Turbinendurchfluss darstellt. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss10[number]`: Pmss Durchfluss P10 (Pmss10).  Mechanische Ausgangsleistung Pmss für Turbinendurchfluss Punkt 10 für die Nachschlagetabelle, die die mechanische Leistung pro Einheit bei der Maschinenleistung MVA in Abhängigkeit vom Turbinendurchfluss darstellt. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss2[number]`: Pmss Durchfluss P2 (Pmss2).  Mechanische Ausgangsleistung Pmss für Turbinendurchfluss Punkt 2 für die Nachschlagetabelle, die die mechanische Leistung pro Einheit der Maschinenleistung MVA in Abhängigkeit vom Turbinendurchfluss darstellt. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss3[number]`: Pmss Durchfluss P3 (Pmss3).  Mechanische Leistungsabgabe Pmss für Turbinendurchfluss Punkt 3 für die Lookup-Tabelle, die die mechanische Leistung pro Einheit bei der Maschinenleistung MVA in Abhängigkeit vom Turbinendurchfluss darstellt. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss4[number]`: Pmss Durchfluss P4 (Pmss4).  Mechanische Leistungsabgabe Pmss für Turbinendurchfluss Punkt 4 für die Nachschlagetabelle, die die mechanische Leistung pro Einheit bei der Maschinenleistung MVA als Funktion des Turbinendurchflusses darstellt. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss5[number]`: Pmss Durchfluss P5 (Pmss5).  Mechanische Ausgangsleistung Pmss für Turbinendurchfluss Punkt 5 für die Nachschlagetabelle, die die mechanische Leistung pro Einheit bei der Maschinenleistung MVA in Abhängigkeit vom Turbinendurchfluss darstellt. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss6[number]`: Pmss Durchfluss P6 (Pmss6).  Mechanische Ausgangsleistung Pmss für Turbinendurchfluss Punkt 6 für die Lookup-Tabelle, die die mechanische Leistung pro Einheit bei der Maschinenleistung MVA in Abhängigkeit vom Turbinendurchfluss darstellt. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss7[number]`: Pmss Durchfluss P7 (Pmss7).  Mechanische Leistungsabgabe Pmss für Turbinendurchfluss Punkt 7 für die Nachschlagetabelle, die die mechanische Leistung pro Einheit bei der Maschinenleistung MVA in Abhängigkeit vom Turbinendurchfluss darstellt. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss8[number]`: Pmss Durchfluss P8 (Pmss8).  Mechanische Ausgangsleistung Pmss für Turbinendurchfluss Punkt 8 für die Nachschlagetabelle, die die mechanische Leistung pro Einheit bei der Maschinenleistung MVA in Abhängigkeit vom Turbinendurchfluss darstellt. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss9[number]`: Pmss Durchfluss P9 (Pmss9).  Mechanische Ausgangsleistung Pmss für Turbinendurchfluss Punkt 9 für die Lookup-Tabelle, die die mechanische Leistung pro Einheit bei der Maschinenleistung MVA in Abhängigkeit vom Turbinendurchfluss darstellt. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rpg[number]`: Permanenter P-Bereich für die Ausgangsrückführung des Reglers (R-Perm-Gate). Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rpp[number]`: Permanenter P-Bereich für die elektrische Leistungsrückführung (R-Perm-Pe). Standardwert: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den voll qualifizierten Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden.  - `td[number]`: Zeitkonstante des Ableitungsreglers zur Begrenzung der Ableitungskennlinie jenseits einer Durchbruchsfrequenz, um eine Verstärkung des hochfrequenten Rauschens zu vermeiden (Td). Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tdv[number]`: Zeitkonstante für die Verzögerung des Verteilerventils (Tdv). Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tg[number]`: Wert, der es der Verteilerventilsteuerung erlaubt, über den Grenzwert für die Schiebergeschwindigkeit (Tg) hinaus zu fahren. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tp[number]`: Zeitkonstante für die Verzögerung des Pilotventils (Tp). Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tpe[number]`: Zeitkonstante für die elektrische Leistungsabsenkung (Tpe). Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw[number]`: Wasserträgheitszeitkonstante (Tw) (>0). Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI-Typ. Es muss GovHydroWEH sein.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
<!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Angepasst von CIM-Datenmodellen und CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Dieses Datenmodell ist eine direkte Umsetzung des Common Information Model (CIM), das durch die Norm IEC61970 spezifiziert ist, in intelligente Datenmodelle. Die Python-Klassen, auf denen dieses Modell basiert, wurden vom Institut für Automatisierung komplexer Stromversorgungssysteme (ACS), dem EON Energy Research Center (EONERC) und der RWTH Aachen, Deutschland, entwickelt. Einige Eigenschaften können den falschen Typ haben. Sollte dies der Fall sein, melden Sie bitte einen Fehler oder senden Sie eine E-Mail an info@smartdatamodels.org.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
    db:    
      description: 'Speed Dead Band (db). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    dicn:    
      description: 'Value to allow the integral controller to advance beyond the gate limits (Dicn). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dpv:    
      description: 'Value to allow the Pilot valve controller to advance beyond the gate limits (Dpv). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dturb:    
      description: 'Turbine damping factor (Dturb).  Unit = delta P (PU of MWbase) / delta speed (PU). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    feedbackSignal:    
      description: 'Feedback signal selection (Sw). true = PID Output (if R-Perm-Gate=droop and R-Perm-Pe=0) false = Electrical Power (if R-Perm-Gate=0 and R-Perm-Pe=droop) or false = Gate Position (if R-Perm-Gate=droop and R-Perm-Pe=0). Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fl1:    
      description: 'Flow Gate 1 (Fl1).  Flow value for gate position point 1 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fl2:    
      description: 'Flow Gate 2 (Fl2).  Flow value for gate position point 2 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fl3:    
      description: 'Flow Gate 3 (Fl3).  Flow value for gate position point 3 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fl4:    
      description: 'Flow Gate 4 (Fl4).  Flow value for gate position point 4 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fl5:    
      description: 'Flow Gate 5 (Fl5).  Flow value for gate position point 5 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp1:    
      description: 'Flow P1 (Fp1).  Turbine Flow value for point 1 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp10:    
      description: 'Flow P10 (Fp10).  Turbine Flow value for point 10 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp2:    
      description: 'Flow P2 (Fp2).  Turbine Flow value for point 2 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp3:    
      description: 'Flow P3 (Fp3).  Turbine Flow value for point 3 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp4:    
      description: 'Flow P4 (Fp4).  Turbine Flow value for point 4 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp5:    
      description: 'Flow P5 (Fp5).  Turbine Flow value for point 5 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp6:    
      description: 'Flow P6 (Fp6).  Turbine Flow value for point 6 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp7:    
      description: 'Flow P7 (Fp7).  Turbine Flow value for point 7 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp8:    
      description: 'Flow P8 (Fp8).  Turbine Flow value for point 8 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp9:    
      description: 'Flow P9 (Fp9).  Turbine Flow value for point 9 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gmax:    
      description: 'Maximum Gate Position (Gmax). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gmin:    
      description: 'Minimum Gate Position (Gmin). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gtmxcl:    
      description: 'Maximum gate closing rate (Gtmxcl). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gtmxop:    
      description: 'Maximum gate opening rate (Gtmxop). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv1:    
      description: 'Gate 1 (Gv1).  Gate Position value for point 1 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv2:    
      description: 'Gate 2 (Gv2).  Gate Position value for point 2 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv3:    
      description: 'Gate 3 (Gv3).  Gate Position value for point 3 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv4:    
      description: 'Gate 4 (Gv4).  Gate Position value for point 4 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv5:    
      description: 'Gate 5 (Gv5).  Gate Position value for point 5 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
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
      x-ngsi:    
        type: Property    
    kd:    
      description: 'Derivative controller derivative gain (Kd). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ki:    
      description: 'Derivative controller Integral gain (Ki). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kp:    
      description: 'Derivative control gain (Kp). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        type: GeoProperty    
    mwbase:    
      description: 'Base for power values (MWbase) (>0).  Unit = MW. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *govhydroweh_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    pmss1:    
      description: 'Pmss Flow P1 (Pmss1).  Mechanical Power output Pmss for Turbine Flow point 1 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss10:    
      description: 'Pmss Flow P10 (Pmss10).  Mechanical Power output Pmss for Turbine Flow point 10 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss2:    
      description: 'Pmss Flow P2 (Pmss2).  Mechanical Power output Pmss for Turbine Flow point 2 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss3:    
      description: 'Pmss Flow P3 (Pmss3).  Mechanical Power output Pmss for Turbine Flow point 3 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss4:    
      description: 'Pmss Flow P4 (Pmss4).  Mechanical Power output Pmss for Turbine Flow point 4 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss5:    
      description: 'Pmss Flow P5 (Pmss5).  Mechanical Power output Pmss for Turbine Flow point 5 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss6:    
      description: 'Pmss Flow P6 (Pmss6).  Mechanical Power output Pmss for Turbine Flow point 6 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss7:    
      description: 'Pmss Flow P7 (Pmss7).  Mechanical Power output Pmss for Turbine Flow point 7 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss8:    
      description: 'Pmss Flow P8 (Pmss8).  Mechanical Power output Pmss for Turbine Flow point 8 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss9:    
      description: 'Pmss Flow P9 (Pmss9).  Mechanical Power output Pmss for Turbine Flow point 9 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rpg:    
      description: 'Permanent droop for governor output feedback (R-Perm-Gate). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rpp:    
      description: 'Permanent droop for electrical power feedback (R-Perm-Pe). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    td:    
      description: 'Derivative controller time constant to limit the derivative characteristic beyond a breakdown frequency to avoid amplification of high-frequency noise (Td). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tdv:    
      description: 'Distributive Valve time lag time constant (Tdv). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tg:    
      description: 'Value to allow the Distribution valve controller to advance beyond the gate movement rate limit (Tg). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tp:    
      description: 'Pilot Valve time lag time constant (Tp). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tpe:    
      description: 'Electrical power droop time constant (Tpe). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tw:    
      description: 'Water inertia time constant (Tw) (>0). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be GovHydroWEH'    
      enum:    
        - GovHydroWEH    
      type: string    
      x-ngsi:    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovHydroWEH/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/GovHydroWEH/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
Nicht verfügbar ist das Beispiel eines GovHydroWEH im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar ist das Beispiel eines GovHydroWEH im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar ist das Beispiel eines GovHydroWEH im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar ist das Beispiel eines GovHydroWEH im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
