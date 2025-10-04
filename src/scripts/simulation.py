"""
simulation.py

Runs the first prototype of the simulation.
- World Creation
- Agent Initialization at Random Positions
- Random Movement
"""

import random

from mutaria.world import World
from mutaria.agent import Agent


def run_simulation(steps: int, world_size: tuple[int, int], num_agents: int):
    """
    Runs a simple simulation with random agent movements.

    Args:
        steps (int): Number of simulation steps to run.
        world_size (tuple[int, int]): Size of the world as (width, height).
        num_agents (int): Number of agents to initialize in the world.
    """
    width, height = world_size
    world = World(width, height)
    print(f"Created world of size {width}x{height}")

    # Initialize agents at random positions
    for agent_id in range(num_agents):
        while True:
            position = (random.randint(0, width - 1),
                        random.randint(0, height - 1))
            if world.grid[position[1], position[0]] is None:
                agent = Agent(agent_id, position)
                world.add_agent(agent, position)
                print(f"Added Agent {agent_id} at position {position}")
                break

    # Run the simulation for the specified number of steps
    for step in range(steps):
        for agent in list(world.agents):
            agent.move_randomly(world)
            print(f"Step {step}: Agent {agent.id} moved to {agent.position}")

    # Final state of the world
    print("Final positions of agents:")
    for agent in world.agents:
        print(f"Agent {agent.id} at position {agent.position}")


if __name__ == "__main__":
    run_simulation(steps=10, world_size=(5, 5), num_agents=3)
