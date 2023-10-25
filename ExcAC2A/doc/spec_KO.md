<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: ExcAC2A  
============<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExcAC2A/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **CIM 데이터 모델에서 수정됨. 필드 전류 제한이 다른 수정된 IEEE AC2A 교류 발전기 공급 정류기 여기 시스템**.  
버전: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `hvgate[number]`: HV 게이트가 활성화되어 있는지(HVgate) 나타냅니다. 참 = 게이트 사용됨 거짓 = 게이트 미사용됨. 일반 값 = true. 기본값입니다: False  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: 엔티티의 고유 식별자  - `ka[number]`: 전압 레귤레이터 이득(Ka).  일반 값 = 400. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kb[number]`: 2단 레귤레이터 게인(Kb)(>0).  여자기 필드 전류 컨트롤러 게인.  일반 값 = 25. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kb1[number]`: 2단 레귤레이터 게인(Kb1). ExcAC2A 모델의 변형을 나타내기 위해 Kb 대신 사용되는 여자기 필드 전류 컨트롤러 게인입니다.  일반 값 = 25. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kc[number]`: 정류 리액턴스(Kc)에 비례하는 정류기 부하 계수입니다.  일반 값 = 0.28. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kd[number]`: 여자 발전기 리액턴스(Kd)의 함수인 자화 계수입니다.  일반 값 = 0.35. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ke[number]`: 여기자 상수 - 자기 여기 필드(Ke)와 관련된 여기자 상수입니다.  일반 값 = 1. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kf[number]`: 여기 제어 시스템 안정기 이득(Kf).  일반 값 = 0.03. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kh[number]`: 여자기 필드 전류 피드백 이득(Kh).  일반 값 = 1. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kl[number]`: 여자기 필드 전류 제한기 이득(Kl).  일반 값 = 10. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kl1[number]`: 모델의 다른 사용을 허용하는 계수(Kl1).  일반 값 = 1. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ks[number]`: 모델 속도 계수(Ks)의 다른 사용을 허용하는 계수입니다.  일반 값 = 0. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `lvgate[number]`: LV 게이트가 활성화되어 있는지(LVgate) 나타냅니다. 참 = 게이트 사용됨 거짓 = 게이트 미사용됨. 일반값 = true. 기본값입니다: False  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `seve1[number]`: 정류 리액턴스(Se[Ve]) 뒤쪽의 해당 여자기 전압, Ve에서의 여자기 포화 함수 값입니다.  일반 값 = 0.037. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seve2[number]`: 정류 리액턴스(Se[Ve]) 뒤쪽의 해당 여자기 전압, Ve에서 여자기 포화 함수 값입니다.  일반 값 = 0.012. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `ta[number]`: 전압 레귤레이터 시간 상수(Ta).  일반 값 = 0.02. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tb[number]`: 전압 조정기 시간 상수(Tb).  일반 값 = 0. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tc[number]`: 전압 조정기 시간 상수(T).  일반 값 = 0. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `te[number]`: 여기자 시간 상수, 여기자 제어와 관련된 적분율(Te)입니다.  일반 값 = 0.6. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tf[number]`: 여기 제어 시스템 안정기 시간 상수(Tf).  일반 값 = 1. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI 유형. ExcAC2A여야 합니다.  - `vamax[number]`: 최대 전압 레귤레이터 출력(V).  일반 값 = 8. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vamin[number]`: 최소 전압 레귤레이터 출력(V).  일반 값 = -8. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ve1[number]`: 포화가 정의된 정류 리액턴스(Ve)의 여자 발전기 출력 전압 백입니다.  일반 값 = 4.4. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ve2[number]`: 포화가 정의된 정류 리액턴스(Ve)의 여자 발전기 출력 전압 백입니다.  일반 값 = 3.3. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vfemax[number]`: 여자기 필드 전류 제한 기준(Vfemax).  일반 값 = 4.4. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vlr[number]`: 최대 여자기 필드 전류(Vlr).  일반 값 = 4.4. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vrmax[number]`: 최대 전압 레귤레이터 출력(Vrmax).  일반 값 = 105. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vrmin[number]`: 최소 전압 레귤레이터 출력(Vrmin).  일반 값 = -95. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
<!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
CIM 데이터 모델 및 CIMpy에서 채택 - [https://github.com/sogno-platform/cimpy](https://github.com/sogno-platform/cimpy). 이 데이터 모델은 IEC61970 표준에 명시된 공통 정보 모델(CIM)을 스마트 데이터 모델로 직접 변환한 것입니다. 이 모델의 기반이 되는 파이썬 클래스는 복잡한 전력 시스템 자동화 연구소(ACS), EON 에너지 연구 센터(EONERC) 및 독일 아헨 RWTH 대학에서 개발했습니다. 일부 속성에는 잘못된 유형이 있을 수 있습니다. 이 경우 문제를 제기하거나 info@smartdatamodels.org 으로 메일을 보내 주시기 바랍니다.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ExcAC2A:    
  description: Adapted from CIM data models. Modified IEEE AC2A alternator-supplied rectifier excitation system with different field current limit.    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    hvgate:    
      description: 'Indicates if HV gate is active (HVgate). true = gate is used false = gate is not used. Typical Value = true. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    ka:    
      description: 'Voltage regulator gain (Ka).  Typical Value = 400. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kb:    
      description: 'Second stage regulator gain (Kb) (>0).  Exciter field current controller gain.  Typical Value = 25. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kb1:    
      description: 'Second stage regulator gain (Kb1). It is exciter field current controller gain used as alternative to Kb to represent a variant of the ExcAC2A model.  Typical Value = 25. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kc:    
      description: 'Rectifier loading factor proportional to commutating reactance (Kc).  Typical Value = 0.28. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kd:    
      description: 'Demagnetizing factor, a function of exciter alternator reactances (Kd).  Typical Value = 0.35. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ke:    
      description: 'Exciter constant related to self-excited field (Ke).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kf:    
      description: 'Excitation control system stabilizer gains (Kf).  Typical Value = 0.03. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kh:    
      description: 'Exciter field current feedback gain (Kh).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kl:    
      description: 'Exciter field current limiter gain (Kl).  Typical Value = 10. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kl1:    
      description: 'Coefficient to allow different usage of the model (Kl1).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ks:    
      description: 'Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
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
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
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
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
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
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
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
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    lvgate:    
      description: 'Indicates if LV gate is active (LVgate). true = gate is used false = gate is not used. Typical Value = true. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
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
    seve1:    
      description: 'Exciter saturation function value at the corresponding exciter voltage, Ve, back of commutating reactance (Se[Ve]).  Typical Value = 0.037. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    seve2:    
      description: 'Exciter saturation function value at the corresponding exciter voltage, Ve, back of commutating reactance (Se[Ve]).  Typical Value = 0.012. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    ta:    
      description: 'Voltage regulator time constant (Ta).  Typical Value = 0.02. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tb:    
      description: 'Voltage regulator time constant (Tb).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tc:    
      description: 'Voltage regulator time constant (T).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    te:    
      description: 'Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 0.6. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tf:    
      description: 'Excitation control system stabilizer time constant (Tf).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: NGSI type. It has to be ExcAC2A    
      enum:    
        - ExcAC2A    
      type: string    
      x-ngsi:    
        type: Property    
    vamax:    
      description: 'Maximum voltage regulator output (V).  Typical Value = 8. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vamin:    
      description: 'Minimum voltage regulator output (V).  Typical Value = -8. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ve1:    
      description: 'Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve).  Typical Value = 4.4. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ve2:    
      description: 'Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve).  Typical Value = 3.3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vfemax:    
      description: 'Exciter field current limit reference (Vfemax).  Typical Value = 4.4. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vlr:    
      description: 'Maximum exciter field current (Vlr).  Typical Value = 4.4. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vrmax:    
      description: 'Maximum voltage regulator outputs (Vrmax).  Typical Value = 105. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vrmin:    
      description: 'Minimum voltage regulator outputs (Vrmin).  Typical Value = -95. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcAC2A/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/ExcAC2A/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
키-값으로 JSON-LD 형식의 ExcAC2A 예제를 사용할 수 없습니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
정규화된 JSON-LD 형식의 ExcAC2A 예제는 사용할 수 없습니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
키 값으로 JSON-LD 형식의 ExcAC2A 예제를 사용할 수 없습니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
정규화된 JSON-LD 형식의 ExcAC2A 예제는 사용할 수 없습니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
