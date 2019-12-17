import random

class Player:
    def __init__(self, name, score=0):
        self.player_name = name
        self.player_score = score

    def get_player_name(self):
        return self.player_name

    def get_player_score(self):
        return self.player_score

    @classmethod
    def generate_players(cls, number):
        return [Player('Player {}'.format(i)) for i in range(1, number)]

class Game(Player):
    def __init__(self,name,score=0):
        Player.__init__(self, name, score=0)
        self.die_roll = random.randint(1,6)

    def get_die_roll(self):
        return self.die_roll

    def single_player_game(self):
        invalid_answer = True
        turn_total= 0
        display_message="You rolled a {}. Your roll total is {}. Your current score is {}."
        r_or_h_message="Would you like to roll(r) or hold(h)? "
        winner = False
        while not winner:
            die_roll = self.get_die_roll()
            if die_roll != 1:
                turn_total += die_roll
                while invalid_answer:
                    print(display_message.format(die_roll, turn_total, self.player_score))
                    response = input(r_or_h_message).lower()
                    if response == 'r':
                        turn_total += die_roll
                        invalid_answer = True
                    elif response == 'h':
                        self.player_score += turn_total
                        turn_total = 0
                        invalid_answer = False
                        break
                    else:
                        print("Please enter valid response.")
                        continue
            else:
                turn_total = 0
                continue
            if self.player_score >= 25:
                print("You win!")
                self.player_score = 0
                winner = True
                break

def main():
    number_of_players = input('Please enter the number of players: ')
    if number_of_players == '1':
        player = Player('Player 1')
        Game(player).single_player_game()
    elif number_of_players > '1':
        print('There are', number_of_players, 'players')
    else:
        print('Please 1 or higher.')

        print

if __name__ == '__main__':
    main()
#print(Game.multiplayer_game)
#print(Game('john').player_name)

#print(Game('Player one').single_player_game())

#print class object location in memory
#print(Player.generate_players(4))

#for player in  Player.generate_players():
#    print(player.player_name)