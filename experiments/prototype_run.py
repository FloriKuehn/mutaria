"""
simulation.py

Entry point to run the simulation.
"""

from mutaria.simulation import Simulation


def main():
    sim = Simulation(width=10, height=10, num_agents=5)
    sim.run(steps=20)


if __name__ == "__main__":
    main()
