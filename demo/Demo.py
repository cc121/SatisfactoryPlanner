import os
import sys
from SatisfactoryPlanner.Resource.Oil import CrudeOil
from SatisfactoryPlanner.Resource.Ore import CateriumOre, Coal, CopperOre, IronOre, Limestone, Sulfur, Bauxite, RawQuartz, NitrogenGas

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from SatisfactoryPlanner.Factory.Factory import Miner, Factory, OilExtractor, WaterExtractor, ResourceWellExtractor
from SatisfactoryPlanner.Machines.Machines import Smelter, Constructor, Assembler, Foundry, Manufacturer, Refinery, \
    FuelGenerator, Blender, ParticleAccelerator, Packager
from SatisfactoryPlanner.Session.Session import Session
from SatisfactoryPlanner.Resource import Resource


def build_adaptive_control_unit_factory(automated_wiring_factory, circuit_board_factory, heavy_modular_frame_factory, computer_factory):
    factory = Factory('Adaptive Control Unit Factory')

    factory.add_input(automated_wiring_factory)
    factory.add_input(circuit_board_factory)
    factory.add_input(heavy_modular_frame_factory)
    factory.add_input(computer_factory)

    factory.add_machine(Manufacturer('Adaptive Control Unit'), Resource.AdaptiveControlUnit)
    factory.add_machine(Manufacturer('Adaptive Control Unit'), Resource.AdaptiveControlUnit)

    return factory


def build_ai_limiter_factory():
    factory = Factory('AI Limiter Factory')

    factory.add_input(Miner(3, CopperOre('Normal')))

    factory.add_input(Miner(3, CateriumOre('Normal')))

    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))

    factory.add_machine(Smelter('Caterium Ingot'))
    factory.add_machine(Smelter('Caterium Ingot'))
    factory.add_machine(Smelter('Caterium Ingot'))
    factory.add_machine(Smelter('Caterium Ingot'))

    factory.add_machine(Constructor('Copper Sheet'))
    factory.add_machine(Constructor('Copper Sheet'))
    factory.add_machine(Constructor('Copper Sheet'))
    factory.add_machine(Constructor('Copper Sheet'))
    factory.add_machine(Constructor('Copper Sheet'))

    factory.add_machine(Constructor('Quickwire'))
    factory.add_machine(Constructor('Quickwire'))
    factory.add_machine(Constructor('Quickwire'))
    factory.add_machine(Constructor('Quickwire'))

    factory.add_machine(Assembler('AI Limiter'), Resource.AILimiter)
    factory.add_machine(Assembler('AI Limiter'), Resource.AILimiter)

    return factory


def build_assembly_director_system_factory(adaptive_control_unit_factory, supercomputer_factory):
    factory = Factory('Assembly Directory System Factory')

    factory.add_input(adaptive_control_unit_factory)
    factory.add_input(supercomputer_factory)

    factory.add_machine(Assembler('Assembly Director System'), Resource.AssemblyDirectorSystem)

    return factory


def build_automated_wiring_factory(stator_factory):
    factory = Factory('Automated Wiring Factory')

    factory.add_input(stator_factory)

    factory.add_input(Miner(3, CopperOre('Normal')))
    factory.add_input(Miner(3, CopperOre('Normal')))

    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))

    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))

    factory.add_machine(Constructor('Cable'))
    factory.add_machine(Constructor('Cable'))
    factory.add_machine(Constructor('Cable'))
    factory.add_machine(Constructor('Cable'))
    factory.add_machine(Constructor('Cable'))
    factory.add_machine(Constructor('Cable'))
    factory.add_machine(Constructor('Cable'))
    factory.add_machine(Constructor('Cable'))
    factory.add_machine(Constructor('Cable'))
    factory.add_machine(Constructor('Cable'))

    factory.add_machine(Assembler('Automated Wiring'), Resource.AutomatedWiring)
    factory.add_machine(Assembler('Automated Wiring'), Resource.AutomatedWiring)
    factory.add_machine(Assembler('Automated Wiring'), Resource.AutomatedWiring)
    factory.add_machine(Assembler('Automated Wiring'), Resource.AutomatedWiring)
    factory.add_machine(Assembler('Automated Wiring'), Resource.AutomatedWiring)
    factory.add_machine(Assembler('Automated Wiring'), Resource.AutomatedWiring)

    return factory


def build_battery_factory(refinery):
    factory = Factory('Battery Factory')

    factory.add_input(refinery)

    factory.add_input(Miner(3, Sulfur('Normal')))

    factory.add_input(Miner(3, Bauxite('Normal')))
    factory.add_input(Miner(3, Bauxite('Normal')))

    factory.add_input(Miner(3, Coal('Normal')))

    factory.add_input(Miner(3, Limestone('Normal')))
    factory.add_input(Miner(3, Limestone('Normal')))

    factory.add_input(Miner(3, CopperOre('Normal')))
    factory.add_input(Miner(3, CopperOre('Normal')))

    factory.add_input(WaterExtractor())
    factory.add_input(WaterExtractor())
    factory.add_input(WaterExtractor())
    factory.add_input(WaterExtractor())

    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))

    factory.add_machine(Refinery('Sloppy Alumina'))
    factory.add_machine(Refinery('Sloppy Alumina'))

    factory.add_machine(Refinery('Aluminum Scrap'))
    factory.add_machine(Refinery('Aluminum Scrap'))

    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))

    factory.add_machine(Smelter('Pure Aluminum Ingot'))
    factory.add_machine(Smelter('Pure Aluminum Ingot'))
    factory.add_machine(Smelter('Pure Aluminum Ingot'))
    factory.add_machine(Smelter('Pure Aluminum Ingot'))
    factory.add_machine(Smelter('Pure Aluminum Ingot'))
    factory.add_machine(Smelter('Pure Aluminum Ingot'))
    factory.add_machine(Smelter('Pure Aluminum Ingot'))
    factory.add_machine(Smelter('Pure Aluminum Ingot'))
    factory.add_machine(Smelter('Pure Aluminum Ingot'))
    factory.add_machine(Smelter('Pure Aluminum Ingot'))
    factory.add_machine(Smelter('Pure Aluminum Ingot'))
    factory.add_machine(Smelter('Pure Aluminum Ingot'))
    factory.add_machine(Smelter('Pure Aluminum Ingot'))
    factory.add_machine(Smelter('Pure Aluminum Ingot'))
    factory.add_machine(Smelter('Pure Aluminum Ingot'))
    factory.add_machine(Smelter('Pure Aluminum Ingot'))
    factory.add_machine(Smelter('Pure Aluminum Ingot'))
    factory.add_machine(Smelter('Pure Aluminum Ingot'))
    factory.add_machine(Smelter('Pure Aluminum Ingot'))
    factory.add_machine(Smelter('Pure Aluminum Ingot'))
    factory.add_machine(Smelter('Pure Aluminum Ingot'))
    factory.add_machine(Smelter('Pure Aluminum Ingot'))
    factory.add_machine(Smelter('Pure Aluminum Ingot'))
    factory.add_machine(Smelter('Pure Aluminum Ingot'))

    factory.add_machine(Assembler('Alclad Casing'), Resource.AluminumCasing)
    factory.add_machine(Assembler('Alclad Casing'), Resource.AluminumCasing)
    factory.add_machine(Assembler('Alclad Casing'), Resource.AluminumCasing)
    factory.add_machine(Assembler('Alclad Casing'), Resource.AluminumCasing)

    factory.add_machine(Assembler('Alclad Aluminum Sheet'), Resource.AlcladAluminumSheet)
    factory.add_machine(Assembler('Alclad Aluminum Sheet'), Resource.AlcladAluminumSheet)

    factory.add_machine(Manufacturer('Classic Battery'), Resource.Battery)

    factory.add_machine(Constructor('Empty Fluid Tank'), Resource.EmptyFluidTank)

    # # Sink the water
    factory.add_machine(Refinery('Wet Concrete'))
    factory.add_machine(Refinery('Wet Concrete'))
    factory.add_machine(Refinery('Wet Concrete', clock_speed_modifier=120/100))

    return factory


def build_circuit_board_factory(refinery):
    factory = Factory('Circuit Board Factory')

    factory.add_input(refinery)

    factory.add_input(Miner(3, CopperOre('Normal')))
    factory.add_input(Miner(3, CopperOre('Normal')))

    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))

    factory.add_machine(Constructor('Copper Sheet'))
    factory.add_machine(Constructor('Copper Sheet'))
    factory.add_machine(Constructor('Copper Sheet'))
    factory.add_machine(Constructor('Copper Sheet'))
    factory.add_machine(Constructor('Copper Sheet'))
    factory.add_machine(Constructor('Copper Sheet'))
    factory.add_machine(Constructor('Copper Sheet'))
    factory.add_machine(Constructor('Copper Sheet'))
    factory.add_machine(Constructor('Copper Sheet'))
    factory.add_machine(Constructor('Copper Sheet'))
    factory.add_machine(Constructor('Copper Sheet'))
    factory.add_machine(Constructor('Copper Sheet'))
    factory.add_machine(Constructor('Copper Sheet'))
    factory.add_machine(Constructor('Copper Sheet'))
    factory.add_machine(Constructor('Copper Sheet'))
    factory.add_machine(Constructor('Copper Sheet'))
    factory.add_machine(Constructor('Copper Sheet'))
    factory.add_machine(Constructor('Copper Sheet'))
    factory.add_machine(Constructor('Copper Sheet'))
    factory.add_machine(Constructor('Copper Sheet'))
    factory.add_machine(Constructor('Copper Sheet'))
    factory.add_machine(Constructor('Copper Sheet'))
    factory.add_machine(Constructor('Copper Sheet'))

    factory.add_machine(Assembler('Circuit Board'), Resource.CircuitBoard)
    factory.add_machine(Assembler('Circuit Board'), Resource.CircuitBoard)
    factory.add_machine(Assembler('Circuit Board'), Resource.CircuitBoard)
    factory.add_machine(Assembler('Circuit Board'), Resource.CircuitBoard)
    factory.add_machine(Assembler('Circuit Board'), Resource.CircuitBoard)
    factory.add_machine(Assembler('Circuit Board'), Resource.CircuitBoard)
    factory.add_machine(Assembler('Circuit Board'), Resource.CircuitBoard)
    factory.add_machine(Assembler('Circuit Board'), Resource.CircuitBoard)
    factory.add_machine(Assembler('Circuit Board'), Resource.CircuitBoard)
    factory.add_machine(Assembler('Circuit Board'), Resource.CircuitBoard)
    factory.add_machine(Assembler('Circuit Board'), Resource.CircuitBoard)
    factory.add_machine(Assembler('Circuit Board'), Resource.CircuitBoard)
    factory.add_machine(Assembler('Circuit Board'), Resource.CircuitBoard)
    factory.add_machine(Assembler('Circuit Board'), Resource.CircuitBoard)
    factory.add_machine(Assembler('Circuit Board'), Resource.CircuitBoard)

    return factory


def build_computer_factory(refinery, circuit_board_factory):
    factory = Factory('Computer Factory')

    factory.add_input(refinery)
    factory.add_input(circuit_board_factory)

    factory.add_input(Miner(3, IronOre('Normal')))

    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))

    factory.add_machine(Constructor('Iron Wire'))
    factory.add_machine(Constructor('Iron Wire'))
    factory.add_machine(Constructor('Iron Wire'))
    factory.add_machine(Constructor('Iron Wire'))
    factory.add_machine(Constructor('Iron Wire'))
    factory.add_machine(Constructor('Iron Wire'))
    factory.add_machine(Constructor('Iron Wire'))
    factory.add_machine(Constructor('Iron Wire'))

    factory.add_machine(Constructor('Cable'))
    factory.add_machine(Constructor('Cable'))
    factory.add_machine(Constructor('Cable'))

    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))

    factory.add_machine(Manufacturer('Computer'), Resource.Computer)
    factory.add_machine(Manufacturer('Computer'), Resource.Computer)
    factory.add_machine(Manufacturer('Computer'), Resource.Computer)

    return factory


def build_cooling_system_factory(heat_sink_factory, refinery):
    factory = Factory('Cooling System Factory')

    factory.add_input(heat_sink_factory)
    factory.add_input(refinery)

    factory.add_input(WaterExtractor())

    factory.add_input(ResourceWellExtractor(NitrogenGas('Normal')))
    factory.add_input(ResourceWellExtractor(NitrogenGas('Normal')))
    factory.add_input(ResourceWellExtractor(NitrogenGas('Normal')))

    factory.add_machine(Blender('Cooling System'), Resource.CoolingSystem)

    return factory


def build_crystal_oscillator_factory(reinforced_iron_plate_factory):
    factory = Factory('Crystal Factory Oscillator')

    factory.add_input(reinforced_iron_plate_factory)

    factory.add_input(Miner(3, RawQuartz('Normal')))

    factory.add_input(Miner(3, CopperOre('Normal')))

    factory.add_machine(Smelter('Copper Ingot'))

    factory.add_machine(Constructor('Quartz Crystal'))

    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))

    factory.add_machine(Constructor('Cable'))

    factory.add_machine(Manufacturer('Crystal Oscillator'), Resource.CrystalOscillator)

    return factory


def build_electromagnetic_control_rod_factory(stator_factory, ai_limiter_factory):
    factory = Factory('Electromagnetic Control Rod Factory')

    factory.add_input(stator_factory)
    factory.add_input(ai_limiter_factory)

    factory.add_machine(Assembler('Electromagnetic Control Rod'))

    return factory


def build_fused_modular_frame_factory(heavy_modular_frame_factory, aluminum_casing_factory):
    factory = Factory('Fused Modular Frame Factory')

    factory.add_input(heavy_modular_frame_factory)
    factory.add_input(aluminum_casing_factory)

    factory.add_input(ResourceWellExtractor(NitrogenGas('Normal')))
    factory.add_input(ResourceWellExtractor(NitrogenGas('Normal')))

    factory.add_machine(Blender('Fused Modular Frame'), Resource.FusedModularFrame)
    factory.add_machine(Blender('Fused Modular Frame'), Resource.FusedModularFrame)
    factory.add_machine(Blender('Fused Modular Frame'), Resource.FusedModularFrame)

    return factory


def build_heat_sink_factory(alclad_aluminum_sheet_factory, refinery):
    factory = Factory('Heat Sink Factory')

    factory.add_input(alclad_aluminum_sheet_factory)
    factory.add_input(refinery)

    factory.add_machine(Assembler('Heat Exchanger'), Resource.HeatSink)
    factory.add_machine(Assembler('Heat Exchanger'), Resource.HeatSink)
    factory.add_machine(Assembler('Heat Exchanger'), Resource.HeatSink)
    factory.add_machine(Assembler('Heat Exchanger'), Resource.HeatSink)
    factory.add_machine(Assembler('Heat Exchanger'), Resource.HeatSink)

    return factory


def build_heavy_modular_frame_factory(steel_foundry, reinforced_iron_plate_factory, modular_frame_factory):
    factory = Factory('Heavy Modular Frame Factory')

    factory.add_input(steel_foundry)
    factory.add_input(reinforced_iron_plate_factory)
    factory.add_input(modular_frame_factory)

    factory.add_input(Miner(3, Limestone('Normal')))
    factory.add_input(Miner(3, Limestone('Normal')))

    factory.add_input(WaterExtractor())
    factory.add_input(WaterExtractor())
    factory.add_input(WaterExtractor())

    factory.add_machine(Refinery('Wet Concrete'))
    factory.add_machine(Refinery('Wet Concrete'))
    factory.add_machine(Refinery('Wet Concrete'))

    factory.add_machine(Assembler('Encased Industrial Pipe'))
    factory.add_machine(Assembler('Encased Industrial Pipe'))
    factory.add_machine(Assembler('Encased Industrial Pipe'))
    factory.add_machine(Assembler('Encased Industrial Pipe'))
    factory.add_machine(Assembler('Encased Industrial Pipe'))
    factory.add_machine(Assembler('Encased Industrial Pipe'))
    factory.add_machine(Assembler('Encased Industrial Pipe'))
    factory.add_machine(Assembler('Encased Industrial Pipe'))

    factory.add_machine(Manufacturer('Heavy Encased Frame'), Resource.HeavyModularFrame)
    factory.add_machine(Manufacturer('Heavy Encased Frame'), Resource.HeavyModularFrame)
    factory.add_machine(Manufacturer('Heavy Encased Frame'), Resource.HeavyModularFrame)

    return factory


def build_high_speed_connector_factory(circuit_board_factory):
    factory = Factory('High-Speed Connector Factory')

    factory.add_input(circuit_board_factory)

    factory.add_input(Miner(3, CateriumOre('Normal')))
    factory.add_input(Miner(3, CateriumOre('Normal')))

    factory.add_input(Miner(3, RawQuartz('Normal')))

    factory.add_machine(Smelter('Caterium Ingot'))
    factory.add_machine(Smelter('Caterium Ingot'))
    factory.add_machine(Smelter('Caterium Ingot'))
    factory.add_machine(Smelter('Caterium Ingot'))
    factory.add_machine(Smelter('Caterium Ingot'))
    factory.add_machine(Smelter('Caterium Ingot'))
    factory.add_machine(Smelter('Caterium Ingot'))
    factory.add_machine(Smelter('Caterium Ingot'))
    factory.add_machine(Smelter('Caterium Ingot'))

    factory.add_machine(Constructor('Quickwire'))
    factory.add_machine(Constructor('Quickwire'))
    factory.add_machine(Constructor('Quickwire'))
    factory.add_machine(Constructor('Quickwire'))
    factory.add_machine(Constructor('Quickwire'))
    factory.add_machine(Constructor('Quickwire'))
    factory.add_machine(Constructor('Quickwire'))
    factory.add_machine(Constructor('Quickwire'))
    factory.add_machine(Constructor('Quickwire'))
    factory.add_machine(Constructor('Quickwire'))
    factory.add_machine(Constructor('Quickwire'))

    factory.add_machine(Constructor('Silica'))
    factory.add_machine(Constructor('Silica'))
    factory.add_machine(Constructor('Silica'))
    factory.add_machine(Constructor('Silica'))
    factory.add_machine(Constructor('Silica'))
    factory.add_machine(Constructor('Silica'))
    factory.add_machine(Constructor('Silica'))

    factory.add_machine(Manufacturer('Silicon High-Speed Connector'), Resource.HighSpeedConnector)
    factory.add_machine(Manufacturer('Silicon High-Speed Connector'), Resource.HighSpeedConnector)
    factory.add_machine(Manufacturer('Silicon High-Speed Connector'), Resource.HighSpeedConnector)
    factory.add_machine(Manufacturer('Silicon High-Speed Connector'), Resource.HighSpeedConnector)
    factory.add_machine(Manufacturer('Silicon High-Speed Connector'), Resource.HighSpeedConnector)
    factory.add_machine(Manufacturer('Silicon High-Speed Connector'), Resource.HighSpeedConnector)
    factory.add_machine(Manufacturer('Silicon High-Speed Connector'), Resource.HighSpeedConnector)

    return factory


def build_magnetic_field_generator_factory(versatile_framework_factory, electromagnetic_control_rod_factory, battery_factory):
    factory = Factory('Magnetic Field Generator Factory')

    factory.add_input(versatile_framework_factory)
    factory.add_input(electromagnetic_control_rod_factory)
    factory.add_input(battery_factory)

    factory.add_machine(Manufacturer('Magnetic Field Generator'), Resource.MagneticFieldGenerator)

    return factory


def build_modular_engine_factory(motor_factory, refinery, smart_plating_factory):
    factory = Factory('Modular Engine Factory')

    factory.add_input(motor_factory)
    factory.add_input(refinery)
    factory.add_input(smart_plating_factory)

    factory.add_machine(Manufacturer('Modular Engine'), Resource.ModularEngine)
    factory.add_machine(Manufacturer('Modular Engine'), Resource.ModularEngine)
    factory.add_machine(Manufacturer('Modular Engine'), Resource.ModularEngine)

    return factory


def build_modular_frame_factory(reinforced_iron_plate_factory):
    factory = Factory('Modular Frame Factory')

    factory.add_input(reinforced_iron_plate_factory)

    factory.add_input(Miner(3, IronOre('Normal')))

    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))

    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))

    factory.add_machine(Assembler('Modular Frame'), Resource.ModularFrame)
    factory.add_machine(Assembler('Modular Frame'), Resource.ModularFrame)
    factory.add_machine(Assembler('Modular Frame'), Resource.ModularFrame)
    factory.add_machine(Assembler('Modular Frame'), Resource.ModularFrame)
    factory.add_machine(Assembler('Modular Frame'), Resource.ModularFrame)
    factory.add_machine(Assembler('Modular Frame'), Resource.ModularFrame)
    factory.add_machine(Assembler('Modular Frame'), Resource.ModularFrame)
    factory.add_machine(Assembler('Modular Frame'), Resource.ModularFrame)
    factory.add_machine(Assembler('Modular Frame'), Resource.ModularFrame)
    factory.add_machine(Assembler('Modular Frame'), Resource.ModularFrame)
    factory.add_machine(Assembler('Modular Frame'), Resource.ModularFrame)
    factory.add_machine(Assembler('Modular Frame'), Resource.ModularFrame)
    factory.add_machine(Assembler('Modular Frame'), Resource.ModularFrame)

    return factory


def build_motor_factory(steel_foundry, stator_factory, rotor_factory):
    factory = Factory('Motor Factory')

    factory.add_input(steel_foundry)
    factory.add_input(stator_factory)
    factory.add_input(rotor_factory)

    factory.add_machine(Assembler('Motor'), Resource.Motor)
    factory.add_machine(Assembler('Motor'), Resource.Motor)
    factory.add_machine(Assembler('Motor'), Resource.Motor)

    return factory


def build_nuclear_pasta_factory(heavy_modular_frame_factory, pressure_conversion_cube_factory):
    factory = Factory('Nuclear Pasta Factory')

    factory.add_input(heavy_modular_frame_factory)
    factory.add_input(pressure_conversion_cube_factory)

    factory.add_input(Miner(3, CopperOre('Normal')))

    factory.add_input(WaterExtractor())
    factory.add_input(WaterExtractor())

    factory.add_machine(Refinery('Pure Copper Ingot'))
    factory.add_machine(Refinery('Pure Copper Ingot'))
    factory.add_machine(Refinery('Pure Copper Ingot'))
    factory.add_machine(Refinery('Pure Copper Ingot'))
    factory.add_machine(Refinery('Pure Copper Ingot'))
    factory.add_machine(Refinery('Pure Copper Ingot'))
    factory.add_machine(Refinery('Pure Copper Ingot'))
    factory.add_machine(Refinery('Pure Copper Ingot'))
    factory.add_machine(Refinery('Pure Copper Ingot'))
    factory.add_machine(Refinery('Pure Copper Ingot'))
    factory.add_machine(Refinery('Pure Copper Ingot'))
    factory.add_machine(Refinery('Pure Copper Ingot'))
    factory.add_machine(Refinery('Pure Copper Ingot'))
    factory.add_machine(Refinery('Pure Copper Ingot'))
    factory.add_machine(Refinery('Pure Copper Ingot'))
    factory.add_machine(Refinery('Pure Copper Ingot'))

    factory.add_machine(Constructor('Copper Powder'))
    factory.add_machine(Constructor('Copper Powder'))

    factory.add_machine(ParticleAccelerator('Nuclear Pasta'), Resource.NuclearPasta)

    return factory


def build_pressure_conversion_cube_factory(fused_modular_frame_factory, radio_control_unit_factory):
    factory = Factory('Pressure Conversion Cube Factory')

    factory.add_input(fused_modular_frame_factory)
    factory.add_input(radio_control_unit_factory)

    factory.add_machine(Assembler('Pressure Conversion Cube'), Resource.PressureConversionCube)
    factory.add_machine(Assembler('Pressure Conversion Cube'), Resource.PressureConversionCube)
    factory.add_machine(Assembler('Pressure Conversion Cube'), Resource.PressureConversionCube)

    return factory


def build_radio_control_unit_factory(heat_sink_factory, high_speed_connector_factory):
    factory = Factory('Radio Control Unit Factory')

    factory.add_input(heat_sink_factory)
    factory.add_input(high_speed_connector_factory)

    factory.add_input(Miner(3, RawQuartz('Normal')))

    factory.add_machine(Constructor('Quartz Crystal'))
    factory.add_machine(Constructor('Quartz Crystal'))
    factory.add_machine(Constructor('Quartz Crystal'))
    factory.add_machine(Constructor('Quartz Crystal'))

    factory.add_machine(Manufacturer('Radio Connection Unit'), Resource.RadioControlUnit)
    factory.add_machine(Manufacturer('Radio Connection Unit'), Resource.RadioControlUnit)

    return factory


def build_reinforced_iron_plate_factory():
    factory = Factory('Reinforced Iron Plate Factory')

    factory.add_input(Miner(3, IronOre('Normal')))
    factory.add_input(Miner(3, IronOre('Normal')))
    factory.add_input(Miner(3, IronOre('Normal')))

    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))

    factory.add_machine(Constructor('Iron Plate'))
    factory.add_machine(Constructor('Iron Plate'))
    factory.add_machine(Constructor('Iron Plate'))
    factory.add_machine(Constructor('Iron Plate'))
    factory.add_machine(Constructor('Iron Plate'))
    factory.add_machine(Constructor('Iron Plate'))
    factory.add_machine(Constructor('Iron Plate'))
    factory.add_machine(Constructor('Iron Plate'))
    factory.add_machine(Constructor('Iron Plate'))
    factory.add_machine(Constructor('Iron Plate'))
    factory.add_machine(Constructor('Iron Plate'))
    factory.add_machine(Constructor('Iron Plate'))
    factory.add_machine(Constructor('Iron Plate'))
    factory.add_machine(Constructor('Iron Plate'))
    factory.add_machine(Constructor('Iron Plate'))

    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))

    factory.add_machine(Assembler('Reinforced Iron Plate'), Resource.ReinforcedIronPlate)
    factory.add_machine(Assembler('Reinforced Iron Plate'), Resource.ReinforcedIronPlate)
    factory.add_machine(Assembler('Reinforced Iron Plate'), Resource.ReinforcedIronPlate)
    factory.add_machine(Assembler('Reinforced Iron Plate'), Resource.ReinforcedIronPlate)
    factory.add_machine(Assembler('Reinforced Iron Plate'), Resource.ReinforcedIronPlate)
    factory.add_machine(Assembler('Reinforced Iron Plate'), Resource.ReinforcedIronPlate)
    factory.add_machine(Assembler('Reinforced Iron Plate'), Resource.ReinforcedIronPlate)
    factory.add_machine(Assembler('Reinforced Iron Plate'), Resource.ReinforcedIronPlate)
    factory.add_machine(Assembler('Reinforced Iron Plate'), Resource.ReinforcedIronPlate)
    factory.add_machine(Assembler('Reinforced Iron Plate'), Resource.ReinforcedIronPlate)

    return factory


def build_refinery():
    factory = Factory('Refinery')

    factory.add_input(OilExtractor(CrudeOil('Pure')))
    factory.add_input(OilExtractor(CrudeOil('Pure')))
    factory.add_input(OilExtractor(CrudeOil('Pure')))

    factory.add_machine(Refinery('Rubber'), Resource.Rubber)
    factory.add_machine(Refinery('Rubber'), Resource.Rubber)
    factory.add_machine(Refinery('Rubber'), Resource.Rubber)
    factory.add_machine(Refinery('Rubber'), Resource.Rubber)
    factory.add_machine(Refinery('Rubber'), Resource.Rubber)
    factory.add_machine(Refinery('Rubber'), Resource.Rubber)
    factory.add_machine(Refinery('Rubber'), Resource.Rubber)
    factory.add_machine(Refinery('Rubber'), Resource.Rubber)
    factory.add_machine(Refinery('Rubber'), Resource.Rubber)
    factory.add_machine(Refinery('Rubber'), Resource.Rubber)
    factory.add_machine(Refinery('Rubber'), Resource.Rubber)

    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)
    factory.add_machine(Refinery('Plastic'), Resource.Plastic)

    # # Sink the heavy oil residue into fuel and convert to power
    factory.add_machine(Refinery('Residual Fuel'))
    factory.add_machine(Refinery('Residual Fuel'))
    factory.add_machine(Refinery('Residual Fuel'))
    factory.add_machine(Refinery('Residual Fuel'))
    factory.add_machine(Refinery('Residual Fuel'))
    factory.add_machine(Refinery('Residual Fuel'))
    factory.add_machine(Refinery('Residual Fuel'))
    factory.add_machine(Refinery('Residual Fuel'))
    factory.add_machine(Refinery('Residual Fuel'))
    factory.add_machine(Refinery('Residual Fuel', clock_speed_modifier=30/60))

    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel'))
    factory.add_machine(FuelGenerator('Fuel', allow_undersupply=True))

    return factory


def build_rotor_factory():
    factory = Factory('Rotor Factory')

    factory.add_input(Miner(3, IronOre('Normal')))
    factory.add_input(Miner(3, IronOre('Normal')))

    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))

    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))

    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))
    factory.add_machine(Constructor('Cast Screw'))

    factory.add_machine(Assembler('Rotor'), Resource.Rotor)
    factory.add_machine(Assembler('Rotor'), Resource.Rotor)
    factory.add_machine(Assembler('Rotor'), Resource.Rotor)
    factory.add_machine(Assembler('Rotor'), Resource.Rotor)
    factory.add_machine(Assembler('Rotor'), Resource.Rotor)
    factory.add_machine(Assembler('Rotor'), Resource.Rotor)
    factory.add_machine(Assembler('Rotor'), Resource.Rotor)
    factory.add_machine(Assembler('Rotor'), Resource.Rotor)
    factory.add_machine(Assembler('Rotor'), Resource.Rotor)

    return factory


def build_smart_plating_factory(reinforced_iron_plate_factory, rotor_factory):
    factory = Factory('Smart Plating Factory')

    factory.add_input(reinforced_iron_plate_factory)
    factory.add_input(rotor_factory)

    factory.add_machine(Assembler('Smart Plating'), Resource.SmartPlating)
    factory.add_machine(Assembler('Smart Plating'), Resource.SmartPlating)
    factory.add_machine(Assembler('Smart Plating'), Resource.SmartPlating)

    return factory


def build_stator_factory(steel_foundry):
    factory = Factory('Stator Factory')

    factory.add_input(steel_foundry)

    factory.add_input(Miner(3, CopperOre('Normal')))
    factory.add_input(Miner(3, CopperOre('Normal')))

    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))

    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))

    factory.add_machine(Assembler('Stator'), Resource.Stator)
    factory.add_machine(Assembler('Stator'), Resource.Stator)
    factory.add_machine(Assembler('Stator'), Resource.Stator)
    factory.add_machine(Assembler('Stator'), Resource.Stator)
    factory.add_machine(Assembler('Stator'), Resource.Stator)
    factory.add_machine(Assembler('Stator'), Resource.Stator)
    factory.add_machine(Assembler('Stator'), Resource.Stator)
    factory.add_machine(Assembler('Stator'), Resource.Stator)
    factory.add_machine(Assembler('Stator'), Resource.Stator)
    factory.add_machine(Assembler('Stator'), Resource.Stator)
    factory.add_machine(Assembler('Stator'), Resource.Stator)
    factory.add_machine(Assembler('Stator'), Resource.Stator)
    factory.add_machine(Assembler('Stator'), Resource.Stator)
    factory.add_machine(Assembler('Stator'), Resource.Stator)

    return factory


def build_steel_foundry():
    factory = Factory('Steel Foundry')

    factory.add_input(Miner(3, IronOre('Normal')))
    factory.add_input(Miner(3, IronOre('Normal')))
    factory.add_input(Miner(3, IronOre('Normal')))

    factory.add_input(Miner(3, Coal('Normal')))
    factory.add_input(Miner(3, Coal('Normal')))
    factory.add_input(Miner(3, Coal('Normal')))

    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))

    factory.add_machine(Foundry('Solid Steel Ingot'))
    factory.add_machine(Foundry('Solid Steel Ingot'))
    factory.add_machine(Foundry('Solid Steel Ingot'))
    factory.add_machine(Foundry('Solid Steel Ingot'))
    factory.add_machine(Foundry('Solid Steel Ingot'))
    factory.add_machine(Foundry('Solid Steel Ingot'))
    factory.add_machine(Foundry('Solid Steel Ingot'))
    factory.add_machine(Foundry('Solid Steel Ingot'))
    factory.add_machine(Foundry('Solid Steel Ingot'))
    factory.add_machine(Foundry('Solid Steel Ingot'))
    factory.add_machine(Foundry('Solid Steel Ingot'))
    factory.add_machine(Foundry('Solid Steel Ingot'))
    factory.add_machine(Foundry('Solid Steel Ingot'))
    factory.add_machine(Foundry('Solid Steel Ingot'))
    factory.add_machine(Foundry('Solid Steel Ingot'))
    factory.add_machine(Foundry('Solid Steel Ingot'))

    factory.add_machine(Constructor('Steel Beam'), Resource.SteelBeam)
    factory.add_machine(Constructor('Steel Beam'), Resource.SteelBeam)

    factory.add_machine(Constructor('Steel Pipe'), Resource.SteelPipe)
    factory.add_machine(Constructor('Steel Pipe'), Resource.SteelPipe)
    factory.add_machine(Constructor('Steel Pipe'), Resource.SteelPipe)
    factory.add_machine(Constructor('Steel Pipe'), Resource.SteelPipe)
    factory.add_machine(Constructor('Steel Pipe'), Resource.SteelPipe)
    factory.add_machine(Constructor('Steel Pipe'), Resource.SteelPipe)
    factory.add_machine(Constructor('Steel Pipe'), Resource.SteelPipe)
    factory.add_machine(Constructor('Steel Pipe'), Resource.SteelPipe)
    factory.add_machine(Constructor('Steel Pipe'), Resource.SteelPipe)
    factory.add_machine(Constructor('Steel Pipe'), Resource.SteelPipe)
    factory.add_machine(Constructor('Steel Pipe'), Resource.SteelPipe)
    factory.add_machine(Constructor('Steel Pipe'), Resource.SteelPipe)
    factory.add_machine(Constructor('Steel Pipe'), Resource.SteelPipe)
    factory.add_machine(Constructor('Steel Pipe'), Resource.SteelPipe)
    factory.add_machine(Constructor('Steel Pipe'), Resource.SteelPipe)
    factory.add_machine(Constructor('Steel Pipe'), Resource.SteelPipe)
    factory.add_machine(Constructor('Steel Pipe'), Resource.SteelPipe)
    factory.add_machine(Constructor('Steel Pipe'), Resource.SteelPipe)
    factory.add_machine(Constructor('Steel Pipe'), Resource.SteelPipe)
    factory.add_machine(Constructor('Steel Pipe'), Resource.SteelPipe)
    factory.add_machine(Constructor('Steel Pipe'), Resource.SteelPipe)
    factory.add_machine(Constructor('Steel Pipe'), Resource.SteelPipe)
    factory.add_machine(Constructor('Steel Pipe'), Resource.SteelPipe)
    factory.add_machine(Constructor('Steel Pipe'), Resource.SteelPipe)
    factory.add_machine(Constructor('Steel Pipe'), Resource.SteelPipe)
    factory.add_machine(Constructor('Steel Pipe'), Resource.SteelPipe)
    factory.add_machine(Constructor('Steel Pipe'), Resource.SteelPipe)

    return factory


def build_supercomputer_factory(computer_factory, ai_limiter_factory, high_speed_connector_factory, refinery):
    factory = Factory('Supercomputer Factory')

    factory.add_input(computer_factory)
    factory.add_input(ai_limiter_factory)
    factory.add_input(high_speed_connector_factory)
    factory.add_input(refinery)

    factory.add_machine(Manufacturer('Supercomputer'))

    return factory


def build_thermal_propulsion_rocket_factory(modular_engine_factory, turbo_motor_factory, cooling_system_factory, fused_modular_frame_factory):
    factory = Factory('Thermal Propulsion Rocket Factory')

    factory.add_input(modular_engine_factory)
    factory.add_input(turbo_motor_factory)
    factory.add_input(cooling_system_factory)
    factory.add_input(fused_modular_frame_factory)

    factory.add_machine(Manufacturer('Thermal Propulsion Rocket'))

    return factory


def build_turbo_motor_factory(motor_factory, pressure_conversion_cube_factory, stator_factory, battery_factory):
    factory = Factory('Turbo Motor Factory')

    factory.add_input(motor_factory)
    factory.add_input(pressure_conversion_cube_factory)
    factory.add_input(stator_factory)
    factory.add_input(battery_factory)

    factory.add_input(ResourceWellExtractor(NitrogenGas('Normal')))
    factory.add_input(ResourceWellExtractor(NitrogenGas('Normal')))
    factory.add_input(ResourceWellExtractor(NitrogenGas('Normal')))
    factory.add_input(ResourceWellExtractor(NitrogenGas('Normal')))

    factory.add_machine(Packager('Packaged Nitrogen Gas'))

    factory.add_machine(Manufacturer('Turbo Pressure Motor'), Resource.TurboMotor)

    return factory


def build_versatile_framework_factory(modular_frame_factory, steel_foundry):
    factory = Factory('Versatile Framework Factory')

    factory.add_input(modular_frame_factory)
    factory.add_input(steel_foundry)

    factory.add_machine(Assembler('Versatile Framework'), Resource.VersatileFramework)

    return factory


if __name__ == '__main__':
    session = Session()

    # ---------------------------------------------------------------------------------------------------------------- #
    # STEP 1
    # ---------------------------------------------------------------------------------------------------------------- #
    # Build Reinforced Iron Plate and Rotor factories and then build the Smart Plating factory that will complete
    # Tier 1 of the space elevator
    reinforced_iron_plate_factory = build_reinforced_iron_plate_factory()
    rotor_factory = build_rotor_factory()

    smart_plating_factory = build_smart_plating_factory(reinforced_iron_plate_factory, rotor_factory)
    session.add_factories(reinforced_iron_plate_factory, rotor_factory, smart_plating_factory)
    session.visualize_factory_relationships('Tier 1.html')

    # ---------------------------------------------------------------------------------------------------------------- #
    # STEP 2
    # ---------------------------------------------------------------------------------------------------------------- #
    # Build factories for modular frames, steel production, and stators. These new factories allow versatile frameworks,
    # automated wiring, and the smart plating from step 1 to complete Space Elevator Tier 2
    modular_frame_factory = build_modular_frame_factory(reinforced_iron_plate_factory)
    steel_foundry = build_steel_foundry()
    stator_factory = build_stator_factory(steel_foundry)

    versatile_framework_factory = build_versatile_framework_factory(modular_frame_factory, steel_foundry)
    automated_wiring_factory = build_automated_wiring_factory(stator_factory)
    session.add_factories(modular_frame_factory, steel_foundry, stator_factory, versatile_framework_factory, automated_wiring_factory)
    session.visualize_factory_relationships('Tier 2.html')

    # ---------------------------------------------------------------------------------------------------------------- #
    # STEP 3
    # ---------------------------------------------------------------------------------------------------------------- #
    # Build factories for motors, circuit boards, heavy modular frame factories and a refinery and then build the
    # modular engine and adaptive control unit factories to complete Space Elevator Tier 3, also using the versativle
    # framework factory from step 2.
    motor_factory = build_motor_factory(steel_foundry, stator_factory, rotor_factory)
    refinery = build_refinery()
    circuit_board_factory = build_circuit_board_factory(refinery)
    heavy_modular_frame_factory = build_heavy_modular_frame_factory(steel_foundry, reinforced_iron_plate_factory, modular_frame_factory)
    computer_factory = build_computer_factory(refinery, circuit_board_factory)

    modular_engine_factory = build_modular_engine_factory(motor_factory, refinery, smart_plating_factory)
    adaptive_control_unit_factory = build_adaptive_control_unit_factory(automated_wiring_factory, circuit_board_factory, heavy_modular_frame_factory, computer_factory)
    session.add_factories(motor_factory, refinery, circuit_board_factory, heavy_modular_frame_factory, computer_factory, modular_engine_factory, adaptive_control_unit_factory)
    session.visualize_factory_relationships('Tier 3.html')

    # ---------------------------------------------------------------------------------------------------------------- #
    # STEP 4
    # ---------------------------------------------------------------------------------------------------------------- #
    ai_limiter_factory = build_ai_limiter_factory()
    high_speed_connector_factory = build_high_speed_connector_factory(circuit_board_factory)
    supercomputer_factory = build_supercomputer_factory(computer_factory, ai_limiter_factory, high_speed_connector_factory, refinery)
    electromagnetic_control_rod_factory = build_electromagnetic_control_rod_factory(stator_factory, ai_limiter_factory)
    battery_factory = build_battery_factory(refinery)
    fused_modular_frame_factory = build_fused_modular_frame_factory(heavy_modular_frame_factory, battery_factory)
    crystal_oscillator_factory = build_crystal_oscillator_factory(reinforced_iron_plate_factory)
    heat_sink_factory = build_heat_sink_factory(battery_factory, refinery)
    radio_control_unit_factory = build_radio_control_unit_factory(heat_sink_factory, high_speed_connector_factory)
    pressure_conversion_cube_factory = build_pressure_conversion_cube_factory(fused_modular_frame_factory, radio_control_unit_factory)
    turbo_motor_factory = build_turbo_motor_factory(motor_factory, pressure_conversion_cube_factory, stator_factory, battery_factory)
    cooling_system_factory = build_cooling_system_factory(heat_sink_factory, refinery)

    assembly_director_system_factory = build_assembly_director_system_factory(adaptive_control_unit_factory, supercomputer_factory)
    magnetic_field_generator_factory = build_magnetic_field_generator_factory(versatile_framework_factory, electromagnetic_control_rod_factory, battery_factory)
    nuclear_pasta_factory = build_nuclear_pasta_factory(heavy_modular_frame_factory, pressure_conversion_cube_factory)
    thermal_propulsion_rocket_factory = build_thermal_propulsion_rocket_factory(modular_engine_factory, turbo_motor_factory, cooling_system_factory, fused_modular_frame_factory)
    session.add_factories(ai_limiter_factory, high_speed_connector_factory, supercomputer_factory, electromagnetic_control_rod_factory, battery_factory, fused_modular_frame_factory,
                          crystal_oscillator_factory, radio_control_unit_factory, pressure_conversion_cube_factory, heat_sink_factory, cooling_system_factory, turbo_motor_factory,
                          assembly_director_system_factory, magnetic_field_generator_factory, nuclear_pasta_factory, thermal_propulsion_rocket_factory)
    session.visualize_factory_relationships('Tier 4.html')
