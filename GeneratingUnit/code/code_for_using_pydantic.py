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
    GeneratingUnit = 'GeneratingUnit'


class GeneratingUnit(BaseModel):
    ControlAreaGeneratingUnit: Optional[float] = Field(
        None,
        description="ControlArea specifications for this generating unit. Default: 'list'",
    )
    GrossToNetActivePowerCurves: Optional[float] = Field(
        None,
        description="A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit. Default: 'list'",
    )
    RotatingMachine: Optional[float] = Field(
        None,
        description="A synchronous machine may operate as a generator and as such becomes a member of a generating unit. Default: 'list'",
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
    genControlSource: Optional[float] = Field(
        None, description='The source of controls for a generating unit. Default: None'
    )
    governorSCD: Optional[float] = Field(
        None,
        description='Governor Speed Changer Droop.   This is the change in generator power output divided by the change in frequency normalized by the nominal power of the generator and the nominal frequency and expressed in percent and negated. A positive value of speed change droop provides additional generator output upon a drop in frequency. Default: 0.0',
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
    initialP: Optional[float] = Field(
        None,
        description='Default initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration. Default: 0.0',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    longPF: Optional[float] = Field(
        None,
        description='Generating unit long term economic participation factor. Default: 0.0',
    )
    maxOperatingP: Optional[float] = Field(
        None,
        description='This is the maximum operating active power limit the dispatcher can enter for this unit. Default: 0.0',
    )
    maximumAllowableSpinningReserve: Optional[float] = Field(
        None,
        description='Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point. Default: 0.0',
    )
    minOperatingP: Optional[float] = Field(
        None,
        description='This is the minimum operating active power limit the dispatcher can enter for this unit. Default: 0.0',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    nominalP: Optional[float] = Field(
        None,
        description='The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes such as the governor speed change droop (governorSCD attribute). The attribute shall be a positive value equal or less than RotatingMachine.ratedS. Default: 0.0',
    )
    normalPF: Optional[float] = Field(
        None, description='Generating unit economic participation factor. Default: 0.0'
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
    ratedGrossMaxP: Optional[float] = Field(
        None,
        description='The unit`s gross rated maximum capacity (book value). Default: 0.0',
    )
    ratedGrossMinP: Optional[float] = Field(
        None,
        description='The gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission grid. Default: 0.0',
    )
    ratedNetMaxP: Optional[float] = Field(
        None,
        description='The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity. Default: 0.0',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    shortPF: Optional[float] = Field(
        None,
        description='Generating unit short term economic participation factor. Default: 0.0',
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    startupCost: Optional[float] = Field(
        None,
        description='The initial startup cost incurred for each start of the GeneratingUnit. Default: 0.0',
    )
    totalEfficiency: Optional[float] = Field(
        None,
        description='The efficiency of the unit in converting the fuel into electrical energy. Default: 0.0',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI type. It has to be GeneratingUnit'
    )
    variableCost: Optional[float] = Field(
        None,
        description='The variable cost component of production per unit of ActivePower. Default: 0.0',
    )
