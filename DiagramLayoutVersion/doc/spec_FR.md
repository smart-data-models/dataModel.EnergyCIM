Entité : DiagramLayoutVersion  
=============================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/DiagramLayoutVersion/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Adapté des modèles de données CIM. Détails de la version.**  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `baseUML`: UML de base fourni par le gestionnaire de modèle CIM. Valeur par défaut : " ".  - `baseURI`: URI de profil utilisé dans l'en-tête d'échange de modèle et défini dans les normes CEI.  Il identifie de manière unique le profil et sa version. Il est donné à titre d'information uniquement et pour identifier le profil CEI le plus proche sur lequel ce profil CGMES est basé. Valeur par défaut : ''.  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `date`: Date de création du profil Le format est YYYY-MM-DD par exemple pour le 5 janvier 2009 c'est 2009-01-05. Valeur par défaut : ''.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `differenceModelURI`: URI du modèle de différence défini par la norme IEC 61970-552. Valeur par défaut : " ".  - `entsoeUML`: UML fourni par ENTSO-E. Valeur par défaut : " ".  - `entsoeURI`: URI du profil défini par ENTSO-E et utilisé dans l'en-tête d'échange de modèle.  Il identifie de manière unique le profil et sa version. Les deux derniers éléments de l'URI (http://entsoe.eu/CIM/DiagramLayout/yy/zzz) indiquent les versions majeures et mineures où :  - yy - indique une version majeure ; - zzz - indique une version mineure. Valeur par défaut : ''.  - `id`: Identifiant unique de l'entité  - `location`:   - `modelDescriptionURI`: URI de description du modèle défini par la norme IEC 61970-552. Valeur par défaut : " ".  - `name`: Le nom de cet élément.  - `namespaceRDF`: Espace de noms RDF. Valeur par défaut : '''  - `namespaceUML`: Espace de noms UML CIM. Valeur par défaut : '''  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `shortName`: Le nom court du profil utilisé dans la documentation du profil. Valeur par défaut : '''.  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type`: Type NGSI. Il doit être DiagramLayoutVersion.    
Propriétés requises  
Adapté de CIM data models and CIMpy - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). Ce modèle de données est une conversion directe du modèle d'information commun (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un mauvais type. Si tel était le cas, veuillez soulever un problème ou envoyer un courrier à info@smartdatamodels.org.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
DiagramLayoutVersion:    
  description: 'Adapted from CIM data models. Version details.'    
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
    baseUML:    
      description: 'Base UML provided by CIM model manager. Default: '''''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    baseURI:    
      description: 'Profile URI used in the Model Exchange header and defined in IEC standards.  It uniquely identifies the Profile and its version. It is given for information only and to identify the closest IEC profile to which this CGMES profile is based on. Default: '''''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    date:    
      description: 'Profile creation date Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05. Default: '''''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    differenceModelURI:    
      description: 'Difference model URI defined by IEC 61970-552. Default: '''''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    entsoeUML:    
      description: 'UML provided by ENTSO-E. Default: '''''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    entsoeURI:    
      description: 'Profile URI defined by ENTSO-E and used in the Model Exchange header.  It uniquely identifies the Profile and its version. The last two elements in the URI (http://entsoe.eu/CIM/DiagramLayout/yy/zzz) indicate major and minor versions where:  - yy - indicates a major version; - zzz - indicates a minor version. Default: '''''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &diagramlayoutversion_-_properties_-_owner_-_items_-_anyof    
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
    modelDescriptionURI:    
      description: 'Model Description URI defined by IEC 61970-552. Default: '''''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    name:    
      description: 'The name of this item.'    
      type: Property    
    namespaceRDF:    
      description: 'RDF namespace. Default: '''''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    namespaceUML:    
      description: 'CIM UML namespace. Default: '''''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *diagramlayoutversion_-_properties_-_owner_-_items_-_anyof    
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
    shortName:    
      description: 'The short name of the profile used in profile documentation. Default: '''''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI type. It has to be DiagramLayoutVersion'    
      enum:    
        - DiagramLayoutVersion    
      type: Property    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un DiagramLayoutVersion au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-v2 en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un DiagramLayoutVersion au format JSON-LD tel que normalisé. Ceci est compatible avec la NGSI-v2 lorsqu'elle n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un DiagramLayoutVersion au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un DiagramLayoutVersion au format JSON-LD tel que normalisé. Ceci est compatible avec NGSI-LD lorsqu'on n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
