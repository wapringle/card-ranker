import pytest
import dragdrop
from dragdrop2 import assignedSlots

@pytest.fixture
def clean():
    global assignedSlots
    assignedSlots=[]
    

def test_eng(clean):
    import airpollution

    global assignedSlots
    assignedSlots=[]

    order=list(range(8))
    
    deck=[
        { "name": "Beijing, China", "front": "beijing_front.jpg", "back": "beijing_back.jpg"},
        { "name": "Bradford, England", "front": "bradford_front.jpg", "back": "bradford_back.jpg"},
        { "name": "Delhi, India", "front": "delhi_front.jpg", "back": "delhi_back.jpg"},
        { "name": "Kampala, Uganda", "front": "kampala_front.jpg", "back": "kampala_back.jpg"},
        { "name": "Lima, Peru", "front": "lima_front.jpg", "back": "lima_back.jpg"},
        { "name": "London, England", "front": "london_front.jpg", "back": "london_back.jpg"},
        { "name": "New York, USA", "front": "new_york_front.jpg", "back": "new_york_back.jpg"},
        { "name": "Paris, France", "front": "paris_front.jpg", "back": "paris_back.jpg"},
    ]
    
    airpollution.DragDrop(deck,order).createLayout(4)
    i=1

def test_1(clean):
    import sys
    import engmonarchs
    sys.path.append("engmonarchs")
    import monarchdata

    global assignedSlots
    assignedSlots=[]
    
    arrangement=list(range(len(monarchdata.window.monarchdata)))
    #random.shuffle(arrangement)
    #order=arrangement[:12]
    order=[4,1,3,2]
    deck=[monarchdata.window.monarchdata[p] for p in order]
    
    engmonarchs.DragDrop(deck,order).createLayout(4)
    dragdrop.revealAll(None)
    dragdrop.arrangeAll(None)
    
def test_oscar(clean):
    import maleoscar
    maleoscar.DragDrop().createLayout(4)

    


def test_president(clean):
    import sys,random
    import presidentdata
    import presidents

    global assignedSlots
    assignedSlots=[]
        
    arrangement=list(range(len(presidentdata.presidentdata)))
    random.shuffle(arrangement)
    order=arrangement[:12]
    #order=[4,1,3,2]
    deck=[presidentdata.presidentdata[p] for p in order]
    
    
    presidents.DragDrop(deck,order).createLayout(4)


"""
test_1()
test_eng()

test_oscar()
test_president()
i=1

"""
