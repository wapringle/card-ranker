from browser import document,html,timer,window
from dragdrop2 import dragover, mydragstart, mydrop, mymouseover, playdrop, mouseover, mousedown, flipper
from dragdrop2 import rankSlots, assignedSlots
import dragdrop




name="name"
front="front"
back="back"
flipped="flipped"

rainbow=[
    { name: "red"},
    { name: "orange" },
    { name: "yellow" },
    { name: "green" },
    { name: "blue" },
    { name: "indigo" },
    { name: "violet" },
]




def px(x):
    return str(x)+"px"

class Rainbow(dragdrop.DragDrop):
    
    def getDeck(self):
        return sorted(rainbow,key=lambda n : n["name"])
    
    def getCard(self,ev):
        id=ev.currentTarget.id
        return document[id]
        
    def flipper1(self,card):
        """ Called before flip
        """
        return
        
    def flipper2(self,card):
        """ Called halfway though
        """
        dk=self.get_deck_for_card(card)
        dk["flipped"]= not dk["flipped"]
        side = back if dk[flipped] else front
        x="I"+card.id[1:]
        elt=document[card.id] 
        elt.clear()
        elt <= dk[side]
        return

 
    def flipper3(self,card):
        """ Called after flip
        """
        return
        
    def createCard(self,cardno,content,left,top):
        #self.id=f'C{self.cardno}'
        
        card_id=f'C{cardno}'
        content[flipped]=False
        content["card"]=card_id
        inner_id=f'I{cardno}'
        ss={"border-radius": "inherit", "width": "inherit", "height": "inherit", "background-color": content["name"], "text-align": "center"}
        content["front"]=html.DIV( id=inner_id, style=ss)
        ss["background-color"]="grey"
        content["back"]=html.DIV(html.SPAN(f'<br><br>{content["name"]}', style={'font-size':'large', "color": content["name"]}), id=inner_id, style=ss)

        
        card=html.DIV(content["front"],
            id=card_id,
            Class="rainbow",
            style={"position":"absolute", "left": px(left), "top": px(top), }
)
            
            
        card.bind("mouseover", mouseover)
        card.bind("mousedown", mousedown)
        card.bind("dblclick",flipper)

        card.draggable = True
        card.bind("dragstart", mydragstart)
        
        
        return card


    



       

