<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: GovHydroWEH  
================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.EnergyCIM/blob/master/GovHydroWEH/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **CIM 데이터 모델에서 수정됨. 우드워드 전기 수력 발전기 모델.**  
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
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `db[number]`: 속도 데드 밴드(db). 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: 이 항목에 대한 설명  - `dicn[number]`: 적분 컨트롤러가 게이트 한계(Dicn)를 넘어 전진할 수 있도록 허용하는 값입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dpv[number]`: 파일럿 밸브 컨트롤러가 게이트 제한(Dpv)을 초과하여 전진할 수 있도록 허용하는 값입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `dturb[number]`: 터빈 감쇠 계수(Dturb).  단위 = 델타 P(MWbase의 PU)/델타 속도(PU). 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `feedbackSignal[number]`: 피드백 신호 선택(Sw) 참 = PID 출력(R-Perm-Gate=드룹 및 R-Perm-Pe=0인 경우) 거짓 = 전기 전력(R-Perm-Gate=0 및 R-Perm-Pe=드룹인 경우) 또는 거짓 = 게이트 위치(R-Perm-Gate=드룹 및 R-Perm-Pe=0인 경우). 기본값입니다: False  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl1[number]`: 유량 게이트 1(Fl1).  정상 상태 유량을 생성하기 위해 터빈을 통과하는 물의 흐름을 게이트 위치의 함수로 나타내는 룩업 테이블의 게이트 위치 지점 1에 대한 유량 값입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl2[number]`: 유량 게이트 2(Fl2).  정상 상태 유량을 생성하기 위해 터빈을 통과하는 물의 흐름을 게이트 위치의 함수로 나타내는 룩업 테이블의 게이트 위치 지점 2에 대한 유량 값입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl3[number]`: 유량 게이트 3(Fl3).  정상 상태 유량을 생성하기 위해 터빈을 통과하는 물의 흐름을 게이트 위치의 함수로 나타내는 룩업 테이블의 게이트 위치 지점 3에 대한 유량 값입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl4[number]`: 유량 게이트 4(Fl4).  정상 상태 유량을 생성하기 위해 터빈을 통과하는 물의 흐름을 게이트 위치의 함수로 나타내는 룩업 테이블의 게이트 위치 지점 4에 대한 유량 값입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fl5[number]`: 유량 게이트 5(Fl5).  정상 상태 유량을 생성하기 위해 터빈을 통과하는 물의 흐름을 게이트 위치의 함수로 나타내는 룩업 테이블의 게이트 위치 지점 5에 대한 유량 값입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp1[number]`: 유량 P1(Fp1).  터빈 유량의 함수로 기계의 단위 기계 전력당 MVA 정격을 나타내는 조회 테이블의 포인트 1에 대한 터빈 유량 값입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp10[number]`: 유량 P10(Fp10).  터빈 유량의 함수로 기계의 단위 기계 전력당 MVA 정격을 나타내는 조회 테이블의 포인트 10에 대한 터빈 유량 값입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp2[number]`: 유량 P2(Fp2).  터빈 유량의 함수로 기계의 단위 기계 전력당 MVA 등급을 나타내는 조회 테이블의 포인트 2에 대한 터빈 유량 값입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp3[number]`: 유량 P3(Fp3).  터빈 유량의 함수로 기계의 단위 기계 전력당 MVA 등급을 나타내는 조회 테이블의 포인트 3에 대한 터빈 유량 값입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp4[number]`: 유량 P4(Fp4).  터빈 유량의 함수로 기계의 단위당 기계 전력을 나타내는 조회 테이블의 포인트 4에 대한 터빈 유량 값입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp5[number]`: 유량 P5(Fp5).  터빈 유량의 함수로 기계의 단위 기계 전력당 MVA 등급을 나타내는 조회 테이블의 포인트 5에 대한 터빈 유량 값입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp6[number]`: 유량 P6(Fp6).  터빈 유량의 함수로 기계의 단위당 기계 전력을 나타내는 조회 테이블의 포인트 6에 대한 터빈 유량 값입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp7[number]`: 유량 P7(Fp7).  터빈 유량의 함수로 기계의 단위 기계 전력당 MVA 등급을 나타내는 조회 테이블의 포인트 7에 대한 터빈 유량 값입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp8[number]`: 유량 P8(Fp8).  터빈 유량의 함수로 기계의 단위당 기계 전력을 나타내는 조회 테이블의 포인트 8에 대한 터빈 유량 값입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `fp9[number]`: 유량 P9(Fp9).  터빈 유량의 함수로 기계의 단위당 기계 전력을 나타내는 조회 테이블의 포인트 9에 대한 터빈 유량 값입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gmax[number]`: 최대 게이트 위치(Gmax). 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gmin[number]`: 최소 게이트 위치(Gmin). 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gtmxcl[number]`: 최대 게이트 닫힘 속도(Gtmxcl). 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gtmxop[number]`: 최대 게이트 개방 속도(Gtmxop). 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv1[number]`: 게이트 1(Gv1).  정상 상태 흐름을 생성하기 위해 터빈을 통과하는 물의 흐름을 게이트 위치의 함수로 나타내는 룩업 테이블의 포인트 1에 대한 게이트 위치 값입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv2[number]`: 게이트 2(Gv2).  정상 상태 흐름을 생성하기 위해 터빈을 통과하는 물의 흐름을 게이트 위치의 함수로 나타내는 룩업 테이블의 포인트 2에 대한 게이트 위치 값입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv3[number]`: 게이트 3(Gv3).  정상 상태 흐름을 생성하기 위한 게이트 위치의 함수로 터빈을 통과하는 물의 흐름을 나타내는 룩업 테이블의 포인트 3에 대한 게이트 위치 값입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv4[number]`: 게이트 4(Gv4).  정상 상태 흐름을 생성하기 위해 터빈을 통과하는 물의 흐름을 게이트 위치의 함수로 나타내는 룩업 테이블의 포인트 4에 대한 게이트 위치 값입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `gv5[number]`: 게이트 5(Gv5).  정상 상태 흐름을 생성하기 위해 터빈을 통과하는 물의 흐름을 게이트 위치의 함수로 나타내는 룩업 테이블의 포인트 5에 대한 게이트 위치 값입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: 엔티티의 고유 식별자  - `kd[number]`: 파생 컨트롤러 파생 이득(Kd). 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `ki[number]`: 파생 컨트롤러 적분 이득(Ki). 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `kp[number]`: 파생 제어 게인(Kp). 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `mwbase[number]`: 전력 값의 기준(MWbase)(>0).  단위 = MW. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `pmss1[number]`: Pmss 유량 P1(Pmss1).  터빈 유량의 함수로서 기계 MVA 정격의 단위당 기계 전력을 나타내는 조회 테이블에 대한 터빈 유량 지점 1의 기계 전력 출력 Pmss입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss10[number]`: Pmss 유량 P10(Pmss10).  터빈 유량의 함수로서 기계 MVA 정격의 단위당 기계 전력을 나타내는 조회 테이블에 대한 터빈 유량 지점 10의 기계 전력 출력 Pmss입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss2[number]`: Pmss 유량 P2(Pmss2).  터빈 유량의 함수로서 기계 MVA 정격의 단위당 기계 전력을 나타내는 조회 테이블에 대한 터빈 유량 포인트 2의 기계 전력 출력 Pmss입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss3[number]`: Pmss 유량 P3(Pmss3).  터빈 유량의 함수로서 기계 MVA 정격의 단위당 기계 전력을 나타내는 조회 테이블에 대한 터빈 유량 지점 3의 기계 전력 출력 Pmss입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss4[number]`: Pmss 유량 P4(Pmss4).  터빈 유량의 함수로서 기계 MVA 정격의 단위당 기계 전력을 나타내는 조회 테이블에 대한 터빈 유량 포인트 4의 기계 전력 출력 Pmss입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss5[number]`: Pmss 유량 P5(Pmss5).  터빈 유량의 함수로서 기계 MVA 정격의 단위당 기계 전력을 나타내는 조회 테이블에 대한 터빈 유량 지점 5의 기계 전력 출력 Pmss입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss6[number]`: Pmss 유량 P6(Pmss6).  터빈 유량의 함수로서 기계 MVA 정격의 단위당 기계 전력을 나타내는 조회 테이블의 터빈 유량 포인트 6에 대한 기계 전력 출력 Pmss입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss7[number]`: Pmss 유량 P7(Pmss7).  터빈 유량의 함수로서 기계 MVA 정격의 단위당 기계 전력을 나타내는 조회 테이블에 대한 터빈 유량 포인트 7의 기계 전력 출력 Pmss입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss8[number]`: Pmss 유량 P8(Pmss8).  터빈 유량의 함수로서 기계 MVA 정격의 단위당 기계 전력을 나타내는 조회 테이블에 대한 터빈 유량 포인트 8의 기계 전력 출력 Pmss입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `pmss9[number]`: Pmss 유량 P9(Pmss9).  터빈 유량의 함수로서 기계 MVA 정격의 단위당 기계 전력을 나타내는 조회 테이블에 대한 터빈 유량 포인트 9의 기계 전력 출력 Pmss입니다. 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rpg[number]`: 거버너 출력 피드백을 위한 영구 드룹(R-Perm-Gate). 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `rpp[number]`: 전력 피드백을 위한 영구 드룹(R-Perm-Pe). 기본값: 0.0  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `td[number]`: 고주파 노이즈(Td)의 증폭을 방지하기 위해 고장 주파수 이상으로 미분 특성을 제한하는 미분 컨트롤러 시간 상수입니다. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tdv[number]`: 분배 밸브 시간 지연 시간 상수(Tdv). 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tg[number]`: 분배 밸브 컨트롤러가 게이트 이동 속도 제한(Tg)을 초과하여 전진할 수 있도록 허용하는 값입니다. 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tp[number]`: 파일럿 밸브 시간 지연 상수(Tp). 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tpe[number]`: 전력 드룹 시간 상수(Tpe). 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `tw[number]`: 물 관성 시간 상수(Tw)(>0). 기본값: 0  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI 유형. GovHydroWEH여야 합니다.  <!-- /30-PropertiesList -->  
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
GovHydroWEH:    
  description: Adapted from CIM data models. Woodward Electric Hydro Governor Model.    
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
    db:    
      description: 'Speed Dead Band (db). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    dicn:    
      description: 'Value to allow the integral controller to advance beyond the gate limits (Dicn). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dpv:    
      description: 'Value to allow the Pilot valve controller to advance beyond the gate limits (Dpv). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dturb:    
      description: 'Turbine damping factor (Dturb).  Unit = delta P (PU of MWbase) / delta speed (PU). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    feedbackSignal:    
      description: 'Feedback signal selection (Sw). true = PID Output (if R-Perm-Gate=droop and R-Perm-Pe=0) false = Electrical Power (if R-Perm-Gate=0 and R-Perm-Pe=droop) or false = Gate Position (if R-Perm-Gate=droop and R-Perm-Pe=0). Default: False'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fl1:    
      description: 'Flow Gate 1 (Fl1).  Flow value for gate position point 1 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fl2:    
      description: 'Flow Gate 2 (Fl2).  Flow value for gate position point 2 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fl3:    
      description: 'Flow Gate 3 (Fl3).  Flow value for gate position point 3 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fl4:    
      description: 'Flow Gate 4 (Fl4).  Flow value for gate position point 4 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fl5:    
      description: 'Flow Gate 5 (Fl5).  Flow value for gate position point 5 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp1:    
      description: 'Flow P1 (Fp1).  Turbine Flow value for point 1 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp10:    
      description: 'Flow P10 (Fp10).  Turbine Flow value for point 10 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp2:    
      description: 'Flow P2 (Fp2).  Turbine Flow value for point 2 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp3:    
      description: 'Flow P3 (Fp3).  Turbine Flow value for point 3 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp4:    
      description: 'Flow P4 (Fp4).  Turbine Flow value for point 4 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp5:    
      description: 'Flow P5 (Fp5).  Turbine Flow value for point 5 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp6:    
      description: 'Flow P6 (Fp6).  Turbine Flow value for point 6 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp7:    
      description: 'Flow P7 (Fp7).  Turbine Flow value for point 7 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp8:    
      description: 'Flow P8 (Fp8).  Turbine Flow value for point 8 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fp9:    
      description: 'Flow P9 (Fp9).  Turbine Flow value for point 9 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gmax:    
      description: 'Maximum Gate Position (Gmax). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gmin:    
      description: 'Minimum Gate Position (Gmin). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gtmxcl:    
      description: 'Maximum gate closing rate (Gtmxcl). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gtmxop:    
      description: 'Maximum gate opening rate (Gtmxop). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv1:    
      description: 'Gate 1 (Gv1).  Gate Position value for point 1 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv2:    
      description: 'Gate 2 (Gv2).  Gate Position value for point 2 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv3:    
      description: 'Gate 3 (Gv3).  Gate Position value for point 3 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv4:    
      description: 'Gate 4 (Gv4).  Gate Position value for point 4 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    gv5:    
      description: 'Gate 5 (Gv5).  Gate Position value for point 5 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0'    
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
    kd:    
      description: 'Derivative controller derivative gain (Kd). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ki:    
      description: 'Derivative controller Integral gain (Ki). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    kp:    
      description: 'Derivative control gain (Kp). Default: 0.0'    
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
    pmss1:    
      description: 'Pmss Flow P1 (Pmss1).  Mechanical Power output Pmss for Turbine Flow point 1 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss10:    
      description: 'Pmss Flow P10 (Pmss10).  Mechanical Power output Pmss for Turbine Flow point 10 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss2:    
      description: 'Pmss Flow P2 (Pmss2).  Mechanical Power output Pmss for Turbine Flow point 2 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss3:    
      description: 'Pmss Flow P3 (Pmss3).  Mechanical Power output Pmss for Turbine Flow point 3 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss4:    
      description: 'Pmss Flow P4 (Pmss4).  Mechanical Power output Pmss for Turbine Flow point 4 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss5:    
      description: 'Pmss Flow P5 (Pmss5).  Mechanical Power output Pmss for Turbine Flow point 5 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss6:    
      description: 'Pmss Flow P6 (Pmss6).  Mechanical Power output Pmss for Turbine Flow point 6 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss7:    
      description: 'Pmss Flow P7 (Pmss7).  Mechanical Power output Pmss for Turbine Flow point 7 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss8:    
      description: 'Pmss Flow P8 (Pmss8).  Mechanical Power output Pmss for Turbine Flow point 8 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pmss9:    
      description: 'Pmss Flow P9 (Pmss9).  Mechanical Power output Pmss for Turbine Flow point 9 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rpg:    
      description: 'Permanent droop for governor output feedback (R-Perm-Gate). Default: 0.0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    rpp:    
      description: 'Permanent droop for electrical power feedback (R-Perm-Pe). Default: 0.0'    
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
    td:    
      description: 'Derivative controller time constant to limit the derivative characteristic beyond a breakdown frequency to avoid amplification of high-frequency noise (Td). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tdv:    
      description: 'Distributive Valve time lag time constant (Tdv). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tg:    
      description: 'Value to allow the Distribution valve controller to advance beyond the gate movement rate limit (Tg). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tp:    
      description: 'Pilot Valve time lag time constant (Tp). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tpe:    
      description: 'Electrical power droop time constant (Tpe). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tw:    
      description: 'Water inertia time constant (Tw) (>0). Default: 0'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: NGSI type. It has to be GovHydroWEH    
      enum:    
        - GovHydroWEH    
      type: string    
      x-ngsi:    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovHydroWEH/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.CIMEnergyClasses/GovHydroWEH/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
키-값으로 JSON-LD 형식의 GovHydroWEH 예제를 사용할 수 없습니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
정규화된 JSON-LD 형식의 GovHydroWEH 예제는 사용할 수 없습니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
키 값으로 JSON-LD 형식의 GovHydroWEH 예제를 사용할 수 없습니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
정규화된 JSON-LD 형식의 GovHydroWEH 예제는 사용할 수 없습니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
