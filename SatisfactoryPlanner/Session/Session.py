from pyvis.network import Network
from ..Factory.Factory import Factory, Miner, OilExtractor


class Session:
    def __init__(self) -> None:
        self.factories = []

    def add_factories(self, *factories: Factory) -> None:
        for factory in factories:
            if factory not in self.factories:
                self.factories.append(factory)

    @staticmethod
    def generate_output_summary(factory: Factory):
        factory_production = factory.get_production()

        production_name_dict = {key.get_name(): key for key in factory_production.keys()}
        keys = list(production_name_dict.keys())
        keys.sort()

        return '\n'.join([f"{key}: {factory_production[production_name_dict[key]]}/minute" for key in keys])

    def visualize_factory_relationships(self, graph_name='Factory.html') -> None:
        network = Network()
        network.toggle_physics(False)

        # Add the factories to the graph
        for factory in self.factories:
            network.add_node(id(factory), label=factory.get_name(), title=self.generate_output_summary(factory))

        # Add the miners
        for factory in self.factories:
            for source in factory.get_inputs():
                # if isinstance(source, Miner):
                network.add_node(id(source), label=source.get_name(), title=self.generate_output_summary(source))

        # Add the edges
        for factory in self.factories:
            for source in factory.get_inputs():
                network.add_edge(id(source), id(factory))

        network.show(graph_name, notebook=False)
