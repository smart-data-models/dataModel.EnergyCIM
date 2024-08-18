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
    SynchronousMachine = 'SynchronousMachine'


class SynchronousMachine(BaseModel):
    InitialReactiveCapabilityCurve: Optional[float] = Field(
        None,
        description='Synchronous machines using this curve as default. Default: None',
    )
    SynchronousMachineDynamics: Optional[float] = Field(
        None,
        description='Synchronous machine dynamics model used to describe dynamic behavior of this synchronous machine. Default: None',
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
    earthing: Optional[float] = Field(
        None,
        description='Indicates whether or not the generator is earthed. Used for short circuit data exchange according to IEC 60909 Default: False',
    )
    earthingStarPointR: Optional[float] = Field(
        None,
        description='Generator star point earthing resistance (Re). Used for short circuit data exchange according to IEC 60909 Default: 0.0',
    )
    earthingStarPointX: Optional[float] = Field(
        None,
        description='Generator star point earthing reactance (Xe). Used for short circuit data exchange according to IEC 60909 Default: 0.0',
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
    ikk: Optional[float] = Field(
        None,
        description='Steady-state short-circuit current (in A for the profile) of generator with compound excitation during 3-phase short circuit. - Ikk=0: Generator with no compound excitation. - Ikk?0: Generator with compound excitation. Ikk is used to calculate the minimum steady-state short-circuit current for generators with compound excitation (Section 4.6.1.2 in the IEC 60909-0) Used only for single fed short circuit on a generator. (Section 4.3.4.2. in the IEC 60909-0) Default: 0.0',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    maxQ: Optional[float] = Field(
        None,
        description='Maximum reactive power limit. This is the maximum (nameplate) limit for the unit. Default: 0.0',
    )
    minQ: Optional[float] = Field(
        None, description='Minimum reactive power limit for the unit. Default: 0.0'
    )
    mu: Optional[float] = Field(
        None,
        description='Factor to calculate the breaking current (Section 4.5.2.1 in the IEC 60909-0). Used only for single fed short circuit on a generator (Section 4.3.4.2. in the IEC 60909-0). Default: 0.0',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    operatingMode: Optional[float] = Field(
        None, description='Current mode of operation. Default: None'
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
    qPercent: Optional[float] = Field(
        None,
        description='Percent of the coordinated reactive control that comes from this machine. Default: 0.0',
    )
    r: Optional[float] = Field(
        None,
        description='Equivalent resistance (RG) of generator. RG is considered for the calculation of all currents, except for the calculation of the peak current ip. Used for short circuit data exchange according to IEC 60909 Default: 0.0',
    )
    r0: Optional[float] = Field(
        None,
        description='Zero sequence resistance of the synchronous machine. Default: 0.0',
    )
    r2: Optional[float] = Field(
        None, description='Negative sequence resistance. Default: 0.0'
    )
    referencePriority: Optional[float] = Field(
        None,
        description='Priority of unit for use as powerflow voltage phase angle reference bus selection. 0 = don t care (default) 1 = highest priority. 2 is less than 1 and so on. Default: 0',
    )
    satDirectSubtransX: Optional[float] = Field(
        None,
        description='Direct-axis subtransient reactance saturated, also known as Xd`sat. Default: 0.0',
    )
    satDirectSyncX: Optional[float] = Field(
        None,
        description='Direct-axes saturated synchronous reactance (xdsat); reciprocal of short-circuit ration. Used for short circuit data exchange, only for single fed short circuit on a generator. (Section 4.3.4.2. in the IEC 60909-0). Default: 0.0',
    )
    satDirectTransX: Optional[float] = Field(
        None,
        description='Saturated Direct-axis transient reactance. The attribute is primarily used for short circuit calculations according to ANSI. Default: 0.0',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    shortCircuitRotorType: Optional[float] = Field(
        None,
        description='Type of rotor, used by short circuit applications, only for single fed short circuit according to IEC 60909. Default: None',
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    type: Optional[Type6] = Field(
        None,
        description='Modes that this synchronous machine can operate in. Default: None. NGSI entity type. it has to be SynchronousMachine',
    )
    voltageRegulationRange: Optional[float] = Field(
        None,
        description='Range of generator voltage regulation (PG in the IEC 60909-0) used for calculation of the impedance correction factor KG defined in IEC 60909-0 This attribute is used to describe the operating voltage of the generating unit. Default: 0.0',
    )
    x0: Optional[float] = Field(
        None,
        description='Zero sequence reactance of the synchronous machine. Default: 0.0',
    )
    x2: Optional[float] = Field(
        None, description='Negative sequence reactance. Default: 0.0'
    )
