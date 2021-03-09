Entité : ExcST3A  
================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExcST3A/LICENSE.md)  
Description globale : **Adapté des modèles de données CIM. Système d'excitation statique IEEE ST3A modifié avec multiplicateur de vitesse ajouté.**  

## Liste des biens  

- `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `efdmax`: Sortie AVR maximale (Efdmax).  Valeur typique = 6,9. Valeur par défaut : 0,0  - `id`: Identifiant unique de l'entité  - `kc`: Facteur de charge du redresseur proportionnel à la réactance de commutation (Kc). Valeur typique = 1,1. Valeur par défaut : 0,0  - `kg`: Constante de gain de rétroaction du régulateur de champ de la boucle interne (Kg).  Valeur typique = 1. Valeur par défaut : 0,0  - `ki`: Coefficient de gain du circuit potentiel (Ki).  Valeur typique = 4,83. Valeur par défaut : 0,0  - `kj`: Gain de l'AVR (Kj).  Valeur typique = 200. Valeur par défaut : 0,0  - `km`: Constante de gain avant du régulateur de champ de la boucle intérieure (Km).  Valeur typique = 7,04. Valeur par défaut : 0,0  - `kp`: Gain potentiel de la source (Kp) (>0).  Valeur typique = 4,37. Valeur par défaut : 0,0  - `ks`: Coefficient permettant une utilisation différente du coefficient de vitesse du modèle (Ks).  Valeur typique = 0, par défaut : 0,0  - `ks1`: Coefficient permettant une utilisation différente du coefficient de vitesse du modèle (Ks1).  Valeur typique = 0, par défaut : 0,0  - `location`:   - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `tb`: Constante de temps du régulateur de tension (Tb).  Valeur typique = 6,67. Valeur par défaut : 0  - `tc`: Constante de temps du régulateur de tension (Tc).  Valeur typique = 1. Valeur par défaut : 0  - `thetap`: Angle de phase du circuit potentiel (thetap).  Valeur typique = 20. Valeur par défaut : 0,0  - `tm`: Constante de temps du régulateur de champ de la boucle interne (Tm).  Valeur typique = 1. Valeur par défaut : 0  - `type`: Type NGSI. Il doit être de type ExcST3A  - `vbmax`: Tension d'excitation maximale (Vbmax).  Valeur typique = 8,63. Valeur par défaut : 0,0  - `vgmax`: Tension de rétroaction maximale de la boucle interne (Vgmax).  Valeur typique = 6,53. Valeur par défaut : 0,0  - `vimax`: Limite maximale d'entrée du régulateur de tension (Vimax).  Valeur typique = 0,2. Valeur par défaut : 0,0  - `vimin`: Limite minimale d'entrée du régulateur de tension (Vimin).  Valeur typique = -0,2. Valeur par défaut : 0,0  - `vrmax`: Sortie maximale du régulateur de tension (Vrmax).  Valeur typique = 1. Valeur par défaut : 0,0  - `vrmin`: Sortie minimale du régulateur de tension (Vrmin).  Valeur typique = 0, par défaut : 0,0  - `xl`: Réaction associée à la source potentielle (Xl).  Valeur typique = 0,09. Valeur par défaut : 0,0    
Propriétés requises  
Ce modèle de données est une conversion directe du modèle commun d'information (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un mauvais type. C'est le cas, pelase soulever un problème ou envoyer un mail à alberto.abella@fiware.org  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ExcST3A:    
  description: 'Adapted from CIM data models. Modified IEEE ST3A static excitation system with added speed multiplier.'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/Text'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/Text'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/Text'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/Text'''    
          type: string    
      type: Property    
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
    efdmax:    
      description: 'Maximum AVR output (Efdmax).  Typical Value = 6.9. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &excst3a_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Rectifier loading factor proportional to commutating reactance (Kc). Typical Value = 1.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kg:    
      description: 'Feedback gain constant of the inner loop field regulator (Kg).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ki:    
      description: 'Potential circuit gain coefficient (Ki).  Typical Value = 4.83. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kj:    
      description: 'AVR gain (Kj).  Typical Value = 200. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    km:    
      description: 'Forward gain constant of the inner loop field regulator (Km).  Typical Value = 7.04. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kp:    
      description: 'Potential source gain (Kp) (>0).  Typical Value = 4.37. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ks:    
      description: 'Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ks1:    
      description: 'Coefficient to allow different usage of the model-speed coefficient (Ks1).  Typical Value = 0. Default: 0.0'    
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
        anyOf: *excst3a_-_properties_-_owner_-_items_-_anyof    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    tb:    
      description: 'Voltage regulator time constant (Tb).  Typical Value = 6.67. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tc:    
      description: 'Voltage regulator time constant (Tc).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    thetap:    
      description: 'Potential circuit phase angle (thetap).  Typical Value = 20. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tm:    
      description: 'Forward time constant of inner loop field regulator (Tm).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be ExcST3A'    
      enum:    
        - ExcST3A    
      type: Property    
    vbmax:    
      description: 'Maximum excitation voltage (Vbmax).  Typical Value = 8.63. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vgmax:    
      description: 'Maximum inner loop feedback voltage (Vgmax).  Typical Value = 6.53. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vimax:    
      description: 'Maximum voltage regulator input limit (Vimax).  Typical Value = 0.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vimin:    
      description: 'Minimum voltage regulator input limit (Vimin).  Typical Value = -0.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vrmax:    
      description: 'Maximum voltage regulator output (Vrmax).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vrmin:    
      description: 'Minimum voltage regulator output (Vrmin).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    xl:    
      description: 'Reactance associated with potential source (Xl).  Typical Value = 0.09. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un ExcST3A en format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsque l'on utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un ExcST3A en format JSON comme normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un ExcST3A en format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un ExcST3A en format JSON-LD comme normalisé. Il est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
