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
    ExcREXS = 'ExcREXS'


class ExcREXS(BaseModel):
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
    e1: Optional[float] = Field(
        None, description='Field voltage value 1 (E1).  Typical Value = 3. Default: 0.0'
    )
    e2: Optional[float] = Field(
        None, description='Field voltage value 2 (E2).  Typical Value = 4. Default: 0.0'
    )
    fbf: Optional[float] = Field(
        None,
        description='Rate feedback signal flag (Fbf). Typical Value = fieldCurrent. Default: None',
    )
    flimf: Optional[float] = Field(
        None, description='Limit type flag (Flimf).  Typical Value = 0. Default: 0.0'
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
    kc: Optional[float] = Field(
        None,
        description='Rectifier regulation factor (Kc).  Typical Value = 0.05. Default: 0.0',
    )
    kd: Optional[float] = Field(
        None,
        description='Exciter regulation factor (Kd).  Typical Value = 2. Default: 0.0',
    )
    ke: Optional[float] = Field(
        None,
        description='Exciter field proportional constant (Ke).  Typical Value = 1. Default: 0.0',
    )
    kefd: Optional[float] = Field(
        None,
        description='Field voltage feedback gain (Kefd).  Typical Value = 0. Default: 0.0',
    )
    kf: Optional[float] = Field(
        None, description='Rate feedback gain (Kf).  Typical Value = 0.05. Default: 0'
    )
    kh: Optional[float] = Field(
        None,
        description='Field voltage controller feedback gain (Kh).  Typical Value = 0. Default: 0.0',
    )
    kii: Optional[float] = Field(
        None,
        description='Field Current Regulator Integral Gain (Kii).  Typical Value = 0. Default: 0.0',
    )
    kip: Optional[float] = Field(
        None,
        description='Field Current Regulator Proportional Gain (Kip).  Typical Value = 1. Default: 0.0',
    )
    ks: Optional[float] = Field(
        None,
        description='Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0. Default: 0.0',
    )
    kvi: Optional[float] = Field(
        None,
        description='Voltage Regulator Integral Gain (Kvi).  Typical Value = 0. Default: 0.0',
    )
    kvp: Optional[float] = Field(
        None,
        description='Voltage Regulator Proportional Gain (Kvp).  Typical Value = 2800. Default: 0.0',
    )
    kvphz: Optional[float] = Field(
        None, description='V/Hz limiter gain (Kvphz).  Typical Value = 0. Default: 0.0'
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    nvphz: Optional[float] = Field(
        None,
        description='Pickup speed of V/Hz limiter (Nvphz).  Typical Value = 0. Default: 0.0',
    )
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
    se1: Optional[float] = Field(
        None,
        description='Saturation factor at E1 (Se1).  Typical Value = 0.0001. Default: 0.0',
    )
    se2: Optional[float] = Field(
        None,
        description='Saturation factor at E2 (Se2).  Typical Value = 0.001. Default: 0.0',
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
        description='Voltage Regulator time constant (Ta).  Typical Value = 0.01. Default: 0',
    )
    tb1: Optional[float] = Field(
        None, description='Lag time constant (Tb1).  Typical Value = 0. Default: 0'
    )
    tb2: Optional[float] = Field(
        None, description='Lag time constant (Tb2).  Typical Value = 0. Default: 0'
    )
    tc1: Optional[float] = Field(
        None, description='Lead time constant (Tc1).  Typical Value = 0. Default: 0'
    )
    tc2: Optional[float] = Field(
        None, description='Lead time constant (Tc2).  Typical Value = 0. Default: 0'
    )
    te: Optional[float] = Field(
        None,
        description='Exciter field time constant (Te).  Typical Value = 1.2. Default: 0',
    )
    tf: Optional[float] = Field(
        None,
        description='Rate feedback time constant (Tf).  Typical Value = 1. Default: 0',
    )
    tf1: Optional[float] = Field(
        None,
        description='Feedback lead time constant (Tf1).  Typical Value = 0. Default: 0',
    )
    tf2: Optional[float] = Field(
        None,
        description='Feedback lag time constant (Tf2).  Typical Value = 0. Default: 0',
    )
    tp: Optional[float] = Field(
        None,
        description='Field current Bridge time constant (Tp).  Typical Value = 0. Default: 0',
    )
    type: Optional[Type6] = Field(None, description='NGSI type. It has to be ExcREXS')
    vcmax: Optional[float] = Field(
        None,
        description='Maximum compounding voltage (Vcmax).  Typical Value = 0. Default: 0.0',
    )
    vfmax: Optional[float] = Field(
        None,
        description='Maximum Exciter Field Current (Vfmax).  Typical Value = 47. Default: 0.0',
    )
    vfmin: Optional[float] = Field(
        None,
        description='Minimum Exciter Field Current (Vfmin).  Typical Value = -20. Default: 0.0',
    )
    vimax: Optional[float] = Field(
        None,
        description='Voltage Regulator Input Limit (Vimax).  Typical Value = 0.1. Default: 0.0',
    )
    vrmax: Optional[float] = Field(
        None,
        description='Maximum controller output (Vrmax).  Typical Value = 47. Default: 0.0',
    )
    vrmin: Optional[float] = Field(
        None,
        description='Minimum controller output (Vrmin).  Typical Value = -20. Default: 0.0',
    )
    xc: Optional[float] = Field(
        None,
        description='Exciter compounding reactance (Xc).  Typical Value = 0. Default: 0.0',
    )
