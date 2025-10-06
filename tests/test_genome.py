import random

from mutaria.genome import Genome
from mutaria.params import config


def test_genome_initialization():
    genome = Genome()
    assert len(genome.genes) == config['n_genes']
    for gene in genome.genes:
        assert len(gene) == 8
        assert all(c in '0123456789abcdef' for c in gene)


def test_genome_mutation():
    random.seed(42)
    genome = Genome()
    original_genes = genome.genes.copy()
    mutated_genome = genome.mutate(mutation_rate=0.5)
    assert len(mutated_genome.genes) == len(original_genes)
    for original, mutated in zip(original_genes, mutated_genome.genes):
        assert len(mutated) == len(original)
        assert any(o != m for o, m in zip(original, mutated))


def test_genome_mutation_extremes():
    random.seed(42)
    genome = Genome()
    no_mutation_genome = genome.mutate(mutation_rate=0.0)
    assert no_mutation_genome.genes == genome.genes

    full_mutation_genome = genome.mutate(mutation_rate=1.0)
    assert full_mutation_genome.genes != genome.genes
    assert all(c in '0123456789abcdef' for c in full_mutation_genome.genes[0])
