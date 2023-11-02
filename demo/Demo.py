import os
import sys
from SatisfactoryPlanner.Resource.Oil import CrudeOil
from SatisfactoryPlanner.Resource.Ore import CateriumOre, Coal, CopperOre, IronOre, Limestone

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from SatisfactoryPlanner.Factory.Factory import Miner, Factory, OilExtractor
from SatisfactoryPlanner.Machines.Machines import Smelter, Constructor, Assembler, Foundry, Manufacturer, Refinery, \
    FuelGenerator
from SatisfactoryPlanner.Session.Session import Session


def build_adaptive_control_unit_factory(automated_wiring_factory, circuit_board_factory, heavy_modular_frame_factory, computer_factory):
    factory = Factory('Adaptive Control Unit Factory')

    factory.add_input(automated_wiring_factory)
    factory.add_input(circuit_board_factory)
    factory.add_input(heavy_modular_frame_factory)
    factory.add_input(computer_factory)

    factory.add_machine(Manufacturer('Adaptive Control Unit'))
    factory.add_machine(Manufacturer('Adaptive Control Unit'))

    return factory


def build_ai_limiter_factory():
    factory = Factory('AI Limiter Factory')

    factory.add_input(Miner(3, CopperOre('Normal')))

    factory.add_input(Miner(3, CateriumOre('Normal')))

    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))

    factory.add_machine(Smelter('Caterium Ingot'))
    factory.add_machine(Smelter('Caterium Ingot'))

    factory.add_machine(Constructor('Copper Sheet'))
    factory.add_machine(Constructor('Copper Sheet'))
    factory.add_machine(Constructor('Copper Sheet'))

    factory.add_machine(Constructor('Quickwire'))
    factory.add_machine(Constructor('Quickwire'))

    factory.add_machine(Assembler('AI Limiter'))

    return factory


def build_assembly_director_system_factory(adaptive_control_unit_factory, supercomputer_factory):
    factory = Factory('Assembly Directory System Factory')

    factory.add_input(adaptive_control_unit_factory)
    factory.add_input(supercomputer_factory)

    factory.add_machine(Assembler('Assembly Director System'))

    return factory


def build_automated_wiring_factory(stator_factory):
    factory = Factory('Automated Wiring Factory')

    factory.add_input(stator_factory)

    factory.add_input(Miner(2, CopperOre('Normal')))
    factory.add_input(Miner(2, CopperOre('Normal')))
    factory.add_input(Miner(2, CopperOre('Normal')))

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

    factory.add_machine(Assembler('Automated Wiring'))
    factory.add_machine(Assembler('Automated Wiring'))
    factory.add_machine(Assembler('Automated Wiring'))
    factory.add_machine(Assembler('Automated Wiring'))
    factory.add_machine(Assembler('Automated Wiring'))
    factory.add_machine(Assembler('Automated Wiring'))

    return factory


def build_circuit_board_factory(refinery):
    factory = Factory('Circuit Board Factory')

    factory.add_input(refinery)

    factory.add_input(Miner(2, CopperOre('Normal')))
    factory.add_input(Miner(2, CopperOre('Normal')))
    factory.add_input(Miner(2, CopperOre('Normal')))
    factory.add_input(Miner(2, CopperOre('Normal')))

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

    factory.add_machine(Assembler('Circuit Board'))
    factory.add_machine(Assembler('Circuit Board'))
    factory.add_machine(Assembler('Circuit Board'))
    factory.add_machine(Assembler('Circuit Board'))
    factory.add_machine(Assembler('Circuit Board'))
    factory.add_machine(Assembler('Circuit Board'))
    factory.add_machine(Assembler('Circuit Board'))
    factory.add_machine(Assembler('Circuit Board'))
    factory.add_machine(Assembler('Circuit Board'))
    factory.add_machine(Assembler('Circuit Board'))
    factory.add_machine(Assembler('Circuit Board'))
    factory.add_machine(Assembler('Circuit Board'))
    factory.add_machine(Assembler('Circuit Board'))

    return factory


def build_computer_factory(refinery, circuit_board_factory):
    factory = Factory('Computer Factory')

    factory.add_input(refinery)
    factory.add_input(circuit_board_factory)

    factory.add_input(Miner(2, CopperOre('Normal')))

    factory.add_input(Miner(2, IronOre('Normal')))

    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))

    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))

    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))

    factory.add_machine(Constructor('Cable'))
    factory.add_machine(Constructor('Cable'))
    factory.add_machine(Constructor('Cable'))

    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))

    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))

    factory.add_machine(Manufacturer('Computer'))
    factory.add_machine(Manufacturer('Computer'))
    factory.add_machine(Manufacturer('Computer'))

    return factory


def build_heavy_modular_frame_factory(steel_foundry, reinforced_iron_plate_factory, modular_frame_factory):
    factory = Factory('Heavy Modular Frame Factory')

    factory.add_input(steel_foundry)
    factory.add_input(reinforced_iron_plate_factory)
    factory.add_input(modular_frame_factory)

    factory.add_input(Miner(2, IronOre('Normal')))
    factory.add_input(Miner(2, IronOre('Normal')))
    factory.add_input(Miner(2, IronOre('Normal')))
    factory.add_input(Miner(2, Limestone('Normal')))
    factory.add_input(Miner(2, Limestone('Normal')))

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

    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))

    factory.add_machine(Constructor('Concrete'))
    factory.add_machine(Constructor('Concrete'))
    factory.add_machine(Constructor('Concrete'))
    factory.add_machine(Constructor('Concrete'))

    factory.add_machine(Assembler('Encased Industrial Beam'))
    factory.add_machine(Assembler('Encased Industrial Beam'))

    factory.add_machine(Manufacturer('Heavy Modular Frame'))

    return factory


def build_high_speed_connector_factory(circuit_board_factory):
    factory = Factory('High-Speed Connector Factory')

    factory.add_input(circuit_board_factory)

    factory.add_input(Miner(3, CateriumOre('Normal')))
    factory.add_input(Miner(3, CateriumOre('Normal')))

    factory.add_input(Miner(3, CopperOre('Normal')))

    factory.add_machine(Smelter('Caterium Ingot'))
    factory.add_machine(Smelter('Caterium Ingot'))
    factory.add_machine(Smelter('Caterium Ingot'))
    factory.add_machine(Smelter('Caterium Ingot'))
    factory.add_machine(Smelter('Caterium Ingot'))
    factory.add_machine(Smelter('Caterium Ingot'))
    factory.add_machine(Smelter('Caterium Ingot'))
    factory.add_machine(Smelter('Caterium Ingot'))

    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))
    factory.add_machine(Smelter('Copper Ingot'))

    factory.add_machine(Constructor('Quickwire'))
    factory.add_machine(Constructor('Quickwire'))
    factory.add_machine(Constructor('Quickwire'))
    factory.add_machine(Constructor('Quickwire'))
    factory.add_machine(Constructor('Quickwire'))
    factory.add_machine(Constructor('Quickwire'))
    factory.add_machine(Constructor('Quickwire'))
    factory.add_machine(Constructor('Quickwire'))
    factory.add_machine(Constructor('Quickwire'))

    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))
    factory.add_machine(Constructor('Wire'))

    factory.add_machine(Constructor('Cable'))
    factory.add_machine(Constructor('Cable'))
    factory.add_machine(Constructor('Cable'))

    factory.add_machine(Manufacturer('High-Speed Connector'))
    factory.add_machine(Manufacturer('High-Speed Connector'))

    return factory


def build_magnetic_field_generator_factory(versatile_framework_factory):
    factory = Factory('Magnetic Field Generator Factory')

    factory.add_input(versatile_framework_factory)

    factory.add_machine(Manufacturer('Magnetic Field Generator'))

    return factory


def build_modular_engine_factory(motor_factory, refinery, smart_plating_factory):
    factory = Factory('Modular Engine Factory')

    factory.add_input(motor_factory)
    factory.add_input(refinery)
    factory.add_input(smart_plating_factory)

    factory.add_machine(Manufacturer('Modular Engine'))

    return factory


def build_modular_frame_factory(reinforced_iron_plate_factory):
    factory = Factory('Modular Frame Factory')

    factory.add_input(reinforced_iron_plate_factory)

    factory.add_input(Miner(2, IronOre('Normal')))

    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))
    factory.add_machine(Smelter('Iron Ingot'))

    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))

    factory.add_machine(Assembler('Modular Frame'))
    factory.add_machine(Assembler('Modular Frame'))
    factory.add_machine(Assembler('Modular Frame'))
    factory.add_machine(Assembler('Modular Frame'))
    factory.add_machine(Assembler('Modular Frame'))
    factory.add_machine(Assembler('Modular Frame'))
    factory.add_machine(Assembler('Modular Frame'))

    return factory


def build_motor_factory(steel_foundry, stator_factory, rotor_factory):
    factory = Factory('Motor Factory')

    factory.add_input(steel_foundry)
    factory.add_input(stator_factory)
    factory.add_input(rotor_factory)

    factory.add_machine(Assembler('Motor'))

    return factory


def build_nuclear_pasta_factor():
    factory = Factory('Nuclear Pasta Factory')

    factory.add_machine(ParticleAccelerator('Nuclear Pasta'))

    return factory


def build_reinforced_iron_plate_factory():
    factory = Factory('Reinforced Iron Plate Factory')

    factory.add_input(Miner(1, IronOre('Normal')))
    factory.add_input(Miner(1, IronOre('Normal')))
    factory.add_input(Miner(1, IronOre('Normal')))
    factory.add_input(Miner(1, IronOre('Normal')))
    factory.add_input(Miner(1, IronOre('Normal')))
    factory.add_input(Miner(1, IronOre('Normal')))

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

    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))
    factory.add_machine(Constructor('Iron Rod'))

    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))

    factory.add_machine(Assembler('Reinforced Iron Plate'))
    factory.add_machine(Assembler('Reinforced Iron Plate'))
    factory.add_machine(Assembler('Reinforced Iron Plate'))
    factory.add_machine(Assembler('Reinforced Iron Plate'))
    factory.add_machine(Assembler('Reinforced Iron Plate'))

    return factory


def build_refinery():
    factory = Factory('Refinery')

    factory.add_input(OilExtractor(CrudeOil('Normal')))
    factory.add_input(OilExtractor(CrudeOil('Normal')))
    factory.add_input(OilExtractor(CrudeOil('Normal')))
    factory.add_input(OilExtractor(CrudeOil('Normal')))
    factory.add_input(OilExtractor(CrudeOil('Normal')))
    factory.add_input(OilExtractor(CrudeOil('Normal')))
    factory.add_input(OilExtractor(CrudeOil('Normal')))
    factory.add_input(OilExtractor(CrudeOil('Normal')))

    factory.add_machine(Refinery('Rubber'))
    factory.add_machine(Refinery('Plastic'))
    factory.add_machine(Refinery('Plastic'))
    factory.add_machine(Refinery('Plastic'))
    factory.add_machine(Refinery('Plastic'))
    factory.add_machine(Refinery('Plastic'))
    factory.add_machine(Refinery('Plastic'))
    factory.add_machine(Refinery('Plastic'))
    factory.add_machine(Refinery('Plastic'))
    factory.add_machine(Refinery('Plastic'))
    factory.add_machine(Refinery('Plastic'))
    factory.add_machine(Refinery('Plastic'))
    factory.add_machine(Refinery('Plastic'))
    factory.add_machine(Refinery('Plastic'))
    factory.add_machine(Refinery('Plastic'))
    factory.add_machine(Refinery('Plastic'))
    factory.add_machine(Refinery('Plastic'))
    factory.add_machine(Refinery('Plastic'))
    factory.add_machine(Refinery('Plastic'))
    factory.add_machine(Refinery('Plastic'))
    factory.add_machine(Refinery('Plastic'))
    factory.add_machine(Refinery('Plastic'))
    factory.add_machine(Refinery('Plastic'))
    factory.add_machine(Refinery('Plastic'))
    factory.add_machine(Refinery('Plastic'))
    factory.add_machine(Refinery('Plastic'))
    factory.add_machine(Refinery('Plastic'))
    factory.add_machine(Refinery('Plastic'))
    factory.add_machine(Refinery('Plastic'))
    factory.add_machine(Refinery('Plastic'))
    factory.add_machine(Refinery('Plastic'))


    # Sink the heavy oil residue into fuel and convert to power
    factory.add_machine(Refinery('Residual Fuel'))
    factory.add_machine(Refinery('Residual Fuel'))
    factory.add_machine(Refinery('Residual Fuel'))
    factory.add_machine(Refinery('Residual Fuel'))
    factory.add_machine(Refinery('Residual Fuel'))
    factory.add_machine(Refinery('Residual Fuel', clock_speed_modifier=20/60))
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

    factory.add_input(Miner(1, IronOre('Normal')))
    factory.add_input(Miner(1, IronOre('Normal')))
    factory.add_input(Miner(1, IronOre('Normal')))

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

    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))
    factory.add_machine(Constructor('Screw'))

    factory.add_machine(Assembler('Rotor'))
    factory.add_machine(Assembler('Rotor'))
    factory.add_machine(Assembler('Rotor'))

    return factory


def build_smart_plating_factory(reinforced_iron_plate_factory, rotor_factory):
    factory = Factory('Smart Plating Factory')

    factory.add_input(reinforced_iron_plate_factory)
    factory.add_input(rotor_factory)

    factory.add_machine(Assembler('Smart Plating'))

    return factory


def build_stator_factory(steel_foundry):
    factory = Factory('Stator Factory')

    factory.add_input(steel_foundry)

    factory.add_input(Miner(2, CopperOre('Normal')))

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

    factory.add_machine(Assembler('Stator'))
    factory.add_machine(Assembler('Stator'))
    factory.add_machine(Assembler('Stator'))
    factory.add_machine(Assembler('Stator'))
    factory.add_machine(Assembler('Stator'))

    return factory


def build_steel_foundry():
    factory = Factory('Steel Foundry')

    factory.add_input(Miner(2, IronOre('Normal')))
    factory.add_input(Miner(2, IronOre('Normal')))
    factory.add_input(Miner(2, IronOre('Normal')))
    factory.add_input(Miner(2, IronOre('Normal')))
    factory.add_input(Miner(2, IronOre('Normal')))

    factory.add_input(Miner(2, Coal('Normal')))
    factory.add_input(Miner(2, Coal('Normal')))
    factory.add_input(Miner(2, Coal('Normal')))
    factory.add_input(Miner(2, Coal('Normal')))
    factory.add_input(Miner(2, Coal('Normal')))

    factory.add_machine(Foundry('Steel Ingot'))
    factory.add_machine(Foundry('Steel Ingot'))
    factory.add_machine(Foundry('Steel Ingot'))
    factory.add_machine(Foundry('Steel Ingot'))
    factory.add_machine(Foundry('Steel Ingot'))
    factory.add_machine(Foundry('Steel Ingot'))
    factory.add_machine(Foundry('Steel Ingot'))
    factory.add_machine(Foundry('Steel Ingot'))
    factory.add_machine(Foundry('Steel Ingot'))
    factory.add_machine(Foundry('Steel Ingot'))
    factory.add_machine(Foundry('Steel Ingot'))
    factory.add_machine(Foundry('Steel Ingot'))

    factory.add_machine(Constructor('Steel Beam'))
    factory.add_machine(Constructor('Steel Beam'))
    factory.add_machine(Constructor('Steel Beam'))
    factory.add_machine(Constructor('Steel Beam'))
    factory.add_machine(Constructor('Steel Beam'))
    factory.add_machine(Constructor('Steel Beam'))

    factory.add_machine(Constructor('Steel Pipe'))
    factory.add_machine(Constructor('Steel Pipe'))
    factory.add_machine(Constructor('Steel Pipe'))
    factory.add_machine(Constructor('Steel Pipe'))
    factory.add_machine(Constructor('Steel Pipe'))
    factory.add_machine(Constructor('Steel Pipe'))

    return factory


def build_supercomputer_factory(computer_factory, ai_limiter_factory, high_speed_connector_factory, refinery):
    factory = Factory('Supercomputer Factory')

    factory.add_input(computer_factory)
    factory.add_input(ai_limiter_factory)
    factory.add_input(high_speed_connector_factory)
    factory.add_input(refinery)

    factory.add_machine(Manufacturer('Supercomputer'))

    return factory


def build_thermal_propulsion_rocket_factory():
    factory = Factory('Thermal Propulsion Rocket Factory')

    factory.add_machine(Manufacturer('Thermal Propulsion Rocket Factory'))

    return factory


def build_versatile_framework_factory(modular_frame_factory, steel_foundry):
    factory = Factory('Versatile Framework Factory')

    factory.add_input(modular_frame_factory)
    factory.add_input(steel_foundry)

    factory.add_machine(Assembler('Versatile Framework'))

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

    assembly_director_system_factory = build_assembly_director_system_factory(adaptive_control_unit_factory, supercomputer_factory)
    magnetic_field_generator_factory = build_magnetic_field_generator_factory(versatile_framework_factory)
    nuclear_pasta_factory = build_nuclear_pasta_factor()
    thermal_propulsion_rocket_factory = build_thermal_propulsion_rocket_factory()