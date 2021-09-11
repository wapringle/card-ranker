from browser import document, html, timer, window
import sys
sys.path.append("engmonarchs")
import dragdrop, monarchdata
from dragdrop2 import dragover, mydragstart, mydrop, mymouseover, playdrop, mouseover, mousedown, flipper, change_card_id, flip
from dragdrop2 import rankSlots, assignedSlots, snapoverRank
import random

import time

import copy


arrangement=list(range(len(monarchdata.monarchdata)))
random.shuffle(arrangement)
order=arrangement[:12]
#order=[4,1,3,2]
dragdrop.deck=[monarchdata.monarchdata[p] for p in order]

def px(x):
    return str(x) + "px"


def revealAll(ev):
    print("reveal all")
    for r in dragdrop.deck:
        
        if r['card'] in assignedSlots and r["flipped"]==False:
            flip(document[r['card']])


actionList=[]
shuffleDoneAction=None

def postArrange():
    global actionList, shuffleDoneAction
    if len(actionList):
        card_id, rank_id=actionList.pop()
        snapoverRank(card_id, rank_id)
        document[rank_id].appendChild(document[card_id])
        #shuffleDoneAction=postArrange
    else:
        shuffleDoneAction=None
        
        
    
def arrangeAll(ev):
    global shuffleDoneAction
    print(assignedSlots)
    print(order)
    
    map={}
    for i,s in enumerate(order):
        map[s]=i
    
    shuffleDoneAction=postArrange
    for i,k in enumerate(sorted(map.keys())):
        
        card_id=f'C{map[k]}'
        rank_id=f'R{i+1}'
        actionList.append((card_id,rank_id))
        
    postArrange()


class DragDrop(dragdrop.DragDrop):
    

    def makeHeader(self,content,cardno):
        header_id = f'H{cardno}'
        
        
        fs= "small" if len(content["Title"])>11 else "large"
            
        header = html.DIV(
            html.SPAN(
                content['Title'],id=f'Q{cardno}'
                ),
                          id=header_id,
                          style={'text-align': 'center', 'font-size': fs, 'height': px(30), 'background-color': 'gray', 'border-bottom': 'dotted black', 'padding': '3px', 'font-family': 'sans-serif', 'font-weight': 'bold', "border-radius": "inherit", "margin": px(4), }
                          )
        return header
    
    def makeFrontImage(self,content,cardno):
        image_id = f'I{cardno}'
        body_id = f'B{cardno}'
        img = content['img url']
        return html.DIV(
            html.IMG(
                src=img, 
                id=image_id, 
                style={"border-radius": "inherit"}
            ),
            Class="card-body",
            id=body_id
            )
        
    def makeBackImage(self,content,cardno):
        image_id = f'I{cardno}'
        body_id = f'B{cardno}'
        img = content['img url']
        return html.DIV(
            #html.DIV(content['Monarch'])+
            html.DIV(html.SPAN(content['Dates']),Class="date")+
            html.DIV(html.P(content['text']))+
            html.A("X",href="https://en.wikipedia.org/"+content['WikiURL'],target='_blank'),
            Class="card-text",
            #style={'font_size': 'small', "text-align": 'center'},
            id=body_id,
            text_align='center'
            )
        pass
    
    def flipper1(self, card):
        super().flipper1(card)

        dk = self.get_deck_for_card(card)
        if dk["flipped"]:
            txt = card.firstChild.nextSibling.innerHTML
            card.firstChild.nextSibling.innerHTML = ""
            """ Naughty - parking txt in card structure
            """
            #print(f'flipper1 {txt}')
            card.zz2 = txt   

    def flipper2(self, card):
        dk = self.get_deck_for_card(card)
        if dk["flipped"]:
            card.firstChild.nextSibling.innerHTML = card.zz2
        
        super().flipper2(card)

        if dk["flipped"]:
            
        
            txt = card.firstChild.nextSibling.innerHTML
            
            card.firstChild.nextSibling.innerHTML = ""
            """ Naughty - parking txt in card structure
            """
            #print(f'flipper2b {txt}')
            card.zz2 = txt   

        return
    
        
    def flipper3(self, card):
        super().flipper3(card)
        dk = self.get_deck_for_card(card)
        if dk["flipped"]:
            #print(f'flipper3 {card.zz2}')
            card.firstChild.nextSibling.innerHTML = card.zz2
        
        # whendone??
  

        
        
    def arrangeCards(self,dd,rankSlots):
        """
        rfirst = document[rankSlots[0].id]
        rlast = document[rankSlots[-1].id]
        for i in range(len(rankSlots)):
            #col = i % columns
            #row = (i - col) / columns40 * i
            card_id = f'C{i}'
            document[card_id].top = rfirst.offsetTop 
            document[card_id].left = rlast.offsetLeft + rlast.width + 40
        """
        super().arrangeCards(dd,rankSlots)
        for i in range(len(rankSlots)):
            card_id=f'C{i}'
            rank_id=f'R{i+1}'
            snapoverRank(card_id,rank_id)
            document[rank_id].appendChild(document[card_id])
            document[card_id].top=0
            
            document[card_id].left=0

    
    def shuffledone(self, freeSlots):
        global shuffleDoneAction
        print('shuffledone',freeSlots)
        if freeSlots==0 and shuffleDoneAction:
            shuffleDoneAction()
     
    def createLayout(self, columns=4):
        super().createLayout(columns)
        play=document['play']
        
        reveal = html.BUTTON(html.SPAN("Reveal all",Class='button-text'),
                        id='reveal',
                        Class='button2',
                        style={
                            "position": "absolute", 
                            "left": px(play.width -100), 
                            "top": px(40), 
                            "width": px(150), 
                            "height": px(30)},
                        )
        reveal.bind("click",revealAll)
        #play.bind("", dragover)
        document <= reveal
        
        arrange = html.BUTTON(html.SPAN("arrange all",Class='button-text'),
                        id='arrange',
                        Class='button2',
                        style={
                            "position": "absolute", 
                            "left": px(play.width -100), 
                            "top": px(100), 
                            "width": px(150), 
                            "height": px(30)},
                        )
        arrange.bind("click",arrangeAll)
        #play.bind("", dragover)
        document <= arrange
        
         
    def xxcreateCard(self, cardno, content, left, top):
        def get_body_text(content):
            side = "back" if content["flipped"] else "front"
            jpg = content['img url']
            return jpg

        card_id = f'C{cardno}'
        content["card"] = card_id

        card = html.DIV(
            id=card_id,
            Class="card",
            style={"position": "absolute", "left": px(left), "top": px(top),
                   })
        #card.bind("mouseover", mouseover)
        card.bind("dblclick", flipper)
        card.bind("mousedown", mousedown)

        card.draggable = True
        card.bind("dragstart", mydragstart)

        header_id = f'H{cardno}'
        if len(content["Title"])>18:
            fs= "small"
        else:
            fs="large"
            
        header = html.DIV(content["Title"],
                          id=header_id,
                          style={'font-size': fs, 'height': px(20), 'background-color': 'gray', 'border-bottom': 'dotted black', 'padding': '3px', 'font-family': 'sans-serif', 'font-weight': 'bold', "border-radius": "inherit", "margin": px(4), }
                          )
        """
        header.bind("mouseover", mymouseover)
        header.bind("mousedown", mousedown)
        
        
        card <= header
        """

        body_height = card.offsetHeight - 20  # a guess

        image_id = f'I{cardno}'
        body_id = f'B{cardno}'

        content["flipped"] = True
        img = get_body_text(content)
        back_image = header + html.DIV(html.IMG(src=img, id=image_id, style={"border-radius": "inherit"}),
                                       Class="card-body",
                                       id=body_id
                                       )
        content["back_image"] = back_image
        content["flipped"] = False
        img = get_body_text(content)
        front_image = header + html.DIV(html.IMG(src=img, id=image_id, style={"border-radius": "inherit"}),
                                        Class="card-body",
                                        id=body_id
                                        )

        content["front_image"] = front_image
        """
        body <=  content["front_image"]

        body.bind("mouseover", mouseover)
        header.bind("mousedown", mousedown)
        """

        card <= front_image

        return card
    
    pass
