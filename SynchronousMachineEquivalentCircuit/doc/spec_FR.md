Entité : SynchronousMachineEquivalentCircuit  
============================================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/SynchronousMachineEquivalentCircuit/LICENSE.md)  
Description globale : **Adapté des modèles de données CIM. Les équations électriques de toutes les variations des modèles synchrones sont basées sur le diagramme SynchronousEquivalentCircuit pour les axes direct et en quadrature.    = + = + * / ( + ) = + * * / ( * + * + * ) = + = + * / (+ ) = + ** / ( * + * + * ) = ( + ) / ( * ) = ( * + * + * ) / ( * * ( + ) = ( + ) / ( * ) = ( * + * +  * )/ ( * * ( + ) Mêmes équations utilisant les attributs CIM de la classe SynchronousMachineTimeConstantReactance à gauche du signe = et de la classe SynchronousMachineEquivalentCircuit à droite (sauf indication contraire) : xDirectSync = xad + RotatingMachineDynamics.Réactivité de fuite du stator xDirectTrans = Dynamique de la machine tournante.statorLeakageReactance + xad * xfd / (xad + xfd) xDirectSubtrans = RotatingMachineDynamics.statorLeakageReactance + xad * xfd * x1d / (xad * xfd + xad * x1d + xfd * x1d) xQuadSync = xaq + RotatingMachineDynamics.statorLeakageReactance xQuadTrans = RotatingMachineDynamics.statorLeakageReactance + xaq * x1q / (xaq+ x1q) xQuadSubtrans = RotatingMachineDynamics.statorLeakageReactance + xaq * x1q* x2q / (xaq * x1q + xaq * x2q + x1q * x2q) tpdo = (xad + xfd) / (2*pi*fréquence nominale * rfd) tppdo = (xad * xfd + xad * x1d + xfd * x1d) / (2*pi*fréquence nominale * r1d * (xad + xfd) tpqo = (xaq + x1q) / (2*pi*fréquence nominale * r1q) tppqo = (xaq * x1q + xaq * x2q + x1q * x2q)/ (2*pi*fréquence nominale * r2q * (xaq + x1q).  Ne sont valables que pour un modèle simplifié où la réactance de Canay est nulle**.  

## Liste des biens  

- `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `location`:   - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `r1d`: Amortisseur de l'axe D 1 résistance d'enroulement. Valeur par défaut : 0,0  - `r1q`: Amortisseur d'axe Q 1 résistance d'enroulement. Valeur par défaut : 0,0  - `r2q`: Résistance d'enroulement de l'amortisseur d'axe Q 2. Valeur par défaut : 0,0  - `rfd`: Résistance de l'enroulement de champ. Valeur par défaut : 0,0  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `type`: Type NGSI. Il doit être de type SynchronousMachineEquivalentCircuit  - `x1d`: Amortisseur de l'axe D 1 : réactance de fuite de l'enroulement. Par défaut : 0,0  - `x1q`: Réaction de fuite du bobinage de l'amortisseur d'axe Q 1. Par défaut : 0,0  - `x2q`: Réactance de fuite de l'enroulement de l'amortisseur d'axe Q 2. Par défaut : 0,0  - `xad`: Réaction mutuelle sur l'axe D. Valeur par défaut : 0,0  - `xaq`: Réaction mutuelle sur l'axe Q. Valeur par défaut : 0,0  - `xf1d`: Réaction mutuelle différentielle (`Canay`). Valeur par défaut : 0.0  - `xfd`: Réactance de fuite de l'enroulement de champ. Valeur par défaut : 0,0    
Propriétés requises  
Ce modèle de données est une conversion directe du modèle commun d'information (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un mauvais type. C'est le cas, pelase soulever un problème ou envoyer un mail à alberto.abella@fiware.org  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
SynchronousMachineEquivalentCircuit:    
  description: 'Adapted from CIM data models. The electrical equations for all variations of the synchronous models are based on the SynchronousEquivalentCircuit diagram for the direct and quadrature axes.    =  +   =  +  *  / ( + )  =  +  * *  / ( *  +  *  +  * )  =  +   =  +  *  / (+ )  =  +  **  / ( *  +  *  +  * )  = ( + ) / ( * )  = ( *  +  *  +  * ) / ( *  * ( + )  = ( + ) / ( * )  = ( *  +  *  +  * )/ ( *  * ( + ) Same equations using CIM attributes from SynchronousMachineTimeConstantReactance class on left of = sign and SynchronousMachineEquivalentCircuit class on right (except as noted): xDirectSync = xad + RotatingMachineDynamics.statorLeakageReactance xDirectTrans = RotatingMachineDynamics.statorLeakageReactance + xad * xfd / (xad + xfd) xDirectSubtrans = RotatingMachineDynamics.statorLeakageReactance + xad * xfd * x1d / (xad * xfd + xad * x1d + xfd * x1d) xQuadSync = xaq + RotatingMachineDynamics.statorLeakageReactance xQuadTrans = RotatingMachineDynamics.statorLeakageReactance + xaq * x1q / (xaq+ x1q) xQuadSubtrans = RotatingMachineDynamics.statorLeakageReactance + xaq * x1q* x2q / (xaq * x1q + xaq * x2q + x1q * x2q)  tpdo = (xad + xfd) / (2*pi*nominal frequency * rfd) tppdo = (xad * xfd + xad * x1d + xfd * x1d) / (2*pi*nominal frequency * r1d * (xad + xfd) tpqo = (xaq + x1q) / (2*pi*nominal frequency * r1q) tppqo = (xaq * x1q + xaq * x2q + x1q * x2q)/ (2*pi*nominal frequency * r2q * (xaq + x1q).  Are only valid for a simplified model where ''Canay'' reactance is zero.'    
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
    id:    
      anyOf: &synchronousmachineequivalentcircuit_-_properties_-_owner_-_items_-_anyof    
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
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *synchronousmachineequivalentcircuit_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    r1d:    
      description: 'D-axis damper 1 winding resistance. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    r1q:    
      description: 'Q-axis damper 1 winding resistance. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    r2q:    
      description: 'Q-axis damper 2 winding resistance. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    rfd:    
      description: 'Field winding resistance. Default: 0.0'    
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
      description: 'NGSI type. It has to be SynchronousMachineEquivalentCircuit'    
      enum:    
        - SynchronousMachineEquivalentCircuit    
      type: Property    
    x1d:    
      description: 'D-axis damper 1 winding leakage reactance. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    x1q:    
      description: 'Q-axis damper 1 winding leakage reactance. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    x2q:    
      description: 'Q-axis damper 2 winding leakage reactance. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    xad:    
      description: 'D-axis mutual reactance. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    xaq:    
      description: 'Q-axis mutual reactance. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    xf1d:    
      description: 'Differential mutual (`Canay`) reactance. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    xfd:    
      description: 'Field winding leakage reactance. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un SynchronousMachineEquivalentCircuit au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un SynchronousMachineEquivalentCircuit en format JSON comme normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un SynchronousMachineEquivalentCircuit au format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un SynchronousMachineEquivalentCircuit en format JSON-LD comme normalisé. Il est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
