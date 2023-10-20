from ..Resource import Resource


class Factory:
    def __init__(self):
        self.capacity = {}

    def add_machine(self):
        """
        Add a machine to the factory.
        :return:
        """
        pass

    # def remove_machine(self):
    #     """
    #     Remove a machine to the factory.
    #     :return:
    #     """
    #     pass

    def add_input(self):
        """
        Add a miner or factory as a source to this factory.
        :return:
        """
        pass

    # def remove_input(self):
    #     '''
    #     Remove a miner or factory as a source to this factory
    #     :return:
    #     '''
    #     pass

    def get_capacity(self):
        """
        Gets the current output capacity of the factory.
        :return:
        """
        return self.capacity

    def consume_capacity(self, resource_name: str, quantity: int):
        """
        Consume available capacity from available output.
        :return:
        """
        current_capacity = self.capacity[resource_name]

        current_capacity -= quantity
        if current_capacity < 0:
            raise ValueError(f"Capacity of {resource_name} exceeded!")
        else:
            self.capacity[resource_name] = current_capacity


    # def return_capacity(self):
    #     """
    #     De-consume available capacity from available output.
    #     :return:
    #     """
    #     pass


class Miner(Factory):
    """
    A variation of a factory that simply produces an output without an input.
    """
    def __init__(self, mark: int, resource: Resource.Resource):
        super().__init__()

        # Calculate the mining rate of the miner based on the miner mark and resource node purity.
        rate = 0
        if mark in [1, 2, 3]:
            # Marks increase the rate by factors of 2
            rate = 30 * 2**(mark - 1) * resource.get_purity_modifier()
        else:
            raise ValueError("Input 'mark' is not of value 1, 2, or 3.")

        self.capacity[resource.get_name()] = rate
