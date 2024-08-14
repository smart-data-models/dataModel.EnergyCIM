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
    ExcELIN1 = 'ExcELIN1'


class ExcELIN1(BaseModel):
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
    dpnf: Optional[float] = Field(
        None,
        description='Controller follow up dead band (Dpnf).  Typical Value = 0. Default: 0.0',
    )
    efmax: Optional[float] = Field(
        None,
        description='Maximum open circuit excitation voltage (Efmax).  Typical Value = 5. Default: 0.0',
    )
    efmin: Optional[float] = Field(
        None,
        description='Minimum open circuit excitation voltage (Efmin).  Typical Value = -5. Default: 0.0',
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
    ks1: Optional[float] = Field(
        None, description='Stabilizer Gain 1 (Ks1).  Typical Value = 0. Default: 0.0'
    )
    ks2: Optional[float] = Field(
        None, description='Stabilizer Gain 2 (Ks2).  Typical Value = 0. Default: 0.0'
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
    smax: Optional[float] = Field(
        None,
        description='Stabilizer Limit Output (smax).  Typical Value = 0.1. Default: 0.0',
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    tfi: Optional[float] = Field(
        None,
        description='Current transducer time constant (Tfi).  Typical Value = 0. Default: 0',
    )
    tnu: Optional[float] = Field(
        None,
        description='Controller reset time constant (Tnu).  Typical Value = 2. Default: 0',
    )
    ts1: Optional[float] = Field(
        None,
        description='Stabilizer Phase Lag Time Constant (Ts1).  Typical Value = 1. Default: 0',
    )
    ts2: Optional[float] = Field(
        None,
        description='Stabilizer Filter Time Constant (Ts2).  Typical Value = 1. Default: 0',
    )
    tsw: Optional[float] = Field(
        None, description='Stabilizer parameters (Tsw).  Typical Value = 3. Default: 0'
    )
    type: Optional[Type6] = Field(None, description='NGSI type. It has to be ExcELIN1')
    vpi: Optional[float] = Field(
        None,
        description='Current controller gain (Vpi).  Typical Value = 12.45. Default: 0.0',
    )
    vpnf: Optional[float] = Field(
        None,
        description='Controller follow up gain (Vpnf).  Typical Value = 2. Default: 0.0',
    )
    vpu: Optional[float] = Field(
        None,
        description='Voltage controller proportional gain (Vpu).  Typical Value = 34.5. Default: 0.0',
    )
    xe: Optional[float] = Field(
        None,
        description='Excitation transformer effective reactance (Xe) (>=0).  Xe represents the regulation of the transformer/rectifier unit.  Typical Value = 0.06. Default: 0.0',
    )
