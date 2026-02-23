# print("hello")

# from typing import Self, reveal_type

# class Foo:
#     def return_self(self) -> Self:
#         return self

# class SubclassOfFoo(Foo): pass

# reveal_type(Foo().return_self()) 
# reveal_type(SubclassOfFoo().return_self())  

# import logging
# logging.basicConfig(level=0)
# # logging.basicConfig(level=logging.DEBUG)

# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")

# import logging
# # logging.basicConfig(format="%(levelname)s: %(name)s:%(message)s")
# logging.basicConfig(
#     format="{asctime} - {levelname} - {message}",
#     style="{",
#     datefmt="%Y-%m-%d %H:%M",
# )
# logging.error("Hello, Warning!")

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
