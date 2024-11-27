class Room1:
    def __init__(self):
        self.scrabble_solved = False
        self.safe_open = False
        self.paper_found = False
        self.drawer_open = False
        self.rug_cut = False
        self.inventory = []
        self.viewable_places = ["room", "bookshelf", "symbols", "bed", "desk", "closet", "door"]
        self.state = "room"
        self.win = False
        self.books = ["The Catcher in The Rye", "Moby Dick", "Anna Karenina", "Ulysses", "Crime and Punishment", "David Copperfield",
"Call of the Wild", "The Great Gatsby", "1984", "The Hound of the Baskervilles", "A Tale of Two Cities", "The Odyssey", "Pride and Prejudice",
"Treasure Island", "The Hobbit", "The Time Traveler", "War and Peace", "The Three Musketeers", "The Odyssey", "Tom Sawyer", "The Art of War", 
"Brave New World", "The Scarlet Letter", "Frankenstein"]

    def display_intro(self):
        print("Lost deep in the mountains, in the midst of a blizzard, you and a friend stumbled upon a cabin in the woods.\n"+
        "Finding it unlocked and empty, yet furnished and with two cozy (and warm) bedrooms, you and your friend talked,\n"+
        "and figured that no one would mind if you stayed the night. You slept peacefully, but awoke to find that you\n"+
        "have been locked in your bedroom. You call to your friend, and discover that they are in the same situation.\n \n"+
        "You start to take another, suspicious look around the room. Does it look like it did last night? You can't remember. \n"+
        "Suddenly, you here the faint slide of paper as a note appears under the door.\n"+
        "It reads simply, in a heavy and intense handwriting:\n\n"+
        "YOU HAVE 30 MINUTES TO LEAVE.\n \n"+
        "You know that you and your friend are in grave danger. Can you work together to both escape your rooms, and the \n"+
        "deadly cabin, before it's too late?\n")

    def shortcuts(self):
        print("Some commands that may be helpful are as follows:\n"+
        "Type 'look' <location> or 'l' <location> to inspect a specific area of the room. Or, type 'look room' to get an\n"+
        "overview of your room.\n"+
        "Type 'open' <item> or 'o' <item> to open doors, boxes, etc. Some locked items will only open if you possess the key\n"+
        "or can provide the correct code.\n"+
        "Type 'inventory' or 'i' to view the items you are holding.\n"+
        "Type 'take' <item> or 't' <item> to put an item into your inventory.\n"+
        "Type 'use' <item> or 'u' <item> to use an item from your inventory.\n"
        "If stuck, type 'hint' and choose the puzzle you would like assistance with from the available menu.\n\n")

    def display_rules(self):
        print("Welcome to Cabin Fever. This is a game for two players. You will each be locked in a different room.\n"+
        "You cannot show each other your screens, but you will need to communicate and work together\n"+
        "if you ever hope to escape. Some of the clues in your room will apply to your friend's puzzles,\n"+
        "and you will need some of the clues from your friend's room to find the way out yourself.\n")
        self.shortcuts()

    def display_scrabble(self):
        if self.scrabble_solved:
            print("         S \n"+
            "         K     S\n"+
            "   C A B I N   T\n"+
            "         I     O\n"+
            "     W I N T E R \n"+
            "         G     M\n"+
            "               Y\n"+
            "The point values of the tiles are:\nA=1\nB=3\nC=3\nD=2\nE=1\nF=4\nG=2\nH=4\nI=1\nJ=8\nK=5\n"+
            "L=1\nM=3\nN=1\nO=1\nP=3\nQ=10\nR=1\nS=1\nT=1\nU=1\nV=4\nW=4\nX=8\nY=4\nZ=10\n\n")
            return
        print("        [] \n"+
        "         K      S\n"+
        "   C A B I N    T\n"+
        "         I      []\n"+
        "    [] I [] T E R \n"+
        "         G      M\n"+
        "                []\n")

    def display_symbols(self):
        print("\n"+
        "________          |\        |         |                \_   \n"+
        "|    \ |          | \       |  \   /  |               /  c) \n"+
        "|     \|          |  \      |    _    |              /      \n"+
        "       |       ___|___\     |   (_)   |     (________)__    \n"+
        "       |       \  |         |         |     //      \   |   \n"+
        "       |        \ |          \       /     //        \ /    \n"+
        " (((())))        \|           \_____/     //          \     \n")

    def display_paper(self):
        print("The paper has four riddles on it, as follows:\n\n"+
                "You are in a town where everybody either always tells the truth or always lies.\n"+
                "You meet two people, A and B. A says 'At least one of us is a liar'. Who tells the truth?\n"+
                "A) Only A\n"+ #correct answer
                "B) Only B\n"+
                "C) A and B\n"+
                "D) Neither A nor B\n\n"+
                "You meet two more people in this town, C and D. C says 'Both of us always lie.' Who tells the truth?\n"+
                "A) C\n"+
                "B) D\n"+ #correct answer
                "C) C and D\n"+
                "D) Neither C nor D\n\n"+
                "You meet three people, E, F, and G. You know one is a truth teller and two always lie.\nPerson A says 'I am the truth teller.'\nPerson B says 'A is a liar, I am the truth teller.'\nPerson C says 'B is a liar, I am the truth teller.'\nWho is telling the truth?\n"+
                "A) A\n"+
                "B) B\n"+ #correct answer
                "C) C\n\n"+
                "What is the correct answer to this question?\n"+
                "A) All of the below\n"+
                "B) None of the below\n"+
                "C) All of the above\n"+
                "D) One of the above\n"+
                "E) None of the above\n"+ #correct answer
                "F) None of the above\n\n")

    def display_room_1(self, location):
        match(location):
            case("room"):
                self.state = "room"
                print("ROOM 1: The room has yellowish walls and blue shag carpet. Taking up the entire left wall is a large bookshelf,\n"+
        "completely stuffed with thick, dusty books. The door leaving the room is to your right, but it is locked tight\n"+
        "and you will need a key to go through it. There is also a bed, a desk, and a closet. There are four strange symbols\n"+
        "written on the ceiling, that you did not notice the previous night in the dark (if they had been there at all).\n")
            case("closet"):
                self.viewable_places += ["coat","safe","skis"]
                if "coat" in self.inventory and "skis" in self.inventory:
                    print("The closet is empty except for a safe.\n")
                elif "coat" in self.inventory:
                    print("In the closet is a pair of skis and a safe.\n")
                elif "skis" in self.inventory:
                    print("In the closet hangs a single old-looking coat. There is also a safe on the floor.\n")
                else:
                    print("In the closet hangs a single old-looking coat. There is also a pair of skis leaning against the wall\n"+
                    "and a safe on the floor.")
                self.state = "closet"
            case("safe"):
                if "safe" in self.viewable_places:
                    if self.safe_open and "key" in self.inventory:
                        print("The safe is empty.\n")
                    elif self.safe_open:
                        print("Inside the safe is a key.\n")
                    else:
                        print("The safe is heavy and industrial. You cannot move it. It looks like it requires a 4-digit\n"+
                "numeric code to open.\n")
                    self.state = "closet"
            case("coat"|"jacket"):
                if "coat" in self.viewable_places:
                    if "note" in self.inventory:
                        print("The coat is heavy and warm.\n")
                    else:
                        print("You search the coat. There is a note in one of its pocket.\n")
                        self.viewable_places += ["note"]
                    self.state = "closet"
            case("note"):
                if "note" in self.inventory or "note" in self.viewable_places:
                    print("The note from the jacket simply says 'A=G'. That's it.\n")
                    self.state = "closet"
            case("skis"|"ski"):
                self.state = "closet"
                if "skis" in self.viewable_places:
                    print("There is nothing interesting about the skis. Except you could ski away from the cabin if and when you escape, I guess.\n")
            case("desk"|"scrabble"):
                if self.scrabble_solved:
                    print("The desk has a single drawer, and a Scrabble game on top.\n Since you added the letters 'SNOWY,' the Scrabble game looks like this:\n")
                else:
                    print("The desk has a single drawer, and a glued-down, partially-completed Scrabble game on top, except for a few missing tiles.\n Someone has helpfully marked the spaces missing tiles. The Scrabble game looks like this:\n")
                self.display_scrabble()
                self.state = "desk"
            case("bookshelf"|"books"|"shelf"|"bookcase"):
                self.state = "bookshelf"
                print("The bookshelf has a lot of books on it. Glancing at just a few of the titles, you see the following:\n")
                for b in self.books:
                    if b not in self.inventory:
                        print(b)
            case("under the desk"|"below the desk"|"under desk"|"below desk"):
                self.state = "under the desk"
                print("You inspect the area under the desk. There seems to be something under the carpet.\n")
            case("drawer"):
                self.drawer_open = True
                self.state = "desk"
                if "knife" in self.inventory:
                    print("The drawer is empty.\n")
                else:
                    print("In the drawer is a knife.\n")
            case("door"):
                self.state = "room"
                if "key" in self.inventory:
                    print("The door is locked, but you have the key. To win the game, both you and\n"+
                    "your friend must escape. When you both have your own four digit win codes,\n"+
                    "enter them as one 8 digit code with player 1's code first. Your code is 9801.\n\n")
                else:
                    print("The door is locked. Perhaps find the key?\n")
            case("A Tale of Two Cities"):
                self.state = "room"
                if ('A Tale of Two Cities' in self.inventory):
                    if self.paper_found == False:
                        print("You flip through 'A Tale of Two Cities'. Out falls a sheet of paper\n")
                        self.paper_found = True
                    else:
                        print("There is nothing else in the book.\n")
            case("paper"|"sheet"):
                self.state = "room"
                if ('paper' in self.inventory or self.paper_found):
                    self.display_paper()
            case("bed"):
                self.state = "room"
                print("The bed is uninteresting. You check, and find that there is not even anything under it.\n")
            case("symbols"|"ceiling"|"up"):
                self.state = "room"
                print("The symbols on the ceiling look like this:\n")
                self.display_symbols()
            case("tiles"):
                self.state = "under the desk"
                if "tiles" in self.viewable_places:
                    print("You found these tiles:\nA=1\nY=4\nO=1\nH=4\nQ=10\nS=1\nN=1\nE=1\nL=1\nW=4\nB=3\nI=1\n")




    def take_item(self, item):
        takeable_items = []
        match(self.state):
            case("bookshelf"):
                takeable_items = [b for b in self.books]
            case("closet"):
                takeable_items = ["skis", "coat", "note"]
                if self.safe_open:
                    takeable_items = ["key"]
            case("desk"):
                takeable_items = ["knife"]
            case("under the desk"):
                if self.rug_cut:
                    takeable_items = ["tiles"]
        if self.paper_found:
            takeable_items += ["paper"] 
        if item in self.inventory:
            print("You already have this item.\n")
            return
        if item in takeable_items:
            self.inventory += [item]
            print("You have taken "+item+"\n")
            return
        print("You cannot take that item.\n")

    def open_item(self, item):
        if item in self.books and item in self.inventory:
            if (item == "A Tale of Two Cities" and self.paper == False):
                print("You flip through 'A Tale of Two Cities'. Out falls a sheet of paper\n")
                self.paper_found = True
            else:
                print("You flip through "+item+". Nothing seems out of the ordinary.\n")
        if item == "door":
            if "key" in self.inventory:
                print("You have opened the door and can now escape. \n"+
                "To win, enter your 4-digit code and player 2's 4-digit code as one 8-digit code.\n"+
                "Your code is 9801\n\n")
            else:
                print("The door is locked.\n")
        if item == "closet":
            if "coat" in self.inventory and "skis" in self.inventory:
                print("The closet only contains a safe.\n")
            elif "coat" in self.inventory:
                print("In the closet is a pair of skis and a safe.\n")
            elif "skis" in self.inventory:
                print("In the closet hangs a single old-looking coat. There is also a safe on the floor.\n")
            else:
                print("In the closet hangs a single old-looking coat. There are also a pair of skis leaning against the wall\n"+
                "and a safe on the floor.")
            self.state = "closet"
        if item == "safe":
            self.state = "closet"
            code = input("Enter the code to the safe: ")
            if code == "5216":
                print("The safe opened. There is a key inside.\n")
                self.safe_open = True
            else:
                print("Incorrect code.\n")
        if item == "drawer":
            if "knife" in self.inventory:
                print("The drawer is empty.\n")
            else:
                print("In the drawer is a knife.\n")
            self.drawer_open = True
        if item == "carpet" and "knife" in self.inventory and self.state == "under the desk":
            print("You cut a hole in the carpet under the desk. There are the following Scrabble tiles with corresponding point values.\n"+
            "A=1\nY=4\nO=1\nH=4\nQ=10\nS=1\nN=1\nE=1\nL=1\nW=4\nB=3\nI=1\n\n") #code to lock on diary in room 2 is 'SNOWY' or 11144
            self.rug_cut = True
            self.viewable_places += ["tiles"]

    def use_item(self, item):
        if item not in self.inventory:
            print("You do not have that item.\n")
            return
        if item == "knife" and self.state == "under the desk" and self.rug_cut == False:
            print("You cut a hole in the carpet under the desk. There are the following Scrabble tiles with corresponding point values.\n"+
            "A=1\nY=4\nO=1\nH=4\nQ=10\nS=1\nN=1\nE=1\nL=1\nW=4\nB=3\nI=1\n\n") #code to lock on diary in room 2 is 'SNOWY' or 11144
            self.rug_cut = True
            self.viewable_places += ["tiles"]
        elif item in self.books:
            if (item == "A Tale of Two Cities" and self.paper_found == False):
                print("You flip through 'A Tale of Two Cities'. Out falls a sheet of paper\n")
                self.paper_found = True
            else:
                print("You flip through "+item+". Nothing seems out of the ordinary.\n")
        elif item == "tiles" and self.state == "desk":
            print("You take out the scrabble tiles you found and look at the board.")
            print("A=1\nY=4\nO=1\nH=4\nQ=10\nS=1\nN=1\nE=1\nL=1\nW=4\nB=3\nI=1\n")
            self.display_scrabble()
            word = input("What word can be made by the tiles you add?")
            if word == 'SNOWY' or word == 'snowy':
                print("That's correct!\n")
                self.scrabble_solved = True
            else:
                print("Incorrect word.\n")
        elif item == "note":
            print("The note says 'A=G'.\n")
        elif item == "paper":
            self.display_paper()
        elif item == "coat":
            print("You put on the coat.\n")
        elif item == "key":
            print("You have opened the door and can now escape. \n"+
                "To win, enter your 4-digit code and player 2's 4-digit code together as one 8-digit code.\n"+
                "Your code is 9801\n\n")
        else: 
            print("You cannot use that item here.\n\n")

    def display_inventory(self):
        print("You are holding:")
        for i in self.inventory:
            print(i)

    def display_hint(self):
        hint_number = input("For which puzzle do you need a hint?\n1. Scrabble\n2. Books\n3. Symbols\n")
        if hint_number == "1":
            print("The extra scrabble tiles are somewhere in the room. (Player 2 might be able to tell you where).\n"+
            "Figure out which tiles would fill the the gaps in the board; they will make a word.\n"+
            "Give the corresponding 5-digit numeric code to player 2.\n\n")
            return
        if hint_number == "2":
            print("Something is hidden in one of the books. Room 2 has a hint to identify the right one.\n"+
            "The item in the book should give you a four digit numeric code that player 2 needs.\n\n")
            return
        if hint_number == "3":
            print("Player 2 will need to help you decode the symbols.\n\n")
            return
        else:
            print("Invalid hint option.\n\n")


r1 = Room1()
r1.display_rules()
user_input = input("Press ENTER to continue\n")
r1.display_intro()
user_input = input("Press ENTER to start\n")
r1.display_room_1("room")

while(r1.win == False):
    user_input = input()
    if user_input == "98014543":
        print("You win! Good job!")
        r1.win = True
        break
    user_input_split = user_input.split(' ',1)
    user_input_split[0] = user_input_split[0].lower()
    if len(user_input_split)==1:
        user_input_split.append('')
    if (user_input=='shortcut' or user_input=='s' or user_input=='shortcuts' or user_input=='S' or user_input=='Shortcut' or user_input=='Shortcuts'):
        r1.shortcuts()
    elif (user_input_split[0]=='look' or user_input_split[0]=='l'):
        r1.display_room_1(user_input_split[1])
    elif (user_input_split[0]=='open' or user_input_split[0]=='o'):
        r1.open_item(user_input_split[1])
    elif (user_input_split[0]=='inventory' or user_input_split[0]=='i'):
        r1.display_inventory()
    elif (user_input_split[0]=='take' or user_input_split[0]=='t'):
        r1.take_item(user_input_split[1])
    elif (user_input_split[0]=='use' or user_input_split[0]=='u'):
        r1.use_item(user_input_split[1])
    elif (user_input_split[0]=='hint'):
        r1.display_hint()
    elif (user_input_split[0]=='cut' and 'rug' in user_input_split[1]):
        r1.use_item("knife")
    elif (user_input == "close safe" or user_input == "shut safe"):
        r1.safe_open == False
        print("Safe has been closed.\n")
    elif (user_input_split[0]=="read" and user_input_split[1] in r1.books):
        print("Unfortunately, you don't have enough time for reading novels.\n")
    else:
        print("Try something else.\n")


