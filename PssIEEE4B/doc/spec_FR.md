Entité : PssIEEE4B  
==================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/PssIEEE4B/LICENSE.md)  
Description globale : **Adapté des modèles de données CIM. La classe représente le modèle de stabilisateur de réseau électrique PSS2B de type IEEE Std 421.5-2005. Le modèle PSS4B représente une structure basée sur plusieurs bandes de fréquences de travail. Trois bandes distinctes, respectivement dédiées aux modes d'oscillations à basse, moyenne et haute fréquence, sont utilisées dans ce PSS delta-oméga (entrée vitesse).  Référence : IEEE 4B 421.5-2005, section 8.4.**.  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `bwh1`: Filtre coupe-bande 1 (bande haute fréquence) : Largeur de bande de trois dB (B). Valeur par défaut : 0.0  - `bwh2`: Filtre coupe-bande 2 (bande haute fréquence) : Largeur de bande de trois dB (B). Valeur par défaut : 0.0  - `bwl1`: Filtre coupe-bande 1 (bande basse fréquence) : Largeur de bande de trois dB (B). Valeur par défaut : 0.0  - `bwl2`: Filtre coupe-bande 2 (bande basse fréquence) : Largeur de bande de trois dB (B). Valeur par défaut : 0.0  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `kh`: Gain en bande haute (K).  Valeur typique = 120. Valeur par défaut : 0.0  - `kh1`: Gain du filtre différentiel à haute bande (K).  Valeur typique = 66. Valeur par défaut : 0.0  - `kh11`: Coefficient de blocage du premier lead-lag de la bande haute (K).  Valeur typique = 1. Valeur par défaut : 0.0  - `kh17`: Coefficient de blocage du premier lead-lag de la bande haute (K).  Valeur typique = 1. Valeur par défaut : 0.0  - `kh2`: Gain du filtre différentiel à haute bande (K).  Valeur typique = 66. Valeur par défaut : 0.0  - `ki`: Gain de la bande intermédiaire (K).  Valeur typique = 30. Valeur par défaut : 0.0  - `ki1`: Gain du filtre différentiel à bande intermédiaire (K).  Valeur typique = 66. Valeur par défaut : 0.0  - `ki11`: Coefficient de blocage du premier lead-lag de la bande intermédiaire (K).  Valeur typique = 1. Valeur par défaut : 0.0  - `ki17`: Coefficient de blocage du premier lead-lag de la bande intermédiaire (K).  Valeur typique = 1. Valeur par défaut : 0.0  - `ki2`: Gain du filtre différentiel à bande intermédiaire (K).  Valeur typique = 66. Valeur par défaut : 0.0  - `kl`: Gain en bande basse (K).  Valeur typique = 7.5. Valeur par défaut : 0.0  - `kl1`: Gain du filtre différentiel à basse bande (K).  Valeur typique = 66. Valeur par défaut : 0.0  - `kl11`: Coefficient de blocage du premier lead-lag de la bande basse (K).  Valeur typique = 1. Valeur par défaut : 0.0  - `kl17`: Coefficient de blocage du premier lead-lag de la bande basse (K).  Valeur typique = 1. Valeur par défaut : 0.0  - `kl2`: Gain du filtre différentiel à basse bande (K).  Valeur typique = 66. Valeur par défaut : 0.0  - `location`:   - `name`: Le nom de cet élément.  - `omeganh1`: Filtre Notch 1 (bande haute fréquence) : fréquence du filtre (oméga). Valeur par défaut : 0,0  - `omeganh2`: Filtre Notch 2 (bande haute fréquence) : fréquence du filtre (oméga). Valeur par défaut : 0,0  - `omeganl1`: Filtre Notch 1 (bande basse fréquence) : fréquence du filtre (oméga). Valeur par défaut : 0,0  - `omeganl2`: Filtre Notch 2 (bande basse fréquence) : fréquence du filtre (oméga). Valeur par défaut : 0,0  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `th1`: Constante de temps de la bande haute (T).  Valeur typique = 0.01513. Valeur par défaut : 0  - `th10`: Constante de temps de la bande haute (T).  Valeur typique = 0. Valeur par défaut : 0  - `th11`: Constante de temps de la bande haute (T).  Valeur typique = 0. Valeur par défaut : 0  - `th12`: Constante de temps de la bande haute (T).  Valeur typique = 0. Valeur par défaut : 0  - `th2`: Constante de temps de la bande haute (T).  Valeur typique = 0.01816. Valeur par défaut : 0  - `th3`: Constante de temps de la bande haute (T).  Valeur typique = 0. Valeur par défaut : 0  - `th4`: Constante de temps de la bande haute (T).  Valeur typique = 0. Valeur par défaut : 0  - `th5`: Constante de temps de la bande haute (T).  Valeur typique = 0. Valeur par défaut : 0  - `th6`: Constante de temps de la bande haute (T).  Valeur typique = 0. Valeur par défaut : 0  - `th7`: Constante de temps de la bande haute (T).  Valeur typique = 0.01816. Valeur par défaut : 0  - `th8`: Constante de temps de la bande haute (T).  Valeur typique = 0.02179. Valeur par défaut : 0  - `th9`: Constante de temps de la bande haute (T).  Valeur typique = 0. Valeur par défaut : 0  - `ti1`: Constante de temps de la bande intermédiaire (T).  Valeur typique = 0.173. Valeur par défaut : 0  - `ti10`: Constante de temps de la bande intermédiaire (T).  Valeur typique = 0. Valeur par défaut : 0  - `ti11`: Constante de temps de la bande intermédiaire (T).  Valeur typique = 0. Valeur par défaut : 0  - `ti12`: Constante de temps de la bande intermédiaire (T).  Valeur typique = 0. Valeur par défaut : 0  - `ti2`: Constante de temps de la bande intermédiaire (T).  Valeur typique = 0.2075. Valeur par défaut : 0  - `ti3`: Constante de temps de la bande intermédiaire (T).  Valeur typique = 0. Valeur par défaut : 0  - `ti4`: Constante de temps de la bande intermédiaire (T).  Valeur typique = 0. Valeur par défaut : 0  - `ti5`: Constante de temps de la bande intermédiaire (T).  Valeur typique = 0. Valeur par défaut : 0  - `ti6`: Constante de temps de la bande intermédiaire (T).  Valeur typique = 0. Valeur par défaut : 0  - `ti7`: Constante de temps de la bande intermédiaire (T).  Valeur typique = 0.2075. Valeur par défaut : 0  - `ti8`: Constante de temps de la bande intermédiaire (T).  Valeur typique = 0.2491. Valeur par défaut : 0  - `ti9`: Constante de temps de la bande intermédiaire (T).  Valeur typique = 0. Valeur par défaut : 0  - `tl1`: Constante de temps de la bande basse (T).  Valeur typique = 1,73. Valeur par défaut : 0  - `tl10`: Constante de temps de la bande basse (T).  Valeur typique = 0. Valeur par défaut : 0  - `tl11`: Constante de temps de la bande basse (T).  Valeur typique = 0. Valeur par défaut : 0  - `tl12`: Constante de temps de la bande basse (T).  Valeur typique = 0. Valeur par défaut : 0  - `tl2`: Constante de temps de la bande basse (T).  Valeur typique = 2.075. Valeur par défaut : 0  - `tl3`: Constante de temps de la bande basse (T).  Valeur typique = 0. Valeur par défaut : 0  - `tl4`: Constante de temps de la bande basse (T).  Valeur typique = 0. Valeur par défaut : 0  - `tl5`: Constante de temps de la bande basse (T).  Valeur typique = 0. Valeur par défaut : 0  - `tl6`: Constante de temps de la bande basse (T).  Valeur typique = 0. Valeur par défaut : 0  - `tl7`: Constante de temps de la bande basse (T).  Valeur typique = 2.075. Valeur par défaut : 0  - `tl8`: Constante de temps de la bande basse (T).  Valeur typique = 2.491. Valeur par défaut : 0  - `tl9`: Constante de temps de la bande basse (T).  Valeur typique = 0. Valeur par défaut : 0  - `type`: Type NGSI. Il doit être PssIEEE4B  - `vhmax`: Limite maximale de la sortie de la bande haute (V).  Valeur typique = 0.6. Valeur par défaut : 0.0  - `vhmin`: Limite minimale de la sortie de la bande haute (V).  Valeur typique = -0.6. Valeur par défaut : 0.0  - `vimax`: Limite maximale de la sortie de la bande intermédiaire (V).  Valeur typique = 0.6. Valeur par défaut : 0.0  - `vimin`: Limite minimale de la sortie de la bande intermédiaire (V).  Valeur typique = -0.6. Valeur par défaut : 0.0  - `vlmax`: Limite maximale de la sortie de la bande basse (V).  Valeur typique = 0.075. Valeur par défaut : 0.0  - `vlmin`: Limite minimale de la sortie de la bande basse (V).  Valeur typique = -0.075. Valeur par défaut : 0.0  - `vstmax`: Limite maximale de la sortie PSS (V).  Valeur typique = 0.15. Valeur par défaut : 0.0  - `vstmin`: Limite minimale de la sortie PSS (V).  Valeur typique = -0.15. Valeur par défaut : 0.0    
Propriétés requises  
Ce modèle de données est une conversion directe du modèle d'information commun (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un type incorrect. Si tel était le cas, veuillez soulever un problème ou envoyer un message à alberto.abella@fiware.org.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PssIEEE4B:    
  description: 'Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type PSS2B power system stabilizer model. The PSS4B model represents a structure based on multiple working frequency bands. Three separate bands, respectively dedicated to the low-, intermediate- and high-frequency modes of oscillations, are used in this delta-omega (speed input) PSS.  Reference: IEEE 4B 421.5-2005 Section 8.4.'    
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
    bwh1:    
      description: 'Notch filter 1 (high-frequency band): Three dB bandwidth (B). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    bwh2:    
      description: 'Notch filter 2 (high-frequency band): Three dB bandwidth (B). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    bwl1:    
      description: 'Notch filter 1 (low-frequency band): Three dB bandwidth (B). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    bwl2:    
      description: 'Notch filter 2 (low-frequency band): Three dB bandwidth (B). Default: 0.0'    
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
    id:    
      anyOf: &pssieee4b_-_properties_-_owner_-_items_-_anyof    
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
    kh:    
      description: 'High band gain (K).  Typical Value = 120. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kh1:    
      description: 'High band differential filter gain (K).  Typical Value = 66. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kh11:    
      description: 'High band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kh17:    
      description: 'High band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kh2:    
      description: 'High band differential filter gain (K).  Typical Value = 66. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ki:    
      description: 'Intermediate band gain (K).  Typical Value = 30. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ki1:    
      description: 'Intermediate band differential filter gain (K).  Typical Value = 66. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ki11:    
      description: 'Intermediate band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ki17:    
      description: 'Intermediate band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ki2:    
      description: 'Intermediate band differential filter gain (K).  Typical Value = 66. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kl:    
      description: 'Low band gain (K).  Typical Value = 7.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kl1:    
      description: 'Low band differential filter gain (K).  Typical Value = 66. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kl11:    
      description: 'Low band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kl17:    
      description: 'Low band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    kl2:    
      description: 'Low band differential filter gain (K).  Typical Value = 66. Default: 0.0'    
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
    omeganh1:    
      description: 'Notch filter 1 (high-frequency band): filter frequency (omega). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    omeganh2:    
      description: 'Notch filter 2 (high-frequency band): filter frequency (omega). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    omeganl1:    
      description: 'Notch filter 1 (low-frequency band): filter frequency (omega). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    omeganl2:    
      description: 'Notch filter 2 (low-frequency band): filter frequency (omega). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *pssieee4b_-_properties_-_owner_-_items_-_anyof    
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
    th1:    
      description: 'High band time constant (T).  Typical Value = 0.01513. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    th10:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    th11:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    th12:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    th2:    
      description: 'High band time constant (T).  Typical Value = 0.01816. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    th3:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    th4:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    th5:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    th6:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    th7:    
      description: 'High band time constant (T).  Typical Value = 0.01816. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    th8:    
      description: 'High band time constant (T).  Typical Value = 0.02179. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    th9:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ti1:    
      description: 'Intermediate band time constant (T).  Typical Value = 0.173. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ti10:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ti11:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ti12:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ti2:    
      description: 'Intermediate band time constant (T).  Typical Value = 0.2075. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ti3:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ti4:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ti5:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ti6:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ti7:    
      description: 'Intermediate band time constant (T).  Typical Value = 0.2075. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ti8:    
      description: 'Intermediate band time constant (T).  Typical Value = 0.2491. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ti9:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tl1:    
      description: 'Low band time constant (T).  Typical Value = 1.73. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tl10:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tl11:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tl12:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tl2:    
      description: 'Low band time constant (T).  Typical Value = 2.075. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tl3:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tl4:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tl5:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tl6:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tl7:    
      description: 'Low band time constant (T).  Typical Value = 2.075. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tl8:    
      description: 'Low band time constant (T).  Typical Value = 2.491. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tl9:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be PssIEEE4B'    
      enum:    
        - PssIEEE4B    
      type: Property    
    vhmax:    
      description: 'High band output maximum limit (V).  Typical Value = 0.6. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vhmin:    
      description: 'High band output minimum limit (V).  Typical Value = -0.6. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vimax:    
      description: 'Intermediate band output maximum limit (V).  Typical Value = 0.6. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vimin:    
      description: 'Intermediate band output minimum limit (V).  Typical Value = -0.6. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vlmax:    
      description: 'Low band output maximum limit (V).  Typical Value = 0.075. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vlmin:    
      description: 'Low band output minimum limit (V).  Typical Value = -0.075. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vstmax:    
      description: 'PSS output maximum limit (V).  Typical Value = 0.15. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vstmin:    
      description: 'PSS output minimum limit (V).  Typical Value = -0.15. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un PssIEEE4B au format JSON comme valeurs-clés. Ceci est compatible avec NGSI V2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un PssIEEE4B au format JSON tel que normalisé. Ceci est compatible avec la NGSI V2 lorsqu'elle n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un PssIEEE4B au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-LD quand on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un PssIEEE4B au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
