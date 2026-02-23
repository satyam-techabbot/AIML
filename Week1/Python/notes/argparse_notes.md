# argparse

Parser for command-line options, arguments and subcommands

- The argparse module makes it easy to write user-friendly command-line interfaces. 
- The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv. 
- The argparse module also automatically generates help and usage messages. 
- The module will also issue errors when users give the program invalid arguments.

```
import argparse
def main():
    # 1. Create the ArgumentParser object with a description
    parser = argparse.ArgumentParser(description="A simple script using argparse.")
    
    # 2. Add arguments
    # Positional arguments are required and defined without a leading '-' or '--'
    parser.add_argument("name", help="The name of the user.")
    
    # Add an optional argument (a boolean flag)
    parser.add_argument("--greet", action="store_true", help="Include a greeting.")
    
    # 3. Parse the arguments from the command line
    args = parser.parse_args()
    
    # 4. Access and use the arguments
    if args.greet:
        print(f"Hello, {args.name}!")
    else:
        print(f"{args.name}, no greeting for you.")

if __name__ == "__main__":
    main()
```

- use -- before arg to make it optional argument