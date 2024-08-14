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
    GovCT2 = 'GovCT2'


class GovCT2(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    aset: Optional[float] = Field(
        None,
        description='Acceleration limiter setpoint (Aset).  Unit = PU/sec.  Typical Value = 10. Default: 0.0',
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
    db: Optional[float] = Field(
        None,
        description='Speed governor dead band in per unit speed (db).  In the majority of applications, it is recommended that this value be set to zero.  Typical Value = 0. Default: 0.0',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    dm: Optional[float] = Field(
        None,
        description='Speed sensitivity coefficient (Dm).  Dm can represent either the variation of the engine power with the shaft speed or the variation of maximum power capability with shaft speed.  If it is positive it describes the falling slope of the engine speed verses power characteristic as speed increases. A slightly falling characteristic is typical for reciprocating engines and some aero-derivative turbines.  If it is negative the engine power is assumed to be unaffected by the shaft speed, but the maximum permissible fuel flow is taken to fall with falling shaft speed. This is characteristic of single-shaft industrial turbines due to exhaust temperature limits.  Typical Value = 0. Default: 0.0',
    )
    flim1: Optional[float] = Field(
        None,
        description='Frequency threshold 1 (Flim1).  Unit = Hz.  Typical Value = 59. Default: 0.0',
    )
    flim10: Optional[float] = Field(
        None,
        description='Frequency threshold 10 (Flim10).  Unit = Hz.  Typical Value = 0. Default: 0.0',
    )
    flim2: Optional[float] = Field(
        None,
        description='Frequency threshold 2 (Flim2).  Unit = Hz.  Typical Value = 0. Default: 0.0',
    )
    flim3: Optional[float] = Field(
        None,
        description='Frequency threshold 3 (Flim3).  Unit = Hz.  Typical Value = 0. Default: 0.0',
    )
    flim4: Optional[float] = Field(
        None,
        description='Frequency threshold 4 (Flim4).  Unit = Hz.  Typical Value = 0. Default: 0.0',
    )
    flim5: Optional[float] = Field(
        None,
        description='Frequency threshold 5 (Flim5).  Unit = Hz.  Typical Value = 0. Default: 0.0',
    )
    flim6: Optional[float] = Field(
        None,
        description='Frequency threshold 6 (Flim6).  Unit = Hz.  Typical Value = 0. Default: 0.0',
    )
    flim7: Optional[float] = Field(
        None,
        description='Frequency threshold 7 (Flim7).  Unit = Hz.  Typical Value = 0. Default: 0.0',
    )
    flim8: Optional[float] = Field(
        None,
        description='Frequency threshold 8 (Flim8).  Unit = Hz.  Typical Value = 0. Default: 0.0',
    )
    flim9: Optional[float] = Field(
        None,
        description='Frequency threshold 9 (Flim9).  Unit = Hz.  Typical Value = 0. Default: 0.0',
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
        description='Acceleration limiter Gain (Ka).  Typical Value = 10. Default: 0.0',
    )
    kdgov: Optional[float] = Field(
        None,
        description='Governor derivative gain (Kdgov).  Typical Value = 0. Default: 0.0',
    )
    kigov: Optional[float] = Field(
        None,
        description='Governor integral gain (Kigov).  Typical Value = 0.45. Default: 0.0',
    )
    kiload: Optional[float] = Field(
        None,
        description='Load limiter integral gain for PI controller (Kiload).  Typical Value = 1. Default: 0.0',
    )
    kimw: Optional[float] = Field(
        None,
        description='Power controller (reset) gain (Kimw).  The default value of 0.01 corresponds to a reset time of 100 seconds.  A value of 0.001 corresponds to a relatively slow acting load controller.  Typical Value = 0. Default: 0.0',
    )
    kpgov: Optional[float] = Field(
        None,
        description='Governor proportional gain (Kpgov).  Typical Value = 4. Default: 0.0',
    )
    kpload: Optional[float] = Field(
        None,
        description='Load limiter proportional gain for PI controller (Kpload).  Typical Value = 1. Default: 0.0',
    )
    kturb: Optional[float] = Field(
        None, description='Turbine gain (Kturb).  Typical Value = 1.9168. Default: 0.0'
    )
    ldref: Optional[float] = Field(
        None,
        description='Load limiter reference value (Ldref).  Typical Value = 1. Default: 0.0',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    maxerr: Optional[float] = Field(
        None,
        description='Maximum value for speed error signal (Maxerr).  Typical Value = 1. Default: 0.0',
    )
    minerr: Optional[float] = Field(
        None,
        description='Minimum value for speed error signal (Minerr).  Typical Value = -1. Default: 0.0',
    )
    mwbase: Optional[float] = Field(
        None,
        description='Base for power values (MWbase) (> 0).  Unit = MW. Default: 0.0',
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
    plim1: Optional[float] = Field(
        None, description='Power limit 1 (Plim1).  Typical Value = 0.8325. Default: 0.0'
    )
    plim10: Optional[float] = Field(
        None, description='Power limit 10 (Plim10).  Typical Value = 0. Default: 0.0'
    )
    plim2: Optional[float] = Field(
        None, description='Power limit 2 (Plim2).  Typical Value = 0. Default: 0.0'
    )
    plim3: Optional[float] = Field(
        None, description='Power limit 3 (Plim3).  Typical Value = 0. Default: 0.0'
    )
    plim4: Optional[float] = Field(
        None, description='Power limit 4 (Plim4).  Typical Value = 0. Default: 0.0'
    )
    plim5: Optional[float] = Field(
        None, description='Power limit 5 (Plim5).  Typical Value = 0. Default: 0.0'
    )
    plim6: Optional[float] = Field(
        None, description='Power limit 6 (Plim6).  Typical Value = 0. Default: 0.0'
    )
    plim7: Optional[float] = Field(
        None, description='Power limit 7 (Plim7).  Typical Value = 0. Default: 0.0'
    )
    plim8: Optional[float] = Field(
        None, description='Power limit 8 (Plim8).  Typical Value = 0. Default: 0.0'
    )
    plim9: Optional[float] = Field(
        None, description='Power Limit 9 (Plim9).  Typical Value = 0. Default: 0.0'
    )
    prate: Optional[float] = Field(
        None,
        description='Ramp rate for frequency-dependent power limit (Prate).  Typical Value = 0.017. Default: 0.0',
    )
    r: Optional[float] = Field(
        None, description='Permanent droop (R).  Typical Value = 0.05. Default: 0.0'
    )
    rclose: Optional[float] = Field(
        None,
        description='Minimum valve closing rate (Rclose).  Unit = PU/sec.  Typical Value = -99. Default: 0.0',
    )
    rdown: Optional[float] = Field(
        None,
        description='Maximum rate of load limit decrease (Rdown).  Typical Value = -99. Default: 0.0',
    )
    ropen: Optional[float] = Field(
        None,
        description='Maximum valve opening rate (Ropen).  Unit = PU/sec.  Typical Value = 99. Default: 0.0',
    )
    rselect: Optional[float] = Field(
        None,
        description='Feedback signal for droop (Rselect).  Typical Value = electricalPower. Default: None',
    )
    rup: Optional[float] = Field(
        None,
        description='Maximum rate of load limit increase (Rup).  Typical Value = 99. Default: 0.0',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    ta: Optional[float] = Field(
        None,
        description='Acceleration limiter time constant (Ta).  Typical Value = 1. Default: 0',
    )
    tact: Optional[float] = Field(
        None,
        description='Actuator time constant (Tact).  Typical Value = 0.4. Default: 0',
    )
    tb: Optional[float] = Field(
        None,
        description='Turbine lag time constant (Tb).  Typical Value = 0.1. Default: 0',
    )
    tc: Optional[float] = Field(
        None,
        description='Turbine lead time constant (Tc).  Typical Value = 0. Default: 0',
    )
    tdgov: Optional[float] = Field(
        None,
        description='Governor derivative controller time constant (Tdgov).  Typical Value = 1. Default: 0',
    )
    teng: Optional[float] = Field(
        None,
        description='Transport time delay for diesel engine used in representing diesel engines where there is a small but measurable transport delay between a change in fuel flow setting and the development of torque (Teng).  Teng should be zero in all but special cases where this transport delay is of particular concern.  Typical Value = 0. Default: 0',
    )
    tfload: Optional[float] = Field(
        None,
        description='Load Limiter time constant (Tfload).  Typical Value = 3. Default: 0',
    )
    tpelec: Optional[float] = Field(
        None,
        description='Electrical power transducer time constant (Tpelec).  Typical Value = 2.5. Default: 0',
    )
    tsa: Optional[float] = Field(
        None,
        description='Temperature detection lead time constant (Tsa).  Typical Value = 0. Default: 0',
    )
    tsb: Optional[float] = Field(
        None,
        description='Temperature detection lag time constant (Tsb).  Typical Value = 50. Default: 0',
    )
    type: Optional[Type6] = Field(None, description='NGSI type. It has to be GovCT2')
    vmax: Optional[float] = Field(
        None,
        description='Maximum valve position limit (Vmax).  Typical Value = 1. Default: 0.0',
    )
    vmin: Optional[float] = Field(
        None,
        description='Minimum valve position limit (Vmin).  Typical Value = 0.175. Default: 0.0',
    )
    wfnl: Optional[float] = Field(
        None,
        description='No load fuel flow (Wfnl).  Typical Value = 0.187. Default: 0.0',
    )
    wfspd: Optional[float] = Field(
        None,
        description='Switch for fuel source characteristic to recognize that fuel flow, for a given fuel valve stroke, can be proportional to engine speed (Wfspd). true = fuel flow proportional to speed (for some gas turbines and diesel engines with positive displacement fuel injectors) false = fuel control system keeps fuel flow independent of engine speed. Typical Value = false. Default: False',
    )
