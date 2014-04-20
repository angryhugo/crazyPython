def using_control():
    answer = raw_input("Type a number greater than 1 and hit 'Enter'.") # raw_input() accepts a string, input() accepts a number only
    if len(answer) > 0:
        try:
            answer=int(answer)
            if answer > 1:
                return "You are right!"
            elif answer == 1:
                return "1 is not greater than it self!"
            else:
                return "Sorry! You are wrong!"
        except:
            return "'"+answer+"' is not a number!"
    else:
        return "You did not type anything!"

print using_control()