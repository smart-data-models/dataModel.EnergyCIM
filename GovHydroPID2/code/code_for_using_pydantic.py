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
    GovHydroPID2 = 'GovHydroPID2'


class GovHydroPID2(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    atw: Optional[float] = Field(
        None,
        description='Factor multiplying Tw (Atw).  Typical Value = 0. Default: 0.0',
    )
    d: Optional[float] = Field(
        None,
        description='Turbine damping factor (D).  Unit = delta P / delta speed.  Typical Value = 0. Default: 0.0',
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
    feedbackSignal: Optional[float] = Field(
        None,
        description='Feedback signal type flag (Flag). true = use gate position feedback signal false = use Pe. Default: False',
    )
    g0: Optional[float] = Field(
        None,
        description='Gate opening at speed no load (G0).  Typical Value = 0. Default: 0.0',
    )
    g1: Optional[float] = Field(
        None,
        description='Intermediate gate opening (G1).  Typical Value = 0. Default: 0.0',
    )
    g2: Optional[float] = Field(
        None,
        description='Intermediate gate opening (G2).  Typical Value = 0. Default: 0.0',
    )
    gmax: Optional[float] = Field(
        None,
        description='Maximum gate opening (Gmax).  Typical Value = 0. Default: 0.0',
    )
    gmin: Optional[float] = Field(
        None,
        description='Minimum gate opening (Gmin).  Typical Value = 0. Default: 0.0',
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
    kd: Optional[float] = Field(
        None, description='Derivative gain (Kd).  Typical Value = 0. Default: 0.0'
    )
    ki: Optional[float] = Field(
        None,
        description='Reset gain (Ki).  Unit = PU/ sec.  Typical Value = 0. Default: 0.0',
    )
    kp: Optional[float] = Field(
        None, description='Proportional gain (Kp).  Typical Value = 0. Default: 0.0'
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
    p1: Optional[float] = Field(
        None,
        description='Power at gate opening G1 (P1).  Typical Value = 0. Default: 0.0',
    )
    p2: Optional[float] = Field(
        None,
        description='Power at gate opening G2 (P2).  Typical Value = 0. Default: 0.0',
    )
    p3: Optional[float] = Field(
        None,
        description='Power at full opened gate (P3).  Typical Value = 0. Default: 0.0',
    )
    rperm: Optional[float] = Field(
        None, description='Permanent drop (Rperm).  Typical Value = 0. Default: 0.0'
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    ta: Optional[float] = Field(
        None,
        description='Controller time constant (Ta) (>0).  Typical Value = 0. Default: 0',
    )
    tb: Optional[float] = Field(
        None,
        description='Gate servo time constant (Tb) (>0).  Typical Value = 0. Default: 0',
    )
    treg: Optional[float] = Field(
        None,
        description='Speed detector time constant (Treg).  Typical Value = 0. Default: 0',
    )
    tw: Optional[float] = Field(
        None,
        description='Water inertia time constant (Tw) (>0).  Typical Value = 0. Default: 0',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI type. It has to be GovHydroPID2'
    )
    velmax: Optional[float] = Field(
        None,
        description='Maximum gate opening velocity (Velmax).  Unit = PU/sec.  Typical Value = 0. Default: 0.0',
    )
    velmin: Optional[float] = Field(
        None,
        description='Maximum gate closing velocity (Velmin).  Unit = PU/sec.  Typical Value = 0. Default: 0.0',
    )
