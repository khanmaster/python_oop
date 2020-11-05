# using __name__ and __main__

print(" this is mod_1 name -->" + __name__)

def main():
    return " from mode 1 function"
    #pass # key word pass helps you by pass without an error

# Syntax if __name__ == "__main__":
if __name__ == '__main__':# it checks the whether the code is run from current file
   main()