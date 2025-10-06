"""
run_prototype.py

This script runs the prototype simulation.
It is currently the only entry point for the simulation.
Later, this directory will contain multiple experiment scripts.
"""

from mutaria.simulator import Simulator
from mutaria.visualizer import Visualizer


def main():
    sim = Simulator()
    visualizer = Visualizer()

    sim.populate_world()
    for generation in range(sim.generations):
        for step in range(sim.steps_per_generation):
            sim.simulate_step()
            visualizer.render_step(sim.world, generation, step)

        sim.reproduce_population()
        print(f"Completed generation {generation}")
    visualizer.close()


if __name__ == "__main__":
    main()
