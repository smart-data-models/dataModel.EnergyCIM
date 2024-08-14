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
    GovHydroWEH = 'GovHydroWEH'


class GovHydroWEH(BaseModel):
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
    db: Optional[float] = Field(None, description='Speed Dead Band (db). Default: 0.0')
    description: Optional[str] = Field(None, description='A description of this item')
    dicn: Optional[float] = Field(
        None,
        description='Value to allow the integral controller to advance beyond the gate limits (Dicn). Default: 0.0',
    )
    dpv: Optional[float] = Field(
        None,
        description='Value to allow the Pilot valve controller to advance beyond the gate limits (Dpv). Default: 0.0',
    )
    dturb: Optional[float] = Field(
        None,
        description='Turbine damping factor (Dturb).  Unit = delta P (PU of MWbase) / delta speed (PU). Default: 0.0',
    )
    feedbackSignal: Optional[float] = Field(
        None,
        description='Feedback signal selection (Sw). true = PID Output (if R-Perm-Gate=droop and R-Perm-Pe=0) false = Electrical Power (if R-Perm-Gate=0 and R-Perm-Pe=droop) or false = Gate Position (if R-Perm-Gate=droop and R-Perm-Pe=0). Default: False',
    )
    fl1: Optional[float] = Field(
        None,
        description='Flow Gate 1 (Fl1).  Flow value for gate position point 1 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0',
    )
    fl2: Optional[float] = Field(
        None,
        description='Flow Gate 2 (Fl2).  Flow value for gate position point 2 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0',
    )
    fl3: Optional[float] = Field(
        None,
        description='Flow Gate 3 (Fl3).  Flow value for gate position point 3 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0',
    )
    fl4: Optional[float] = Field(
        None,
        description='Flow Gate 4 (Fl4).  Flow value for gate position point 4 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0',
    )
    fl5: Optional[float] = Field(
        None,
        description='Flow Gate 5 (Fl5).  Flow value for gate position point 5 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0',
    )
    fp1: Optional[float] = Field(
        None,
        description='Flow P1 (Fp1).  Turbine Flow value for point 1 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0',
    )
    fp10: Optional[float] = Field(
        None,
        description='Flow P10 (Fp10).  Turbine Flow value for point 10 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0',
    )
    fp2: Optional[float] = Field(
        None,
        description='Flow P2 (Fp2).  Turbine Flow value for point 2 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0',
    )
    fp3: Optional[float] = Field(
        None,
        description='Flow P3 (Fp3).  Turbine Flow value for point 3 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0',
    )
    fp4: Optional[float] = Field(
        None,
        description='Flow P4 (Fp4).  Turbine Flow value for point 4 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0',
    )
    fp5: Optional[float] = Field(
        None,
        description='Flow P5 (Fp5).  Turbine Flow value for point 5 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0',
    )
    fp6: Optional[float] = Field(
        None,
        description='Flow P6 (Fp6).  Turbine Flow value for point 6 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0',
    )
    fp7: Optional[float] = Field(
        None,
        description='Flow P7 (Fp7).  Turbine Flow value for point 7 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0',
    )
    fp8: Optional[float] = Field(
        None,
        description='Flow P8 (Fp8).  Turbine Flow value for point 8 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0',
    )
    fp9: Optional[float] = Field(
        None,
        description='Flow P9 (Fp9).  Turbine Flow value for point 9 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0',
    )
    gmax: Optional[float] = Field(
        None, description='Maximum Gate Position (Gmax). Default: 0.0'
    )
    gmin: Optional[float] = Field(
        None, description='Minimum Gate Position (Gmin). Default: 0.0'
    )
    gtmxcl: Optional[float] = Field(
        None, description='Maximum gate closing rate (Gtmxcl). Default: 0.0'
    )
    gtmxop: Optional[float] = Field(
        None, description='Maximum gate opening rate (Gtmxop). Default: 0.0'
    )
    gv1: Optional[float] = Field(
        None,
        description='Gate 1 (Gv1).  Gate Position value for point 1 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0',
    )
    gv2: Optional[float] = Field(
        None,
        description='Gate 2 (Gv2).  Gate Position value for point 2 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0',
    )
    gv3: Optional[float] = Field(
        None,
        description='Gate 3 (Gv3).  Gate Position value for point 3 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0',
    )
    gv4: Optional[float] = Field(
        None,
        description='Gate 4 (Gv4).  Gate Position value for point 4 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0',
    )
    gv5: Optional[float] = Field(
        None,
        description='Gate 5 (Gv5).  Gate Position value for point 5 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0',
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
    kd: Optional[float] = Field(
        None, description='Derivative controller derivative gain (Kd). Default: 0.0'
    )
    ki: Optional[float] = Field(
        None, description='Derivative controller Integral gain (Ki). Default: 0.0'
    )
    kp: Optional[float] = Field(
        None, description='Derivative control gain (Kp). Default: 0.0'
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
    pmss1: Optional[float] = Field(
        None,
        description='Pmss Flow P1 (Pmss1).  Mechanical Power output Pmss for Turbine Flow point 1 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0',
    )
    pmss10: Optional[float] = Field(
        None,
        description='Pmss Flow P10 (Pmss10).  Mechanical Power output Pmss for Turbine Flow point 10 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0',
    )
    pmss2: Optional[float] = Field(
        None,
        description='Pmss Flow P2 (Pmss2).  Mechanical Power output Pmss for Turbine Flow point 2 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0',
    )
    pmss3: Optional[float] = Field(
        None,
        description='Pmss Flow P3 (Pmss3).  Mechanical Power output Pmss for Turbine Flow point 3 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0',
    )
    pmss4: Optional[float] = Field(
        None,
        description='Pmss Flow P4 (Pmss4).  Mechanical Power output Pmss for Turbine Flow point 4 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0',
    )
    pmss5: Optional[float] = Field(
        None,
        description='Pmss Flow P5 (Pmss5).  Mechanical Power output Pmss for Turbine Flow point 5 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0',
    )
    pmss6: Optional[float] = Field(
        None,
        description='Pmss Flow P6 (Pmss6).  Mechanical Power output Pmss for Turbine Flow point 6 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0',
    )
    pmss7: Optional[float] = Field(
        None,
        description='Pmss Flow P7 (Pmss7).  Mechanical Power output Pmss for Turbine Flow point 7 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0',
    )
    pmss8: Optional[float] = Field(
        None,
        description='Pmss Flow P8 (Pmss8).  Mechanical Power output Pmss for Turbine Flow point 8 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0',
    )
    pmss9: Optional[float] = Field(
        None,
        description='Pmss Flow P9 (Pmss9).  Mechanical Power output Pmss for Turbine Flow point 9 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0',
    )
    rpg: Optional[float] = Field(
        None,
        description='Permanent droop for governor output feedback (R-Perm-Gate). Default: 0.0',
    )
    rpp: Optional[float] = Field(
        None,
        description='Permanent droop for electrical power feedback (R-Perm-Pe). Default: 0.0',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    td: Optional[float] = Field(
        None,
        description='Derivative controller time constant to limit the derivative characteristic beyond a breakdown frequency to avoid amplification of high-frequency noise (Td). Default: 0',
    )
    tdv: Optional[float] = Field(
        None, description='Distributive Valve time lag time constant (Tdv). Default: 0'
    )
    tg: Optional[float] = Field(
        None,
        description='Value to allow the Distribution valve controller to advance beyond the gate movement rate limit (Tg). Default: 0',
    )
    tp: Optional[float] = Field(
        None, description='Pilot Valve time lag time constant (Tp). Default: 0'
    )
    tpe: Optional[float] = Field(
        None, description='Electrical power droop time constant (Tpe). Default: 0'
    )
    tw: Optional[float] = Field(
        None, description='Water inertia time constant (Tw) (>0). Default: 0'
    )
    type: Optional[Type6] = Field(
        None, description='NGSI type. It has to be GovHydroWEH'
    )
