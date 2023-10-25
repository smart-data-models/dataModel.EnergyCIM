<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: ExcREXS  
============<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/ExcREXS/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **CIM 데이터 모델에서 수정되었습니다. 범용 회전 여기 시스템 모델.  이 모델은 DC 전원이 AC 또는 DC 발전기인 광범위한 여기 시스템을 표현하는 데 사용할 수 있습니다. 여기에는 IEEE 유형 AC1, AC2, DC1 및 DC2 여기 시스템 모델이 포함됩니다.**  
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
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `e1[number]`: 필드 전압 값 1(E1).  일반 값 = 3. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `e2[number]`: 필드 전압 값 2(E2).  일반 값 = 4. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fbf[number]`: 속도 피드백 신호 플래그(Fbf). 일반 값 = fieldCurrent. 기본값입니다: None  . Model: [https://schema.org/Number](https://schema.org/Number)- `flimf[number]`: 유형 제한 플래그(Flimf).  일반값 = 0. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: 엔티티의 고유 식별자  - `kc[number]`: 정류기 조절 계수(Kc).  일반 값 = 0.05. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kd[number]`: 여기자 조절 계수(Kd).  일반 값 = 2. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ke[number]`: 여기자 필드 비례 상수(Ke).  일반 값 = 1. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kefd[number]`: 필드 전압 피드백 이득(Kefd).  일반 값 = 0. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kf[number]`: 피드백 게인(Kf)을 평가합니다.  일반 값 = 0.05. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kh[number]`: 필드 전압 컨트롤러 피드백 게인(Kh).  일반 값 = 0. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kii[number]`: 필드 전류 레귤레이터 적분 이득(Kii).  일반 값 = 0. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kip[number]`: 필드 전류 레귤레이터 비례 게인(Kip).  일반 값 = 1. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ks[number]`: 모델 속도 계수(Ks)의 다른 사용을 허용하는 계수입니다.  일반 값 = 0. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kvi[number]`: 전압 레귤레이터 적분 이득(Kvi).  일반 값 = 0. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kvp[number]`: 전압 레귤레이터 비례 게인(Kvp).  일반 값 = 2800. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kvphz[number]`: V/Hz 리미터 게인(Kvphz).  일반 값 = 0. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `nvphz[number]`: V/Hz 리미터의 픽업 속도(Nvphz).  일반값 = 0. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `se1[number]`: E1(Se1)에서의 포화 계수입니다.  일반 값 = 0.0001. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `se2[number]`: E2(Se2)에서의 포화 계수입니다.  일반 값 = 0.001. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `ta[number]`: 전압 레귤레이터 시간 상수(Ta).  일반 값 = 0.01. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tb1[number]`: 지연 시간 상수(Tb1).  일반 값 = 0. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tb2[number]`: 지연 시간 상수(Tb2).  일반 값 = 0. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tc1[number]`: 리드 타임 상수(Tc1).  일반 값 = 0. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tc2[number]`: 리드 타임 상수(Tc2).  일반 값 = 0. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `te[number]`: 여기자 필드 시간 상수(Te).  일반 값 = 1.2. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tf[number]`: 속도 피드백 시간 상수(Tf).  일반 값 = 1. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tf1[number]`: 피드백 리드 타임 상수(Tf1).  일반 값 = 0. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tf2[number]`: 피드백 지연 시간 상수(Tf2).  일반 값 = 0. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tp[number]`: 필드 전류 브리지 시간 상수(Tp).  일반 값 = 0. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI 유형. ExcREX여야 합니다.  - `vcmax[number]`: 최대 컴파운딩 전압(Vcmax).  일반 값 = 0. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vfmax[number]`: 최대 여자기 전계 전류(Vfmax).  일반 값 = 47. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vfmin[number]`: 최소 여자기 필드 전류(Vfmin).  일반 값 = -20. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vimax[number]`: 전압 레귤레이터 입력 제한(Vimax).  일반 값 = 0.1. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vrmax[number]`: 최대 컨트롤러 출력(Vrmax).  일반 값 = 47. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `vrmin[number]`: 최소 컨트롤러 출력(Vrmin).  일반 값 = -20. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `xc[number]`: 여기자 컴파운딩 리액턴스(Xc).  일반 값 = 0. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
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
ExcREXS:    
  description: 'Adapted from CIM data models. General Purpose Rotating Excitation System Model.  This model can be used to represent a wide range of excitation systems whose DC power source is an AC or DC generator. It encompasses IEEE type AC1, AC2, DC1, and DC2 excitation system models.'    
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
    e1:    
      description: 'Field voltage value 1 (E1).  Typical Value = 3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    e2:    
      description: 'Field voltage value 2 (E2).  Typical Value = 4. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fbf:    
      description: 'Rate feedback signal flag (Fbf). Typical Value = fieldCurrent. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    flimf:    
      description: 'Limit type flag (Flimf).  Typical Value = 0. Default: 0.0'    
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
    kc:    
      description: 'Rectifier regulation factor (Kc).  Typical Value = 0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kd:    
      description: 'Exciter regulation factor (Kd).  Typical Value = 2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ke:    
      description: 'Exciter field proportional constant (Ke).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kefd:    
      description: 'Field voltage feedback gain (Kefd).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kf:    
      description: 'Rate feedback gain (Kf).  Typical Value = 0.05. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kh:    
      description: 'Field voltage controller feedback gain (Kh).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kii:    
      description: 'Field Current Regulator Integral Gain (Kii).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kip:    
      description: 'Field Current Regulator Proportional Gain (Kip).  Typical Value = 1. Default: 0.0'    
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
    kvi:    
      description: 'Voltage Regulator Integral Gain (Kvi).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kvp:    
      description: 'Voltage Regulator Proportional Gain (Kvp).  Typical Value = 2800. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kvphz:    
      description: 'V/Hz limiter gain (Kvphz).  Typical Value = 0. Default: 0.0'    
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
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    nvphz:    
      description: 'Pickup speed of V/Hz limiter (Nvphz).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    se1:    
      description: 'Saturation factor at E1 (Se1).  Typical Value = 0.0001. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    se2:    
      description: 'Saturation factor at E2 (Se2).  Typical Value = 0.001. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    ta:    
      description: 'Voltage Regulator time constant (Ta).  Typical Value = 0.01. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tb1:    
      description: 'Lag time constant (Tb1).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tb2:    
      description: 'Lag time constant (Tb2).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tc1:    
      description: 'Lead time constant (Tc1).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tc2:    
      description: 'Lead time constant (Tc2).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    te:    
      description: 'Exciter field time constant (Te).  Typical Value = 1.2. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tf:    
      description: 'Rate feedback time constant (Tf).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tf1:    
      description: 'Feedback lead time constant (Tf1).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tf2:    
      description: 'Feedback lag time constant (Tf2).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tp:    
      description: 'Field current Bridge time constant (Tp).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: NGSI type. It has to be ExcREXS    
      enum:    
        - ExcREXS    
      type: string    
      x-ngsi:    
        type: Property    
    vcmax:    
      description: 'Maximum compounding voltage (Vcmax).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vfmax:    
      description: 'Maximum Exciter Field Current (Vfmax).  Typical Value = 47. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vfmin:    
      description: 'Minimum Exciter Field Current (Vfmin).  Typical Value = -20. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vimax:    
      description: 'Voltage Regulator Input Limit (Vimax).  Typical Value = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vrmax:    
      description: 'Maximum controller output (Vrmax).  Typical Value = 47. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vrmin:    
      description: 'Minimum controller output (Vrmin).  Typical Value = -20. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    xc:    
      description: 'Exciter compounding reactance (Xc).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcREXS/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/ExcREXS/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
키-값으로 JSON-LD 형식의 ExcREX 예제를 사용할 수 없습니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
정규화된 JSON-LD 형식의 ExcREX 예제는 사용할 수 없습니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
키-값으로 JSON-LD 형식의 ExcREXS 예제를 사용할 수 없습니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
정규화된 JSON-LD 형식의 ExcREXS 예제는 사용할 수 없습니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
