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
    GovGAST3 = 'GovGAST3'


class GovGAST3(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    bca: Optional[float] = Field(
        None,
        description='Acceleration limit set-point (Bca).  Unit = 1/s.  Typical Value = 0.01. Default: 0.0',
    )
    bp: Optional[float] = Field(
        None, description='Droop (bp).  Typical Value = 0.05. Default: 0.0'
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
    dtc: Optional[float] = Field(
        None,
        description='Exhaust temperature variation due to fuel flow increasing from 0 to 1 PU (deltaTc).  Typical Value = 390. Default: 0.0',
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
    ka: Optional[float] = Field(
        None, description='Minimum fuel flow (Ka).  Typical Value = 0.23. Default: 0.0'
    )
    kac: Optional[float] = Field(
        None, description='Fuel system feedback (K).  Typical Value = 0. Default: 0.0'
    )
    kca: Optional[float] = Field(
        None,
        description='Acceleration control integral gain (Kca). Unit = 1/s.  Typical Value = 100. Default: 0.0',
    )
    ksi: Optional[float] = Field(
        None,
        description='Gain of radiation shield (Ksi).  Typical Value = 0.8. Default: 0.0',
    )
    ky: Optional[float] = Field(
        None,
        description='Coefficient of transfer function of fuel valve positioner (Ky).  Typical Value = 1. Default: 0.0',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    mnef: Optional[float] = Field(
        None,
        description='Fuel flow maximum negative error value (MN).  Typical Value = -0.05. Default: 0.0',
    )
    mxef: Optional[float] = Field(
        None,
        description='Fuel flow maximum positive error value (MX).  Typical Value = 0.05. Default: 0.0',
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
    rcmn: Optional[float] = Field(
        None,
        description='Minimum fuel flow (RCMN).  Typical Value = -0.1. Default: 0.0',
    )
    rcmx: Optional[float] = Field(
        None, description='Maximum fuel flow (RCMX).  Typical Value = 1. Default: 0.0'
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    tac: Optional[float] = Field(
        None,
        description='Fuel control time constant (Tac).  Typical Value = 0.1. Default: 0',
    )
    tc: Optional[float] = Field(
        None,
        description='Compressor discharge volume time constant (Tc).  Typical Value = 0.2. Default: 0',
    )
    td: Optional[float] = Field(
        None,
        description='Temperature controller derivative gain (Td).  Typical Value = 3.3. Default: 0',
    )
    tfen: Optional[float] = Field(
        None,
        description='Turbine rated exhaust temperature correspondent to Pm=1 PU (Tfen).  Typical Value = 540. Default: 0.0',
    )
    tg: Optional[float] = Field(
        None,
        description='Time constant of speed governor (Tg).  Typical Value = 0.05. Default: 0',
    )
    tsi: Optional[float] = Field(
        None,
        description='Time constant of radiation shield (Tsi).  Typical Value = 15. Default: 0',
    )
    tt: Optional[float] = Field(
        None,
        description='Temperature controller integration rate (Tt).  Typical Value = 250. Default: 0.0',
    )
    ttc: Optional[float] = Field(
        None,
        description='Time constant of thermocouple (Ttc).  Typical Value = 2.5. Default: 0',
    )
    ty: Optional[float] = Field(
        None,
        description='Time constant of fuel valve positioner (Ty).  Typical Value = 0.2. Default: 0',
    )
    type: Optional[Type6] = Field(None, description='NGSI type. It has to be GovGAST3')
