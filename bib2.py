from browser import document,html,timer,window
from dragdrop2 import dragover, mydragstart, mydrop, mymouseover, playdrop, mouseover, mousedown, flipper, change_card_id
from dragdrop2 import rankSlots, assignedSlots
import dragdrop




name="name"
front="front"
back="back"
flipped="flipped"

xxdeck=[
    { name: "Beijing, China", front: "beijing_front.jpg", back: "beijing_back.jpg"},
    { name: "Bradford, England", front: "bradford_front.jpg", back: "bradford_back.jpg"},
    { name: "Delhi, India", front: "delhi_front.jpg", back: "delhi_back.jpg"},
    { name: "Kampala, Uganda", front: "kampala_front.jpg", back: "kampala_back.jpg"},
    { name: "Lima, Peru", front: "lima_front.jpg", back: "lima_back.jpg"},
    { name: "London, England", front: "london_front.jpg", back: "london_back.jpg"},
    { name: "New York, USA", front: "new_york_front.jpg", back: "new_york_back.jpg"},
    { name: "Paris, France", front: "paris_front.jpg", back: "paris_back.jpg"},
]



def px(x):
    return str(x)+"px"

class DragDrop(dragdrop.DragDrop):
    
    def flipper2(self,card):
        """ Called halfway though
        """
        dk=self.get_deck_for_card(card)
        dk["flipped"]= not dk["flipped"]
        img=self.get_body_text(dk)
        
        document[card.id].style["background-image"]= f'url("{img}")'
        
    def createCard(self,cardno,content,left,top):
        #self.id=f'C{self.cardno}'
        
        card_id=f'C{cardno}'
        content[flipped]=False
        content["card"]=card_id
        img=self.get_body_text(content)

        card=html.DIV(
            id=card_id,
            Class="card2",
            style={"position":"absolute", "left": px(left), "top": px(top), 
                   "background-image": f'url("{img}")',
#                   "backgroundSize": f"{width}px {height}px",
            })
        card.bind("mouseover", mouseover)
        card.bind("mousedown", mousedown)
        card.bind("dblclick",flipper)

        card.draggable = True
        card.bind("dragstart", mydragstart)
        
        header= html.DIV(content[name],
            id=f'H{cardno}',
            style={ 'height': px(20), 'background-color':'gray', 'border-bottom': 'dotted black', 'padding': '3px', 'font-family': 'sans-serif', 'font-weight': 'bold',  "border-radius": "inherit", "margin": px(4),}
        )
        header.bind("mouseover", mymouseover)
        header.bind("mousedown", mousedown)

        card <= header
        
        return card


    



       

