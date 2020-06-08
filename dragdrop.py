from browser import document,html,timer,window
from dragdrop2 import dragover, mydragstart, mydrop, mymouseover, playdrop, mouseover, mousedown, flipper, change_card_id
from dragdrop2 import rankSlots, assignedSlots
import dragdrop2




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



def px(x):
    return str(x)+"px"

class DragDrop(dragdrop2.DragDrop):
    
    def __init__(self):
        dragdrop2.interface=self
        
    def getDeck(self):
        return deck
    
    def get_deck_for_card(self,c):
        for dk in self.getDeck():
            if dk["card"]==c.id:
                return dk
        return None; # not found - shouldn't happen haha
    
    
    def get_body_text(self,content):
        side = back if content[flipped] else front
        jpg=content[side]
        return 'include/'+jpg
    
    def flipper1(self,card):
        """ Called before flip
        """
        txt=card.firstChild.innerText
        card.firstChild.innerText=""
        """ Naughty - parking txt in card structure
        """
        card.zz=txt
        
    def flipper2(self,card):
        """ Called halfway though
        """
        dk=self.get_deck_for_card(card)
        dk["flipped"]= not dk["flipped"]
        img=self.get_body_text(dk)
        x="I"+card.id[1:]
        i2=document[x]
        i2['src']=img
        
    def flipper3(self,card):
        """ Called after flip
        """
        card.firstChild.innerText=card.zz
        
    def createCard(self,cardno,content,left,top):
        card_id=f'C{cardno}'
        content[flipped]=False
        content["card"]=card_id
        img=self.get_body_text(content)

        card=html.DIV(
            id=card_id,
            Class="card",
            style={"position":"absolute", "left": px(left), "top": px(top), 
            })
        card.bind("mouseover", mouseover)
        card.bind("dblclick",flipper)

        #card.style.zIndex=0

        card.draggable = True
        card.bind("dragstart", mydragstart)
        
        header_id=f'H{cardno}'
        header= html.DIV(content[name],
            id=header_id,
            style={ 'height': px(20), 'background-color':'gray', 'border-bottom': 'dotted black', 'padding': '3px', 'font-family': 'sans-serif', 'font-weight': 'bold',  "border-radius": "inherit", "margin": px(4),}
        )
        header.bind("mouseover", mymouseover)
        header.bind("mousedown", mousedown)

        card <= header
        
        body_height=card.offsetHeight - 20; # a guess
        img=self.get_body_text(content)
        image_id=f'I{cardno}'
        body_id =f'B{cardno}'
        body = html.DIV(html.IMG(src=img, id=image_id, style={"border-radius": "inherit"}), 
            Class="card-body",
        #style={'margin': px(4),   "height": px(card.offsetHeight-40), "border-radius": "inherit"},
        id=body_id)
        body.bind("mouseover", mouseover)
        header.bind("mousedown", mousedown)
        #body.bind("dblclick",flipper)
        card <= body

        return card

    def createRank(self,rankno,left,top):
        rank_id=f'R{rankno}'
        rank=html.DIV(html.DIV(str(rankno),style={'font-size': 'xx-large', 'text-align': 'left', 'margin': px(20)}),
            id=rank_id,
            Class='rank',
            style={"position":"absolute", "left": px(left), "top": px(top)},
            )
        
        rank.bind("drop", mydrop)
        rank.bind("dragover", dragover)
        return rank

    def createLayout(self, columns=4) :
        """ 
        Use this as a container for ranking slots. 
        """
        play =html.DIV("",
            id='play',
            Class='play',
            style={"position":"absolute", "left": px(0), "top": px(0 ), "width": px(window.innerWidth-100), "height": px(window.innerHeight-100)},
            )
        play.bind("dragover", dragover)
        play.bind("drop", playdrop)
        document <= play
    
        x = html.DIV("",
            id="Cool as a penguin's sit-upon",
            Class='rank-holder'
            #style={"position":"absolute", "left": px(0), "top": px(0), "width": px(1), "height": px(1)},
            )
        document <= x
        
        lhmargin=1
        dd=self.getDeck()
        cardCount=len(dd)
        for i in range(cardCount):
            card=self.createCard(i,dd[i],0,0)
            play <= card
        
        #use cardsize to calculate spacings for rank    
        c=document[card.id]
        hsep=c.offsetWidth+x.width
        vsep=c.offsetHeight+ x.height
    
        for i in range(cardCount):
            col = i % columns
            row = (i - col)/columns
            r=self.createRank(i+1,x.left+(hsep)*(col),x.top+(vsep)*row)
            x <= r
            rankSlots.append(r)
            assignedSlots.append(None)
    
        rfirst=document[rankSlots[0].id]
        rlast=document[rankSlots[-1].id]
        for i in range(cardCount):
            col = i % columns
            row = (i - col)/columns
            document[dd[i]["card"]].top=rlast.offsetTop+rlast.offsetHeight+ 40*i
            document[dd[i]["card"]].left=rfirst.offsetLeft
    
    



       

