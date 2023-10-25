<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: 엔티티: GovSteamEU  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovSteamEU/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **CIM 데이터 모델에서 수정됨. PID 거버너가 있는 보일러 및 증기 터빈의 단순화된 모델**.  
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
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `chc[number]`: 제어 밸브 속도 폐쇄 한계(Chc).  단위 = PU/sec.  일반 값 = -3.3. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `cho[number]`: 제어 밸브 속도 개방 제한(Cho).  단위 = PU/sec.  일반 값 = 0.17. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `cic[number]`: 인터셉트 밸브 속도 폐쇄 제한(Cic).  일반 값 = -2.2. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `cio[number]`: 인터셉트 밸브 속도 개방 제한(Cio).  일반 값 = 0.123. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `db1[number]`: 주파수 보정기의 데드 밴드(db1).  일반 값 = 0. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `db2[number]`: 속도 조절기의 데드 밴드(db2).  일반 값 = 0.0004. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: 이 항목에 대한 설명  - `hhpmax[number]`: 최대 제어 밸브 위치(Hhpmax).  일반 값 = 1. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: 엔티티의 고유 식별자  - `ke[number]`: 전력 컨트롤러의 이득(Ke).  일반 값 = 0.65. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kfcor[number]`: 주파수 보정기의 이득(Kfcor).  일반 값 = 20. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `khp[number]`: HP 부품에서 생성되는 총 터빈 출력의 비율(Khp).  일반 값 = 0.277. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `klp[number]`: HP 부품에서 생성되는 총 터빈 출력의 비율(Klp).  일반 값 = 0.723. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kwcor[number]`: 스피드 거버너의 이득(Kwcor).  일반값 = 20. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `mwbase[number]`: 전력 값의 기준(MWbase)(>0).  단위 = MW. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `pmax[number]`: 터빈의 최대 유효 전력(Pmax).  일반 값 = 1. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `prhmax[number]`: 최대 저압 한계(Prhmax).  일반 값 = 1.4. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `simx[number]`: 인터셉트 밸브 전송 제한(Simx).  일반 값 = 0.425. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `tb[number]`: 보일러 시간 상수(Tb).  일반 값 = 100입니다. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tdp[number]`: 전력 컨트롤러의 미분 시간 상수(Tdp)입니다.  일반 값 = 0. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ten[number]`: 전기 유압 변환기 (10).  일반 값 = 0.1. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tf[number]`: 주파수 변환기 시간 상수(Tf).  일반 값 = 0. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tfp[number]`: 전력 컨트롤러의 시간 상수(Tfp)입니다.  일반 값 = 0. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `thp[number]`: 터빈의 고압(HP) 시간 상수(Thp).  일반 값 = 0.31. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tip[number]`: 전력 컨트롤러의 적분 시간 상수(팁).  일반 값 = 2. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tlp[number]`: 터빈의 저압(LP) 시간 상수(Tlp).  일반 값 = 0.45. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tp[number]`: 전력 변환기 시간 상수(Tp).  일반 값 = 0.07. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `trh[number]`: 터빈의 재가열기 시간 상수(Trh).  일반 값 = 8. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tvhp[number]`: 제어 밸브 서보 시간 상수(Tvhp).  일반 값 = 0.1. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tvip[number]`: 인터셉트 밸브 서보 시간 상수(Tvip).  일반 값 = 0.15. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw[number]`: 속도 변환기 시간 상수(Tw).  일반 값 = 0.02. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI 유형. GovSteamEU여야 합니다.  - `wfmax[number]`: 주파수 보정 상한(Wfmax).  일반 값 = 0.05. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `wfmin[number]`: 주파수 보정 하한(Wfmin).  일반 값 = -0.05. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `wmax1[number]`: 비상 속도 제어 하한(wmax1).  일반 값 = 1.025. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `wmax2[number]`: 비상 속도 제어 상한(wmax2).  일반 값 = 1.05. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `wwmax[number]`: 속도 조절기의 상한(Wwmax).  일반 값 = 0.1. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `wwmin[number]`: 조속기 주파수 보정 하한(Wwmin)입니다.  일반 값 = -1. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
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
GovSteamEU:    
  description: Adapted from CIM data models. Simplified model  of boiler and steam turbine with PID governor.    
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
    chc:    
      description: 'Control valves rate closing limit (Chc).  Unit = PU/sec.  Typical Value = -3.3. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    cho:    
      description: 'Control valves rate opening limit (Cho).  Unit = PU/sec.  Typical Value = 0.17. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    cic:    
      description: 'Intercept valves rate closing limit (Cic).  Typical Value = -2.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    cio:    
      description: 'Intercept valves rate opening limit (Cio).  Typical Value = 0.123. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    db1:    
      description: 'Dead band of the frequency corrector (db1).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    db2:    
      description: 'Dead band of the speed governor (db2).  Typical Value = 0.0004. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    hhpmax:    
      description: 'Maximum control valve position (Hhpmax).  Typical Value = 1. Default: 0.0'    
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
    ke:    
      description: 'Gain of the power controller (Ke).  Typical Value = 0.65. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kfcor:    
      description: 'Gain of the frequency corrector (Kfcor).  Typical Value = 20. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    khp:    
      description: 'Fraction of total turbine output generated by HP part (Khp).  Typical Value = 0.277. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    klp:    
      description: 'Fraction of total turbine output generated by HP part (Klp).  Typical Value = 0.723. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kwcor:    
      description: 'Gain of the speed governor (Kwcor).  Typical Value = 20. Default: 0.0'    
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
    mwbase:    
      description: 'Base for power values (MWbase) (>0).  Unit = MW. Default: 0.0'    
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
    pmax:    
      description: 'Maximal active power of the turbine (Pmax).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    prhmax:    
      description: 'Maximum low pressure limit (Prhmax).  Typical Value = 1.4. Default: 0.0'    
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
    simx:    
      description: 'Intercept valves transfer limit (Simx).  Typical Value = 0.425. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    tb:    
      description: 'Boiler time constant (Tb).  Typical Value = 100. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tdp:    
      description: 'Derivative time constant of the power controller (Tdp).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ten:    
      description: 'Electro hydraulic transducer (Ten).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tf:    
      description: 'Frequency transducer time constant (Tf).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tfp:    
      description: 'Time constant of the power controller (Tfp).  Typical Value = 0. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    thp:    
      description: 'High pressure (HP) time constant of the turbine (Thp).  Typical Value = 0.31. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tip:    
      description: 'Integral time constant of the power controller (Tip).  Typical Value = 2. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tlp:    
      description: 'Low pressure(LP) time constant of the turbine (Tlp).  Typical Value = 0.45. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tp:    
      description: 'Power transducer time constant (Tp).  Typical Value = 0.07. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    trh:    
      description: 'Reheater  time constant of the turbine (Trh).  Typical Value = 8. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tvhp:    
      description: 'Control valves servo time constant (Tvhp).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tvip:    
      description: 'Intercept valves servo time constant (Tvip).  Typical Value = 0.15. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tw:    
      description: 'Speed transducer time constant (Tw).  Typical Value = 0.02. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: NGSI type. It has to be GovSteamEU    
      enum:    
        - GovSteamEU    
      type: string    
      x-ngsi:    
        type: Property    
    wfmax:    
      description: 'Upper limit for frequency correction (Wfmax).  Typical Value = 0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    wfmin:    
      description: 'Lower limit for frequency correction (Wfmin).  Typical Value = -0.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    wmax1:    
      description: 'Emergency speed control lower limit (wmax1).  Typical Value = 1.025. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    wmax2:    
      description: 'Emergency speed control upper limit (wmax2).  Typical Value = 1.05. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    wwmax:    
      description: 'Upper limit for the speed governor (Wwmax).  Typical Value = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    wwmin:    
      description: 'Lower limit for the speed governor frequency correction (Wwmin).  Typical Value = -1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovSteamEU/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/GovSteamEU/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
키-값으로 JSON-LD 형식의 GovSteamEU 예제를 사용할 수 없습니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
정규화된 JSON-LD 형식의 GovSteamEU 예제를 사용할 수 없습니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
키 값으로 JSON-LD 형식의 GovSteamEU 예제를 사용할 수 없습니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
정규화된 JSON-LD 형식의 GovSteamEU 예제는 사용할 수 없습니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
