# dataModel.EnergyCIM

### List of data models

The following entity types are available:
- [Accumulator](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Accumulator/README.md). Adapted from CIM data models. Accumulator represents an accumulated (counted) Measurement, e.g. an energy value.

- [AccumulatorLimit](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/AccumulatorLimit/README.md). Adapted from CIM data models. Limit values for Accumulator measurements.

- [AccumulatorLimitSet](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/AccumulatorLimitSet/README.md). Adapted from CIM data models. An AccumulatorLimitSet specifies a set of Limits that are associated with an Accumulator measurement.

- [AccumulatorReset](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/AccumulatorReset/README.md). Adapted from CIM data models. This command reset the counter value to zero.

- [AccumulatorValue](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/AccumulatorValue/README.md). Adapted from CIM data models. AccumulatorValue represents an accumulated (counted) MeasurementValue.

- [ACDCConverter](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ACDCConverter/README.md). Adapted from CIM data models. A unit with valves for three phases, together with unit control equipment, essential protective and switching devices, DC storage capacitors, phase reactors and auxiliaries, if any, used for conversion.

- [ACDCConverterDCTerminal](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ACDCConverterDCTerminal/README.md). Adapted from CIM data models. A DC electrical connection point at the AC/DC converter. The AC/DC converter is electrically connected also to the AC side. The AC connection is inherited from the AC conducting equipment in the same way as any other AC equipment. The AC/DC converter DC terminal is separate from generic DC terminal to restrict the connection with the AC side to AC/DC converter and so that no other DC conducting equipment can be connected to the AC side.

- [ACDCTerminal](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ACDCTerminal/README.md). Adapted from CIM data models. An electrical connection point (AC or DC) to a piece of conducting equipment. Terminals are connected at physical connection points called connectivity nodes.

- [ACLineSegment](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ACLineSegment/README.md). Adapted from CIM data models. A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system. For symmetrical, transposed 3ph lines, it is sufficient to use  attributes of the line segment, which describe impedances and admittances for the entire length of the segment.  Additionally impedances can be computed by using length and associated per length impedances. The BaseVoltage at the two ends of ACLineSegments in a Line shall have the same BaseVoltage.nominalVoltage. However, boundary lines  may have slightly different BaseVoltage.nominalVoltages and  variation is allowed. Larger voltage difference in general requires use of an equivalent branch.

- [ActivePower](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ActivePower/README.md). Adapted from CIM data models. Product of RMS value of the voltage and the RMS value of the in-phase component of the current.

- [ActivePowerLimit](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ActivePowerLimit/README.md). Adapted from CIM data models. Limit on active power flow.

- [ActivePowerPerCurrentFlow](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ActivePowerPerCurrentFlow/README.md). Adapted from CIM data models. 

- [ActivePowerPerFrequency](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ActivePowerPerFrequency/README.md). Adapted from CIM data models. Active power variation with frequency.

- [Analog](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Analog/README.md). Adapted from CIM data models. Analog represents an analog Measurement.

- [AnalogControl](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/AnalogControl/README.md). Adapted from CIM data models. An analog control used for supervisory control.

- [AnalogLimit](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/AnalogLimit/README.md). Adapted from CIM data models. Limit values for Analog measurements.

- [AnalogLimitSet](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/AnalogLimitSet/README.md). Adapted from CIM data models. An AnalogLimitSet specifies a set of Limits that are associated with an Analog measurement.

- [AnalogValue](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/AnalogValue/README.md). Adapted from CIM data models. AnalogValue represents an analog MeasurementValue.

- [AngleDegrees](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/AngleDegrees/README.md). Adapted from CIM data models. Measurement of angle in degrees.

- [AngleRadians](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/AngleRadians/README.md). Adapted from CIM data models. Phase angle in radians.

- [ApparentPower](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ApparentPower/README.md). Adapted from CIM data models. Product of the RMS value of the voltage and the RMS value of the current.

- [ApparentPowerLimit](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ApparentPowerLimit/README.md). Adapted from CIM data models. Apparent power limit.

- [Area](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Area/README.md). Adapted from CIM data models. Area.

- [AsynchronousMachine](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/AsynchronousMachine/README.md). Adapted from CIM data models. A rotating machine whose shaft rotates asynchronously with the electrical field.  Also known as an induction machine with no external connection to the rotor windings, e.g squirrel-cage induction machine.

- [AsynchronousMachineDynamics](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/AsynchronousMachineDynamics/README.md). Adapted from CIM data models. Asynchronous machine whose behaviour is described by reference to a standard model expressed in either time constant reactance form or equivalent circuit form

- [AsynchronousMachineEquivalentCircuit](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/AsynchronousMachineEquivalentCircuit/README.md). Adapted from CIM data models. The electrical equations of all variations of the asynchronous model are based on the AsynchronousEquivalentCircuit diagram for the direct and quadrature axes, with two equivalent rotor windings in each axis.      =  +   =  +  *  / ( + )  =  +  * *  / ( *  +  *  +  * )  = ( + ) / ( * )  = ( *  +  *  +  * ) / ( *  * (+ ) Same equations using CIM attributes from AsynchronousMachineTimeConstantReactance class on left of = sign and AsynchronousMachineEquivalentCircuit class on right (except as noted): xs = xm + RotatingMachineDynamics.statorLeakageReactance xp = RotatingMachineDynamics.statorLeakageReactance + xm * xlr1 / (xm + xlr1) xpp = RotatingMachineDynamics.statorLeakageReactance + xm * xlr1* xlr2 / (xm * xlr1 + xm * xlr2 + xlr1 * xlr2) tpo = (xm + xlr1) / (2*pi*nominal frequency * rr1) tppo = (xm * xlr1 + xm * xlr2 + xlr1 * xlr2) / (2*pi*nominal frequency * rr2 * (xm + xlr1).

- [AsynchronousMachineTimeConstantReactance](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/AsynchronousMachineTimeConstantReactance/README.md). Adapted from CIM data models. The parameters used for models expressed in time constant reactance form include:

- [AsynchronousMachineUserDefined](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/AsynchronousMachineUserDefined/README.md). Adapted from CIM data models. Asynchronous machine whose dynamic behaviour is described by a user-defined model.

- [BaseVoltage](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/BaseVoltage/README.md). Adapted from CIM data models. Defines a system base voltage which is referenced.

- [BasicIntervalSchedule](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/BasicIntervalSchedule/README.md). Adapted from CIM data models. Schedule of values at points in time.

- [Bay](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Bay/README.md). Adapted from CIM data models. A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry.  A bay typically represents a physical grouping related to modularization of equipment.

- [BusbarSection](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/BusbarSection/README.md). Adapted from CIM data models. A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.

- [BusNameMarker](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/BusNameMarker/README.md). Adapted from CIM data models. Used to apply user standard names to topology buses. Typically used for bus/branch case generation. Associated with one or more terminals that are normally connected with the bus name. The associated terminals are normally connected by non-retained switches. For a ring bus station configuration, all busbar terminals in the ring are typically associated. For a breaker and a half scheme, both busbars would normally be associated.  For a ring bus, all busbars would normally be associated.  For a 'straight' busbar configuration, normally only the main terminal at the busbar would be associated.

- [Capacitance](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Capacitance/README.md). Adapted from CIM data models. Capacitive part of reactance (imaginary part of impedance), at rated frequency.

- [CapacitancePerLength](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/CapacitancePerLength/README.md). Adapted from CIM data models. Capacitance per unit of length.

- [Command](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Command/README.md). Adapted from CIM data models. A Command is a discrete control used for supervisory control.

- [Conductance](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Conductance/README.md). Adapted from CIM data models. Factor by which voltage must be multiplied to give corresponding power lost from a circuit. Real part of admittance.

- [ConductingEquipment](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ConductingEquipment/README.md). Adapted from CIM data models. The parts of the AC power system that are designed to carry current or that are conductively connected through terminals.

- [Conductor](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Conductor/README.md). Adapted from CIM data models. Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.

- [ConformLoad](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ConformLoad/README.md). Adapted from CIM data models. ConformLoad represent loads that follow a daily load change pattern where the pattern can be used to scale the load with a system load.

- [ConformLoadGroup](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ConformLoadGroup/README.md). Adapted from CIM data models. A group of loads conforming to an allocation pattern.

- [ConformLoadSchedule](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ConformLoadSchedule/README.md). Adapted from CIM data models. A curve of load  versus time (X-axis) showing the active power values (Y1-axis) and reactive power (Y2-axis) for each unit of the period covered. This curve represents a typical pattern of load over the time period for a given day type and season.

- [ConnectivityNode](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ConnectivityNode/README.md). Adapted from CIM data models. Connectivity nodes are points where terminals of AC conducting equipment are connected together with zero impedance.

- [ConnectivityNodeContainer](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ConnectivityNodeContainer/README.md). Adapted from CIM data models. A base class for all objects that may contain connectivity nodes or topological nodes.

- [Control](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Control/README.md). Adapted from CIM data models. Control is used for supervisory/device control. It represents control outputs that are used to change the state in a process, e.g. close or open breaker, a set point value or a raise lower command.

- [ControlArea](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ControlArea/README.md). Adapted from CIM data models. A control areais a grouping of generating units and/or loads and a cutset of tie lines (as terminals) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model.

- [ControlAreaGeneratingUnit](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ControlAreaGeneratingUnit/README.md). Adapted from CIM data models. A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit.

- [CoordinateSystem](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/CoordinateSystem/README.md). Adapted from CIM data models. Coordinate reference system.

- [CsConverter](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/CsConverter/README.md). Adapted from CIM data models. DC side of the current source converter (CSC).

- [CurrentFlow](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/CurrentFlow/README.md). Adapted from CIM data models. Electrical current with sign convention: positive flow is out of the conducting equipment into the connectivity node. Can be both AC and DC.

- [CurrentLimit](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/CurrentLimit/README.md). Adapted from CIM data models. Operational limit on current.

- [Curve](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Curve/README.md). Adapted from CIM data models. A multi-purpose curve or functional relationship between an independent variable (X-axis) and dependent (Y-axis) variables.

- [CurveData](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/CurveData/README.md). Adapted from CIM data models. Multi-purpose data points for defining a curve.  The use of this generic class is discouraged if a more specific class  can be used to specify the x and y axis values along with their specific data types.

- [DayType](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/DayType/README.md). Adapted from CIM data models. Group of similar days.   For example it could be used to represent weekdays, weekend, or holidays.

- [DCBaseTerminal](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/DCBaseTerminal/README.md). Adapted from CIM data models. An electrical connection point at a piece of DC conducting equipment. DC terminals are connected at one physical DC node that may have multiple DC terminals connected. A DC node is similar to an AC connectivity node. The model enforces that DC connections are distinct from AC connections.

- [DCConductingEquipment](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/DCConductingEquipment/README.md). Adapted from CIM data models. The parts of the DC power system that are designed to carry current or that are conductively connected through DC terminals.

- [DCConverterUnit](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/DCConverterUnit/README.md). Adapted from CIM data models. Indivisible operative unit comprising all equipment between the point of common coupling on the AC side and the point of common coupling - DC side, essentially one or more converters, together with one or more converter transformers, converter control equipment, essential protective and switching devices and auxiliaries, if any, used for conversion.

- [DCEquipmentContainer](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/DCEquipmentContainer/README.md). Adapted from CIM data models. A modeling construct to provide a root class for containment of DC as well as AC equipment. The class differ from the EquipmentContaner for AC in that it may also contain DCNodes. Hence it can contain both AC and DC equipment.

- [DCGround](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/DCGround/README.md). Adapted from CIM data models. A ground within a DC system.

- [DCLine](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/DCLine/README.md). Adapted from CIM data models. Overhead lines and/or cables connecting two or more HVDC substations.

- [DCLineSegment](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/DCLineSegment/README.md). Adapted from CIM data models. A wire or combination of wires not insulated from one another, with consistent electrical characteristics, used to carry direct current between points in the DC region of the power system.

- [DCNode](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/DCNode/README.md). Adapted from CIM data models. DC nodes are points where terminals of DC conducting equipment are connected together with zero impedance.

- [DCSeriesDevice](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/DCSeriesDevice/README.md). Adapted from CIM data models. A series device within the DC system, typically a reactor used for filtering or smoothing.  Needed for transient and short circuit studies.

- [DCShunt](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/DCShunt/README.md). Adapted from CIM data models. A shunt device within the DC system, typically used for filtering.  Needed for transient and short circuit studies.

- [DCTerminal](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/DCTerminal/README.md). Adapted from CIM data models. An electrical connection point to generic DC conducting equipment.

- [DCTopologicalIsland](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/DCTopologicalIsland/README.md). Adapted from CIM data models. An electrically connected subset of the network. DC topological islands can change as the current network state changes: e.g. due to  - disconnect switches or breakers change state in a SCADA/EMS - manual creation, change or deletion of topological nodes in a planning tool.

- [DCTopologicalNode](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/DCTopologicalNode/README.md). Adapted from CIM data models. DC bus.

- [Diagram](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Diagram/README.md). Adapted from CIM data models. The diagram being exchanged.  The coordinate system is a standard Cartesian coordinate system and the orientation attribute defines the orientation.

- [DiagramLayoutVersion](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/DiagramLayoutVersion/README.md). Adapted from CIM data models. Version details.

- [DiagramObject](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/DiagramObject/README.md). Adapted from CIM data models. An object that defines one or more points in a given space. This object can be associated with anything that specializes IdentifiedObject. For single line diagrams such objects typically include such items as analog values, breakers, disconnectors, power transformers, and transmission lines.

- [DiagramObjectGluePoint](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/DiagramObjectGluePoint/README.md). Adapted from CIM data models. This is used for grouping diagram object points from different diagram objects that are considered to be glued together in a diagram even if they are not at the exact same coordinates.

- [DiagramObjectPoint](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/DiagramObjectPoint/README.md). Adapted from CIM data models. A point in a given space defined by 3 coordinates and associated to a diagram object.  The coordinates may be positive or negative as the origin does not have to be in the corner of a diagram.

- [DiagramObjectStyle](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/DiagramObjectStyle/README.md). Adapted from CIM data models. A reference to a style used by the originating system for a diagram object.  A diagram object style describes information such as line thickness, shape such as circle or rectangle etc, and color.

- [DiagramStyle](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/DiagramStyle/README.md). Adapted from CIM data models. The diagram style refer to a style used by the originating system for a diagram.  A diagram style describes information such as schematic, geographic, bus-branch etc.

- [DiscExcContIEEEDEC1A](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/DiscExcContIEEEDEC1A/README.md). Adapted from CIM data models. The class represents IEEE Type DEC1A discontinuous excitation control model that boosts generator excitation to a level higher than that demanded by the voltage regulator and stabilizer immediately following a system fault.  Reference: IEEE Standard 421.5-2005 Section 12.2.

- [DiscExcContIEEEDEC2A](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/DiscExcContIEEEDEC2A/README.md). Adapted from CIM data models. The class represents IEEE Type DEC2A model for the discontinuous excitation control. This system provides transient excitation boosting via an open-loop control as initiated by a trigger signal generated remotely.  Reference: IEEE Standard 421.5-2005 Section 12.3.

- [DiscExcContIEEEDEC3A](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/DiscExcContIEEEDEC3A/README.md). Adapted from CIM data models. The class represents IEEE Type DEC3A model. In some systems, the stabilizer output is disconnected from the regulator immediately following a severe fault to prevent the stabilizer from competing with action of voltage regulator during the first swing.  Reference: IEEE Standard 421.5-2005 Section 12.4.

- [DiscontinuousExcitationControlDynamics](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/DiscontinuousExcitationControlDynamics/README.md). Adapted from CIM data models. Discontinuous excitation control function block whose behaviour is described by reference to a standard model .

- [DiscontinuousExcitationControlUserDefined](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/DiscontinuousExcitationControlUserDefined/README.md). Adapted from CIM data models. Discontinuous excitation control function block whose dynamic behaviour is described by

- [Discrete](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Discrete/README.md). Adapted from CIM data models. Discrete represents a discrete Measurement, i.e. a Measurement representing discrete values, e.g. a Breaker position.

- [DiscreteValue](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/DiscreteValue/README.md). Adapted from CIM data models. DiscreteValue represents a discrete MeasurementValue.

- [DynamicsFunctionBlock](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/DynamicsFunctionBlock/README.md). Adapted from CIM data models. Abstract parent class for all Dynamics function blocks.

- [DynamicsVersion](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/DynamicsVersion/README.md). Adapted from CIM data models. Version details.

- [EarthFaultCompensator](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/EarthFaultCompensator/README.md). Adapted from CIM data models. A conducting equipment used to represent a connection to ground which is typically used to compensate earth faults..   An earth fault compensator device modeled with a single terminal implies a second terminal solidly connected to ground.  If two terminals are modeled, the ground is not assumed and normal connection rules apply.

- [EnergyArea](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/EnergyArea/README.md). Adapted from CIM data models. Describes an area having energy production or consumption.  Specializations are intended to support the load allocation function as typically required in energy management systems or planning studies to allocate hypothesized load levels to individual load points for power flow analysis.  Often the energy area can be linked to both measured and forecast load levels.

- [EnergyConsumer](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/EnergyConsumer/README.md). Adapted from CIM data models. Generic user of energy - a  point of consumption on the power system model.

- [EnergySchedulingType](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/EnergySchedulingType/README.md). Adapted from CIM data models. Used to define the type of generation for scheduling purposes.

- [EnergySource](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/EnergySource/README.md). Adapted from CIM data models. A generic equivalent for an energy supplier on a transmission or distribution voltage level.

- [Equipment](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Equipment/README.md). Adapted from CIM data models. The parts of a power system that are physical devices, electronic or mechanical.

- [EquipmentBoundaryVersion](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/EquipmentBoundaryVersion/README.md). Adapted from CIM data models. Profile version details.

- [EquipmentContainer](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/EquipmentContainer/README.md). Adapted from CIM data models. A modeling construct to provide a root class for containing equipment.

- [EquipmentVersion](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/EquipmentVersion/README.md). Adapted from CIM data models. Version details.

- [EquivalentBranch](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/EquivalentBranch/README.md). Adapted from CIM data models. The class represents equivalent branches.

- [EquivalentEquipment](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/EquivalentEquipment/README.md). Adapted from CIM data models. The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of different types.

- [EquivalentInjection](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/EquivalentInjection/README.md). Adapted from CIM data models. This class represents equivalent injections (generation or load).  Voltage regulation is allowed only at the point of connection.

- [EquivalentNetwork](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/EquivalentNetwork/README.md). Adapted from CIM data models. A class that represents an external meshed network that has been reduced to an electrically equivalent model. The ConnectivityNodes contained in the equivalent are intended to reflect internal nodes of the equivalent. The boundary Connectivity nodes where the equivalent connects outside itself are NOT contained by the equivalent.

- [EquivalentShunt](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/EquivalentShunt/README.md). Adapted from CIM data models. The class represents equivalent shunts.

- [ExcAC1A](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcAC1A/README.md). Adapted from CIM data models. Modified IEEE AC1A alternator-supplied rectifier excitation system with different rate feedback source.

- [ExcAC2A](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcAC2A/README.md). Adapted from CIM data models. Modified IEEE AC2A alternator-supplied rectifier excitation system with different field current limit.

- [ExcAC3A](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcAC3A/README.md). Adapted from CIM data models. Modified IEEE AC3A alternator-supplied rectifier excitation system with different field current limit.

- [ExcAC4A](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcAC4A/README.md). Adapted from CIM data models. Modified IEEE AC4A alternator-supplied rectifier excitation system with different minimum controller output.

- [ExcAC5A](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcAC5A/README.md). Adapted from CIM data models. Modified IEEE AC5A alternator-supplied rectifier excitation system with different minimum controller output.

- [ExcAC6A](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcAC6A/README.md). Adapted from CIM data models. Modified IEEE AC6A alternator-supplied rectifier excitation system with speed input.

- [ExcAC8B](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcAC8B/README.md). Adapted from CIM data models. Modified IEEE AC8B alternator-supplied rectifier excitation system with speed input and input limiter.

- [ExcANS](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcANS/README.md). Adapted from CIM data models. Italian excitation system. It represents static field voltage or excitation current feedback excitation system.

- [ExcAVR1](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcAVR1/README.md). Adapted from CIM data models. Italian excitation system corresponding to IEEE (1968) Type 1 Model. It represents exciter dynamo and electromechanical regulator.

- [ExcAVR2](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcAVR2/README.md). Adapted from CIM data models. Italian excitation system corresponding to IEEE (1968) Type 2 Model. It represents alternator and rotating diodes and electromechanic voltage regulators.

- [ExcAVR3](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcAVR3/README.md). Adapted from CIM data models. Italian excitation system. It represents exciter dynamo and electric regulator.

- [ExcAVR4](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcAVR4/README.md). Adapted from CIM data models. Italian excitation system. It represents static exciter and electric voltage regulator.

- [ExcAVR5](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcAVR5/README.md). Adapted from CIM data models. Manual excitation control with field circuit resistance. This model can be used as a very simple representation of manual voltage control.

- [ExcAVR7](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcAVR7/README.md). Adapted from CIM data models. IVO excitation system.

- [ExcBBC](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcBBC/README.md). Adapted from CIM data models. Transformer fed static excitation system (static with ABB regulator). This model represents a static excitation system in which a gated thyristor bridge fed by a transformer at the main generator terminals feeds the main generator directly.

- [ExcCZ](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcCZ/README.md). Adapted from CIM data models. Czech Proportion/Integral Exciter.

- [ExcDC1A](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcDC1A/README.md). Adapted from CIM data models. Modified IEEE DC1A direct current commutator exciter with speed input and without underexcitation limiters (UEL) inputs.

- [ExcDC2A](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcDC2A/README.md). Adapted from CIM data models. Modified IEEE DC2A direct current commutator exciters with speed input, one more leg block in feedback loop and without underexcitation limiters (UEL) inputs.  DC type 2 excitation system model with added speed multiplier, added lead-lag, and voltage-dependent limits.

- [ExcDC3A](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcDC3A/README.md). Adapted from CIM data models. This is modified IEEE DC3A direct current commutator exciters with speed input, and death band.  DC old type 4.

- [ExcDC3A1](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcDC3A1/README.md). Adapted from CIM data models. This is modified old IEEE type 3 excitation system.

- [ExcELIN1](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcELIN1/README.md). Adapted from CIM data models. Static PI transformer fed excitation system: ELIN (VATECH) - simplified model.  This model represents an all-static excitation system. A PI voltage controller establishes a desired field current set point for a proportional current controller. The integrator of the PI controller has a follow-up input to match its signal to the present field current.  A power system stabilizer with power input is included in the model.

- [ExcELIN2](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcELIN2/README.md). Adapted from CIM data models. Detailed Excitation System Model - ELIN (VATECH).  This model represents an all-static excitation system. A PI voltage controller establishes a desired field current set point for a proportional current controller. The integrator of the PI controller has a follow-up input to match its signal to the present field current.  Power system stabilizer models used in conjunction with this excitation system model: PssELIN2, PssIEEE2B, Pss2B.

- [ExcHU](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcHU/README.md). Adapted from CIM data models. Hungarian Excitation System Model, with built-in voltage transducer.

- [ExcIEEEAC1A](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcIEEEAC1A/README.md). Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type AC1A model. The model represents the field-controlled alternator-rectifier excitation systems designated Type AC1A. These excitation systems consist of an alternator main exciter with non-controlled rectifiers.  Reference: IEEE Standard 421.5-2005 Section 6.1.

- [ExcIEEEAC2A](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcIEEEAC2A/README.md). Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type AC2A model. The model represents a high initial response field-controlled alternator-rectifier excitation system. The alternator main exciter is used with non-controlled rectifiers. The Type AC2A model is similar to that of Type AC1A except for the inclusion of exciter time constant compensation and exciter field current limiting elements.  Reference: IEEE Standard 421.5-2005 Section 6.2.

- [ExcIEEEAC3A](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcIEEEAC3A/README.md). Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type AC3A model. The model represents the field-controlled alternator-rectifier excitation systems designated Type AC3A. These excitation systems include an alternator main exciter with non-controlled rectifiers. The exciter employs self-excitation, and the voltage regulator power is derived from the exciter output voltage.  Therefore, this system has an additional nonlinearity, simulated by the use of a multiplier whose inputs are the voltage regulator command signal, , and the exciter output voltage, , times .  This model is applicable to excitation systems employing static voltage regulators.   Reference: IEEE Standard 421.5-2005 Section 6.3.

- [ExcIEEEAC4A](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcIEEEAC4A/README.md). Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type AC4A model. The model represents type AC4A alternator-supplied controlled-rectifier excitation system which is quite different from the other type ac systems. This high initial response excitation system utilizes a full thyristor bridge in the exciter output circuit.  The voltage regulator controls the firing of the thyristor bridges. The exciter alternator uses an independent voltage regulator to control its output voltage to a constant value. These effects are not modeled; however, transient loading effects on the exciter alternator are included.   Reference: IEEE Standard 421.5-2005 Section 6.4.

- [ExcIEEEAC5A](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcIEEEAC5A/README.md). Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type AC5A model. The model represents a simplified model for brushless excitation systems. The regulator is supplied from a source, such as a permanent magnet generator, which is not affected by system disturbances.  Unlike other ac models, this model uses loaded rather than open circuit exciter saturation data in the same way as it is used for the dc models.  Because the model has been widely implemented by the industry, it is sometimes used to represent other types of systems when either detailed data for them are not available or simplified models are required.   Reference: IEEE Standard 421.5-2005 Section 6.5.

- [ExcIEEEAC6A](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcIEEEAC6A/README.md). Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type AC6A model. The model represents field-controlled alternator-rectifier excitation systems with system-supplied electronic voltage regulators.  The maximum output of the regulator, , is a function of terminal voltage, . The field current limiter included in the original model AC6A remains in the 2005 update.  Reference: IEEE Standard 421.5-2005 Section 6.6.

- [ExcIEEEAC7B](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcIEEEAC7B/README.md). Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type AC7B model. The model represents excitation systems which consist of an ac alternator with either stationary or rotating rectifiers to produce the dc field requirements. It is an upgrade to earlier ac excitation systems, which replace only the controls but retain the ac alternator and diode rectifier bridge.  Reference: IEEE Standard 421.5-2005 Section 6.7.  In the IEEE Standard 421.5 - 2005, the [1 / sT] block is shown as [1 / (1 + sT)], which is incorrect.

- [ExcIEEEAC8B](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcIEEEAC8B/README.md). Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type AC8B model. This model represents a PID voltage regulator with either a brushless exciter or dc exciter. The AVR in this model consists of PID control, with separate constants for the proportional (), integral (), and derivative () gains. The representation of the brushless exciter (, , , , ) is similar to the model Type AC2A. The Type AC8B model can be used to represent static voltage regulators applied to brushless excitation systems. Digitally based voltage regulators feeding dc rotating main exciters can be represented with the AC Type AC8B model with the parameters  and  set to 0.  For thyristor power stages fed from the generator terminals, the limits  and  should be a function of terminal voltage:  * and  * .     Reference: IEEE Standard 421.5-2005 Section 6.8.

- [ExcIEEEDC1A](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcIEEEDC1A/README.md). Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type DC1A model. This model represents field-controlled dc commutator exciters with continuously acting voltage regulators (especially the direct-acting rheostatic, rotating amplifier, and magnetic amplifier types).  Because this model has been widely implemented by the industry, it is sometimes used to represent other types of systems when detailed data for them are not available or when a simplified model is required.   Reference: IEEE Standard 421.5-2005 Section 5.1.

- [ExcIEEEDC2A](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcIEEEDC2A/README.md). Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type DC2A model. This model represents represent field-controlled dc commutator exciters with continuously acting voltage regulators having supplies obtained from the generator or auxiliary bus.  It differs from the Type DC1A model only in the voltage regulator output limits, which are now proportional to terminal voltage . It is representative of solid-state replacements for various forms of older mechanical and rotating amplifier regulating equipment connected to dc commutator exciters.  Reference: IEEE Standard 421.5-2005 Section 5.2.

- [ExcIEEEDC3A](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcIEEEDC3A/README.md). Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type DC3A model. This model represents represent older systems, in particular those dc commutator exciters with non-continuously acting regulators that were commonly used before the development of the continuously acting varieties.  These systems respond at basically two different rates, depending upon the magnitude of voltage error. For small errors, adjustment is made periodically with a signal to a motor-operated rheostat. Larger errors cause resistors to be quickly shorted or inserted and a strong forcing signal applied to the exciter. Continuous motion of the motor-operated rheostat occurs for these larger error signals, even though it is bypassed by contactor action.   Reference: IEEE Standard 421.5-2005 Section 5.3.

- [ExcIEEEDC4B](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcIEEEDC4B/README.md). Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type DC4B model. These excitation systems utilize a field-controlled dc commutator exciter with a continuously acting voltage regulator having supplies obtained from the generator or auxiliary bus.  Reference: IEEE Standard 421.5-2005 Section 5.4.

- [ExcIEEEST1A](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcIEEEST1A/README.md). Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type ST1A model. This model represents systems in which excitation power is supplied through a transformer from the generator terminals (or the unit's auxiliary bus) and is regulated by a controlled rectifier.  The maximum exciter voltage available from such systems is directly related to the generator terminal voltage.  Reference: IEEE Standard 421.5-2005 Section 7.1.

- [ExcIEEEST2A](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcIEEEST2A/README.md). Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type ST2A model. Some static systems utilize both current and voltage sources (generator terminal quantities) to comprise the power source.  The regulator controls the exciter output through controlled saturation of the power transformer components.  These compound-source rectifier excitation systems are designated Type ST2A and are represented by ExcIEEEST2A.  Reference: IEEE Standard 421.5-2005 Section 7.2.

- [ExcIEEEST3A](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcIEEEST3A/README.md). Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type ST3A model.  Some static systems utilize a field voltage control loop to linearize the exciter control characteristic. This also makes the output independent of supply source variations until supply limitations are reached.  These systems utilize a variety of controlled-rectifier designs: full thyristor complements or hybrid bridges in either series or shunt configurations. The power source may consist of only a potential source, either fed from the machine terminals or from internal windings. Some designs may have compound power sources utilizing both machine potential and current. These power sources are represented as phasor combinations of machine terminal current and voltage and are accommodated by suitable parameters in model Type ST3A which is represented by ExcIEEEST3A.   Reference: IEEE Standard 421.5-2005 Section 7.3.

- [ExcIEEEST4B](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcIEEEST4B/README.md). Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type ST4B model. This model is a variation of the Type ST3A model, with a proportional plus integral (PI) regulator block replacing the lag-lead regulator characteristic that is in the ST3A model. Both potential and compound source rectifier excitation systems are modeled.  The PI regulator blocks have non-windup limits that are represented. The voltage regulator of this model is typically implemented digitally.  Reference: IEEE Standard 421.5-2005 Section 7.4.

- [ExcIEEEST5B](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcIEEEST5B/README.md). Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type ST5B model. The Type ST5B excitation system is a variation of the Type ST1A model, with alternative overexcitation and underexcitation inputs and additional limits.  Reference: IEEE Standard 421.5-2005 Section 7.5.   Note: the block diagram in the IEEE 421.5 standard has input signal Vc and does not indicate the summation point with Vref. The implementation of the ExcIEEEST5B shall consider summation point with Vref.

- [ExcIEEEST6B](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcIEEEST6B/README.md). Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type ST6B model. This model consists of a PI voltage regulator with an inner loop field voltage regulator and pre-control. The field voltage regulator implements a proportional control. The pre-control and the delay in the feedback circuit increase the dynamic response.  Reference: IEEE Standard 421.5-2005 Section 7.6.

- [ExcIEEEST7B](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcIEEEST7B/README.md). Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type ST7B model. This model is representative of static potential-source excitation systems. In this system, the AVR consists of a PI voltage regulator. A phase lead-lag filter in series allows introduction of a derivative function, typically used with brushless excitation systems. In that case, the regulator is of the PID type. In addition, the terminal voltage channel includes a phase lead-lag filter.  The AVR includes the appropriate inputs on its reference for overexcitation limiter (OEL1), underexcitation limiter (UEL), stator current limiter (SCL), and current compensator (DROOP). All these limitations, when they work at voltage reference level, keep the PSS (VS signal from Type PSS1A, PSS2A, or PSS2B) in operation. However, the UEL limitation can also be transferred to the high value (HV) gate acting on the output signal. In addition, the output signal passes through a low value (LV) gate for a ceiling overexcitation limiter (OEL2).  Reference: IEEE Standard 421.5-2005 Section 7.7.

- [ExcitationSystemDynamics](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcitationSystemDynamics/README.md). Adapted from CIM data models. Excitation system function block whose behavior is described by reference to a standard model

- [ExcitationSystemUserDefined](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcitationSystemUserDefined/README.md). Adapted from CIM data models. Excitation system function block whose dynamic behaviour is described by

- [ExcOEX3T](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcOEX3T/README.md). Adapted from CIM data models. Modified IEEE Type ST1 Excitation System with semi-continuous and acting terminal voltage limiter.

- [ExcPIC](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcPIC/README.md). Adapted from CIM data models. Proportional/Integral Regulator Excitation System Model.  This model can be used to represent excitation systems with a proportional-integral (PI) voltage regulator controller.

- [ExcREXS](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcREXS/README.md). Adapted from CIM data models. General Purpose Rotating Excitation System Model.  This model can be used to represent a wide range of excitation systems whose DC power source is an AC or DC generator. It encompasses IEEE type AC1, AC2, DC1, and DC2 excitation system models.

- [ExcSCRX](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcSCRX/README.md). Adapted from CIM data models. Simple excitation system model representing generic characteristics of many excitation systems; intended for use where negative field current may be a problem.

- [ExcSEXS](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcSEXS/README.md). Adapted from CIM data models. Simplified Excitation System Model.

- [ExcSK](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcSK/README.md). Adapted from CIM data models. Slovakian Excitation System Model.  UEL and secondary voltage control are included in this model. When this model is used, there cannot be a separate underexcitation limiter or VAr controller model.

- [ExcST1A](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcST1A/README.md). Adapted from CIM data models. Modification of an old IEEE ST1A static excitation system without overexcitation limiter (OEL) and underexcitation limiter (UEL).

- [ExcST2A](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcST2A/README.md). Adapted from CIM data models. Modified IEEE ST2A static excitation system - another lead-lag block added to match  the model defined by WECC.

- [ExcST3A](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcST3A/README.md). Adapted from CIM data models. Modified IEEE ST3A static excitation system with added speed multiplier.

- [ExcST4B](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcST4B/README.md). Adapted from CIM data models. Modified IEEE ST4B static excitation system with maximum inner loop feedback gain .

- [ExcST6B](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcST6B/README.md). Adapted from CIM data models. Modified IEEE ST6B static excitation system with PID controller and optional inner feedbacks loop.

- [ExcST7B](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExcST7B/README.md). Adapted from CIM data models. Modified IEEE ST7B static excitation system without stator current limiter (SCL) and current compensator (DROOP) inputs.

- [ExternalNetworkInjection](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ExternalNetworkInjection/README.md). Adapted from CIM data models. This class represents external network and it is used for IEC 60909 calculations.

- [FossilFuel](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/FossilFuel/README.md). Adapted from CIM data models. The fossil fuel consumed by the non-nuclear thermal generating unit.   For example, coal, oil, gas, etc.   This a the specific fuels that the generating unit can consume.

- [Frequency](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Frequency/README.md). Adapted from CIM data models. Cycles per second.

- [GeneratingUnit](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GeneratingUnit/README.md). Adapted from CIM data models. A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.

- [GenICompensationForGenJ](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GenICompensationForGenJ/README.md). Adapted from CIM data models. This class provides the resistive and reactive components of compensation for the generator associated with the IEEE Type 2 voltage compensator for current flow out of one of the other generators in the interconnection.

- [GeographicalLocationVersion](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GeographicalLocationVersion/README.md). Adapted from CIM data models. Version details.

- [GeographicalRegion](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GeographicalRegion/README.md). Adapted from CIM data models. A geographical region of a power system network model.

- [GovCT1](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovCT1/README.md). Adapted from CIM data models. General model for any prime mover with a PID governor, used primarily for combustion turbine and combined cycle units. This model can be used to represent a variety of prime movers controlled by PID governors.  It is suitable, for example, for representation of     Additional information on this model is available in the 2012 IEEE report, , section 3.1.2.3 page 3-4 (GGOV1).

- [GovCT2](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovCT2/README.md). Adapted from CIM data models. General governor model with frequency-dependent fuel flow limit.  This model is a modification of the GovCT1model in order to represent the frequency-dependent fuel flow limit of a specific gas turbine manufacturer.

- [GovGAST](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovGAST/README.md). Adapted from CIM data models. Single shaft gas turbine.

- [GovGAST1](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovGAST1/README.md). Adapted from CIM data models. Modified single shaft gas turbine.

- [GovGAST2](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovGAST2/README.md). Adapted from CIM data models. Gas turbine model.

- [GovGAST3](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovGAST3/README.md). Adapted from CIM data models. Generic turbogas with acceleration and temperature controller.

- [GovGAST4](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovGAST4/README.md). Adapted from CIM data models. Generic turbogas.

- [GovGASTWD](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovGASTWD/README.md). Adapted from CIM data models. Woodward Gas turbine governor model.

- [GovHydro1](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovHydro1/README.md). Adapted from CIM data models. Basic Hydro turbine governor model.

- [GovHydro2](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovHydro2/README.md). Adapted from CIM data models. IEEE hydro turbine governor model represents plants with straightforward penstock configurations and hydraulic-dashpot governors.

- [GovHydro3](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovHydro3/README.md). Adapted from CIM data models. Modified IEEE Hydro Governor-Turbine Model.  This model differs from that defined in the IEEE modeling guideline paper in that the limits on gate position and velocity do not permit wind up of the upstream signals.

- [GovHydro4](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovHydro4/README.md). Adapted from CIM data models. Hydro turbine and governor. Represents plants with straight-forward penstock configurations and hydraulic governors of traditional 'dashpot' type.  This model can be used to represent simple, Francis, Pelton or Kaplan turbines.

- [GovHydroDD](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovHydroDD/README.md). Adapted from CIM data models. Double derivative hydro governor and turbine.

- [GovHydroFrancis](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovHydroFrancis/README.md). Adapted from CIM data models. Detailed hydro unit - Francis model.  This model can be used to represent three types of governors. A schematic of the hydraulic system of detailed hydro unit models, like Francis and Pelton, is provided in the DetailedHydroModelHydraulicSystem diagram.

- [GovHydroIEEE0](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovHydroIEEE0/README.md). Adapted from CIM data models. IEEE Simplified Hydro Governor-Turbine Model.  Used for Mechanical-Hydraulic and Electro-Hydraulic turbine governors, with our without steam feedback. Typical values given are for Mechanical-Hydraulic.  Ref

- [GovHydroIEEE2](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovHydroIEEE2/README.md). Adapted from CIM data models. IEEE hydro turbine governor model represents plants with straightforward penstock configurations and hydraulic-dashpot governors.  Ref

- [GovHydroPelton](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovHydroPelton/README.md). Adapted from CIM data models. Detailed hydro unit - Pelton model.  This model can be used to represent the dynamic related to water tunnel and surge chamber. A schematic of the hydraulic system of detailed hydro unit models, like Francis and Pelton, is located under the GovHydroFrancis class.

- [GovHydroPID](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovHydroPID/README.md). Adapted from CIM data models. PID governor and turbine.

- [GovHydroPID2](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovHydroPID2/README.md). Adapted from CIM data models. Hydro turbine and governor. Represents plants with straight forward penstock configurations and three term electro-hydraulic governors (i.e. Woodard electronic).

- [GovHydroR](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovHydroR/README.md). Adapted from CIM data models. Fourth order lead-lag governor and hydro turbine.

- [GovHydroWEH](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovHydroWEH/README.md). Adapted from CIM data models. Woodward Electric Hydro Governor Model.

- [GovHydroWPID](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovHydroWPID/README.md). Adapted from CIM data models. Woodward PID Hydro Governor.

- [GovSteam0](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovSteam0/README.md). Adapted from CIM data models. A simplified steam turbine governor model.

- [GovSteam1](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovSteam1/README.md). Adapted from CIM data models. Steam turbine governor model, based on the GovSteamIEEE1 model  (with optional deadband and nonlinear valve gain added).

- [GovSteam2](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovSteam2/README.md). Adapted from CIM data models. Simplified governor model.

- [GovSteamCC](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovSteamCC/README.md). Adapted from CIM data models. Cross compound turbine governor model.

- [GovSteamEU](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovSteamEU/README.md). Adapted from CIM data models. Simplified model  of boiler and steam turbine with PID governor.

- [GovSteamFV2](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovSteamFV2/README.md). Adapted from CIM data models. Steam turbine governor with reheat time constants and modeling of the effects of fast valve closing to reduce mechanical power.

- [GovSteamFV3](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovSteamFV3/README.md). Adapted from CIM data models. Simplified GovSteamIEEE1 Steam turbine governor model with Prmax limit and fast valving.

- [GovSteamFV4](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovSteamFV4/README.md). Adapted from CIM data models. Detailed electro-hydraulic governor for steam unit.

- [GovSteamIEEE1](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovSteamIEEE1/README.md). Adapted from CIM data models. IEEE steam turbine governor model.  Ref

- [GovSteamSGO](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GovSteamSGO/README.md). Adapted from CIM data models. Simplified Steam turbine governor model.

- [GrossToNetActivePowerCurve](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GrossToNetActivePowerCurve/README.md). Adapted from CIM data models. Relationship between the generating unit's gross active power output on the X-axis (measured at the terminals of the machine(s)) and the generating unit's net active power output on the Y-axis (based on utility-defined measurements at the power station). Station service loads, when modeled, should be treated as non-conforming bus loads. There may be more than one curve, depending on the auxiliary equipment that is in service.

- [GroundingImpedance](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/GroundingImpedance/README.md). Adapted from CIM data models. A fixed impedance device used for grounding.

- [HydroGeneratingUnit](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/HydroGeneratingUnit/README.md). Adapted from CIM data models. A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan).

- [HydroPowerPlant](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/HydroPowerPlant/README.md). Adapted from CIM data models. A hydro power station which can generate or pump. When generating, the generator turbines receive water from an upper reservoir. When pumping, the pumps receive their water from a lower reservoir.

- [HydroPump](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/HydroPump/README.md). Adapted from CIM data models. A synchronous motor-driven pump, typically associated with a pumped storage plant.

- [IdentifiedObject](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/IdentifiedObject/README.md). Adapted from CIM data models. This is a root class to provide common identification for all classes needing identification and naming attributes.

- [Inductance](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Inductance/README.md). Adapted from CIM data models. Inductive part of reactance (imaginary part of impedance), at rated frequency.

- [InductancePerLength](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/InductancePerLength/README.md). Adapted from CIM data models. Inductance per unit of length.

- [Length](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Length/README.md). Adapted from CIM data models. Unit of length. Never negative.

- [LimitSet](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/LimitSet/README.md). Adapted from CIM data models. Specifies a set of Limits that are associated with a Measurement. A Measurement may have several LimitSets corresponding to seasonal or other changing conditions. The condition is captured in the name and description attributes. The same LimitSet may be used for several Measurements. In particular percentage limits are used this way.

- [Line](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Line/README.md). Adapted from CIM data models. Contains equipment beyond a substation belonging to a power transmission line.

- [LinearShuntCompensator](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/LinearShuntCompensator/README.md). Adapted from CIM data models. A linear shunt compensator has banks or sections with equal admittance values.

- [LoadAggregate](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/LoadAggregate/README.md). Adapted from CIM data models. Standard aggregate load model comprised of static and/or dynamic components.  A static load model represents the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage. A dynamic load model can used to represent the aggregate response of the motor components of the load.

- [LoadArea](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/LoadArea/README.md). Adapted from CIM data models. The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.

- [LoadComposite](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/LoadComposite/README.md). Adapted from CIM data models. This models combines static load and induction motor load effects. The dynamics of the motor are simplified by linearizing the induction machine equations.

- [LoadDynamics](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/LoadDynamics/README.md). Adapted from CIM data models. Load whose behaviour is described by reference to a standard model   A standard feature of dynamic load behaviour modelling is the ability to associate the same behaviour to multiple energy consumers by means of a single aggregate load definition.  Aggregate loads are used to represent all or part of the real and reactive load from one or more loads in the static (power flow) data. This load is usually the aggregation of many individual load devices and the load model is approximate representation of the aggregate response of the load devices to system disturbances. The load model is always applied to individual bus loads (energy consumers) but a single set of load model parameters can used for all loads in the grouping.

- [LoadGenericNonLinear](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/LoadGenericNonLinear/README.md). Adapted from CIM data models. These load models (known also as generic non-linear dynamic (GNLD) load models) can be used in mid-term and long-term voltage stability simulations (i.e., to study voltage collapse), as they can replace a more detailed representation of aggregate load, including induction motors, thermostatically controlled and static loads.

- [LoadGroup](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/LoadGroup/README.md). Adapted from CIM data models. The class is the third level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.

- [LoadMotor](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/LoadMotor/README.md). Adapted from CIM data models. Aggregate induction motor load. This model  is used to represent a fraction of an ordinary load as induction motor load.  It allows load that is treated as ordinary constant power in power flow analysis to be represented by an induction motor in dynamic simulation.  If  = 0. or  = , or  = 0.,  only one cage is represented. Magnetic saturation is not modelled. Either a 'one-cage' or 'two-cage' model of the induction machine can be modelled. Magnetic saturation is not modelled.  This model is intended for representation of aggregations of many motors dispersed through a load represented at a high voltage bus but where there is no information on the characteristics of individual motors.  This model treats a fraction of the constant power part of a load as a motor. During initialisation, the initial power drawn by the motor is set equal to  times the constant  part of the static load.  The remainder of the load is left as static load.  The reactive power demand of the motor is calculated during initialisation as a function of voltage at the load bus. This reactive power demand may be less than or greater than the constant  component of the load.  If the motor's reactive demand is greater than the constant  component of the load, the model inserts a shunt capacitor at the terminal of the motor to bring its reactive demand down to equal the constant  reactive load.   If a motor model and a static load model are both present for a load, the motor  is assumed to be subtracted from the power flow constant  load before the static load model is applied.  The remainder of the load, if any, is then represented by the static load model.

- [LoadResponseCharacteristic](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/LoadResponseCharacteristic/README.md). Adapted from CIM data models. Models the characteristic response of the load demand due to changes in system conditions such as voltage and frequency. This is not related to demand response.  If LoadResponseCharacteristic.exponentModel is True, the voltage exponents are specified and used as to calculate:  Active power component = Pnominal * (Voltage/cim:BaseVoltage.nominalVoltage) ** cim:LoadResponseCharacteristic.pVoltageExponent  Reactive power component = Qnominal * (Voltage/cim:BaseVoltage.nominalVoltage)** cim:LoadResponseCharacteristic.qVoltageExponent  Where  * means 'multiply' and ** is 'raised to power of'.

- [LoadStatic](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/LoadStatic/README.md). Adapted from CIM data models. General static load model representing the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage.

- [LoadUserDefined](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/LoadUserDefined/README.md). Adapted from CIM data models. Load whose dynamic behaviour is described by a user-defined model.

- [Location](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Location/README.md). Adapted from CIM data models. The place, scene, or point of something where someone or something has been, is, and/or will be at a given moment in time. It can be defined with one or more postition points (coordinates) in a given coordinate system.

- [Measurement](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Measurement/README.md). Adapted from CIM data models. A Measurement represents any measured, calculated or non-measured non-calculated quantity. Any piece of equipment may contain Measurements, e.g. a substation may have temperature measurements and door open indications, a transformer may have oil temperature and tank pressure measurements, a bay may contain a number of power flow measurements and a Breaker may contain a switch status measurement.  The PSR - Measurement association is intended to capture this use of Measurement and is included in the naming hierarchy based on EquipmentContainer. The naming hierarchy typically has Measurements as leafs, e.g. Substation-VoltageLevel-Bay-Switch-Measurement. Some Measurements represent quantities related to a particular sensor location in the network, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is not captured in the PSR - Measurement association. Instead it is captured by the Measurement - Terminal association that is used to define the sensing location in the network topology. The location is defined by the connection of the Terminal to ConductingEquipment.  If both a Terminal and PSR are associated, and the PSR is of type ConductingEquipment, the associated Terminal should belong to that ConductingEquipment instance. When the sensor location is needed both Measurement-PSR and Measurement-Terminal are used. The Measurement-Terminal association is never used alone.

- [MeasurementValue](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/MeasurementValue/README.md). Adapted from CIM data models. The current state for a measurement. A state value is an instance of a measurement from a specific source. Measurements can be associated with many state values, each representing a different source for the measurement.

- [MeasurementValueQuality](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/MeasurementValueQuality/README.md). Adapted from CIM data models. Measurement quality flags. Bits 0-10 are defined for substation automation in draft IEC 61850 part 7-3. Bits 11-15 are reserved for future expansion by that document. Bits 16-31 are reserved for EMS applications.

- [MeasurementValueSource](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/MeasurementValueSource/README.md). Adapted from CIM data models. MeasurementValueSource describes the alternative sources updating a MeasurementValue. User conventions for how to use the MeasurementValueSource attributes are described in the introduction to IEC 61970-301.

- [MechanicalLoadDynamics](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/MechanicalLoadDynamics/README.md). Adapted from CIM data models. Mechanical load function block whose behavior is described by reference to a standard model

- [MechanicalLoadUserDefined](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/MechanicalLoadUserDefined/README.md). Adapted from CIM data models. Mechanical load function block whose dynamic behaviour is described by

- [MechLoad1](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/MechLoad1/README.md). Adapted from CIM data models. Mechanical load model type 1.

- [Money](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Money/README.md). Adapted from CIM data models. Amount of money.

- [MutualCoupling](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/MutualCoupling/README.md). Adapted from CIM data models. This class represents the zero sequence line mutual coupling.

- [NonConformLoad](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/NonConformLoad/README.md). Adapted from CIM data models. NonConformLoad represent loads that do not follow a daily load change pattern and changes are not correlated with the daily load change pattern.

- [NonConformLoadGroup](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/NonConformLoadGroup/README.md). Adapted from CIM data models. Loads that do not follow a daily and seasonal load variation pattern.

- [NonConformLoadSchedule](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/NonConformLoadSchedule/README.md). Adapted from CIM data models. An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves) versus time (X-axis) for non-conforming loads, e.g., large industrial load or power station service (where modeled).

- [NonlinearShuntCompensator](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/NonlinearShuntCompensator/README.md). Adapted from CIM data models. A non linear shunt compensator has bank or section admittance values that differs.

- [NonlinearShuntCompensatorPoint](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/NonlinearShuntCompensatorPoint/README.md). Adapted from CIM data models. A non linear shunt compensator bank or section admittance value.

- [OperationalLimit](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/OperationalLimit/README.md). Adapted from CIM data models. A value associated with a specific kind of limit.  The sub class value attribute shall be positive.  The sub class value attribute is inversely proportional to OperationalLimitType.acceptableDuration (acceptableDuration for short). A pair of value_x and acceptableDuration_x are related to each other as follows: if value_1 > value_2 > value_3 >... then acceptableDuration_1 < acceptableDuration_2 < acceptableDuration_3 < ... A value_x with direction='high' shall be greater than a value_y with direction='low'.

- [OperationalLimitSet](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/OperationalLimitSet/README.md). Adapted from CIM data models. A set of limits associated with equipment.  Sets of limits might apply to a specific temperature, or season for example. A set of limits may contain different severities of limit levels that would apply to the same equipment. The set may contain limits of different types such as apparent power and current limits or high and low voltage limits  that are logically applied together as a set.

- [OperationalLimitType](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/OperationalLimitType/README.md). Adapted from CIM data models. The operational meaning of a category of limits.

- [OverexcitationLimiterDynamics](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/OverexcitationLimiterDynamics/README.md). Adapted from CIM data models. Overexcitation limiter function block whose behaviour is described by reference to a standard model

- [OverexcitationLimiterUserDefined](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/OverexcitationLimiterUserDefined/README.md). Adapted from CIM data models. Overexcitation limiter system function block whose dynamic behaviour is described by

- [OverexcLim2](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/OverexcLim2/README.md). Adapted from CIM data models. Different from LimIEEEOEL, LimOEL2 has a fixed pickup threshold and reduces the excitation set-point by mean of non-windup integral regulator. Irated is the rated machine excitation current (calculated from nameplate conditions: V, P, CosPhi).

- [OverexcLimIEEE](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/OverexcLimIEEE/README.md). Adapted from CIM data models. The over excitation limiter model is intended to represent the significant features of OELs necessary for some large-scale system studies. It is the result of a pragmatic approach to obtain a model that can be widely applied with attainable data from generator owners. An attempt to include all variations in the functionality of OELs and duplicate how they interact with the rest of the excitation systems would likely result in a level of application insufficient for the studies for which they are intended.  Reference: IEEE OEL 421.5-2005 Section 9.

- [OverexcLimX1](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/OverexcLimX1/README.md). Adapted from CIM data models. Field voltage over excitation limiter.

- [OverexcLimX2](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/OverexcLimX2/README.md). Adapted from CIM data models. Field Voltage or Current overexcitation limiter designed to protect the generator field of an AC machine with automatic excitation control from overheating due to prolonged overexcitation.

- [PerCent](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PerCent/README.md). Adapted from CIM data models. Percentage on a defined base.   For example, specify as 100 to indicate at the defined base.

- [PerLengthDCLineParameter](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PerLengthDCLineParameter/README.md). Adapted from CIM data models. 

- [PetersenCoil](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PetersenCoil/README.md). Adapted from CIM data models. A tunable impedance device normally used to offset line charging during single line faults in an ungrounded section of network.

- [PFVArControllerType1Dynamics](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PFVArControllerType1Dynamics/README.md). Adapted from CIM data models. Power Factor or VAr controller Type I function block whose behaviour is described by reference to a standard model

- [PFVArControllerType1UserDefined](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PFVArControllerType1UserDefined/README.md). Adapted from CIM data models. Power Factor or VAr controller Type I function block whose dynamic behaviour is described by

- [PFVArControllerType2Dynamics](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PFVArControllerType2Dynamics/README.md). Adapted from CIM data models. Power Factor or VAr controller Type II function block whose behaviour is described by reference to a standard model

- [PFVArControllerType2UserDefined](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PFVArControllerType2UserDefined/README.md). Adapted from CIM data models. Power Factor or VAr controller Type II function block whose dynamic behaviour is described by

- [PFVArType1IEEEPFController](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PFVArType1IEEEPFController/README.md). Adapted from CIM data models. The class represents IEEE PF Controller Type 1 which operates by moving the voltage reference directly.  Reference: IEEE Standard 421.5-2005 Section 11.2.

- [PFVArType1IEEEVArController](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PFVArType1IEEEVArController/README.md). Adapted from CIM data models. The class represents IEEE VAR Controller Type 1 which operates by moving the voltage reference directly.  Reference: IEEE Standard 421.5-2005 Section 11.3.

- [PFVArType2Common1](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PFVArType2Common1/README.md). Adapted from CIM data models. Power factor / Reactive power regulator. This model represents the power factor or reactive power controller such as the Basler SCP-250. The controller measures power factor or reactive power (PU on generator rated power) and compares it with the operator's set point.

- [PFVArType2IEEEPFController](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PFVArType2IEEEPFController/README.md). Adapted from CIM data models. The class represents IEEE PF Controller Type 2 which is a summing point type controller and makes up the outside loop of a two-loop system. This controller is implemented as a slow PI type controller. The voltage regulator forms the inner loop and is implemented as a fast controller.  Reference: IEEE Standard 421.5-2005 Section 11.4.

- [PFVArType2IEEEVArController](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PFVArType2IEEEVArController/README.md). Adapted from CIM data models. The class represents IEEE VAR Controller Type 2 which is a summing point type controller. It makes up the outside loop of a two-loop system. This controller is implemented as a slow PI type controller, and the voltage regulator forms the inner loop and is implemented as a fast controller.  Reference: IEEE Standard 421.5-2005 Section 11.5.

- [PhaseTapChanger](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PhaseTapChanger/README.md). Adapted from CIM data models. A transformer phase shifting tap model that controls the phase angle difference across the power transformer and potentially the active power flow through the power transformer.  This phase tap model may also impact the voltage magnitude.

- [PhaseTapChangerAsymmetrical](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PhaseTapChangerAsymmetrical/README.md). Adapted from CIM data models. Describes the tap model for an asymmetrical phase shifting transformer in which the difference voltage vector adds to the primary side voltage. The angle between the primary side voltage and the difference voltage is named the winding connection angle. The phase shift depends on both the difference voltage magnitude and the winding connection angle.

- [PhaseTapChangerLinear](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PhaseTapChangerLinear/README.md). Adapted from CIM data models. Describes a tap changer with a linear relation between the tap step and the phase angle difference across the transformer. This is a mathematical model that is an approximation of a real phase tap changer. The phase angle is computed as stepPhaseShitfIncrement times the tap position. The secondary side voltage magnitude is the same as at the primary side.

- [PhaseTapChangerNonLinear](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PhaseTapChangerNonLinear/README.md). Adapted from CIM data models. The non-linear phase tap changer describes the non-linear behavior of a phase tap changer. This is a base class for the symmetrical and asymmetrical phase tap changer models. The details of these models can be found in the IEC 61970-301 document.

- [PhaseTapChangerTable](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PhaseTapChangerTable/README.md). Adapted from CIM data models. Describes a tabular curve for how the phase angle difference and impedance varies with the tap step.

- [PhaseTapChangerTablePoint](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PhaseTapChangerTablePoint/README.md). Adapted from CIM data models. Describes each tap step in the phase tap changer tabular curve.

- [PhaseTapChangerTabular](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PhaseTapChangerTabular/README.md). Adapted from CIM data models. 

- [PositionPoint](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PositionPoint/README.md). Adapted from CIM data models. Set of spatial coordinates that determine a point, defined in the coordinate system specified in 'Location.CoordinateSystem'. Use a single position point instance to desribe a point-oriented location. Use a sequence of position points to describe a line-oriented object (physical location of non-point oriented objects like cables or lines), or area of an object (like a substation or a geographical zone - in this case, have first and last position point with the same values).

- [PowerSystemResource](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PowerSystemResource/README.md). Adapted from CIM data models. A power system resource can be an item of equipment such as a switch, an equipment container containing many individual items of equipment such as a substation, or an organisational entity such as sub-control area. Power system resources can have measurements associated.

- [PowerSystemStabilizerDynamics](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PowerSystemStabilizerDynamics/README.md). Adapted from CIM data models. Power system stabilizer function block whose behaviour is described by reference to a standard model

- [PowerSystemStabilizerUserDefined](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PowerSystemStabilizerUserDefined/README.md). Adapted from CIM data models. function block whose dynamic behaviour is described by

- [PowerTransformer](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PowerTransformer/README.md). Adapted from CIM data models. An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow). A power transformer may be composed of separate transformer tanks that need not be identical. A power transformer can be modeled with or without tanks and is intended for use in both balanced and unbalanced representations.   A power transformer typically has two terminals, but may have one (grounding), three or more terminals. The inherited association ConductingEquipment.BaseVoltage should not be used.  The association from TransformerEnd to BaseVoltage should be used instead.

- [PowerTransformerEnd](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PowerTransformerEnd/README.md). Adapted from CIM data models. A PowerTransformerEnd is associated with each Terminal of a PowerTransformer. The impedance values r, r0, x, and x0 of a PowerTransformerEnd represents a star equivalent as follows 1) for a two Terminal PowerTransformer the high voltage PowerTransformerEnd has non zero values on r, r0, x, and x0 while the low voltage PowerTransformerEnd has zero values for r, r0, x, and x0. 2) for a three Terminal PowerTransformer the three PowerTransformerEnds represents a star equivalent with each leg in the star represented by r, r0, x, and x0 values. 3) for a PowerTransformer with more than three Terminals the PowerTransformerEnd impedance values cannot be used. Instead use the TransformerMeshImpedance or split the transformer into multiple PowerTransformers.

- [ProprietaryParameterDynamics](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ProprietaryParameterDynamics/README.md). Adapted from CIM data models. Supports definition of one or more parameters of several different datatypes for use by proprietary user-defined models.  NOTE: This class does not inherit from IdentifiedObject since it is not intended that a single instance of it be referenced by more than one proprietary user-defined model instance.

- [Pss1](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Pss1/README.md). Adapted from CIM data models. Italian PSS - three input PSS (speed, frequency, power).

- [Pss1A](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Pss1A/README.md). Adapted from CIM data models. Single input power system stabilizer. It is a modified version in order to allow representation of various vendors' implementations on PSS type 1A.

- [Pss2B](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Pss2B/README.md). Adapted from CIM data models. Modified IEEE PSS2B Model.  Extra lead/lag (or rate) block added at end (up to 4 lead/lags total).

- [Pss2ST](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Pss2ST/README.md). Adapted from CIM data models. PTI Microprocessor-Based Stabilizer type 1.

- [Pss5](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Pss5/README.md). Adapted from CIM data models. Italian PSS - Detailed PSS.

- [PssELIN2](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PssELIN2/README.md). Adapted from CIM data models. Power system stabilizer typically associated with ExcELIN2 (though PssIEEE2B or Pss2B can also be used).

- [PssIEEE1A](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PssIEEE1A/README.md). Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type PSS1A power system stabilizer model. PSS1A is the generalized form of a PSS with a single input. Some common stabilizer input signals are speed, frequency, and power.  Reference: IEEE 1A 421.5-2005 Section 8.1.

- [PssIEEE2B](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PssIEEE2B/README.md). Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type PSS2B power system stabilizer model. This stabilizer model is designed to represent a variety of dual-input stabilizers, which normally use combinations of power and speed or frequency to derive the stabilizing signal.  Reference: IEEE 2B 421.5-2005 Section 8.2.

- [PssIEEE3B](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PssIEEE3B/README.md). Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type PSS3B power system stabilizer model. The PSS model PSS3B has dual inputs of electrical power and rotor angular frequency deviation. The signals are used to derive an equivalent mechanical power signal.  Reference: IEEE 3B 421.5-2005 Section 8.3.

- [PssIEEE4B](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PssIEEE4B/README.md). Adapted from CIM data models. The class represents IEEE Std 421.5-2005 type PSS2B power system stabilizer model. The PSS4B model represents a structure based on multiple working frequency bands. Three separate bands, respectively dedicated to the low-, intermediate- and high-frequency modes of oscillations, are used in this delta-omega (speed input) PSS.  Reference: IEEE 4B 421.5-2005 Section 8.4.

- [PssPTIST1](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PssPTIST1/README.md). Adapted from CIM data models. PTI Microprocessor-Based Stabilizer type 1.

- [PssPTIST3](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PssPTIST3/README.md). Adapted from CIM data models. PTI Microprocessor-Based Stabilizer type 3.

- [PssSB4](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PssSB4/README.md). Adapted from CIM data models. Power sensitive stabilizer model.

- [PssSH](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PssSH/README.md). Adapted from CIM data models. Model for Siemens 'H infinity' power system stabilizer with generator electrical power input.

- [PssSK](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PssSK/README.md). Adapted from CIM data models. PSS Slovakian type - three inputs.

- [PssWECC](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PssWECC/README.md). Adapted from CIM data models. Dual input Power System Stabilizer, based on IEEE type 2, with modified output limiter defined by WECC (Western Electricity Coordinating Council, USA).

- [PU](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/PU/README.md). Adapted from CIM data models. Per Unit - a positive or negative value referred to a defined base. Values typically range from -10 to +10.

- [Quality61850](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Quality61850/README.md). Adapted from CIM data models. Quality flags in this class are as defined in IEC 61850, except for estimatorReplaced, which has been included in this class for convenience.

- [RaiseLowerCommand](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/RaiseLowerCommand/README.md). Adapted from CIM data models. An analog control that increase or decrease a set point value with pulses.

- [RatioTapChanger](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/RatioTapChanger/README.md). Adapted from CIM data models. A tap changer that changes the voltage ratio impacting the voltage magnitude but not the phase angle across the transformer.

- [RatioTapChangerTable](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/RatioTapChangerTable/README.md). Adapted from CIM data models. Describes a curve for how the voltage magnitude and impedance varies with the tap step.

- [RatioTapChangerTablePoint](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/RatioTapChangerTablePoint/README.md). Adapted from CIM data models. Describes each tap step in the ratio tap changer tabular curve.

- [Reactance](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Reactance/README.md). Adapted from CIM data models. Reactance (imaginary part of impedance), at rated frequency.

- [ReactiveCapabilityCurve](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ReactiveCapabilityCurve/README.md). Adapted from CIM data models. Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.

- [ReactivePower](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ReactivePower/README.md). Adapted from CIM data models. Product of RMS value of the voltage and the RMS value of the quadrature component of the current.

- [RegularIntervalSchedule](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/RegularIntervalSchedule/README.md). Adapted from CIM data models. The schedule has time points where the time between them is constant.

- [RegularTimePoint](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/RegularTimePoint/README.md). Adapted from CIM data models. Time point for a schedule where the time between the consecutive points is constant.

- [RegulatingCondEq](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/RegulatingCondEq/README.md). Adapted from CIM data models. A type of conducting equipment that can regulate a quantity (i.e. voltage or flow) at a specific point in the network.

- [RegulatingControl](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/RegulatingControl/README.md). Adapted from CIM data models. Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.  Remote bus voltage control is possible by specifying the controlled terminal located at some place remote from the controlling equipment. In case multiple equipment, possibly of different types, control same terminal there must be only one RegulatingControl at that terminal. The most specific subtype of RegulatingControl shall be used in case such equipment participate in the control, e.g. TapChangerControl for tap changers. For flow control  load sign convention is used, i.e. positive sign means flow out from a TopologicalNode (bus) into the conducting equipment.

- [RegulationSchedule](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/RegulationSchedule/README.md). Adapted from CIM data models. A pre-established pattern over time for a controlled variable, e.g., busbar voltage.

- [RemoteInputSignal](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/RemoteInputSignal/README.md). Adapted from CIM data models. Supports connection to a terminal associated with a remote bus from which an input signal of a specific type is coming.

- [ReportingGroup](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ReportingGroup/README.md). Adapted from CIM data models. A reporting group is used for various ad-hoc groupings used for reporting.

- [Resistance](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Resistance/README.md). Adapted from CIM data models. Resistance (real part of impedance).

- [ResistancePerLength](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ResistancePerLength/README.md). Adapted from CIM data models. Resistance (real part of impedance) per unit of length.

- [RotatingMachine](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/RotatingMachine/README.md). Adapted from CIM data models. A rotating machine which may be used as a generator or motor.

- [RotatingMachineDynamics](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/RotatingMachineDynamics/README.md). Adapted from CIM data models. Abstract parent class for all synchronous and asynchronous machine standard models.

- [RotationSpeed](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/RotationSpeed/README.md). Adapted from CIM data models. Number of revolutions per second.

- [Season](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Season/README.md). Adapted from CIM data models. A specified time period of the year.

- [SeasonDayTypeSchedule](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/SeasonDayTypeSchedule/README.md). Adapted from CIM data models. A time schedule covering a 24 hour period, with curve data for a specific type of season and day.

- [Seconds](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Seconds/README.md). Adapted from CIM data models. Time, in seconds.

- [SeriesCompensator](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/SeriesCompensator/README.md). Adapted from CIM data models. A Series Compensator is a series capacitor or reactor or an AC transmission line without charging susceptance.  It is a two terminal device.

- [SetPoint](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/SetPoint/README.md). Adapted from CIM data models. An analog control that issue a set point value.

- [ShuntCompensator](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ShuntCompensator/README.md). Adapted from CIM data models. A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  A negative value for reactivePerSection indicates that the compensator is a reactor. ShuntCompensator is a single terminal device.  Ground is implied.

- [Simple_Float](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Simple_Float/README.md). Adapted from CIM data models. A floating point number. The range is unspecified and not limited.

- [StateVariablesVersion](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/StateVariablesVersion/README.md). Adapted from CIM data models. Version details.

- [StaticVarCompensator](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/StaticVarCompensator/README.md). Adapted from CIM data models. A facility for providing variable and controllable shunt reactive power. The SVC typically consists of a stepdown transformer, filter, thyristor-controlled reactor, and thyristor-switched capacitor arms.  The SVC may operate in fixed MVar output mode or in voltage control mode. When in voltage control mode, the output of the SVC will be proportional to the deviation of voltage at the controlled bus from the voltage setpoint.  The SVC characteristic slope defines the proportion.  If the voltage at the controlled bus is equal to the voltage setpoint, the SVC MVar output is zero.

- [SteadyStateHypothesisVersion](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/SteadyStateHypothesisVersion/README.md). Adapted from CIM data models. Version details.

- [StringMeasurement](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/StringMeasurement/README.md). Adapted from CIM data models. StringMeasurement represents a measurement with values of type string.

- [StringMeasurementValue](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/StringMeasurementValue/README.md). Adapted from CIM data models. StringMeasurementValue represents a measurement value of type string.

- [SubGeographicalRegion](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/SubGeographicalRegion/README.md). Adapted from CIM data models. A subset of a geographical region of a power system network model.

- [SubLoadArea](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/SubLoadArea/README.md). Adapted from CIM data models. The class is the second level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.

- [Substation](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Substation/README.md). Adapted from CIM data models. A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.

- [Susceptance](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Susceptance/README.md). Adapted from CIM data models. Imaginary part of admittance.

- [SvInjection](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/SvInjection/README.md). Adapted from CIM data models. The SvInjection is reporting the calculated bus injection minus the sum of the terminal flows. The terminal flow is positive out from the bus (load sign convention) and bus injection has positive flow into the bus. SvInjection may have the remainder after state estimation or slack after power flow calculation.

- [SvPowerFlow](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/SvPowerFlow/README.md). Adapted from CIM data models. State variable for power flow. Load convention is used for flow direction. This means flow out from the TopologicalNode into the equipment is positive.

- [SvShuntCompensatorSections](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/SvShuntCompensatorSections/README.md). Adapted from CIM data models. State variable for the number of sections in service for a shunt compensator.

- [SvStatus](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/SvStatus/README.md). Adapted from CIM data models. State variable for status.

- [SvTapStep](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/SvTapStep/README.md). Adapted from CIM data models. State variable for transformer tap step.     This class is to be used for taps of LTC (load tap changing) transformers, not fixed tap transformers.

- [SvVoltage](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/SvVoltage/README.md). Adapted from CIM data models. State variable for voltage.

- [Switch](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Switch/README.md). Adapted from CIM data models. A generic device designed to close, or open, or both, one or more electric circuits.  All switches are two terminal devices including grounding switches.

- [SwitchSchedule](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/SwitchSchedule/README.md). Adapted from CIM data models. A schedule of switch positions.  If RegularTimePoint.value1 is 0, the switch is open.  If 1, the switch is closed.

- [SynchronousMachine](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/SynchronousMachine/README.md). Adapted from CIM data models. An electromechanical device that operates with shaft rotating synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.

- [SynchronousMachineDetailed](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/SynchronousMachineDetailed/README.md). Adapted from CIM data models. All synchronous machine detailed types use a subset of the same data parameters and input/output variables.   The several variations differ in the following ways:   It is not necessary for each simulation tool to have separate models for each of the model types.  The same model can often be used for several types by alternative logic within the model.  Also, differences in saturation representation may not result in significant model performance differences so model substitutions are often acceptable.

- [SynchronousMachineDynamics](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/SynchronousMachineDynamics/README.md). Adapted from CIM data models. Synchronous machine whose behaviour is described by reference to a standard model expressed in one of the following forms:

- [SynchronousMachineEquivalentCircuit](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/SynchronousMachineEquivalentCircuit/README.md). Adapted from CIM data models. The electrical equations for all variations of the synchronous models are based on the SynchronousEquivalentCircuit diagram for the direct and quadrature axes.    =  +   =  +  *  / ( + )  =  +  * *  / ( *  +  *  +  * )  =  +   =  +  *  / (+ )  =  +  **  / ( *  +  *  +  * )  = ( + ) / ( * )  = ( *  +  *  +  * ) / ( *  * ( + )  = ( + ) / ( * )  = ( *  +  *  +  * )/ ( *  * ( + ) Same equations using CIM attributes from SynchronousMachineTimeConstantReactance class on left of = sign and SynchronousMachineEquivalentCircuit class on right (except as noted): xDirectSync = xad + RotatingMachineDynamics.statorLeakageReactance xDirectTrans = RotatingMachineDynamics.statorLeakageReactance + xad * xfd / (xad + xfd) xDirectSubtrans = RotatingMachineDynamics.statorLeakageReactance + xad * xfd * x1d / (xad * xfd + xad * x1d + xfd * x1d) xQuadSync = xaq + RotatingMachineDynamics.statorLeakageReactance xQuadTrans = RotatingMachineDynamics.statorLeakageReactance + xaq * x1q / (xaq+ x1q) xQuadSubtrans = RotatingMachineDynamics.statorLeakageReactance + xaq * x1q* x2q / (xaq * x1q + xaq * x2q + x1q * x2q)  tpdo = (xad + xfd) / (2*pi*nominal frequency * rfd) tppdo = (xad * xfd + xad * x1d + xfd * x1d) / (2*pi*nominal frequency * r1d * (xad + xfd) tpqo = (xaq + x1q) / (2*pi*nominal frequency * r1q) tppqo = (xaq * x1q + xaq * x2q + x1q * x2q)/ (2*pi*nominal frequency * r2q * (xaq + x1q).  Are only valid for a simplified model where 'Canay' reactance is zero.

- [SynchronousMachineTimeConstantReactance](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/SynchronousMachineTimeConstantReactance/README.md). Adapted from CIM data models. Synchronous machine detailed modelling types are defined by the combination of the attributes SynchronousMachineTimeConstantReactance.modelType and SynchronousMachineTimeConstantReactance.rotorType.     The parameters used for models expressed in time constant reactance form include:

- [SynchronousMachineUserDefined](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/SynchronousMachineUserDefined/README.md). Adapted from CIM data models. Synchronous machine whose dynamic behaviour is described by a user-defined model.

- [TapChanger](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/TapChanger/README.md). Adapted from CIM data models. Mechanism for changing transformer winding tap positions.

- [TapChangerControl](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/TapChangerControl/README.md). Adapted from CIM data models. Describes behavior specific to tap changers, e.g. how the voltage at the end of a line varies with the load level and compensation of the voltage drop by tap adjustment.

- [TapChangerTablePoint](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/TapChangerTablePoint/README.md). Adapted from CIM data models. 

- [TapSchedule](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/TapSchedule/README.md). Adapted from CIM data models. A pre-established pattern over time for a tap step.

- [Temperature](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Temperature/README.md). Adapted from CIM data models. Value of temperature in degrees Celsius.

- [Terminal](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Terminal/README.md). Adapted from CIM data models. An AC electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called connectivity nodes.

- [TextDiagramObject](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/TextDiagramObject/README.md). Adapted from CIM data models. A diagram object for placing free-text or text derived from an associated domain object.

- [ThermalGeneratingUnit](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ThermalGeneratingUnit/README.md). Adapted from CIM data models. A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.

- [TieFlow](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/TieFlow/README.md). Adapted from CIM data models. A flow specification in terms of location and direction for a control area.

- [TopologicalIsland](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/TopologicalIsland/README.md). Adapted from CIM data models. An electrically connected subset of the network. Topological islands can change as the current network state changes: e.g. due to  - disconnect switches or breakers change state in a SCADA/EMS - manual creation, change or deletion of topological nodes in a planning tool.

- [TopologicalNode](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/TopologicalNode/README.md). Adapted from CIM data models. For a detailed substation model a topological node is a set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes change as the current network state changes (i.e., switches, breakers, etc. change state). For a planning model, switch statuses are not used to form topological nodes. Instead they are manually created or deleted in a model builder tool. Topological nodes maintained this way are also called 'busses'.

- [TopologyBoundaryVersion](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/TopologyBoundaryVersion/README.md). Adapted from CIM data models. Version details.

- [TopologyVersion](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/TopologyVersion/README.md). Adapted from CIM data models. Version details.

- [TransformerEnd](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/TransformerEnd/README.md). Adapted from CIM data models. A conducting connection point of a power transformer. It corresponds to a physical transformer winding terminal.  In earlier CIM versions, the TransformerWinding class served a similar purpose, but this class is more flexible because it associates to terminal but is not a specialization of ConductingEquipment.

- [TurbineGovernorDynamics](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/TurbineGovernorDynamics/README.md). Adapted from CIM data models. Turbine-governor function block whose behavior is described by reference to a standard model

- [TurbineGovernorUserDefined](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/TurbineGovernorUserDefined/README.md). Adapted from CIM data models. Turbine-governor function block whose dynamic behaviour is described by

- [TurbineLoadControllerDynamics](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/TurbineLoadControllerDynamics/README.md). Adapted from CIM data models. Turbine load controller function block whose behavior is described by reference to a standard model

- [TurbineLoadControllerUserDefined](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/TurbineLoadControllerUserDefined/README.md). Adapted from CIM data models. Turbine load controller function block whose dynamic behaviour is described by

- [TurbLCFB1](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/TurbLCFB1/README.md). Adapted from CIM data models. Turbine Load Controller model developed in the WECC.  This model represents a supervisory turbine load controller that acts to maintain turbine power at a set value by continuous adjustment of the turbine governor speed-load reference. This model is intended to represent slow reset 'outer loop' controllers managing the action of the turbine governor.

- [UnderexcitationLimiterDynamics](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/UnderexcitationLimiterDynamics/README.md). Adapted from CIM data models. Underexcitation limiter function block whose behaviour is described by reference to a standard model

- [UnderexcitationLimiterUserDefined](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/UnderexcitationLimiterUserDefined/README.md). Adapted from CIM data models. Underexcitation limiter function block whose dynamic behaviour is described by

- [UnderexcLim2Simplified](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/UnderexcLim2Simplified/README.md). Adapted from CIM data models. This model can be derived from UnderexcLimIEEE2. The limit characteristic (look -up table) is a single straight-line, the same as UnderexcLimIEEE2 (see Figure 10.4 (p 32), IEEE 421.5-2005 Section 10.2).

- [UnderexcLimIEEE1](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/UnderexcLimIEEE1/README.md). Adapted from CIM data models. The class represents the Type UEL1 model which has a circular limit boundary when plotted in terms of machine reactive power vs. real power output.  Reference: IEEE UEL1 421.5-2005 Section 10.1.

- [UnderexcLimIEEE2](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/UnderexcLimIEEE2/README.md). Adapted from CIM data models. The class represents the Type UEL2 which has either a straight-line or multi-segment characteristic when plotted in terms of machine reactive power output vs. real power output.  Reference: IEEE UEL2 421.5-2005 Section 10.2.  (Limit characteristic lookup table shown in Figure 10.4 (p 32) of the standard).

- [UnderexcLimX1](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/UnderexcLimX1/README.md). Adapted from CIM data models. 

- [UnderexcLimX2](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/UnderexcLimX2/README.md). Adapted from CIM data models. 

- [VAdjIEEE](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/VAdjIEEE/README.md). Adapted from CIM data models. The class represents IEEE Voltage Adjuster which is used to represent the voltage adjuster in either a power factor or var control system.  Reference: IEEE Standard 421.5-2005 Section 11.1.

- [ValueAliasSet](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ValueAliasSet/README.md). Adapted from CIM data models. Describes the translation of a set of values into a name and is intendend to facilitate cusom translations. Each ValueAliasSet has a name, description etc. A specific Measurement may represent a discrete state like Open, Closed, Intermediate etc. This requires a translation from the MeasurementValue.value number to a string, e.g. 0->'Invalid', 1->'Open', 2->'Closed', 3->'Intermediate'. Each ValueToAlias member in ValueAliasSet.Value describe a mapping for one particular value to a name.

- [ValueToAlias](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/ValueToAlias/README.md). Adapted from CIM data models. Describes the translation of one particular value into a name, e.g. 1 as 'Open'.

- [VCompIEEEType1](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/VCompIEEEType1/README.md). Adapted from CIM data models. Reference: IEEE Standard 421.5-2005 Section 4.

- [VCompIEEEType2](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/VCompIEEEType2/README.md). Adapted from CIM data models. 

- [VisibilityLayer](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/VisibilityLayer/README.md). Adapted from CIM data models. Layers are typically used for grouping diagram objects according to themes and scales. Themes are used to display or hide certain information (e.g., lakes, borders), while scales are used for hiding or displaying information depending on the current zoom level (hide text when it is too small to be read, or when it exceeds the screen size). This is also called de-cluttering.  CIM based graphics exchange will support an m:n relationship between diagram objects and layers. It will be the task of the importing system to convert an m:n case into an appropriate 1:n representation if the importing system does not support m:n.

- [Voltage](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/Voltage/README.md). Adapted from CIM data models. Electrical voltage, can be both AC and DC.

- [VoltageAdjusterDynamics](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/VoltageAdjusterDynamics/README.md). Adapted from CIM data models. Voltage adjuster function block whose behaviour is described by reference to a standard model

- [VoltageAdjusterUserDefined](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/VoltageAdjusterUserDefined/README.md). Adapted from CIM data models. function block whose dynamic behaviour is described by

- [VoltageCompensatorDynamics](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/VoltageCompensatorDynamics/README.md). Adapted from CIM data models. Voltage compensator function block whose behaviour is described by reference to a standard model

- [VoltageCompensatorUserDefined](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/VoltageCompensatorUserDefined/README.md). Adapted from CIM data models. Voltage compensator function block whose dynamic behaviour is described by

- [VoltageLevel](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/VoltageLevel/README.md). Adapted from CIM data models. A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.

- [VoltageLimit](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/VoltageLimit/README.md). Adapted from CIM data models. Operational limit applied to voltage.

- [VoltagePerReactivePower](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/VoltagePerReactivePower/README.md). Adapted from CIM data models. Voltage variation with reactive power.

- [VolumeFlowRate](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/VolumeFlowRate/README.md). Adapted from CIM data models. Volume per time.

- [VsCapabilityCurve](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/VsCapabilityCurve/README.md). Adapted from CIM data models. The P-Q capability curve for a voltage source converter, with P on x-axis and Qmin and Qmax on y1-axis and y2-axis.

- [VsConverter](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/VsConverter/README.md). Adapted from CIM data models. DC side of the voltage source converter (VSC).

- [WindAeroConstIEC](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindAeroConstIEC/README.md). Adapted from CIM data models. The constant aerodynamic torque model assumes that the aerodynamic torque is constant.  Reference: IEC Standard 61400-27-1 Section 6.6.1.1.

- [WindAeroLinearIEC](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindAeroLinearIEC/README.md). Adapted from CIM data models. The linearised aerodynamic model.    Reference: IEC Standard 614000-27-1 Section 6.6.1.2.

- [WindContCurrLimIEC](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindContCurrLimIEC/README.md). Adapted from CIM data models. Current limitation model.  The current limitation model combines the physical limits.  Reference: IEC Standard 61400-27-1 Section 6.6.5.7.

- [WindContPitchAngleIEC](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindContPitchAngleIEC/README.md). Adapted from CIM data models. Pitch angle control model.  Reference: IEC Standard 61400-27-1 Section 6.6.5.8.

- [WindContPType3IEC](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindContPType3IEC/README.md). Adapted from CIM data models. P control model Type 3.  Reference: IEC Standard 61400-27-1 Section 6.6.5.3.

- [WindContPType4aIEC](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindContPType4aIEC/README.md). Adapted from CIM data models. P control model Type 4A.  Reference: IEC Standard 61400-27-1 Section 6.6.5.4.

- [WindContPType4bIEC](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindContPType4bIEC/README.md). Adapted from CIM data models. P control model Type 4B.  Reference: IEC Standard 61400-27-1 Section 6.6.5.5.

- [WindContQIEC](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindContQIEC/README.md). Adapted from CIM data models. Q control model.  Reference: IEC Standard 61400-27-1 Section 6.6.5.6.

- [WindContRotorRIEC](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindContRotorRIEC/README.md). Adapted from CIM data models. Rotor resistance control model.  Reference: IEC Standard 61400-27-1 Section 6.6.5.2.

- [WindDynamicsLookupTable](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindDynamicsLookupTable/README.md). Adapted from CIM data models. The class models a look up table for the purpose of wind standard models.

- [WindGeneratingUnit](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindGeneratingUnit/README.md). Adapted from CIM data models. A wind driven generating unit.  May be used to represent a single turbine or an aggregation.

- [WindGenTurbineType1IEC](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindGenTurbineType1IEC/README.md). Adapted from CIM data models. Wind turbine IEC Type 1.  Reference: IEC Standard 61400-27-1, section 6.5.2.

- [WindGenTurbineType2IEC](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindGenTurbineType2IEC/README.md). Adapted from CIM data models. Wind turbine IEC Type 2.  Reference: IEC Standard 61400-27-1, section 6.5.3.

- [WindGenTurbineType3aIEC](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindGenTurbineType3aIEC/README.md). Adapted from CIM data models. IEC Type 3A generator set model.  Reference: IEC Standard 61400-27-1 Section 6.6.3.2.

- [WindGenTurbineType3bIEC](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindGenTurbineType3bIEC/README.md). Adapted from CIM data models. IEC Type 3B generator set model.  Reference: IEC Standard 61400-27-1 Section 6.6.3.3.

- [WindGenTurbineType3IEC](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindGenTurbineType3IEC/README.md). Adapted from CIM data models. Generator model for wind turbines of IEC type 3A and 3B.

- [WindGenType4IEC](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindGenType4IEC/README.md). Adapted from CIM data models. IEC Type 4 generator set model.  Reference: IEC Standard 61400-27-1 Section 6.6.3.4.

- [WindMechIEC](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindMechIEC/README.md). Adapted from CIM data models. Two mass model.  Reference: IEC Standard 61400-27-1 Section 6.6.2.1.

- [WindPitchContEmulIEC](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindPitchContEmulIEC/README.md). Adapted from CIM data models. Pitch control emulator model.  Reference: IEC Standard 61400-27-1 Section 6.6.5.1.

- [WindPlantDynamics](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindPlantDynamics/README.md). Adapted from CIM data models. Parent class supporting relationships to wind turbines Type 3 and 4 and wind plant IEC and user defined wind plants including their control models.

- [WindPlantFreqPcontrolIEC](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindPlantFreqPcontrolIEC/README.md). Adapted from CIM data models. Frequency and active power controller model.  Reference: IEC Standard 61400-27-1 Annex E.

- [WindPlantIEC](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindPlantIEC/README.md). Adapted from CIM data models. Simplified IEC type plant level model.   Reference: IEC 61400-27-1, AnnexE.

- [WindPlantReactiveControlIEC](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindPlantReactiveControlIEC/README.md). Adapted from CIM data models. Simplified plant voltage and reactive power control model for use with type 3 and type 4 wind turbine models.  Reference: IEC Standard 61400-27-1 Annex E.

- [WindPlantUserDefined](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindPlantUserDefined/README.md). Adapted from CIM data models. Wind plant function block whose dynamic behaviour is described by

- [WindProtectionIEC](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindProtectionIEC/README.md). Adapted from CIM data models. The grid protection model includes protection against over and under voltage, and against over and under frequency.  Reference: IEC Standard 614000-27-1 Section 6.6.6.

- [WindTurbineType1or2Dynamics](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindTurbineType1or2Dynamics/README.md). Adapted from CIM data models. Parent class supporting relationships to wind turbines Type 1 and 2 and their control models.

- [WindTurbineType1or2IEC](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindTurbineType1or2IEC/README.md). Adapted from CIM data models. Generator model for wind turbine of IEC Type 1 or Type 2 is a standard asynchronous generator model.  Reference: IEC Standard 614000-27-1 Section 6.6.3.1.

- [WindTurbineType3or4Dynamics](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindTurbineType3or4Dynamics/README.md). Adapted from CIM data models. Parent class supporting relationships to wind turbines Type 3 and 4 and wind plant including their control models.

- [WindTurbineType3or4IEC](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindTurbineType3or4IEC/README.md). Adapted from CIM data models. Parent class supporting relationships to IEC wind turbines Type 3 and 4 and wind plant including their control models.

- [WindTurbineType4aIEC](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindTurbineType4aIEC/README.md). Adapted from CIM data models. Wind turbine IEC Type 4A.  Reference: IEC Standard 61400-27-1, section 6.5.5.2.

- [WindTurbineType4bIEC](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindTurbineType4bIEC/README.md). Adapted from CIM data models. Wind turbine IEC Type 4A.  Reference: IEC Standard 61400-27-1, section 6.5.5.3.

- [WindType1or2UserDefined](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindType1or2UserDefined/README.md). Adapted from CIM data models. Wind Type 1 or Type 2 function block whose dynamic behaviour is described by

- [WindType3or4UserDefined](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/WindType3or4UserDefined/README.md). Adapted from CIM data models. Wind Type 3 or Type 4 function block whose dynamic behaviour is described by



### Contributors
[Link](https://github.com/smart-data-models/dataModel.EnergyCIM/blob/master/CONTRIBUTORS.yaml) to the 1 current contributors of the data models of this Subject.


### Contribution
You can raise an [issue](https://github.com/smart-data-models/dataModel.EnergyCIM/issues) or submit your [PR](https://github.com/smart-data-models/dataModel.EnergyCIM/pulls) on existing data models


