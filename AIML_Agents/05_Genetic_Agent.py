# 05_Genetic_Agent.py
# -------------------
# A Genetic Algorithm agent that evolves a random string to match a target string.

import random
import string

class GeneticAgent:
    def __init__(self, target, population_size=100, mutation_rate=0.01):
        self.target = target
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.genes = string.ascii_letters + " " # Allowed characters

    def create_genome(self):
        return "".join(random.choice(self.genes) for _ in range(len(self.target)))

    def fitness(self, genome):
        # Higher fitness is better. Count matching characters.
        return sum(1 for i, char in enumerate(genome) if char == self.target[i])

    def selection(self, population):
        # Tournament selection
        return max(random.sample(population, 3), key=self.fitness)

    def crossover(self, parent1, parent2):
        # Single point crossover
        point = random.randint(1, len(self.target) - 1)
        child = parent1[:point] + parent2[point:]
        return child

    def mutation(self, genome):
        genome_list = list(genome)
        for i in range(len(genome_list)):
            if random.random() < self.mutation_rate:
                genome_list[i] = random.choice(self.genes)
        return "".join(genome_list)

    def evolve(self):
        print(f"--- Genetic Agent ---")
        print(f"Target: '{self.target}'")
        
        # 1. Initialize Population
        population = [self.create_genome() for _ in range(self.population_size)]
        generation = 1
        
        while True:
            # Sort by fitness
            population = sorted(population, key=self.fitness, reverse=True)
            best_genome = population[0]
            best_fitness = self.fitness(best_genome)
            
            print(f"Gen {generation}: {best_genome} (Fitness: {best_fitness})")
            
            if best_fitness == len(self.target):
                print("\nTarget reached!")
                break
            
            # 2. Create new generation
            new_population = [best_genome] # Elitism: keep the best
            
            while len(new_population) < self.population_size:
                parent1 = self.selection(population)
                parent2 = self.selection(population)
                child = self.crossover(parent1, parent2)
                child = self.mutation(child)
                new_population.append(child)
            
            population = new_population
            generation += 1
            
            if generation > 1000: # Safety break
                print("Max generations reached.")
                break

if __name__ == "__main__":
    agent = GeneticAgent(target="Hello World")
    agent.evolve()
