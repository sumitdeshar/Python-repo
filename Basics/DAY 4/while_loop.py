#i = 1
#while i<=20:
   # print(i)
  #  i += 1
#print("loop end")

secret_word = "nepal"
guess = ""
guess_limit = 5 #no of guesses
guess_count = 0
out_of_guesses = False
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("guess a word :")
        guess_count += 1

    else:
        out_of_guesses = True
if out_of_guesses == False:
    print("you won")
else:
    print("guess limit is reached")
    print("you lose")

