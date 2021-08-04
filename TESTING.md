# Battleships - Testing details

[Main README.md file](README.md)

[View Github Repository](https://github.com/Lynch4360/Battleships)

## Testing

### Validation Testing

- [PEP8 Online Validator](http://pep8online.com/)

- All code was run through the validator and no issues arose.

### Testing Table
| Test Label      | Test Action    | Expected Outcome    | Test Outcome     |
| :-------------- | :------------: | ------------------: | ---------------: |
|Run<br> Program|Click Run <br>Program|The program <br>restarts and<br> continues with <br>instructions|PASS|
|Enter coordinate<br> that is off<br> the grid| Enter 110<br>as coordinate|An error occurs<br>asking for user<br>to repeat<br>their input|PASS|
|Repeat Guess|Type in the <br>same guess<br>twice|An error<br>occurs saying<br>that you already<br>attempted<br>this guess|PASS|
|Run Out of<br> Bullets|Disable AI<br>Fill out over<br>80 coordinate<br>on game grid|Game Ends|PASS|
|AI win condition|Lose against AI|Game prints<br>that AI<br>won game in<br>x moves|PASS|
|User win condition|Beat the AI|Game prints<br>that user<br>won game in<br>x moves|PASS|

### User stories Testing

- User stories testing has been lined out in the [README.md](README.md) file.

- The features directly answer the user stories and all were completed and testing was met.

## Further Testing

1. Fellow students in the Code Institute Slack channel were asked to review the code and no issues were found.

2. I have ran through the app myself multiple times and no futher issues were found that have not been outlined.

3. Debugging and testing was done frequently during the creating of this app.