<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: WindContPType3IEC  
======================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/WindContPType3IEC/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **CIM 데이터 모델에서 수정됨. P 제어 모델 유형 3.  참조: IEC 표준 61400-27-1 섹션 6.6.5.3.**  
버전: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `WindDynamicsLookupTable[number]`: 이 바람 역학 룩업 테이블이 연결된 P 제어 유형 3 모델입니다. 기본값: '목록'  . Model: [https://schema.org/Number](https://schema.org/Number)- `WindGenTurbineType3IEC[number]`: 이 풍력 터빈 유형 3 모델과 연결된 풍력 제어 P 유형 3 모델입니다. 기본값입니다: 없음  . Model: [https://schema.org/Number](https://schema.org/Number)- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `dpmax[number]`: 최대 풍력 터빈 전력 램프 속도 (). 프로젝트에 따라 달라지는 파라미터입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dtrisemaxlvrt[number]`: S(d)에 대한 LVRT 중 토크 상승률의 제한입니다. 프로젝트에 따라 달라지는 파라미터입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: 엔티티의 고유 식별자  - `kdtd[number]`: 액티브 드라이브 트레인 댐핑을 위한 게인(). 유형에 따라 달라지는 파라미터입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kip[number]`: PI 컨트롤러 통합 파라미터 (). 유형 종속 파라미터입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kpp[number]`: PI 컨트롤러 비례 게인 (). 유형에 따라 달라지는 파라미터입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `mplvrt[number]`: LVRT 전력 제어 모드 활성화(M true = 1: 전압 제어 거짓 = 0: 무효 전력 제어).  프로젝트에 따라 달라지는 파라미터입니다. 기본값입니다: False  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: 이 항목의 이름  - `omegaoffset[number]`: 로터 속도 변경 시 컨트롤러 동작을 제한하는 기준값(오메가)에 대한 오프셋입니다. 대소문자가 구분되는 파라미터입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `pdtdmax[number]`: 최대 액티브 드라이브 트레인 감쇠력 (). 유형에 따라 달라지는 파라미터입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rramp[number]`: 일부 그리드 코드()에서 필요한 토크의 램프 제한입니다. 프로젝트에 따라 달라지는 파라미터입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `tdvs[number]`: 전압 강하 후 시간 지연(T). 프로젝트에 따라 달라지는 파라미터입니다. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `temin[number]`: 최소 발전기 토크 (). 유형에 따라 달라지는 매개변수입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tomegafilt[number]`: 발전기 속도 측정을 위한 필터 시간 상수(). 유형에 따라 달라지는 매개변수입니다. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tpfilt[number]`: 전력 측정을 위한 필터 시간 상수(). 유형에 따라 달라지는 매개변수입니다. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tpord[number]`: 전력 순서 지연 ()의 시간 상수입니다. 유형에 따라 달라지는 매개변수입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tufilt[number]`: 전압 측정을 위한 필터 시간 상수(). 유형에 따라 달라지는 매개변수입니다. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tuscale[number]`: 리셋 토크(T)의 전압 스케일링 계수입니다. 프로젝트에 따라 달라지는 파라미터입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `twref[number]`: 속도 기준 필터의 시간 상수(). 유형에 따라 달라지는 매개변수입니다. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI 유형. WindContPType3IEC여야 합니다.  - `udvs[number]`: 전압 강하() 후 LVRT 상태 유지를 위한 전압 제한입니다. 프로젝트에 따라 달라지는 파라미터입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `updip[number]`: P-제어()에 대한 전압 강하 임계값.  터빈 제어의 일부로, 컨버터 임계값과 다른 경우가 많습니다(예: 0.8). 프로젝트에 따라 달라지는 파라미터입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `wdtd[number]`: 액티브 드라이브 트레인 감쇠 주파수(오메가). 두 개의 질량 모델 파라미터로 계산할 수 있습니다. 유형에 따라 달라지는 파라미터입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `zeta[number]`: 액티브 드라이브 트레인 댐핑 계수(제타)입니다. 유형에 따라 달라지는 파라미터입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
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
WindContPType3IEC:    
  description: 'Adapted from CIM data models. P control model Type 3.  Reference: IEC Standard 61400-27-1 Section 6.6.5.3.'    
  properties:    
    WindDynamicsLookupTable:    
      description: 'The P control type 3 model with which this wind dynamics lookup table is associated. Default: ''list'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    WindGenTurbineType3IEC:    
      description: 'Wind turbine type 3 model with which this Wind control P type 3 model is associated. Default: None'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
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
    dpmax:    
      description: 'Maximum wind turbine power ramp rate (). It is project dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dtrisemaxlvrt:    
      description: 'Limitation of torque rise rate during LVRT for S (d). It is project dependent parameter. Default: 0.0'    
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
    kdtd:    
      description: 'Gain for active drive train damping (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kip:    
      description: 'PI controller integration parameter (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kpp:    
      description: 'PI controller proportional gain (). It is type dependent parameter. Default: 0.0'    
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
    mplvrt:    
      description: 'Enable LVRT power control mode (M true = 1: voltage control false = 0: reactive power control.  It is project dependent parameter. Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    omegaoffset:    
      description: 'Offset to reference value that limits controller action during rotor speed changes (omega). It is case dependent parameter. Default: 0.0'    
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
    pdtdmax:    
      description: 'Maximum active drive train damping power (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rramp:    
      description: 'Ramp limitation of torque, required in some grid codes (). It is project dependent parameter. Default: 0.0'    
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
    tdvs:    
      description: 'Timedelay after deep voltage sags (T). It is project dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    temin:    
      description: 'Minimum electrical generator torque (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tomegafilt:    
      description: 'Filter time constant for generator speed measurement (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tpfilt:    
      description: 'Filter time constant for power measurement (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tpord:    
      description: 'Time constant in power order lag (). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tufilt:    
      description: 'Filter time constant for voltage measurement (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tuscale:    
      description: 'Voltage scaling factor of reset-torque (T). It is project dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    twref:    
      description: 'Time constant in speed reference filter (). It is type dependent parameter. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: NGSI type. It has to be WindContPType3IEC    
      enum:    
        - WindContPType3IEC    
      type: string    
      x-ngsi:    
        type: Property    
    udvs:    
      description: 'Voltage limit for hold LVRT status after deep voltage sags (). It is project dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    updip:    
      description: 'Voltage dip threshold for P-control ().  Part of turbine control, often different (e.g 0.8) from converter thresholds. It is project dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    wdtd:    
      description: 'Active drive train damping frequency (omega). It can be calculated from two mass model parameters. It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    zeta:    
      description: 'Coefficient for active drive train damping (zeta). It is type dependent parameter. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindContPType3IEC/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/WindContPType3IEC/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
키-값으로 JSON-LD 형식의 WindContPType3IEC 예제를 사용할 수 없습니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
정규화된 JSON-LD 형식의 WindContPType3IEC 예제를 사용할 수 없습니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
키-값으로 JSON-LD 형식의 WindContPType3IEC 예제를 사용할 수 없습니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
정규화된 JSON-LD 형식의 WindContPType3IEC 예제를 사용할 수 없습니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
