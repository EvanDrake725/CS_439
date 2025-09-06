Game Documentation: Finely in: Rushtime Madness 
Game overview: When making this game I took heavy inspiration from the death and post night minigames of the Five Nights at Freddy’s franchise developed by Scott Cawthon. They usually act as small and simple minigames that usually end in a jumpscare or a crash. This mainly takes inspiration from the minigames “Give Gifts Give Life” and “Deliver Cake” with the main goal of feeding customers that get angry overtime being lifted from that with the final “game crash” being reminiscent of those games. As mentioned before the goal of this game is to deliver food to customers during rush hour before an invisible counter drops to 0. When dropping to 0 a mystery figure briefly appears and “crashes” the game.

Classes:
Imports: Pygame(obviously), SimpleGE(obvious), random(needed for customer emotions)
Finely: Finley(or Finnley I don’t actually know how to spell the name) is the player sprite class. It uses the sprites Finely_l for left movement and Finely_r for right movement. This is decided on by a variable called self.facing that will read what the last input was between left or right and will then keep that sprite active until the other direction is pressed. This means up and down just use the last pressed between left or right. Finley is a sailor shark because I asked my friends for ideas and that is what I got. Much like my cs120 project I have specific bounds for the character and thus plan on using if statements to keep it in a designated area that is shorter than the bounds of the screen. UPDATED: Forgot to mention it uses the arrow keys to move.


Shadow finley: An instance of the sprite class that takes after the player class. Will use opposite controls then finley so if you move finley up then SF moves down. So a simple x-=move speed when finley does a x+=move speed. UPDATED: Shadow Finley was left out. This mainly came down to when I added more children in a circle and couldn’t think of a way to implement him. It was a lot easier when it was in columns.


End trigger: This is another instance of the sprite class. This will appear in the middle of the screen after a certain amount of time has passed. This will take the form of a chocolate cake that if the player collides with will close the game to replicate a crash. UPDATED: The sprite got changed to that of a grey zombie at a table with a slice of chocolate cake instead. Also now runs off that invisible clock where it appears a little before it ends instead of when it ends. These were because: 1. Zombies look cooler than cake and 2. Fits more inline with those original FNaF games which this was supposed to be similar to. The name in code wasn’t updated though.


Children: Guessed it, another instance of the sprite class. What would you do without it? This will filter between two states much like the player(finley) class does. These states are mad about not getting their food or happy they have their food. To tell which state they should be in there will be a random timer for 3-8 seconds that when it goes off they change states using if statements. In this upset state if the player collides with them then they go back to being in the happy state. As if they got food when Finley stopped by. If shadow Finley collides with them then they get mad no matter the time. As mentioned this will use the simpleGE timer to make one for 3-8 seconds and will be reset whenever the player makes them happy. Will have 4 of them spawned around. Planning on maybe doing a separate class for each so they can differentiate in small ways like times. UPDATED: This class kinda got the short end. Still works mostly as intended however the sprites weren’t fully working for some reason so they got stuck with basic squares that change from green=happy or red=mad. Also got renamed to brats because that seemed funny. Also the adding to the scoring got moved to here as it just worked better. Also added more children around (like 3 extra I think) and used a list in the game class like the platformer demo to add more instead of multiple classes.


Score label: First instance of the label class. Does as the name suggests and displays player score in the top left corner. It starts with a “Score = 0” text but will get updated as the game progresses. Mostly figured out in game class.


Note there shouldn’t need to be a separate Timer class since it should all be handled in the separate classes. Will update if needed.


Main game class: This will be a scene class and first of 3 hopefully. This will use a background made in Krita probably of a restaurant to sell the feel I am going for. It is also in this class I can change the caption to the name of the game, something that will follow in all scene classes. In this scene class I will set all the different moving and important parts of my game. In the first main defined part as mentioned this is where I will set stuff like all my classes in a way that can gel well. Also here at the end of it I will decide the hierarchy that they follow. In the process part of it is where I will have the code to update and display that score. In the process  area I will also set the timers and tell them that when they go off to show the final cake using a .show() command. UPDATED: So this one mostly played the way it was supposed to. As mentioned earlier the code to update the score got moved to the “Brat” class as it worked better for some reason. Also I incorrectly said we’d set up the time in the process area even though we don’t, we do that in the original initializer. The last main change I can think of is that as mentioned I didn’t do separate classes for all the children and instead are made in a list in the initializer like on the platformer demo.


Title screen: The second of three scene classes. Technically the first but since you I will mostly testing the actual game I will make the game one first. This class will show the main title along with an image of Finley and buttons to press. The buttons needed will be one to start the game, one to see controls, and then one to quit. When it comes to coding I need to add the caption and the initializer for all the buttons, but I think that most stuff will be handled in the process part. In the process part I need a way to send the player to different screens. The slide and catch I know has that. I am pretty sure that you just do if statements that are in the main area will then display the screens. Buttons will be in the top right corners. UPDATED: I was mostly right but I left out some key stuff like the self.stop()’s that actually despawn the screens and the part of the responses needed to actually know what was clicked. Also buttons got moved.


Instruction class: This class works only to show instructions. Will just say use the arrow keys. It will also have a back button to send back to the main menu. This will work similarly to the ones on the home screen. Should be in the bottom left corner. UPDATED: now called story class and goes more indepth. Nothing to much just says that it is lunch ruch hour and you have to serve guests.


Play button: This will be a sprite class I think. Same with all buttons. I wanna customly do these so that they look nice and not the stock pygame gray. This means I will need to make and import a custom sprite that says play. Just use a similar import method to the player sprite or the children.


Instruction button: same as the play button just says instructions. UPDATED: I changed it to say story.


Quit button: same as play button just says quit.


Back button: same as play button but says back.


Main: The main cheese. I know that I use if statements to learn if they were earlier clicked and then do what is needed from there. I also know the command of game=Game() and then game.start() so I just use that on repeat but change what scene class it displays. UPDATED: Close on this one but left out the loop needed for it. This was because at the time I was looking at single screen demos like the space ship which didn’t have the loop.


Last if statement: if __name__==”__main__”: main(). It runs main.
Assets Needed: Finley sprites for right and left, customer sprites for happy and mad, special cake sprite, button sprites for (start, instructions, quit, and back), and backgrounds for (title, game, and instruction) screens All assets will be made in Krita and or Aseprite

RoadMap:
Install everything (<--important)
Get a moving character
Make it so that when character moves one way he changes sprites (start with colored squares)
Add a customer that has a “emotion” states
Add timer for emotions
Make it so color and emotion switches when timer goes off
Make it so that something happens if they collide (just print something for now)
Make clock re randomize when collision
Make colors and emotion change back when collision
Add player score when emotion changes and it prints when it happens
Add timer for end of game
Make it so when timer done the end appears (square is fine for now)
Add collision for end item that closes game *CHANGED*
Make dark finley that does opposite of inputs *CHANGED*
Make so dark finley can collide with customer *CHANGED*
Make it so that if collision happens then customer gets upset and lose point*CHANGED*
Make more classes for customers and spread them around *CHANGED*
Add actual label for score that updates as progress happens
Add title screen with main game button and quit button that work (Good to go here)
Add a screen and button for instructions and a back button on instruction screen
Make visual assets for the stuff that needs it
Turn in
Extras:
Add sound effects.
Maybe add a limit to how many you can feed at once, like you have to return to the kitchen to get food. 
Add a throwable. It would be fun. 
Maybe add a way to actually beat the game and not insta lose when you touch the cake or go on forever.


