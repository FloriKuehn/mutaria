"""
world.py

Defines the World class, which represents a 2D grid environment for evolving
agents.
"""

import numpy as np

from mutaria.params import config


class World:
    """
    Represents a 2D grid world where agents can evolve and interact.
    The world is defined by its width and height, and contains a grid where
    each cell can be empty or occupied by an agent.
    Empty cells are represented by 0, and occupied cells by the agent's ID.
    """

    def __init__(self, params=config):
        """
        Initializes the world with given dimensions.
        """
        self.size = params['world_size']
        self.width, self.height = self.size
        self.grid = np.zeros((self.height, self.width))
        self.agents = []

    def reset(self):
        """
        Resets the world to its initial empty state.
        """
        self.grid = np.zeros((self.height, self.width))
        self.agents = []

    def is_empty_at(self, position: tuple[int, int]) -> bool:
        """
        Checks if a given position in the grid is empty.

        Args:
            position (tuple[int, int]): The (x, y) coordinates to check.

        Returns:
            Bool: True if the cell is empty, False otherwise.
        """
        x, y = position
        return self.grid[x, y] == 0

    def find_empty_cell(self) -> tuple[int, int]:
        """
        Finds a random empty cell in the grid.

        Returns:
            A tuple (x, y) representing the coordinates of an empty cell,
            or None if no empty cell is available.
        """
        if np.all(self.grid != 0):
            raise ValueError("No empty cells available in the world.")
        while True:
            x = np.random.randint(0, self.width - 1)
            y = np.random.randint(0, self.height - 1)
            if self.is_empty_at((x, y)):
                return (x, y)

    def add_agent(self, agent, position: tuple[int, int]):
        """
        Adds an agent to the world at the specified position.

        Args:
            agent: The agent to add.
            position (tuple[int, int]): The (x, y) position to place the agent.
        """
        x, y = position
        self.grid[y, x] = agent.id
        self.agents.append(agent)
        agent.position = position

    def move_agent(self, agent, new_position: tuple[int, int]):
        """
        Moves an agent to a new position in the world.

        Args:
            agent: The agent to move.
            new_position (tuple[int, int]): The (x, y) position to move the
            agent to.
        """
        old_x, old_y = agent.position
        new_x, new_y = new_position
        self.grid[old_y, old_x] = 0
        self.grid[new_y, new_x] = agent.id
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
