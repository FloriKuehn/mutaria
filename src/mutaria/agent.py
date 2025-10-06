"""
agent.py

Defines the Agent class, which represents an individual agent in the
simulation.
"""

import random

from mutaria.genome import Genome


class Agent:
    """
    Represents an individual agent in the simulation.
    """

    def __init__(
            self,
            id: int,
            genome: Genome = Genome(),
            position: tuple[int, int] = (0, 0)
            ):
        """
        Initializes the agent with a unique ID and a genome.

        Args:
            id (int): Unique identifier for the agent.
            genome (Genome): The genome of the agent.
            position (tuple[int, int]): The (x, y) position of the agent in
                the world.
        """
        self.id = id
        self.position = position
        self.genome = genome

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
            and world.is_empty_at((new_x, new_y))
        ]

        if valid_moves:
            new_position = random.choice(valid_moves)
            world.move_agent(self, new_position)

    def reproduce(self, child_id: int):
        """
        Creates a new agent as a child of this agent.
        Needs to be passed a unique ID for the child agent.
        """
        child_genome = self.genome.mutate()
        return Agent(child_id, genome=child_genome)
