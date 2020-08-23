    def simple_mutation(child1,child2):
        chromosome_len = len(child1)
        pos1 = random.randint(0, chromosome_len-1)
        pos2 = random.randint(0, chromosome_len-1)
        print(">> swaping point" , pos1, "and, ",pos2 )
        child1[pos1], child1[pos2] = child1[pos2], child1[pos1]
        child2[pos1], child2[pos2] = child2[pos2], child2[pos1]
        return child1, child2
        
   def binary_mutation(child1, child2):
        posi = random.randint(0, len(child1)-1)
        if child1[posi] == 1:
            child1[posi] = 0
        elif child1[posi] == 0:
            child1[posi] = 1
        if child2[posi] == 1:
            child2[posi] = 0
        elif child2[posi] == 0:
            child2[posi] = 1
        return child1, child2
   
 def mutation(parent1_cost,parent2_cost):
    size = min(len(parent1_cost), len(parent2_cost))
    sigma=gamma*(size/1.5)
    mutation_point1 = random.randint(1, size-1)
    mutation_point2 = random.randint(1, size-1)
    while mutation_point1==mutation_point2:
        mutation_point2 = random.randint(1, size-1)  
    offspring1=parent1_cost.copy()
    offspring2=parent2_cost.copy()
    offspring1=offspring1.reshape((1,number_of_variable))
    offspring2=offspring2.reshape((1,number_of_variable))
    parent1_cost=parent1_cost.reshape((1,number_of_variable))
    parent2_cost=parent2_cost.reshape((1,number_of_variable))
    for i in range(number_of_mutated_chromosome):
        offspring1[0,mutation_point1]=parent1_cost[0,mutation_point2]+sigma*np.random.randn()
        offspring2[0,mutation_point1]=parent2_cost[0,mutation_point2]+sigma*np.random.randn()
    return np.around(offspring1, decimals=-1),np.around(offspring2, decimals=-1)
