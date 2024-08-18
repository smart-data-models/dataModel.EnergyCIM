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
    WindContQIEC = 'WindContQIEC'


class WindContQIEC(BaseModel):
    WindTurbineType3or4IEC: Optional[float] = Field(
        None,
        description='Wind turbine type 3 or 4 model with which this reactive control mode is associated. Default: None',
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
    iqh1: Optional[float] = Field(
        None,
        description='Maximum reactive current injection during dip (i). It is type dependent parameter. Default: 0.0',
    )
    iqmax: Optional[float] = Field(
        None,
        description='Maximum reactive current injection (i). It is type dependent parameter. Default: 0.0',
    )
    iqmin: Optional[float] = Field(
        None,
        description='Minimum reactive current injection (i). It is type dependent parameter. Default: 0.0',
    )
    iqpost: Optional[float] = Field(
        None,
        description='Post fault reactive current injection (). It is project dependent parameter. Default: 0.0',
    )
    kiq: Optional[float] = Field(
        None,
        description='Reactive power PI controller integration gain (). It is type dependent parameter. Default: 0.0',
    )
    kiu: Optional[float] = Field(
        None,
        description='Voltage PI controller integration gain (). It is type dependent parameter. Default: 0.0',
    )
    kpq: Optional[float] = Field(
        None,
        description='Reactive power PI controller proportional gain (). It is type dependent parameter. Default: 0.0',
    )
    kpu: Optional[float] = Field(
        None,
        description='Voltage PI controller proportional gain (). It is type dependent parameter. Default: 0.0',
    )
    kqv: Optional[float] = Field(
        None,
        description='Voltage scaling factor for LVRT current (). It is project dependent parameter. Default: 0.0',
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
    qmax: Optional[float] = Field(
        None,
        description='Maximum reactive power (q). It is type dependent parameter. Default: 0.0',
    )
    qmin: Optional[float] = Field(
        None,
        description='Minimum reactive power (q). It is type dependent parameter. Default: 0.0',
    )
    rdroop: Optional[float] = Field(
        None,
        description='Resistive component of voltage drop impedance (). It is project dependent parameter. Default: 0.0',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    tiq: Optional[float] = Field(
        None,
        description='Time constant in reactive current lag (T). It is type dependent parameter. Default: 0',
    )
    tpfilt: Optional[float] = Field(
        None,
        description='Power measurement filter time constant (). It is type dependent parameter. Default: 0',
    )
    tpost: Optional[float] = Field(
        None,
        description='Length of time period where post fault reactive power is injected (). It is project dependent parameter. Default: 0',
    )
    tqord: Optional[float] = Field(
        None,
        description='Time constant in reactive power order lag (). It is type dependent parameter. Default: 0',
    )
    tufilt: Optional[float] = Field(
        None,
        description='Voltage measurement filter time constant (). It is type dependent parameter. Default: 0',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI type. It has to be WindContQIEC'
    )
    udb1: Optional[float] = Field(
        None,
        description='Voltage dead band lower limit (). It is type dependent parameter. Default: 0.0',
    )
    udb2: Optional[float] = Field(
        None,
        description='Voltage dead band upper limit (). It is type dependent parameter. Default: 0.0',
    )
    umax: Optional[float] = Field(
        None,
        description='Maximum voltage in voltage PI controller integral term (u). It is type dependent parameter. Default: 0.0',
    )
    umin: Optional[float] = Field(
        None,
        description='Minimum voltage in voltage PI controller integral term (u). It is type dependent parameter. Default: 0.0',
    )
    uqdip: Optional[float] = Field(
        None,
        description='Voltage threshold for LVRT detection in q control (). It is type dependent parameter. Default: 0.0',
    )
    uref0: Optional[float] = Field(
        None,
        description='User defined bias in voltage reference (), used when  =. It is case dependent parameter. Default: 0.0',
    )
    windLVRTQcontrolModesType: Optional[float] = Field(
        None,
        description='Types of LVRT Q control modes (). It is project dependent parameter. Default: None',
    )
    windQcontrolModesType: Optional[float] = Field(
        None,
        description='Types of general wind turbine Q control modes ().  It is project dependent parameter. Default: None',
    )
    xdroop: Optional[float] = Field(
        None,
        description='Inductive component of voltage drop impedance (). It is project dependent parameter. Default: 0.0',
    )
