class Room2:
    def __init__(self):
        self.trunk_open = False 
        self.key_found = False
        self.journal_open = False
        self.inventory = [] #hammer, journal, each figurine, key, goggles, boots, note
        self.state = "room"
        self.win = False
        self.viewable_places = ["pictures","fireplace","door","table","trunk","bed", "room"]
        self.broken = [] #the key is in the tiger figurine
        self.figurines = ["gecko", "pig", "rabbit", "bear", "snail", "crane", "giraffe", "dog", "kitten", "llama", "monkey", "fish", "snake",
        "koala", "frog", "goat", "tiger", "elephant", "penguin", "ox", "parrot", "owl", "wolf", "horse", "mouse", "dolphin",
        "zebra", "turtle", "cow", "sea lion", "crab", "weasel", "hippo","kangaroo", "sheep", "swan", "moose", "cheetah", "hippo", "alligator", "buffalo"]

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
        "deadly cabin, before it's too late?\n\n")

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

    def display_pictures(self):
        print("There are three pictures on the wall. The first is of the ocean at sunset,\n"+
        "a whale's tail rising above the water and silhouetted against the sun.\n"+
        "The second is a photo of the New York City skyline at night.\nThe third is of the Eiffel Tower in France.\n")

    def display_goggles(self): #5216 should be the code
        print("Putting on the ski goggles, you see the following symbol code scratched on the lens:\n"+
        "|         |          |\        ___________      ___________        ________                    \_               /*~      ======//|     \n"+
        "|  \   /  |          | \       __-__-__-__      \   -^-    /       |    \ |                   /  c)            (              // |      \n"+
        "|    _    |          |  \      || || || ||       \  / \  /         |     \|                  /                  \            //  |    \n"+
        "|   (_)   |       ___|___\     || || || ||        \/___\/                 |         (________)__        _        \          //   |     \n"+
        "|         |       \  |         || || || ||         \   /                  |         //      \   |        \        )        //         \n"+
        " \       /         \ |         || || || ||          \ /                   |        //        \ /          \      /      ==//|         \n"+
        "1.\_____/       2.  \|      3. || || || ||      4.   V          5. (((())))    6. //          \     7.     \____/     8.=//|        \n")

    def display_paper(self):
        print("On the paper is written: UTSKOLDEEHONRKDE\n\n")

    def display_room_2(self, location):
        match(location):
            case("room"):
                self.state = "room"
                print("ROOM 2: The room has maroon walls and dark wood floor. There are three pictures in a row on one wall.\n"+
    "There is a small, cold fireplace near the locked door. There is also a bed, a small table, and a very large, heavy, locked trunk.\n\n")
            case("fireplace"):
                if "paper" in self.inventory:
                    print("You find nothing else in the fireplace.\n")
                else:
                    print("You inspect the fireplace. It is cold and dirty and there is no wood. You find a paper in the ashes.\n\n")
                    self.viewable_places += ["paper"]
                self.state = "fireplace"
            case("pictures"|"picture"|"paintings"|"wall"|"decor"|"photos"|"photographs"):
                self.display_pictures()
                self.state = "room"
            case("table"|"figurines"|"ceramic figurines"|"figures"):
                if len(self.broken)==len(self.figurines):
                    print("The table is covered in broken pieces of ceramic. Someone made a real mess here\n")
                elif len(self.broken)>3:
                    print("The table is covered in ceramic animal figurines, some of which are broken. Left intact are:\n")
                else:
                    print("The table is covered in small, ceramic animal figurines. They are listed below:\n")
                for i in self.figurines:
                    if i not in self.inventory and i not in self.broken:
                        print(i)
                self.state = "table"
            case("trunk"):
                if self.trunk_open:
                    self.viewable_places += ["ski boots", "goggles", "hammer", "boots"]
                    in_trunk = []
                    for item in ["ski boots", "hammer", "goggles"]:
                        if item not in self.inventory:
                            in_trunk.append(item)
                    if len(in_trunk) == 0:
                        print("The trunk is empty.\n")
                    else:
                        print("The trunk contains:\n")
                        for item in in_trunk:
                            print(item)
                else:
                    print("The trunk is very large, too heavy to lift, and locked securely. The lock requires a four letter code.\n\n")
                self.state = "trunk"
            case("goggles"|"ski goggles"):
                self.state = "trunk"
                if "goggles" in self.inventory or "goggles" in self.viewable_places:
                    print("You notice a lot of little scratches on the inner surface of the goggles.\n")
            case("boots"|"ski boots"|"boot"|"ski boot"):
                self.state = "trunk"
                if "ski boots" in self.inventory or "ski boots" in self.viewable_places or "boots" in self.inventory or "boots" in self.viewable_places:
                    print("There is nothing particularly interesting about the ski boots.\n\n")
            case("hammer"):
                self.state = "trunk"
                if "hammer" in self.inventory or "hammer" in self.viewable_places:
                    print("The hammer is a nice sturdy tool, perfect for nailing things together and taking them apart.\n\n")
            case("journal"):
                self.state = "under the bed"
                if "journal" in self.inventory or "journal" in self.viewable_places:
                    if self.journal_open:
                        print("You flip through the journal. All the pages are blank except one. It says 'NCAYL'\n\n")
                    else:
                        print("The journal is locked. The lock requires a 5-digit numeric code.\n\n")            
            case("door"):
                self.state = "room"
                if "key" in self.inventory:
                    print("The door is locked, but you have the key. To win the game, both you and\n"+
                    "your friend must escape. When you both have your own four digit win codes,\n"+
                    "enter them as one 8 digit code with player 1's code first. Your code is 4543.\n\n")
                else:
                    print("The door is locked. Perhaps find the key?\n")
            case("paper"|"sheet"):#from the fireplace
                if "paper" in self.inventory or "paper" in self.viewable_places:
                    self.state = "fireplace"
                    self.display_paper()
            case("bed"):
                self.state = "under the bed"
                print("You search the bed. There is nothing interesting on it, but underneath, you notice something.\n")
            case("under the bed"|"under bed"|"below bed"|"below the bed"):
                self.state = "under the bed"
                print("There is a locked journal under the bed.\n")
                self.viewable_places += ["journal"]

    def take_item(self, item):
        if item in self.inventory or item=="boots" and "ski boots" in self.inventory or item=="ski boots" and "boots" in self.inventory:
            print("You already have this item.\n")
            return
        takeable_items = []
        match(self.state):
            case("table"):
                takeable_items = [b for b in self.figurines if b not in self.broken]
                if "tiger" in self.broken or self.key_found:
                    takeable_items += ["key"]
                print(takeable_items)
            case("trunk"):
                if self.trunk_open:
                    takeable_items = ["ski boots", "goggles", "boots", "hammer"]
            case("under the bed"):
                takeable_items = ["journal"]
            case("fireplace"):
                takeable_items = ["paper"]
        if item in takeable_items:
            self.inventory += [item]
            print("You have taken "+item+"\n")
        else:
            print("You cannot take that item.\n")

    def open_item(self, item):
        if item in self.figurines and item not in self.broken and "hammer" in self.inventory:
            self.state = "table"
            print("You use the hammer to smash the",item,"figurine.\n")
            if item == "tiger":
                print("You find a key inside.\n")
        if item == "door":
            if "key" in self.inventory:
                print("You have opened the door and can now escape. \n"+
                "To win, enter your 4-digit code and player 1's 4-digit code as one 8-digit code.\n"+
                "Your code is 4543.\n\n")
            else:
                print("The door is locked.\n")
        if item == "trunk":
            if self.trunk_open == False:
                code = input("Enter the 4-letter code to unlock the trunk:\n")
                if code == "ABBE" or code == "abbe " or code == "ABBE " or code == "abbe":
                    print("The trunk opens. Inside, you see a pair of ski boots, goggles, and a hammer.\n")
                    self.trunk_open = True
                    self.viewable_places += ["goggles", "ski boots", "hammer"]
                else:
                    print("Incorrect code.\n")
            else: 
                print("The trunk is already open.\n")
            self.state = "trunk"
        if item == "journal":
            if self.journal_open:
                print("You flip through the journal. All the pages are blank except one. It says 'NCAYL'\n")
            else:
                code = input("Enter the 5-digit code to the lock on the journal: ")
                if code == "11144":
                    print("The journal opened. You flip through. All the pages are blank except one. It says 'NCAYL'\n")
                    self.journal_open = True
                else:
                    print("Incorrect code.\n")


    def use_item(self, item):
        if item not in self.inventory:
            print("You do not have that item.\n")
            return
        if item == "goggles" or item == "ski goggles":
            self.display_goggles()
        elif item == "hammer":
            b = input("You use the hammer to break one of the figurines. Which would you like to smash first?\n")
            if b in self.figurines and b not in self.broken:
                self.broken += [b]
                print("You break the",b,"\n")
                if b == "tiger":
                    print("You find a key inside\n")
            else:
                print("Invalid option.\n")
        elif item == "boots" or item == "ski boots":
            print("You put on the ski boots.\n")
        elif item == "journal" or item == "diary":
            if self.journal_open:
                print("You flip through the journal. All the pages are blank except one. It says 'NCAYL'\n")
            else:
                code = input("Enter the 5-digit code to the lock on the journal: ")
                if code == "11144":
                    print("The journal opened. You flip through. All the pages are blank except one. It says 'NCAYL'\n")
                    self.journal_open = True
                else:
                    print("Incorrect code.\n")
        elif item == "paper" or item == "note":
            self.display_paper()
        elif item == "key":
            print("You have opened the door and can now escape. \n"+
                "To win, enter player 1's 4-digit win code and your 4-digit code together as one 8-digit code.\n"+
                "Your code is 4543.\n\n")
        else: 
            print("you cannot use that item here.\n\n")

    def display_inventory(self):
        print("You are holding:\n")
        for i in self.inventory:
            print(i)

    def display_hint(self):
        hint_number = input("For which puzzle do you need a hint?\n1. Pictures\n2. Journal\n 3. Trunk")
        if hint_number == "1":
            print("Player 1 needs to now about the pictures.\n\n")
            return
        if hint_number == "2":
            print("Player 1 will be able to give you the 5-digit code to open the journal, at some point\n"+
            "Player 1 also has the information to decode the contents of the journal.\n\n")
            return
        if hint_number == "3":
            print("Player 1 will find a paper that will lead you to the four letter code to open the trunk's lock\n"+
            "Two of the items in the trunk will need to be used to win the game.\n\n")
            return
        else:
            print("Invalid hint option.\n\n")


r = Room2()
r.display_rules()
user_input = input("Press ENTER to continue\n")
r.display_intro()
user_input = input("Press ENTER to start\n")
r.display_room_2("room")

while(r.win == False):
    user_input = input()
    if user_input == "98014543":
        print("You win! Good job!")
        r.win == True
        break
    user_input_split = user_input.split(' ',1)
    if len(user_input_split)==1:
        user_input_split.append('')
    if (user_input == 's' or user_input == 'S' or user_input == 'Shortcut' or user_input == 'shortcut'or user_input == 'Shortcuts' or user_input == 'shortcuts'):
        r.shortcuts()
    elif (user_input_split[0]=='look' or user_input_split[0]=='l' or user_input_split[0]=='Look' or user_input_split[0]=='L'):
        r.display_room_2(user_input_split[1])
    elif (user_input_split[0]=='open' or user_input_split[0]=='o' or user_input_split[0]=='Open' or user_input_split[0]=='O'):
        r.open_item(user_input_split[1])
    elif (user_input_split[0]=='inventory' or user_input_split[0]=='i' or user_input_split[0]=='I' or user_input_split[0]=='Inventory'):
        r.display_inventory()
    elif (user_input_split[0]=='take' or user_input_split[0]=='t' or user_input_split[0]=='Take' or user_input_split[0]=='T'):
        print(user_input_split[1])
        r.take_item(user_input_split[1])
    elif (user_input_split[0]=='hint' or user_input_split[0]=='Hint' or user_input_split[0]=='hints'):
        r.display_hint()
    elif ((user_input_split[0]=='wear' or (user_input_split[0]=='put' and 'on' in user_input_split[1]) and 'goggles' in user_input_split[1])):
        r.use_item("goggles")
    elif (user_input_split[0]=='break' or user_input_split[0]=='smash' or user_input_split[0]=='destroy' or "use hammer" in user_input):
        toBreak = []
        for i in r.figurines:
            if i not in r.broken:
                if i in user_input_split[1]:
                    toBreak += [i]
        if len(toBreak)==1:
            print("You break the",toBreak[0])
            r.broken += toBreak[0]
            r.state = "table"
            if toBreak[0] == "tiger":
                r.key_found = True
                print("You find a key inside\n")
        elif ("figurines" in user_input_split[1] or "figures" in user_input_split[1] or "statues" in user_input_split[1] or "ceramic" in user_input_split[1] or "ceramic figurines" in user_input_split[1]or len(toBreak)>1):
            b = input("You use the hammer to break one of the figurines. Which would you like to smash first?\n")
            if b in r.figurines and b not in r.broken:
                r.broken += [b]
                print("You break the",b)
                r.state = "table"
                if b == "tiger":
                    print("You find a key inside\n")
            else:
                print("Invalid option.\n")
        else:
            print("You cannot break that item.\n")  
        r.state = "table"
    elif (user_input == "close trunk" or user_input == "shut trunk" or user_input == "close the trunk" or user_input == "shut the trunk"):
        r.trunk_open = False
        print("Trunk has been closed.\n")
    elif (user_input_split[0]=='use' or user_input_split[0]=='u'):
        r.use_item(user_input_split[1])
    else:
        print("Try something else.\n")




