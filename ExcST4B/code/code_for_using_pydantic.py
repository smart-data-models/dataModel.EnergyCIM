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
    ExcST4B = 'ExcST4B'


class ExcST4B(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
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
    kc: Optional[float] = Field(
        None,
        description='Rectifier loading factor proportional to commutating reactance (Kc). Typical Value = 0.113. Default: 0.0',
    )
    kg: Optional[float] = Field(
        None,
        description='Feedback gain constant of the inner loop field regulator (Kg). Typical Value = 0. Default: 0.0',
    )
    ki: Optional[float] = Field(
        None,
        description='Potential circuit gain coefficient (Ki).  Typical Value = 0. Default: 0.0',
    )
    kim: Optional[float] = Field(
        None,
        description='Voltage regulator integral gain output (Kim).  Typical Value = 0. Default: 0.0',
    )
    kir: Optional[float] = Field(
        None,
        description='Voltage regulator integral gain (Kir).  Typical Value = 10.75. Default: 0.0',
    )
    kp: Optional[float] = Field(
        None,
        description='Potential circuit gain coefficient (Kp).  Typical Value = 9.3. Default: 0.0',
    )
    kpm: Optional[float] = Field(
        None,
        description='Voltage regulator proportional gain output (Kpm).  Typical Value = 1. Default: 0.0',
    )
    kpr: Optional[float] = Field(
        None,
        description='Voltage regulator proportional gain (Kpr).  Typical Value = 10.75. Default: 0.0',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    lvgate: Optional[float] = Field(
        None,
        description='Selector (LVgate). true = LVgate is part of the block diagram false = LVgate is not part of the block diagram.  Typical Value = false. Default: False',
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
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    ta: Optional[float] = Field(
        None,
        description='Voltage regulator time constant (Ta).  Typical Value = 0.02. Default: 0',
    )
    thetap: Optional[float] = Field(
        None,
        description='Potential circuit phase angle (thetap).  Typical Value = 0. Default: 0.0',
    )
    type: Optional[Type6] = Field(None, description='NGSI type. It has to be ExcST4B')
    uel: Optional[float] = Field(
        None,
        description='Selector (Uel). true = UEL is part of block diagram false = UEL is not part of block diagram.  Typical Value = false. Default: False',
    )
    vbmax: Optional[float] = Field(
        None,
        description='Maximum excitation voltage (Vbmax).  Typical Value = 11.63. Default: 0.0',
    )
    vgmax: Optional[float] = Field(
        None,
        description='Maximum inner loop feedback voltage (Vgmax).  Typical Value = 5.8. Default: 0.0',
    )
    vmmax: Optional[float] = Field(
        None,
        description='Maximum inner loop output (Vmmax).  Typical Value = 99. Default: 0.0',
    )
    vmmin: Optional[float] = Field(
        None,
        description='Minimum inner loop output (Vmmin).  Typical Value = -99. Default: 0.0',
    )
    vrmax: Optional[float] = Field(
        None,
        description='Maximum voltage regulator output (Vrmax).  Typical Value = 1. Default: 0.0',
    )
    vrmin: Optional[float] = Field(
        None,
        description='Minimum voltage regulator output (Vrmin).  Typical Value = -0.87. Default: 0.0',
    )
    xl: Optional[float] = Field(
        None,
        description='Reactance associated with potential source (Xl).  Typical Value = 0.124. Default: 0.0',
    )
