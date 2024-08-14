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
    CsConverter = 'CsConverter'


class CsConverter(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alpha: Optional[float] = Field(
        None,
        description='Firing angle, typical value between 10 and 18 degrees for a rectifier. CSC state variable, result from power flow. Default: 0.0',
    )
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
    gamma: Optional[float] = Field(
        None,
        description='Extinction angle. CSC state variable, result from power flow. Default: 0.0',
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
    maxAlpha: Optional[float] = Field(
        None,
        description='Maximum firing angle. CSC configuration data used in power flow. Default: 0.0',
    )
    maxGamma: Optional[float] = Field(
        None,
        description='Maximum extinction angle. CSC configuration data used in power flow. Default: 0.0',
    )
    maxIdc: Optional[float] = Field(
        None,
        description='The maximum direct current (Id) on the DC side at which the converter should operate. Converter configuration data use in power flow. Default: 0.0',
    )
    minAlpha: Optional[float] = Field(
        None,
        description='Minimum firing angle. CSC configuration data used in power flow. Default: 0.0',
    )
    minGamma: Optional[float] = Field(
        None,
        description='Minimum extinction angle. CSC configuration data used in power flow. Default: 0.0',
    )
    minIdc: Optional[float] = Field(
        None,
        description='The minimum direct current (Id) on the DC side at which the converter should operate. CSC configuration data used in power flow. Default: 0.0',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    operatingMode: Optional[float] = Field(
        None,
        description='Indicates whether the DC pole is operating as an inverter or as a rectifier. CSC control variable used in power flow. Default: None',
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
    pPccControl: Optional[float] = Field(None, description=' Default: None')
    ratedIdc: Optional[float] = Field(
        None,
        description='Rated converter DC current, also called IdN. Converter configuration data used in power flow. Default: 0.0',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    targetAlpha: Optional[float] = Field(
        None,
        description='Target firing angle. CSC control variable used in power flow. Default: 0.0',
    )
    targetGamma: Optional[float] = Field(
        None,
        description='Target extinction angle. CSC  control variable used in power flow. Default: 0.0',
    )
    targetIdc: Optional[float] = Field(
        None,
        description='DC current target value. CSC control variable used in power flow. Default: 0.0',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI type. It has to be CsConverter'
    )
