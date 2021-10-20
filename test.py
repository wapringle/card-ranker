def test_1():
    import sys
    import engmonarchs
    import dragdrop
    sys.path.append("engmonarchs")
    import monarchdata
    
    arrangement=list(range(len(monarchdata.window.monarchdata)))
    #random.shuffle(arrangement)
    #order=arrangement[:12]
    order=[4,1,3,2]
    deck=[monarchdata.window.monarchdata[p] for p in order]
    
    engmonarchs.DragDrop(deck,order).createLayout(12)
    dragdrop.revealAll(None)
    dragdrop.arrangeAll(None)
    dragdrop.assignedSlots=[]
def test_eng():
    import airpollution
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
    
def test_oscar():
    import maleoscar
    import dragdrop
    maleoscar.DragDrop().createLayout(4)
    dragdrop.assignedSlots=[]
    


def test_president():
    import sys,random
    import presidentdata
    import dragdrop
    
    
    import presidents
        
    arrangement=list(range(len(presidentdata.presidentdata)))
    random.shuffle(arrangement)
    order=arrangement[:12]
    #order=[4,1,3,2]
    deck=[presidentdata.presidentdata[p] for p in order]
    
    
    presidents.DragDrop(deck,order).createLayout(4)
    dragdrop.assignedSlots=[]

test_1()
test_eng()

test_oscar()
test_president()
i=1