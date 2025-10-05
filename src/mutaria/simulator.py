"""
simulator.py

Defines the Simulator class, which orchestrates the simulation by managing
the world, the agents and all simulation steps.
"""

from mutaria.world import World
from mutaria.agent import Agent


class Simulator:
    """
    Orchestrates the simulation by managing the world and agents.
    """

    def __init__(self,
                 width: int,
                 height: int,
                 num_agents: int,
                 generations: int,
                 steps_per_generation: int
                 ):
        """
        Initializes the simulation with a world and a set of agents.

        Args:
            width (int): Width of the world.
            height (int): Height of the world.
            num_agents (int): Number of agents to create in the simulation.
                The world is repopulated with this many agents at the start of
                each generation.
            generations (int): Number of generations to simulate.
            steps_per_generation (int): Number of steps per generation.
        """
        self.world = World(width, height)
        self.num_agents = num_agents
        self.generations = generations
        self.steps_per_generation = steps_per_generation

    def populate_world(self):
        """
        Places agents randomly in onoccupied cells in the world.
        Used at the start of the simulation or when no parents are available.
        """
        self.agents = [Agent(id=i) for i in range(self.num_agents)]
        for agent in self.agents:
            self.world.add_agent(agent, self.world._find_empty_cell())

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
        parents = list(self.world.agents)
        children = []
        self.world.grid.fill(None)

        if not parents:
            self.populate_world()
            return

        for parent in parents:
            child = parent.reproduce(len(children))
            children.append(child)
            self.world.add_agent(child, self.world._find_empty_cell())

        self.world.agents = children
