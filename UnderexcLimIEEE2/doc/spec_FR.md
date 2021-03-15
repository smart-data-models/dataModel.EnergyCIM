Entité : UnderexcLimIEEE2  
=========================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/UnderexcLimIEEE2/LICENSE.md)  
Description globale : **Adaptée des modèles de données CIM. La classe représente le type UEL2 qui présente une caractéristique linéaire ou multisegmentaire lorsqu'il est tracé en termes de puissance réactive de la machine par rapport à la puissance réelle.  Référence : IEEE UEL2 421.5-2005 Section 10.2 (tableau de consultation des caractéristiques des limites présenté à la Figure 10.4 (p 32) de la norme).  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `k1`: Exposant de la tension aux bornes de l'UEL appliqué à la puissance réelle entrée dans la table de consultation des limites de l'UEL (k1).  Valeur typique = 2. Valeur par défaut : 0.0  - `k2`: Exposant de la tension aux bornes de l'UEL appliqué à la sortie de la puissance réactive à partir de la table de consultation des limites de l'UEL (k2).  Valeur typique = 2. Valeur par défaut : 0.0  - `kfb`: Gain associé au signal d'entrée de rétroaction de l'intégrateur optionnel vers UEL (K).  Valeur typique = 0. Valeur par défaut : 0.0  - `kuf`: Gain du stabilisateur du système d'excitation UEL (K).  Valeur typique = 0. Valeur par défaut : 0.0  - `kui`: Gain intégral de l'UEL (K).  Valeur typique = 0.5. Valeur par défaut : 0.0  - `kul`: Gain proportionnel de l'UEL (K).  Valeur typique = 0.8. Valeur par défaut : 0.0  - `location`:   - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `p0`: Valeurs de la puissance réelle pour les points finaux (P).  Valeur typique = 0. Valeur par défaut : 0.0  - `p1`: Valeurs de la puissance réelle pour les points finaux (P).  Valeur typique = 0.3. Valeur par défaut : 0.0  - `p10`: Valeurs de la puissance réelle pour les points finaux (P). Valeur par défaut : 0.0  - `p2`: Valeurs de la puissance réelle pour les points finaux (P).  Valeur typique = 0.6. Valeur par défaut : 0.0  - `p3`: Valeurs de la puissance réelle pour les points finaux (P).  Valeur typique = 0.9. Valeur par défaut : 0.0  - `p4`: Valeurs de puissance réelle pour les points finaux (P).  Valeur typique = 1.02. Valeur par défaut : 0.0  - `p5`: Valeurs de la puissance réelle pour les points finaux (P). Valeur par défaut : 0.0  - `p6`: Valeurs de la puissance réelle pour les points finaux (P). Valeur par défaut : 0.0  - `p7`: Valeurs de la puissance réelle pour les points finaux (P). Valeur par défaut : 0.0  - `p8`: Valeurs de la puissance réelle pour les points finaux (P). Valeur par défaut : 0.0  - `p9`: Valeurs de la puissance réelle pour les points finaux (P). Valeur par défaut : 0.0  - `q0`: Valeurs de la puissance réactive pour les points d'extrémité (Q).  Valeur typique = -0.31. Valeur par défaut : 0.0  - `q1`: Valeurs de la puissance réactive pour les points d'extrémité (Q).  Valeur typique = -0.31. Valeur par défaut : 0.0  - `q10`: Valeurs de la puissance réactive pour les points d'extrémité (Q). Valeur par défaut : 0.0  - `q2`: Valeurs de la puissance réactive pour les points d'extrémité (Q).  Valeur typique = -0.28. Valeur par défaut : 0.0  - `q3`: Valeurs de la puissance réactive pour les points d'extrémité (Q).  Valeur typique = -0.21. Valeur par défaut : 0.0  - `q4`: Valeurs de la puissance réactive pour les points d'extrémité (Q).  Valeur typique = 0. Valeur par défaut : 0.0  - `q5`: Valeurs de la puissance réactive pour les points d'extrémité (Q). Valeur par défaut : 0.0  - `q6`: Valeurs de la puissance réactive pour les points d'extrémité (Q). Valeur par défaut : 0.0  - `q7`: Valeurs de la puissance réactive pour les points d'extrémité (Q). Valeur par défaut : 0.0  - `q8`: Valeurs de la puissance réactive pour les points d'extrémité (Q). Valeur par défaut : 0.0  - `q9`: Valeurs de la puissance réactive pour les points d'extrémité (Q). Valeur par défaut : 0.0  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `tu1`: Constante de temps de plomb UEL (T).  Valeur typique = 0. Valeur par défaut : 0  - `tu2`: Constante de temps du décalage UEL (T).  Valeur typique = 0. Valeur par défaut : 0  - `tu3`: Constante de temps de plomb UEL (T).  Valeur typique = 0. Valeur par défaut : 0  - `tu4`: Constante de temps du décalage UEL (T).  Valeur typique = 0. Valeur par défaut : 0  - `tul`: Constante de temps associée au signal d'entrée de retour de l'intégrateur optionnel vers UEL (T).  Valeur typique = 0. Valeur par défaut : 0  - `tup`: Constante de temps du filtre de puissance réelle (T).  Valeur typique = 5. Valeur par défaut : 0  - `tuq`: Constante de temps du filtre de puissance réactive (T).  Valeur typique = 0. Valeur par défaut : 0  - `tuv`: Constante de temps du filtre de tension (T).  Valeur typique = 5. Valeur par défaut : 0  - `type`: Type NGSI. Il doit être UnderexcLimIEEE2.  - `vuimax`: Limite maximale de la sortie de l'intégrateur UEL (V).  Valeur typique = 0.25. Valeur par défaut : 0.0  - `vuimin`: Limite minimale de la sortie de l'intégrateur UEL (V).  Valeur typique = 0. Valeur par défaut : 0.0  - `vulmax`: Limite maximale de la sortie UEL (V).  Valeur typique = 0.25. Valeur par défaut : 0.0  - `vulmin`: Limite minimale de la sortie UEL (V).  Valeur typique = 0. Valeur par défaut : 0.0    
Propriétés requises  
Ce modèle de données est une conversion directe du modèle d'information commun (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un type incorrect. Si tel était le cas, veuillez soulever un problème ou envoyer un message à alberto.abella@fiware.org.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
## Exemples de charges utiles  
Non disponible l'exemple d'un UnderexcLimIEEE2 au format JSON comme valeurs-clés. Ceci est compatible avec NGSI V2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un UnderexcLimIEEE2 au format JSON tel que normalisé. Ceci est compatible avec la NGSI V2 lorsqu'elle n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un UnderexcLimIEEE2 en format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un UnderexcLimIEEE2 au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
