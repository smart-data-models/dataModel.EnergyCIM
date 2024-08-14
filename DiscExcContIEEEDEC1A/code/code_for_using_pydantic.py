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
    DiscExcContIEEEDEC1A = 'DiscExcContIEEEDEC1A'


class DiscExcContIEEEDEC1A(BaseModel):
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
    esc: Optional[float] = Field(
        None,
        description='Speed change reference ().  Typical Value = 0.0015. Default: 0.0',
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
    kan: Optional[float] = Field(
        None,
        description='Discontinuous controller gain ().  Typical Value = 400. Default: 0.0',
    )
    ketl: Optional[float] = Field(
        None,
        description='Terminal voltage limiter gain ().  Typical Value = 47. Default: 0.0',
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
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    tan: Optional[float] = Field(
        None,
        description='Discontinuous controller time constant ().  Typical Value = 0.08. Default: 0',
    )
    td: Optional[float] = Field(
        None, description='Time constant ().  Typical Value = 0.03. Default: 0'
    )
    tl1: Optional[float] = Field(
        None, description='Time constant ().  Typical Value = 0.025. Default: 0'
    )
    tl2: Optional[float] = Field(
        None, description='Time constant ().  Typical Value = 1.25. Default: 0'
    )
    tw5: Optional[float] = Field(
        None, description='DEC washout time constant ().  Typical Value = 5. Default: 0'
    )
    type: Optional[Type6] = Field(
        None, description='NGSI type. It has to be DiscExcContIEEEDEC1A'
    )
    val: Optional[float] = Field(
        None,
        description='Regulator voltage reference ().  Typical Value = 5.5. Default: 0.0',
    )
    vanmax: Optional[float] = Field(
        None, description='Limiter for Van (). Default: 0.0'
    )
    vomax: Optional[float] = Field(
        None, description='Limiter ().  Typical Value = 0.3. Default: 0.0'
    )
    vomin: Optional[float] = Field(
        None, description='Limiter ().  Typical Value = 0.1. Default: 0.0'
    )
    vsmax: Optional[float] = Field(
        None, description='Limiter ().  Typical Value = 0.2. Default: 0.0'
    )
    vsmin: Optional[float] = Field(
        None, description='Limiter ().  Typical Value = -0.066. Default: 0.0'
    )
    vtc: Optional[float] = Field(
        None,
        description='Terminal voltage level reference ().  Typical Value = 0.95. Default: 0.0',
    )
    vtlmt: Optional[float] = Field(
        None, description='Voltage reference ().  Typical Value = 1.1. Default: 0.0'
    )
    vtm: Optional[float] = Field(
        None, description='Voltage limits ().  Typical Value = 1.13. Default: 0.0'
    )
    vtn: Optional[float] = Field(
        None, description='Voltage limits ().  Typical Value = 1.12. Default: 0.0'
    )
