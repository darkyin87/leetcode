
def climb_stairs(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0:
        return 0
    
    steps = [0 for x in range(0, n+1)]
    
    steps[0] = 1
    steps[1] = 2
    
    for i in range(2, n):
        steps[i] = steps[i-1] + steps[i-2]

    return steps[n-1]
        
climb_stairs(1)
climb_stairs(1)
climb_stairs(1)
