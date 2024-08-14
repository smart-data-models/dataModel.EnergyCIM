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
    ExcAC2A = 'ExcAC2A'


class ExcAC2A(BaseModel):
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
    hvgate: Optional[float] = Field(
        None,
        description='Indicates if HV gate is active (HVgate). true = gate is used false = gate is not used. Typical Value = true. Default: False',
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
        None,
        description='Voltage regulator gain (Ka).  Typical Value = 400. Default: 0.0',
    )
    kb: Optional[float] = Field(
        None,
        description='Second stage regulator gain (Kb) (>0).  Exciter field current controller gain.  Typical Value = 25. Default: 0.0',
    )
    kb1: Optional[float] = Field(
        None,
        description='Second stage regulator gain (Kb1). It is exciter field current controller gain used as alternative to Kb to represent a variant of the ExcAC2A model.  Typical Value = 25. Default: 0.0',
    )
    kc: Optional[float] = Field(
        None,
        description='Rectifier loading factor proportional to commutating reactance (Kc).  Typical Value = 0.28. Default: 0.0',
    )
    kd: Optional[float] = Field(
        None,
        description='Demagnetizing factor, a function of exciter alternator reactances (Kd).  Typical Value = 0.35. Default: 0.0',
    )
    ke: Optional[float] = Field(
        None,
        description='Exciter constant related to self-excited field (Ke).  Typical Value = 1. Default: 0.0',
    )
    kf: Optional[float] = Field(
        None,
        description='Excitation control system stabilizer gains (Kf).  Typical Value = 0.03. Default: 0.0',
    )
    kh: Optional[float] = Field(
        None,
        description='Exciter field current feedback gain (Kh).  Typical Value = 1. Default: 0.0',
    )
    kl: Optional[float] = Field(
        None,
        description='Exciter field current limiter gain (Kl).  Typical Value = 10. Default: 0.0',
    )
    kl1: Optional[float] = Field(
        None,
        description='Coefficient to allow different usage of the model (Kl1).  Typical Value = 1. Default: 0.0',
    )
    ks: Optional[float] = Field(
        None,
        description='Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0. Default: 0.0',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    lvgate: Optional[float] = Field(
        None,
        description='Indicates if LV gate is active (LVgate). true = gate is used false = gate is not used. Typical Value = true. Default: False',
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
    seve1: Optional[float] = Field(
        None,
        description='Exciter saturation function value at the corresponding exciter voltage, Ve, back of commutating reactance (Se[Ve]).  Typical Value = 0.037. Default: 0.0',
    )
    seve2: Optional[float] = Field(
        None,
        description='Exciter saturation function value at the corresponding exciter voltage, Ve, back of commutating reactance (Se[Ve]).  Typical Value = 0.012. Default: 0.0',
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    ta: Optional[float] = Field(
        None,
        description='Voltage regulator time constant (Ta).  Typical Value = 0.02. Default: 0',
    )
    tb: Optional[float] = Field(
        None,
        description='Voltage regulator time constant (Tb).  Typical Value = 0. Default: 0',
    )
    tc: Optional[float] = Field(
        None,
        description='Voltage regulator time constant (T).  Typical Value = 0. Default: 0',
    )
    te: Optional[float] = Field(
        None,
        description='Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 0.6. Default: 0',
    )
    tf: Optional[float] = Field(
        None,
        description='Excitation control system stabilizer time constant (Tf).  Typical Value = 1. Default: 0',
    )
    type: Optional[Type6] = Field(None, description='NGSI type. It has to be ExcAC2A')
    vamax: Optional[float] = Field(
        None,
        description='Maximum voltage regulator output (V).  Typical Value = 8. Default: 0.0',
    )
    vamin: Optional[float] = Field(
        None,
        description='Minimum voltage regulator output (V).  Typical Value = -8. Default: 0.0',
    )
    ve1: Optional[float] = Field(
        None,
        description='Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve).  Typical Value = 4.4. Default: 0.0',
    )
    ve2: Optional[float] = Field(
        None,
        description='Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve).  Typical Value = 3.3. Default: 0.0',
    )
    vfemax: Optional[float] = Field(
        None,
        description='Exciter field current limit reference (Vfemax).  Typical Value = 4.4. Default: 0.0',
    )
    vlr: Optional[float] = Field(
        None,
        description='Maximum exciter field current (Vlr).  Typical Value = 4.4. Default: 0.0',
    )
    vrmax: Optional[float] = Field(
        None,
        description='Maximum voltage regulator outputs (Vrmax).  Typical Value = 105. Default: 0.0',
    )
    vrmin: Optional[float] = Field(
        None,
        description='Minimum voltage regulator outputs (Vrmin).  Typical Value = -95. Default: 0.0',
    )