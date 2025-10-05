import random

from mutaria.genome import Genome


def test_genome_initialization():
    genome = Genome(n_genes=3, gene_length=4)
    assert len(genome.genes) == 3
    for gene in genome.genes:
        assert len(gene) == 4
        assert all(c in '0123456789abcdef' for c in gene)


def test_genome_mutation():
    random.seed(42)
    genome = Genome(n_genes=2, gene_length=4)
    original_genes = genome.genes.copy()
    mutated_genome = genome.mutate(mutation_rate=0.5)
    assert len(mutated_genome.genes) == 2
    for original, mutated in zip(original_genes, mutated_genome.genes):
        assert len(mutated) == 4
        assert any(o != m for o, m in zip(original, mutated))


def test_genome_mutation_extremes():
    random.seed(42)
    genome = Genome(n_genes=1, gene_length=4)
    no_mutation_genome = genome.mutate(mutation_rate=0.0)
    assert no_mutation_genome.genes == genome.genes

    full_mutation_genome = genome.mutate(mutation_rate=1.0)
    assert full_mutation_genome.genes != genome.genes
    assert all(c in '0123456789abcdef' for c in full_mutation_genome.genes[0])
