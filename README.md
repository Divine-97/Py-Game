# Adventure Game

Adventure game is a text based game using Python. The game is just about different scenarios and is very easy to play. The player has to answer the questions provied in order to advance to the next scenario making sure to input valid answers in order to win the game. 

Check out the live project [here](https://adventure-game-py.herokuapp.com/).
![Image 15-08-2021 at 11 16](https://user-images.githubusercontent.com/81257331/129475101-437fbfcf-11b0-47e9-baa4-05e7a505f6ee.jpg)

## How to play

Adventure game is based on choices made by the player. To play the game the player is presented with different prompts, each prompt results to a different outcome. The player needs to select a choice that will advance to the next scenario by making sure they enter valid data in order to win the game. The player has to make sure to answer the answer thinking deep as to what the outcome will be. If the player mistakenly inputs invalid data, the player will be asked to try again. First, we are giving some messages to the player to describe the current situation. Then we take the player's choice as an input. 


### Features
 Existing features
 * Introduction to the game
 
    The player can see the first prompts of the game
  
 ![Image 16-08-2021 at 16 15](https://user-images.githubusercontent.com/81257331/129587155-ad34fdf0-033c-4fd8-96c2-215175a9a915.jpg)
 
  * Accepts users input
  * Brings the user to a different scenario after answering the first one
   

![Image 16-08-2021 at 16 25](https://user-images.githubusercontent.com/81257331/129588779-54764694-019d-40af-ab9f-bab8db05a8aa.jpg)

* Input validation and error checking
   * You must enter the numbers 1/2 on some questions or letters l/r.
   * If you enter invalid data the game ends and your asked to try again.

![Image 16-08-2021 at 16 35](https://user-images.githubusercontent.com/81257331/129590192-85b5e0fd-47c6-4b7f-b9e7-a9667a608f5a.jpg)

## Data Model

Before starting my code I looked up a lot of text based adventure games on google and youtube just to grasp some ideas. Then I decided what i wanted to include in my own game. The final adventure game was as per below:

![Image 17-08-2021 at 22 39](https://user-images.githubusercontent.com/81257331/129804207-deec3a85-59cb-44a0-bf10-90eb69b6c591.jpg)


The different rooms have been created using functions, to connect them they call each other depending on what the player's answer is. It's pretty self-explanatory. First, we are giving some messages to the player to describe the current situation. Then we take the player's choice as input, then we check if the player typed "1" or "2" or anything else.If the player typed "1", then the game is over. Else if the player typed "2", lead them to the diamond_room().Else, call the game_over function if the player inputs invalid data. The same goes on with all other scenarios till the player either wins or loses the game.

 
## Testing

I have manually tested the code by doing the following:
* Passed the code through PEP8 and confirmed there are no problems.
* Tested in my local terminal and Code Institute Heroku terminal.
* The game gives an input of invalid data if the player inputs invalid data.


 Bugs
  
   Solved bugs
   * When testing my code using PEP8 I was getting identation errors (identation is not a multilple of four) which i corrected.
 
   Remaining bugs
   * No remaining bugs


 ## Deployment
 How to deploy the project

 Hosted on github pages

 Steps for deployment:

  * Fork or clone this repository.
  * Create a new Heroku app.
  * Set the buildpacks to Python and NodeJS in that order.
  * Link the Heroku app to the repository.
  * Click on Deploy.
 
  
## Validator Testing 
 * PEP8
  No errors were returned from PEP8online.com
  
  ## Credits
   * I had a better understanding of how to create a text based game by watching this youtube [video](https://www.youtube.com/watch?v=DEcFCn2ubSg).
   * I also used this [page](https://thecodingpie.com/post/make-your-own-text-based-adventure-game-in-python3) to learn how to build this game.
   * Code Institute for the deployment terminal.
   * I would like to thank Tutor support for the assistance and also my Mentor.
  
  
  
