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
    Pss1A = 'Pss1A'


class Pss1A(BaseModel):
    a1: Optional[float] = Field(
        None, description='Notch filter parameter (A1). Default: 0.0'
    )
    a2: Optional[float] = Field(
        None, description='Notch filter parameter (A2). Default: 0.0'
    )
    a3: Optional[float] = Field(
        None, description='Notch filter parameter (A3). Default: 0.0'
    )
    a4: Optional[float] = Field(
        None, description='Notch filter parameter (A4). Default: 0.0'
    )
    a5: Optional[float] = Field(
        None, description='Notch filter parameter (A5). Default: 0.0'
    )
    a6: Optional[float] = Field(
        None, description='Notch filter parameter (A6). Default: 0.0'
    )
    a7: Optional[float] = Field(
        None, description='Notch filter parameter (A7). Default: 0.0'
    )
    a8: Optional[float] = Field(
        None, description='Notch filter parameter (A8). Default: 0.0'
    )
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
    inputSignalType: Optional[float] = Field(
        None, description='Type of input signal. Default: None'
    )
    kd: Optional[float] = Field(
        None,
        description='Selector (Kd).  true = e used false = e not used. Default: False',
    )
    ks: Optional[float] = Field(None, description='Stabilizer gain (Ks). Default: 0.0')
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
    t1: Optional[float] = Field(
        None, description='Lead/lag time constant (T1). Default: 0'
    )
    t2: Optional[float] = Field(
        None, description='Lead/lag time constant (T2). Default: 0'
    )
    t3: Optional[float] = Field(
        None, description='Lead/lag time constant (T3). Default: 0'
    )
    t4: Optional[float] = Field(
        None, description='Lead/lag time constant (T4). Default: 0'
    )
    t5: Optional[float] = Field(
        None, description='Washout time constant (T5). Default: 0'
    )
    t6: Optional[float] = Field(
        None, description='Transducer time constant (T6). Default: 0'
    )
    tdelay: Optional[float] = Field(
        None, description='Time constant (Tdelay). Default: 0'
    )
    type: Optional[Type6] = Field(None, description='NGSI type. It has to be Pss1A')
    vcl: Optional[float] = Field(
        None, description='Stabilizer input cutoff threshold (Vcl). Default: 0.0'
    )
    vcu: Optional[float] = Field(
        None, description='Stabilizer input cutoff threshold (Vcu). Default: 0.0'
    )
    vrmax: Optional[float] = Field(
        None, description='Maximum stabilizer output (Vrmax). Default: 0.0'
    )
    vrmin: Optional[float] = Field(
        None, description='Minimum stabilizer output (Vrmin). Default: 0.0'
    )
