
from election import Election
from user import User

people_running = {"Jeff" : 0, "John" : 0}

election = Election(people_running, 10)

id = 6969420

user = User("Kay", "123 e rd", id)

verify = user.verify()

if verify == True:
    print("You are logged in")
else:
    print("Enter your id right")
    quit()

person = input("Who do you want to vote for: ")
election.vote(person)
print(f"You have vote for {person}")



    