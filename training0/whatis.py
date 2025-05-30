import sys

def main():
    """Determine if the provided integer argument is even or odd and print the result."""
    args = sys.argv[1:]
    # No argument: exit quietly
    if len(args) == 0:
        return
    # More than one argument: error
    if len(args) > 1:
        print("AssertionError: more than one argument is provided")
        return
    arg = args[0]
    # Argument must be an integer
    try:
        n = int(arg)
    except ValueError:
        print("AssertionError: argument is not an integer")
        return
    # Check even or odd
    if n % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__ == "__main__":
    main()
