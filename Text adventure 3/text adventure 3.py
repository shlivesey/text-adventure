#Name of Coder: Harper Livesey
#Name of Script: Text Adventure Build 3  
#You get cought in a storm and the only dry place is a museum.
#You walk in and hear a voice telling you, you need to play a game

import name_test

#beginning 
def textadventure():
    
    #setting the scene
    print("The sky is dark and rain falls all around the building.")
    print("You look at your surroundings. And then you hear it.")
    print("A voice, no one is with you so who would it be?")

#introduction of the ghost
def Intro():
    
    #speaking intro
    intro=input("Welcome! I am a ghost, I live here.")
    print("Well it looks like your not going anywhere any time soon.")
    print("So how about this, let's learn about some of the worst serial")
    print("killers of all time. You get the questions right, you can leave.")
    print("Get any wrong, however, you will stay here, with me, forever.")
    print("How about that! Would you like to get started? Yes or No?")

    #answer option 1
if intro== "yes":

        #responce 1
        print("Ok, great. I see your feelng lucky")

firstMove()

    #answer option 2
if intro=="no":

        #responce 2
        print("Too bad for you. Looks like i've got my self a friend.")

                  
def firstMove():
    
    #first move
    firstMove=input("Lets get started, which way right or left?")

    #goes left on the first move
    if firstMove== "left":

        #say Joel the Ripper
        print("Let's learn about Joel the Ripper.")
        print("Joel the Ripper aka Joel David Rifkin was born on January 20, ")
        print("1959 in New York City, New York.")
        print("When he was arrested police found a body under a tarp.")
        print("He was found guilty of nine counts of second degree")
        print("murder in 1994.")
        print("Rifkin was then sentenced to 203 years to life in prison.")

        JoelQuestion()
        
    #goes right on the first move
    if firstMove== "right":

        #say Lady Rotten
        print("Let's learn about Lady Rotten.")
        print("Lady Rotten aka Mary Ann Cotton was born on October 31,")
        print("1832 in Low Moorsley, England.")
        print("Cotton killed around 21 people including 3 out of 4 husbands")
        print("and 11 of her children.")
        print("Before she was arrested rumors were spread saying that")
        print("Mary Ann was killing people with arsenic.")
        print("After some tests on the poison she was arrested but")
        print("the trial was delayed because she was pregnant.")
        print("She was executed by hanging on March 24, 1873.")
        print("Two out of her 13 children survived.")

        MaryQuestion()

#question about Joel
def JoelQuestion():

    #question-when was he born?
    JoelQuestion=input("When was he born? 1959 or 1877?")

    #right answer
    if JoelQuestion=="1959":

        #say
        print("Good job!")

    #wrong answer
    if JoelQuestion=="1877":

        #say
        print("Wrong, I thought you were better than this.")

#question about Mary
def MaryQuestion():
    
    #question- how many kids did she have?
    MaryQuestion=input("How many kids did she have? 11 or 13?")

    #wrong answer
    if MaryQuestion=="11":
        
        #say
        print("NO!! But eather way it was too many.")

    #right answer
    if MaryQuestion=="13":
        
        #say
        print("Your doing better than I thought.")

#second move
def secondMove():
    
    #question to move
    secondMove=input("Good, you made it this far not many poeple do.")
    print("Now lets see... left or right?")

    #goes left second
    if secondMove=="left":

        #responce for left move
        print("Ooh you got Mr. Pickton.")
        print("The Pig Farmer aka Robert William Pickton was born on")
        print("October 24, 1949, in Port Coquitlam, British Columbia.")
        print("He was convicted of six murders but has confessed to 49.")
        print("In 1999,  police got a tip telling them that Robert had a")
        print("freezer full of human flesh. On February 22, 2002, he was arrested")
        print("and charged with two counts of first-degree murder.")
        print("After a long trial he was sentenced to life in prison")
        print("on December 22, 2007.")

        RobertQuestion()

    #goes right second
    if secondMove=="right":

        #responce for right move
        print("Dennis Andrew Nilsen aka The Kindly Killer was born November 23,")
        print("1945 in Fraserburgh Aberdeenshire, Scotland.")
        print("He murdered at least 13 boys and young men between 1978 and 1983.")
        print("He was arrested on February 9, 1983, and was sentenced to life in")
        print("prison. He died on May 12 2018 due to Pulmonary embolism")
        print("(blocking of an artery in the lungs.)")


        DennisQuestion()

#question about Robert
def RobertQuestion():

    #question- how many murders?
    RobertQuestion=input("How many murders did he confess to? 49 or 94?")

    #right answer
    if RobertQuestion=="49":
        
        #say
        print("Correct. Your doing better than I thought.")

    #wrong answer
    if RobertQuestion=="94":

            #say
            print("Wrong, my expectations were low but you made me re-think everyting.")

#question about Dennis
def DennisQuestion():

    #question- when did he die?
    DennisQuestion=input("When did Dennis die? February 9 1983 or May 12 2018?")

    #wrong answer
    if DennisQuestion=="February 9 1983":

        #say
        print(" Sorry but that was when he was arrested. Bless your heart.")

    #right answer
    if DennisQuestion=="May 12 2018":
        
        #say
        print("Well well well. I thought I would get you with that one.")
        print("Let's see how you do on the next one.")

#thirdMove
def thirdMove():

    #question to move
    thirdMove=input("Okay, well, I didn't think you would get here.")
    print("I guess it's only fair to keep going. So left or right?")

    #goes left third
    if thirdMove=="left":

        #response for left move
        print("Anna Marie Hanhn also known by her nickname Arsenic Anna.")
        print("She was born on July 7, 1907, in Bavaria, Germany.")
        print("She murdered five people in the years 1933-1937.")
        print("She would poison her victims (elderly men) and then rob them")
        print("to help support her gambling habit. An autopsy revealed high")
        print("levels of arsenic in one of her victims which was very suspicious")
        print("so police opened an investigation. Because this victim was one")
        print("of her clients, it was even more suspicious that two more of her")
        print("previous clients had died. It was revealed that they also had")
        print("high levels of arsenic. She was arrested and was convicted in")
        print("November 1937. She was sentenced to death.")
        print("She went to the electric chair on December 7, 1939. ")

        AnnaMarieQuestion()
    
    #goes right third
    if thirdMove=="right":

        #response for right move
        print("Nannie Doss also known as The Giggling Granny.")
        print("She was born with the name Nancy Hazel. She was born on")
        print("November 4, 1905.")
        print("She murdered 11 people through the years 1927-1954.")
        print("She killed her four husbands, two children, her sister,")
        print("her mother, two grandsons, and a mother-in-law.")
        print("Her last husband started feeling sick and was admitted to")
        print("the hospital with flu-like symptoms. He was treated then released")
        print("on the fifth of October. He died a week later.")
        print("His sudden death was very suspicious so police ordered an autopsy.")
        print("The autopsy revealed he ingested a huge amount of arsenic.")
        print("Nannie Doss was arrested and she confessed to killing her family.")

        NannieDossQuestion()

#question about Anna Marie
def AnnaMarieQuestion():

    #question- convicted?
    AnnaMarieQuestion=input("What day did she die? July 7th or December 7th?")

    #wrong answer
    if AnnaMarieQuestion=="July 7th":

        #say
        print("She was BORN on July 7th.")

    #right answer
    if AnnaMarieQuestion=="December 7th":

        print("Wow ok, you got right.")


#question about Nannie Doss
def NannieDossQuestion():

    #question- name
    NannieDossQuestion=input("What name was she born with?")
    print("Nannie Doss or Nancy Hazle?")

    #wrong answer
    if NannieDossQuestion=="Nannie Doss":
    
        #say
        print("Wrong")

    #right answer
    if NannieDossQuestion=="Nancy Hazle":

        #say
        print("Nice one.")

#fourth move
def fourthMove():
    
        #say
    print("You have no idea where you are.")
    print("You have gone down numerous hallways snd everything looks the same.")
    print("No matter how hard you try you can't remember where you turned.")
    print("What after feels like an eternity you finally hear the voice again.")

        #say
    print("You did well, I am very surprised that you made it.")
    


#question to stay
    fourthMove=input("So you can leave... but would you like to stay? Yes or no?")

            #yes
    if fouthMove=="yes":

            #say

            print("Yay! I am so excited to have a friend!")

            #no
    elif fourthMove=="no":

            #say

                print("Fair enough. See ya later. Hope you come back soon") 
        

        

    

    
    

 
                     



textadventure()
Intro()
secondMove()
thirdMove()
fourthMove()


