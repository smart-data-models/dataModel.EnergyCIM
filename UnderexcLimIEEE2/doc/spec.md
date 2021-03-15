Entity: UnderexcLimIEEE2  
========================  
[Open License](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/UnderexcLimIEEE2/LICENSE.md)  
Global description: **Adapted from CIM data models. The class represents the Type UEL2 which has either a straight-line or multi-segment characteristic when plotted in terms of machine reactive power output vs. real power output.  Reference: IEEE UEL2 421.5-2005 Section 10.2.  (Limit characteristic lookup table shown in Figure 10.4 (p 32) of the standard).**  

## List of properties  

- `address`: The mailing address  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `id`: Unique identifier of the entity  - `k1`: UEL terminal voltage exponent applied to real power input to UEL limit look-up table (k1).  Typical Value = 2. Default: 0.0  - `k2`: UEL terminal voltage exponent applied to reactive power output from UEL limit look-up table (k2).  Typical Value = 2. Default: 0.0  - `kfb`: Gain associated with optional integrator feedback input signal to UEL (K).  Typical Value = 0. Default: 0.0  - `kuf`: UEL excitation system stabilizer gain (K).  Typical Value = 0. Default: 0.0  - `kui`: UEL integral gain (K).  Typical Value = 0.5. Default: 0.0  - `kul`: UEL proportional gain (K).  Typical Value = 0.8. Default: 0.0  - `location`:   - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `p0`: Real power values for endpoints (P).  Typical Value = 0. Default: 0.0  - `p1`: Real power values for endpoints (P).  Typical Value = 0.3. Default: 0.0  - `p10`: Real power values for endpoints (P). Default: 0.0  - `p2`: Real power values for endpoints (P).  Typical Value = 0.6. Default: 0.0  - `p3`: Real power values for endpoints (P).  Typical Value = 0.9. Default: 0.0  - `p4`: Real power values for endpoints (P).  Typical Value = 1.02. Default: 0.0  - `p5`: Real power values for endpoints (P). Default: 0.0  - `p6`: Real power values for endpoints (P). Default: 0.0  - `p7`: Real power values for endpoints (P). Default: 0.0  - `p8`: Real power values for endpoints (P). Default: 0.0  - `p9`: Real power values for endpoints (P). Default: 0.0  - `q0`: Reactive power values for endpoints (Q).  Typical Value = -0.31. Default: 0.0  - `q1`: Reactive power values for endpoints (Q).  Typical Value = -0.31. Default: 0.0  - `q10`: Reactive power values for endpoints (Q). Default: 0.0  - `q2`: Reactive power values for endpoints (Q).  Typical Value = -0.28. Default: 0.0  - `q3`: Reactive power values for endpoints (Q).  Typical Value = -0.21. Default: 0.0  - `q4`: Reactive power values for endpoints (Q).  Typical Value = 0. Default: 0.0  - `q5`: Reactive power values for endpoints (Q). Default: 0.0  - `q6`: Reactive power values for endpoints (Q). Default: 0.0  - `q7`: Reactive power values for endpoints (Q). Default: 0.0  - `q8`: Reactive power values for endpoints (Q). Default: 0.0  - `q9`: Reactive power values for endpoints (Q). Default: 0.0  - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `tu1`: UEL lead time constant (T).  Typical Value = 0. Default: 0  - `tu2`: UEL lag time constant (T).  Typical Value = 0. Default: 0  - `tu3`: UEL lead time constant (T).  Typical Value = 0. Default: 0  - `tu4`: UEL lag time constant (T).  Typical Value = 0. Default: 0  - `tul`: Time constant associated with optional integrator feedback input signal to UEL (T).  Typical Value = 0. Default: 0  - `tup`: Real power filter time constant (T).  Typical Value = 5. Default: 0  - `tuq`: Reactive power filter time constant (T).  Typical Value = 0. Default: 0  - `tuv`: Voltage filter time constant (T).  Typical Value = 5. Default: 0  - `type`: NGSI type. It has to be UnderexcLimIEEE2  - `vuimax`: UEL integrator output maximum limit (V).  Typical Value = 0.25. Default: 0.0  - `vuimin`: UEL integrator output minimum limit (V).  Typical Value = 0. Default: 0.0  - `vulmax`: UEL output maximum limit (V).  Typical Value = 0.25. Default: 0.0  - `vulmin`: UEL output minimum limit (V).  Typical Value = 0. Default: 0.0    
Required properties  
This data model is a direct conversion of the Common Information Model (CIM) specified by the IEC61970 standard into smart data models. The python classes this model is based on were developed by these entities Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) and RWTH University Aachen, Germany. some properties can have wrong type. This was the case, pelase raise an issue or send mail to alberto.abella@fiware.org  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
UnderexcLimIEEE2:    
  description: 'Adapted from CIM data models. The class represents the Type UEL2 which has either a straight-line or multi-segment characteristic when plotted in terms of machine reactive power output vs. real power output.  Reference: IEEE UEL2 421.5-2005 Section 10.2.  (Limit characteristic lookup table shown in Figure 10.4 (p 32) of the standard).'    
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
    description:    
      description: 'A description of this item'    
      type: Property    
    id:    
      anyOf: &underexclimieee2_-_properties_-_owner_-_items_-_anyof    
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
    k1:    
      description: 'UEL terminal voltage exponent applied to real power input to UEL limit look-up table (k1).  Typical Value = 2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    k2:    
      description: 'UEL terminal voltage exponent applied to reactive power output from UEL limit look-up table (k2).  Typical Value = 2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kfb:    
      description: 'Gain associated with optional integrator feedback input signal to UEL (K).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kuf:    
      description: 'UEL excitation system stabilizer gain (K).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kui:    
      description: 'UEL integral gain (K).  Typical Value = 0.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kul:    
      description: 'UEL proportional gain (K).  Typical Value = 0.8. Default: 0.0'    
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
        anyOf: *underexclimieee2_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    p0:    
      description: 'Real power values for endpoints (P).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    p1:    
      description: 'Real power values for endpoints (P).  Typical Value = 0.3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    p10:    
      description: 'Real power values for endpoints (P). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    p2:    
      description: 'Real power values for endpoints (P).  Typical Value = 0.6. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    p3:    
      description: 'Real power values for endpoints (P).  Typical Value = 0.9. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    p4:    
      description: 'Real power values for endpoints (P).  Typical Value = 1.02. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    p5:    
      description: 'Real power values for endpoints (P). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    p6:    
      description: 'Real power values for endpoints (P). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    p7:    
      description: 'Real power values for endpoints (P). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    p8:    
      description: 'Real power values for endpoints (P). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    p9:    
      description: 'Real power values for endpoints (P). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    q0:    
      description: 'Reactive power values for endpoints (Q).  Typical Value = -0.31. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    q1:    
      description: 'Reactive power values for endpoints (Q).  Typical Value = -0.31. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    q10:    
      description: 'Reactive power values for endpoints (Q). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    q2:    
      description: 'Reactive power values for endpoints (Q).  Typical Value = -0.28. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    q3:    
      description: 'Reactive power values for endpoints (Q).  Typical Value = -0.21. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    q4:    
      description: 'Reactive power values for endpoints (Q).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    q5:    
      description: 'Reactive power values for endpoints (Q). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    q6:    
      description: 'Reactive power values for endpoints (Q). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    q7:    
      description: 'Reactive power values for endpoints (Q). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    q8:    
      description: 'Reactive power values for endpoints (Q). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    q9:    
      description: 'Reactive power values for endpoints (Q). Default: 0.0'    
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
    tu1:    
      description: 'UEL lead time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tu2:    
      description: 'UEL lag time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tu3:    
      description: 'UEL lead time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tu4:    
      description: 'UEL lag time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tul:    
      description: 'Time constant associated with optional integrator feedback input signal to UEL (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tup:    
      description: 'Real power filter time constant (T).  Typical Value = 5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tuq:    
      description: 'Reactive power filter time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tuv:    
      description: 'Voltage filter time constant (T).  Typical Value = 5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be UnderexcLimIEEE2'    
      enum:    
        - UnderexcLimIEEE2    
      type: Property    
    vuimax:    
      description: 'UEL integrator output maximum limit (V).  Typical Value = 0.25. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vuimin:    
      description: 'UEL integrator output minimum limit (V).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vulmax:    
      description: 'UEL output maximum limit (V).  Typical Value = 0.25. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vulmin:    
      description: 'UEL output minimum limit (V).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Example payloads    
Not available the example of a UnderexcLimIEEE2 in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
Not available the example of a UnderexcLimIEEE2 in JSON format as normalized. This is compatible with NGSI V2 when not using options and returns the context data of an individual entity.  
Not available the example of a UnderexcLimIEEE2 in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
Not available the example of a UnderexcLimIEEE2 in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
