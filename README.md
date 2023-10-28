# Overview
The Satisfactory Planner is a tool for macro-level planning of factories in Satisfactory.

A factory in this tool is a collection of machines (e.g. constructors, assemblers, etc.)
with input requirements that need to be met. Those input requirements can be met by other
machines producing within the factory (e.g. a constructor producing screws in a factory 
consumes iron rods produced by another constructor in the same factory) or by connecting 
the outputs of other factories to factories with unmet input requirements (e.g. a 
constructor producing screws in a factory consumes the available iron rods produced by a 
different factory). 

The result of meeting all the input needs of the machines of a factory is collection of 
outputs of the factory that can be consumed by other factories or meet a desired 
production rate of resources to solve other needs (e.g. excess resources for building or 
to complete the space elevator requirements).

By providing a macro-level view to planning, pioneers can logically group and place 
production at strategic locations on the map and plan the movement of key resources 
without being overwhelmed by the micro-details of organizing and connecting individual 
machines. 

Once the macro-level factory planning and connections have been performed, pioneers can 
use micro-level planning tools, such as https://satisfactory-calculator.com, to organize 
and plan the internal functionality of each individual factory in the macro-level plan.

# Getting Started
The `demo/` directory of this repository provides a demonstration of the Satisfactory 
Planner tool. The code under the `__main__` section of `Demo.py` shows an example of the 
steps that can be completed to complete Tiers 1 through 3 of the Space Elevator. 


## Demonstration Step 1
At step 1, a factory to complete Space Elevator Tier 1 (50 Smart Plating) is planned for
(see the factories and machines planned for in the `build_space_elevator_1_factory` 
function). 

To complete this step, the pioneer will be building Rotor and Reinforced Iron Plate
factories that provide the inputs to a Smart Plating factory.

`Tier 1.html` is an interactive network graph, also built using the Satisfactory Planner 
that show the factories built in step 1 plus their inputs and outputs.

## Demonstration Step 2
To prepare for building the factory that will meet needs for Space Elevator Tier 2 (i.e. 
adding production for Versatile Framework and Automated Wiring), the pioneer will plan for
and implement an upgrade to the Reinforced Iron Plate factory they built in Step 1 to 
increase their overall production of Reinforced Iron Plates while still meeting the needs
of the other factories built in step 1 (i.e. the Smart Plating factory).

They will then build Modular Frame and Stator factories as well as start the Steel Foundry 
that will be used several more times on the way to completing Tiers 3 and 4. 

At this point the pioneer has already planned for the Versatile Framework and Automated 
Wiring factory that will consume the outputs of the Space Elevator 1, Stator, and Modular
Frame factories as well as the Steel Foundry and can start building their final factory 
for Tier 2.

`Tier 2.html` shows the network graph of the factories built in Tiers 1 and 2 and how they
are planned to connect to meet the needs of Space Elevator Tier 2.

## Demonstration Step 3 
The remainder of the demonstration shows the planned upgrades and factories that will have
be performed and built on the path to completing Space Elevator Tier 3. `Tier 3.html` 
shows the network graph for this tier of the Space Elevator.

## Demonstration Key Concepts
The demonstration script shows how not only how specific Space Elevator tiers can be 
planned for using the Satisfactory Planner tool. It also shows how the pioneer can define
factories they frequently build in their play-throughs (e.g. steel foundries and 
refineries) and how they can plan and organize their play-through from start to finish, 
including planned upgrades of factories built in earlier steps of their play-through.