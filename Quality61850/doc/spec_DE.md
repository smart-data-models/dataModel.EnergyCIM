Entität: Qualität61850  
======================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/Quality61850/LICENSE.md)  
Globale Beschreibung: **Adaptiert von CIM-Datenmodellen. Qualitätsflags in dieser Klasse sind wie in IEC 61850 definiert, mit Ausnahme von estimatorReplaced, das der Einfachheit halber in diese Klasse aufgenommen wurde.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `badReference`: Der Messwert kann falsch sein, weil eine Referenz nicht kalibriert ist. Voreinstellung: Falsch  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `estimatorReplaced`: Wert wurde durch State Estimator ersetzt. estimatorReplaced ist kein IEC61850-Qualitätsbit, wurde aber der Einfachheit halber in diese Klasse aufgenommen. Voreinstellung: False  - `failure`: Dieser Identifier zeigt an, dass eine Überwachungsfunktion einen internen oder externen Fehler erkannt hat, z. B. einen Kommunikationsfehler. Voreinstellung: False  - `id`: Eindeutiger Bezeichner der Entität  - `location`:   - `name`: Der Name dieses Elements.  - `oldData`: Messwert ist alt und möglicherweise ungültig, da er in einem bestimmten Zeitintervall nicht erfolgreich aktualisiert wurde. Voreinstellung: False  - `operatorBlocked`: Messwert ist blockiert und damit für die Übertragung nicht verfügbar. Voreinstellung: False  - `oscillatory`: Um eine Überlastung der Kommunikation zu verhindern, ist es sinnvoll, oszillierende (schnell wechselnde) Binäreingänge zu erkennen und zu unterdrücken. Ändert sich ein Signal in einer definierten Zeit (tosc) zweimal in die gleiche Richtung (von 0 nach 1 oder von 1 nach 0), so wird ein Schwingen erkannt und die Detailgütekennung `oszillatorisch` gesetzt. Wenn es erkannt wird, kann eine konfigurierte Anzahl von transienten Änderungen vergehen. In dieser Zeit wird der Gültigkeitsstatus `questionable` gesetzt. Befindet sich das Signal nach dieser definierten Anzahl von Änderungen immer noch im schwingenden Zustand, so wird der Wert entweder auf den entgegengesetzten Zustand des vorherigen stabilen Wertes oder auf einen definierten Standardwert gesetzt. In diesem Fall wird der Gültigkeitsstatus `questionable` zurückgesetzt und `invalid` gesetzt, solange das Signal schwingt. Wenn es so konfiguriert ist, dass keine transienten Änderungen durchlaufen werden sollen, dann wird zusätzlich zur Detailqualitätskennung `oscillatory` (dient nur zur Statusinformation) sofort der Gültigkeitsstatus `invalid` gesetzt. Voreinstellung: False  - `outOfRange`: Messwert liegt außerhalb eines vordefinierten Wertebereichs. Voreinstellung: Falsch  - `overFlow`: Der Messwert kann nicht mehr richtig dargestellt werden. Zum Beispiel überläuft ein Zählerwert vom maximalen Zählerstand zurück auf einen Wert von Null. Voreinstellung: Falsch  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Quelle gibt Informationen über die Herkunft eines Wertes. Der Wert kann vom Prozess übernommen, vorgegeben oder ersetzt werden. Vorgabe: Keine  - `suspect`: Eine Korrelationsfunktion hat festgestellt, dass der Wert nicht mit anderen Werten konsistent ist. Wird typischerweise von einem Netzwerk State Estimator gesetzt. Voreinstellung: Falsch  - `test`: Messwert wird zu Testzwecken übertragen. Voreinstellung: Falsch  - `type`: NGSI-Typ. Es muss Qualität61850 sein  - `validity`: Gültigkeitsdauer des Messwerts. Voreinstellung: Keine    
Erforderliche Eigenschaften  
Dieses Datenmodell ist eine direkte Umsetzung des Common Information Model (CIM), das durch die Norm IEC61970 spezifiziert ist, in Smart Data Models. Die Python-Klassen, auf denen dieses Modell basiert, wurden von diesen Einrichtungen entwickelt Institut für Automatisierung komplexer Stromversorgungssysteme (ACS), EON Energy Research Center (EONERC) und RWTH Aachen, Deutschland. einige Eigenschaften können einen falschen Typ haben. Dies war der Fall, bitte melden Sie einen Fehler oder senden Sie eine E-Mail an alberto.abella@fiware.org  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Quality61850:    
  description: 'Adapted from CIM data models. Quality flags in this class are as defined in IEC 61850, except for estimatorReplaced, which has been included in this class for convenience.'    
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
    badReference:    
      description: 'Measurement value may be incorrect due to a reference being out of calibration. Default: False'    
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
    estimatorReplaced:    
      description: 'Value has been replaced by State Estimator. estimatorReplaced is not an IEC61850 quality bit but has been put in this class for convenience. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    failure:    
      description: 'This identifier indicates that a supervision function has detected an internal or external failure, e.g. communication failure. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &quality61850_-_properties_-_owner_-_items_-_anyof    
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
    name:    
      description: 'The name of this item.'    
      type: Property    
    oldData:    
      description: 'Measurement value is old and possibly invalid, as it has not been successfully updated during a specified time interval. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    operatorBlocked:    
      description: 'Measurement value is blocked and hence unavailable for transmission. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    oscillatory:    
      description: 'To prevent some overload of the communication it is sensible to detect and suppress oscillating (fast changing) binary inputs. If a signal changes in a defined time (tosc) twice in the same direction (from 0 to 1 or from 1 to 0) then oscillation is detected and the detail quality identifier `oscillatory` is set. If it is detected a configured numbers of transient changes could be passed by. In this time the validity status `questionable` is set. If after this defined numbers of changes the signal is still in the oscillating state the value shall be set either to the opposite state of the previous stable value or to a defined default value. In this case the validity status `questionable` is reset and `invalid` is set as long as the signal is oscillating. If it is configured such that no transient changes should be passed by then the validity status `invalid` is set immediately in addition to the detail quality identifier `oscillatory` (used for status information only). Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    outOfRange:    
      description: 'Measurement value is beyond a predefined range of value. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    overFlow:    
      description: 'Measurement value is beyond the capability of being  represented properly. For example, a counter value overflows from maximum count back to a value of zero. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *quality61850_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Source gives information related to the origin of a value. The value may be acquired from the process, defaulted or substituted. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    suspect:    
      description: 'A correlation function has detected that the value is not consitent with other values. Typically set by a network State Estimator. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    test:    
      description: 'Measurement value is transmitted for test purposes. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be Quality61850'    
      enum:    
        - Quality61850    
      type: Property    
    validity:    
      description: 'Validity of the measurement value. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
Nicht verfügbar das Beispiel einer Quality61850 im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer Quality61850 im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer Quality61850 im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar das Beispiel einer Quality61850 im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
