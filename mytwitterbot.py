# mytwitterbot.py
import sys
import time, random
import simple_twit

# Assign the string values that represent your developer credentials to
# each of these variables; credentials provided by the instructor.
# If you have your own developer credentials, then this is where you add
# them to the program.
# Consumer Key also known as API key
CONSUMER_KEY = 
# Consumer Secret also known as API Key Secret
CONSUMER_SECRET = 

# Project 04 Exercises

##api = simple_twit.create_api(CONSUMER_KEY, CONSUMER_SECRET)

# Exercise 1 - Get and print 10 tweets from your home timeline
# For each tweet, print the tweet ID, the author's name,
# the author's screen_name, the tweet creation date, and the
# tweet full_text
def exercise1(api):
    Home_TimeLine = simple_twit.get_home_timeline(api, 10)
    for i in Home_TimeLine:
        print()
        print("Tweet ID: " + str(i.id))
        print("Author's Name: " + i.user.name)
        print("Author's screen_name: " + i.author.screen_name)
        print("Creation date: " + str(i.created_at)) 
        print("Full Text: " + i.full_text)
        print() 
        time.sleep(15)        

# Exercise 2 - Get and print 10 tweets from another user's timeline
# For each tweet, print the tweet ID, the author's name,
# the author's screen_name, the tweet creation date, and the
# tweet full_text
def exercise2(api):
    User_TimeLine = simple_twit.get_user_timeline(api, "webtoonofficial", 10)
    for i in User_TimeLine:
        print()
        print("Tweet ID: " + str(i.id))
        print("Author's Name: " + i.user.name)
        print("Author's screen_name: " + i.author.screen_name)
        print("Creation date: " + str(i.created_at))
        print("Full Text: " + i.full_text)
        print()
        time.sleep(15)

# Exercise 3 - Post 1 tweet to your timeline.
def exercise3(api):
    #For this I will randomly tweet out a class and a random prediction for the grade I will get
    #For privacy sake I will not state the actual class name/number and instead use psuedonyms 
    classes = ["Applied Math & Stats With R", "Linear Algebra", "Intro to Writing", "Campus Life", "Digital Technology"]
    Grades = ["A","A-","B+","B","B-","C+","C","D+","D"]
    selected_class = random.choice(classes)
    selected_grade = random.choice(Grades)
    simple_twit.send_tweet(api, "For " + selected_class + " I predict that I will get a " + selected_grade)



# Exercise 4 - Post 1 media tweet to your timeline.
def exercise4(api):
    simple_twit.send_media_tweet(api, "Loved seeing this duo perform such a clean counter in the recent episode!", "Blue_Lock.jpg")  

# End of Project 04 Exercises


# YOUR BOT CODE GOES IN HERE

#First want to create a Webtoon Class to help store Genre, Title & Day
class Webtoon():
    def __init__(self, title = None, genre = None, day = None, rank = None):
        self.title = title
        self.genre = genre
        self.day = day
        self.rank = rank
#create list to hold all webtoons, will call this AW 
AW = []

#Creating all the Webtoon Objects 
W1 = Webtoon("Flawed Almighty","Action","Monday","3rd")
AW.append(W1) 
W2 = Webtoon("Reality Quest","Action","Monday","8th")
AW.append(W2) 
W3 = Webtoon("Wind Breaker","Sports","Monday","1st")
AW.append(W3) 
W4 = Webtoon("The Lazy Lord Masters The Sword","Action","Monday","4th")
AW.append(W4) 
W5 = Webtoon("The Build Up","Sports","Monday","5th")
AW.append(W5)
W6 = Webtoon("To You Who Swallowed A Star","Romance","Monday","7th")
AW.append(W6) 
W7 = Webtoon("Marry My Husband","Romance","Monday","6th")
AW.append(W7) 
W8 = Webtoon("Dungeons and Artifacts","Action","Monday","9th")
AW.append(W8) 
W9 = Webtoon("Tower of God","Action","Monday","2nd")
AW.append(W9) 
W10 = Webtoon("No Outtakes","Romance","Monday","10th")
AW.append(W10)

W11 = Webtoon("The Advanced Player of the Tutorial Tower","Action","Tuesday","3rd") 
AW.append(W11) 
W12 = Webtoon("My Younger Brother's Friend","Romance","Tuesday","4th") 
AW.append(W12)
W13 = Webtoon("Seasons of Blossom","Romance","Tuesday","1st")
AW.append(W13)
W14 = Webtoon("Exchange Student","Drama","Tuesday","6th")
AW.append(W14)
W15 = Webtoon("Villian to Kill","Action","Tuesday","5th")
AW.append(W15)
W16 = Webtoon("The Tex Reaper","Drama","Tuesday","7th")
AW.append(W16)
W17 = Webtoon("Odd Girl Out","Drama","Tuesday","2nd")
AW.append(W17)
W18 = Webtoon("Viral Hit","Action","Tuesday","8th")
AW.append(W18)
W19 = Webtoon("Who's Mr. President?","Drama","Tuesday","10th")
AW.append(W19)
W20 = Webtoon("Eleceed","Action","Tuesday","9th")
AW.append(W20)

W21 = Webtoon("My S-Class Hunters","Action","Wednesday","3rd")
AW.append(W21)
W22 = Webtoon("Teenage Mercernary","Action","Wednesday","4th")
AW.append(W22)
W23 = Webtoon("Infinite Leveling:Murim","Action","Wednesday","2nd")
AW.append(W23)
W24 = Webtoon("The Fox Club","Romance","Wednesday","5th")
AW.append(W24)
W25 = Webtoon("Omniscient Reader","Action","Wednesday","1st")
AW.append(W25)
W26 = Webtoon("Return of the Mad Demon","Action","Wednesday","9th")
AW.append(W26)
W27 = Webtoon("The Dungeon Cleaning Life of a Once Genius Hunter","Action","Wednesday","10th")
AW.append(W27)
W28 = Webtoon("True Beauty","Romance","Wednesday","6th")
AW.append(W28)
W29 = Webtoon("Date First, Love Later","Romance","Wednesday","7th")
AW.append(W29)
W30 = Webtoon("Return of the Mad Demon","Action","Wednesday","8th")
AW.append(W30)

#Create the Genre Comments

W31 = Webtoon("unOrdinary","Action","Thursday","5th")
AW.append(W31)
W32 = Webtoon("Pyramid Game","Drama","Thursday","1st")
AW.append(W32)
W33 = Webtoon("Best Teacher Baek","Action","Thursday","2nd")
AW.append(W33)
W34 = Webtoon("Act Like you Love Me!","Romance","Thursday","3rd")
AW.append(W34)
W35 = Webtoon("See you in my 19th Life","Romance","Thursday","4th")
AW.append(W35)
W36 = Webtoon("Mythic Item Obtained","Action","Thursday","6th")
AW.append(W36)
W37 = Webtoon("Kill The Dragon","Action","Thursday","7th")
AW.append(W37)
W38 = Webtoon("My Dud to Stud Boyfriend","Drama","Thursday","8th")
AW.append(W38)
W39 = Webtoon("Weak Hero","Action","Thursday","9th")
AW.append(W39)
W40 = Webtoon("Threads of Love","Romance","Thursday","10th")
AW.append(W40)

W41 = Webtoon("Romance 101","Romance","Friday","2nd")
AW.append(W41)
W42 = Webtoon("Maybe Meant to Be","Romance","Friday","3rd")
AW.append(W42)
W43 = Webtoon("Murim RPG Simulation","Action","Friday","4th")
AW.append(W43)
W44 = Webtoon("Operation: True Love","Romance","Friday","5th")
AW.append(W44)
W45 = Webtoon("Return of the Blossoming Blade","Action","Friday","1st")
AW.append(W45)
W46 = Webtoon("So I Married the Anti-Fan","Romance","Friday","6th")
AW.append(W46)
W47 = Webtoon("The God of Highschool","Action","Friday","7th")
AW.append(W47)
W48 = Webtoon("Rewriting the Villianess","Drama","Friday","8th")
AW.append(W48)
W49 = Webtoon("The Earth's Chosen Savior","Action","Friday","10th")
AW.append(W49)
W50 = Webtoon("I Love Yoo","Drama","Friday","9th")
AW.append(W50)

W51 = Webtoon("Return to Player","Action","Saturday","1st")
AW.append(W51)
W52 = Webtoon("She's Hopeless","Drama","Saturday","2nd")
AW.append(W52)
W53 = Webtoon("Double Click","Sports","Saturday","3rd")
AW.append(W53)
W54 = Webtoon("How to Become A Dragon","Drama","Saturday","4th")
AW.append(W54)
W55 = Webtoon("Our Secret Alliance","Romance","Saturday","5th")
AW.append(W55)
W56 = Webtoon("The Academy's Undercover Professor","Action","Saturday","6th")
AW.append(W56)
W57 = Webtoon("I Get Stronger The More I Eat","Action","Saturday","7th")
AW.append(W57)
W58 = Webtoon("Knight Under My Heart","Action","Saturday","8th")
AW.append(W58)
W59 = Webtoon("To Be Ordinary!","Drama","Saturday","9th")
AW.append(W59)
W60 = Webtoon("The Blood of the Butterfly","Action","Saturday","10th")
AW.append(W60)

W61 = Webtoon("Get Education","Drama","Sunday","1st") 
AW.append(W61)
W62 = Webtoon("The Lone Necromancer","Action","Sunday","2nd")
AW.append(W62)
W63 = Webtoon("After School Lessons for Unripe Apples","Drama","Sunday","3rd")
AW.append(W63)
W64 = Webtoon("The World is Money and Power","Action","Sunday","4th")
AW.append(W64)
W65 = Webtoon("Time Roulette","Action","Sunday","5th")
AW.append(W65)
W66 = Webtoon("Master of Villains","Action","Sunday","6th")
AW.append(W66)
W67 = Webtoon("There Must Be Happy Endings","Romance","Sunday","7th")
AW.append(W67)
W68 = Webtoon("From a Kinght to a Lady","Drama","Sunday","8th")
AW.append(W68)
W69 = Webtoon("Can I Take it Back?","Romance","Sunday","9th")
AW.append(W69)
W70 = Webtoon("Perfect Marriage Revenge","Romance","Sunday","10th")
AW.append(W70)

Mon = [] 
Tue = [] 
Wed = [] 
Thur = [] 
Fri = [] 
Sat = [] 
Sun = []


for i in AW:
    if i.day == "Monday":
        Mon.append(i)
    elif i.day == "Tuesday":
        Tue.append(i)
    elif i.day == "Wednesday":
        Wed.append(i)
    elif i.day == "Thursday":
        Thur.append(i)
    elif i.day == "Friday":
        Fri.append(i)
    elif i.day == "Saturday":
        Sat.append(i)
    elif i.day == "Sunday":
        Sun.append(i)
    
Sports = ["The friendship in today's chapter was wholesome!",
        "All the supporting characters played so well in the match!",
        "I really want our main characters to lose for once. It's no fun if they will all the time!",
        "Can anyone even rival the main cast????",
        "I might not watch IRL sports but Webtoons about Sports is a different story!"]

Romance = ["The relationship between the two leads is goals fr fr!",
           "Here we go again with the common romance troupes",
           "Ughhh really hate how the antagonist is trying to ruin their relationship, like damn get a life",
           "OOOoooh the love traingle this episode was very tension filled"]

Action = ["DAMMNNNNN the action in this episode was immaculate!",
          "Watching our main characters in action is always riveting!",
          "HMMMMMMMMMMM the power diff between our main character and everyone else is kinda broken ngl..",
          "All I can really say about this chapter is SKILL ISSUE tbh",
          "Ok but like it's kinda crazy that I'll never get tired of this",
          "Bruh if this ever get's animated, it would be \U0001f525"]

Drama = ["I LIVEEE for the petty drama in today's chapter",
         "All the drama I'm glad I missed in highschool gets fufilled by this Webtoon",
         "Okay, IK I kinda signed up for this when I decided to read a Webtoon under Drama, but like you didn't have to do the characters like that",
         "That's enough Drama today for me, I shall now just not react to anything anymore for today",
         "I'm in shambles after reading this chapter, if you need to contact me, just don't \U0001f62d"]

Day_List = [Mon, Tue, Wed, Thur, Fri, Sat, Sun] 
def twitterbot(api):
    #First I want to determine what day it is, I will import datetime to do this
    from datetime import datetime
    #Let TD stand for Today, D stand for Day and COD be choice of the day
    TD = datetime.now()
    D = TD.weekday()
    COD = random.choice(Day_List[D])
    #Now that I know that I can choose a title, I now have to choose a genre comment
    #Let the choice of genre comment be represented by COG
    if COD.genre == "Action":
        COG = random.choice(Action)
    elif COD.genre == "Romance":
        COG = random.choice(Romance)
    elif COD.genre == "Drama":
        COG = random.choice(Drama)
    elif COD.genre == "Sports":
        COG = random.choice(Sports)

    simple_twit.send_media_tweet(api,"Today's Recommendation is: " + COD.title + "\n" + "My comment on today's chapter: " + COG, COD.day +".gif")
    #Now I need to reply to my earlier tweet with what I want to say
    #Need to get earlier tweet, inputting the username of the bot and etc
    time.sleep(20) 
    Last_Tweet = simple_twit.get_user_timeline(api, "Username", 1)
    Last_Tweet_ID = Last_Tweet[0].id 
    simple_twit.send_reply_tweet(api, "@Username" + " Out of My Personal Top 10 For " + COD.day + " This is Ranked " + COD.rank +
                                 "\n" + "Disclaimer: These rankings are my personal opinion and is still considered a Top 10 of Mine " + 
                                 " So, give it a try even if it's ranked low! I'm sure you won't be dissapointed! " + "\U0001f601", Last_Tweet_ID)


if __name__ == "__main__":
    # This call to simple_twit.create_api will create the api object that
    # Tweepy needs in order to make authenticated requests to Twitter's API.
    # Do not remove or change this function call.
    # Pass the variable "api" holding this Tweepy API object as the first
    # argument to simple_twit functions.
    simple_twit.version()
    api = simple_twit.create_api(CONSUMER_KEY, CONSUMER_SECRET)

    # Once you are satisified that your exercises are completed correctly
    # you may comment out these function calls.
##    exercise1(api)
##    exercise2(api)
##    exercise3(api)
##    exercise4(api)

    # This is the function call that executes the code you defined above
    # for your twitterbot.
    twitterbot(api)
