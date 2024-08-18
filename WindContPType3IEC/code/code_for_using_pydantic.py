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
    WindContPType3IEC = 'WindContPType3IEC'


class WindContPType3IEC(BaseModel):
    WindDynamicsLookupTable: Optional[float] = Field(
        None,
        description="The P control type 3 model with which this wind dynamics lookup table is associated. Default: 'list'",
    )
    WindGenTurbineType3IEC: Optional[float] = Field(
        None,
        description='Wind turbine type 3 model with which this Wind control P type 3 model is associated. Default: None',
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
    dpmax: Optional[float] = Field(
        None,
        description='Maximum wind turbine power ramp rate (). It is project dependent parameter. Default: 0.0',
    )
    dtrisemaxlvrt: Optional[float] = Field(
        None,
        description='Limitation of torque rise rate during LVRT for S (d). It is project dependent parameter. Default: 0.0',
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
    kdtd: Optional[float] = Field(
        None,
        description='Gain for active drive train damping (). It is type dependent parameter. Default: 0.0',
    )
    kip: Optional[float] = Field(
        None,
        description='PI controller integration parameter (). It is type dependent parameter. Default: 0.0',
    )
    kpp: Optional[float] = Field(
        None,
        description='PI controller proportional gain (). It is type dependent parameter. Default: 0.0',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    mplvrt: Optional[float] = Field(
        None,
        description='Enable LVRT power control mode (M true = 1: voltage control false = 0: reactive power control.  It is project dependent parameter. Default: False',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    omegaoffset: Optional[float] = Field(
        None,
        description='Offset to reference value that limits controller action during rotor speed changes (omega). It is case dependent parameter. Default: 0.0',
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
    pdtdmax: Optional[float] = Field(
        None,
        description='Maximum active drive train damping power (). It is type dependent parameter. Default: 0.0',
    )
    rramp: Optional[float] = Field(
        None,
        description='Ramp limitation of torque, required in some grid codes (). It is project dependent parameter. Default: 0.0',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    tdvs: Optional[float] = Field(
        None,
        description='Timedelay after deep voltage sags (T). It is project dependent parameter. Default: 0',
    )
    temin: Optional[float] = Field(
        None,
        description='Minimum electrical generator torque (). It is type dependent parameter. Default: 0.0',
    )
    tomegafilt: Optional[float] = Field(
        None,
        description='Filter time constant for generator speed measurement (). It is type dependent parameter. Default: 0',
    )
    tpfilt: Optional[float] = Field(
        None,
        description='Filter time constant for power measurement (). It is type dependent parameter. Default: 0',
    )
    tpord: Optional[float] = Field(
        None,
        description='Time constant in power order lag (). It is type dependent parameter. Default: 0.0',
    )
    tufilt: Optional[float] = Field(
        None,
        description='Filter time constant for voltage measurement (). It is type dependent parameter. Default: 0',
    )
    tuscale: Optional[float] = Field(
        None,
        description='Voltage scaling factor of reset-torque (T). It is project dependent parameter. Default: 0.0',
    )
    twref: Optional[float] = Field(
        None,
        description='Time constant in speed reference filter (). It is type dependent parameter. Default: 0',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI type. It has to be WindContPType3IEC'
    )
    udvs: Optional[float] = Field(
        None,
        description='Voltage limit for hold LVRT status after deep voltage sags (). It is project dependent parameter. Default: 0.0',
    )
    updip: Optional[float] = Field(
        None,
        description='Voltage dip threshold for P-control ().  Part of turbine control, often different (e.g 0.8) from converter thresholds. It is project dependent parameter. Default: 0.0',
    )
    wdtd: Optional[float] = Field(
        None,
        description='Active drive train damping frequency (omega). It can be calculated from two mass model parameters. It is type dependent parameter. Default: 0.0',
    )
    zeta: Optional[float] = Field(
        None,
        description='Coefficient for active drive train damping (zeta). It is type dependent parameter. Default: 0.0',
    )
