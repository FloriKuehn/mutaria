"""
genome.py

Defines the Gennome class for managing genetic information.
Each genome consists of one or more genes, each represented by a hexadecimal
string.
"""

import random


class Genome:
    """
    Class representing a genome composed of multiple genes.
    """
    def __init__(self, n_genes=1, gene_length=8):
        """
        Creates a genome with the specified number of genes and gene length.
        Each gene is represented as a hexadecimal string.

        Args:
            n_genes (int): Number of genes in the genome.
            gene_length (int): Length of each gene in hexadecimal characters.
        """
        self.n_genes = n_genes
        self.gene_length = gene_length
        self.genes = [self._random_gene() for _ in range(n_genes)]

    def _random_gene(self) -> str:
        """
        Generates a random gene represented as a hexadecimal string.

        Returns:
            A hexadecimal string representing the gene.
        """
        return ''.join(random.choices('0123456789abcdef', k=self.gene_length))

    def mutate(self, mutation_rate=0.01) -> 'Genome':
        """
        Creates a mutated copy of the genome.

        Args:
            mutation_rate (float): Probability of each character in a gene
                being mutated.

        Returns:
            A new Genome instance with mutations applied.
        """
        new_genome = Genome(self.n_genes, self.gene_length)
        new_genome.genes = []

        for gene in self.genes:
            new_gene = ''.join(
                char if random.random() > mutation_rate
                else random.choice('0123456789abcdef')
                for char in gene
            )
            new_genome.genes.append(new_gene)

        return new_genome
