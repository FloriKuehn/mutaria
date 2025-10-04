"""
simulation.py

Defines the Simulation class, which orchestrates the simulation by managing
the world, the agents and all simulation steps.
"""

from mutaria.world import World
from mutaria.agent import Agent


class Simulation:
    """
    Orchestrates the simulation by managing the world and agents.
    """

    def __init__(self, width: int, height: int, num_agents: int):
        """
        Initializes the simulation with a world and a set of agents.

        Args:
            width (int): Width of the world.
            height (int): Height of the world.
            num_agents (int): Number of agents to create in the simulation.
        """
        self.world = World(width, height)
        self.agents = [Agent(id=i) for i in range(num_agents)]

    def _populate_world(self):
        """
        Places agents randomly in the world.
        """
        import random

        for agent in self.agents:
            while True:
                position = (random.randint(0, self.world.width - 1),
                            random.randint(0, self.world.height - 1))
                if self.world.grid[position[1], position[0]] is None:
                    self.world.add_agent(agent, position)
                    break

    def _simulate_step(self):
        """
        Advances the simulation by one step, allowing each agent to move.
        """
        for agent in self.agents:
            agent.act(self.world)

    def run(self, steps: int):
        """
        Runs the simulation for a specified number of steps.

        Args:
            steps (int): Number of steps to run the simulation.
        """
        self._populate_world()

        for step in range(steps):
            self._simulate_step()
            print(f"After step {step + 1}:")
            for agent in self.agents:
                print(f"Agent {agent.id} at position {agent.position}")
