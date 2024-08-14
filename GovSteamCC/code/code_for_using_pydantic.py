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
    GovSteamCC = 'GovSteamCC'


class GovSteamCC(BaseModel):
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
    dhp: Optional[float] = Field(
        None, description='HP damping factor (Dhp).  Typical Value = 0. Default: 0.0'
    )
    dlp: Optional[float] = Field(
        None, description='LP damping factor (Dlp).  Typical Value = 0. Default: 0.0'
    )
    fhp: Optional[float] = Field(
        None,
        description='Fraction of HP power ahead of reheater (Fhp).  Typical Value = 0.3. Default: 0.0',
    )
    flp: Optional[float] = Field(
        None,
        description='Fraction of LP power ahead of reheater (Flp).  Typical Value = 0.7. Default: 0.0',
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
    pmaxhp: Optional[float] = Field(
        None,
        description='Maximum HP value position (Pmaxhp).  Typical Value = 1. Default: 0.0',
    )
    pmaxlp: Optional[float] = Field(
        None,
        description='Maximum LP value position (Pmaxlp).  Typical Value = 1. Default: 0.0',
    )
    rhp: Optional[float] = Field(
        None, description='HP governor droop (Rhp).  Typical Value = 0.05. Default: 0.0'
    )
    rlp: Optional[float] = Field(
        None, description='LP governor droop (Rlp).  Typical Value = 0.05. Default: 0.0'
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    t1hp: Optional[float] = Field(
        None,
        description='HP governor time constant (T1hp).  Typical Value = 0.1. Default: 0',
    )
    t1lp: Optional[float] = Field(
        None,
        description='LP governor time constant (T1lp).  Typical Value = 0.1. Default: 0',
    )
    t3hp: Optional[float] = Field(
        None,
        description='HP turbine time constant (T3hp).  Typical Value = 0.1. Default: 0',
    )
    t3lp: Optional[float] = Field(
        None,
        description='LP turbine time constant (T3lp).  Typical Value = 0.1. Default: 0',
    )
    t4hp: Optional[float] = Field(
        None,
        description='HP turbine time constant (T4hp).  Typical Value = 0.1. Default: 0',
    )
    t4lp: Optional[float] = Field(
        None,
        description='LP turbine time constant (T4lp).  Typical Value = 0.1. Default: 0',
    )
    t5hp: Optional[float] = Field(
        None,
        description='HP reheater time constant (T5hp).  Typical Value = 10. Default: 0',
    )
    t5lp: Optional[float] = Field(
        None,
        description='LP reheater time constant (T5lp).  Typical Value = 10. Default: 0',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI type. It has to be GovSteamCC'
    )