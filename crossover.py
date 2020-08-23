 def single_point_crossover(parent1,parent2):
        crossover_point = random.randint(1,9)
        #print("crossover point", crossover_point)
        child_1 = np.hstack((parent1[0:crossover_point], parent2[crossover_point:]))
        child_2 = np.hstack((parent2[:crossover_point],parent1[crossover_point:]))
        return child_1,child_2
        
def two_point_crossover(parent1,parent2):
    size = min(len(parent1), len(parent2))
    crosspoint1 = random.randint(1, size)
    crosspoint2 = random.randint(1, size-1)
    print("crosspoint1",crosspoint1)
    print("crosspoint2",crosspoint2)
    print(parent1,parent2)
    if crosspoint2 >= crosspoint1:
        crosspoint2 += 1
    else:
        crosspoint1, crosspoint2 = crosspoint2, crosspoint1
    parent1[crosspoint1:crosspoint2], parent2[crosspoint1:crosspoint2] = parent2[crosspoint1:crosspoint2], parent1[crosspoint1:crosspoint2]
    return parent1,parent2
    
    
def uniform_crossover(parent1,parent2,probability):
    print(parent1,parent2)
    size = min(len(parent1), len(parent2))
    for i in range(size):
        if random.random() < probability:
            parent1[i], parent2[i] = parent2[i], parent1[i]
    return parent1,parent2

def whole_arithmetic_crossover(parent1, parent2 ,alfa):
        cross_child1 = []
        cross_child2 = []
        for index, gen in np.ndenumerate(parent1):
            y = parent2[index]
            new_gen = alfa * gen + (1 - alfa) * y
            cross_child1:int = np.append(cross_child1,(new_gen))
        for index,gen in np.ndenumerate(parent2):
            x = parent1[index]
            cross_child2.append(alfa*gen+(1-alfa)*x)
        return cross_child1,cross_child2
