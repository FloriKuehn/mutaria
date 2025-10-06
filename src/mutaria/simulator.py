"""
simulator.py

Defines the Simulator class, which orchestrates the simulation by managing
the world, the agents and all simulation steps.
"""

from mutaria.world import World
from mutaria.agent import Agent
from mutaria.params import config


class Simulator:
    """
    Orchestrates the simulation by managing the world and agents.
    """

    def __init__(self, params=config):
        """
        Initializes the simulation with a world and a set of agents.
        """
        self.world = World()
        self.num_agents = params['population_size']
        self.generations = params['n_generations']
        self.steps_per_generation = params['steps_per_generation']

    def populate_world(self):
        """
        Places agents randomly in onoccupied cells in the world.
        Used at the start of the simulation or when no parents are available.
        """
        self.agents = [Agent(id=i) for i in range(self.num_agents)]
        for agent in self.agents:
            self.world.add_agent(agent, self.world.find_empty_cell())

    def simulate_step(self):
        """
        Advances the simulation by one time step, allowing each agent to move.
        """
        for agent in self.agents:
            agent.act(self.world)

    def reproduce_population(self):
        """
        Repopulates the world with new agents.
        Used at the end of each generation.
        """
        # Check for survivors
        if len(self.agents) == 0:
            self.populate_world()
            return

        # Create new agents from existing ones
        parents = self.agents.copy()
        children = []

        for parent in parents:
            child_id = parent.id
            child = parent.reproduce(child_id)
            children.append(child)

        # If not enough children, fill with random agents
        while len(children) < self.num_agents:
            new_id = len(children)
            child = Agent(id=new_id)
            children.append(child)

        # Clear the world and add children
        self.world.reset()
        self.agents = children

        for agent in self.agents:
            self.world.add_agent(agent, self.world.find_empty_cell())
