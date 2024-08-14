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
    ExcST6B = 'ExcST6B'


class ExcST6B(BaseModel):
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
    ilr: Optional[float] = Field(
        None,
        description='Exciter output current limit reference (Ilr).  Typical Value = 4.164. Default: 0.0',
    )
    k1: Optional[float] = Field(
        None,
        description='Selector (K1). true = feedback is from Ifd false = feedback is not from Ifd. Typical Value = true. Default: False',
    )
    kcl: Optional[float] = Field(
        None,
        description='Exciter output current limit adjustment (Kcl).  Typical Value = 1.0577. Default: 0.0',
    )
    kff: Optional[float] = Field(
        None,
        description='Pre-control gain constant of the inner loop field regulator (Kff).  Typical Value = 1. Default: 0.0',
    )
    kg: Optional[float] = Field(
        None,
        description='Feedback gain constant of the inner loop field regulator (Kg).  Typical Value = 1. Default: 0.0',
    )
    kia: Optional[float] = Field(
        None,
        description='Voltage regulator integral gain (Kia).  Typical Value = 45.094. Default: 0.0',
    )
    klr: Optional[float] = Field(
        None,
        description='Exciter output current limit adjustment (Kcl).  Typical Value = 17.33. Default: 0.0',
    )
    km: Optional[float] = Field(
        None,
        description='Forward gain constant of the inner loop field regulator (Km).  Typical Value = 1. Default: 0.0',
    )
    kpa: Optional[float] = Field(
        None,
        description='Voltage regulator proportional gain (Kpa).  Typical Value = 18.038. Default: 0.0',
    )
    kvd: Optional[float] = Field(
        None,
        description='Voltage regulator derivative gain (Kvd).  Typical Value = 0. Default: 0.0',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    oelin: Optional[float] = Field(
        None,
        description='OEL input selector (OELin). Typical Value = noOELinput. Default: None',
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
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    tg: Optional[float] = Field(
        None,
        description='Feedback time constant of inner loop field voltage regulator (Tg).  Typical Value = 0.02. Default: 0',
    )
    ts: Optional[float] = Field(
        None,
        description='Rectifier firing time constant (Ts).  Typical Value = 0. Default: 0',
    )
    tvd: Optional[float] = Field(
        None,
        description='Voltage regulator derivative gain (Tvd).  Typical Value = 0. Default: 0',
    )
    type: Optional[Type6] = Field(None, description='NGSI type. It has to be ExcST6B')
    vamax: Optional[float] = Field(
        None,
        description='Maximum voltage regulator output (Vamax).  Typical Value = 4.81. Default: 0.0',
    )
    vamin: Optional[float] = Field(
        None,
        description='Minimum voltage regulator output (Vamin).  Typical Value = -3.85. Default: 0.0',
    )
    vilim: Optional[float] = Field(
        None,
        description='Selector (Vilim). true = Vimin-Vimax limiter is active false = Vimin-Vimax limiter is not active. Typical Value = true. Default: False',
    )
    vimax: Optional[float] = Field(
        None,
        description='Maximum voltage regulator input limit (Vimax).  Typical Value = 10. Default: 0.0',
    )
    vimin: Optional[float] = Field(
        None,
        description='Minimum voltage regulator input limit (Vimin).  Typical Value = -10. Default: 0.0',
    )
    vmult: Optional[float] = Field(
        None,
        description='Selector (Vmult). true = multiply regulator output by terminal voltage false = do not multiply regulator output by terminal voltage.  Typical Value = true. Default: False',
    )
    vrmax: Optional[float] = Field(
        None,
        description='Maximum voltage regulator output (Vrmax).  Typical Value = 4.81. Default: 0.0',
    )
    vrmin: Optional[float] = Field(
        None,
        description='Minimum voltage regulator output (Vrmin).  Typical Value = -3.85. Default: 0.0',
    )
    xc: Optional[float] = Field(
        None,
        description='Excitation source reactance (Xc).  Typical Value = 0.05. Default: 0.0',
    )
