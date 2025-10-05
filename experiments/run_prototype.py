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
        width=8,
        height=8,
        num_agents=5,
        generations=10,
        steps_per_generation=100
    )
    visualizer = Visualizer(
        video_out_path="output/prototype_simulation.mp4",
        cell_size=100
        )

    sim.populate_world()
    for generation in range(sim.generations):
        for step in range(sim.steps_per_generation):
            sim.simulate_step()
            visualizer.render_step(sim.world, generation, step)
        sim.reproduce_population()
    visualizer.close()


if __name__ == "__main__":
    main()
