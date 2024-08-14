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
    ExcELIN2 = 'ExcELIN2'


class ExcELIN2(BaseModel):
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
    efdbas: Optional[float] = Field(
        None, description='Gain (Efdbas).  Typical Value = 0.1. Default: 0.0'
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
    iefmax: Optional[float] = Field(
        None, description='Limiter (Iefmax).  Typical Value = 1. Default: 0.0'
    )
    iefmax2: Optional[float] = Field(
        None,
        description='Minimum open circuit excitation voltage (Iefmax2).  Typical Value = -5. Default: 0.0',
    )
    iefmin: Optional[float] = Field(
        None, description='Limiter (Iefmin).  Typical Value = 1. Default: 0.0'
    )
    k1: Optional[float] = Field(
        None,
        description='Voltage regulator input gain (K1).  Typical Value = 0. Default: 0.0',
    )
    k1ec: Optional[float] = Field(
        None,
        description='Voltage regulator input limit (K1ec).  Typical Value = 2. Default: 0.0',
    )
    k2: Optional[float] = Field(
        None, description='Gain (K2).  Typical Value = 5. Default: 0.0'
    )
    k3: Optional[float] = Field(
        None, description='Gain (K3).  Typical Value = 0.1. Default: 0.0'
    )
    k4: Optional[float] = Field(
        None, description='Gain (K4).  Typical Value = 0. Default: 0.0'
    )
    kd1: Optional[float] = Field(
        None,
        description='Voltage controller derivative gain (Kd1).  Typical Value = 34.5. Default: 0.0',
    )
    ke2: Optional[float] = Field(
        None, description='Gain (Ke2).  Typical Value = 0.1. Default: 0.0'
    )
    ketb: Optional[float] = Field(
        None, description='Gain (Ketb).  Typical Value = 0.06. Default: 0.0'
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
    pid1max: Optional[float] = Field(
        None,
        description='Controller follow up gain (PID1max).  Typical Value = 2. Default: 0.0',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    seve1: Optional[float] = Field(
        None,
        description='Exciter saturation function value at the corresponding exciter voltage, Ve1, back of commutating reactance (Se[Ve1]).  Typical Value = 0. Default: 0.0',
    )
    seve2: Optional[float] = Field(
        None,
        description='Exciter saturation function value at the corresponding exciter voltage, Ve2, back of commutating reactance (Se[Ve2]).  Typical Value = 1. Default: 0.0',
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    tb1: Optional[float] = Field(
        None,
        description='Voltage controller derivative washout time constant (Tb1).  Typical Value = 12.45. Default: 0',
    )
    te: Optional[float] = Field(
        None, description='Time constant (Te).  Typical Value = 0. Default: 0'
    )
    te2: Optional[float] = Field(
        None, description='Time Constant (Te2).  Typical Value = 1. Default: 0'
    )
    ti1: Optional[float] = Field(
        None,
        description='Controller follow up dead band (Ti1).  Typical Value = 0. Default: 0.0',
    )
    ti3: Optional[float] = Field(
        None, description='Time constant (Ti3).  Typical Value = 3. Default: 0'
    )
    ti4: Optional[float] = Field(
        None, description='Time constant (Ti4).  Typical Value = 0. Default: 0'
    )
    tr4: Optional[float] = Field(
        None, description='Time constant (Tr4).  Typical Value = 1. Default: 0'
    )
    type: Optional[Type6] = Field(None, description='NGSI type. It has to be ExcELIN2')
    upmax: Optional[float] = Field(
        None, description='Limiter (Upmax).  Typical Value = 3. Default: 0.0'
    )
    upmin: Optional[float] = Field(
        None, description='Limiter (Upmin).  Typical Value = 0. Default: 0.0'
    )
    ve1: Optional[float] = Field(
        None,
        description='Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1).  Typical Value = 3. Default: 0.0',
    )
    ve2: Optional[float] = Field(
        None,
        description='Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve2).  Typical Value = 0. Default: 0.0',
    )
    xp: Optional[float] = Field(
        None,
        description='Excitation transformer effective reactance (Xp).  Typical Value = 1. Default: 0.0',
    )
