def test_1():
    import sys
    import engmonarchs
    import dragdrop
    sys.path.append("engmonarchs")
    import monarchdata
    
    arrangement=list(range(len(monarchdata.monarchdata)))
    #random.shuffle(arrangement)
    engmonarchs.order=arrangement[:12]
    #order=[4,1,3,2]
    deck=[monarchdata.monarchdata[p] for p in engmonarchs.order]
    
    engmonarchs.DragDrop(deck).createLayout(12)
    engmonarchs.revealAll(None)
    engmonarchs.arrangeAll(None)
    
def test_eng():
    import airpollution
    
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
    
    airpollution.DragDrop(deck).createLayout(4)
    i=1
    
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
    
    
    presidents.DragDrop(deck).createLayout(4)

test_1()
test_eng()
test_president()
i=1