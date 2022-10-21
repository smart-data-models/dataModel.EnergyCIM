<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: UnderexcLimIEEE2  
========================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/UnderexcLimIEEE2/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **Adapted from CIM data models. The class represents the Type UEL2 which has either a straight-line or multi-segment characteristic when plotted in terms of machine reactive power output vs. real power output.  Reference: IEEE UEL2 421.5-2005 Section 10.2.  (Limit characteristic lookup table shown in Figure 10.4 (p 32) of the standard).**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated[string]`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified[string]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description[string]`: A description of this item  - `id[*]`: Unique identifier of the entity  - `k1[number]`: UEL terminal voltage exponent applied to real power input to UEL limit look-up table (k1).  Typical Value = 2. Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `k2[number]`: UEL terminal voltage exponent applied to reactive power output from UEL limit look-up table (k2).  Typical Value = 2. Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kfb[number]`: Gain associated with optional integrator feedback input signal to UEL (K).  Typical Value = 0. Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kuf[number]`: UEL excitation system stabilizer gain (K).  Typical Value = 0. Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kui[number]`: UEL integral gain (K).  Typical Value = 0.5. Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kul[number]`: UEL proportional gain (K).  Typical Value = 0.8. Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name[string]`: The name of this item.  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `p0[number]`: Real power values for endpoints (P).  Typical Value = 0. Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `p1[number]`: Real power values for endpoints (P).  Typical Value = 0.3. Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `p10[number]`: Real power values for endpoints (P). Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `p2[number]`: Real power values for endpoints (P).  Typical Value = 0.6. Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `p3[number]`: Real power values for endpoints (P).  Typical Value = 0.9. Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `p4[number]`: Real power values for endpoints (P).  Typical Value = 1.02. Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `p5[number]`: Real power values for endpoints (P). Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `p6[number]`: Real power values for endpoints (P). Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `p7[number]`: Real power values for endpoints (P). Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `p8[number]`: Real power values for endpoints (P). Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `p9[number]`: Real power values for endpoints (P). Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `q0[number]`: Reactive power values for endpoints (Q).  Typical Value = -0.31. Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `q1[number]`: Reactive power values for endpoints (Q).  Typical Value = -0.31. Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `q10[number]`: Reactive power values for endpoints (Q). Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `q2[number]`: Reactive power values for endpoints (Q).  Typical Value = -0.28. Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `q3[number]`: Reactive power values for endpoints (Q).  Typical Value = -0.21. Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `q4[number]`: Reactive power values for endpoints (Q).  Typical Value = 0. Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `q5[number]`: Reactive power values for endpoints (Q). Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `q6[number]`: Reactive power values for endpoints (Q). Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `q7[number]`: Reactive power values for endpoints (Q). Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `q8[number]`: Reactive power values for endpoints (Q). Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `q9[number]`: Reactive power values for endpoints (Q). Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `tu1[number]`: UEL lead time constant (T).  Typical Value = 0. Default: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tu2[number]`: UEL lag time constant (T).  Typical Value = 0. Default: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tu3[number]`: UEL lead time constant (T).  Typical Value = 0. Default: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tu4[number]`: UEL lag time constant (T).  Typical Value = 0. Default: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tul[number]`: Time constant associated with optional integrator feedback input signal to UEL (T).  Typical Value = 0. Default: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tup[number]`: Real power filter time constant (T).  Typical Value = 5. Default: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tuq[number]`: Reactive power filter time constant (T).  Typical Value = 0. Default: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tuv[number]`: Voltage filter time constant (T).  Typical Value = 5. Default: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI type. It has to be UnderexcLimIEEE2  - `vuimax[number]`: UEL integrator output maximum limit (V).  Typical Value = 0.25. Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vuimin[number]`: UEL integrator output minimum limit (V).  Typical Value = 0. Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vulmax[number]`: UEL output maximum limit (V).  Typical Value = 0.25. Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vulmin[number]`: UEL output minimum limit (V).  Typical Value = 0. Default: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
<!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Adapted from CIM data models and CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). This data model is a direct conversion of the Common Information Model (CIM) specified by the IEC61970 standard into smart data models. The python classes this model is based on were developed by these entities Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) and RWTH University Aachen, Germany. Some properties can have wrong type. This was the case, please raise an issue or send mail to info@smartdatamodels.org.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
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
      x-ngsi:    
        type: Property    
    k1:    
      description: 'UEL terminal voltage exponent applied to real power input to UEL limit look-up table (k1).  Typical Value = 2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    k2:    
      description: 'UEL terminal voltage exponent applied to reactive power output from UEL limit look-up table (k2).  Typical Value = 2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kfb:    
      description: 'Gain associated with optional integrator feedback input signal to UEL (K).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kuf:    
      description: 'UEL excitation system stabilizer gain (K).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kui:    
      description: 'UEL integral gain (K).  Typical Value = 0.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kul:    
      description: 'UEL proportional gain (K).  Typical Value = 0.8. Default: 0.0'    
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
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *underexclimieee2_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    p0:    
      description: 'Real power values for endpoints (P).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    p1:    
      description: 'Real power values for endpoints (P).  Typical Value = 0.3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    p10:    
      description: 'Real power values for endpoints (P). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    p2:    
      description: 'Real power values for endpoints (P).  Typical Value = 0.6. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    p3:    
      description: 'Real power values for endpoints (P).  Typical Value = 0.9. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    p4:    
      description: 'Real power values for endpoints (P).  Typical Value = 1.02. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    p5:    
      description: 'Real power values for endpoints (P). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    p6:    
      description: 'Real power values for endpoints (P). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    p7:    
      description: 'Real power values for endpoints (P). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    p8:    
      description: 'Real power values for endpoints (P). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    p9:    
      description: 'Real power values for endpoints (P). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    q0:    
      description: 'Reactive power values for endpoints (Q).  Typical Value = -0.31. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    q1:    
      description: 'Reactive power values for endpoints (Q).  Typical Value = -0.31. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    q10:    
      description: 'Reactive power values for endpoints (Q). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    q2:    
      description: 'Reactive power values for endpoints (Q).  Typical Value = -0.28. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    q3:    
      description: 'Reactive power values for endpoints (Q).  Typical Value = -0.21. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    q4:    
      description: 'Reactive power values for endpoints (Q).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    q5:    
      description: 'Reactive power values for endpoints (Q). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    q6:    
      description: 'Reactive power values for endpoints (Q). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    q7:    
      description: 'Reactive power values for endpoints (Q). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    q8:    
      description: 'Reactive power values for endpoints (Q). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    q9:    
      description: 'Reactive power values for endpoints (Q). Default: 0.0'    
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
    tu1:    
      description: 'UEL lead time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tu2:    
      description: 'UEL lag time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tu3:    
      description: 'UEL lead time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tu4:    
      description: 'UEL lag time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tul:    
      description: 'Time constant associated with optional integrator feedback input signal to UEL (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tup:    
      description: 'Real power filter time constant (T).  Typical Value = 5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tuq:    
      description: 'Reactive power filter time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tuv:    
      description: 'Voltage filter time constant (T).  Typical Value = 5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be UnderexcLimIEEE2'    
      enum:    
        - UnderexcLimIEEE2    
      type: string    
      x-ngsi:    
        type: Property    
    vuimax:    
      description: 'UEL integrator output maximum limit (V).  Typical Value = 0.25. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vuimin:    
      description: 'UEL integrator output minimum limit (V).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vulmax:    
      description: 'UEL output maximum limit (V).  Typical Value = 0.25. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vulmin:    
      description: 'UEL output minimum limit (V).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/UnderexcLimIEEE2/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/UnderexcLimIEEE2/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
Not available the example of a UnderexcLimIEEE2 in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
Not available the example of a UnderexcLimIEEE2 in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
Not available the example of a UnderexcLimIEEE2 in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
Not available the example of a UnderexcLimIEEE2 in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
