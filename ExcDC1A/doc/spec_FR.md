Entité : ExcDC1A  
================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExcDC1A/LICENSE.md)  
Description globale : **Adapté des modèles de données CIM. Excitateur à collecteur en courant continu IEEE DC1A modifié avec entrée de vitesse et sans entrée de limiteur de sous-excitation (UEL).**  

## Liste des biens  

- `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `edfmax`: Limiteur de sortie de l'excitateur à tension maximale (Efdmax).  Valeur typique = 99. Valeur par défaut : 0,0  - `efd1`: Tension d'excitation à laquelle la saturation de l'excitateur est définie (Efd1).  Valeur typique = 3,1. Valeur par défaut : 0,0  - `efd2`: Tension d'excitation à laquelle la saturation de l'excitateur est définie (Efd2).  Valeur typique = 2,3. Valeur par défaut : 0,0  - `efdmin`: Limiteur de sortie de l'excitateur à tension minimale (Efdmin).  Valeur typique = -99. Valeur par défaut : 0,0  - `exclim`: (exclu). La norme IEEE est ambiguë en ce qui concerne la limite inférieure de la sortie de l'excitateur. vrai = une limite inférieure de zéro est appliquée à la sortie de l'intégrateur faux = une limite inférieure de zéro n'est pas appliquée à la sortie de l'intégrateur. Valeur typique = vrai. Par défaut : False  - `id`: Identifiant unique de l'entité  - `ka`: Gain du régulateur de tension (Ka).  Valeur typique = 46. Valeur par défaut : 0,0  - `ke`: Constante d'excitation liée au champ d'auto-excitation (Ke).  Valeur typique = 0, valeur par défaut : 0,0  - `kf`: Gain stabilisateur du système de contrôle de l'excitation (Kf).  Valeur typique = 0,1. Valeur par défaut : 0,0  - `ks`: Coefficient permettant une utilisation différente du coefficient de vitesse du modèle (Ks).  Valeur typique = 0, par défaut : 0,0  - `location`:   - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `seefd1`: Valeur de la fonction de saturation de l'excitateur à la tension d'excitation correspondante, Efd1 (Se [Eefd1]).  Valeur typique = 0,33. Valeur par défaut : 0,0  - `seefd2`: Valeur de la fonction de saturation de l'excitateur à la tension d'excitation correspondante, Efd1 (Se [Eefd1]).  Valeur typique = 0,33. Valeur par défaut : 0,0  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `ta`: Constante de temps du régulateur de tension (Ta).  Valeur typique = 0,06. Valeur par défaut : 0  - `tb`: Constante de temps du régulateur de tension (Tb).  Valeur typique = 0, par défaut : 0  - `tc`: Constante de temps du régulateur de tension (Tc).  Valeur typique = 0, par défaut : 0  - `te`: Constante de temps de l'excitateur, taux d'intégration associé au contrôle de l'excitateur (Te).  Valeur typique = 0,46. Valeur par défaut : 0  - `tf`: Constante de temps du stabilisateur du système de contrôle de l'excitation (Tf).  Valeur typique = 1. Valeur par défaut : 0  - `type`: Type NGSI. Il doit être de type ExcDC1A  - `vrmax`: Sortie maximale du régulateur de tension (Vrmax).  Valeur typique = 1. Valeur par défaut : 0,0  - `vrmin`: Sortie minimale du régulateur de tension (Vrmin).  Valeur typique = -0,9. Valeur par défaut : 0,0    
Propriétés requises  
Ce modèle de données est une conversion directe du modèle commun d'information (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un mauvais type. C'est le cas, pelase soulever un problème ou envoyer un mail à alberto.abella@fiware.org  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ExcDC1A:    
  description: 'Adapted from CIM data models. Modified IEEE DC1A direct current commutator exciter with speed input and without underexcitation limiters (UEL) inputs.'    
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
    edfmax:    
      description: 'Maximum voltage exciter output limiter (Efdmax).  Typical Value = 99. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    efd1:    
      description: 'Exciter voltage at which exciter saturation is defined (Efd1).  Typical Value = 3.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    efd2:    
      description: 'Exciter voltage at which exciter saturation is defined (Efd2).  Typical Value = 2.3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    efdmin:    
      description: 'Minimum voltage exciter output limiter (Efdmin).  Typical Value = -99. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    exclim:    
      description: '(exclim). IEEE standard is ambiguous about lower limit on exciter output.  true = a lower limit of zero is applied to integrator output false = a lower limit of zero is not applied to integrator output. Typical Value = true. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &excdc1a_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Voltage regulator gain (Ka).  Typical Value = 46. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ke:    
      description: 'Exciter constant related to self-excited field (Ke).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kf:    
      description: 'Excitation control system stabilizer gain (Kf).  Typical Value = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ks:    
      description: 'Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0. Default: 0.0'    
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
        anyOf: *excdc1a_-_properties_-_owner_-_items_-_anyof    
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
    seefd1:    
      description: 'Exciter saturation function value at the corresponding exciter voltage, Efd1 (Se[Eefd1]).  Typical Value = 0.33. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    seefd2:    
      description: 'Exciter saturation function value at the corresponding exciter voltage, Efd1 (Se[Eefd1]).  Typical Value = 0.33. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    ta:    
      description: 'Voltage regulator time constant (Ta).  Typical Value = 0.06. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tb:    
      description: 'Voltage regulator time constant (Tb).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tc:    
      description: 'Voltage regulator time constant (Tc).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    te:    
      description: 'Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 0.46. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tf:    
      description: 'Excitation control system stabilizer time constant (Tf).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be ExcDC1A'    
      enum:    
        - ExcDC1A    
      type: Property    
    vrmax:    
      description: 'Maximum voltage regulator output (Vrmax).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vrmin:    
      description: 'Minimum voltage regulator output (Vrmin).  Typical Value = -0.9. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un ExcDC1A en format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsque l'on utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un ExcDC1A en format JSON comme normalisé. Il est compatible avec la version 2 du NGSI lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un ExcDC1A en format JSON-LD comme valeurs clés. Il est compatible avec le format JSON-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un ExcDC1A en format JSON-LD comme normalisé. Il est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
