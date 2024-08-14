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
    GovGASTWD = 'GovGASTWD'


class GovGASTWD(BaseModel):
    a: Optional[float] = Field(None, description='Valve positioner (). Default: 0.0')
    address: Optional[Address] = Field(None, description='The mailing address')
    af1: Optional[float] = Field(
        None, description='Exhaust temperature Parameter (Af1). Default: 0.0'
    )
    af2: Optional[float] = Field(
        None, description='Coefficient equal to 0.5(1-speed) (Af2). Default: 0.0'
    )
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    b: Optional[float] = Field(None, description='Valve positioner (). Default: 0.0')
    bf1: Optional[float] = Field(
        None,
        description='(Bf1).  Bf1 = E(1-w) where E (speed sensitivity coefficient) is 0.55 to 0.65 x Tr. Default: 0.0',
    )
    bf2: Optional[float] = Field(
        None,
        description='Turbine Torque Coefficient K (depends on heating value of fuel stream in combustion chamber) (Bf2). Default: 0.0',
    )
    c: Optional[float] = Field(None, description='Valve positioner (). Default: 0.0')
    cf2: Optional[float] = Field(
        None,
        description='Coefficient defining fuel flow where power output is 0% (Cf2).  Synchronous but no output.  Typically 0.23 x K(23% fuel flow). Default: 0.0',
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
    ecr: Optional[float] = Field(
        None, description='Combustion reaction time delay (Ecr). Default: 0'
    )
    etd: Optional[float] = Field(
        None, description='Turbine and exhaust delay (Etd). Default: 0'
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
    k3: Optional[float] = Field(
        None, description='Ratio of Fuel Adjustment (K3). Default: 0.0'
    )
    k4: Optional[float] = Field(
        None, description='Gain of radiation shield (K4). Default: 0.0'
    )
    k5: Optional[float] = Field(
        None, description='Gain of radiation shield (K5). Default: 0.0'
    )
    k6: Optional[float] = Field(
        None, description='Minimum fuel flow (K6). Default: 0.0'
    )
    kd: Optional[float] = Field(
        None, description='Drop Governor Gain (Kd). Default: 0.0'
    )
    kdroop: Optional[float] = Field(None, description='(Kdroop). Default: 0.0')
    kf: Optional[float] = Field(
        None, description='Fuel system feedback (Kf). Default: 0.0'
    )
    ki: Optional[float] = Field(
        None, description='Isochronous Governor Gain (Ki). Default: 0.0'
    )
    kp: Optional[float] = Field(
        None, description='PID Proportional gain (Kp). Default: 0.0'
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    mwbase: Optional[float] = Field(
        None,
        description='Base for power values (MWbase) (> 0).  Unit = MW. Default: 0.0',
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
    t: Optional[float] = Field(
        None, description='Fuel Control Time Constant (T). Default: 0'
    )
    t3: Optional[float] = Field(
        None, description='Radiation shield time constant (T3). Default: 0'
    )
    t4: Optional[float] = Field(
        None, description='Thermocouple time constant (T4). Default: 0'
    )
    t5: Optional[float] = Field(
        None, description='Temperature control time constant (T5). Default: 0'
    )
    tc: Optional[float] = Field(
        None, description='Temperature control (Tc). Default: 0.0'
    )
    tcd: Optional[float] = Field(
        None, description='Compressor discharge time constant (Tcd). Default: 0'
    )
    td: Optional[float] = Field(
        None, description='Power transducer time constant (Td). Default: 0'
    )
    tf: Optional[float] = Field(
        None, description='Fuel system time constant (Tf). Default: 0'
    )
    tmax: Optional[float] = Field(
        None, description='Maximum Turbine limit (Tmax). Default: 0.0'
    )
    tmin: Optional[float] = Field(
        None, description='Minimum Turbine limit (Tmin). Default: 0.0'
    )
    tr: Optional[float] = Field(
        None, description='Rated temperature (Tr). Default: 0.0'
    )
    trate: Optional[float] = Field(
        None, description='Turbine rating (Trate).  Unit = MW. Default: 0.0'
    )
    tt: Optional[float] = Field(
        None, description='Temperature controller integration rate (Tt). Default: 0'
    )
    type: Optional[Type6] = Field(None, description='NGSI type. It has to be GovGASTWD')
