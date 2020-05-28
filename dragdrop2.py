from browser import document,html

""" translate css strings
import re
dict(re.findall(r'(\w+): *(\w+);',s))
dict(re.findall(r'([\w-]+): *([^;]*);',s))
"""

# offset of mouse relatively to dragged object when dragging starts
m0 = [None, None]

def mouseover(ev):
    """When mouse is over the draggable element, change cursor."""
    print('mouse over ! ')
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

topmargin=100
lhmargin=100
rhmargin=100
gap=30
width=250
height=166
margin=4
rankWidth=width+3*margin
rankHeight=height+3*margin

name="name"
front="front"
back="back"
deck=[
    { name: "Beijing, China", front: "beijing_front.jpg", back: "kampala_back.jpg"},
    { name: "Delhi, India", front: "delhi_front.jpg", back: "kampala_back.jpg"},
    { name: "Doha, Qatar ", front: "doha_front.jpg", back: "kampala_back.jpg"},
    { name: "Istanbul, Turkey", front: "istanbul_front.jpg", back: "kampala_back.jpg"},]
"""
    { name: "Kampala, Uganda", front: "kampala_front.jpg", back: "kampala_back.jpg"},
    { name: "Leeds, England", front: "leeds_front.jpg", back: "kampala_back.jpg"},
    { name: "Lima, Peru", front: "lima_front.jpg", back: "kampala_back.jpg"},
    { name: "London, England", front: "london_front.jpg", back: "kampala_back.jpg"},
    { name: "New York, USA", front: "new_york_front.jpg", back: "kampala_back.jpg"},
    { name: "Paris, France", front: "paris_front.jpg", back: "kampala_back.jpg"},
    { name: "Sydney, Australia", front: "sydney_front.jpg", back: "kampala_back.jpg"},
    """


def px(x):
    return str(x)+"px"


def mymouseover(ev):
    print(ev.currentTarget.id)
    mouseover(ev)
    
def mydragstart(ev):
    id=ev.currentTarget.id
    dragstart(ev)
    
def mymousedown(ev):
    id=ev.currentTarget.id
    document[id].parent.style["zIndex"] = 2
    
def mymouseup(ev):
    id=ev.currentTarget.id
    document[id].parent.style["zIndex"] = 0
    
    
class Card():
    def __init__(self,cardno):
        self.cardno=cardno
        self.content=deck[cardno]
                            
    def get_body_text(self):
        body_height=height - 20; # a guess
        
        jpg=self.content[front]
        return html.DIV(html.IMG(src='include/'+jpg, style={"border-radius": "inherit"}), style={'margin': px(4),   "height": px(height-40), "border-radius": "inherit"})
    def create(self,left,top):
        card=html.DIV(
            id=f'C{self.cardno}',
            Class="card",
            style={"position":"absolute", "left": px(left), "top": px(top), "width": px(width), "height": px(height),  "border-radius": px(10)},
            )
        card.draggable = True
        card.bind("dragstart", mydragstart)
        
        header= html.DIV(self.content[name],
            id=f'H{self.cardno}',
            style={'background-color': 'gray', 'border-bottom': 'dotted black', 'padding': '3px', 'font-family': 'sans-serif', 'font-weight': 'bold',  "border-radius": "inherit", "margin": px(4),}

        )
        header.bind("mouseover", mymouseover)
        header.bind("mousedown", mymousedown)
        header.bind("mouseup", mymouseup)
        
        body=self.get_body_text()
        
        card <= header + body
        
        return card
   

def mydrop(ev):
    """Function attached to the destination zone.
    Describes what happens when the object is dropped, ie when the mouse is
    released while the object is over the zone.
    """
    # retrieve data stored in drag_start (the draggable element's id)
    src_id = ev.dataTransfer.getData('text')
    elt = document[src_id]
    
    id=id=ev.currentTarget.id # target
    document[id].appendChild(document[src_id])
    # set the new coordinates of the dragged object
    elt.style.left = px(margin) #{}px".format(ev.x - m0[0])
    elt.style.top =  px(margin) #"{}px".format(ev.y - m0[1])
    # don't drag the object any more
    #elt.draggable = False
    # remove the callback function
    #elt.unbind("mouseover")
    elt.style.cursor = "auto"
    ev.preventDefault()

        
class Rank():
    def __init__(self,rankno):
        self.rankno=rankno
                            
    def create(self,left,top):
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
activeSlot=-1

def createCards() :
    cardCount=len(deck)
    print(cardCount)
    for i in range(cardCount):
        cc=Card(i)   
        document <= cc.create(lhmargin,topmargin+i*(height + gap))
    
    for i in range(cardCount):
        r=Rank(i+1)
        row = i % 4
        col = (i - row)/4
        document <= r.create(lhmargin+(width+rhmargin)*(col+1),topmargin+(height+gap)*row)
        rankSlots.append(r)
        assignedSlots.append(None)
        
createCards()

