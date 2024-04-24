q1 = input("Which is my favorite color? \n a.Black, b.White, c.Blue, d.Yellow \n" )
q2 = input("What is my name? \n a.Dev, b.Devendra, c.Devang, d.Devans \n" )
q3 = input("What is my Religion? \n a.Christian, b.Parsi, c.Hindu, d.Sikh \n" )
q4 = input("In which year there is first covid-19 case in india? \n a.2003, b.2019, c.2021, d.2020 \n" )
questions = [q1,q2,q3,q3]
answers = ['b','a','c','d']
score = 0

for i in questions:
    print(questions)
    if (q1 == answers[0], q2 == answers[1], q3 == answers[2], q4 == answers[3]):
        score = score+5
    if (q1 != answers[0], q2 != answers[1], q3 != answers[2], q4 != answers[3]):
        break
print("Well played, Your score is : ",score)

#  error