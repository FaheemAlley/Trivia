

print("Welcome to my Trivia!\n I will ask you some questions and if you get them correct you get a point!\n") 

print("But beware as if you answer a question wrong you will loose a point \n")

print("Lets get started!\n")

points = 0

answer = input("Would you like to play? Y or N ")
if answer != "Y":
	print("Bye! See you Soon!! \n") 
else:
	print("First Question: \n")
	question1 = input("What is the captial of Canada? Is it A) Vancouver B) Toronto C) Ottawa D) London ")
	if question1 == "C":
		print("Correct!")
		points += 1
	else:
			print("Incorrect! \n")
			points -= 1
	
	print("Second Question: \n")
	question2 = input("Who designed Microsoft? Is it A) Donald Trump B) Bill Gates C) Steve Jobs D) Lee Byung-Chull ")
	if question2 == "B":
		print("Correct!")
		points += 1
	else:
			print("Incorrect \n")
			points -= 1

	print("Third Question \n")
	question3 = input("Who was the 1st president of the United States Of America A) Barack Obama B) John F. Kennedy C) Richard Nixon D) George Washington ")
	if question3 == "D":
		print("Correct!")
		points += 1
	else:
			print("Incorrect! \n")
			points -= 1

	print("Fourth Question \n")
	question4 = input("Who was the first man in space? A) Yuri Gagarin B) James T. Kirk C) Buzz Aldron D) Neil Armstrong ")
	if question4 == "A":
		print("Well Done! Thats Correct!")
		points += 1
	else:
		print("Uh oh! Incorrect! \n")
		points -= 1

	print("Fifth Question! \n")
	question5 = input("What is the biggest desert on Earth? A) Sahara B) Antartica C) Arabian D) Gobi ")
	if question5 == "B":
		print("Correct!")
		points += 1
	else:
		print("Incorrect \n")
		points -= 1

	print("Sixth Question \n")
	question6 = input("Where was the Titanic heading to before it sank? A) New York B) California C) Canada D) Cape town ")
	if question6 == "A":
		print("Correct!")
		points += 1
	else:
		print("Incorrect \n")
		points -= 1

	print("Seventh Question \n")
	question7 = input("Who was the English king who had 6 wives? A) William The Conqueror B) Henry VII C) Henry I D) Henry VIII ")
	if question7 == "D":
		print("Correct!")
		points += 1
	else:
		print("Incorrect \n")
		points -= 1

	print("Eighth Question \n")
	question8 = input("Who was the president who gave 'I have a dream' speech A) John F. Kennedy B) Richard Nixon C) Martin Luther King D) Barack Obama ")
	if question8 == "C":
		print("Correct")
		points += 1
	else: 
		print("Incorrect")
		points -= 1
	print("points", points, "/8")







