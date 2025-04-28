
# Grindlang 

GrindLang is a very simply, gaming themed, interactive interpreted programming language designed for educational purposes. It allows users to experiment with basic programming concepts such as variables, loops, user input, and string manipulation through a series of predefined commands. The language supports interactive features like prompting the user for input, performing mathematical operations, reversing strings, and more. The GrindLang interpreter processes commands defined in text-based program files and executes them in a straightforward manner, making it ideal for learning the fundamentals of programming.



## Installation/Instructions

Since the primary people that may try this are students, I will assume all of you have a IDE of your choice to run this.
The interpreter is python, download all the files and import them into your IDE (I used visual studio code), then open a terminal in VS code and navigate to where the interpreter is saved in your file system (i.e. c:\user\codebase\grindlang) and type. 
"python grindlang.py"   You will then be prompted to specify which of the 5 programs you want to run. i.e. helloworld.txt, multiply.txt. Simply specific which one, and follow along in the terminal if it asks for user input. 


## Authors

- [@WheatiesJN](https://www.github.com/WheatiesJN)


## Features

* User input handling : Allows users to input values during runtime using the quest command, storing them in variables for further use.
* Variable Assignment and Manipulation : Supports variable creation and assignment with commands like equip and spawn, enabling flexible data management within the programs.
* String Manipulation: Provides built-in functions like chant to modify strings, such as reversing them, through simple commands.
* Basic Arithmetic Operations: Uses the loot command to evaluate and store the result of arithmetic expressions, allowing basic math operations between variables.
* Loops and Repetition : The repeat command enables users to repeat actions or outputs multiple times, controlled by user input.
* Conditionally Reversed Output: The cat program supports 4 different modes for string outputs. 1 (normal) 2 (Reversed) 3 (Reversed lines) 4 (both reversals)
* Grind Mode (Interactive Loops): The grind command activates an interactive mode where the program executes a series of commands repeatedly until the user chooses to exit.
* Data Type Conversion: The forge command allows typecasting variables between int and str to perform operations based on the correct data type.

## List of keywords/operators

Command | Description
* spawn varname | Creates a new variable named varname and sets it to an empty string (""). Think of it like getting an empty inventory slot ready.
* equip varname = value | Assigns a value to an existing variable. If the value is a number or another variable, it's stored directly.
* quest varname | Prompts the user to enter input during the program's run, and stores that input into the specified variable.
* say value_or_varname | Prints a string literal or the contents of a variable to the terminal. Used for displaying messages to the player.
* loot varname = value1 + value2 | Performs basic addition between two numbers or variables. The result is stored into varname.
* chant reverse varname | Takes a string stored in varname and reverses its characters. Good for puzzles or simple transformations.
* repeat varname value_to_repeat | Repeats a printed value a number of times based on the integer stored in varname. Think of it like a simple for-loop.
* grind | Enters "grind mode," an interactive loop where a block of commands is repeated until the user types exit. Useful for continuous action.
* forge varname = type | Converts the data type of a variable to either int or str. Example: forge score = int turns score into an integer for math.
* cat mode | Special command for controlling how text is output. Modes:  1 = normal,  2 = reversed characters,  3 = reversed lines,  4 = both reversed characters and lines.

## Example Program | reversestring.txt

quest userinput  

chant reverse userinput  

say userinput

quest message:  
Prompts the user to type a message. Saves it into the variable message.

chant reverse message:  
Takes the message variable and reverses its string contents.

say message:  
Prints the reversed message back to the user.
