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
    GovSteam1 = 'GovSteam1'


class GovSteam1(BaseModel):
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
    db1: Optional[float] = Field(
        None,
        description='Intentional deadband width (db1).  Unit = Hz.  Typical Value = 0. Default: 0.0',
    )
    db2: Optional[float] = Field(
        None,
        description='Unintentional deadband (db2).  Unit = MW.  Typical Value = 0. Default: 0.0',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    eps: Optional[float] = Field(
        None,
        description='Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0. Default: 0.0',
    )
    gv1: Optional[float] = Field(
        None,
        description='Nonlinear gain valve position point 1 (GV1).  Typical Value = 0. Default: 0.0',
    )
    gv2: Optional[float] = Field(
        None,
        description='Nonlinear gain valve position point 2 (GV2).  Typical Value = 0.4. Default: 0.0',
    )
    gv3: Optional[float] = Field(
        None,
        description='Nonlinear gain valve position point 3 (GV3).  Typical Value = 0.5. Default: 0.0',
    )
    gv4: Optional[float] = Field(
        None,
        description='Nonlinear gain valve position point 4 (GV4).  Typical Value = 0.6. Default: 0.0',
    )
    gv5: Optional[float] = Field(
        None,
        description='Nonlinear gain valve position point 5 (GV5).  Typical Value = 1. Default: 0.0',
    )
    gv6: Optional[float] = Field(
        None,
        description='Nonlinear gain valve position point 6 (GV6).  Typical Value = 0. Default: 0.0',
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
    k: Optional[float] = Field(
        None,
        description='Governor gain (reciprocal of droop) (K) (>0).  Typical Value = 25. Default: 0.0',
    )
    k1: Optional[float] = Field(
        None,
        description='Fraction of HP shaft power after first boiler pass (K1).  Typical Value = 0.2. Default: 0.0',
    )
    k2: Optional[float] = Field(
        None,
        description='Fraction of LP shaft power after first boiler pass (K2).  Typical Value = 0. Default: 0.0',
    )
    k3: Optional[float] = Field(
        None,
        description='Fraction of HP shaft power after second boiler pass (K3).  Typical Value = 0.3. Default: 0.0',
    )
    k4: Optional[float] = Field(
        None,
        description='Fraction of LP shaft power after second boiler pass (K4).  Typical Value = 0. Default: 0.0',
    )
    k5: Optional[float] = Field(
        None,
        description='Fraction of HP shaft power after third boiler pass (K5).  Typical Value = 0.5. Default: 0.0',
    )
    k6: Optional[float] = Field(
        None,
        description='Fraction of LP shaft power after third boiler pass (K6).  Typical Value = 0. Default: 0.0',
    )
    k7: Optional[float] = Field(
        None,
        description='Fraction of HP shaft power after fourth boiler pass (K7).  Typical Value = 0. Default: 0.0',
    )
    k8: Optional[float] = Field(
        None,
        description='Fraction of LP shaft power after fourth boiler pass (K8).  Typical Value = 0. Default: 0.0',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    mwbase: Optional[float] = Field(
        None,
        description='Base for power values (MWbase) (>0).  Unit = MW. Default: 0.0',
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
        description='Nonlinear gain power value point 1 (Pgv1).  Typical Value = 0. Default: 0.0',
    )
    pgv2: Optional[float] = Field(
        None,
        description='Nonlinear gain power value point 2 (Pgv2).  Typical Value = 0.75. Default: 0.0',
    )
    pgv3: Optional[float] = Field(
        None,
        description='Nonlinear gain power value point 3 (Pgv3).  Typical Value = 0.91. Default: 0.0',
    )
    pgv4: Optional[float] = Field(
        None,
        description='Nonlinear gain power value point 4 (Pgv4).  Typical Value = 0.98. Default: 0.0',
    )
    pgv5: Optional[float] = Field(
        None,
        description='Nonlinear gain power value point 5 (Pgv5).  Typical Value = 1. Default: 0.0',
    )
    pgv6: Optional[float] = Field(
        None,
        description='Nonlinear gain power value point 6 (Pgv6).  Typical Value = 0. Default: 0.0',
    )
    pmax: Optional[float] = Field(
        None,
        description='Maximum valve opening (Pmax) (> Pmin).  Typical Value = 1. Default: 0.0',
    )
    pmin: Optional[float] = Field(
        None,
        description='Minimum valve opening (Pmin) (>=0).  Typical Value = 0. Default: 0.0',
    )
    sdb1: Optional[float] = Field(
        None,
        description='Intentional deadband indicator. true = intentional deadband is applied false = intentional deadband is not applied. Typical Value = true. Default: False',
    )
    sdb2: Optional[float] = Field(
        None,
        description='Unintentional deadband location. true = intentional deadband is applied before point `A` false = intentional deadband is applied after point `A`. Typical Value = true. Default: False',
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
        description='Governor lag time constant (T1).  Typical Value = 0. Default: 0',
    )
    t2: Optional[float] = Field(
        None,
        description='Governor lead time constant (T2).  Typical Value = 0. Default: 0',
    )
    t3: Optional[float] = Field(
        None,
        description='Valve positioner time constant (T3(>0).  Typical Value = 0.1. Default: 0',
    )
    t4: Optional[float] = Field(
        None,
        description='Inlet piping/steam bowl time constant (T4).  Typical Value = 0.3. Default: 0',
    )
    t5: Optional[float] = Field(
        None,
        description='Time constant of second boiler pass (T5).  Typical Value = 5. Default: 0',
    )
    t6: Optional[float] = Field(
        None,
        description='Time constant of third boiler pass (T6).  Typical Value = 0.5. Default: 0',
    )
    t7: Optional[float] = Field(
        None,
        description='Time constant of fourth boiler pass (T7).  Typical Value = 0. Default: 0',
    )
    type: Optional[Type6] = Field(None, description='NGSI type. It has to be GovSteam1')
    uc: Optional[float] = Field(
        None,
        description='Maximum valve closing velocity (Uc) (<0).  Unit = PU/sec.  Typical Value = -10. Default: 0.0',
    )
    uo: Optional[float] = Field(
        None,
        description='Maximum valve opening velocity (Uo) (>0).  Unit = PU/sec.  Typical Value = 1. Default: 0.0',
    )
    valve: Optional[float] = Field(
        None,
        description='Nonlinear valve characteristic. true = nonlinear valve characteristic is used false = nonlinear valve characteristic is not used. Typical Value = true. Default: False',
    )
