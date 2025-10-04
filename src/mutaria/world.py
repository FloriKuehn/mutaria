"""
world.py

Defines the World class, which represents a 2D grid environment for evolving
agents.
"""

import numpy as np

from mutaria.agent import Agent


class World:
    """
    Represents a 2D grid world where agents can evolve and interact.
    """

    def __init__(self, width: int, height: int):
        """
        Initializes the world with given dimensions.

        Args:
            width (int): Width of the world.
            height (int): Height of the world.
        """
        self.width = width
        self.height = height
        self.grid = np.full((height, width), None)
        self.agents = []

    def add_agent(self, agent: Agent, position: tuple[int, int]):
        """
        Adds an agent to the world at the specified position.

        Args:
            agent: The agent to add.
            position (tuple[int, int]): The (x, y) position to place the agent.
        """
        x, y = position
        if self.grid[y, x] is None:
            self.grid[y, x] = agent
            self.agents.append(agent)
            agent.position = position
        else:
            raise ValueError("Position is already occupied.")

    def move_agent(self, agent: Agent, new_position: tuple[int, int]):
        """
        Moves an agent to a new position in the world.

        Args:
            agent: The agent to move.
            new_position (tuple[int, int]): The (x, y) position to move the
            agent to.
        """
        old_x, old_y = agent.position
        new_x, new_y = new_position
        if (0 <= new_x < self.width and 0 <= new_y < self.height and
                self.grid[new_y, new_x] is None):
            self.grid[old_y, old_x] = None
            self.grid[new_y, new_x] = agent
            agent.position = new_position
        else:
            raise ValueError("Invalid move or position is occupied.")
