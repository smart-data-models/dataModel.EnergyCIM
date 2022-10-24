<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : UnderexcLimIEEE2  
=========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/UnderexcLimIEEE2/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Adaptée des modèles de données CIM. La classe représente le type UEL2 qui présente une caractéristique linéaire ou multisegmentaire lorsqu'il est tracé en termes de puissance réactive de la machine par rapport à la puissance réelle.  Référence : IEEE UEL2 421.5-2005 Section 10.2 (tableau de consultation des caractéristiques des limites présenté à la Figure 10.4 (p 32) de la norme).  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour cet élément  - `areaServed[string]`: La zone géographique où un service ou un article offert est fourni  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified[string]`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description[string]`: Une description de cet article  - `id[*]`: Identifiant unique de l'entité  - `k1[number]`: Exposant de la tension aux bornes de l'UEL appliqué à la puissance réelle entrée dans la table de consultation des limites de l'UEL (k1).  Valeur typique = 2. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `k2[number]`: Exposant de la tension aux bornes de l'UEL appliqué à la sortie de la puissance réactive à partir de la table de consultation des limites de l'UEL (k2).  Valeur typique = 2. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kfb[number]`: Gain associé au signal d'entrée de rétroaction de l'intégrateur optionnel vers UEL (K).  Valeur typique = 0. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kuf[number]`: Gain du stabilisateur du système d'excitation UEL (K).  Valeur typique = 0. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kui[number]`: Gain intégral de l'UEL (K).  Valeur typique = 0.5. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kul[number]`: Gain proportionnel de l'UEL (K).  Valeur typique = 0.8. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément.  - `owner[array]`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `p0[number]`: Valeurs de la puissance réelle pour les points finaux (P).  Valeur typique = 0. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `p1[number]`: Valeurs de la puissance réelle pour les points finaux (P).  Valeur typique = 0.3. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `p10[number]`: Valeurs de la puissance réelle pour les points finaux (P). Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `p2[number]`: Valeurs de la puissance réelle pour les points finaux (P).  Valeur typique = 0.6. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `p3[number]`: Valeurs de la puissance réelle pour les points finaux (P).  Valeur typique = 0.9. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `p4[number]`: Valeurs de puissance réelle pour les points finaux (P).  Valeur typique = 1.02. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `p5[number]`: Valeurs de la puissance réelle pour les points finaux (P). Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `p6[number]`: Valeurs de la puissance réelle pour les points finaux (P). Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `p7[number]`: Valeurs de la puissance réelle pour les points finaux (P). Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `p8[number]`: Valeurs de la puissance réelle pour les points finaux (P). Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `p9[number]`: Valeurs de la puissance réelle pour les points finaux (P). Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `q0[number]`: Valeurs de la puissance réactive pour les points d'extrémité (Q).  Valeur typique = -0.31. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `q1[number]`: Valeurs de la puissance réactive pour les points d'extrémité (Q).  Valeur typique = -0.31. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `q10[number]`: Valeurs de la puissance réactive pour les points d'extrémité (Q). Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `q2[number]`: Valeurs de la puissance réactive pour les points d'extrémité (Q).  Valeur typique = -0.28. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `q3[number]`: Valeurs de la puissance réactive pour les points d'extrémité (Q).  Valeur typique = -0.21. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `q4[number]`: Valeurs de la puissance réactive pour les points d'extrémité (Q).  Valeur typique = 0. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `q5[number]`: Valeurs de la puissance réactive pour les points d'extrémité (Q). Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `q6[number]`: Valeurs de la puissance réactive pour les points d'extrémité (Q). Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `q7[number]`: Valeurs de la puissance réactive pour les points d'extrémité (Q). Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `q8[number]`: Valeurs de la puissance réactive pour les points d'extrémité (Q). Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `q9[number]`: Valeurs de la puissance réactive pour les points d'extrémité (Q). Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires sur l'article  - `source[string]`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `tu1[number]`: Constante de temps de plomb UEL (T).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tu2[number]`: Constante de temps du décalage UEL (T).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tu3[number]`: Constante de temps de plomb UEL (T).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tu4[number]`: Constante de temps du décalage UEL (T).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tul[number]`: Constante de temps associée au signal d'entrée de retour de l'intégrateur optionnel vers UEL (T).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tup[number]`: Constante de temps du filtre de puissance réelle (T).  Valeur typique = 5. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tuq[number]`: Constante de temps du filtre de puissance réactive (T).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tuv[number]`: Constante de temps du filtre de tension (T).  Valeur typique = 5. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Type NGSI. Il doit être UnderexcLimIEEE2.  - `vuimax[number]`: Limite maximale de la sortie de l'intégrateur UEL (V).  Valeur typique = 0.25. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vuimin[number]`: Limite minimale de la sortie de l'intégrateur UEL (V).  Valeur typique = 0. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vulmax[number]`: Limite maximale de la sortie UEL (V).  Valeur typique = 0.25. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vulmin[number]`: Limite minimale de la sortie UEL (V).  Valeur typique = 0. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
<!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Adapté de CIM data models and CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Ce modèle de données est une conversion directe du modèle d'information commun (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un mauvais type. Si tel était le cas, veuillez soulever un problème ou envoyer un courrier à info@smartdatamodels.org.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
## Exemples de charges utiles  
Non disponible l'exemple d'un UnderexcLimIEEE2 en format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un UnderexcLimIEEE2 au format JSON-LD tel que normalisé. Ceci est compatible avec la NGSI-v2 lorsqu'elle n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un UnderexcLimIEEE2 en format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un UnderexcLimIEEE2 au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
