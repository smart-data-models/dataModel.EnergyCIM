Entité : EquivalentInjection  
============================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/EquivalentInjection/LICENSE.md)  
Description globale : **Adapté des modèles de données CIM. Cette classe représente les injections équivalentes (génération ou charge).  La régulation de la tension n'est autorisée qu'au point de raccordement.**  

## Liste des biens  

- `ReactiveCapabilityCurve`: L'injection équivalente en utilisant cette courbe de capacité réactive. Par défaut : Aucun  - `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `location`:   - `maxP`: Puissance active maximale de l'injection. Valeur par défaut : 0,0  - `maxQ`: Utilisé pour la modélisation de l'alimentation pour l'échange de flux de charge. Non utilisé pour la modélisation des courts-circuits.  Si maxQ et minQ ne sont pas utilisés, ReactiveCapabilityCurve peut être utilisée. Valeur par défaut : 0.0  - `minP`: Puissance active minimale de l'injection. Valeur par défaut : 0,0  - `minQ`: Utilisé pour la modélisation de l'alimentation pour l'échange de flux de charge. Non utilisé pour la modélisation des courts-circuits.  Si maxQ et minQ ne sont pas utilisés, ReactiveCapabilityCurve peut être utilisée. Valeur par défaut : 0.0  - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `p`: Injection de puissance active équivalente. La convention du signe de charge est utilisée, c'est-à-dire que le signe positif signifie le flux sortant d'un nœud. Valeur de départ pour les solutions en régime permanent. Valeur par défaut : 0,0  - `q`: Injection de puissance réactive équivalente. La convention du signe de charge est utilisée, c'est-à-dire que le signe positif signifie le flux sortant d'un nœud. Valeur de départ pour les solutions en régime permanent. Valeur par défaut : 0,0  - `r`: Résistance à la séquence positive. Utilisée pour représenter la norme Extended-Ward (IEC 60909). Utilisation : Extended-Ward est le résultat de la réduction du réseau avant l'échange de données. Valeur par défaut : 0.0  - `r0`: Résistance à la séquence zéro. Utilisée pour représenter la norme Extended-Ward (IEC 60909). Utilisation : Extended-Ward est le résultat de la réduction du réseau avant l'échange de données. Valeur par défaut : 0.0  - `r2`: Résistance à la séquence négative. Utilisée pour représenter la norme Extended-Ward (IEC 60909). Utilisation : Extended-Ward est le résultat de la réduction du réseau avant l'échange de données. Valeur par défaut : 0.0  - `regulationCapability`: Spécifie si l'EquivalentInjection a ou non la capacité de réguler la tension locale. Par défaut : Faux :  - `regulationStatus`: Précise le statut de régulation par défaut de l'EquivalentInjection.  True est en train de réguler.  Faux n'est pas une réglementation. Par défaut : False  - `regulationTarget`: La tension cible pour la régulation de la tension. Valeur par défaut : 0,0  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `type`: Type NGSI. Il doit être de type EquivalentInjection  - `x`: Réaction positive de la séquence. Utilisée pour représenter la norme Extended-Ward (IEC 60909). Utilisation : Extended-Ward est le résultat de la réduction du réseau avant l'échange de données. Valeur par défaut : 0.0  - `x0`: Réactivité zéro. Utilisé pour représenter la norme Extended-Ward (IEC 60909). Utilisation : Extended-Ward est le résultat de la réduction du réseau avant l'échange de données. Valeur par défaut : 0.0  - `x2`: Réaction négative à la séquence. Utilisé pour représenter l'Extended-Ward (IEC 60909). Utilisation : Extended-Ward est le résultat de la réduction du réseau avant l'échange de données. Valeur par défaut : 0.0    
Propriétés requises  
Ce modèle de données est une conversion directe du modèle commun d'information (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un mauvais type. C'est le cas, pelase soulever un problème ou envoyer un mail à alberto.abella@fiware.org  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EquivalentInjection:    
  description: 'Adapted from CIM data models. This class represents equivalent injections (generation or load).  Voltage regulation is allowed only at the point of connection.'    
  properties:    
    ReactiveCapabilityCurve:    
      description: 'The equivalent injection using this reactive capability curve. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    id:    
      anyOf: &equivalentinjection_-_properties_-_owner_-_items_-_anyof    
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
    maxP:    
      description: 'Maximum active power of the injection. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    maxQ:    
      description: 'Used for modeling of infeed for load flow exchange. Not used for short circuit modeling.  If maxQ and minQ are not used ReactiveCapabilityCurve can be used. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    minP:    
      description: 'Minimum active power of the injection. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    minQ:    
      description: 'Used for modeling of infeed for load flow exchange. Not used for short circuit modeling.  If maxQ and minQ are not used ReactiveCapabilityCurve can be used. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *equivalentinjection_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    p:    
      description: 'Equivalent active power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for steady state solutions. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    q:    
      description: 'Equivalent reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for steady state solutions. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    r:    
      description: 'Positive sequence resistance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of network reduction prior to the data exchange. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    r0:    
      description: 'Zero sequence resistance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of network reduction prior to the data exchange. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    r2:    
      description: 'Negative sequence resistance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of network reduction prior to the data exchange. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    regulationCapability:    
      description: 'Specifies whether or not the EquivalentInjection has the capability to regulate the local voltage. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    regulationStatus:    
      description: 'Specifies the default regulation status of the EquivalentInjection.  True is regulating.  False is not regulating. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    regulationTarget:    
      description: 'The target voltage for voltage regulation. Default: 0.0'    
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
    type:    
      description: 'NGSI type. It has to be EquivalentInjection'    
      enum:    
        - EquivalentInjection    
      type: Property    
    x:    
      description: 'Positive sequence reactance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of network reduction prior to the data exchange. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    x0:    
      description: 'Zero sequence reactance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of network reduction prior to the data exchange. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    x2:    
      description: 'Negative sequence reactance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of network reduction prior to the data exchange. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'une EquivalentInjection au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsque l'on utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'une EquivalentInjection en format JSON comme normalisé. Il est compatible avec la version 2 du NGSI lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'une EquivalentInjection au format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'une EquivalentInjection en format JSON-LD comme normalisé. Ce format est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
