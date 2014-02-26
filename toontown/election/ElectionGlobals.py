from direct.interval.IntervalGlobal import *
from otp.nametag.NametagConstants import *
from pandac.PandaModules import *
from random import choice

########################
#        Props         #
########################

FlippyWheelbarrowPies = [
    # Format: posHprScale
    [1.16, 11.24, 7.00, 246.80, 351.25, 0.00, 1.60, 1.40, 1.8],
    [2.27, 8.02, 6.35, 104.04, 311.99, 9.46, 1.35, 1.35, 1],
    [-1.23, 7.33, 6.88, 276.34, 28.61, 350.54, 1.41, 1.41, 1.6],
    [0.27, 8.24, 6.42, 198.15, 351.87, 355.24, 1.93, 2, 2],
    [0.06, 5.23, 6.78, 63.43, 355.91, 15.26, 1.3, 1.6, 1.8],
    [-0.81, 11.37, 6.82, 326.31, 5.19, 19.98, 1.76, 1.86, 1.5],
    [1.35, 10.09, 5.92, 35.54, 353.66, 343.30, 1.50, 1.90, 1.8],
    [1.9, 5.59, 6.5, 75.96, 326.31, 8, 1.76, 1.56, 1.5],
    [-1.74, 5.42, 6.28, 327.53, 318.81, 4.76, 1.8, 2, 2],
    [-1.55, 9.22, 5.72, 266.53, 341.57, 0.00, 2.09, 1.68, 1.81],
]



########################
#   Election Sequence  #
########################

#Election Sequence Music
IntroMusic = 'phase_4/audio/bgm/EE_intro.ogg' #Played when Alec, Flippy, and Slappy enter



########################
#   Slappy's Balloon   #
########################

BalloonBasePosition = [-15, 33, 1.1]
BalloonScale = 2.5

# Let's define all of Slappy's speeches.
# There should be exactly 12 phrases for each to fit with the sequence.
# If you add another, make sure to add it to SlappySpeechChoices.
SlappySpeech1 = [
    'Hiya! Up for a ride?',
    'Off we goooo!',
    "In case you didn't get it back there, that was a pun.",
    '"Up" for a ride. Get it?',
    'Haha! I quack myself up.',
    'That was another pun!',
    "Do you know any good puns? I'm full of them.",
    "That wasn't a pun, though. I should have had one there. It was fitting.",
    "Oh man, we're almost back already?",
    "Well, at least we had a WHALE of a time!",
    "Err- no. Wrong pun. That one didn't make sense.",
    "I'll CATCHA later! Get it, because of the whale pun? It makes sense now. I planned that."
]
SlappySpeech2 = [
    'Hello! Want a ride, I assume?',
    "Good! It would be kind of weird if you didn't.",
    "I take it you're a balloon fanatic like myself, eh?",
    "No? Oh. I don't see how you can't be.",
    "Just look at this thing. It's a 500 pound bag floating in the sky!",
    "If that isn't amazing, I don't know what is.",
    "Small balloons, too. You know, I've always wanted to be a balloon salesman.",
    "I'd get my own little cart and everything!",
    "They soar thrugh the skies, going beyond what we know.",
    "Maybe even into another world. Who knows what they'd see on the outskirts of Toontown?",
    "I've always wondered what kind of mysteries lie out there. The balloons know.",
    "D'awh, here already. I was just about to get into the history of balloons. Come back any time!"
]
SlappySpeech3 = [
    'Hey there! Yep, just hop on in!',
    "You know, some may consider it rude to jump into someone else's balloon without permission.",
    "In fact, I'm going to have to ask you to step out now.",
    "Yeah, just right off the side there. It's not too high up yet.",
    "I'm joking! I'm joking. Don't jump out, the ride is free.",
    "Can you see your house from up here?",
    "I can't. This cardboard hill is in the way.",
    "I've always wondered why they put those up. Why not enjoy the scenery?",
    "Not to mention the Jellybeans they could have saved by not buying paint.",
    "It seems counterproductive to me. Those are definitely getting torn down.",
    "That is, if I get elected. Hey, are you voting for me?",
    "Nonono, don't tell me. I want to be surprised. Remember this free balloon ride at the pools, though!"
]
# This one was being chosen too often. It got old. Renable it if more phrases are added so there is a larger pool to choose from.
'''SlappySpeech4 = [
    'Quackity quack quack!',
    "Quack!",
    "Quack quackity, quackity quacky quack.",
    "Quack quack quacky?",
    "Quack quack quack. Quack quack, quacky quack quacky quack quackity quack!",
    "Quackity?",
    "Quack. Quack quack, quacky quack quackity.",
    "Quack quacky. Quack?",
    "Quack, quack, quack, quackity quacky. Quacky!",
    "Quack, quack quacky! Quack?",
    "Ohohoh man, I'm just messing with you! I was pretending to use SpeedChat that whole time.",
    "Did I have you fooled or what? Hahahaha, that's rich. Come back again and we might have a real conversation!"
]'''
SlappySpeech5 = [
    'Oooh, look who it is!',
    "I was wondering when you would come by for a ride.",
    "How are things going? Having fun with this election excitement?",
    "I know I certainly am. I've been on hundreds of these balloon rides, and they never get old.",
    "You get used to the air sickness after a while.",
    "Woah, look over there! You can see some of the grey!",
    "The grey is just one of those many things in Toontown that bewilders me.",
    "An undrawn area, just waiting for color. Can you imagine the creativity?",
    "It's an unexplored blank canvas of imagination.",
    "You know what? You and I -- after this election, we're going to go out there.",
    "You and I will figure out the secrets of the grey, unleash the creativity it holds. I promise you on that.",
    "We'll find out what it is, for not only Toontown but for the whole Tooniverse. Make sure you hold me to it! "
]
# Now we need to take those phrases and pick one to use
SlappySpeechChoices = [SlappySpeech1, SlappySpeech2, SlappySpeech3, SlappySpeech5]
SlappySpeeches = choice(SlappySpeechChoices)

# Number of balloon flight paths. Change if you add more below.
NumBalloonPaths = 1

def generateFlightPaths(balloon):
    # This is quite messy imo... but I didn't have much time to think about it.
    # For each sequence, you basically copy and paste this whole section and edit
    # the sequence. When you add a new sequence here, you MUST edit the 
    # SLAPPY_BALLOON_NUM_PATHS constant.
    flightPaths = []
    flightPaths.append(
        Sequence(
            # Lift Off
            Wait(0.5),
            balloon.balloon.posHprInterval(1.5, Point3(-19, 35, 3), (0, 2, 2)),
            balloon.balloon.posHprInterval(1.5, Point3(-23, 38, 5), (0, -2, -2)),
            balloon.balloon.posHprInterval(8.0, Point3(-53, 75, 24), (0, 0, 0)),
            balloon.balloon.posHprInterval(0.5, Point3(-54, 76, 25), (5, 2, 2)),

            # To the tunnel we go
            balloon.balloon.posHprInterval(11.0, Point3(-105, 33, 54), (180, -2, -2)),
            balloon.balloon.posHprInterval(0.5, Point3(-106, 34, 55), (175, -4, 0)),

            # Lets drop a weight on the gag shop
            balloon.balloon.posHprInterval(10.0, Point3(-100, -60, 54), (0, 2, -2)),
            balloon.balloon.posHprInterval(0.5, Point3(-97.5, -59.5, 54), (-2, -2, 2)), 

            # Rats, we missed! Lets checkout the podium
            balloon.balloon.posHprInterval(18.0, Point3(60, -10, 54), (-70, 0, 0)),
            balloon.balloon.posHprInterval(0.5, Point3(62, -11, 54), (-65, -2, 2)),

            # Set her down; gently
            balloon.balloon.posHprInterval(15.0, Point3(-15, 33, 1.1), (0, 0, 0)),
        )
    )
    
    # Return the flight paths back to the HotAirBalloon...
    return flightPaths

def generateToonFlightPaths(balloon):
    # This isn't all that great of a solution, but it stops jittering caused when we reparent the client to the balloon.
    # The downside is that it causes some minor latency for others, but not enough to care.
    toonFlightPaths = []
    toonFlightPaths.append(
        Sequence(
            # Lift Off
            Wait(0.5),
            base.localAvatar.posInterval(1.5, Point3(-19, 35, 3)),
            base.localAvatar.posInterval(1.5, Point3(-23, 38, 5)),
            base.localAvatar.posInterval(8.0, Point3(-53, 75, 24)),
            base.localAvatar.posInterval(0.5, Point3(-54, 76, 25)),

            base.localAvatar.posInterval(11.0, Point3(-105, 33, 54)),
            base.localAvatar.posInterval(0.5, Point3(-106, 34, 55)),
            # Lets drop a weight on the gag shop
            base.localAvatar.posInterval(10.0, Point3(-100, -60, 54)),
            base.localAvatar.posInterval(0.5, Point3(-99, -59, 53)),      
            # Rats, we missed! Lets checkout the podium
            base.localAvatar.posInterval(18.0, Point3(60, -10, 54)),
            base.localAvatar.posInterval(0.5, Point3(62, -11, 54)),
            # Set her down; gently
            base.localAvatar.posInterval(15.0, Point3(-15, 33, 1.1)),
        )
    )

    return toonFlightPaths

def generateSpeechSequence(balloon):
    # This is the interval for Slappy's phrases to say throughout the flight.
    # It shouldn't really be edited. Instead, add more phrases above with SlappySpeechX and SlappySpeechChoices.
    speechSequence = Sequence(
        Func(balloon.slappy.setChatAbsolute, SlappySpeeches[0], CFSpeech | CFTimeout),
        Wait(4),
        Func(balloon.slappy.setChatAbsolute, SlappySpeeches[1], CFSpeech | CFTimeout),
        Wait(6),
        Func(balloon.slappy.setChatAbsolute, SlappySpeeches[2], CFSpeech | CFTimeout),
        Wait(4),
        Func(balloon.slappy.setChatAbsolute, SlappySpeeches[3], CFSpeech | CFTimeout),
        Wait(6),
        Func(balloon.slappy.setChatAbsolute, SlappySpeeches[4], CFSpeech | CFTimeout),
        Wait(10),
        Func(balloon.slappy.setChatAbsolute, SlappySpeeches[5], CFSpeech | CFTimeout),
        Wait(6),
        Func(balloon.slappy.setChatAbsolute, SlappySpeeches[6], CFSpeech | CFTimeout),
        Wait(10),
        Func(balloon.slappy.setChatAbsolute, SlappySpeeches[7], CFSpeech | CFTimeout),
        Wait(6),
        Func(balloon.slappy.setChatAbsolute, SlappySpeeches[8], CFSpeech | CFTimeout),
        Wait(7),
        Func(balloon.slappy.setChatAbsolute, SlappySpeeches[9], CFSpeech | CFTimeout),
        Wait(5),
        Func(balloon.slappy.setChatAbsolute, SlappySpeeches[10], CFSpeech | CFTimeout),
        Wait(6),
        Func(balloon.slappy.setChatAbsolute, SlappySpeeches[11], CFSpeech | CFTimeout)
    )

    # Return the sequence back to the balloon to run
    return speechSequence