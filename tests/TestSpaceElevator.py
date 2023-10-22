import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from SatisfactoryPlanner.Factory.Factory import Miner, Factory
from SatisfactoryPlanner.Resource.Resource import *
from SatisfactoryPlanner.Machines.Machines import Smelter, Constructor, Assembler, Foundry, Manufacturer


class TestSpaceElevator(unittest.TestCase):
    def build_space_elevator_1_factory(self):
        factory = Factory()

        # Reinforced Iron Plate Factory
        ripf = Factory()

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

        self.assertEqual(ripf.get_capacity(), {
            IronIngot: 0,
            IronPlate: 10,
            IronRod: 10,
            Screw: 20,
            ReinforcedIronPlate: 5
        })
        factory.add_input(ripf)

        # Rotor Factory
        rf = Factory()

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

        self.assertEqual(rf.get_capacity(), {
            IronIngot: 00,
            IronRod: 10,
            Screw: 20,
            Rotor: 4
        })
        factory.add_input(rf)

        # Produce the Smart Plating at 2/minute
        factory.add_machine(Assembler('Smart Plating'))

        self.assertEqual(factory.get_capacity(), {
            SmartPlating: 2
        })

        return factory

    def build_space_elevator_2_factory(self, se1_factory):
        factory = Factory()

        # Use any excess production from Space Elevator 1 Factory
        factory.add_input(se1_factory)

        # Modular Frame Factory
        mff = Factory()

        mff.add_input(Miner(1, IronOre('Normal')))
        mff.add_input(Miner(1, IronOre('Normal')))
        mff.add_input(Miner(1, IronOre('Normal')))

        mff.add_machine(Smelter('Iron Ingot'))
        mff.add_machine(Smelter('Iron Ingot'))
        mff.add_machine(Smelter('Iron Ingot'))
        mff.add_machine(Smelter('Iron Ingot'))
        mff.add_machine(Smelter('Iron Ingot'))
        mff.add_machine(Smelter('Iron Ingot'))

        mff.add_machine(Constructor('Iron Plate'))
        mff.add_machine(Constructor('Iron Plate'))
        mff.add_machine(Constructor('Iron Plate'))
        mff.add_machine(Constructor('Iron Plate'))

        mff.add_machine(Constructor('Iron Rod'))
        mff.add_machine(Constructor('Iron Rod'))
        mff.add_machine(Constructor('Iron Rod'))
        mff.add_machine(Constructor('Iron Rod'))

        mff.add_machine(Constructor('Screw'))
        mff.add_machine(Constructor('Screw'))
        mff.add_machine(Constructor('Screw'))

        mff.add_machine(Assembler('Reinforced Iron Plate'))
        mff.add_machine(Assembler('Reinforced Iron Plate'))

        mff.add_machine(Assembler('Modular Frame'))
        mff.add_machine(Assembler('Modular Frame'))

        self.assertEqual(mff.get_capacity(), {
            IronIngot: 0,
            IronRod: 6,
            IronPlate: 20,
            Screw: 0,
            ReinforcedIronPlate: 4,
            ModularFrame: 4
        })
        factory.add_input(mff)

        # Steel Foundry Factory
        sff = Factory()

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

        self.assertEqual(sff.get_capacity(), {
            SteelIngot: 15,
            SteelBeam:  30,
            SteelPipe: 60
        })
        factory.add_input(sff)

        # Stator and Cable Factory (Import from the Foundry)
        sf = Factory()

        sf.add_input(sff)

        sf.add_input(Miner(1, CopperOre('Normal')))
        sf.add_input(Miner(1, CopperOre('Normal')))

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

        self.assertEqual(sf.get_capacity(), {
            CopperIngot: 0,
            Wire: 20,
            Stator: 5,
            Cable: 60
        })
        factory.add_input(sf)

        # Produce the Space Elevator resources
        factory.add_machine(Assembler('Versatile Framework'))
        factory.add_machine(Assembler('Automated Wiring'))

        self.assertEqual(factory.get_capacity(), {
            VersatileFramework: 5,
            AutomatedWiring: 2.5
        })

        return factory, sff

    def build_space_elevator_3_factory(self, se1_factory, se2_factory, foundry):
        factory = Factory()

        # Use any excess production from Space Elevator 1 and 2 Factories
        factory.add_input(se1_factory)
        factory.add_input(se2_factory)

        # Produce Motors (Import from Foundry)
        mf = Factory()

        mf.add_input(foundry)

        mf.add_input(Miner(1, IronOre('Normal')))
        mf.add_input(Miner(1, IronOre('Normal')))
        mf.add_input(Miner(1, IronOre('Normal')))

        mf.add_input(Miner(1, CopperOre('Normal')))

        mf.add_machine(Smelter('Iron Ingot'))
        mf.add_machine(Smelter('Iron Ingot'))
        mf.add_machine(Smelter('Iron Ingot'))
        mf.add_machine(Smelter('Iron Ingot'))
        mf.add_machine(Smelter('Iron Ingot'))

        mf.add_machine(Smelter('Copper Ingot'))
        mf.add_machine(Smelter('Copper Ingot'))

        mf.add_machine(Constructor('Iron Rod'))
        mf.add_machine(Constructor('Iron Rod'))
        mf.add_machine(Constructor('Iron Rod'))
        mf.add_machine(Constructor('Iron Rod'))
        mf.add_machine(Constructor('Iron Rod'))
        mf.add_machine(Constructor('Iron Rod'))
        mf.add_machine(Constructor('Iron Rod'))
        mf.add_machine(Constructor('Iron Rod'))
        mf.add_machine(Constructor('Iron Rod'))
        mf.add_machine(Constructor('Iron Rod'))

        mf.add_machine(Constructor('Screw'))
        mf.add_machine(Constructor('Screw'))
        mf.add_machine(Constructor('Screw'))
        mf.add_machine(Constructor('Screw'))
        mf.add_machine(Constructor('Screw'))
        mf.add_machine(Constructor('Screw'))
        mf.add_machine(Constructor('Screw'))
        mf.add_machine(Constructor('Screw'))

        mf.add_machine(Assembler('Rotor'))
        mf.add_machine(Assembler('Rotor'))
        mf.add_machine(Assembler('Rotor'))

        mf.add_machine(Constructor('Wire'))
        mf.add_machine(Constructor('Wire'))
        mf.add_machine(Constructor('Wire'))

        mf.add_machine(Assembler('Stator'))
        mf.add_machine(Assembler('Stator'))

        mf.add_machine(Assembler('Motor'))

        self.assertEqual(mf.get_capacity(), {
            Screw: 20,
            Stator: 0,
            IronIngot: 0,
            Motor: 5,
            IronRod: 10,
            Rotor: 2,
            Wire: 10,
            CopperIngot: 15
        })
        factory.add_input(mf)


        # Produce the Space Elevator resources
        factory.add_machine(Manufacturer('Modular Engine'))
        factory.add_machine(Manufacturer('Adaptive Control Unit'))

    def test_tier_1(self):
        self.build_space_elevator_1_factory()

    def test_tier_2(self):
        se1_factory = self.build_space_elevator_1_factory()
        self.build_space_elevator_2_factory(se1_factory)

    def test_tier_3(self):
        se1_factory = self.build_space_elevator_1_factory()
        se2_factory, foundry = self.build_space_elevator_2_factory(se1_factory)
        self.build_space_elevator_3_factory(se1_factory, se2_factory, foundry)

if __name__ == '__main__':
    unittest.main()
