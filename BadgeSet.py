import PIL as pil

'''
The BadgeSet class holds a list of Badges which are available to the user.
Each BadgeSet has a list containing all the Badge objects.
'''
class BadgeSet:
    def __init__(self, badgeList):
        badgeList = [Badge(pil.Image.open(Badges/bmedal1.png), "Starting out", "set a goal", False),
                     Badge(pil.Image.open(Badges/bmedal2.png), "Friends!", "make a friend", False),
                     Badge(pil.Image.open(Badges/bmedal3.png), "Together We Start", "create a shared goal with your friends", False),
                     Badge(pil.Image.open(Badges/bmedal4.png), "More Goals", "set 10 goals", False),
                     Badge(pil.Image.open(Badges/bmedal5.png), "Reaching the Finish Line", "finish a goal", False),
                     Badge(pil.Image.open(Badges/bmedal6.png), "Marathon", "finish a goal that took longer than 26 hours", False),
                     Badge(pil.Image.open(Badges/bmedal7.png), "Friend Circle!", "make 5 friends", False),
                     Badge(pil.Image.open(Badges/bmedal8.png), "Sweet Victory", "win a competition", False),
                     Badge(pil.Image.open(Badges/bmedal9.png), "Room for Improvement", "lose a competition", False),
                     Badge(pil.Image.open(Badges/bmedal10.png), "Tournament Player", "participate in 10 competitions", False),
                     Badge(pil.Image.open(Badges/dmedal1.png), "Tough Luck", "lose 200 competitions", False),
                     Badge(pil.Image.open(Badges/dmedal2.png), "Finishing V", "finish 500 goals", False),
                     Badge(pil.Image.open(Badges/dmedal3.png), "Overpowered", "win 1000 competitions", False),
                     Badge(pil.Image.open(Badges/gmedal1.png), "Share the Wealth", "win 25 competitions with friends", False),
                     Badge(pil.Image.open(Badges/gmedal2.png), "Smart Setter", "set 100 goals", False),
                     Badge(pil.Image.open(Badges/gmedal3.png), "Finishing IV", "finish 100 goals", False),
                     Badge(pil.Image.open(Badges/gmedal4.png), "God Mode", "win 100 competitions", False),
                     Badge(pil.Image.open(Badges/gmedal5.png), "Insane Person", "place top 10 in daily goals challenge", False),
                     Badge(pil.Image.open(Badges/smedal1.png), "Finishing II", "set 10 goals", False),
                     Badge(pil.Image.open(Badges/smedal2.png), "Productive Person", "set 50 goals", False),
                     Badge(pil.Image.open(Badges/smedal3.png), "Marathon II", "finish a goal that took a month", False),
                     Badge(pil.Image.open(Badges/smedal4.png), "Popular Person", "make 20 friends", False),
                     Badge(pil.Image.open(Badges/smedal5.png), "Victorious", "win 20 competitions", False),
                     Badge(pil.Image.open(Badges/smedal6.png), "Hard Loser", "lose 10 competitions", False),
                     Badge(pil.Image.open(Badges/smedal7.png), "Finishing III", "finish 50 goals", False),
                     Badge(pil.Image.open(Badges/smedal8.png), "Synergy", "win 5 competitions with friends", False)]