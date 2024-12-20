def alpha_beta_pruning(node, depth, alpha, beta, find_powerful_plyer):
   
    if depth == 5 or type(node) is not list: 
        return node
   
    if find_powerful_plyer:     
        max_evaluation = float('-inf')
        for child in node:
            select_value = alpha_beta_pruning(child, depth + 1, alpha, beta, False)
            max_evaluation = max(max_evaluation, select_value)
            alpha = max(alpha, select_value)
           
            if (beta <= alpha):
                break

        return max_evaluation
   
    else:   
        min_evaluation = float('inf')
       
        for child in node:
            select_value = alpha_beta_pruning(child, depth + 1, alpha, beta, True)
            min_evaluation = min(min_evaluation, select_value)
            beta = min(beta, select_value)
           
            if (beta <= alpha):
                break
       
        return min_evaluation


def fight(first_move):
    #tree for each command
    tree_building_for_games = [
        [1, -1],  
        [1, -1],  
        [1, -1],
        [1, -1],  
        [1, -1]  
    ]
    res_lst = []
    calc_count = 0

    for i in range(len(tree_building_for_games)):
       
        result = alpha_beta_pruning(tree_building_for_games[i], 0, float('-inf'), float('inf'), True if first_move == 0 else False)
        calc_count += 1
        round_winner = "Sub-Zero" if result == 1 else "Scorpion"
        res_lst.append(f"Winner of Round {i+1}: {round_winner}")

        first_move = 1 if first_move == 0 else 0

 
    game_winner = "Scorpion" if res_lst.count("Scorpion") > res_lst.count("Sub-Zero") else "Sub-Zero"
   
    print(f"Game winner: {game_winner}")
    print(f"Total Rounds Played: {calc_count}")
   
    for res in res_lst:
        print(res)

first_move = int(input())
fight(first_move)  
