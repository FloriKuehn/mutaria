"""
agent.py

Defines the Agent class, which represents an individual agent in the
simulation.
"""

import random


class Agent:
    """
    Represents an individual agent in the simulation.
    """

    def __init__(self, id: int, position: tuple[int, int] = (0, 0)):
        """
        Initializes the agent with a unique ID.

        Args:
            id (int): Unique identifier for the agent.
        """
        self.id = id
        self.position = position

    def act(self, world):
        """
        Defines the agent's behavior for a simulation step.
        For now, the agent moves randomly to an unoccupied adjacent cell.

        Args:
            world (World): The world in which the agent exists.
        """

        x, y = self.position
        possible_moves = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1),
        ]

        valid_moves = [
            (new_x, new_y) for new_x, new_y in possible_moves
            if 0 <= new_x < world.width
            and 0 <= new_y < world.height
            and world.grid[new_y, new_x] is None
        ]

        if valid_moves:
            new_position = random.choice(valid_moves)
            world.move_agent(self, new_position)
