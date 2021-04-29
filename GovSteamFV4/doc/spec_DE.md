Entität: GovSteamFV4  
====================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovSteamFV4/LICENSE.md)  
Globale Beschreibung: **Abgeleitet aus CIM-Datenmodellen. Detaillierter elektrohydraulischer Regler für das Dampfaggregat.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `cpsmn`: Mindestwert des Druckreglerausgangs (Cpsmn).  Typischer Wert = -1. Voreinstellung: 0.0  - `cpsmx`: Maximaler Wert des Druckreglerausgangs (Cpsmx).  Typischer Wert = 1. Voreinstellung: 0.0  - `crmn`: Minimaler Wert des Regler-Sollwerts (Crmn).  Typischer Wert = 0. Voreinstellung: 0.0  - `crmx`: Maximaler Wert des Regler-Sollwerts (Crmx).  Typischer Wert = 1,2. Voreinstellung: 0,0  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `id`: Eindeutiger Bezeichner der Entität  - `kdc`: Derivative Verstärkung des Druckreglers (Kdc).  Typischer Wert = 1. Voreinstellung: 0.0  - `kf1`: Frequenzvorspannung (Kehrwert des P-Bereichs) (Kf1).  Typischer Wert = 20. Voreinstellung: 0,0  - `kf3`: Frequenzregelung (Kehrwert des P-Bereichs) (Kf3).  Typischer Wert = 20. Voreinstellung: 0.0  - `khp`: Anteil der vom HP-Teil erzeugten Gesamtleistung der Turbine (Khp).  Typischer Wert = 0,35. Voreinstellung: 0.0  - `kic`: Integrale Verstärkung des Druckreglers (Kic).  Typischer Wert = 0,0033. Voreinstellung: 0,0  - `kip`: Integrale Verstärkung des Druckrückführungsreglers (Kip).  Typischer Wert = 0,5. Voreinstellung: 0,0  - `kit`: Integralverstärkung des elektrohydraulischen Reglers (Kit).  Typischer Wert = 0,04. Voreinstellung: 0.0  - `kmp1`: Erster Verstärkungskoeffizient der Intercept-Ventil-Kennlinie (Kmp1).  Typischer Wert = 0,5. Voreinstellung: 0,0  - `kmp2`: Zweiter Verstärkungskoeffizient der Intercept-Ventilkennlinie (Kmp2).  Typischer Wert = 3,5. Voreinstellung: 0,0  - `kpc`: Proportionale Verstärkung des Druckreglers (Kpc).  Typischer Wert = 0,5. Voreinstellung: 0,0  - `kpp`: Proportionale Verstärkung des Druckrückführungsreglers (Kpp).  Typischer Wert = 1. Voreinstellung: 0.0  - `kpt`: Proportionalverstärkung des elektrohydraulischen Reglers (Kpt).  Typischer Wert = 0,3. Voreinstellung: 0,0  - `krc`: Maximale Variation des Kraftstoffflusses (Krc).  Typischer Wert = 0,05. Voreinstellung: 0,0  - `ksh`: Druckverlust aufgrund von Strömungsreibung in den Kesselrohren (Ksh).  Typischer Wert = 0,08. Voreinstellung: 0.0  - `location`:   - `lpi`: Maximaler negativer Leistungsfehler (Lpi).  Typischer Wert = -0,15. Voreinstellung: 0,0  - `lps`: Maximaler positiver Leistungsfehler (Lps).  Typischer Wert = 0,03. Voreinstellung: 0,0  - `mnef`: Unterer Grenzwert für die Frequenzkorrektur (MN).  Typischer Wert = -0,05. Voreinstellung: 0,0  - `mxef`: Oberer Grenzwert für die Frequenzkorrektur (MX).  Typischer Wert = 0,05. Voreinstellung: 0,0  - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `pr1`: Erster Wert der statischen Drucksollwertkennlinie (Pr1).  Typischer Wert = 0,2. Voreinstellung: 0,0  - `pr2`: Zweiter Wert der statischen Drucksollwertkennlinie, entsprechend Ps0 = 1,0 VPE (Pr2).  Typischer Wert = 0,75. Voreinstellung: 0,0  - `psmn`: Mindestwert der statischen Drucksollwertkennlinie (Psmn).  Typischer Wert = 1. Voreinstellung: 0.0  - `rsmimn`: Mindestwert des Integralreglers (Rsmimn).  Typischer Wert = 0. Voreinstellung: 0.0  - `rsmimx`: Maximaler Wert des Integralreglers (Rsmimx).  Typischer Wert = 1,1. Voreinstellung: 0,0  - `rvgmn`: Minimaler Wert des Integralreglers (Rvgmn).  Typischer Wert = 0. Voreinstellung: 0.0  - `rvgmx`: Maximaler Wert des Integralreglers (Rvgmx).  Typischer Wert = 1,2. Voreinstellung: 0,0  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `srmn`: Minimale Ventilöffnung (Srmn).  Typischer Wert = 0. Voreinstellung: 0.0  - `srmx`: Maximale Ventilöffnung (Srmx).  Typischer Wert = 1,1. Voreinstellung: 0,0  - `srsmp`: Schnittpunkt Ventile charakteristischer Unstetigkeitspunkt (Srsmp).  Typischer Wert = 0,43. Voreinstellung: 0.0  - `svmn`: Maximale Schließgeschwindigkeit des Reglertors (Svmn).  Typischer Wert = -0,0333. Voreinstellung: 0,0  - `svmx`: Maximale Öffnungsgeschwindigkeit des Reglertors (Svmx).  Typischer Wert = 0,0333. Voreinstellung: 0,0  - `ta`: Steuerventilrate Öffnungszeit (Ta).  Typischer Wert = 0,8. Voreinstellung: 0  - `tam`: Intercept Ventile Rate Öffnungszeit (Tam).  Typischer Wert = 0,8. Voreinstellung: 0  - `tc`: Regelventilrate Schließzeit (Tc).  Typischer Wert = 0,5. Voreinstellung: 0  - `tcm`: Intercept Ventile Rate Schließzeit (Tcm).  Typischer Wert = 0,5. Voreinstellung: 0  - `tdc`: Vorhaltezeitkonstante des Druckreglers (Tdc).  Typischer Wert = 90. Voreinstellung: 0  - `tf1`: Zeitkonstante der Kraftstoffregelung (Tf1).  Typischer Wert = 10. Voreinstellung: 0  - `tf2`: Zeitkonstante der Dampftruhe (Tf2).  Typischer Wert = 10. Voreinstellung: 0  - `thp`: Hochdruck (HP) Zeitkonstante der Turbine (Thp).  Typischer Wert = 0,15. Voreinstellung: 0  - `tmp`: Niederdruck (ND) Zeitkonstante der Turbine (Tmp).  Typischer Wert = 0,4. Voreinstellung: 0  - `trh`: Nachheizzeitkonstante der Turbine (Trh).  Typischer Wert = 10. Voreinstellung: 0  - `tv`: Kesselzeitkonstante (Tv).  Typischer Wert = 60. Voreinstellung: 0  - `ty`: Regelventile Servo-Zeitkonstante (Ty).  Typischer Wert = 0,1. Voreinstellung: 0  - `type`: NGSI-Typ. Es muss GovSteamFV4 sein  - `y`: Koeffizient der linearisierten Gleichungen der Turbine (Stodola-Formulierung) (Y).  Typischer Wert = 0,13. Voreinstellung: 0.0  - `yhpmn`: Minimale Regelventilposition (Yhpmn).  Typischer Wert = 0. Voreinstellung: 0.0  - `yhpmx`: Maximale Regelventilposition (Yhpmx).  Typischer Wert = 1,1. Voreinstellung: 0,0  - `ympmn`: Minimale Abfangventilposition (Ympmn).  Typischer Wert = 0. Voreinstellung: 0.0  - `ympmx`: Maximale Abfangventilposition (Ympmx).  Typischer Wert = 1,1. Voreinstellung: 0,0    
Erforderliche Eigenschaften  
Dieses Datenmodell ist eine direkte Umsetzung des Common Information Model (CIM), das durch die Norm IEC61970 spezifiziert ist, in Smart Data Models. Die Python-Klassen, auf denen dieses Modell basiert, wurden von diesen Einrichtungen entwickelt Institut für Automatisierung komplexer Stromversorgungssysteme (ACS), EON Energy Research Center (EONERC) und RWTH Aachen, Deutschland. einige Eigenschaften können einen falschen Typ haben. Dies war der Fall, bitte melden Sie einen Fehler oder senden Sie eine E-Mail an alberto.abella@fiware.org  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
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
    cpsmn:    
      description: 'Minimum value of pressure regulator output (Cpsmn).  Typical Value = -1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    cpsmx:    
      description: 'Maximum value of pressure regulator output (Cpsmx).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    crmn:    
      description: 'Minimum value of regulator set-point (Crmn).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    crmx:    
      description: 'Maximum value of regulator set-point (Crmx).  Typical Value = 1.2. Default: 0.0'    
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
      type: Property    
    kdc:    
      description: 'Derivative gain of pressure regulator (Kdc).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kf1:    
      description: 'Frequency bias (reciprocal of droop) (Kf1).  Typical Value = 20. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kf3:    
      description: 'Frequency control (reciprocal of droop) (Kf3).  Typical Value = 20. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    khp:    
      description: 'Fraction  of total turbine output generated by HP part (Khp).  Typical Value = 0.35. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kic:    
      description: 'Integral gain of pressure regulator (Kic).  Typical Value = 0.0033. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kip:    
      description: 'Integral gain of pressure feedback regulator (Kip).  Typical Value = 0.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kit:    
      description: 'Integral gain of electro-hydraulic regulator (Kit).  Typical Value = 0.04. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kmp1:    
      description: 'First gain coefficient of  intercept valves characteristic (Kmp1).  Typical Value = 0.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kmp2:    
      description: 'Second gain coefficient of intercept valves characteristic (Kmp2).  Typical Value = 3.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kpc:    
      description: 'Proportional gain of pressure regulator (Kpc).  Typical Value = 0.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kpp:    
      description: 'Proportional gain of pressure feedback regulator (Kpp).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kpt:    
      description: 'Proportional gain of electro-hydraulic regulator (Kpt).  Typical Value = 0.3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    krc:    
      description: 'Maximum variation of fuel flow (Krc).  Typical Value = 0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ksh:    
      description: 'Pressure loss due to flow friction in the boiler tubes (Ksh).  Typical Value = 0.08. Default: 0.0'    
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
    lpi:    
      description: 'Maximum negative power error (Lpi).  Typical Value = -0.15. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    lps:    
      description: 'Maximum positive power error (Lps).  Typical Value = 0.03. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    mnef:    
      description: 'Lower limit for frequency correction (MN).  Typical Value = -0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    mxef:    
      description: 'Upper limit for frequency correction (MX).  Typical Value = 0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *govsteamfv4_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    pr1:    
      description: 'First value of pressure set point static characteristic (Pr1).  Typical Value = 0.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pr2:    
      description: 'Second value of pressure set point static characteristic, corresponding to Ps0 = 1.0 PU (Pr2).  Typical Value = 0.75. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    psmn:    
      description: 'Minimum value of pressure set point static characteristic (Psmn).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rsmimn:    
      description: 'Minimum value of integral regulator (Rsmimn).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rsmimx:    
      description: 'Maximum value of integral regulator (Rsmimx).  Typical Value = 1.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rvgmn:    
      description: 'Minimum value of integral regulator (Rvgmn).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rvgmx:    
      description: 'Maximum value of integral regulator (Rvgmx).  Typical Value = 1.2. Default: 0.0'    
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
    srmn:    
      description: 'Minimum valve opening (Srmn).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    srmx:    
      description: 'Maximum valve opening (Srmx).  Typical Value = 1.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    srsmp:    
      description: 'Intercept valves characteristic discontinuity point (Srsmp).  Typical Value = 0.43. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    svmn:    
      description: 'Maximum regulator gate closing velocity (Svmn).  Typical Value = -0.0333. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    svmx:    
      description: 'Maximum regulator gate opening velocity (Svmx).  Typical Value = 0.0333. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ta:    
      description: 'Control valves rate opening time (Ta).  Typical Value = 0.8. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tam:    
      description: 'Intercept valves rate opening time (Tam).  Typical Value = 0.8. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tc:    
      description: 'Control valves rate closing time (Tc).  Typical Value = 0.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tcm:    
      description: 'Intercept valves rate closing time (Tcm).  Typical Value = 0.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tdc:    
      description: 'Derivative time constant of pressure regulator (Tdc).  Typical Value = 90. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tf1:    
      description: 'Time constant of fuel regulation (Tf1).  Typical Value = 10. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tf2:    
      description: 'Time constant of steam chest (Tf2).  Typical Value = 10. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    thp:    
      description: 'High pressure (HP) time constant of the turbine (Thp).  Typical Value = 0.15. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tmp:    
      description: 'Low pressure (LP) time constant of the turbine (Tmp).  Typical Value = 0.4. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    trh:    
      description: 'Reheater  time constant of the turbine (Trh).  Typical Value = 10. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tv:    
      description: 'Boiler time constant (Tv).  Typical Value = 60. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ty:    
      description: 'Control valves servo time constant (Ty).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be GovSteamFV4'    
      enum:    
        - GovSteamFV4    
      type: Property    
    y:    
      description: 'Coefficient of linearized equations of turbine (Stodola formulation) (Y).  Typical Value = 0.13. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    yhpmn:    
      description: 'Minimum control valve position (Yhpmn).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    yhpmx:    
      description: 'Maximum control valve position (Yhpmx).  Typical Value = 1.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ympmn:    
      description: 'Minimum intercept valve position (Ympmn).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ympmx:    
      description: 'Maximum intercept valve position (Ympmx).  Typical Value = 1.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
Nicht verfügbar das Beispiel einer GovSteamFV4 im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer GovSteamFV4 im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer GovSteamFV4 im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer GovSteamFV4 im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
