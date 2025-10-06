"""
params.py

Defines global parameters for the Mutaria simulation.
Later, I will add functionality to load these from a config file.
"""

config = {
    # World parameters
    'world_size': (64, 64),

    # Simulator parameters
    'n_generations': 10,
    'steps_per_generation': 300,
    'population_size': 100,

    # Genome parameters
    'n_genes': 5,
    'mutation_rate': 0.01,

    # NeuralNetwork parameters
    'max_hidden_neurons': 2,

    # Visualizer parameters
    'video_out_path': 'output/prototype_simulation.mp4',
    'video_scale': 16,
    'fps': 30,
}
