def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1: 
        name = "mbox-short.txt"
    handle = open(name)
    dict = {}
    for line in handle:
        if line.startswith("From:"):
            rhand = line.rstrip()
            list = rhand.split()
            email = list[1]
            dict[email] = dict.get(email, 0) + 1
    
    largest_num = -1
    largest_word = None
    for k,v in dict.items():
        if v > largest_num:
            largest_num = v
            largest_word = k
    print(largest_word, largest_num)

    #print(dict.items())

            #hand_list = rhand.split
            #print(hand_list)
            #email = hand_list[1]
            #print(email)
    
    


## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
