"""
run_prototype.py

This script runs the prototype simulation.
It is currently the only entry point for the simulation.
Later, this directory will contain multiple experiment scripts.
"""

from mutaria.simulator import Simulator
from mutaria.visualizer import Visualizer


def main():
    sim = Simulator(
        width=512,
        height=512,
        num_agents=1000,
        generations=10,
        steps_per_generation=100
    )
    visualizer = Visualizer(
        video_out_path="output/prototype_simulation.mp4",
        cell_size=1
        )

    sim.populate_world()
    for generation in range(sim.generations):
        for step in range(sim.steps_per_generation):
            sim.simulate_step()
            visualizer.render_step(sim.world, generation, step)

        # Before repopulating, clear the right half of the world
        for y in range(sim.world.height):
            for x in range(sim.world.width // 2, sim.world.width):
                agent = sim.world.grid[y, x]
                if agent is not None:
                    sim.world.grid[y, x] = None
                    sim.agents.remove(agent)
        sim.reproduce_population()
        print(f"Completed generation {generation}")
    visualizer.close()


if __name__ == "__main__":
    main()
