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
    ExcST3A = 'ExcST3A'


class ExcST3A(BaseModel):
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
    efdmax: Optional[float] = Field(
        None,
        description='Maximum AVR output (Efdmax).  Typical Value = 6.9. Default: 0.0',
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
        description='Rectifier loading factor proportional to commutating reactance (Kc). Typical Value = 1.1. Default: 0.0',
    )
    kg: Optional[float] = Field(
        None,
        description='Feedback gain constant of the inner loop field regulator (Kg).  Typical Value = 1. Default: 0.0',
    )
    ki: Optional[float] = Field(
        None,
        description='Potential circuit gain coefficient (Ki).  Typical Value = 4.83. Default: 0.0',
    )
    kj: Optional[float] = Field(
        None, description='AVR gain (Kj).  Typical Value = 200. Default: 0.0'
    )
    km: Optional[float] = Field(
        None,
        description='Forward gain constant of the inner loop field regulator (Km).  Typical Value = 7.04. Default: 0.0',
    )
    kp: Optional[float] = Field(
        None,
        description='Potential source gain (Kp) (>0).  Typical Value = 4.37. Default: 0.0',
    )
    ks: Optional[float] = Field(
        None,
        description='Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0. Default: 0.0',
    )
    ks1: Optional[float] = Field(
        None,
        description='Coefficient to allow different usage of the model-speed coefficient (Ks1).  Typical Value = 0. Default: 0.0',
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
    tb: Optional[float] = Field(
        None,
        description='Voltage regulator time constant (Tb).  Typical Value = 6.67. Default: 0',
    )
    tc: Optional[float] = Field(
        None,
        description='Voltage regulator time constant (Tc).  Typical Value = 1. Default: 0',
    )
    thetap: Optional[float] = Field(
        None,
        description='Potential circuit phase angle (thetap).  Typical Value = 20. Default: 0.0',
    )
    tm: Optional[float] = Field(
        None,
        description='Forward time constant of inner loop field regulator (Tm).  Typical Value = 1. Default: 0',
    )
    type: Optional[Type6] = Field(None, description='NGSI type. It has to be ExcST3A')
    vbmax: Optional[float] = Field(
        None,
        description='Maximum excitation voltage (Vbmax).  Typical Value = 8.63. Default: 0.0',
    )
    vgmax: Optional[float] = Field(
        None,
        description='Maximum inner loop feedback voltage (Vgmax).  Typical Value = 6.53. Default: 0.0',
    )
    vimax: Optional[float] = Field(
        None,
        description='Maximum voltage regulator input limit (Vimax).  Typical Value = 0.2. Default: 0.0',
    )
    vimin: Optional[float] = Field(
        None,
        description='Minimum voltage regulator input limit (Vimin).  Typical Value = -0.2. Default: 0.0',
    )
    vrmax: Optional[float] = Field(
        None,
        description='Maximum voltage regulator output (Vrmax).  Typical Value = 1. Default: 0.0',
    )
    vrmin: Optional[float] = Field(
        None,
        description='Minimum voltage regulator output (Vrmin).  Typical Value = 0. Default: 0.0',
    )
    xl: Optional[float] = Field(
        None,
        description='Reactance associated with potential source (Xl).  Typical Value = 0.09. Default: 0.0',
    )