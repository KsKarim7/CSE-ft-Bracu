MAX, MIN = 2, -2


class MiniMax:
    def __init__(self, tree, max_depth = 5):
        self.tree = tree
        self.max_depth = max_depth
        self.rounds_played = 0
        self.round_results = []

    def alpha_beta_pruning(self, depth, nodeIndex, maximizingPlayer, 
                values, alpha, beta): 

        if depth == self.max_depth: 
            self.rounds_played += 1 
            self.round_results.append(-1 if values[nodeIndex] == -1 else 1)
            return values[nodeIndex] 

        if maximizingPlayer: 
        
            best = MIN

            for i in range(0, 2): 
                
                val = self.alpha_beta_pruning(depth + 1, nodeIndex * 2 + i, 
                            False, values, alpha, beta) 
                best = max(best, val) 
                alpha = max(alpha, best) 

                if beta <= alpha: 
                    break
            
            return best 
        
        else:
            best = MAX

            for i in range(0, 2): 
            
                val = self.alpha_beta_pruning(depth + 1, nodeIndex * 2 + i, 
                                True, values, alpha, beta) 
                best = min(best, val) 
                beta = min(beta, best) 

                if beta <= alpha: 
                    break
            
            return best 

    def determine_winner(self, starting_player):
        maximizing_player = True if starting_player == 0 else False
        result = self.alpha_beta_pruning(0, 0, maximizing_player, values, MIN, MAX)
        overall_winner = "Scorpion" if result == -1 else "Sub-Zero"
        return overall_winner, self.rounds_played, self.round_results


values = [-1, -1, 1, -1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1] 
MK = MiniMax(values)
winner, rounds_played, round_results =  MK.determine_winner(int(input()))
print("Game Winner", winner)
print(f'Total Rounds Played: {rounds_played}\n')

for i in range(rounds_played):
    print(f"Winner of Round {i + 1}", round_results[i])
	