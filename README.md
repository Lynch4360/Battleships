<h1 align="center">Battleships</h1>

[View the live project here](https://battleships-ms3.herokuapp.com/)

Battleships is a command line app based on the game that has roots going back to 1931. Where two players place ships on a game board and take turns trying to find and sink their opponent's fleet.

The current state of the game has no GUI and is terminal only. It is played against an AI only, and does not offer two player in this current state.

## Index - Table of Contents
* [User Experience (UX)](#user-experience-ux) 
* [Features](#features)
* [Design](#design)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## User Experience (UX)

### User stories - As a user I want to be able to:
    1. Read clear instructions on what the game is and how to play it.

    2. See my game board and the opponent's game board at the same time.
    Just like the traitional battleships board game.

    3. Tell if a shot that has been entered by user has been entered before.

    4. See how many moves I won the game in.

    5. See how many moves I lost the game against the computer in.

    6. Play the game again after I am finished.

## Features

### Existing Features
  F1 [Instructions](assets/readme/images/instruction.jpg)

  F2 [Game Board](assets/readme/images/gameBoard.jpg.png)

  F3 [Repeated shot detection](assets/readme/images/repeatShotDetection.jpg)

  F4 [Victory message](assets/readme/images/winCondition.jpg.png)

  F5 [Defeat message](assets/readme/images/defeat.jpg.png)

  F6 [Run Program again button](assets/readme/images/runButtonAgain.jpg.png)
  
### How these features support User Stories

- The user stories above are number 1-6 and the existing features are listed F1-F6. These are directly linked to eachother and F1 corresponds with Number 1 in the user stories section.

### Features which could be implemented in the future

- __Appropriate UI__

This application uses the command line interface it is not very user friendly. An obvious future feature of this application would be to build a better user-interface layer using HTML/CSS and possibly JavaScript to make it much more intuitive to use. A Python GUI could also be another viable option.

- __Controlled Instructions__

The instructions begin playing when program is opened, ideally this could take input from the user to play the instructions if they feel they need to read them and then they could repeat them if they needed a refresher.

- __Exit and Restart buttons__

There is no exit or restart button in the game. On Heroku there is a run program button built in. In this version of the game this is the only way to restart. A future feature could be to add both these buttons to the command line process.

- __Player vs, Player__

As this had a deadline for submission the amount of features that were able to be implemented were limited, the only way you can play the game is vs. AI. Perhaps making a code that you can send to a friend that would allow you to play against eachother would be a future feature this would most likely be done using Websockets.
You can find More about WebSockets [here](https://en.wikipedia.org/wiki/WebSocket)

- __Smarter AI__

The route taken in this application concerning the computers moves is an AI that hunts for a ship once it gets a hit. Quite a simple bot. A future feature that could be implemented would be an AI that works from a heat map of the board showing the most accurate guess. This would make the AI finish in about 20 less moves according to some resources online. A video that I recommend for anyone interested in this concept is [here](https://www.youtube.com/watch?v=tgcwSkKWJ9E)

- __Leaderboard__

Another future feature that given more time could have been implemented in this version would be a leaderboard system that prints how many moves it took you to win and stores it in Google sheets using an API.

## Design

### Flow charts
The diagrams below outline the high level flow of control within the application:
This is the published flowchart

  [Main Game Flowchart](https://lucid.app/publicSegments/view/a7c401ff-150b-4823-8fd1-355c72700131/image.jpeg)

If the puplished link does not work, you can find the image of it [here](assets/readme/images/flowchart.jpg.png)

## Technologies Used

### Languages Used
 
-   [Markdown](https://en.wikipedia.org/wiki/Markdown)
-   [Python 3.8.10](https://www.python.org/)

### Frameworks & Programs Used

-   [Git:](https://git-scm.com/) was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
-   [GitHub:](https://github.com/) is used as the respository for the projects code after being pushed from Git.
-   [Heroku:](https://heroku.com) is used to deploy the application and provides an enviroment in which the code can execute
-   [Lucid Chart](https://lucid.app/documents#/dashboard) was used to create the flow chart for this app.

## Testing

Testing information can be found i seperate [TESTING.md](TESTING.md) file

### Known Bugs

- Problem with print statements not showing up before input in Heroku App


This  worked fine when testing within the Gitpod enviroment, but did not work when the application was deployed to Heroku. No error messages or warnings were displayed when the application was run on the Heroku platform, to patch up this problem and make it less debilitating for the user experience. I placed an empty print statement before the input.
This did not fix it entirely but the app is still usable.

The reference to this code is: [Print statement Fix](assets/readme/images/printScreenFix.jpg.png)

## Deployment

To deploy this page to GitHub Pages from its [GitHub repository](https://github.com/Lynch4360/Battleships), the following steps were taken: 
1. Log into GitHub. 
2. From the list of repositories on the screen, select **Lynch4360/Battleships**.
3. From the menu items near the top of the page, select **Settings**.
4. Scroll down to the **GitHub Pages** section.
5. Under **Source** click the drop-down menu labelled **None** and select **Main Branch**
6. On selecting Main Branch the page is automatically refreshed, the website is now deployed. 
7. Scroll back down to the **GitHub Pages** section to retrieve the link to the deployed website. 

### How to run this project locally

<details>
<summary>Steps to follow to run this locally</summary>

To clone this project into Gitpod you will need:
1. A Github account. [Create a Github account here](https://github.com/)
2. Use the Chrome browser 

Then follow these steps:
1. Install the [Gitpod Browser Extensions for Chrome](https://www.gitpod.io/docs/browser-extension/)
2. After installation, restart the browser
3. Log into [Gitpod](https://www.gitpod.io/) with your gitpod account.
4. Navigate to the [Project GitHub repository](https://github.com/Lynch4360/Battleships)
5. Click the green "Gitpod" button in the top right corner of the respository
6. This will trigger a new gitpod workspace to be created from the code in Github where you can work locally.

To work on the project code within a local IDE such as Jetbrains, VScode, Pycharm etc:
1. Follow this link to the [Project GitHub repository](https://github.com/Lynch4360/Battleships).
2. Under the repository name, click "Clone or download".
3. In the Clone with HTTPs section, copy the clone URL for the repository. 
4. In your local IDE open the terminal.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type ```git clone```, and then paste the URL you copied in Step 3.
```console
git clone https://github.com/USERNAME/REPOSITORY
```
7. Press Enter. Your local clone will be created.

Further reading and troubleshooting on cloning a repository from GitHub [here](https://help.github.com/en/articles/cloning-a-repository).

</details>

### How this site was deployed to Heroku 
   
  <details>
    <summary>Steps followed to deploy</summary>

- Log in to [Heroku](https://heroku.com/), create an account if necessary.
  - From the Heroku dashboard, click the 'Create new app' button. For a new account an icon will be visible on screen to allow you to Create an app, otherwise a link to this function is located under the New dropdown menu at the top right of the screen.
  - On the Create New App page, enter a unique name for the application and select region. Then click Create app.
  - You will then be brought to the Application Configuration page for your new app. Changes are needed here on the Settings and Deploy tabs.
  - Next, scroll down the Settings page to Buildpacks.  Click 'Add buildpack', select Python from the pop up window and click on 'Save changes'. Click Add buildpack again, select Node.js from the pop up window and click on 'Save changes'. It is important that the buildpacks are listed Python first, then Node.js beneath.
  - Click on the 'Deploy tab' on the Application Configuration page.
  - Select GitHub as the Deployment Method and if prompted, confirm that you want to connect to GitHub.  Enter the name of the github
repository (the one used for this project is https://github.com/Lynch4360/Battleships) and click on 'Connect' to link up the Heroku app to the GitHub repository code.
  - Scroll down the page and choose to either Automatically Deploy each time changes are pushed to GitHub, or Manually deploy - for this project
Automatic Deploy was selected.
  - The application can be run from the Application Configuration page by clicking on the Open App button.
  - The live link for this project is (https://battleships-ms3.herokuapp.com/)

 </details>

 ## Credits
  Inspiration has been taken from exterior sources in the creating of this app.

  CS Students YouTube channel has been a very informative source and has influenced this project's inception drastically you can find the Video [here](https://www.youtube.com/watch?v=MgJBgnsDcF0)

  Some Concepts spoken about in this video even though written in JavaScript have been used in this project. For that, many thanks to Ania Kubów and her video on Battleships found [here](https://www.youtube.com/watch?v=U64vIhh0TyM&t=12s)


 ### Code
  As stated above there has been information taken from some sources for the project but in all the code was written by the developer. One piece that has been used from a Stack Overflow Post is [here](assets/stackOverflowFunc.jpg.png)



 ### Acknowledgements

 - Thank you to my mentor Brian Macharia, for his help and feedback throughout this project. He has given me countless tips and multiple resources to help me improve my coding and my testing. Thanks also to my tutor Miguel Martinez for the facillitator sessions and classes on Python and Object Orientated Programming.