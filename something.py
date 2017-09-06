a = 3
if a == 1:
    print('a is 1!')
elif a == 2:
    print('a is 2!')
elif a == 3:
    print('a is 3!')
else:
    print("I don't know what a is")

#OTHER STUFF

cn = 17

prompt = "What is your guess? "

while True:
    players_guess = raw_input(prompt)
    if cn == int(players_guess):
        print("Correct")
        break
    elif computers_number > int(players_guess):
        print('too low')
    else:
        print('too high')
        
name = "Jeremiah"

while name == "Jeremiah":
    print('My name is ' + name)
    print "Setting name to Raymond"
    name = 'Raymond'
    
