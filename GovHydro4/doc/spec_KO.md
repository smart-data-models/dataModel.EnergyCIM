<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: GovHydro4  
==============<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovHydro4/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **CIM 데이터 모델에서 수정됨. 수력 터빈 및 거버너. 간단한 펜스톡 구성과 전통적인 '대시팟' 유형의 유압 거버너를 갖춘 플랜트를 나타냅니다.  이 모델은 단순, 프란시스, 펠튼 또는 카플란 터빈을 나타내는 데 사용할 수 있습니다.**  
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
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `at[number]`: 터빈 게인(At).  일반 값 = 1.2. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bgv0[number]`: 카플란 블레이드 서보 포인트 0(Bgv0).  일반 값 = 0. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bgv1[number]`: 카플란 블레이드 서보 포인트 1(Bgv1).  일반 값 = 0. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bgv2[number]`: 카플란 블레이드 서보 포인트 2(Bgv2). 일반값 = 0. 일반값 프랜시스 = 0, 카플란 = 0.1. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bgv3[number]`: 카플란 블레이드 서보 포인트 3(Bgv3). 일반 값 = 0. 일반 값 프랜시스 = 0, 카플란 = 0.667. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bgv4[number]`: 카플란 블레이드 서보 포인트 4(Bgv4).  일반값 = 0. 일반값 프랜시스 = 0, 카플란 = 0.9. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bgv5[number]`: 카플란 블레이드 서보 포인트 5(Bgv5). 일반값 = 0. 일반값 프랜시스 = 0, 카플란 = 1. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `bmax[number]`: 최대 블레이드 조정 계수(Bmax). 일반값 = 0. 일반값 프랜시스 = 0, 카플란 = 1.1276. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `db1[number]`: 의도적 데드밴드 폭(db1).  단위 = Hz.  일반 값 = 0. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `db2[number]`: 의도하지 않은 데드 밴드(db2).  단위 = MW.  일반 값 = 0. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: 이 항목에 대한 설명  - `dturb[number]`: 터빈 감쇠 계수(Dturb).  단위 = 델타 P(MWbase의 PU) / 델타 속도(PU). 일반 값 = 0.5.  일반 값 프랜시스 = 1.1, 카플란 = 1.1. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `eps[number]`: 의도적 DB 히스테리시스(eps).  단위 = Hz.  일반 값 = 0. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gmax[number]`: 최대 게이트 개방, MWbase의 PU(Gmax).  일반 값 = 1. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gmin[number]`: 최소 게이트 개방, MWbase의 PU(Gmin).  일반 값 = 0. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv0[number]`: 비선형 게인 포인트 0, PU gv(Gv0). 일반값 = 0. 일반값 프랜시스 = 0.1, 카플란 = 0.1. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv1[number]`: 비선형 게인 포인트 1, PU gv(Gv1). 일반값 = 0. 일반값 프랜시스 = 0.4, 카플란 = 0.4. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv2[number]`: 비선형 게인 포인트 2, PU gv(Gv2). 일반값 = 0. 일반값 프랜시스 = 0.5, 카플란 = 0.5. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv3[number]`: 비선형 게인 포인트 3, PU gv(Gv3). 일반값 = 0. 일반값 프랜시스 = 0.7, 카플란 = 0.7. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv4[number]`: 비선형 게인 포인트 4, PU gv(Gv4). 일반값 = 0. 일반값 프랜시스 = 0.8, 카플란 = 0.8. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv5[number]`: 비선형 게인 포인트 5, PU gv(Gv5). 일반값 = 0. 일반값 프랜시스 = 0.9, 카플란 = 0.9. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `hdam[number]`: 댐에서 사용 가능한 헤드(hdam).  일반 값 = 1. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `mwbase[number]`: 전력 값의 기준(MWbase)(>0).  단위 = MW. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `pgv0[number]`: 비선형 게인 포인트 0, PU 전력(Pgv0).  일반 값 = 0. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pgv1[number]`: 비선형 게인 포인트 1, PU 전력(Pgv1). 일반값 = 0. 일반값 프랜시스 = 0.42, 카플란 = 0.35. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pgv2[number]`: 비선형 게인 포인트 2, PU 전력(Pgv2). 일반값 = 0. 일반값 프랜시스 = 0.56, 카플란 = 0.468. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pgv3[number]`: 비선형 게인 포인트 3, PU 전력(Pgv3). 일반값 = 0. 일반값 프랜시스 = 0.8, 카플란 = 0.796. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pgv4[number]`: 비선형 게인 포인트 4, PU 전력(Pgv4). 일반값 = 0. 일반값 프랜시스 = 0.9, 카플란 = 0.917. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pgv5[number]`: 비선형 게인 포인트 5, PU 전력(Pgv5).  일반값 = 0. 일반값 프랜시스 = 0.97, 카플란 = 0.99. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `qn1[number]`: 공칭 수두에서의 무부하 유량(Qnl). 일반 값 = 0.08.  일반 값 프랜시스 = 0, 카플란 = 0. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rperm[number]`: 영구 처짐(Rperm).  일반 값 = 0.05. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rtemp[number]`: 일시적 드룹(Rtemp).  일반 값 = 0.3. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `tblade[number]`: 블레이드 서보 시간 상수(T블레이드).  일반 값 = 100. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tg[number]`: 게이트 서보 시간 상수(Tg)(>0).  일반 값 = 0.5. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tp[number]`: 파일럿 서보 시간 상수(Tp).  일반 값 = 0.1. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tr[number]`: 대시보드 시간 상수(Tr)(>0).  일반 값 = 5. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw[number]`: 물 관성 시간 상수(Tw)(>0).  일반 값 = 1. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI 유형. GovHydro4여야 합니다.  - `uc[number]`: 최대 게이트 폐쇄 속도(Uc).  일반 값 = 0.2. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `uo[number]`: 최대 게이트 개방 속도(Uo).  일반적인 Vlaue = 0.2. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
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
GovHydro4:    
  description: 'Adapted from CIM data models. Hydro turbine and governor. Represents plants with straight-forward penstock configurations and hydraulic governors of traditional ''dashpot'' type.  This model can be used to represent simple, Francis, Pelton or Kaplan turbines.'    
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
    at:    
      description: 'Turbine gain (At).  Typical Value = 1.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bgv0:    
      description: 'Kaplan blade servo point 0 (Bgv0).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bgv1:    
      description: 'Kaplan blade servo point 1 (Bgv1).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bgv2:    
      description: 'Kaplan blade servo point 2 (Bgv2). Typical Value = 0.  Typical Value Francis = 0, Kaplan = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bgv3:    
      description: 'Kaplan blade servo point 3 (Bgv3). Typical Value = 0.  Typical Value Francis = 0, Kaplan = 0.667. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bgv4:    
      description: 'Kaplan blade servo point 4 (Bgv4).  Typical Value = 0.  Typical Value Francis = 0, Kaplan = 0.9. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bgv5:    
      description: 'Kaplan blade servo point 5 (Bgv5). Typical Value = 0.  Typical Value Francis = 0, Kaplan = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    bmax:    
      description: 'Maximum blade adjustment factor (Bmax). Typical Value = 0.  Typical Value Francis = 0, Kaplan = 1.1276. Default: 0.0'    
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
      description: 'Intentional deadband width (db1).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    db2:    
      description: 'Unintentional dead-band (db2).  Unit = MW.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    dturb:    
      description: 'Turbine damping factor (Dturb).  Unit = delta P (PU of MWbase) / delta speed (PU). Typical Value = 0.5.  Typical Value Francis = 1.1, Kaplan = 1.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    eps:    
      description: 'Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gmax:    
      description: 'Maximum gate opening, PU of MWbase (Gmax).  Typical Value = 1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gmin:    
      description: 'Minimum gate opening, PU of MWbase (Gmin).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv0:    
      description: 'Nonlinear gain point 0, PU gv (Gv0). Typical Value = 0.  Typical Value Francis = 0.1, Kaplan = 0.1. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv1:    
      description: 'Nonlinear gain point 1, PU gv (Gv1). Typical Value = 0.  Typical Value Francis = 0.4, Kaplan = 0.4. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv2:    
      description: 'Nonlinear gain point 2, PU gv (Gv2). Typical Value = 0.  Typical Value Francis = 0.5, Kaplan = 0.5. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv3:    
      description: 'Nonlinear gain point 3, PU gv (Gv3). Typical Value = 0.  Typical Value Francis = 0.7, Kaplan = 0.7. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv4:    
      description: 'Nonlinear gain point 4, PU gv (Gv4). Typical Value = 0.  Typical Value Francis = 0.8, Kaplan = 0.8. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv5:    
      description: 'Nonlinear gain point 5, PU gv (Gv5). Typical Value = 0.  Typical Value Francis = 0.9, Kaplan = 0.9. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    hdam:    
      description: 'Head available at dam (hdam).  Typical Value = 1. Default: 0.0'    
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
    pgv0:    
      description: 'Nonlinear gain point 0, PU power (Pgv0).  Typical Value = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pgv1:    
      description: 'Nonlinear gain point 1, PU power (Pgv1). Typical Value = 0.  Typical Value Francis = 0.42, Kaplan = 0.35. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pgv2:    
      description: 'Nonlinear gain point 2, PU power (Pgv2). Typical Value = 0.  Typical Value Francis = 0.56, Kaplan = 0.468. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pgv3:    
      description: 'Nonlinear gain point 3, PU power (Pgv3). Typical Value = 0.  Typical Value Francis = 0.8, Kaplan = 0.796. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pgv4:    
      description: 'Nonlinear gain point 4, PU power (Pgv4). Typical Value = 0.  Typical Value Francis = 0.9, Kaplan = 0.917. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pgv5:    
      description: 'Nonlinear gain point 5, PU power (Pgv5).  Typical Value = 0.  Typical Value Francis = 0.97, Kaplan = 0.99. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    qn1:    
      description: 'No-load flow at nominal head (Qnl). Typical Value = 0.08.  Typical Value Francis = 0, Kaplan = 0. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rperm:    
      description: 'Permanent droop (Rperm).  Typical Value = 0.05. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rtemp:    
      description: 'Temporary droop (Rtemp).  Typical Value = 0.3. Default: 0'    
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
    tblade:    
      description: 'Blade servo time constant (Tblade).  Typical Value = 100. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tg:    
      description: 'Gate servo time constant (Tg) (>0).  Typical Value = 0.5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tp:    
      description: 'Pilot servo time constant (Tp).  Typical Value = 0.1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tr:    
      description: 'Dashpot time constant (Tr) (>0).  Typical Value = 5. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tw:    
      description: 'Water inertia time constant (Tw) (>0).  Typical Value = 1. Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: NGSI type. It has to be GovHydro4    
      enum:    
        - GovHydro4    
      type: string    
      x-ngsi:    
        type: Property    
    uc:    
      description: 'Max gate closing velocity (Uc).  Typical Value = 0.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    uo:    
      description: 'Max gate opening velocity (Uo).  Typical Vlaue = 0.2. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovHydro4/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/GovHydro4/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
키-값으로 JSON-LD 형식의 GovHydro4 예제를 사용할 수 없습니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
정규화된 JSON-LD 형식의 GovHydro4 예제는 사용할 수 없습니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
키-값으로 JSON-LD 형식의 GovHydro4 예제를 사용할 수 없습니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
정규화된 JSON-LD 형식의 GovHydro4 예제는 사용할 수 없습니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
