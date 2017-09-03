
def get_amount():
    """
    Function to get amount of mails to sent
    """
    while True:
        num = int(input("How many mails do you'd like to sent to your victim?: "))
        if 0 < num < 2001:
            return num
        print("You've entered wrong amount of entries.")

