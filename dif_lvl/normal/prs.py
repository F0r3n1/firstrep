from random import choice as ch

player_pts=0
pc_pts=0

pc_choices=["paper","rock","scissors"]



while player_pts<3 and pc_pts<3:
    
    player_choice=input("Ваш ход(paper, rock, scissors): ")
    
    pc_choice=ch(pc_choices)
    
    old_pc_choice=None
    while pc_choice==old_pc_choice:
        pc_choice=ch(pc_choices)
    
    if player_choice==pc_choice:
        print(f"Ничья, счет: пк - {pc_pts},игрок - {player_pts}")
    elif(player_choice == "rock" and pc_choice == "scissors") or \
        (player_choice == "scissors" and pc_choice == "paper") or \
        (player_choice == "paper" and pc_choice == "rock"):
        player_pts += 1 
        print(f"Вы выиграли раунд!, счет: пк - {pc_pts},игрок - {player_pts}")
    else:
        pc_pts += 1
        print(f"Вы проиграли раунд, счет: пк - {pc_pts},игрок - {player_pts}")

    old_pc_choice=pc_choice
        
if player_pts==3:
    print("Вы победили")
else:
    print("Вы проиграли")







    
