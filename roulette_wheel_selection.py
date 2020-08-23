def roulettewheel_selection(p_population):

    #print(random_number)
    cumulative_sum=np.cumsum(p_population) # Return the cumulative sum of the elements along a given axis
    random_number=np.random.uniform(0,cumulative_sum[-1])
    place=np.argwhere(random_number<cumulative_sum) #Find the indices of array elements that are non-zero, grouped by element
    i=int(place[0][0])
    return i
