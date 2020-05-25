# demonstrate template string functions
from string import Template

# def main():
    # # Usual string formatting with format()
    # str1 = "You're watching {0} by {1}".format("Advanced Python", "Joe Marini")
    # print(str1)
    
    # # TODO: create a template with placeholders
def main():
    Yunting = Template("Yunting is a ${mood} ${sex}")
    # TODO: use the substitute method with keyword arguments
    Yuntingchiu = Yunting.substitute(mood = "bad", sex = "boy")
    # TODO: use the substitute method with a dictionary
    print(Yuntingchiu)



    
if __name__ == "__main__":
    main()
    