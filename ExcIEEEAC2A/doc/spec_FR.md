Entité : ExcIEEEAC2A  
====================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExcIEEEAC2A/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Adapté des modèles de données CIM. La classe représente le modèle IEEE Std 421.5-2005 type AC2A. Le modèle représente un système d'excitation d'alternateur-rectificateur commandé par le champ à réponse initiale élevée. L'excitateur principal de l'alternateur est utilisé avec des redresseurs non contrôlés. Le modèle de type AC2A est similaire à celui du type AC1A sauf pour l'inclusion de la compensation de la constante de temps de l'excitatrice et des éléments de limitation du courant de champ de l'excitatrice.  Référence : IEEE Standard 421.5-2005 Section 6.2.**  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `ka`: Gain du régulateur de tension (K).  Valeur typique = 400. Valeur par défaut : 0.0  - `kb`: Gain du régulateur de deuxième étage (K).  Valeur typique = 25. Valeur par défaut : 0.0  - `kc`: Facteur de charge du redresseur proportionnel à la réactance de commutation (K).  Valeur typique = 0.28. Valeur par défaut : 0.0  - `kd`: Facteur de démagnétisation, fonction des réactances de l'alternateur de l'excitateur (K).  Valeur typique = 0,35. Valeur par défaut : 0,0  - `ke`: Constante d'excitation liée au champ auto-excité (K).  Valeur typique = 1. Valeur par défaut : 0.0  - `kf`: Gains des stabilisateurs du système de contrôle d'excitation (K).  Valeur typique = 0.03. Valeur par défaut : 0.0  - `kh`: Gain de rétroaction du courant d'excitation de l'excitateur (K).  Valeur typique = 1. Valeur par défaut : 0.0  - `location`:   - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `seve1`: Valeur de la fonction de saturation de l'excitatrice à la tension correspondante de l'excitatrice, V, en arrière de la réactance de commutation (S[V]).  Valeur typique = 0.037. Valeur par défaut : 0.0  - `seve2`: Valeur de la fonction de saturation de l'excitatrice à la tension correspondante de l'excitatrice, V, en arrière de la réactance de commutation (S[V]).  Valeur typique = 0.012. Valeur par défaut : 0.0  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `ta`: Constante de temps du régulateur de tension (T).  Valeur typique = 0,02. Valeur par défaut : 0  - `tb`: Constante de temps du régulateur de tension (T).  Valeur typique = 0. Valeur par défaut : 0  - `tc`: Constante de temps du régulateur de tension (T).  Valeur typique = 0. Valeur par défaut : 0  - `te`: Constante de temps de l'excitatrice, taux d'intégration associé à la commande de l'excitatrice (T).  Valeur typique = 0,6. Valeur par défaut : 0  - `tf`: Constante de temps du stabilisateur du système de contrôle d'excitation (T).  Valeur typique = 1. Valeur par défaut : 0  - `type`: Type NGSI. Il doit être ExcIEEEAC2A  - `vamax`: Sortie maximale du régulateur de tension (V).  Valeur typique = 8. Valeur par défaut : 0.0  - `vamin`: Tension minimale de sortie du régulateur (V).  Valeur typique = -8. Valeur par défaut : 0.0  - `ve1`: Tensions de sortie de l'alternateur de l'excitateur en arrière de la réactance de commutation à laquelle la saturation est définie (V).  Valeur typique = 4.4. Valeur par défaut : 0,0  - `ve2`: Tensions de sortie de l'alternateur de l'excitateur en arrière de la réactance de commutation à laquelle la saturation est définie (V).  Valeur typique = 3.3. Valeur par défaut : 0,0  - `vfemax`: Référence de la limite de courant du champ d'excitation (V).  Valeur typique = 4,4. Valeur par défaut : 0,0  - `vrmax`: Sorties maximales du régulateur de tension (V).  Valeur typique = 105. Valeur par défaut : 0.0  - `vrmin`: Tension minimale des sorties du régulateur (V).  Valeur typique = -95. Valeur par défaut : 0.0    
Propriétés requises  
Adapté de CIM data models and CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Ce modèle de données est une conversion directe du modèle d'information commun (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un mauvais type. Si tel était le cas, veuillez soulever un problème ou envoyer un courrier à info@smartdatamodels.org.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ExcIEEEAC2A:    
  description: 'Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type AC2A model. The model represents a high initial response field-controlled alternator-rectifier excitation system. The alternator main exciter is used with non-controlled rectifiers. The Type AC2A model is similar to that of Type AC1A except for the inclusion of exciter time constant compensation and exciter field current limiting elements.  Reference: IEEE Standard 421.5-2005 Section 6.2.'    
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
      anyOf: &excieeeac2a_-_properties_-_owner_-_items_-_anyof    
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
    ka:    
      description: 'Voltage regulator gain (K).  Typical Value = 400. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kb:    
      description: 'Second stage regulator gain (K).  Typical Value = 25. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kc:    
      description: 'Rectifier loading factor proportional to commutating reactance (K).  Typical Value = 0.28. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kd:    
      description: 'Demagnetizing factor, a function of exciter alternator reactances (K).  Typical Value = 0.35. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ke:    
      description: 'Exciter constant related to self-excited field (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kf:    
      description: 'Excitation control system stabilizer gains (K).  Typical Value = 0.03. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kh:    
      description: 'Exciter field current feedback gain (K).  Typical Value = 1. Default: 0.0'    
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
        anyOf: *excieeeac2a_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
      type: Property    
    seve1:    
      description: 'Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance (S[V]).  Typical Value = 0.037. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    seve2:    
      description: 'Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance (S[V]).  Typical Value = 0.012. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    ta:    
      description: 'Voltage regulator time constant (T).  Typical Value = 0.02. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tb:    
      description: 'Voltage regulator time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tc:    
      description: 'Voltage regulator time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    te:    
      description: 'Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 0.6. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tf:    
      description: 'Excitation control system stabilizer time constant (T).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be ExcIEEEAC2A'    
      enum:    
        - ExcIEEEAC2A    
      type: Property    
    vamax:    
      description: 'Maximum voltage regulator output (V).  Typical Value = 8. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vamin:    
      description: 'Minimum voltage regulator output (V).  Typical Value = -8. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ve1:    
      description: 'Exciter alternator output voltages back of commutating reactance at which saturation is defined (V).  Typical Value = 4.4. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ve2:    
      description: 'Exciter alternator output voltages back of commutating reactance at which saturation is defined (V).  Typical Value = 3.3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vfemax:    
      description: 'Exciter field current limit reference (V).  Typical Value = 4.4. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vrmax:    
      description: 'Maximum voltage regulator outputs (V).  Typical Value = 105. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vrmin:    
      description: 'Minimum voltage regulator outputs (V).  Typical Value = -95. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un ExcIEEEAC2A au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-v2 quand on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un ExcIEEEAC2A au format JSON-LD tel que normalisé. Ceci est compatible avec la NGSI-v2 lorsqu'elle n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un ExcIEEEAC2A au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-LD quand on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un ExcIEEEAC2A au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
