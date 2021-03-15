Entité : PssPTIST3  
==================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/PssPTIST3/LICENSE.md)  
Description globale : **Adapté des modèles de données CIM. Stabilisateur à microprocesseur PTI type 3.**  

## Liste des propriétés  

- `a0`: Coefficient de filtrage (A0). Valeur par défaut : 0.0  - `a1`: Limiteur (Al). Valeur par défaut : 0.0  - `a2`: Coefficient de filtrage (A2). Valeur par défaut : 0.0  - `a3`: Coefficient de filtrage (A3). Valeur par défaut : 0.0  - `a4`: Coefficient de filtrage (A4). Valeur par défaut : 0.0  - `a5`: Coefficient de filtrage (A5). Valeur par défaut : 0.0  - `address`: L'adresse postale  - `al`: Limiteur (Al). Valeur par défaut : 0.0  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `athres`: Valeur seuil au-dessus de laquelle le moyennage de sortie sera contourné (Athres).  Valeur typique = 0.005. Valeur par défaut : 0.0  - `b0`: Coefficient de filtrage (B0). Valeur par défaut : 0.0  - `b1`: Coefficient de filtrage (B1). Valeur par défaut : 0.0  - `b2`: Coefficient de filtrage (B2). Valeur par défaut : 0.0  - `b3`: Coefficient de filtrage (B3). Valeur par défaut : 0.0  - `b4`: Coefficient de filtrage (B4). Valeur par défaut : 0.0  - `b5`: Coefficient de filtrage (B5). Valeur par défaut : 0.0  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `dl`: Limiteur (Dl). Valeur par défaut : 0.0  - `dtc`: Pas de temps lié à l'activation des contrôles (0.03 pour 50 Hz) (Dtc).  Valeur typique = 0.025. Valeur par défaut : 0  - `dtf`: Calcul de la fréquence du pas de temps (0,03 pour 50 Hz) (Dtf).  Valeur typique = 0.025. Valeur par défaut : 0  - `dtp`: Calcul de la puissance active par pas de temps (0.015 pour 50 Hz) (Dtp).  Valeur typique = 0.0125. Valeur par défaut : 0  - `id`: Identifiant unique de l'entité  - `isw`: Commutateur de sortie numérique/analogique (Isw). true = produire une sortie analogique false = convertir en sortie numérique, en utilisant le tableau de sélection des robinets. Défaut : Faux  - `k`: Gain (K).  Valeur typique = 9. Valeur par défaut : 0.0  - `location`:   - `lthres`: Valeur du seuil (Lthres). Valeur par défaut : 0.0  - `m`: (M).  M=2*H.  Valeur typique = 5. Valeur par défaut : 0.0  - `name`: Le nom de cet élément.  - `nav`: Nombre de sorties de contrôle à moyenner (Nav) (1 <= Nav <= 16).  Valeur typique = 4. Valeur par défaut : 0.0  - `ncl`: Nombre de comptes à la limite pour activer la fonction de limite (Ncl) (>0). Valeur par défaut : 0.0  - `ncr`: Nombre de comptes jusqu'à la réinitialisation après le déclenchement de la fonction de limite (Ncr). Valeur par défaut : 0.0  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `pmin`: (Pmin). Valeur par défaut : 0.0  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `t1`: Constante de temps (T1).  Valeur typique = 0,3. Valeur par défaut : 0  - `t2`: Constante de temps (T2).  Valeur typique = 1. Valeur par défaut : 0  - `t3`: Constante de temps (T3).  Valeur typique = 0,2. Valeur par défaut : 0  - `t4`: Constante de temps (T4).  Valeur typique = 0,05. Valeur par défaut : 0  - `t5`: Constante de temps (T5). Valeur par défaut : 0  - `t6`: Constante de temps (T6). Valeur par défaut : 0  - `tf`: Constante de temps (Tf).  Valeur typique = 0,2. Valeur par défaut : 0  - `tp`: Constante de temps (Tp).  Valeur typique = 0,2. Valeur par défaut : 0  - `type`: Type NGSI. Il doit être PssPTIST3.    
Propriétés requises  
Ce modèle de données est une conversion directe du modèle d'information commun (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un type incorrect. Si tel était le cas, veuillez soulever un problème ou envoyer un message à alberto.abella@fiware.org.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PssPTIST3:    
  description: 'Adapted from CIM data models. PTI Microprocessor-Based Stabilizer type 3.'    
  properties:    
    a0:    
      description: 'Filter coefficient (A0). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    a1:    
      description: 'Limiter (Al). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    a2:    
      description: 'Filter coefficient (A2). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    a3:    
      description: 'Filter coefficient (A3). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    a4:    
      description: 'Filter coefficient (A4). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    a5:    
      description: 'Filter coefficient (A5). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    al:    
      description: 'Limiter (Al). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    athres:    
      description: 'Threshold value above which output averaging will be bypassed (Athres).  Typical Value = 0.005. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    b0:    
      description: 'Filter coefficient (B0). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    b1:    
      description: 'Filter coefficient (B1). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    b2:    
      description: 'Filter coefficient (B2). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    b3:    
      description: 'Filter coefficient (B3). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    b4:    
      description: 'Filter coefficient (B4). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    b5:    
      description: 'Filter coefficient (B5). Default: 0.0'    
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
    dl:    
      description: 'Limiter (Dl). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    dtc:    
      description: 'Time step related to activation of controls (0.03 for 50 Hz) (Dtc).  Typical Value = 0.025. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    dtf:    
      description: 'Time step frequency calculation (0.03 for 50 Hz) (Dtf).  Typical Value = 0.025. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    dtp:    
      description: 'Time step active power calculation (0.015 for 50 Hz) (Dtp).  Typical Value = 0.0125. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &pssptist3_-_properties_-_owner_-_items_-_anyof    
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
    isw:    
      description: 'Digital/analog output switch (Isw). true = produce analog output false = convert to digital output, using tap selection table. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    k:    
      description: 'Gain (K).  Typical Value = 9. Default: 0.0'    
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
    lthres:    
      description: 'Threshold value (Lthres). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    m:    
      description: '(M).  M=2*H.  Typical Value = 5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    name:    
      description: 'The name of this item.'    
      type: Property    
    nav:    
      description: 'Number of control outputs to average (Nav) (1 <= Nav <= 16).  Typical Value = 4. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ncl:    
      description: 'Number of counts at limit to active limit function (Ncl) (>0). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ncr:    
      description: 'Number of counts until reset after limit function is triggered (Ncr). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *pssptist3_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    pmin:    
      description: '(Pmin). Default: 0.0'    
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
    t1:    
      description: 'Time constant (T1).  Typical Value = 0.3. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t2:    
      description: 'Time constant (T2).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t3:    
      description: 'Time constant (T3).  Typical Value = 0.2. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t4:    
      description: 'Time constant (T4).  Typical Value = 0.05. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t5:    
      description: 'Time constant (T5). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    t6:    
      description: 'Time constant (T6). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tf:    
      description: 'Time constant (Tf).  Typical Value = 0.2. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tp:    
      description: 'Time constant (Tp).  Typical Value = 0.2. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be PssPTIST3'    
      enum:    
        - PssPTIST3    
      type: Property    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un PssPTIST3 au format JSON comme valeurs-clés. Ceci est compatible avec NGSI V2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un PssPTIST3 au format JSON tel que normalisé. Ceci est compatible avec la NGSI V2 lorsqu'elle n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un PssPTIST3 au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un PssPTIST3 au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
