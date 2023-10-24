from ..Resource import Resource


class Factory:
    def __init__(self):
        self.capacity = {}
        self.input_sources = []
        self.machines = []

    def add_machine(self, machine):
        """
        Add a machine to the factory.
        :return:
        """
        # Update factory input consumption for each input resource to the machine
        # NOTE: we are being greedy with our consumption and will exhaust an input source's full
        # capacity if it has any. We search the sources in the order that they were added and will
        # exhaust those sources before we exhaust later added sources.
        for resource, desired_capacity in machine.get_consumption_rate().items():
            # Check our available sources for the resource we need
            for input_source in self.input_sources:
                source_capacity = input_source.get_capacity()
                if resource in source_capacity:
                    # The source was available in the source, check how much of its capacity we
                    # need to consume
                    available_capacity = source_capacity[resource]

                    remaining_capacity = desired_capacity - available_capacity
                    if remaining_capacity >= 0:
                        # We consumed all the available capacity with no capacity left from
                        # the input source
                        input_source.consume_capacity(resource, available_capacity)
                        desired_capacity = remaining_capacity
                    else:
                        # There is available capacity left from the source and we didn't have to
                        # consume it all
                        input_source.consume_capacity(resource, desired_capacity)
                        desired_capacity = 0

                    if desired_capacity == 0:
                        break
            else:
                # Check the factory for the capacity we need since we didn't find it in the inputs
                # NOTE: This means factories prefer to consume imported resources than produce them
                # in-house where it can be avoided.
                if resource in self.capacity:
                    available_capacity = self.capacity[resource]

                    remaining_capacity = desired_capacity - available_capacity
                    if remaining_capacity >= 0:
                        # We consumed all the available capacity with no capacity left in the factory
                        self.consume_capacity(resource, available_capacity)
                        desired_capacity = remaining_capacity
                    else:
                        # There is available capacity left in the factory and we didn't have to
                        # consume it all
                        self.consume_capacity(resource, desired_capacity)
                        desired_capacity = 0

                    if desired_capacity != 0 and not machine.get_allow_undersupply():
                        raise ValueError(f"Not enough capacity found in sources for {resource.get_name()}! Need {desired_capacity}/minute more.")
                else:
                    if not machine.get_allow_undersupply():
                        raise ValueError(f"Not enough capacity found in sources for {resource.get_name()}! Need {desired_capacity}/minute more.")
        # Update factory output consumption
        for resource, output_capacity in machine.get_production_rates().items():
            current_capacity = self.capacity.get(resource, 0)
            current_capacity += output_capacity
            self.capacity[resource] = current_capacity

        # Add the machine to our tracking
        self.machines.append(machine)

    # def remove_machine(self):
    #     """
    #     Remove a machine to the factory.
    #     :return:
    #     """
    #     pass

    def add_input(self, factory):
        """
        Add a miner or factory as a source to this factory.
        :return:
        """
        self.input_sources.append(factory)

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
        # Check that all the liquids in the factory are being used.
        for resource, capacity in self.capacity.items():
            if not resource.get_sinkable() and capacity > 0:
                raise ValueError(f'Unsunk {resource.get_name()}! \n {capacity} remaining capacity to sink.')
        return self.capacity

    def consume_capacity(self, resource, quantity: int):
        """
        Consume available capacity from available output.
        :return:
        """
        current_capacity = self.capacity[resource]

        current_capacity -= quantity
        if current_capacity < 0:
            raise ValueError(f"Capacity of {resource.get_name()} exceeded!")
        else:
            self.capacity[resource] = current_capacity

    # def return_capacity(self):
    #     """
    #     De-consume available capacity from available output.
    #     :return:
    #     """
    #     pass

    def upgrade_miners(self, new_mark):
        for input_source in self.input_sources:
            if isinstance(input_source, Miner):
                input_source.upgrade_mark(new_mark)


class Miner(Factory):
    """
    A variation of a factory that simply produces an output without an input.
    """
    def __init__(self, mark: int, resource: Resource.Resource):
        super().__init__()

        rate = self.calculate_rate(mark, resource)

        self.resource = resource
        self.rate = rate
        self.capacity[resource.get_class()] = rate

    @staticmethod
    def calculate_rate(mark, resource):
        # Calculate the mining rate of the miner based on the miner mark and resource node purity.
        rate = 0
        if mark in [1, 2, 3]:
            # Marks increase the rate by factors of 2
            rate = 30 * 2 ** (mark - 1) * resource.get_purity_modifier()
        else:
            raise ValueError("Input 'mark' is not of value 1, 2, or 3.")

        return rate

    def get_capacity(self):
        # Don't worry about consuming all the capacity like the parent factory
        return self.capacity

    def upgrade_mark(self, new_mark):
        # TODO - Test
        new_rate = self.calculate_rate(new_mark, self.resource)

        # Upgrade only
        if new_rate > self.rate:
            new_rate_delta = new_rate - self.rate
            self.capacity[self.resource.get_class()] = self.capacity[self.resource.get_class()] + new_rate_delta
            self.rate = new_rate


class OilExtractor(Factory):
    """
    A variation of a factory that simply produces an output without an input.
    """
    def __init__(self, resource: Resource.Resource):
        super().__init__()

        rate = 60 * 2**(resource.get_purity_modifier()-1)

        self.capacity[resource.get_class()] = rate

    def get_capacity(self):
        # Don't worry about consuming all the capacity like the parent factory
        return self.capacity
