MAX, MIN = 1000, -1000

def minimax(nodeIndex, depth, maximizingPlayer, values, alpha, beta): 
	if depth == 3: 
		return values[nodeIndex] 

	if maximizingPlayer: 
		best = MIN
		for i in range(0, 2): 
			
			val = minimax(nodeIndex * 2 + i,depth + 1, 
						False, values, alpha, beta) 
			best = max(best, val) 
			alpha = max(alpha, best) 

			if beta <= alpha: 
				break
		return best 
	
	else:
		best = MAX
		for i in range(0, 2): 
			val = minimax(nodeIndex * 2 + i,depth + 1, 
							True, values, alpha, beta) 
			best = min(best, val) 
			beta = min(beta, best) 
			if beta <= alpha: 
				break
		
		return best 
	

values = [3, 6, 2, 3, 7, 1, 2, 0]
without_magic = minimax(0, 0, True, values, MIN, MAX)


def minimax_magic(nodeIndex,depth, 
			values, alpha, beta): 
        if depth == 3: 
            return values[nodeIndex] 
        
        best = MIN

        for i in range(0, 2): 
            val = minimax_magic(nodeIndex * 2 + i,depth + 1, values, alpha, beta) 
            alpha = max(alpha, best) 
            best = max(best, val) 

            if beta <= alpha: 
                break
			
        return best 


values = [3, 6, 2, 3, 7, 1, 2, 0]
with_magic = minimax_magic(0, 0, values, MIN, MAX)

expense = int(input())


if with_magic - expense < without_magic:
	print(f"The minimax value is {without_magic}. Pacman does not use dark magic")

else:
    if with_magic - expense > 7:
        print(f'The new minimax value is {with_magic}. Pacman goes right and uses dark magic')
    else:
        print(f'The new minimax value is {with_magic - expense}. Pacman goes right and uses dark magic')
	