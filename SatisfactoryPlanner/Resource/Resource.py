class Resource:
    SINKABLE = True

    @classmethod
    def get_name(cls):
        return cls.__name__

    @classmethod
    def get_sinkable(cls):
        return cls.SINKABLE

    def get_class(self):
        return self.__class__


class AdaptiveControlUnit(Resource):
    pass


class AILimiter(Resource):
    pass


class AlcladAluminumSheet(Resource):
    pass


class AlienDNACapsule(Resource):
    pass


class AlienProtein(Resource):
    SINKABLE = False


class AlienRemains(Resource):
    SINKABLE = False


class AluminaSolution(Resource):
    SINKABLE = False


class AluminumCasing(Resource):
    pass


class AluminumIngot(Resource):
    pass


class AluminumScrap(Resource):
    pass


class AssemblyDirectorSystem(Resource):
    pass


class AutomatedWiring(Resource):
    pass


class Battery(Resource):
    pass


class Beacon(Resource):
    pass


class Biomass(Resource):
    pass


class BlackPowder(Resource):
    pass


class BluePowerSlug(Resource):
    pass


class Cable(Resource):
    pass


class CateriumIngot(Resource):
    pass


class CircuitBoard(Resource):
    pass


class ClusterNobelisk(Resource):
    pass


class ColorCartridge(Resource):
    pass


class CompactedCoal(Resource):
    pass


class Computer(Resource):
    pass


class Concrete(Resource):
    pass


class CoolingSystem(Resource):
    pass


class CopperIngot(Resource):
    pass


class CopperPowder(Resource):
    pass


class CopperSheet(Resource):
    pass


class CrystalOscillator(Resource):
    pass


class ElectromagneticControlRod(Resource):
    pass


class EmptyCanister(Resource):
    pass


class EmptyFluidTank(Resource):
    pass


class EncasedIndustrialBeam(Resource):
    pass


class EncasedPlutoniumCell(Resource):
    pass


class EncasedUraniumCell(Resource):
    pass


class ExplosiveRebar(Resource):
    pass


class Fabric(Resource):
    pass


class FlowerPetals(Resource):
    pass


class Fuel(Resource):
    SINKABLE = False


class FusedModularFrame(Resource):
    pass


class GasFilter(Resource):
    pass


class GasNobelisk(Resource):
    pass


class HatcherRemains(Resource):
    pass


class HeatSink(Resource):
    pass


class HeavyModularFrame(Resource):
    pass


class HeavyOilResidue(Resource):
    SINKABLE = False


class HighSpeedConnector(Resource):
    pass


class HogRemains(Resource):
    pass


class HomingRifleAmmo(Resource):
    pass


class IodineInfusedFilter(Resource):
    pass


class IronIngot(Resource):
    pass


class IronPlate(Resource):
    pass


class IronRebar(Resource):
    pass


class IronRod(Resource):
    pass


class Leaves(Resource):
    pass


class LiquidBiofuel(Resource):
    SINKABLE = False


class MagneticFieldGenerator(Resource):
    pass


class ModularEngine(Resource):
    pass


class ModularFrame(Resource):
    pass


class Motor(Resource):
    pass


class Mycelia(Resource):
    pass


class NitricAcid(Resource):
    SINKABLE = False


class Nobelisk(Resource):
    pass


class NonFissileUranium(Resource):
    SINKABLE = False


class NuclearPasta(Resource):
    pass


class NukeNobelisk(Resource):
    pass


class PackagedAluminaSolution(Resource):
    pass


class PackagedFuel(Resource):
    pass


class PackagedHeavyOilResidue(Resource):
    pass


class PackagedLiquidBiofuel(Resource):
    pass


class PackagedNitricAcid(Resource):
    pass


class PackagedNitrogenGas(Resource):
    pass


class PackagedOil(Resource):
    pass


class PackagedSulfuricAcid(Resource):
    pass


class PackagedTurboFuel(Resource):
    pass


class PackagedWater(Resource):
    pass


class PetroleumCoke(Resource):
    pass


class PlasmaSpitterRemains(Resource):
    pass


class Plastic(Resource):
    pass


class PlutoniumFuelRod(Resource):
    pass


class PlutoniumPellet(Resource):
    SINKABLE = False


class PlutoniumWaste(Resource):
    SINKABLE = False


class PolymerResin(Resource):
    pass


class PortableMiner(Resource):
    pass


class PowerShard(Resource):
    pass


class PressureConversionCube(Resource):
    pass


class PulseNobelisk(Resource):
    pass


class PurplePowerSlug(Resource):
    pass


class QuantumComputer(Resource):
    SINKABLE = False


class QuartzCrystal(Resource):
    pass


class Quickwire(Resource):
    pass


class RadioControlUnit(Resource):
    pass


class ReinforcedIronPlate(Resource):
    pass


class RifleAmmo(Resource):
    pass


class Rotor(Resource):
    pass


class Rubber(Resource):
    pass


class Screw(Resource):
    pass


class ShatterRebar(Resource):
    pass


class Silica(Resource):
    pass


class SmartPlating(Resource):
    pass


class SmokelessPowder(Resource):
    pass


class SolidBiofuel(Resource):
    pass


class Stator(Resource):
    pass


class SteelBeam(Resource):
    pass


class SteelIngot(Resource):
    pass


class SteelPipe(Resource):
    pass


class StingerRemains(Resource):
    pass


class StunRebar(Resource):
    pass


class SulfuricAcid(Resource):
    SINKABLE = False


class Supercomputer(Resource):
    pass


class ThermalPropulsionRocket(Resource):
    pass


class Turbofuel(Resource):
    SINKABLE = False


class TurboMotor(Resource):
    pass


class TurboRifleAmmo(Resource):
    pass


class UraniumFuelRod(Resource):
    pass


class UraniumWaste(Resource):
    SINKABLE = False


class VersatileFramework(Resource):
    pass


class Water(Resource):
    SINKABLE = False


class Wire(Resource):
    pass


class Wood(Resource):
    pass


class YellowPowerSlug(Resource):
    pass
