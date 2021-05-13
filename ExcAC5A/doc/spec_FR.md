Entité : ExcAC5A  
================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExcAC5A/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Adapté des modèles de données du CIM. Système d'excitation redresseur alimenté par un alternateur IEEE AC5A modifié avec une sortie minimale différente du contrôleur.**  

## Liste des propriétés  

- `a`: Coefficient permettant une utilisation différente du modèle (a).  Valeur typique = 1. Valeur par défaut : 0.0  - `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `efd1`: Tension d'excitation à laquelle la saturation de l'excitation est définie (Efd1).  Valeur typique = 5.6. Valeur par défaut : 0.0  - `efd2`: Tension d'excitation à laquelle la saturation de l'excitation est définie (Efd2).  Valeur typique = 4,2. Valeur par défaut : 0.0  - `id`: Identifiant unique de l'entité  - `ka`: Gain du régulateur de tension (Ka).  Valeur typique = 400. Valeur par défaut : 0.0  - `ke`: Constante d'excitation liée au champ auto-excité (Ke).  Valeur typique = 1. Valeur par défaut : 0.0  - `kf`: Gains des stabilisateurs du système de contrôle d'excitation (Kf).  Valeur typique = 0.03. Valeur par défaut : 0.0  - `ks`: Coefficient permettant une utilisation différente du coefficient de vitesse du modèle (Ks).  Valeur typique = 0. Valeur par défaut : 0.0  - `location`:   - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `seefd1`: Valeur de la fonction de saturation de l'excitatrice à la tension d'excitation correspondante, Efd1 (S[Efd1]).  Valeur typique = 0.86. Valeur par défaut : 0.0  - `seefd2`: Valeur de la fonction de saturation de l'excitatrice à la tension d'excitation correspondante, Efd2 (S[Efd2]).  Valeur typique = 0,5. Valeur par défaut : 0.0  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `ta`: Constante de temps du régulateur de tension (Ta).  Valeur typique = 0.02. Valeur par défaut : 0  - `tb`: Constante de temps du régulateur de tension (Tb).  Valeur typique = 0. Valeur par défaut : 0  - `tc`: Constante de temps du régulateur de tension (Tc).  Valeur typique = 0. Valeur par défaut : 0  - `te`: Constante de temps de l'excitateur, taux d'intégration associé à la commande de l'excitateur (Te).  Valeur typique = 0,8. Valeur par défaut : 0  - `tf1`: Constante de temps du stabilisateur du système de commande d'excitation (Tf1).  Valeur typique = 1. Valeur par défaut : 0  - `tf2`: Constante de temps du stabilisateur du système de commande d'excitation (Tf2).  Valeur typique = 0,8. Valeur par défaut : 0  - `tf3`: Constante de temps du stabilisateur du système de commande d'excitation (Tf3).  Valeur typique = 0. Valeur par défaut : 0  - `type`: Type NGSI. Il doit être ExcAC5A  - `vrmax`: Sortie maximale du régulateur de tension (Vrmax).  Valeur typique = 7.3. Valeur par défaut : 0.0  - `vrmin`: Sortie minimale du régulateur de tension (Vrmin).  Valeur typique =-7.3. Valeur par défaut : 0.0    
Propriétés requises  
Adapté de CIM data models and CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Ce modèle de données est une conversion directe du modèle d'information commun (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un mauvais type. Si tel était le cas, veuillez soulever un problème ou envoyer un courrier à info@smartdatamodels.org.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ExcAC5A:    
  description: 'Adapted from CIM data models. Modified IEEE AC5A alternator-supplied rectifier excitation system with different minimum controller output.'    
  properties:    
    a:    
      description: 'Coefficient to allow different usage of the model (a).  Typical Value = 1. Default: 0.0'    
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
    efd1:    
      description: 'Exciter voltage at which exciter saturation is defined (Efd1).  Typical Value = 5.6. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    efd2:    
      description: 'Exciter voltage at which exciter saturation is defined (Efd2).  Typical Value = 4.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &excac5a_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Voltage regulator gain (Ka).  Typical Value = 400. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ke:    
      description: 'Exciter constant related to self-excited field (Ke).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kf:    
      description: 'Excitation control system stabilizer gains (Kf).  Typical Value = 0.03. Default: 0.0'    
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
        anyOf: *excac5a_-_properties_-_owner_-_items_-_anyof    
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
    seefd1:    
      description: 'Exciter saturation function value at the corresponding exciter voltage, Efd1 (S[Efd1]).  Typical Value = 0.86. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    seefd2:    
      description: 'Exciter saturation function value at the corresponding exciter voltage, Efd2 (S[Efd2]).  Typical Value = 0.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    ta:    
      description: 'Voltage regulator time constant (Ta).  Typical Value = 0.02. Default: 0'    
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
      description: 'Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 0.8. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tf1:    
      description: 'Excitation control system stabilizer time constant (Tf1).  Typical Value  = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tf2:    
      description: 'Excitation control system stabilizer time constant (Tf2).  Typical Value = 0.8. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tf3:    
      description: 'Excitation control system stabilizer time constant (Tf3).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be ExcAC5A'    
      enum:    
        - ExcAC5A    
      type: Property    
    vrmax:    
      description: 'Maximum voltage regulator output (Vrmax).  Typical Value = 7.3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vrmin:    
      description: 'Minimum voltage regulator output (Vrmin).  Typical Value =-7.3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un ExcAC5A au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-v2 en utilisant `options=keyValues` et retourne les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un ExcAC5A au format JSON-LD tel que normalisé. Ceci est compatible avec NGSI-v2 lorsqu'on n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un ExcAC5A au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-LD quand on utilise `options=keyValues` et retourne les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un ExcAC5A au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
