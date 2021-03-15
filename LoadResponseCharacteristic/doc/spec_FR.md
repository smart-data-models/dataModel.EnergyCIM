Entité : LoadResponseCharacteristic  
===================================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/LoadResponseCharacteristic/LICENSE.md)  
Description globale : **Adapté des modèles de données CIM. Modélise la réponse caractéristique de la demande de la charge en raison des changements des conditions du système telles que la tension et la fréquence. Ceci n'est pas lié à la réponse à la demande.  Si LoadResponseCharacteristic.exponentModel est True, les exposants de tension sont spécifiés et utilisés pour calculer :  Composante de puissance active = Pnominal * (Voltage/cim:BaseVoltage.nominalVoltage) ** cim:LoadResponseCharacteristic.pVoltageExponent Composante de puissance réactive = Qnominal * (Voltage/cim:BaseVoltage.nominalVoltage)** cim:LoadResponseCharacteristic.qVoltageExponent Où * signifie 'multiplier' et ** signifie 'élevé à la puissance de'.**  

## Liste des propriétés  

- `EnergyConsumer`: L'ensemble des charges qui ont les caractéristiques de la réponse. Valeur par défaut : 'list'.  - `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `exponentModel`: Indique que le modèle de dépendance exponentielle de la tension doit être utilisé.   S'il est faux, le modèle de coefficient doit être utilisé. Le modèle exponentiel de dépendance à la tension est constitué des attributs suivants : pVoltageExponent - qVoltageExponent. Le modèle de coefficient se compose des attributs suivants : pConstantImpedance - pConstantCourant - pConstantPuissance - qConstantImpedance - qConstantCourant - qConstantPuissance. La somme de pConstantImpedance, pConstantCurrent et pConstantPower est égale à 1. La somme de qConstantImpedance, qConstantCurrent et qConstantPower doit être égale à 1. Valeur par défaut : False  - `id`: Identifiant unique de l'entité  - `location`:   - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `pConstantCurrent`: Portion de la charge de puissance active modélisée comme courant constant. Valeur par défaut : 0.0  - `pConstantImpedance`: Portion de la charge de puissance active modélisée comme une impédance constante. Valeur par défaut : 0.0  - `pConstantPower`: Portion de la charge de puissance active modélisée comme puissance constante. Valeur par défaut : 0.0  - `pFrequencyExponent`: Exposant de la fréquence unitaire affectant la puissance active. Valeur par défaut : 0,0  - `pVoltageExponent`: Exposant de la tension unitaire affectant la puissance réelle. Valeur par défaut : 0.0  - `qConstantCurrent`: Portion de la charge de puissance réactive modélisée comme courant constant. Valeur par défaut : 0.0  - `qConstantImpedance`: Portion de la charge de puissance réactive modélisée comme une impédance constante. Valeur par défaut : 0.0  - `qConstantPower`: Portion de la charge de puissance réactive modélisée comme une puissance constante. Valeur par défaut : 0.0  - `qFrequencyExponent`: Exposant de la puissance réactive affectant la fréquence par unité. Valeur par défaut : 0.0  - `qVoltageExponent`: Exposant de la puissance réactive affectant la tension par unité. Valeur par défaut : 0.0  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type`: Type NGSI. Il doit être LoadResponseCharacteristic.    
Propriétés requises  
Ce modèle de données est une conversion directe du modèle d'information commun (CIM) spécifié par la norme IEC61970 en modèles de données intelligents. Les classes python sur lesquelles ce modèle est basé ont été développées par ces entités : Institute for Automation of Complex Power Systems (ACS), EON Energy Research Center (EONERC) et RWTH University Aachen, Allemagne. Certaines propriétés peuvent avoir un type incorrect. Si tel était le cas, veuillez soulever un problème ou envoyer un message à alberto.abella@fiware.org.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
LoadResponseCharacteristic:    
  description: 'Adapted from CIM data models. Models the characteristic response of the load demand due to changes in system conditions such as voltage and frequency. This is not related to demand response.  If LoadResponseCharacteristic.exponentModel is True, the voltage exponents are specified and used as to calculate:  Active power component = Pnominal * (Voltage/cim:BaseVoltage.nominalVoltage) ** cim:LoadResponseCharacteristic.pVoltageExponent  Reactive power component = Qnominal * (Voltage/cim:BaseVoltage.nominalVoltage)** cim:LoadResponseCharacteristic.qVoltageExponent  Where  * means ''multiply'' and ** is ''raised to power of''.'    
  properties:    
    EnergyConsumer:    
      description: 'The set of loads that have the response characteristics. Default: ''list'''    
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
    exponentModel:    
      description: 'Indicates the exponential voltage dependency model is to be used.   If false, the coefficient model is to be used. The exponential voltage dependency model consist of the attributes - pVoltageExponent - qVoltageExponent. The coefficient model consist of the attributes - pConstantImpedance - pConstantCurrent - pConstantPower - qConstantImpedance - qConstantCurrent - qConstantPower. The sum of pConstantImpedance, pConstantCurrent and pConstantPower shall equal 1. The sum of qConstantImpedance, qConstantCurrent and qConstantPower shall equal 1. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &loadresponsecharacteristic_-_properties_-_owner_-_items_-_anyof    
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
        anyOf: *loadresponsecharacteristic_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    pConstantCurrent:    
      description: 'Portion of active power load modeled as constant current. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pConstantImpedance:    
      description: 'Portion of active power load modeled as constant impedance. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pConstantPower:    
      description: 'Portion of active power load modeled as constant power. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pFrequencyExponent:    
      description: 'Exponent of per unit frequency effecting active power. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    pVoltageExponent:    
      description: 'Exponent of per unit voltage effecting real power. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    qConstantCurrent:    
      description: 'Portion of reactive power load modeled as constant current. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    qConstantImpedance:    
      description: 'Portion of reactive power load modeled as constant impedance. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    qConstantPower:    
      description: 'Portion of reactive power load modeled as constant power. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    qFrequencyExponent:    
      description: 'Exponent of per unit frequency effecting reactive power. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
    qVoltageExponent:    
      description: 'Exponent of per unit voltage effecting reactive power. Default: 0.0'    
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
      description: 'NGSI type. It has to be LoadResponseCharacteristic'    
      enum:    
        - LoadResponseCharacteristic    
      type: Property    
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
Non disponible l'exemple d'un LoadResponseCharacteristic au format JSON en tant que key-values. Ceci est compatible avec la NGSI V2 lorsqu'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un LoadResponseCharacteristic au format JSON tel que normalisé. Ceci est compatible avec la NGSI V2 lorsqu'elle n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un LoadResponseCharacteristic au format JSON-LD en tant que key-values. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'un LoadResponseCharacteristic au format JSON-LD tel que normalisé. Ceci est compatible avec NGSI-LD lorsqu'on n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
