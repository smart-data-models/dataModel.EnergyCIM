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
    Pss5 = 'Pss5'


class Pss5(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    ctw2: Optional[float] = Field(
        None,
        description='Selector for Second washout enabling (C). true = second washout filter is bypassed false = second washout filter in use. Typical Value = true. Default: False',
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
    deadband: Optional[float] = Field(
        None,
        description='Stabilizer output dead band (DeadBand).  Typical Value = 0. Default: 0.0',
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
    isfreq: Optional[float] = Field(
        None,
        description='Selector for Frequency/shaft speed input (IsFreq). true = speed false = frequency. Typical Value = true. Default: False',
    )
    kf: Optional[float] = Field(
        None,
        description='Frequency/shaft speed input gain (K).  Typical Value = 5. Default: 0.0',
    )
    kpe: Optional[float] = Field(
        None,
        description='Electric power input gain (K).  Typical Value = 0.3. Default: 0.0',
    )
    kpss: Optional[float] = Field(
        None, description='PSS gain (K).  Typical Value = 1. Default: 0.0'
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
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
    pmm: Optional[float] = Field(
        None,
        description='Minimum power PSS enabling (P).  Typical Value = 0.25. Default: 0.0',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    tl1: Optional[float] = Field(
        None, description='Lead/lag time constant (T).  Typical Value = 0. Default: 0'
    )
    tl2: Optional[float] = Field(
        None, description='Lead/lag time constant (T).  Typical Value = 0. Default: 0'
    )
    tl3: Optional[float] = Field(
        None, description='Lead/lag time constant (T).  Typical Value = 0. Default: 0'
    )
    tl4: Optional[float] = Field(
        None, description='Lead/lag time constant (T).  Typical Value = 0. Default: 0'
    )
    tpe: Optional[float] = Field(
        None,
        description='Electric power filter time constant (T).  Typical Value = 0.05. Default: 0',
    )
    tw1: Optional[float] = Field(
        None, description='First WashOut (T).  Typical Value = 3.5. Default: 0'
    )
    tw2: Optional[float] = Field(
        None, description='Second WashOut (T).  Typical Value = 0. Default: 0'
    )
    type: Optional[Type6] = Field(None, description='NGSI type. It has to be Pss5')
    vadat: Optional[float] = Field(None, description=' Default: False')
    vsmn: Optional[float] = Field(
        None,
        description='Stabilizer output max limit (V).  Typical Value = -0.1. Default: 0.0',
    )
    vsmx: Optional[float] = Field(
        None,
        description='Stabilizer output min limit (V).  Typical Value = 0.1. Default: 0.0',
    )
