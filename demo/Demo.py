import os
import sys
from SatisfactoryPlanner.Resource.Oil import CrudeOil
from SatisfactoryPlanner.Resource.Ore import Coal, CopperOre, IronOre, Limestone

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from SatisfactoryPlanner.Factory.Factory import Miner, Factory, OilExtractor
from SatisfactoryPlanner.Machines.Machines import Smelter, Constructor, Assembler, Foundry, Manufacturer, Refinery, FuelGenerator
from SatisfactoryPlanner.Session.Session import Session


def foundry_factory():
    # Refinery Factory
    rf = Factory('Refinery')

    rf.add_input(OilExtractor(CrudeOil('Normal')))
    rf.add_input(OilExtractor(CrudeOil('Normal')))
    rf.add_input(OilExtractor(CrudeOil('Normal')))

    rf.add_machine(Refinery('Rubber'))
    rf.add_machine(Refinery('Plastic'))
    rf.add_machine(Refinery('Plastic'))
    rf.add_machine(Refinery('Plastic'))
    rf.add_machine(Refinery('Plastic'))
    rf.add_machine(Refinery('Plastic'))
    rf.add_machine(Refinery('Plastic'))
    rf.add_machine(Refinery('Plastic'))
    rf.add_machine(Refinery('Plastic'))
    rf.add_machine(Refinery('Plastic'))

    # Sink the heavy oil residue into fuel and convert to power
    rf.add_machine(Refinery('Residual Fuel', clock_speed_modifier=110 / 60))
    rf.add_machine(FuelGenerator('Fuel'))
    rf.add_machine(FuelGenerator('Fuel'))
    rf.add_machine(FuelGenerator('Fuel'))
    rf.add_machine(FuelGenerator('Fuel'))
    rf.add_machine(FuelGenerator('Fuel'))
    rf.add_machine(FuelGenerator('Fuel'))
    rf.add_machine(FuelGenerator('Fuel', allow_undersupply=True))

    return rf


def reinforced_iron_plate_factory():
    ripf = Factory('Reinforced Iron Plate Factory')

    ripf.add_input(Miner(1, IronOre('Normal')))
    ripf.add_input(Miner(1, IronOre('Normal')))

    ripf.add_machine(Smelter('Iron Ingot'))
    ripf.add_machine(Smelter('Iron Ingot'))
    ripf.add_machine(Smelter('Iron Ingot'))

    ripf.add_machine(Constructor('Iron Plate'))
    ripf.add_machine(Constructor('Iron Plate'))

    ripf.add_machine(Constructor('Iron Rod'))
    ripf.add_machine(Constructor('Iron Rod'))

    ripf.add_machine(Constructor('Screw'))
    ripf.add_machine(Constructor('Screw'))

    ripf.add_machine(Assembler('Reinforced Iron Plate'))

    return ripf


def rotor_factory():
    rf = Factory('Rotor Factory')

    rf.add_input(Miner(1, IronOre('Normal')))

    rf.add_machine(Smelter('Iron Ingot'))
    rf.add_machine(Smelter('Iron Ingot'))

    rf.add_machine(Constructor('Iron Rod'))
    rf.add_machine(Constructor('Iron Rod'))
    rf.add_machine(Constructor('Iron Rod'))
    rf.add_machine(Constructor('Iron Rod'))

    rf.add_machine(Constructor('Screw'))
    rf.add_machine(Constructor('Screw'))
    rf.add_machine(Constructor('Screw'))

    rf.add_machine(Assembler('Rotor'))

    return rf


def steel_foundry_factory():
    sff = Factory('Steel Foundry')

    sff.add_input(Miner(1, IronOre('Normal')))
    sff.add_input(Miner(1, IronOre('Normal')))
    sff.add_input(Miner(1, IronOre('Normal')))
    sff.add_input(Miner(1, IronOre('Normal')))

    sff.add_input(Miner(1, Coal('Normal')))
    sff.add_input(Miner(1, Coal('Normal')))
    sff.add_input(Miner(1, Coal('Normal')))
    sff.add_input(Miner(1, Coal('Normal')))

    sff.add_machine(Foundry('Steel Ingot'))
    sff.add_machine(Foundry('Steel Ingot'))
    sff.add_machine(Foundry('Steel Ingot'))
    sff.add_machine(Foundry('Steel Ingot'))
    sff.add_machine(Foundry('Steel Ingot'))

    sff.add_machine(Constructor('Steel Beam'))
    sff.add_machine(Constructor('Steel Beam'))

    sff.add_machine(Constructor('Steel Pipe'))
    sff.add_machine(Constructor('Steel Pipe'))
    sff.add_machine(Constructor('Steel Pipe'))

    return sff


def upgrade_foundry(sff):
    # Upgrade the Foundry
    sff.upgrade_miners(2)

    sff.add_input(Miner(2, IronOre('Normal')))
    sff.add_input(Miner(2, Coal('Normal')))

    sff.add_machine(Foundry('Steel Ingot'))
    sff.add_machine(Foundry('Steel Ingot'))
    sff.add_machine(Foundry('Steel Ingot'))
    sff.add_machine(Foundry('Steel Ingot'))
    sff.add_machine(Foundry('Steel Ingot'))
    sff.add_machine(Foundry('Steel Ingot'))
    sff.add_machine(Foundry('Steel Ingot'))

    sff.add_machine(Constructor('Steel Pipe'))
    sff.add_machine(Constructor('Steel Pipe'))

    sff.add_machine(Constructor('Steel Beam'))
    sff.add_machine(Constructor('Steel Beam'))
    sff.add_machine(Constructor('Steel Beam'))
    sff.add_machine(Constructor('Steel Beam'))

    return sff


def upgrade_modular_frame_factory(mff):
    mff.upgrade_miners(2)

    mff.add_machine(Smelter('Iron Ingot'))
    mff.add_machine(Smelter('Iron Ingot'))

    mff.add_machine(Constructor('Iron Rod'))
    mff.add_machine(Constructor('Iron Rod'))
    mff.add_machine(Constructor('Iron Rod'))

    mff.add_machine(Assembler('Modular Frame'))
    mff.add_machine(Assembler('Modular Frame'))
    mff.add_machine(Assembler('Modular Frame'))
    mff.add_machine(Assembler('Modular Frame'))
    mff.add_machine(Assembler('Modular Frame'))

    return mff


def upgrade_reinforced_iron_plate_factory(ripf):
    # Upgrade your Miners to Mark 2
    ripf.upgrade_miners(2)

    ripf.add_input(Miner(2, IronOre('Normal')))

    ripf.add_machine(Smelter('Iron Ingot'))
    ripf.add_machine(Smelter('Iron Ingot'))
    ripf.add_machine(Smelter('Iron Ingot'))
    ripf.add_machine(Smelter('Iron Ingot'))
    ripf.add_machine(Smelter('Iron Ingot'))

    ripf.add_machine(Constructor('Iron Plate'))
    ripf.add_machine(Constructor('Iron Plate'))
    ripf.add_machine(Constructor('Iron Plate'))
    ripf.add_machine(Constructor('Iron Plate'))

    ripf.add_machine(Constructor('Iron Rod'))
    ripf.add_machine(Constructor('Iron Rod'))

    ripf.add_machine(Constructor('Screw'))
    ripf.add_machine(Constructor('Screw'))
    ripf.add_machine(Constructor('Screw'))
    ripf.add_machine(Constructor('Screw'))

    # Increase the Reinforced Iron Plate output
    ripf.add_machine(Assembler('Reinforced Iron Plate'))
    ripf.add_machine(Assembler('Reinforced Iron Plate'))
    ripf.add_machine(Assembler('Reinforced Iron Plate'))

    return ripf


def upgrade_reinforced_iron_plate_factory_again(ripf):
    ripf.add_machine(Smelter('Iron Ingot'))
    ripf.add_machine(Smelter('Iron Ingot'))
    ripf.add_machine(Smelter('Iron Ingot'))
    #
    ripf.add_machine(Constructor('Iron Plate'))
    ripf.add_machine(Constructor('Iron Plate'))

    ripf.add_machine(Constructor('Iron Rod'))
    ripf.add_machine(Constructor('Iron Rod'))

    ripf.add_machine(Constructor('Screw'))
    ripf.add_machine(Constructor('Screw'))

    # Increase the Reinforced Iron Plate output
    ripf.add_machine(Assembler('Reinforced Iron Plate'))

    return ripf


def upgrade_rotor_factory(rot_f):
    rot_f.upgrade_miners(2)

    rot_f.add_input(Miner(2, IronOre('Normal')))

    rot_f.add_machine(Smelter('Iron Ingot'))
    rot_f.add_machine(Smelter('Iron Ingot'))
    rot_f.add_machine(Smelter('Iron Ingot'))
    rot_f.add_machine(Smelter('Iron Ingot'))

    rot_f.add_machine(Constructor('Iron Rod'))
    rot_f.add_machine(Constructor('Iron Rod'))
    rot_f.add_machine(Constructor('Iron Rod'))
    rot_f.add_machine(Constructor('Iron Rod'))
    rot_f.add_machine(Constructor('Iron Rod'))
    rot_f.add_machine(Constructor('Iron Rod'))

    rot_f.add_machine(Constructor('Screw'))
    rot_f.add_machine(Constructor('Screw'))
    rot_f.add_machine(Constructor('Screw'))
    rot_f.add_machine(Constructor('Screw'))
    rot_f.add_machine(Constructor('Screw'))

    rot_f.add_machine(Assembler('Rotor'))
    rot_f.add_machine(Assembler('Rotor'))

    return rot_f


def upgrade_se2_factory(se2_factory):
    # Upgrade Space Elevator Factory 2 to produce more Automated Wiring
    se2_factory.upgrade_miners(2)

    se2_factory.add_input(Miner(2, CopperOre('Normal')))

    se2_factory.add_machine(Smelter('Copper Ingot'))
    se2_factory.add_machine(Smelter('Copper Ingot'))
    se2_factory.add_machine(Smelter('Copper Ingot'))

    se2_factory.add_machine(Constructor('Wire'))
    se2_factory.add_machine(Constructor('Wire'))
    se2_factory.add_machine(Constructor('Wire'))
    se2_factory.add_machine(Constructor('Wire'))
    se2_factory.add_machine(Constructor('Wire'))
    se2_factory.add_machine(Constructor('Wire'))

    se2_factory.add_machine(Constructor('Cable'))
    se2_factory.add_machine(Constructor('Cable'))
    se2_factory.add_machine(Constructor('Cable'))

    se2_factory.add_machine(Assembler('Automated Wiring'))
    se2_factory.add_machine(Assembler('Automated Wiring'))

    return se2_factory


def upgrade_stator_factory(sf):
    # Upgrade the Stator factory Used by Space Elevator Factory 2 to produce more stators
    sf.upgrade_miners(2)

    sf.add_input(Miner(2, CopperOre('Normal')))

    sf.add_machine(Smelter('Copper Ingot'))
    sf.add_machine(Smelter('Copper Ingot'))

    sf.add_machine(Constructor('Wire'))
    sf.add_machine(Constructor('Wire'))
    sf.add_machine(Constructor('Wire'))
    sf.add_machine(Constructor('Wire'))

    sf.add_machine(Assembler('Stator'))
    sf.add_machine(Assembler('Stator'))
    sf.add_machine(Assembler('Stator'))

    return sf


def build_space_elevator_1_factory():
    factory = Factory('Space Elevator 1 Factory')

    # Reinforced Iron Plate Factory
    ripf = reinforced_iron_plate_factory()
    factory.add_input(ripf)

    # Rotor Factory
    rf = rotor_factory()
    factory.add_input(rf)

    # Produce the Smart Plating at 2/minute
    factory.add_machine(Assembler('Smart Plating'))

    return factory, ripf, rf


def build_space_elevator_2_factory(se1_factory, ripf):
    factory = Factory('Space Elevator 2 Factory')

    # Use any excess production from Space Elevator 1 Factory
    factory.add_input(se1_factory)

    # Build a Modular Frame Factory (Import from RIPF)
    mff = Factory('Modular Frame Factory')

    mff.add_input(ripf)

    mff.add_input(Miner(2, IronOre('Normal')))

    mff.add_machine(Smelter('Iron Ingot'))

    mff.add_machine(Constructor('Iron Rod'))
    mff.add_machine(Constructor('Iron Rod'))

    mff.add_machine(Assembler('Modular Frame'))
    mff.add_machine(Assembler('Modular Frame'))

    factory.add_input(mff)

    # Build a Steel Foundry
    sff = steel_foundry_factory()

    factory.add_input(sff)

    # Stator and Cable Factory (Import from the Foundry)
    sf = Factory('Stator Factory')

    sf.add_input(sff)

    sf.add_input(Miner(2, CopperOre('Normal')))

    sf.add_machine(Smelter('Copper Ingot'))
    sf.add_machine(Smelter('Copper Ingot'))
    sf.add_machine(Smelter('Copper Ingot'))

    sf.add_machine(Constructor('Wire'))
    sf.add_machine(Constructor('Wire'))
    sf.add_machine(Constructor('Wire'))
    sf.add_machine(Constructor('Wire'))
    sf.add_machine(Constructor('Wire'))
    sf.add_machine(Constructor('Wire'))

    sf.add_machine(Constructor('Cable'))
    sf.add_machine(Constructor('Cable'))

    sf.add_machine(Assembler('Stator'))

    factory.add_input(sf)

    # Produce the Space Elevator resources
    factory.add_machine(Assembler('Versatile Framework'))
    factory.add_machine(Assembler('Automated Wiring'))

    return factory, mff, sff, sf


def build_space_elevator_3_factory(se1_factory, se2_factory, sff, sf, rot_f, ripf, mff):
    factory = Factory('Space Elevator 3 Factory')

    # Use any excess production from Space Elevator 1
    factory.add_input(se1_factory)

    factory.add_input(se2_factory)

    # Produce Motors (Import from Foundry and Stator Factory)
    mf = Factory('Motor Factory')

    mf.add_input(sff)
    mf.add_input(sf)
    mf.add_input(rot_f)

    mf.add_machine(Assembler('Motor'))

    factory.add_input(mf)

    # Build a refinery
    rf = foundry_factory()

    factory.add_input(rf)

    # Computer Factory (Import Plastic from Refinery)
    cf = Factory('Computer Factory')

    cf.add_input(rf)

    cf.add_input(Miner(2, CopperOre('Normal')))
    cf.add_input(Miner(2, CopperOre('Normal')))
    cf.add_input(Miner(2, IronOre('Normal')))

    cf.add_machine(Smelter('Copper Ingot'))
    cf.add_machine(Smelter('Copper Ingot'))
    cf.add_machine(Smelter('Copper Ingot'))
    cf.add_machine(Smelter('Copper Ingot'))
    cf.add_machine(Smelter('Copper Ingot'))
    cf.add_machine(Smelter('Iron Ingot'))
    cf.add_machine(Smelter('Iron Ingot'))

    cf.add_machine(Constructor('Copper Sheet'))
    cf.add_machine(Constructor('Copper Sheet'))
    cf.add_machine(Constructor('Copper Sheet'))
    cf.add_machine(Constructor('Copper Sheet'))
    cf.add_machine(Constructor('Copper Sheet'))
    cf.add_machine(Constructor('Copper Sheet'))

    cf.add_machine(Assembler('Circuit Board'))
    cf.add_machine(Assembler('Circuit Board'))
    cf.add_machine(Assembler('Circuit Board'))
    cf.add_machine(Assembler('Circuit Board'))

    cf.add_machine(Constructor('Wire'))
    cf.add_machine(Constructor('Wire'))

    cf.add_machine(Constructor('Cable'))

    cf.add_machine(Constructor('Iron Rod'))
    cf.add_machine(Constructor('Iron Rod'))
    cf.add_machine(Constructor('Iron Rod'))

    cf.add_machine(Constructor('Screw'))
    cf.add_machine(Constructor('Screw'))
    cf.add_machine(Constructor('Screw'))
    cf.add_machine(Constructor('Screw'))

    cf.add_machine(Manufacturer('Computer'))

    factory.add_input(cf)

    # Heavy Modular Frame factory (import from the Foundry)
    hmff = Factory('Heavy Modular Frame Factory')

    hmff.add_input(sff)
    hmff.add_input(ripf)
    hmff.add_input(mff)

    hmff.add_input(Miner(2, IronOre('Normal')))
    hmff.add_input(Miner(2, IronOre('Normal')))
    hmff.add_input(Miner(2, IronOre('Normal')))
    hmff.add_input(Miner(2, Limestone('Normal')))
    hmff.add_input(Miner(2, Limestone('Normal')))

    hmff.add_machine(Smelter('Iron Ingot'))
    hmff.add_machine(Smelter('Iron Ingot'))
    hmff.add_machine(Smelter('Iron Ingot'))
    hmff.add_machine(Smelter('Iron Ingot'))
    hmff.add_machine(Smelter('Iron Ingot'))
    hmff.add_machine(Smelter('Iron Ingot'))
    hmff.add_machine(Smelter('Iron Ingot'))
    hmff.add_machine(Smelter('Iron Ingot'))
    hmff.add_machine(Smelter('Iron Ingot'))
    hmff.add_machine(Smelter('Iron Ingot'))
    hmff.add_machine(Smelter('Iron Ingot'))

    hmff.add_machine(Constructor('Iron Plate'))
    hmff.add_machine(Constructor('Iron Plate'))
    hmff.add_machine(Constructor('Iron Plate'))
    hmff.add_machine(Constructor('Iron Plate'))
    hmff.add_machine(Constructor('Iron Plate'))

    hmff.add_machine(Constructor('Iron Rod'))
    hmff.add_machine(Constructor('Iron Rod'))
    hmff.add_machine(Constructor('Iron Rod'))
    hmff.add_machine(Constructor('Iron Rod'))
    hmff.add_machine(Constructor('Iron Rod'))
    hmff.add_machine(Constructor('Iron Rod'))
    hmff.add_machine(Constructor('Iron Rod'))
    hmff.add_machine(Constructor('Iron Rod'))
    hmff.add_machine(Constructor('Iron Rod'))
    hmff.add_machine(Constructor('Iron Rod'))
    hmff.add_machine(Constructor('Iron Rod'))

    hmff.add_machine(Constructor('Screw'))
    hmff.add_machine(Constructor('Screw'))
    hmff.add_machine(Constructor('Screw'))
    hmff.add_machine(Constructor('Screw'))
    hmff.add_machine(Constructor('Screw'))
    hmff.add_machine(Constructor('Screw'))
    hmff.add_machine(Constructor('Screw'))
    hmff.add_machine(Constructor('Screw'))
    hmff.add_machine(Constructor('Screw'))
    hmff.add_machine(Constructor('Screw'))

    hmff.add_machine(Constructor('Concrete'))
    hmff.add_machine(Constructor('Concrete'))
    hmff.add_machine(Constructor('Concrete'))
    hmff.add_machine(Constructor('Concrete'))

    hmff.add_machine(Assembler('Encased Industrial Beam'))
    hmff.add_machine(Assembler('Encased Industrial Beam'))

    hmff.add_machine(Manufacturer('Heavy Modular Frame'))

    factory.add_input(hmff)

    # Produce the Space Elevator resources
    factory.add_machine(Manufacturer('Modular Engine'))
    factory.add_machine(Manufacturer('Adaptive Control Unit'))

    return factory, mf, rf, cf, hmff


if __name__ == '__main__':
    session = Session()

    # Build Reinforced Iron Plate and Rotor factories and then Complete Space Elevator Tier 1
    se1_factory, ripf, rot_f = build_space_elevator_1_factory()
    session.add_factories(se1_factory, ripf, rot_f)
    session.visualize_factory_relationships('Tier 1.html')

    # Upgrade your Reinforced Iron Plate Factory
    ripf = upgrade_reinforced_iron_plate_factory(ripf)

    # Build Modular Frame, Steel Foundry, and Stator factories and Complete Space Elevator Tier 2
    se2_factory, mff, sff, sf = build_space_elevator_2_factory(se1_factory, ripf)
    session.add_factories(se2_factory, mff, sff, sf)
    session.visualize_factory_relationships('Tier 2.html')

    # Upgrade the Stator Factory
    sf = upgrade_stator_factory(sf)

    # Upgrade Steel Foundry
    sff = upgrade_foundry(sff)

    # Upgrade the Rotor Factory
    rot_f = upgrade_rotor_factory(rot_f)

    # Upgrade your Reinforced Iron Plate Factory again
    ripf = upgrade_reinforced_iron_plate_factory_again(ripf)

    # Upgrade you Modular Frame Factory
    mff = upgrade_modular_frame_factory(mff)

    # Upgrade the se2_factory
    se2_factory = upgrade_se2_factory(se2_factory)

    # Build Motor, Refinery, Computer, and Heavy Modular Frame Factories and Complete Space Elevator Tier 3
    se3_factory, mf, rf, cf, hmff = build_space_elevator_3_factory(se1_factory, se2_factory, sff, sf, rot_f, ripf, mff)
    session.add_factories(se3_factory, mf, rf, cf, hmff)
    session.visualize_factory_relationships('Tier 3.html')

