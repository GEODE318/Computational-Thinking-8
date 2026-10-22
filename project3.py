Happiness = 100
Health = 100
Karma = 0
World_Anger = 100

Answer = input ("You wake up at 11 pm what chaos or goodness will you cause today? Go out on the town or stay inside? how strange the it feels like you have lived this life a million times already.")
if Answer == "Stay" or "Stay inside" or "stay" or "stay inside" or " Stay" or " Stay inside" or " Stay Inside" or " stay" or "stay inside":
    Home = input("Do you want to play video games or go outside?")
    if Home == "video games":
        Health -= 2
        print("You stay a home playing video games and eating junk food for hours your parents wake up and are really mad at you.")
        input
        Health -= 1
        Home == ("You keep playing video games all day for the rest your life and you waste you day and your life")
        input()
        #Gamer ending this happens if you 
        print ("you live until the good old age of 45 probably as a result of all of that screen time and junk food as you close your eyes and drift off a person walks towards they are ancient with rings of diffrent sizes and color going from their wrist to there elbow and as they walk towards you. you realize that they are you you look down and see a plain flat ring appear around your arm as you stare you realize that they are you. you but having lives so many lives they open their mouth to speak")
        print ("Wow you really did nothing how sad but i will give you another chance")
    Answer1 = input ("You wake up at 11 pm what chaos or goodness will you cause today? Go out on the town or study? how strange the it feels like you have lived this life a million times already")
    if Answer1 == "Study" or "study":
        Health -= 2
        Home2 = input = ("You stay at home studing for your quiz on monday and crying over math problems for hours your parents wake up and are really proud of you. Keep studing or Keep studing? you don't have a choice here")
        if Home2 == "Study" or "Keep studing" or " Study" or " study" or " Keep studing" or "study":
            Health  -= 2
            Karma += 1
            input()
            #Good student ending you get it if you just study
            Home2 == ("You keep studing all day for the rest your life not stopping to even eat or sleep and you waste you day and your life")
            print ("you live until the good old age 15 of probably as a result because you didn't sleep or eat as close your eyes and drift off to the end a person walks towards they are ancient with rings of diffrent sizes and color going from their wrist to there elbow and as they walk towards you. you realize that they are you you look down and see a plain ring with little math problem in graved on it appear around your arm as you stare you realize that they are you. you but having lives so many lives they open their mouth to speak")
            print ("Wow you are quite the sudent huh.")
if Answer == "Town" or "Go out on the town" or "town":
    Stranger = input ("you sneak around in the dark and you see a strange man wandering around. Do you follow him? Run up to him? or keep walking?")
    if Stranger == "Follow him":
        Karma += -1
        What_now = input("you followe him until he turns a conner and dissapears as you walk around sad trying to find somthing else to do you think you see glowing eye but when you blink they are gone, What should you do now? go home or go to your friends house")
        if What_now == "go home" or "Go Home" or "Go home" or " go home":
            # Go home after going out ending
            print ("when you go home the sun is already rising you go and sleep to the next night")
            
        if What_now == "go to friends house" or "Friends house" or "Friend" or "friend house" or "friend":
           #Hang out with friend ending
           print ("you go to your friends house and have a great time")

    if Stranger == "Run up to him" and World_Anger == 100:
         #This is meet strange enity ending you get it if you run up to strange enity
        Health -= 100
        print ("His head turns around while his body stays put his head keeps turning until it has locked eyes with and says one word in a whisper run, you turn and run you try to stop but you can't your legs are a blur underneth you. keep running and never stop. later people will tell stories about you they will call you the ghost runner.")