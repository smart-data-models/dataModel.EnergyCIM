Entity: GovHydroFrancis  
=======================  
[Open License](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovHydroFrancis/LICENSE.md)  
Global description: **Adapted from CIM data models. Detailed hydro unit - Francis model.  This model can be used to represent three types of governors. A schematic of the hydraulic system of detailed hydro unit models, like Francis and Pelton, is provided in the DetailedHydroModelHydraulicSystem diagram.**  

## List of properties  

- `address`: The mailing address  - `alternateName`: An alternative name for this item  - `am`: Opening section S at the maximum efficiency (Am).  Typical Value = 0.7. Default: 0.0  - `areaServed`: The geographic area where a service or offered item is provided  - `av0`: Area of the surge tank (A). Unit = m. Typical Value = 30. Default: 0.0  - `av1`: Area of the compensation tank (A). Unit = m. Typical Value = 700. Default: 0.0  - `bp`: Droop (Bp).  Typical Value = 0.05. Default: 0.0  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `db1`: Intentional dead-band width (DB1).  Unit = Hz.  Typical Value = 0. Default: 0.0  - `description`: A description of this item  - `etamax`: Maximum efficiency (EtaMax).  Typical Value = 1.05. Default: 0.0  - `governorControl`: Governor control flag (Cflag).  Typical Value = mechanicHydrolicTachoAccelerator. Default: None  - `h1`: Head of compensation chamber water level with respect to the level of penstock (H).  Unit = m. Typical Value = 4. Default: 0.0  - `h2`: Head of surge tank water level with respect to the level of penstock (H).  Unit = m. Typical Value = 40. Default: 0.0  - `hn`: Rated hydraulic head (H).  Unit = m. Typical Value = 250. Default: 0.0  - `id`: Unique identifier of the entity  - `kc`: Penstock loss coefficient (due to friction) (Kc).  Typical Value = 0.025. Default: 0.0  - `kg`: Water tunnel and surge chamber loss coefficient (due to friction) (Kg).  Typical Value = 0.025. Default: 0.0  - `kt`: Washout gain (Kt).  Typical Value = 0.25. Default: 0.0  - `location`:   - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `qc0`: No-load turbine flow at nominal head (Qc0).  Typical Value = 0.21. Default: 0.0  - `qn`: Rated flow (Q). Unit = m/s. Typical Value = 40. Default: 0.0  - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `ta`: Derivative gain (Ta).  Typical Value = 3. Default: 0  - `td`: Washout time constant (Td).  Typical Value = 3. Default: 0  - `ts`: Gate servo time constant (Ts).  Typical Value = 0.5. Default: 0  - `twnc`: Water inertia time constant (Twnc).  Typical Value = 1. Default: 0  - `twng`: Water tunnel and surge chamber inertia time constant (Twng). Typical Value = 3. Default: 0  - `tx`: Derivative feedback gain (Tx).  Typical Value = 1. Default: 0  - `type`: NGSI type. It has to be GovHydroFrancis  - `va`: Maximum gate opening velocity (Va).  Unit = PU/sec.  Typical Value = 0.011. Default: 0.0  - `valvmax`: Maximum gate opening (ValvMax).  Typical Value = 1. Default: 0.0  - `valvmin`: Minimum gate opening (ValvMin).  Typical Value = 0. Default: 0.0  - `vc`: Maximum gate closing velocity (Vc).  Unit = PU/sec.  Typical Value = -0.011. Default: 0.0  - `waterTunnelSurgeChamberSimulation`: Water tunnel and surge chamber simulation (Tflag). true = enable of water tunnel and surge chamber simulation false = inhibit of water tunnel and surge chamber simulation. Typical Value = false. Default: False  - `zsfc`: Head of upper water level with respect to the level of penstock (Zsfc).  Unit = m.  Typical Value = 25. Default: 0.0    
Required properties  
This data model is a direct conversion of the Common Information Model (CIM) specified by the IEC61970 standard into smart data models. The python classes this model is based on were developed by these entities Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) and RWTH University Aachen, Germany. some properties can have wrong type. This was the case, pelase raise an issue or send mail to alberto.abella@fiware.org  
## Data Model description of properties  
Sorted alphabetically (click for details)  
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
## Example payloads    
Not available the example of a GovHydroFrancis in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
Not available the example of a GovHydroFrancis in JSON format as normalized. This is compatible with NGSI V2 when not using options and returns the context data of an individual entity.  
Not available the example of a GovHydroFrancis in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
Not available the example of a GovHydroFrancis in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
