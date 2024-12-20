MAX, MIN = 1000, -1000

def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta): 

	if depth == 3: 
		return values[nodeIndex] 

	if maximizingPlayer: 
	
		best = MIN

		for i in range(0, 2): 
			
			val = minimax(depth + 1, nodeIndex * 2 + i, 
						False, values, alpha, beta) 
			best = max(best, val) 
			alpha = max(alpha, best) 

			if beta <= alpha: 
				break
		
		return best 
	
	else:
		best = MAX

		for i in range(0, 2): 
		
			val = minimax(depth + 1, nodeIndex * 2 + i, 
							True, values, alpha, beta) 
			best = min(best, val) 
			beta = min(beta, best) 

			if beta <= alpha: 
				break
		
		return best 
	

values = [3, 6, 2, 3, 7, 1, 2, 0]
without_magic = minimax(0, 0, True, values, MIN, MAX)


def minimax_checkAdvantage(depth, nodeIndex, 
			values, alpha, beta): 

        if depth == 3: 
            return values[nodeIndex] 
        
        best = MIN

        for i in range(0, 2): 

            val = minimax_checkAdvantage(depth + 1, nodeIndex * 2 + i, values, alpha, beta) 
            best = max(best, val) 
            alpha = max(alpha, best) 

            if beta <= alpha: 
                break


        return best 


values = [3, 6, 2, 3, 7, 1, 2, 0]
with_magic = minimax_checkAdvantage(0, 0, values, MIN, MAX)

cost = int(input())


if with_magic - cost < without_magic:
	print(f"The minimax value is {without_magic}. Pacman does not use dark magic")

else:
    if with_magic - cost > 7:
        print(f'The newminimax value is {with_magic}. Pacman goes right and uses dark magic')
    else:
        print(f'The newminimax value is {with_magic - cost}. Pacman goes right and uses dark magic')
	