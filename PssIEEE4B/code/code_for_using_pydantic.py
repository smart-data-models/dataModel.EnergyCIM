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
    PssIEEE4B = 'PssIEEE4B'


class PssIEEE4B(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    bwh1: Optional[float] = Field(
        None,
        description='Notch filter 1 (high-frequency band): Three dB bandwidth (B). Default: 0.0',
    )
    bwh2: Optional[float] = Field(
        None,
        description='Notch filter 2 (high-frequency band): Three dB bandwidth (B). Default: 0.0',
    )
    bwl1: Optional[float] = Field(
        None,
        description='Notch filter 1 (low-frequency band): Three dB bandwidth (B). Default: 0.0',
    )
    bwl2: Optional[float] = Field(
        None,
        description='Notch filter 2 (low-frequency band): Three dB bandwidth (B). Default: 0.0',
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
    kh: Optional[float] = Field(
        None, description='High band gain (K).  Typical Value = 120. Default: 0.0'
    )
    kh1: Optional[float] = Field(
        None,
        description='High band differential filter gain (K).  Typical Value = 66. Default: 0.0',
    )
    kh11: Optional[float] = Field(
        None,
        description='High band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0',
    )
    kh17: Optional[float] = Field(
        None,
        description='High band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0',
    )
    kh2: Optional[float] = Field(
        None,
        description='High band differential filter gain (K).  Typical Value = 66. Default: 0.0',
    )
    ki: Optional[float] = Field(
        None,
        description='Intermediate band gain (K).  Typical Value = 30. Default: 0.0',
    )
    ki1: Optional[float] = Field(
        None,
        description='Intermediate band differential filter gain (K).  Typical Value = 66. Default: 0.0',
    )
    ki11: Optional[float] = Field(
        None,
        description='Intermediate band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0',
    )
    ki17: Optional[float] = Field(
        None,
        description='Intermediate band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0',
    )
    ki2: Optional[float] = Field(
        None,
        description='Intermediate band differential filter gain (K).  Typical Value = 66. Default: 0.0',
    )
    kl: Optional[float] = Field(
        None, description='Low band gain (K).  Typical Value = 7.5. Default: 0.0'
    )
    kl1: Optional[float] = Field(
        None,
        description='Low band differential filter gain (K).  Typical Value = 66. Default: 0.0',
    )
    kl11: Optional[float] = Field(
        None,
        description='Low band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0',
    )
    kl17: Optional[float] = Field(
        None,
        description='Low band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0',
    )
    kl2: Optional[float] = Field(
        None,
        description='Low band differential filter gain (K).  Typical Value = 66. Default: 0.0',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    omeganh1: Optional[float] = Field(
        None,
        description='Notch filter 1 (high-frequency band): filter frequency (omega). Default: 0.0',
    )
    omeganh2: Optional[float] = Field(
        None,
        description='Notch filter 2 (high-frequency band): filter frequency (omega). Default: 0.0',
    )
    omeganl1: Optional[float] = Field(
        None,
        description='Notch filter 1 (low-frequency band): filter frequency (omega). Default: 0.0',
    )
    omeganl2: Optional[float] = Field(
        None,
        description='Notch filter 2 (low-frequency band): filter frequency (omega). Default: 0.0',
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
    th1: Optional[float] = Field(
        None,
        description='High band time constant (T).  Typical Value = 0.01513. Default: 0',
    )
    th10: Optional[float] = Field(
        None, description='High band time constant (T).  Typical Value = 0. Default: 0'
    )
    th11: Optional[float] = Field(
        None, description='High band time constant (T).  Typical Value = 0. Default: 0'
    )
    th12: Optional[float] = Field(
        None, description='High band time constant (T).  Typical Value = 0. Default: 0'
    )
    th2: Optional[float] = Field(
        None,
        description='High band time constant (T).  Typical Value = 0.01816. Default: 0',
    )
    th3: Optional[float] = Field(
        None, description='High band time constant (T).  Typical Value = 0. Default: 0'
    )
    th4: Optional[float] = Field(
        None, description='High band time constant (T).  Typical Value = 0. Default: 0'
    )
    th5: Optional[float] = Field(
        None, description='High band time constant (T).  Typical Value = 0. Default: 0'
    )
    th6: Optional[float] = Field(
        None, description='High band time constant (T).  Typical Value = 0. Default: 0'
    )
    th7: Optional[float] = Field(
        None,
        description='High band time constant (T).  Typical Value = 0.01816. Default: 0',
    )
    th8: Optional[float] = Field(
        None,
        description='High band time constant (T).  Typical Value = 0.02179. Default: 0',
    )
    th9: Optional[float] = Field(
        None, description='High band time constant (T).  Typical Value = 0. Default: 0'
    )
    ti1: Optional[float] = Field(
        None,
        description='Intermediate band time constant (T).  Typical Value = 0.173. Default: 0',
    )
    ti10: Optional[float] = Field(
        None,
        description='Intermediate band time constant (T).  Typical Value = 0. Default: 0',
    )
    ti11: Optional[float] = Field(
        None,
        description='Intermediate band time constant (T).  Typical Value = 0. Default: 0',
    )
    ti12: Optional[float] = Field(
        None,
        description='Intermediate band time constant (T).  Typical Value = 0. Default: 0',
    )
    ti2: Optional[float] = Field(
        None,
        description='Intermediate band time constant (T).  Typical Value = 0.2075. Default: 0',
    )
    ti3: Optional[float] = Field(
        None,
        description='Intermediate band time constant (T).  Typical Value = 0. Default: 0',
    )
    ti4: Optional[float] = Field(
        None,
        description='Intermediate band time constant (T).  Typical Value = 0. Default: 0',
    )
    ti5: Optional[float] = Field(
        None,
        description='Intermediate band time constant (T).  Typical Value = 0. Default: 0',
    )
    ti6: Optional[float] = Field(
        None,
        description='Intermediate band time constant (T).  Typical Value = 0. Default: 0',
    )
    ti7: Optional[float] = Field(
        None,
        description='Intermediate band time constant (T).  Typical Value = 0.2075. Default: 0',
    )
    ti8: Optional[float] = Field(
        None,
        description='Intermediate band time constant (T).  Typical Value = 0.2491. Default: 0',
    )
    ti9: Optional[float] = Field(
        None,
        description='Intermediate band time constant (T).  Typical Value = 0. Default: 0',
    )
    tl1: Optional[float] = Field(
        None,
        description='Low band time constant (T).  Typical Value = 1.73. Default: 0',
    )
    tl10: Optional[float] = Field(
        None, description='Low band time constant (T).  Typical Value = 0. Default: 0'
    )
    tl11: Optional[float] = Field(
        None, description='Low band time constant (T).  Typical Value = 0. Default: 0'
    )
    tl12: Optional[float] = Field(
        None, description='Low band time constant (T).  Typical Value = 0. Default: 0'
    )
    tl2: Optional[float] = Field(
        None,
        description='Low band time constant (T).  Typical Value = 2.075. Default: 0',
    )
    tl3: Optional[float] = Field(
        None, description='Low band time constant (T).  Typical Value = 0. Default: 0'
    )
    tl4: Optional[float] = Field(
        None, description='Low band time constant (T).  Typical Value = 0. Default: 0'
    )
    tl5: Optional[float] = Field(
        None, description='Low band time constant (T).  Typical Value = 0. Default: 0'
    )
    tl6: Optional[float] = Field(
        None, description='Low band time constant (T).  Typical Value = 0. Default: 0'
    )
    tl7: Optional[float] = Field(
        None,
        description='Low band time constant (T).  Typical Value = 2.075. Default: 0',
    )
    tl8: Optional[float] = Field(
        None,
        description='Low band time constant (T).  Typical Value = 2.491. Default: 0',
    )
    tl9: Optional[float] = Field(
        None, description='Low band time constant (T).  Typical Value = 0. Default: 0'
    )
    type: Optional[Type6] = Field(None, description='NGSI type. It has to be PssIEEE4B')
    vhmax: Optional[float] = Field(
        None,
        description='High band output maximum limit (V).  Typical Value = 0.6. Default: 0.0',
    )
    vhmin: Optional[float] = Field(
        None,
        description='High band output minimum limit (V).  Typical Value = -0.6. Default: 0.0',
    )
    vimax: Optional[float] = Field(
        None,
        description='Intermediate band output maximum limit (V).  Typical Value = 0.6. Default: 0.0',
    )
    vimin: Optional[float] = Field(
        None,
        description='Intermediate band output minimum limit (V).  Typical Value = -0.6. Default: 0.0',
    )
    vlmax: Optional[float] = Field(
        None,
        description='Low band output maximum limit (V).  Typical Value = 0.075. Default: 0.0',
    )
    vlmin: Optional[float] = Field(
        None,
        description='Low band output minimum limit (V).  Typical Value = -0.075. Default: 0.0',
    )
    vstmax: Optional[float] = Field(
        None,
        description='PSS output maximum limit (V).  Typical Value = 0.15. Default: 0.0',
    )
    vstmin: Optional[float] = Field(
        None,
        description='PSS output minimum limit (V).  Typical Value = -0.15. Default: 0.0',
    )
