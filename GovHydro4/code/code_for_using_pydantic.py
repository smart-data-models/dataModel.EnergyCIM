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
    GovHydro4 = 'GovHydro4'


class GovHydro4(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    at: Optional[float] = Field(
        None, description='Turbine gain (At).  Typical Value = 1.2. Default: 0.0'
    )
    bgv0: Optional[float] = Field(
        None,
        description='Kaplan blade servo point 0 (Bgv0).  Typical Value = 0. Default: 0.0',
    )
    bgv1: Optional[float] = Field(
        None,
        description='Kaplan blade servo point 1 (Bgv1).  Typical Value = 0. Default: 0.0',
    )
    bgv2: Optional[float] = Field(
        None,
        description='Kaplan blade servo point 2 (Bgv2). Typical Value = 0.  Typical Value Francis = 0, Kaplan = 0.1. Default: 0.0',
    )
    bgv3: Optional[float] = Field(
        None,
        description='Kaplan blade servo point 3 (Bgv3). Typical Value = 0.  Typical Value Francis = 0, Kaplan = 0.667. Default: 0.0',
    )
    bgv4: Optional[float] = Field(
        None,
        description='Kaplan blade servo point 4 (Bgv4).  Typical Value = 0.  Typical Value Francis = 0, Kaplan = 0.9. Default: 0.0',
    )
    bgv5: Optional[float] = Field(
        None,
        description='Kaplan blade servo point 5 (Bgv5). Typical Value = 0.  Typical Value Francis = 0, Kaplan = 1. Default: 0.0',
    )
    bmax: Optional[float] = Field(
        None,
        description='Maximum blade adjustment factor (Bmax). Typical Value = 0.  Typical Value Francis = 0, Kaplan = 1.1276. Default: 0.0',
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
        description='Unintentional dead-band (db2).  Unit = MW.  Typical Value = 0. Default: 0.0',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    dturb: Optional[float] = Field(
        None,
        description='Turbine damping factor (Dturb).  Unit = delta P (PU of MWbase) / delta speed (PU). Typical Value = 0.5.  Typical Value Francis = 1.1, Kaplan = 1.1. Default: 0.0',
    )
    eps: Optional[float] = Field(
        None,
        description='Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0. Default: 0.0',
    )
    gmax: Optional[float] = Field(
        None,
        description='Maximum gate opening, PU of MWbase (Gmax).  Typical Value = 1. Default: 0.0',
    )
    gmin: Optional[float] = Field(
        None,
        description='Minimum gate opening, PU of MWbase (Gmin).  Typical Value = 0. Default: 0.0',
    )
    gv0: Optional[float] = Field(
        None,
        description='Nonlinear gain point 0, PU gv (Gv0). Typical Value = 0.  Typical Value Francis = 0.1, Kaplan = 0.1. Default: 0.0',
    )
    gv1: Optional[float] = Field(
        None,
        description='Nonlinear gain point 1, PU gv (Gv1). Typical Value = 0.  Typical Value Francis = 0.4, Kaplan = 0.4. Default: 0.0',
    )
    gv2: Optional[float] = Field(
        None,
        description='Nonlinear gain point 2, PU gv (Gv2). Typical Value = 0.  Typical Value Francis = 0.5, Kaplan = 0.5. Default: 0.0',
    )
    gv3: Optional[float] = Field(
        None,
        description='Nonlinear gain point 3, PU gv (Gv3). Typical Value = 0.  Typical Value Francis = 0.7, Kaplan = 0.7. Default: 0.0',
    )
    gv4: Optional[float] = Field(
        None,
        description='Nonlinear gain point 4, PU gv (Gv4). Typical Value = 0.  Typical Value Francis = 0.8, Kaplan = 0.8. Default: 0.0',
    )
    gv5: Optional[float] = Field(
        None,
        description='Nonlinear gain point 5, PU gv (Gv5). Typical Value = 0.  Typical Value Francis = 0.9, Kaplan = 0.9. Default: 0.0',
    )
    hdam: Optional[float] = Field(
        None,
        description='Head available at dam (hdam).  Typical Value = 1. Default: 0.0',
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
    pgv0: Optional[float] = Field(
        None,
        description='Nonlinear gain point 0, PU power (Pgv0).  Typical Value = 0. Default: 0.0',
    )
    pgv1: Optional[float] = Field(
        None,
        description='Nonlinear gain point 1, PU power (Pgv1). Typical Value = 0.  Typical Value Francis = 0.42, Kaplan = 0.35. Default: 0.0',
    )
    pgv2: Optional[float] = Field(
        None,
        description='Nonlinear gain point 2, PU power (Pgv2). Typical Value = 0.  Typical Value Francis = 0.56, Kaplan = 0.468. Default: 0.0',
    )
    pgv3: Optional[float] = Field(
        None,
        description='Nonlinear gain point 3, PU power (Pgv3). Typical Value = 0.  Typical Value Francis = 0.8, Kaplan = 0.796. Default: 0.0',
    )
    pgv4: Optional[float] = Field(
        None,
        description='Nonlinear gain point 4, PU power (Pgv4). Typical Value = 0.  Typical Value Francis = 0.9, Kaplan = 0.917. Default: 0.0',
    )
    pgv5: Optional[float] = Field(
        None,
        description='Nonlinear gain point 5, PU power (Pgv5).  Typical Value = 0.  Typical Value Francis = 0.97, Kaplan = 0.99. Default: 0.0',
    )
    qn1: Optional[float] = Field(
        None,
        description='No-load flow at nominal head (Qnl). Typical Value = 0.08.  Typical Value Francis = 0, Kaplan = 0. Default: 0.0',
    )
    rperm: Optional[float] = Field(
        None, description='Permanent droop (Rperm).  Typical Value = 0.05. Default: 0'
    )
    rtemp: Optional[float] = Field(
        None, description='Temporary droop (Rtemp).  Typical Value = 0.3. Default: 0'
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    tblade: Optional[float] = Field(
        None,
        description='Blade servo time constant (Tblade).  Typical Value = 100. Default: 0',
    )
    tg: Optional[float] = Field(
        None,
        description='Gate servo time constant (Tg) (>0).  Typical Value = 0.5. Default: 0',
    )
    tp: Optional[float] = Field(
        None,
        description='Pilot servo time constant (Tp).  Typical Value = 0.1. Default: 0',
    )
    tr: Optional[float] = Field(
        None,
        description='Dashpot time constant (Tr) (>0).  Typical Value = 5. Default: 0',
    )
    tw: Optional[float] = Field(
        None,
        description='Water inertia time constant (Tw) (>0).  Typical Value = 1. Default: 0',
    )
    type: Optional[Type6] = Field(None, description='NGSI type. It has to be GovHydro4')
    uc: Optional[float] = Field(
        None,
        description='Max gate closing velocity (Uc).  Typical Value = 0.2. Default: 0.0',
    )
    uo: Optional[float] = Field(
        None,
        description='Max gate opening velocity (Uo).  Typical Vlaue = 0.2. Default: 0.0',
    )
