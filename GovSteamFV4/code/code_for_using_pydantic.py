from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, constr


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class Type6(Enum):
    GovSteamFV4 = 'GovSteamFV4'


class GovSteamFV4(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    cpsmn: Optional[float] = Field(
        None,
        description='Minimum value of pressure regulator output (Cpsmn).  Typical Value = -1. Default: 0.0',
    )
    cpsmx: Optional[float] = Field(
        None,
        description='Maximum value of pressure regulator output (Cpsmx).  Typical Value = 1. Default: 0.0',
    )
    crmn: Optional[float] = Field(
        None,
        description='Minimum value of regulator set-point (Crmn).  Typical Value = 0. Default: 0.0',
    )
    crmx: Optional[float] = Field(
        None,
        description='Maximum value of regulator set-point (Crmx).  Typical Value = 1.2. Default: 0.0',
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    kdc: Optional[float] = Field(
        None,
        description='Derivative gain of pressure regulator (Kdc).  Typical Value = 1. Default: 0.0',
    )
    kf1: Optional[float] = Field(
        None,
        description='Frequency bias (reciprocal of droop) (Kf1).  Typical Value = 20. Default: 0.0',
    )
    kf3: Optional[float] = Field(
        None,
        description='Frequency control (reciprocal of droop) (Kf3).  Typical Value = 20. Default: 0.0',
    )
    khp: Optional[float] = Field(
        None,
        description='Fraction  of total turbine output generated by HP part (Khp).  Typical Value = 0.35. Default: 0.0',
    )
    kic: Optional[float] = Field(
        None,
        description='Integral gain of pressure regulator (Kic).  Typical Value = 0.0033. Default: 0.0',
    )
    kip: Optional[float] = Field(
        None,
        description='Integral gain of pressure feedback regulator (Kip).  Typical Value = 0.5. Default: 0.0',
    )
    kit: Optional[float] = Field(
        None,
        description='Integral gain of electro-hydraulic regulator (Kit).  Typical Value = 0.04. Default: 0.0',
    )
    kmp1: Optional[float] = Field(
        None,
        description='First gain coefficient of  intercept valves characteristic (Kmp1).  Typical Value = 0.5. Default: 0.0',
    )
    kmp2: Optional[float] = Field(
        None,
        description='Second gain coefficient of intercept valves characteristic (Kmp2).  Typical Value = 3.5. Default: 0.0',
    )
    kpc: Optional[float] = Field(
        None,
        description='Proportional gain of pressure regulator (Kpc).  Typical Value = 0.5. Default: 0.0',
    )
    kpp: Optional[float] = Field(
        None,
        description='Proportional gain of pressure feedback regulator (Kpp).  Typical Value = 1. Default: 0.0',
    )
    kpt: Optional[float] = Field(
        None,
        description='Proportional gain of electro-hydraulic regulator (Kpt).  Typical Value = 0.3. Default: 0.0',
    )
    krc: Optional[float] = Field(
        None,
        description='Maximum variation of fuel flow (Krc).  Typical Value = 0.05. Default: 0.0',
    )
    ksh: Optional[float] = Field(
        None,
        description='Pressure loss due to flow friction in the boiler tubes (Ksh).  Typical Value = 0.08. Default: 0.0',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    lpi: Optional[float] = Field(
        None,
        description='Maximum negative power error (Lpi).  Typical Value = -0.15. Default: 0.0',
    )
    lps: Optional[float] = Field(
        None,
        description='Maximum positive power error (Lps).  Typical Value = 0.03. Default: 0.0',
    )
    mnef: Optional[float] = Field(
        None,
        description='Lower limit for frequency correction (MN).  Typical Value = -0.05. Default: 0.0',
    )
    mxef: Optional[float] = Field(
        None,
        description='Upper limit for frequency correction (MX).  Typical Value = 0.05. Default: 0.0',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    pr1: Optional[float] = Field(
        None,
        description='First value of pressure set point static characteristic (Pr1).  Typical Value = 0.2. Default: 0.0',
    )
    pr2: Optional[float] = Field(
        None,
        description='Second value of pressure set point static characteristic, corresponding to Ps0 = 1.0 PU (Pr2).  Typical Value = 0.75. Default: 0.0',
    )
    psmn: Optional[float] = Field(
        None,
        description='Minimum value of pressure set point static characteristic (Psmn).  Typical Value = 1. Default: 0.0',
    )
    rsmimn: Optional[float] = Field(
        None,
        description='Minimum value of integral regulator (Rsmimn).  Typical Value = 0. Default: 0.0',
    )
    rsmimx: Optional[float] = Field(
        None,
        description='Maximum value of integral regulator (Rsmimx).  Typical Value = 1.1. Default: 0.0',
    )
    rvgmn: Optional[float] = Field(
        None,
        description='Minimum value of integral regulator (Rvgmn).  Typical Value = 0. Default: 0.0',
    )
    rvgmx: Optional[float] = Field(
        None,
        description='Maximum value of integral regulator (Rvgmx).  Typical Value = 1.2. Default: 0.0',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    srmn: Optional[float] = Field(
        None,
        description='Minimum valve opening (Srmn).  Typical Value = 0. Default: 0.0',
    )
    srmx: Optional[float] = Field(
        None,
        description='Maximum valve opening (Srmx).  Typical Value = 1.1. Default: 0.0',
    )
    srsmp: Optional[float] = Field(
        None,
        description='Intercept valves characteristic discontinuity point (Srsmp).  Typical Value = 0.43. Default: 0.0',
    )
    svmn: Optional[float] = Field(
        None,
        description='Maximum regulator gate closing velocity (Svmn).  Typical Value = -0.0333. Default: 0.0',
    )
    svmx: Optional[float] = Field(
        None,
        description='Maximum regulator gate opening velocity (Svmx).  Typical Value = 0.0333. Default: 0.0',
    )
    ta: Optional[float] = Field(
        None,
        description='Control valves rate opening time (Ta).  Typical Value = 0.8. Default: 0',
    )
    tam: Optional[float] = Field(
        None,
        description='Intercept valves rate opening time (Tam).  Typical Value = 0.8. Default: 0',
    )
    tc: Optional[float] = Field(
        None,
        description='Control valves rate closing time (Tc).  Typical Value = 0.5. Default: 0',
    )
    tcm: Optional[float] = Field(
        None,
        description='Intercept valves rate closing time (Tcm).  Typical Value = 0.5. Default: 0',
    )
    tdc: Optional[float] = Field(
        None,
        description='Derivative time constant of pressure regulator (Tdc).  Typical Value = 90. Default: 0',
    )
    tf1: Optional[float] = Field(
        None,
        description='Time constant of fuel regulation (Tf1).  Typical Value = 10. Default: 0',
    )
    tf2: Optional[float] = Field(
        None,
        description='Time constant of steam chest (Tf2).  Typical Value = 10. Default: 0',
    )
    thp: Optional[float] = Field(
        None,
        description='High pressure (HP) time constant of the turbine (Thp).  Typical Value = 0.15. Default: 0',
    )
    tmp: Optional[float] = Field(
        None,
        description='Low pressure (LP) time constant of the turbine (Tmp).  Typical Value = 0.4. Default: 0',
    )
    trh: Optional[float] = Field(
        None,
        description='Reheater  time constant of the turbine (Trh).  Typical Value = 10. Default: 0',
    )
    tv: Optional[float] = Field(
        None, description='Boiler time constant (Tv).  Typical Value = 60. Default: 0'
    )
    ty: Optional[float] = Field(
        None,
        description='Control valves servo time constant (Ty).  Typical Value = 0.1. Default: 0',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI type. It has to be GovSteamFV4'
    )
    y: Optional[float] = Field(
        None,
        description='Coefficient of linearized equations of turbine (Stodola formulation) (Y).  Typical Value = 0.13. Default: 0.0',
    )
    yhpmn: Optional[float] = Field(
        None,
        description='Minimum control valve position (Yhpmn).  Typical Value = 0. Default: 0.0',
    )
    yhpmx: Optional[float] = Field(
        None,
        description='Maximum control valve position (Yhpmx).  Typical Value = 1.1. Default: 0.0',
    )
    ympmn: Optional[float] = Field(
        None,
        description='Minimum intercept valve position (Ympmn).  Typical Value = 0. Default: 0.0',
    )
    ympmx: Optional[float] = Field(
        None,
        description='Maximum intercept valve position (Ympmx).  Typical Value = 1.1. Default: 0.0',
    )
