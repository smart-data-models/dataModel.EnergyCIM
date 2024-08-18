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
    UnderexcLimIEEE2 = 'UnderexcLimIEEE2'


class UnderexcLimIEEE2(BaseModel):
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
    k1: Optional[float] = Field(
        None,
        description='UEL terminal voltage exponent applied to real power input to UEL limit look-up table (k1).  Typical Value = 2. Default: 0.0',
    )
    k2: Optional[float] = Field(
        None,
        description='UEL terminal voltage exponent applied to reactive power output from UEL limit look-up table (k2).  Typical Value = 2. Default: 0.0',
    )
    kfb: Optional[float] = Field(
        None,
        description='Gain associated with optional integrator feedback input signal to UEL (K).  Typical Value = 0. Default: 0.0',
    )
    kuf: Optional[float] = Field(
        None,
        description='UEL excitation system stabilizer gain (K).  Typical Value = 0. Default: 0.0',
    )
    kui: Optional[float] = Field(
        None, description='UEL integral gain (K).  Typical Value = 0.5. Default: 0.0'
    )
    kul: Optional[float] = Field(
        None,
        description='UEL proportional gain (K).  Typical Value = 0.8. Default: 0.0',
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
    p0: Optional[float] = Field(
        None,
        description='Real power values for endpoints (P).  Typical Value = 0. Default: 0.0',
    )
    p1: Optional[float] = Field(
        None,
        description='Real power values for endpoints (P).  Typical Value = 0.3. Default: 0.0',
    )
    p10: Optional[float] = Field(
        None, description='Real power values for endpoints (P). Default: 0.0'
    )
    p2: Optional[float] = Field(
        None,
        description='Real power values for endpoints (P).  Typical Value = 0.6. Default: 0.0',
    )
    p3: Optional[float] = Field(
        None,
        description='Real power values for endpoints (P).  Typical Value = 0.9. Default: 0.0',
    )
    p4: Optional[float] = Field(
        None,
        description='Real power values for endpoints (P).  Typical Value = 1.02. Default: 0.0',
    )
    p5: Optional[float] = Field(
        None, description='Real power values for endpoints (P). Default: 0.0'
    )
    p6: Optional[float] = Field(
        None, description='Real power values for endpoints (P). Default: 0.0'
    )
    p7: Optional[float] = Field(
        None, description='Real power values for endpoints (P). Default: 0.0'
    )
    p8: Optional[float] = Field(
        None, description='Real power values for endpoints (P). Default: 0.0'
    )
    p9: Optional[float] = Field(
        None, description='Real power values for endpoints (P). Default: 0.0'
    )
    q0: Optional[float] = Field(
        None,
        description='Reactive power values for endpoints (Q).  Typical Value = -0.31. Default: 0.0',
    )
    q1: Optional[float] = Field(
        None,
        description='Reactive power values for endpoints (Q).  Typical Value = -0.31. Default: 0.0',
    )
    q10: Optional[float] = Field(
        None, description='Reactive power values for endpoints (Q). Default: 0.0'
    )
    q2: Optional[float] = Field(
        None,
        description='Reactive power values for endpoints (Q).  Typical Value = -0.28. Default: 0.0',
    )
    q3: Optional[float] = Field(
        None,
        description='Reactive power values for endpoints (Q).  Typical Value = -0.21. Default: 0.0',
    )
    q4: Optional[float] = Field(
        None,
        description='Reactive power values for endpoints (Q).  Typical Value = 0. Default: 0.0',
    )
    q5: Optional[float] = Field(
        None, description='Reactive power values for endpoints (Q). Default: 0.0'
    )
    q6: Optional[float] = Field(
        None, description='Reactive power values for endpoints (Q). Default: 0.0'
    )
    q7: Optional[float] = Field(
        None, description='Reactive power values for endpoints (Q). Default: 0.0'
    )
    q8: Optional[float] = Field(
        None, description='Reactive power values for endpoints (Q). Default: 0.0'
    )
    q9: Optional[float] = Field(
        None, description='Reactive power values for endpoints (Q). Default: 0.0'
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    tu1: Optional[float] = Field(
        None, description='UEL lead time constant (T).  Typical Value = 0. Default: 0'
    )
    tu2: Optional[float] = Field(
        None, description='UEL lag time constant (T).  Typical Value = 0. Default: 0'
    )
    tu3: Optional[float] = Field(
        None, description='UEL lead time constant (T).  Typical Value = 0. Default: 0'
    )
    tu4: Optional[float] = Field(
        None, description='UEL lag time constant (T).  Typical Value = 0. Default: 0'
    )
    tul: Optional[float] = Field(
        None,
        description='Time constant associated with optional integrator feedback input signal to UEL (T).  Typical Value = 0. Default: 0',
    )
    tup: Optional[float] = Field(
        None,
        description='Real power filter time constant (T).  Typical Value = 5. Default: 0',
    )
    tuq: Optional[float] = Field(
        None,
        description='Reactive power filter time constant (T).  Typical Value = 0. Default: 0',
    )
    tuv: Optional[float] = Field(
        None,
        description='Voltage filter time constant (T).  Typical Value = 5. Default: 0',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI type. It has to be UnderexcLimIEEE2'
    )
    vuimax: Optional[float] = Field(
        None,
        description='UEL integrator output maximum limit (V).  Typical Value = 0.25. Default: 0.0',
    )
    vuimin: Optional[float] = Field(
        None,
        description='UEL integrator output minimum limit (V).  Typical Value = 0. Default: 0.0',
    )
    vulmax: Optional[float] = Field(
        None,
        description='UEL output maximum limit (V).  Typical Value = 0.25. Default: 0.0',
    )
    vulmin: Optional[float] = Field(
        None,
        description='UEL output minimum limit (V).  Typical Value = 0. Default: 0.0',
    )
