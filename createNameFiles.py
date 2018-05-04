# Author: Kyle Mayer
# Date: 5/3/2018

#TODO:
    #could always add more names
    #could also add addresses to random




firstNames = ["John", "Christy", "Mike", "Ashley", "Thomas", "Harry", "Marie",
       "Al", "Johnathan", "Terry", "Joe", "Bob", "Jennifer", "Teresa", "Mary",
       "Larry", "Todd", "Jerry", "Rick", "Morty", "Owen", "Toby", "Maggie",
       "Michelle", "Christina", "Amanda", "Aaron", "Erin", "Aaron", "Andrew",
       "Kelly", "Malcom", "Martin", "Michael", "Lauren", "Susan", "Angela",
       "Richard", "Sam", "Steven", "Phil", "Larry", "Ray", "Chelsea", "Sarah",
       "Barry", "Linda", "Germaine", "Cindy", "Cynthia", "Tom", "Ted", "Teddy",
       "Jon", "Jimmy", "James", "Jonny", "Jane", "Janie", "Estevan", "Esteban",
       "Stephen", "Steven", "Steve", "Cathy", "Hillary", "Bill", "Alan", "Allen"
       "Pat", "Patrick", "Dion", "Kevin", "Kyle", "Daniel", "Dan", "David",
       "Dave", "Andrew", "Luke", "Rachel", "Christina", "Lauren", "Christi", 
       "George", "Anne", "Annie", "Anabelle", "Maggie", "Meg", "Melissa"]

lastNames = ["Sanchez", "Doe", "James", "Jones", "Guiterrez", "Bryant",
        "Davidson", "Smith", "Brady", "Patton", "Williams", "Miller", "Taylor",
        "Thompson", "Hill", "Allen", "Scott", "Young", "Jackson", "Long",
        "Black", "Wilson", "Dillard", "Burnett", "Rodriguez", "Simpson",
        "Lucero", "Dean", "Segura", "Wilson", "Paul", "Cranston", "Hughes",
        "Thomas", "Velez", "Salazar", "Sisneros", "Peters", "Hunt", "Mills",
        "Grey", "Johnson", "Mitchell", "Carter", "Perez", "Nelson", "Roberts",
        "Collins", "Edwards", "Cook", "Bell", "Murphy", "Evans", "Myers",
        "Campbell", "Morris", "Rogers", "Bailey", "Rivera", "Scott", "Turner",
        "Gomez", "Murray", "Freeman", "Webb", "Porter", "Tucker", "Hunter", 
        "Ortiz", "Gibson", "McDonald", "Lane", "Fox", "Harper", "Lewis",
        "Armstrong", "Weaver", "Greene", "Green", "Andrews"]

domainNames = ["hotmail.com", "yahoo.com", "gmail.com", "cnm.edu",
            "outlook.com", "amazon.com", "abq.com", "live.com", "aol.com",
            "juno.com", "mac.com", "hotmail.co.uk", "4chan.org"]



def writeListToFile(filename, nameList):
    f = open(filename, "w")
    
    for name in nameList:
        f.write(name + "\n")

    f.close()


writeListToFile("firstNames.txt", firstNames)
writeListToFile("lastNames.txt", lastNames)
writeListToFile("domainNames.txt", domainNames)

