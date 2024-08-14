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
    GovHydroPelton = 'GovHydroPelton'


class GovHydroPelton(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    av0: Optional[float] = Field(
        None,
        description='Area of the surge tank (A). Unit = m. Typical Value = 30. Default: 0.0',
    )
    av1: Optional[float] = Field(
        None,
        description='Area of the compensation tank (A). Unit = m. Typical Value = 700. Default: 0.0',
    )
    bp: Optional[float] = Field(
        None, description='Droop (bp).  Typical Value = 0.05. Default: 0.0'
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
        description='Intentional dead-band width (DB1).  Unit = Hz.  Typical Value = 0. Default: 0.0',
    )
    db2: Optional[float] = Field(
        None,
        description='Intentional dead-band width of valve opening error (DB2). Unit = Hz.  Typical Value = 0.01. Default: 0.0',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    h1: Optional[float] = Field(
        None,
        description='Head of compensation chamber water level with respect to the level of penstock (H).  Unit = m. Typical Value = 4. Default: 0.0',
    )
    h2: Optional[float] = Field(
        None,
        description='Head of surge tank water level with respect to the level of penstock (H).  Unit = m. Typical Value = 40. Default: 0.0',
    )
    hn: Optional[float] = Field(
        None,
        description='Rated hydraulic head (H).  Unit = m. Typical Value = 250. Default: 0.0',
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
        description='Penstock loss coefficient (due to friction) (Kc).  Typical Value = 0.025. Default: 0.0',
    )
    kg: Optional[float] = Field(
        None,
        description='Water tunnel and surge chamber loss coefficient (due to friction) (Kg).  Typical Value = -0.025. Default: 0.0',
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
    qc0: Optional[float] = Field(
        None,
        description='No-load turbine flow at nominal head (Qc0).  Typical Value = 0.05. Default: 0.0',
    )
    qn: Optional[float] = Field(
        None, description='Rated flow (Q). Unit = m/s. Typical Value = 40. Default: 0.0'
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    simplifiedPelton: Optional[float] = Field(
        None,
        description='Simplified Pelton model simulation (Sflag). true = enable of simplified Pelton model simulation false = enable of complete Pelton model simulation (non linear gain). Typical Value = false. Default: False',
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    staticCompensating: Optional[float] = Field(
        None,
        description='Static compensating characteristic (Cflag). true = enable of static compensating characteristic  false = inhibit of static compensating characteristic. Typical Value = false. Default: False',
    )
    ta: Optional[float] = Field(
        None,
        description='Derivative gain (accelerometer time constant) (Ta).  Typical Value = 3. Default: 0',
    )
    ts: Optional[float] = Field(
        None,
        description='Gate servo time constant (Ts).  Typical Value = 0.15. Default: 0',
    )
    tv: Optional[float] = Field(
        None,
        description='Servomotor integrator time constant (TV).  Typical Value = 0.3. Default: 0',
    )
    twnc: Optional[float] = Field(
        None,
        description='Water inertia time constant (Twnc).  Typical Value = 1. Default: 0',
    )
    twng: Optional[float] = Field(
        None,
        description='Water tunnel and surge chamber inertia time constant (Twng). Typical Value = 3. Default: 0',
    )
    tx: Optional[float] = Field(
        None,
        description='Electronic integrator time constant (Tx).  Typical Value = 0.5. Default: 0',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI type. It has to be GovHydroPelton'
    )
    va: Optional[float] = Field(
        None,
        description='Maximum gate opening velocity (Va).  Unit = PU/sec.  Typical Value = 0.016. Default: 0.0',
    )
    valvmax: Optional[float] = Field(
        None,
        description='Maximum gate opening (ValvMax).  Typical Value = 1. Default: 0.0',
    )
    valvmin: Optional[float] = Field(
        None,
        description='Minimum gate opening (ValvMin).  Typical Value = 0. Default: 0.0',
    )
    vav: Optional[float] = Field(
        None,
        description='Maximum servomotor valve opening velocity (Vav).  Typical Value = 0.017. Default: 0.0',
    )
    vc: Optional[float] = Field(
        None,
        description='Maximum gate closing velocity (Vc).  Unit = PU/sec.  Typical Value = -0.016. Default: 0.0',
    )
    vcv: Optional[float] = Field(
        None,
        description='Maximum servomotor valve closing velocity (Vcv).  Typical Value = -0.017. Default: 0.0',
    )
    waterTunnelSurgeChamberSimulation: Optional[float] = Field(
        None,
        description='Water tunnel and surge chamber simulation (Tflag). true = enable of water tunnel and surge chamber simulation false = inhibit of water tunnel and surge chamber simulation. Typical Value = false. Default: False',
    )
    zsfc: Optional[float] = Field(
        None,
        description='Head of upper water level with respect to the level of penstock (Zsfc).  Unit = m. Typical Value = 25. Default: 0.0',
    )
