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
    GovGAST1 = 'GovGAST1'


class GovGAST1(BaseModel):
    a: Optional[float] = Field(
        None,
        description='Turbine power time constant numerator scale factor (a).  Typical Value = 0.8. Default: 0.0',
    )
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    b: Optional[float] = Field(
        None,
        description='Turbine power time constant denominator scale factor (b).  Typical Value = 1. Default: 0.0',
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
    db1: Optional[float] = Field(
        None,
        description='Intentional dead-band width (db1).  Unit = Hz.  Typical Value = 0. Default: 0.0',
    )
    db2: Optional[float] = Field(
        None,
        description='Unintentional dead-band (db2).  Unit = MW.  Typical Value = 0. Default: 0.0',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    eps: Optional[float] = Field(
        None,
        description='Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0. Default: 0.0',
    )
    fidle: Optional[float] = Field(
        None,
        description='Fuel flow at zero power output (Fidle).  Typical Value = 0.18. Default: 0.0',
    )
    gv1: Optional[float] = Field(
        None,
        description='Nonlinear gain point 1, PU gv (Gv1).  Typical Value = 0. Default: 0.0',
    )
    gv2: Optional[float] = Field(
        None,
        description='Nonlinear gain point 2,PU gv (Gv2).  Typical Value = 0. Default: 0.0',
    )
    gv3: Optional[float] = Field(
        None,
        description='Nonlinear gain point 3, PU gv (Gv3).  Typical Value = 0. Default: 0.0',
    )
    gv4: Optional[float] = Field(
        None,
        description='Nonlinear gain point 4, PU gv (Gv4).  Typical Value = 0. Default: 0.0',
    )
    gv5: Optional[float] = Field(
        None,
        description='Nonlinear gain point 5, PU gv (Gv5).  Typical Value = 0. Default: 0.0',
    )
    gv6: Optional[float] = Field(
        None,
        description='Nonlinear gain point 6, PU gv (Gv6).  Typical Value = 0. Default: 0.0',
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
    ka: Optional[float] = Field(
        None, description='Governor gain (Ka).  Typical Value = 0. Default: 0.0'
    )
    kt: Optional[float] = Field(
        None,
        description='Temperature limiter gain (Kt).  Typical Value = 3. Default: 0.0',
    )
    lmax: Optional[float] = Field(
        None,
        description='Ambient temperature load limit (Lmax).  Lmax is the turbine power output corresponding to the limiting exhaust gas temperature.  Typical Value = 1. Default: 0.0',
    )
    loadinc: Optional[float] = Field(
        None,
        description='Valve position change allowed at fast rate (Loadinc).  Typical Value = 0.05. Default: 0.0',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    ltrate: Optional[float] = Field(
        None,
        description='Maximum long term fuel valve opening rate (Ltrate).  Typical Value = 0.02. Default: 0.0',
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
    pgv1: Optional[float] = Field(
        None,
        description='Nonlinear gain point 1, PU power (Pgv1).  Typical Value = 0. Default: 0.0',
    )
    pgv2: Optional[float] = Field(
        None,
        description='Nonlinear gain point 2, PU power (Pgv2).  Typical Value = 0. Default: 0.0',
    )
    pgv3: Optional[float] = Field(
        None,
        description='Nonlinear gain point 3, PU power (Pgv3).  Typical Value = 0. Default: 0.0',
    )
    pgv4: Optional[float] = Field(
        None,
        description='Nonlinear gain point 4, PU power (Pgv4).  Typical Value = 0. Default: 0.0',
    )
    pgv5: Optional[float] = Field(
        None,
        description='Nonlinear gain point 5, PU power (Pgv5).  Typical Value = 0. Default: 0.0',
    )
    pgv6: Optional[float] = Field(
        None,
        description='Nonlinear gain point 6, PU power (Pgv6).  Typical Value = 0. Default: 0.0',
    )
    r: Optional[float] = Field(
        None, description='Permanent droop (R).  Typical Value = 0.04. Default: 0.0'
    )
    rmax: Optional[float] = Field(
        None,
        description='Maximum fuel valve opening rate (Rmax).  Unit = PU/sec.  Typical Value = 1. Default: 0.0',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    t1: Optional[float] = Field(
        None,
        description='Governor mechanism time constant (T1).  T1 represents the natural valve positioning time constant of the governor for small disturbances, as seen when rate limiting is not in effect.  Typical Value = 0.5. Default: 0',
    )
    t2: Optional[float] = Field(
        None,
        description='Turbine power time constant (T2).  T2 represents delay due to internal energy storage of the gas turbine engine. T2 can be used to give a rough approximation to the delay associated with acceleration of the compressor spool of a multi-shaft engine, or with the compressibility of gas in the plenum of the free power turbine of an aero-derivative unit, for example.  Typical Value = 0.5. Default: 0',
    )
    t3: Optional[float] = Field(
        None,
        description='Turbine exhaust temperature time constant (T3).  T3 represents delay in the exhaust temperature and load limiting system. Typical Value = 3. Default: 0',
    )
    t4: Optional[float] = Field(
        None,
        description='Governor lead time constant (T4).  Typical Value = 0. Default: 0',
    )
    t5: Optional[float] = Field(
        None,
        description='Governor lag time constant (T5).  Typical Value = 0. Default: 0',
    )
    tltr: Optional[float] = Field(
        None,
        description='Valve position averaging time constant (Tltr).  Typical Value = 10. Default: 0',
    )
    type: Optional[Type6] = Field(None, description='NGSI type. It has to be GovGAST1')
    vmax: Optional[float] = Field(
        None,
        description='Maximum turbine power, PU of MWbase (Vmax).  Typical Value = 1. Default: 0.0',
    )
    vmin: Optional[float] = Field(
        None,
        description='Minimum turbine power, PU of MWbase (Vmin).  Typical Value = 0. Default: 0.0',
    )
