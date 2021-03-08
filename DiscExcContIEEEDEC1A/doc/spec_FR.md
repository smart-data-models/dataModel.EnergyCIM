Entité : DiscExcContIEEEDEC1A  
=============================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/DiscExcContIEEEDEC1A/LICENSE.md)  
Description globale : **Adapté des modèles de données CIM. La classe représente le modèle de contrôle d'excitation discontinue IEEE de type DEC1A qui augmente l'excitation du générateur à un niveau supérieur à celui exigé par le régulateur et le stabilisateur de tension immédiatement après un défaut du système.  Référence : Norme IEEE 421.5-2005, section 12.2.**  

## Liste des biens  

- `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `esc`: Référence de changement de vitesse ().  Valeur typique = 0,0015. Valeur par défaut : 0.0  - `id`: Identifiant unique de l'entité  - `kan`: Gain discontinu du contrôleur ().  Valeur typique = 400. Valeur par défaut : 0,0  - `ketl`: Gain du limiteur de tension aux bornes ().  Valeur typique = 47. Valeur par défaut : 0,0  - `location`:   - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `tan`: Constante de temps du contrôleur discontinu ().  Valeur typique = 0,08. Valeur par défaut : 0  - `td`: Constante de temps ().  Valeur typique = 0,03. Valeur par défaut : 0  - `tl1`: Constante de temps ().  Valeur typique = 0,025. Valeur par défaut : 0  - `tl2`: Constante de temps ().  Valeur typique = 1,25. Valeur par défaut : 0  - `tw5`: Constante de temps de lavage du DEC ().  Valeur typique = 5. Valeur par défaut : 0  - `type`: Type NGSI. Il doit être de type DiscExcContIEEEDEC1A  - `val`: Référence de la tension du régulateur ().  Valeur typique = 5,5. Valeur par défaut : 0,0  - `vanmax`: Limiteur pour Van (). Valeur par défaut : 0.0  - `vomax`: Limiteur ().  Valeur typique = 0,3. Valeur par défaut : 0.0  - `vomin`: Limiteur ().  Valeur typique = 0,1. Valeur par défaut : 0.0  - `vsmax`: Limiteur ().  Valeur typique = 0,2. Valeur par défaut : 0.0  - `vsmin`: Limiteur ().  Valeur typique = -0,066. Valeur par défaut : 0,0  - `vtc`: Référence du niveau de tension aux bornes ().  Valeur typique = 0,95. Valeur par défaut : 0,0  - `vtlmt`: Référence de tension ().  Valeur typique = 1,1. Valeur par défaut : 0,0  - `vtm`: Limites de tension ().  Valeur typique = 1,13. Valeur par défaut : 0,0  - `vtn`: Limites de tension ().  Valeur typique = 1,12. Valeur par défaut : 0,0    
Propriétés requises  
Ce modèle de données est une conversion directe du modèle commun d'information (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un mauvais type. C'est le cas, pelase soulever un problème ou envoyer un mail à alberto.abella@fiware.org  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
DiscExcContIEEEDEC1A:    
  description: 'Adapted from CIM data models. The class represents IEEE Type DEC1A discontinuous excitation control model that boosts generator excitation to a level higher than that demanded by the voltage regulator and stabilizer immediately following a system fault.  Reference: IEEE Standard 421.5-2005 Section 12.2.'    
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
    esc:    
      description: 'Speed change reference ().  Typical Value = 0.0015. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &discexccontieeedec1a_-_properties_-_owner_-_items_-_anyof    
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
    kan:    
      description: 'Discontinuous controller gain ().  Typical Value = 400. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    ketl:    
      description: 'Terminal voltage limiter gain ().  Typical Value = 47. Default: 0.0'    
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
        anyOf: *discexccontieeedec1a_-_properties_-_owner_-_items_-_anyof    
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
    tan:    
      description: 'Discontinuous controller time constant ().  Typical Value = 0.08. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    td:    
      description: 'Time constant ().  Typical Value = 0.03. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tl1:    
      description: 'Time constant ().  Typical Value = 0.025. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tl2:    
      description: 'Time constant ().  Typical Value = 1.25. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    tw5:    
      description: 'DEC washout time constant ().  Typical Value = 5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI type. It has to be DiscExcContIEEEDEC1A'    
      enum:    
        - DiscExcContIEEEDEC1A    
      type: Property    
    val:    
      description: 'Regulator voltage reference ().  Typical Value = 5.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vanmax:    
      description: 'Limiter for Van (). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vomax:    
      description: 'Limiter ().  Typical Value = 0.3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vomin:    
      description: 'Limiter ().  Typical Value = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vsmax:    
      description: 'Limiter ().  Typical Value = 0.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vsmin:    
      description: 'Limiter ().  Typical Value = -0.066. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vtc:    
      description: 'Terminal voltage level reference ().  Typical Value = 0.95. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vtlmt:    
      description: 'Voltage reference ().  Typical Value = 1.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vtm:    
      description: 'Voltage limits ().  Typical Value = 1.13. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    vtn:    
      description: 'Voltage limits ().  Typical Value = 1.12. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un DiscExcContIEEEDEC1A en format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un DiscExcContIEEEDEC1A en format JSON comme normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un DiscExcContIEEEDEC1A en format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un DiscExcContIEEEDEC1A en format JSON-LD comme normalisé. Il est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
