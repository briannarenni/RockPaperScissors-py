import new_game

while True:

    game = new_game.Game()

    game.print_result()

    play_again = input("Do you want to play again? (y/n): ")

    # if user enter any other character other than y, the game ends
    if play_again != "y":
        break
