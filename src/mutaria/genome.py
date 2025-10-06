"""
genome.py

Defines the Gennome class for managing genetic information.
Each genome consists of one or more genes, each represented by a hexadecimal
string.
"""

import random

from mutaria.params import config


class Genome:
    """
    Class representing a genome composed of multiple genes.
    """
    def __init__(self, params=config):
        """
        Creates a genome with the specified number of genes and gene length.
        Each gene is represented as a hexadecimal string.
        """
        self.n_genes = params['n_genes']
        self.mutation_rate = params['mutation_rate']
        self.genes = [self._get_random_gene() for _ in range(self.n_genes)]

    def _get_random_gene(self) -> str:
        """
        Generates a random gene represented as an 8-char
        hexadecimal string.

        Returns:
            A hexadecimal string representing the gene.
        """
        return ''.join(random.choices('0123456789abcdef', k=8))

    def mutate(self) -> 'Genome':
        """
        Creates a mutated copy of the genome.

        Args:
            mutation_rate (float): Probability of each character in a gene
                being mutated.

        Returns:
            A new Genome instance with mutations applied.
        """
        new_genome = Genome()
        new_genome.genes = []

        for gene in self.genes:
            new_gene = ''.join(
                char if random.random() > self.mutation_rate
                else random.choice('0123456789abcdef')
                for char in gene
            )
            new_genome.genes.append(new_gene)

        return new_genome
