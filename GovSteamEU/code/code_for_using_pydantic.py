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
    GovSteamEU = 'GovSteamEU'


class GovSteamEU(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    chc: Optional[float] = Field(
        None,
        description='Control valves rate closing limit (Chc).  Unit = PU/sec.  Typical Value = -3.3. Default: 0.0',
    )
    cho: Optional[float] = Field(
        None,
        description='Control valves rate opening limit (Cho).  Unit = PU/sec.  Typical Value = 0.17. Default: 0.0',
    )
    cic: Optional[float] = Field(
        None,
        description='Intercept valves rate closing limit (Cic).  Typical Value = -2.2. Default: 0.0',
    )
    cio: Optional[float] = Field(
        None,
        description='Intercept valves rate opening limit (Cio).  Typical Value = 0.123. Default: 0.0',
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
    db1: Optional[float] = Field(
        None,
        description='Dead band of the frequency corrector (db1).  Typical Value = 0. Default: 0.0',
    )
    db2: Optional[float] = Field(
        None,
        description='Dead band of the speed governor (db2).  Typical Value = 0.0004. Default: 0.0',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    hhpmax: Optional[float] = Field(
        None,
        description='Maximum control valve position (Hhpmax).  Typical Value = 1. Default: 0.0',
    )
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
    ke: Optional[float] = Field(
        None,
        description='Gain of the power controller (Ke).  Typical Value = 0.65. Default: 0.0',
    )
    kfcor: Optional[float] = Field(
        None,
        description='Gain of the frequency corrector (Kfcor).  Typical Value = 20. Default: 0.0',
    )
    khp: Optional[float] = Field(
        None,
        description='Fraction of total turbine output generated by HP part (Khp).  Typical Value = 0.277. Default: 0.0',
    )
    klp: Optional[float] = Field(
        None,
        description='Fraction of total turbine output generated by HP part (Klp).  Typical Value = 0.723. Default: 0.0',
    )
    kwcor: Optional[float] = Field(
        None,
        description='Gain of the speed governor (Kwcor).  Typical Value = 20. Default: 0.0',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    mwbase: Optional[float] = Field(
        None,
        description='Base for power values (MWbase) (>0).  Unit = MW. Default: 0.0',
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
    pmax: Optional[float] = Field(
        None,
        description='Maximal active power of the turbine (Pmax).  Typical Value = 1. Default: 0.0',
    )
    prhmax: Optional[float] = Field(
        None,
        description='Maximum low pressure limit (Prhmax).  Typical Value = 1.4. Default: 0.0',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    simx: Optional[float] = Field(
        None,
        description='Intercept valves transfer limit (Simx).  Typical Value = 0.425. Default: 0.0',
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    tb: Optional[float] = Field(
        None, description='Boiler time constant (Tb).  Typical Value = 100. Default: 0'
    )
    tdp: Optional[float] = Field(
        None,
        description='Derivative time constant of the power controller (Tdp).  Typical Value = 0. Default: 0',
    )
    ten: Optional[float] = Field(
        None,
        description='Electro hydraulic transducer (Ten).  Typical Value = 0.1. Default: 0',
    )
    tf: Optional[float] = Field(
        None,
        description='Frequency transducer time constant (Tf).  Typical Value = 0. Default: 0',
    )
    tfp: Optional[float] = Field(
        None,
        description='Time constant of the power controller (Tfp).  Typical Value = 0. Default: 0',
    )
    thp: Optional[float] = Field(
        None,
        description='High pressure (HP) time constant of the turbine (Thp).  Typical Value = 0.31. Default: 0',
    )
    tip: Optional[float] = Field(
        None,
        description='Integral time constant of the power controller (Tip).  Typical Value = 2. Default: 0',
    )
    tlp: Optional[float] = Field(
        None,
        description='Low pressure(LP) time constant of the turbine (Tlp).  Typical Value = 0.45. Default: 0',
    )
    tp: Optional[float] = Field(
        None,
        description='Power transducer time constant (Tp).  Typical Value = 0.07. Default: 0',
    )
    trh: Optional[float] = Field(
        None,
        description='Reheater  time constant of the turbine (Trh).  Typical Value = 8. Default: 0',
    )
    tvhp: Optional[float] = Field(
        None,
        description='Control valves servo time constant (Tvhp).  Typical Value = 0.1. Default: 0',
    )
    tvip: Optional[float] = Field(
        None,
        description='Intercept valves servo time constant (Tvip).  Typical Value = 0.15. Default: 0',
    )
    tw: Optional[float] = Field(
        None,
        description='Speed transducer time constant (Tw).  Typical Value = 0.02. Default: 0',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI type. It has to be GovSteamEU'
    )
    wfmax: Optional[float] = Field(
        None,
        description='Upper limit for frequency correction (Wfmax).  Typical Value = 0.05. Default: 0.0',
    )
    wfmin: Optional[float] = Field(
        None,
        description='Lower limit for frequency correction (Wfmin).  Typical Value = -0.05. Default: 0.0',
    )
    wmax1: Optional[float] = Field(
        None,
        description='Emergency speed control lower limit (wmax1).  Typical Value = 1.025. Default: 0.0',
    )
    wmax2: Optional[float] = Field(
        None,
        description='Emergency speed control upper limit (wmax2).  Typical Value = 1.05. Default: 0.0',
    )
    wwmax: Optional[float] = Field(
        None,
        description='Upper limit for the speed governor (Wwmax).  Typical Value = 0.1. Default: 0.0',
    )
    wwmin: Optional[float] = Field(
        None,
        description='Lower limit for the speed governor frequency correction (Wwmin).  Typical Value = -1. Default: 0.0',
    )
