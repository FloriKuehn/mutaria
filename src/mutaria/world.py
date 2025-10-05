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

    def _find_empty_cell(self) -> tuple[int, int]:
        """
        Finds a random empty cell in the grid.

        Returns:
            A tuple (x, y) representing the coordinates of an empty cell,
            or None if no empty cell is available.
        """
        while True:
            x = np.random.randint(0, self.width - 1)
            y = np.random.randint(0, self.height - 1)
            if self.grid[y, x] is None:
                return (x, y)

    def add_agent(self, agent: Agent, position: tuple[int, int]):
        """
        Adds an agent to the world at the specified position.

        Args:
            agent: The agent to add.
            position (tuple[int, int]): The (x, y) position to place the agent.
        """
        x, y = position
        self.grid[y, x] = agent
        self.agents.append(agent)
        agent.position = position

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
        self.grid[old_y, old_x] = None
        self.grid[new_y, new_x] = agent
        agent.position = new_position

    def render_array(self) -> np.ndarray:
        """
        Renders the world as a 2D array for visualization.

        Returns:
            A 2D numpy array representing the world, where each cell contains
            1 if occupied by an agent, and 0 if empty.
        """
        render = np.zeros((self.height, self.width))
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y, x] is not None:
                    render[y, x] = 1
        return render
