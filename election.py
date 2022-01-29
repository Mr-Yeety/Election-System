class Election():
     
    def __init__(self, people_running,num_of_people ):
        self.people_running = people_running
        self.num_of_people = num_of_people
        
    
    def vote(self, candidate):
        self.people_running[candidate]+=1
    

