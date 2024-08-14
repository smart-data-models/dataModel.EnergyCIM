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
    PssPTIST3 = 'PssPTIST3'


class PssPTIST3(BaseModel):
    a0: Optional[float] = Field(
        None, description='Filter coefficient (A0). Default: 0.0'
    )
    a1: Optional[float] = Field(None, description='Limiter (Al). Default: 0.0')
    a2: Optional[float] = Field(
        None, description='Filter coefficient (A2). Default: 0.0'
    )
    a3: Optional[float] = Field(
        None, description='Filter coefficient (A3). Default: 0.0'
    )
    a4: Optional[float] = Field(
        None, description='Filter coefficient (A4). Default: 0.0'
    )
    a5: Optional[float] = Field(
        None, description='Filter coefficient (A5). Default: 0.0'
    )
    address: Optional[Address] = Field(None, description='The mailing address')
    al: Optional[float] = Field(None, description='Limiter (Al). Default: 0.0')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    athres: Optional[float] = Field(
        None,
        description='Threshold value above which output averaging will be bypassed (Athres).  Typical Value = 0.005. Default: 0.0',
    )
    b0: Optional[float] = Field(
        None, description='Filter coefficient (B0). Default: 0.0'
    )
    b1: Optional[float] = Field(
        None, description='Filter coefficient (B1). Default: 0.0'
    )
    b2: Optional[float] = Field(
        None, description='Filter coefficient (B2). Default: 0.0'
    )
    b3: Optional[float] = Field(
        None, description='Filter coefficient (B3). Default: 0.0'
    )
    b4: Optional[float] = Field(
        None, description='Filter coefficient (B4). Default: 0.0'
    )
    b5: Optional[float] = Field(
        None, description='Filter coefficient (B5). Default: 0.0'
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
    dl: Optional[float] = Field(None, description='Limiter (Dl). Default: 0.0')
    dtc: Optional[float] = Field(
        None,
        description='Time step related to activation of controls (0.03 for 50 Hz) (Dtc).  Typical Value = 0.025. Default: 0',
    )
    dtf: Optional[float] = Field(
        None,
        description='Time step frequency calculation (0.03 for 50 Hz) (Dtf).  Typical Value = 0.025. Default: 0',
    )
    dtp: Optional[float] = Field(
        None,
        description='Time step active power calculation (0.015 for 50 Hz) (Dtp).  Typical Value = 0.0125. Default: 0',
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
    isw: Optional[float] = Field(
        None,
        description='Digital/analog output switch (Isw). true = produce analog output false = convert to digital output, using tap selection table. Default: False',
    )
    k: Optional[float] = Field(
        None, description='Gain (K).  Typical Value = 9. Default: 0.0'
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    lthres: Optional[float] = Field(
        None, description='Threshold value (Lthres). Default: 0.0'
    )
    m: Optional[float] = Field(
        None, description='(M).  M=2*H.  Typical Value = 5. Default: 0.0'
    )
    name: Optional[str] = Field(None, description='The name of this item')
    nav: Optional[float] = Field(
        None,
        description='Number of control outputs to average (Nav) (1 <= Nav <= 16).  Typical Value = 4. Default: 0.0',
    )
    ncl: Optional[float] = Field(
        None,
        description='Number of counts at limit to active limit function (Ncl) (>0). Default: 0.0',
    )
    ncr: Optional[float] = Field(
        None,
        description='Number of counts until reset after limit function is triggered (Ncr). Default: 0.0',
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
    pmin: Optional[float] = Field(None, description='(Pmin). Default: 0.0')
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    t1: Optional[float] = Field(
        None, description='Time constant (T1).  Typical Value = 0.3. Default: 0'
    )
    t2: Optional[float] = Field(
        None, description='Time constant (T2).  Typical Value = 1. Default: 0'
    )
    t3: Optional[float] = Field(
        None, description='Time constant (T3).  Typical Value = 0.2. Default: 0'
    )
    t4: Optional[float] = Field(
        None, description='Time constant (T4).  Typical Value = 0.05. Default: 0'
    )
    t5: Optional[float] = Field(None, description='Time constant (T5). Default: 0')
    t6: Optional[float] = Field(None, description='Time constant (T6). Default: 0')
    tf: Optional[float] = Field(
        None, description='Time constant (Tf).  Typical Value = 0.2. Default: 0'
    )
    tp: Optional[float] = Field(
        None, description='Time constant (Tp).  Typical Value = 0.2. Default: 0'
    )
    type: Optional[Type6] = Field(None, description='NGSI type. It has to be PssPTIST3')
