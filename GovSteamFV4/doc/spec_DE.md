<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: GovSteamFV4  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovSteamFV4/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Aus den CIM-Datenmodellen übernommen. Detaillierter elektrohydraulischer Regler für das Dampfaggregat**.  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, liegt das daran, dass es mehrere Typen oder unterschiedliche Formate/Muster haben kann</sub></sup>.  
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `cpsmn[number]`: Mindestwert des Druckreglerausgangs (Cpsmn).  Typischer Wert = -1. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `cpsmx[number]`: Höchstwert des Druckreglerausgangs (Cpsmx).  Typischer Wert = 1. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `crmn[number]`: Minimaler Wert des Regler-Sollwerts (Crmn).  Typischer Wert = 0. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `crmx[number]`: Maximaler Wert des Regler-Sollwerts (Crmx).  Typischer Wert = 1,2. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated[string]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified[string]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description[string]`: Eine Beschreibung dieses Artikels  - `id[*]`: Eindeutiger Bezeichner der Entität  - `kdc[number]`: Abgeleitete Verstärkung des Druckreglers (Kdc).  Typischer Wert = 1. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kf1[number]`: Frequenzvorspannung (Kehrwert der Abweichung) (Kf1).  Typischer Wert = 20. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kf3[number]`: Frequenzregelung (Kehrwert der Abweichung) (Kf3).  Typischer Wert = 20. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `khp[number]`: Anteil der vom HP-Teil erzeugten Gesamtleistung der Turbine (Khp).  Typischer Wert = 0,35. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kic[number]`: Integrale Verstärkung des Druckreglers (Kic).  Typischer Wert = 0,0033. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kip[number]`: Integrale Verstärkung des Druckrückführungsreglers (Kip).  Typischer Wert = 0,5. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kit[number]`: Integralverstärkung des elektrohydraulischen Reglers (Kit).  Typischer Wert = 0,04. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kmp1[number]`: Erster Verstärkungskoeffizient der Intercept-Ventilkennlinie (Kmp1).  Typischer Wert = 0,5. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kmp2[number]`: Zweiter Verstärkungskoeffizient der Intercept-Ventilkennlinie (Kmp2).  Typischer Wert = 3,5. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kpc[number]`: Proportionalverstärkung des Druckreglers (Kpc).  Typischer Wert = 0,5. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kpp[number]`: Proportionale Verstärkung des Druckrückführungsreglers (Kpp).  Typischer Wert = 1. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kpt[number]`: Proportionalverstärkung des elektro-hydraulischen Reglers (Kpt).  Typischer Wert = 0,3. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `krc[number]`: Maximale Abweichung des Kraftstoffdurchflusses (Krc).  Typischer Wert = 0,05. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ksh[number]`: Druckverlust aufgrund von Strömungsreibung in den Kesselrohren (Ksh).  Typischer Wert = 0,08. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `lpi[number]`: Maximaler negativer Leistungsfehler (Lpi).  Typischer Wert = -0,15. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `lps[number]`: Maximaler positiver Leistungsfehler (Lps).  Typischer Wert = 0,03. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `mnef[number]`: Unterer Grenzwert für die Frequenzkorrektur (MN).  Typischer Wert = -0,05. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `mxef[number]`: Oberer Grenzwert für die Frequenzkorrektur (MX).  Typischer Wert = 0,05. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: Der Name dieses Artikels.  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `pr1[number]`: Erster Wert der statischen Drucksollwertkennlinie (Pr1).  Typischer Wert = 0,2. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pr2[number]`: Zweiter Wert der statischen Drucksollwertkennlinie, entsprechend Ps0 = 1,0 VPE (Pr2).  Typischer Wert = 0,75. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `psmn[number]`: Mindestwert der statischen Drucksollwertkennlinie (Psmn).  Typischer Wert = 1. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rsmimn[number]`: Mindestwert des Integralreglers (Rsmimn).  Typischer Wert = 0. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rsmimx[number]`: Höchstwert des Integralreglers (Rsmimx).  Typischer Wert = 1,1. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rvgmn[number]`: Mindestwert des Integralreglers (Rvgmn).  Typischer Wert = 0. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rvgmx[number]`: Höchstwert des Integralreglers (Rvgmx).  Typischer Wert = 1,2. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den voll qualifizierten Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden.  - `srmn[number]`: Minimale Ventilöffnung (Srmn).  Typischer Wert = 0. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `srmx[number]`: Maximale Ventilöffnung (Srmx).  Typischer Wert = 1,1. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `srsmp[number]`: Schnittpunkt Ventile charakteristischer Unstetigkeitspunkt (Srsmp).  Typischer Wert = 0,43. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `svmn[number]`: Maximale Schließgeschwindigkeit des Reglers (Svmn).  Typischer Wert = -0,0333. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `svmx[number]`: Maximale Öffnungsgeschwindigkeit des Reglers (Svmx).  Typischer Wert = 0,0333. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ta[number]`: Öffnungszeit der Steuerventile (Ta).  Typischer Wert = 0,8. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tam[number]`: Öffnungszeit des Abschnittsventils (Tam).  Typischer Wert = 0,8. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tc[number]`: Regelventile: Schließzeit (Tc).  Typischer Wert = 0,5. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tcm[number]`: Schließzeit des Abschnittsventils (Tcm).  Typischer Wert = 0,5. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tdc[number]`: Abgeleitete Zeitkonstante des Druckreglers (Tdc).  Typischer Wert = 90. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tf1[number]`: Zeitkonstante der Kraftstoffregelung (Tf1).  Typischer Wert = 10. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tf2[number]`: Zeitkonstante der Dampfkammer (Tf2).  Typischer Wert = 10. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `thp[number]`: Hochdruck-Zeitkonstante (HP) der Turbine (Thp).  Typischer Wert = 0,15. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tmp[number]`: Niederdruck-Zeitkonstante (LP) der Turbine (Tmp).  Typischer Wert = 0,4. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `trh[number]`: Nachheizzeitkonstante der Turbine (Trh).  Typischer Wert = 10. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tv[number]`: Zeitkonstante des Kessels (Tv).  Typischer Wert = 60. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ty[number]`: Zeitkonstante der Servoventile (Ty).  Typischer Wert = 0,1. Voreinstellung: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI-Typ. Es muss GovSteamFV4 sein.  - `y[number]`: Koeffizient der linearisierten Gleichungen der Turbine (Stodola-Formulierung) (Y).  Typischer Wert = 0,13. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `yhpmn[number]`: Minimale Regelventilstellung (Yhpmn).  Typischer Wert = 0. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `yhpmx[number]`: Maximale Regelventilstellung (Yhpmx).  Typischer Wert = 1,1. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ympmn[number]`: Minimale Abfangventilstellung (Ympmn).  Typischer Wert = 0. Voreinstellung: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ympmx[number]`: Maximale Abfangventilstellung (Ympmx).  Typischer Wert = 1,1. Voreinstellung: 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
<!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Angepasst von CIM-Datenmodellen und CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Dieses Datenmodell ist eine direkte Umsetzung des Common Information Model (CIM), das durch die Norm IEC61970 spezifiziert ist, in intelligente Datenmodelle. Die Python-Klassen, auf denen dieses Modell basiert, wurden vom Institut für Automatisierung komplexer Stromversorgungssysteme (ACS), dem EON Energy Research Center (EONERC) und der RWTH Aachen, Deutschland, entwickelt. Einige Eigenschaften können einen falschen Typ haben. Sollte dies der Fall sein, melden Sie bitte einen Fehler oder senden Sie eine E-Mail an info@smartdatamodels.org.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GovSteamFV4:    
  description: 'Adapted from CIM data models. Detailed electro-hydraulic governor for steam unit.'    
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
    cpsmn:    
      description: 'Minimum value of pressure regulator output (Cpsmn).  Typical Value = -1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    cpsmx:    
      description: 'Maximum value of pressure regulator output (Cpsmx).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    crmn:    
      description: 'Minimum value of regulator set-point (Crmn).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    crmx:    
      description: 'Maximum value of regulator set-point (Crmx).  Typical Value = 1.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    id:    
      anyOf: &govsteamfv4_-_properties_-_owner_-_items_-_anyof    
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
    kdc:    
      description: 'Derivative gain of pressure regulator (Kdc).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kf1:    
      description: 'Frequency bias (reciprocal of droop) (Kf1).  Typical Value = 20. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kf3:    
      description: 'Frequency control (reciprocal of droop) (Kf3).  Typical Value = 20. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    khp:    
      description: 'Fraction  of total turbine output generated by HP part (Khp).  Typical Value = 0.35. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kic:    
      description: 'Integral gain of pressure regulator (Kic).  Typical Value = 0.0033. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kip:    
      description: 'Integral gain of pressure feedback regulator (Kip).  Typical Value = 0.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kit:    
      description: 'Integral gain of electro-hydraulic regulator (Kit).  Typical Value = 0.04. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kmp1:    
      description: 'First gain coefficient of  intercept valves characteristic (Kmp1).  Typical Value = 0.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kmp2:    
      description: 'Second gain coefficient of intercept valves characteristic (Kmp2).  Typical Value = 3.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kpc:    
      description: 'Proportional gain of pressure regulator (Kpc).  Typical Value = 0.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kpp:    
      description: 'Proportional gain of pressure feedback regulator (Kpp).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kpt:    
      description: 'Proportional gain of electro-hydraulic regulator (Kpt).  Typical Value = 0.3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    krc:    
      description: 'Maximum variation of fuel flow (Krc).  Typical Value = 0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ksh:    
      description: 'Pressure loss due to flow friction in the boiler tubes (Ksh).  Typical Value = 0.08. Default: 0.0'    
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
    lpi:    
      description: 'Maximum negative power error (Lpi).  Typical Value = -0.15. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    lps:    
      description: 'Maximum positive power error (Lps).  Typical Value = 0.03. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    mnef:    
      description: 'Lower limit for frequency correction (MN).  Typical Value = -0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    mxef:    
      description: 'Upper limit for frequency correction (MX).  Typical Value = 0.05. Default: 0.0'    
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
        anyOf: *govsteamfv4_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    pr1:    
      description: 'First value of pressure set point static characteristic (Pr1).  Typical Value = 0.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pr2:    
      description: 'Second value of pressure set point static characteristic, corresponding to Ps0 = 1.0 PU (Pr2).  Typical Value = 0.75. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    psmn:    
      description: 'Minimum value of pressure set point static characteristic (Psmn).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rsmimn:    
      description: 'Minimum value of integral regulator (Rsmimn).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rsmimx:    
      description: 'Maximum value of integral regulator (Rsmimx).  Typical Value = 1.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rvgmn:    
      description: 'Minimum value of integral regulator (Rvgmn).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rvgmx:    
      description: 'Maximum value of integral regulator (Rvgmx).  Typical Value = 1.2. Default: 0.0'    
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
    srmn:    
      description: 'Minimum valve opening (Srmn).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    srmx:    
      description: 'Maximum valve opening (Srmx).  Typical Value = 1.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    srsmp:    
      description: 'Intercept valves characteristic discontinuity point (Srsmp).  Typical Value = 0.43. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    svmn:    
      description: 'Maximum regulator gate closing velocity (Svmn).  Typical Value = -0.0333. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    svmx:    
      description: 'Maximum regulator gate opening velocity (Svmx).  Typical Value = 0.0333. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ta:    
      description: 'Control valves rate opening time (Ta).  Typical Value = 0.8. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tam:    
      description: 'Intercept valves rate opening time (Tam).  Typical Value = 0.8. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tc:    
      description: 'Control valves rate closing time (Tc).  Typical Value = 0.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tcm:    
      description: 'Intercept valves rate closing time (Tcm).  Typical Value = 0.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tdc:    
      description: 'Derivative time constant of pressure regulator (Tdc).  Typical Value = 90. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tf1:    
      description: 'Time constant of fuel regulation (Tf1).  Typical Value = 10. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tf2:    
      description: 'Time constant of steam chest (Tf2).  Typical Value = 10. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    thp:    
      description: 'High pressure (HP) time constant of the turbine (Thp).  Typical Value = 0.15. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tmp:    
      description: 'Low pressure (LP) time constant of the turbine (Tmp).  Typical Value = 0.4. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    trh:    
      description: 'Reheater  time constant of the turbine (Trh).  Typical Value = 10. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tv:    
      description: 'Boiler time constant (Tv).  Typical Value = 60. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ty:    
      description: 'Control valves servo time constant (Ty).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be GovSteamFV4'    
      enum:    
        - GovSteamFV4    
      type: string    
      x-ngsi:    
        type: Property    
    y:    
      description: 'Coefficient of linearized equations of turbine (Stodola formulation) (Y).  Typical Value = 0.13. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    yhpmn:    
      description: 'Minimum control valve position (Yhpmn).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    yhpmx:    
      description: 'Maximum control valve position (Yhpmx).  Typical Value = 1.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ympmn:    
      description: 'Minimum intercept valve position (Ympmn).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ympmx:    
      description: 'Maximum intercept valve position (Ympmx).  Typical Value = 1.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovSteamFV4/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/GovSteamFV4/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
Nicht verfügbar ist das Beispiel eines GovSteamFV4 im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar ist das Beispiel eines GovSteamFV4 im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar ist das Beispiel eines GovSteamFV4 im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar ist das Beispiel eines GovSteamFV4 im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
