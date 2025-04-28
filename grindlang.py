def run_grindlang_code(filename):
    variables = {}  # Store variables and their values
    in_grind_mode = False  # Flag for Grind mode (interactive loop)

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()  # Read the program file

        i = 0
        while i < len(lines):
            line = lines[i].strip()  # Clean up the line

            if not line or line.startswith('#'):  # Skip empty lines or comments
                i += 1
                continue

            parts = line.split()  # Split the line into command and arguments
            command = parts[0]  # First part is the command

            # 'say' command prints a message or variable's value
            if command == 'say':
                content = ' '.join(parts[1:])
                if content in variables:
                    print(variables[content])  # Print the stored value
                else:
                    print(content)  # Print the literal content

            # 'quest' command prompts user for input and stores it in a variable
            elif command == 'quest':
                varname = parts[1]
                user_input = input(f"Enter a value for {varname}: ")
                variables[varname] = user_input  # Store the input value in the variable

            # 'equip' command assigns a value or variable to another variable
            elif command == 'equip':
                varname = parts[1]
                value = ' '.join(parts[3:])
                if value in variables:
                    variables[varname] = variables[value]  # Copy the value from another variable
                else:
                    variables[varname] = value  # Directly assign the value

            # 'spawn' command initializes a variable to 0
            elif command == 'spawn':
                varname = parts[1]
                variables[varname] = 0  # Initialize the variable to 0

            # 'forge' command changes the data type of a variable
            elif command == 'forge':
                varname = parts[1]
                typecast = parts[2]
                if typecast == 'int':
                    variables[varname] = int(variables[varname])  # Convert to integer
                elif typecast == 'str':
                    variables[varname] = str(variables[varname])  # Convert to string

            # 'chant' command performs string operations, e.g., reversing a string
            elif command == 'chant':
                func = parts[1]
                varname = parts[2]
                if func == 'reverse':
                    variables[varname] = variables[varname][::-1]  # Reverse the string

            # 'loot' command evaluates and assigns expressions to variables
            elif command == 'loot':
                varname = parts[1]
                expr = ' '.join(parts[3:])
                expr = expr.replace(varname, f"variables['{varname}']")  # Replace variable name
                for var in variables:  # Replace other variables in the expression
                    expr = expr.replace(var, f"variables['{var}']")
                variables[varname] = eval(expr)  # Evaluate and store the result

            # 'repeat' command repeats a character a specified number of times
            elif command == 'repeat':
                if 'character' in variables and 'times' in variables:
                    character = variables['character']
                    times = int(variables['times'])
                    for _ in range(times):
                        print(character)  # Print the character 'times' number of times
                else:
                    print("Error: character or times variable missing")

            # 'cat' command processes text input in different modes
            elif command == 'cat':
                cat_mode = variables['cat_mode']
                user_input = input("Enter text: ")

                if cat_mode == '1':  # Normal mode
                    print(user_input)
                elif cat_mode == '2':  # Reverse characters mode
                    print(user_input[::-1])
                elif cat_mode == '3':  # Reverse lines mode
                    reversed_lines = '\n'.join(user_input.splitlines()[::-1])
                    print(reversed_lines)
                elif cat_mode == '4':  # Reverse both characters and lines
                    reversed_lines = '\n'.join(user_input.splitlines()[::-1])
                    print('\n'.join([line[::-1] for line in reversed_lines.splitlines()]))

            # 'grind' command starts an interactive loop for repetitive actions
            elif command == 'grind':
                in_grind_mode = True
                grind_block = []
                i += 1
                while i < len(lines):
                    grind_line = lines[i].strip()
                    if grind_line == 'rest':  # Exit grind loop when 'rest' is encountered
                        break
                    grind_block.append(grind_line)
                    i += 1
                while True:
                    for grind_command in grind_block:
                        sub_parts = grind_command.split()
                        sub_command = sub_parts[0]

                        # Nested 'say', 'quest', and 'chant' within grind mode
                        if sub_command == 'say':
                            content = ' '.join(sub_parts[1:])
                            if content in variables:
                                print(variables[content])
                            else:
                                print(content)

                        elif sub_command == 'quest':
                            varname = sub_parts[1]
                            user_input = input(f"Enter a value for {varname}: ")
                            variables[varname] = user_input

                        elif sub_command == 'chant':
                            func = sub_parts[1]
                            varname = sub_parts[2]
                            if func == 'reverse':
                                variables[varname] = variables[varname][::-1]
                    print('(type "exit" to quit grind loop)')
                    user_exit = input()
                    if user_exit.lower() == 'exit':  # Break the grind loop
                        break

            # 'afk' command exits the program with a custom message
            elif command == 'afk':
                print("Going afk. See ya!")
                break

            else:
                print(f"Unknown command: {line}")  # Handle unknown commands

            i += 1  # Move to the next line

    except Exception as e:
        print(f"Error: {e}")  # Print error message if any exception occurs

if __name__ == "__main__":
    filename = input("Enter the GrindLang program filename: ")  # Prompt for file name
    run_grindlang_code(filename)  # Run the code with the specified file
