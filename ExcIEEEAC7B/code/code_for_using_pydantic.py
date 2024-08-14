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
    ExcIEEEAC7B = 'ExcIEEEAC7B'


class ExcIEEEAC7B(BaseModel):
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
        description='Rectifier loading factor proportional to commutating reactance (K). Typical Value = 0.18. Default: 0.0',
    )
    kd: Optional[float] = Field(
        None,
        description='Demagnetizing factor, a function of exciter alternator reactances (K).  Typical Value = 0.02. Default: 0.0',
    )
    kdr: Optional[float] = Field(
        None,
        description='Voltage regulator derivative gain (K).  Typical Value = 0. Default: 0.0',
    )
    ke: Optional[float] = Field(
        None,
        description='Exciter constant related to self-excited field (K).  Typical Value = 1. Default: 0.0',
    )
    kf1: Optional[float] = Field(
        None,
        description='Excitation control system stabilizer gain (K).  Typical Value = 0.212. Default: 0.0',
    )
    kf2: Optional[float] = Field(
        None,
        description='Excitation control system stabilizer gain (K).  Typical Value = 0. Default: 0.0',
    )
    kf3: Optional[float] = Field(
        None,
        description='Excitation control system stabilizer gain (K).  Typical Value = 0. Default: 0.0',
    )
    kia: Optional[float] = Field(
        None,
        description='Voltage regulator integral gain (K).  Typical Value = 59.69. Default: 0.0',
    )
    kir: Optional[float] = Field(
        None,
        description='Voltage regulator integral gain (K).  Typical Value = 4.24. Default: 0.0',
    )
    kl: Optional[float] = Field(
        None,
        description='Exciter field voltage lower limit parameter (K).  Typical Value = 10. Default: 0.0',
    )
    kp: Optional[float] = Field(
        None,
        description='Potential circuit gain coefficient (K).  Typical Value = 4.96. Default: 0.0',
    )
    kpa: Optional[float] = Field(
        None,
        description='Voltage regulator proportional gain (K).  Typical Value = 65.36. Default: 0.0',
    )
    kpr: Optional[float] = Field(
        None,
        description='Voltage regulator proportional gain (K).  Typical Value = 4.24. Default: 0.0',
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
    seve1: Optional[float] = Field(
        None,
        description='Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance (S[V]).  Typical Value = 0.44. Default: 0.0',
    )
    seve2: Optional[float] = Field(
        None,
        description='Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance (S[V]).  Typical Value = 0.075. Default: 0.0',
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    tdr: Optional[float] = Field(
        None, description='Lag time constant (T).  Typical Value = 0. Default: 0'
    )
    te: Optional[float] = Field(
        None,
        description='Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 1.1. Default: 0',
    )
    tf: Optional[float] = Field(
        None,
        description='Excitation control system stabilizer time constant (T).  Typical Value = 1. Default: 0',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI type. It has to be ExcIEEEAC7B'
    )
    vamax: Optional[float] = Field(
        None,
        description='Maximum voltage regulator output (V).  Typical Value = 1. Default: 0.0',
    )
    vamin: Optional[float] = Field(
        None,
        description='Minimum voltage regulator output (V).  Typical Value = -0.95. Default: 0.0',
    )
    ve1: Optional[float] = Field(
        None,
        description='Exciter alternator output voltages back of commutating reactance at which saturation is defined (V) equals V (V).  Typical Value = 6.3. Default: 0.0',
    )
    ve2: Optional[float] = Field(
        None,
        description='Exciter alternator output voltages back of commutating reactance at which saturation is defined (V).  Typical Value = 3.02. Default: 0.0',
    )
    vemin: Optional[float] = Field(
        None,
        description='Minimum exciter voltage output (V).  Typical Value = 0. Default: 0.0',
    )
    vfemax: Optional[float] = Field(
        None,
        description='Exciter field current limit reference (V).  Typical Value = 6.9. Default: 0.0',
    )
    vrmax: Optional[float] = Field(
        None,
        description='Maximum voltage regulator output (V).  Typical Value = 5.79. Default: 0.0',
    )
    vrmin: Optional[float] = Field(
        None,
        description='Minimum voltage regulator output (V).  Typical Value = -5.79. Default: 0.0',
    )
