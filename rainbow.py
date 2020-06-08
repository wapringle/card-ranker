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
        t="Richard of York gained battles in vain".split(" ")
        for i in range(len(rainbow)):
            rainbow[i]["more"]=t[i]
        return sorted(rainbow,key=lambda n : n["name"])
    
    def flipper1(self,card):
        """ Called before flip
        """
        dk=self.get_deck_for_card(card)
        if dk["flipped"]:
            elt=document[card.id] 
            elt.clear()
            elt <= dk["back_image"]
            
        
    def flipper3(self,card):
        dk=self.get_deck_for_card(card)
        if dk["flipped"]:
            elt=document[card.id] 
            elt.clear()
            elt <= dk["titled_image"]
            
            elt.firstChild.html=elt.html

        
    def createCard(self,cardno,content,left,top):
        #self.id=f'C{self.cardno}'
        
        card_id=f'C{cardno}'
        content[flipped]=False
        content["card"]=card_id
        inner_id=f'I{cardno}'
        span_id=f'S{cardno}'
        ss={"border-radius": "inherit", "width": "inherit", "height": "inherit", "background-color": content["name"], "text-align": "center"}
        content["front_image"]=html.DIV( id=inner_id, style=ss)
        ss["background-color"]="grey"
        content["titled_image"]=html.DIV(html.SPAN(f'<br>{content["name"]}<br><br>{content["more"]}', Class="sansserif", style={'font-size':'large', "color": content["name"]},id=span_id), id=inner_id, style=ss)
        content["back_image"]=html.DIV( id=inner_id, style=ss)

        
        card=html.DIV(content["front_image"],
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


    



       

