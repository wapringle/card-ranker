from browser import document,html,timer
import math


""" translate css strings
import re
dict(re.findall(r'(\w+): *(\w+);',s))
dict(re.findall(r'([\w-]+): *([^;]*);',s))
"""

# offset of mouse relatively to dragged object when dragging starts
m0 = [None, None]

def mouseover(ev):
    """When mouse is over the draggable element, change cursor."""
    #print('mouse over ! ')
    ev.target.style.cursor = "move"


def dragstart(ev):
    """Function called when the user starts dragging the object."""
    global m0
    # compute mouse offset
    # ev.x and ev.y are the coordinates of the mouse when the event is fired
    # ev.target is the dragged element. Its attributes "left" and "top" are
    # integers, the distance from the left and top borders of the document
    m0 = [ev.x - ev.target.left, ev.y - ev.target.top]
    # associate data to the dragging process
    ev.dataTransfer.setData("text", ev.target.id)
    # allow dragged object to be moved
    ev.dataTransfer.effectAllowed = "move"


def dragover(ev):
    """Function called when the draggable object comes over the destination
    zone.
    """
    ev.dataTransfer.dropEffect = "move"
    # here we must prevent the default behaviour for this kind of event
    ev.preventDefault()


def drop(ev):
    """Function attached to the destination zone.
    Describes what happens when the object is dropped, ie when the mouse is
    released while the object is over the zone.
    """
    # retrieve data stored in drag_start (the draggable element's id)
    src_id = ev.dataTransfer.getData('text')
    elt = document[src_id]
    # set the new coordinates of the dragged object
    elt.style.left = "{}px".format(ev.x - m0[0])
    elt.style.top = "{}px".format(ev.y - m0[1])
    # don't drag the object any more
    elt.draggable = False
    # remove the callback function
    elt.unbind("mouseover")
    elt.style.cursor = "auto"
    ev.preventDefault()

"""
panel = document["panel"] # yellow zone

source = document["source"] # red zone
# place it at (10, 10) from panel top left corner
source.style.top = "{}px".format(10 + panel.abs_top)
source.style.left = "{}px".format(10 + panel.abs_left)
# make red zone draggable
source.draggable = True

dest = document["dest"] # green zone
# place it at (10, 150) from panel top left corner
dest.style.top = "{}px".format(10 + panel.abs_top)
dest.style.left = "{}px".format(150 + panel.abs_left)

dest.bind("drop", drop)
dest.bind("dragover", dragover)
source.bind("mouseover", mouseover)
source.bind("dragstart", dragstart)
"""

topmargin=40
lhmargin=40
rhmargin=40
gap=20
width=230
height=166
margin=4
rankWidth=width+3*margin
rankHeight=height+3*margin

name="name"
front="front"
back="back"
flipped="flipped"

deck=[
    { name: "Beijing, China", front: "beijing_front.jpg", back: "beijing_back.jpg"},
    { name: "Bradford, England", front: "bradford_front.jpg", back: "bradford_back.jpg"},
    { name: "Delhi, India", front: "delhi_front.jpg", back: "delhi_back.jpg"},
    { name: "Kampala, Uganda", front: "kampala_front.jpg", back: "kampala_back.jpg"},
    { name: "Lima, Peru", front: "lima_front.jpg", back: "lima_back.jpg"},
    { name: "London, England", front: "london_front.jpg", back: "london_back.jpg"},
    { name: "New York, USA", front: "new_york_front.jpg", back: "new_york_back.jpg"},
    { name: "Paris, France", front: "paris_front.jpg", back: "paris_back.jpg"},
]

"""
    { name: "Istanbul, Turkey", front: "istanbul_front.jpg", back: "kampala_back.jpg"},]
    { name: "Doha, Qatar ", front: "doha_front.jpg", back: "kampala_back.jpg"},
    { name: "Sydney, Australia", front: "sydney_front.jpg", back: "kampala_back.jpg"},
    """

sema4=False

def get_deck_for_card(c):
    for dk in deck:
        if dk["card"]==c.id:
            return dk
    return None; # not found - shouldn't happen haha


def px(x):
    return str(x)+"px"


def mymouseover(ev):
    #print(ev.currentTarget.id)
    mouseover(ev)
    
def mydragstart(ev):
    global sema4,m0
    id=ev.currentTarget.id
    dragstart(ev)
    # compute mouse offset
    # ev.x and ev.y are the coordinates of the mouse when the event is fired
    # ev.target is the dragged element. Its attributes "left" and "top" are
    # integers, the distance from the left and top borders of the document
    m0 = [ev.x - document[id].left, ev.y - document[id].top]
    if sema4:
        ev.dataTransfer.effectAllowed = "none"
    
def mymousedown(ev):
    id=ev.currentTarget.id
    print(f"mousedown {id}")
    document[id].parent.style.zIndex = 2
    
def mymouseup(ev):
    id=ev.currentTarget.id
    document[id].parent.style.zIndex= 1
    
def flipper(ev):
    id=ev.currentTarget.parent.id
    card=document[id]
    frameCount=20
    delta_width=width / frameCount
    ll=card.offsetLeft
    txt=card.firstChild.innerText;
    card.firstChild.innerText="";
    def flipper3(card):
        card.firstChild.innerText=txt

    def flipper2(card):
        # This is called to show the reverse side 
        dk=get_deck_for_card(card)
        dk[flipped]= not dk[flipped]
        img=get_body_text(dk)
        x="I"+card.id
        i2=document[x]
        i2['src']=img
        animateCSS(card,frameCount,30,{ 
            "width":  lambda frame,time: px((width * math.cos((frameCount - frame -1 )/frameCount * math.pi / 2))),
            "left":  lambda frame,time: px((ll+width/2 - (width * math.cos((frameCount - frame -1 )/frameCount * math.pi / 2))/2) ),
        },flipper3)
    
    animateCSS(card,frameCount,30,{ 
        'width':  lambda frame,time: px(width * math.cos((frame+1)/frameCount * math.pi / 2)) ,
        'left':  lambda frame,time: px(ll+width/2 - (width * math.cos((frame+1)/frameCount * math.pi / 2))/2),
    },flipper2);



    

def get_body_text(content):
    side = back if content[flipped] else front
    jpg=content[side]
    return 'include/'+jpg

class Card():
    def __init__(self,cardno):
        self.cardno=cardno
        self.content=deck[cardno]
                            
    def create(self,left,top):
        self.id=f'C{self.cardno}'
        card=html.DIV(
            id=f'C{self.cardno}',
            Class="card",
            style={"position":"absolute", "left": px(left), "top": px(top), "width": px(width), "height": px(height),  "border-radius": px(10), "background-color": "lightblue"},
            )
        card.draggable = True
        card.style.zIndex=1
        card.bind("dragstart", mydragstart)
        
        header= html.DIV(self.content[name],
            id=f'H{self.cardno}',
            style={ 'height': px(20), 'background-color':'gray', 'border-bottom': 'dotted black', 'padding': '3px', 'font-family': 'sans-serif', 'font-weight': 'bold',  "border-radius": "inherit", "margin": px(4),}

        )
        header.bind("mouseover", mymouseover)
        header.bind("mousedown", mymousedown)
        header.bind("mouseup", mymouseup)
        body_height=height - 20; # a guess
        img=get_body_text(self.content)
        body = html.DIV(html.IMG(src=img, id="I"+self.id, style={"border-radius": "inherit"}), style={'margin': px(4),   "height": px(height-40), "border-radius": "inherit"},id="B"+self.id)

        body.bind("dblclick",flipper)
        card <= header + body
        return card
   

def mydrop(ev):
    # retrieve data stored in drag_start (the draggable element's id)
    src_id = change_card_id(ev.dataTransfer.getData('text'))
    elt = document[src_id]
    rank_id=ev.currentTarget.id # target
    snapoverRank(src_id,rank_id )
    document[rank_id].appendChild(document[src_id])
    # set the new coordinates of the dragged object
    elt.style.left = px(margin) 
    elt.style.top =  px(margin) 
    # don't drag the object any more
    #elt.draggable = False
    # remove the callback function
    #elt.unbind("mouseover")
    elt.style.cursor = "auto"
    ev.preventDefault()

        
def playdrop(ev):
    global m0
    # retrieve data stored in drag_start (the draggable element's id)
    src_id = change_card_id(ev.dataTransfer.getData('text'))
    elt = document[src_id]

    remove_from_slot(change_card_id(src_id))
    
    # set the new coordinates of the dragged object
    elt.style.left = px(ev.x - m0[0])
    elt.style.top = px(ev.y - m0[1])
    elt.style.cursor = "auto"
    ev.preventDefault()

        
class Rank():
    def __init__(self,rankno):
        self.rankno=rankno
                            
    def create(self,left,top):
        self.id=f'R{self.rankno}'
        rank=html.DIV(html.DIV(str(self.rankno),style={'font-size': 'xx-large', 'text-align': 'left', 'margin': px(20)}),
            id=f'R{self.rankno}',
            Class='rank',
            style={"position":"absolute", "left": px(left), "top": px(top), "width": px(rankWidth), "height": px(rankHeight)},
            )
        
        rank.bind("drop", mydrop)
        rank.bind("dragover", dragover)
        return rank
        
rankSlots=[]
assignedSlots=[]

def createCards() :
    global deck
    cardCount=len(deck)
    print(cardCount)
    for i in range(cardCount):
        r=Rank(i+1)
        col = i % 4
        row = (i - col)/4
        document <= r.create(lhmargin+(width+rhmargin)*(col),topmargin+(height+gap)*row)
        rankSlots.append(r)
        assignedSlots.append(None)

    for i in range(cardCount):
        deck[i][flipped]=False
        cc=Card(i)   
 
        col = i % 4
        row = (i - col)/4
        if False:
            document <= cc.create(lhmargin+(width+rhmargin)*(col),topmargin+(height+gap)*(row+3))
        else:
            document <= cc.create(lhmargin,topmargin+(height+gap)*3 +gap*i)
        deck[i]["card"]=cc.id
        
    play =html.DIV("Hello",
        id='play',
        Class='rank',
        style={"position":"absolute", "left": px(lhmargin), "top": px(topmargin+(height+gap)*2 ), "width": px(4*width+3*rhmargin+12), "height": px(3*rankHeight)},
        )
    play.bind("dragover", dragover)
    
    play.bind("drop", playdrop)
    document <= play
    
    
"""
    for i in range(cardCount):
        src_id=deck[i]["card"]
        rank_id=rankSlots[i].id
        snapoverRank(src_id,rank_id )
        document[rank_id].appendChild(document[src_id if src_id[0]!= 'I' else src_id[1:]])
        elt=document[src_id]
        elt.style.left = px(margin) 
        elt.style.top =  px(margin) 
"""            
        
        
        
    
    
def animateCSS(element, numFrames, timePerFrame, animation, whendone):
    """ Adapted from Flanagan's javascript version
    """
    global frame, time
    frame = 0 #  // Store current frame number
    time = 0.0 #   // Store total elapsed time
    """
    // Arrange to call displayNextFrame() every timePerFrame milliseconds.
    // This will display each of the frames of the animation.
    """
    intervalId=None
    def displayNextFrame():
        global frame,time
#        print(frame,numFrames,time)
        if frame >= numFrames: #             #// First, see if we're done
            timer.clear_interval(intervalId) #// If so, stop calling ourselves
            if whendone:
                whendone(element) #// Invoke whendone function
            return


        for cssprop in animation:
            """
                // For each property, call its animation function, passing the
                // frame number and the elapsed time. Use the return value of the
                // function as the new value of the corresponding style property
                // of the specified element. Use try/catch to ignore any
                // exceptions caused by bad return values.
            """
            element.style[cssprop] = animation[cssprop](frame, time);
        
        frame+=1  #               // Increment the frame number
        time += timePerFrame  #// Increment the elapsed time
        

    intervalId = timer.set_interval(displayNextFrame, timePerFrame)
    
    """
    // The call to animateCSS() returns now, but the previous line ensures that
    // the following nested function will be invoked once for each frame
    // of the animation.

    // Now loop through all properties defined in the animation object
    """


def shuffleCards():
    """
    This routine shuffles cards one at a time by recursive calls from animateCSS
    """
    global shuffleSrc,shuffleFrom, shuffleDown # parameters for call
    global sema4
    oldslot=shuffleFrom
    oldsrc=shuffleSrc
    if assignedSlots[shuffleFrom]==None:
        sema4=False
    else:
        shuffleSrc=assignedSlots[shuffleFrom]
        to=shuffleFrom+1 if shuffleDown else shuffleFrom -1 #ither shuffle up or down
        originRank=document[rankSlots[shuffleFrom].id]
        targetRank=document[rankSlots[to].id]
        delta_top=targetRank.top - originRank.top
        delta_left=targetRank.left - originRank.left
        frameCount=20
        shuffleFrom=to
        if assignedSlots[to]:
            targetRank.style.zIindex=0
            document[assignedSlots[to]].style.zIindex=0
        src=document[shuffleSrc]
        def shuffle2(src):
            src.style.left = px(margin) 
            src.style.top =  px(margin) 
            targetRank.appendChild(src)
            if assignedSlots[to]:
                targetRank.style.zIindex=1
                document[assignedSlots[to]].style.zIindex=1
            shuffleCards()
        animateCSS(src,frameCount,30,{ 
            "top":  lambda frame,time: px(delta_top/frameCount*frame+margin) ,
            "left": lambda frame,time:px(delta_left/frameCount*frame+margin) ,
        },shuffle2);
        
        
    assignedSlots[oldslot]=oldsrc
    
def change_card_id(card_id):
    if card_id[0]=='I':
        # dragging using picture, change id to card
        return card_id[1:]
    else:
        return card_id
        
    
def remove_from_slot(card_id):
    cardCount=len(deck)
    for i in range(cardCount):
        if assignedSlots[i]==card_id:
            assignedSlots[i]=None
            break
    
def snapoverRank(card_id,rank_id):
    global shuffleSrc,shuffleFrom, shuffleDown
    global sema4
    #print(f"snapover {card_id} {rank_id} {assignedSlots} {[i.id for i in rankSlots]}")
    cardCount=len(deck)
    card_id=change_card_id(card_id)
    remove_from_slot(card_id)
        
        
    for r in range(cardCount):
        if rankSlots[r].id ==rank_id:
            # this is our slot
            if assignedSlots[r]==None:
                # it's empty, so no shuffling
                assignedSlots[r]=card_id
                break
            else:
                sema4=True
                moved=False
                shuffleFrom=r
                for a in range(r+1,cardCount):
                    if assignedSlots[a]==None:
                        shuffleSrc=card_id
                        shuffleDown=True
                        shuffleCards()
                        moved=True
                        break
                if not moved:
                    # else move up, assume there is an empty slot available
                    shuffleSrc=card_id
                    shuffleDown=False
                    shuffleCards()
                    
            break
    assignedSlots[r]=card_id
    shuffling=False
    pass

createCards()
