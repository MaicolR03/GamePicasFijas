# This function validate the type of variable wrote by the user
def validate_type(user):
    try:
        int(user) # Try to cast the input variable into an int, this confirms if the variable wrote by the user is a number 
    except:
        print("The number typed is not an number, input a new number again \n")
        return -1
    return 0

# This function validate if the length of the number wrote by the user is correct
def validate_length(user):
    if len(user) > 4:
        print("the typed number has more than 4 digits \n")
        return -1
    else:
        return 0
    
# This function request the player 1 for the initial own number
def ask_inicial_value_player1():
    numPlayer1 = input("Write the 4 digits for the Picas y fija -- Player 1:       ")
    validation_type1 = validate_type(numPlayer1)
    validation_length = validate_length(numPlayer1)
    if validation_type1 == -1 or validation_length == -1:
        ask_inicial_value_player1()
    else:
        return numPlayer1

# This function request the player 2 for the initial own number
def ask_inicial_value_player2():
    numPlayer2 = input("Write the 4 digits for the Picas y fijas -- Player 2:       ")
    validation_type2 = validate_type(numPlayer2)
    validation_length2 = validate_length(numPlayer2)
    if validation_type2 == -1 or validation_length2 == -1:
        ask_inicial_value_player2()
    else:
        return numPlayer2
    
# This function request the player 1 for the number that he thinks the other player have
def guessed_valuePlayer1(value_player2):
    guessed_numP1 = input("Type the value that you think the player 2 have:        ")
    validation_type1 = validate_type(guessed_numP1)
    validation_length1 = validate_length(guessed_numP1)
    countFijas = 0
    countPicas = 0
    if validation_type1 == -1 or validation_length1 == -1:
        guessed_valuePlayer1(value_player2)
    else:
        for i in range(4):
            if guessed_numP1[i] == value_player2[i]:
                countFijas+=1
            if i == 0:
                if guessed_numP1[i] == value_player2[i+1] or guessed_numP1[i] == value_player2[i+2] or guessed_numP1 == value_player2[i+3]:
                    countPicas+=1
            elif i == 1:
                if guessed_numP1[i] == value_player2[i-1] or guessed_numP1[i] == value_player2[i+1] or guessed_numP1[i] == value_player2[i+2]:
                    countPicas+=1
            elif i == 2:
                if guessed_numP1[i] == value_player2[i-2] or guessed_numP1[i] == value_player2[i-1] or guessed_numP1[i] == value_player2[i+1]:
                    countPicas+=1
            elif i == 3:
                if guessed_numP1[i] == value_player2[i-3] or guessed_numP1[i] == value_player2[i-2] or guessed_numP1[i] == value_player2[i-1]:
                    countPicas+=1
        if countFijas < 4:
            #print("En else", countFijas)
            print(f"You have {countPicas} picas")
            print(f"You have {countFijas} fijas")
            guessed_valuePlayer2(value_player1)
        else:
            print("Wins player 1")

# This function request the player 2 for the number that he thinks the other player have
def guessed_valuePlayer2(value_player1):
    guessed_numP2 = input("Type the value that you think the player 1 have:        ")
    validation_type2 = validate_type(guessed_numP2)
    validation_length2 = validate_length(guessed_numP2)
    countFijas = 0
    countPicas = 0
    if validation_type2 == -1 or validation_length2 == -1:
        guessed_valuePlayer2(value_player1)
    else:
        for i in range(4):
            if guessed_numP2[i] == value_player1[i]:
                countFijas+=1
            if i == 0:
                if guessed_numP2[i] == value_player1[i+1] or guessed_numP2[i] == value_player1[i+2] or guessed_numP2[i] == value_player1[i+3]:
                    countPicas+=1
            elif i == 1:
                if guessed_numP2[i] == value_player1[i-1] or guessed_numP2[i] == value_player1[i+1] or guessed_numP2[i] == value_player1[i+2]:
                    countPicas+=1
            elif i == 2:
                if guessed_numP2[i] == value_player1[i-2] or guessed_numP2[i] == value_player1[i-1] or guessed_numP2[i] == value_player1[i+1]:
                    countPicas+=1
            elif i == 3:
                if guessed_numP2[i] == value_player1[i-3] or guessed_numP2[i] == value_player1[i-2] or guessed_numP2[i] == value_player1[i-1]:
                    countPicas+=1
        if countFijas < 4:
            print(f"You have {countPicas} picas")
            print(f"You have {countFijas} fijas")
            guessed_valuePlayer1(value_player2)
        else:
            print("Wins player 2")

value_player1 = ask_inicial_value_player1()
value_player2 = ask_inicial_value_player2()
guessed_valuePlayer1(value_player2)

