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
    ExcSK = 'ExcSK'


class ExcSK(BaseModel):
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
    efdmax: Optional[float] = Field(
        None, description='Field voltage clipping limit (Efdmax). Default: 0.0'
    )
    efdmin: Optional[float] = Field(
        None, description='Field voltage clipping limit (Efdmin). Default: 0.0'
    )
    emax: Optional[float] = Field(
        None,
        description='Maximum field voltage output (Emax).  Typical Value = 20. Default: 0.0',
    )
    emin: Optional[float] = Field(
        None,
        description='Minimum field voltage output (Emin).  Typical Value = -20. Default: 0.0',
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
        None, description='Gain (K).  Typical Value = 1. Default: 0.0'
    )
    k1: Optional[float] = Field(
        None,
        description='Parameter of underexcitation limit (K1).  Typical Value = 0.1364. Default: 0.0',
    )
    k2: Optional[float] = Field(
        None,
        description='Parameter of underexcitation limit (K2).  Typical Value = -0.3861. Default: 0.0',
    )
    kc: Optional[float] = Field(
        None, description='PI controller gain (Kc).  Typical Value = 70. Default: 0.0'
    )
    kce: Optional[float] = Field(
        None,
        description='Rectifier regulation factor (Kce).  Typical Value = 0. Default: 0.0',
    )
    kd: Optional[float] = Field(
        None,
        description='Exciter internal reactance (Kd).  Typical Value = 0. Default: 0.0',
    )
    kgob: Optional[float] = Field(
        None, description='P controller gain (Kgob).  Typical Value = 10. Default: 0.0'
    )
    kp: Optional[float] = Field(
        None, description='PI controller gain (Kp).  Typical Value = 1. Default: 0.0'
    )
    kqi: Optional[float] = Field(
        None,
        description='PI controller gain of integral component (Kqi).  Typical Value = 0. Default: 0.0',
    )
    kqob: Optional[float] = Field(
        None, description='Rate of rise of the reactive power (Kqob). Default: 0.0'
    )
    kqp: Optional[float] = Field(
        None, description='PI controller gain (Kqp).  Typical Value = 0. Default: 0.0'
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    nq: Optional[float] = Field(
        None,
        description='Dead band of reactive power (nq).  Determines the range of sensitivity.  Typical Value = 0.001. Default: 0.0',
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
    qconoff: Optional[float] = Field(
        None,
        description='Secondary voltage control state (Qc_on_off). true = secondary voltage control is ON false = secondary voltage control is OFF. Typical Value = false. Default: False',
    )
    qz: Optional[float] = Field(
        None,
        description='Desired value (setpoint) of reactive power, manual setting (Qz). Default: 0.0',
    )
    remote: Optional[float] = Field(
        None,
        description='Selector to apply automatic calculation in secondary controller model. true = automatic calculation is activated false = manual set is active; the use of desired value of reactive power (Qz) is required. Typical Value = true. Default: False',
    )
    sbase: Optional[float] = Field(
        None,
        description='Apparent power of the unit (Sbase).  Unit = MVA.  Typical Value = 259. Default: 0.0',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    tc: Optional[float] = Field(
        None,
        description='PI controller phase lead time constant (Tc).  Typical Value = 8. Default: 0',
    )
    te: Optional[float] = Field(
        None,
        description='Time constant of gain block (Te).  Typical Value = 0.1. Default: 0',
    )
    ti: Optional[float] = Field(
        None,
        description='PI controller phase lead time constant (Ti).  Typical Value = 2. Default: 0',
    )
    tp: Optional[float] = Field(
        None, description='Time constant (Tp).  Typical Value = 0.1. Default: 0'
    )
    tr: Optional[float] = Field(
        None,
        description='Voltage transducer time constant (Tr).  Typical Value = 0.01. Default: 0',
    )
    type: Optional[Type6] = Field(None, description='NGSI type. It has to be ExcSK')
    uimax: Optional[float] = Field(
        None, description='Maximum error (Uimax).  Typical Value = 10. Default: 0.0'
    )
    uimin: Optional[float] = Field(
        None, description='Minimum error (UImin).  Typical Value = -10. Default: 0.0'
    )
    urmax: Optional[float] = Field(
        None,
        description='Maximum controller output (URmax).  Typical Value = 10. Default: 0.0',
    )
    urmin: Optional[float] = Field(
        None,
        description='Minimum controller output (URmin).  Typical Value = -10. Default: 0.0',
    )
    vtmax: Optional[float] = Field(
        None,
        description='Maximum terminal voltage input (Vtmax).  Determines the range of voltage dead band.  Typical Value = 1.05. Default: 0.0',
    )
    vtmin: Optional[float] = Field(
        None,
        description='Minimum terminal voltage input (Vtmin).  Determines the range of voltage dead band.  Typical Value = 0.95. Default: 0.0',
    )
    yp: Optional[float] = Field(
        None,
        description='Maximum output (Yp).  Minimum output = 0.  Typical Value = 1. Default: 0.0',
    )
