<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : PssIEEE4B  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/PssIEEE4B/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Adapté des modèles de données CIM. La classe représente le modèle de stabilisateur de réseau électrique PSS2B de type IEEE Std 421.5-2005. Le modèle PSS4B représente une structure basée sur plusieurs bandes de fréquences de travail. Trois bandes distinctes, respectivement dédiées aux modes d'oscillations à basse, moyenne et haute fréquence, sont utilisées dans ce PSS delta-oméga (entrée vitesse).  Référence : IEEE 4B 421.5-2005, section 8.4.**.  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour cet élément  - `areaServed[string]`: La zone géographique où un service ou un article offert est fourni  . Model: [https://schema.org/Text](https://schema.org/Text)- `bwh1[number]`: Filtre coupe-bande 1 (bande haute fréquence) : Largeur de bande de trois dB (B). Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bwh2[number]`: Filtre coupe-bande 2 (bande haute fréquence) : Largeur de bande de trois dB (B). Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bwl1[number]`: Filtre coupe-bande 1 (bande basse fréquence) : Largeur de bande de trois dB (B). Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bwl2[number]`: Filtre coupe-bande 2 (bande basse fréquence) : Largeur de bande de trois dB (B). Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified[string]`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description[string]`: Une description de cet article  - `id[*]`: Identifiant unique de l'entité  - `kh[number]`: Gain en bande haute (K).  Valeur typique = 120. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kh1[number]`: Gain du filtre différentiel à haute bande (K).  Valeur typique = 66. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kh11[number]`: Coefficient de blocage du premier lead-lag de la bande haute (K).  Valeur typique = 1. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kh17[number]`: Coefficient de blocage du premier lead-lag de la bande haute (K).  Valeur typique = 1. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kh2[number]`: Gain du filtre différentiel à haute bande (K).  Valeur typique = 66. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ki[number]`: Gain de la bande intermédiaire (K).  Valeur typique = 30. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ki1[number]`: Gain du filtre différentiel à bande intermédiaire (K).  Valeur typique = 66. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ki11[number]`: Coefficient de blocage du premier lead-lag de la bande intermédiaire (K).  Valeur typique = 1. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ki17[number]`: Coefficient de blocage du premier lead-lag de la bande intermédiaire (K).  Valeur typique = 1. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ki2[number]`: Gain du filtre différentiel à bande intermédiaire (K).  Valeur typique = 66. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kl[number]`: Gain en bande basse (K).  Valeur typique = 7.5. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kl1[number]`: Gain du filtre différentiel à basse bande (K).  Valeur typique = 66. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kl11[number]`: Coefficient de blocage du premier lead-lag de la bande basse (K).  Valeur typique = 1. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kl17[number]`: Coefficient de blocage du premier lead-lag de la bande basse (K).  Valeur typique = 1. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kl2[number]`: Gain du filtre différentiel à basse bande (K).  Valeur typique = 66. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément.  - `omeganh1[number]`: Filtre Notch 1 (bande haute fréquence) : fréquence du filtre (oméga). Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `omeganh2[number]`: Filtre Notch 2 (bande haute fréquence) : fréquence du filtre (oméga). Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `omeganl1[number]`: Filtre Notch 1 (bande basse fréquence) : fréquence du filtre (oméga). Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `omeganl2[number]`: Filtre Notch 2 (bande basse fréquence) : fréquence du filtre (oméga). Valeur par défaut : 0,0  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires sur l'article  - `source[string]`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `th1[number]`: Constante de temps de la bande haute (T).  Valeur typique = 0.01513. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th10[number]`: Constante de temps de la bande haute (T).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th11[number]`: Constante de temps de la bande haute (T).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th12[number]`: Constante de temps de la bande haute (T).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th2[number]`: Constante de temps de la bande haute (T).  Valeur typique = 0.01816. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th3[number]`: Constante de temps de la bande haute (T).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th4[number]`: Constante de temps de la bande haute (T).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th5[number]`: Constante de temps de la bande haute (T).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th6[number]`: Constante de temps de la bande haute (T).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th7[number]`: Constante de temps de la bande haute (T).  Valeur typique = 0.01816. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th8[number]`: Constante de temps de la bande haute (T).  Valeur typique = 0.02179. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `th9[number]`: Constante de temps de la bande haute (T).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti1[number]`: Constante de temps de la bande intermédiaire (T).  Valeur typique = 0.173. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti10[number]`: Constante de temps de la bande intermédiaire (T).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti11[number]`: Constante de temps de la bande intermédiaire (T).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti12[number]`: Constante de temps de la bande intermédiaire (T).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti2[number]`: Constante de temps de la bande intermédiaire (T).  Valeur typique = 0.2075. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti3[number]`: Constante de temps de la bande intermédiaire (T).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti4[number]`: Constante de temps de la bande intermédiaire (T).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti5[number]`: Constante de temps de la bande intermédiaire (T).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti6[number]`: Constante de temps de la bande intermédiaire (T).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti7[number]`: Constante de temps de la bande intermédiaire (T).  Valeur typique = 0.2075. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti8[number]`: Constante de temps de la bande intermédiaire (T).  Valeur typique = 0.2491. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ti9[number]`: Constante de temps de la bande intermédiaire (T).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl1[number]`: Constante de temps de la bande basse (T).  Valeur typique = 1,73. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl10[number]`: Constante de temps de la bande basse (T).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl11[number]`: Constante de temps de la bande basse (T).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl12[number]`: Constante de temps de la bande basse (T).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl2[number]`: Constante de temps de la bande basse (T).  Valeur typique = 2.075. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl3[number]`: Constante de temps de la bande basse (T).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl4[number]`: Constante de temps de la bande basse (T).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl5[number]`: Constante de temps de la bande basse (T).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl6[number]`: Constante de temps de la bande basse (T).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl7[number]`: Constante de temps de la bande basse (T).  Valeur typique = 2.075. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl8[number]`: Constante de temps de la bande basse (T).  Valeur typique = 2.491. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tl9[number]`: Constante de temps de la bande basse (T).  Valeur typique = 0. Valeur par défaut : 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Type NGSI. Il doit être PssIEEE4B.  - `vhmax[number]`: Limite maximale de la sortie de la bande haute (V).  Valeur typique = 0.6. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vhmin[number]`: Limite minimale de la sortie de la bande haute (V).  Valeur typique = -0.6. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vimax[number]`: Limite maximale de la sortie de la bande intermédiaire (V).  Valeur typique = 0.6. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vimin[number]`: Limite minimale de la sortie de la bande intermédiaire (V).  Valeur typique = -0.6. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vlmax[number]`: Limite maximale de la sortie de la bande basse (V).  Valeur typique = 0.075. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vlmin[number]`: Limite minimale de la sortie de la bande basse (V).  Valeur typique = -0.075. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vstmax[number]`: Limite maximale de la sortie PSS (V).  Valeur typique = 0.15. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vstmin[number]`: Limite minimale de la sortie PSS (V).  Valeur typique = -0.15. Valeur par défaut : 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
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
    bwh1:    
      description: 'Notch filter 1 (high-frequency band): Three dB bandwidth (B). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bwh2:    
      description: 'Notch filter 2 (high-frequency band): Three dB bandwidth (B). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bwl1:    
      description: 'Notch filter 1 (low-frequency band): Three dB bandwidth (B). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bwl2:    
      description: 'Notch filter 2 (low-frequency band): Three dB bandwidth (B). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
      x-ngsi:    
        type: Property    
    kh:    
      description: 'High band gain (K).  Typical Value = 120. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kh1:    
      description: 'High band differential filter gain (K).  Typical Value = 66. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kh11:    
      description: 'High band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kh17:    
      description: 'High band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kh2:    
      description: 'High band differential filter gain (K).  Typical Value = 66. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ki:    
      description: 'Intermediate band gain (K).  Typical Value = 30. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ki1:    
      description: 'Intermediate band differential filter gain (K).  Typical Value = 66. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ki11:    
      description: 'Intermediate band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ki17:    
      description: 'Intermediate band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ki2:    
      description: 'Intermediate band differential filter gain (K).  Typical Value = 66. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kl:    
      description: 'Low band gain (K).  Typical Value = 7.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kl1:    
      description: 'Low band differential filter gain (K).  Typical Value = 66. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kl11:    
      description: 'Low band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kl17:    
      description: 'Low band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kl2:    
      description: 'Low band differential filter gain (K).  Typical Value = 66. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        type: GeoProperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    omeganh1:    
      description: 'Notch filter 1 (high-frequency band): filter frequency (omega). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    omeganh2:    
      description: 'Notch filter 2 (high-frequency band): filter frequency (omega). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    omeganl1:    
      description: 'Notch filter 1 (low-frequency band): filter frequency (omega). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    omeganl2:    
      description: 'Notch filter 2 (low-frequency band): filter frequency (omega). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *pssieee4b_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
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
    th1:    
      description: 'High band time constant (T).  Typical Value = 0.01513. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th10:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th11:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th12:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th2:    
      description: 'High band time constant (T).  Typical Value = 0.01816. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th3:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th4:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th5:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th6:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th7:    
      description: 'High band time constant (T).  Typical Value = 0.01816. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th8:    
      description: 'High band time constant (T).  Typical Value = 0.02179. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    th9:    
      description: 'High band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti1:    
      description: 'Intermediate band time constant (T).  Typical Value = 0.173. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti10:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti11:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti12:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti2:    
      description: 'Intermediate band time constant (T).  Typical Value = 0.2075. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti3:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti4:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti5:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti6:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti7:    
      description: 'Intermediate band time constant (T).  Typical Value = 0.2075. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti8:    
      description: 'Intermediate band time constant (T).  Typical Value = 0.2491. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ti9:    
      description: 'Intermediate band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl1:    
      description: 'Low band time constant (T).  Typical Value = 1.73. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl10:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl11:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl12:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl2:    
      description: 'Low band time constant (T).  Typical Value = 2.075. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl3:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl4:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl5:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl6:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl7:    
      description: 'Low band time constant (T).  Typical Value = 2.075. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl8:    
      description: 'Low band time constant (T).  Typical Value = 2.491. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tl9:    
      description: 'Low band time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI type. It has to be PssIEEE4B'    
      enum:    
        - PssIEEE4B    
      type: string    
      x-ngsi:    
        type: Property    
    vhmax:    
      description: 'High band output maximum limit (V).  Typical Value = 0.6. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vhmin:    
      description: 'High band output minimum limit (V).  Typical Value = -0.6. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vimax:    
      description: 'Intermediate band output maximum limit (V).  Typical Value = 0.6. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vimin:    
      description: 'Intermediate band output minimum limit (V).  Typical Value = -0.6. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vlmax:    
      description: 'Low band output maximum limit (V).  Typical Value = 0.075. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vlmin:    
      description: 'Low band output minimum limit (V).  Typical Value = -0.075. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vstmax:    
      description: 'PSS output maximum limit (V).  Typical Value = 0.15. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vstmin:    
      description: 'PSS output minimum limit (V).  Typical Value = -0.15. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PssIEEE4B/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/PssIEEE4B/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
Non disponible l'exemple d'un PssIEEE4B au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un PssIEEE4B au format JSON-LD tel que normalisé. Ceci est compatible avec la NGSI-v2 lorsqu'elle n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un PssIEEE4B au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-LD quand on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un PssIEEE4B au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
