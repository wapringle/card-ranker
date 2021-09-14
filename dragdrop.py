from dataclasses import dataclass

from browser import document, html, window
from dragdrop2 import dragover, drop, mydrop, mydragstart, playdrop, mousedown, flipper, change_card_id
from dragdrop2 import px, rankSlots, assignedSlots
import dragdrop2

@dataclass
class Content:
    def __post_init__(self):
        self.flipped:bool=False
        self.card: str=''
        self.front_image=None
        self.back_image=None
    


    


#deck = []
#contentDeck=[]




class DragDrop(dragdrop2.DragDrop):
    """ This class contains all elements that should be configurable. 
    """

    def __init__(self,deck):
        """ The class dragdrop2.DragDrop provides an interface for the module dragdrop2 which should be 
            fairly immutible. We instantiate it by overwriting dragdrop2.interface
        """
        dragdrop2.interface = self
        self.getDeck(deck)

    def getDeck(self,deck):
        self.contentDeck= [Content(**p) for p in deck]

    def get_deck_for_card(self, c):
        for dk in self.contentDeck:
            if dk.card == c.id:
                return dk
        return None  # not found - shouldn't happen haha

    def get_body_text(self, content):
        return content

    def shuffledone(self, freeSlots):
        pass

    """ dragdrop2.flipper rotates a card. These routines permit different styles of flip
    """

    def flipper1(self, card):
        """ Called before flip
        """
        txt = card.firstChild.innerText
        card.firstChild.innerText = ""
        """ Naughty - parking txt in card structure
        """
        card.zz = txt

    def flipper2(self, card):
        """ Called halfway though
        """
        dk = self.get_deck_for_card(card)
        dk.flipped = not dk.flipped
        elt = document[card.id]
        elt.clear()
        if dk.flipped :
            elt <= dk.back_image 
        else:
            elt <= dk.front_image
        return

    def flipper3(self, card):
        """ Called after flip
        """
        card.firstChild.innerText = card.zz

      
         
    def createCard(self, cardno, content: Content, left, top):
        def get_body_text(content: Content):
            jpg = content.back if content.flipped else content.front
            return 'include/' + jpg

        card_id = f'C{cardno}'
        content.card = card_id

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

        header=self.makeHeader(content,cardno)

        body_height = card.offsetHeight - 20  # a guess

        content.flipped= True
        back_image = header + self.makeBackImage(content,cardno)

        content.back_image = back_image
        content.flipped = False
        
        front_image = header + self.makeFrontImage(content,cardno)
    
        content.front_image = front_image

        card <= front_image

        return card

    def createRank(self, rankno, left, top):
        rank_id = f'R{rankno}'
        rank = html.DIV(html.DIV(str(rankno), style={'font-size': 'xx-large', 'text-align': 'left', 'margin': px(20)}),
                        id=rank_id,
                        Class='rank',
                        style={"position": "absolute", "left": px(left), "top": px(top)},
                        )

        rank.bind("drop", mydrop)
        rank.bind("dragover", dragover)
        return rank

    def createLayout(self, columns=4):
        """ 
        Use this as a container for ranking slots. 
        """
        play = html.DIV("",
                        id='play',
                        Class='play',
                        style={"position": "absolute", "left": px(0), "top": px(0), "width": px(window.innerWidth - 100), "height": px(window.innerHeight - 100)},
                        )
        play.bind("dragover", dragover)
        play.bind("drop", playdrop)
        document <= play

        x = html.DIV("",
                     id="Cool as a penguin's sit-upon",
                     Class='rank-holder'
                     )
        document <= x

        lhmargin = 1
        dd = self.contentDeck
        cardCount = len(dd)
        for i in range(cardCount):
            card = self.createCard(i, dd[i], 0, 0)
            play <= card

        # use cardsize to calculate spacings for rank
        c = document[card.id]
        hsep = c.offsetWidth + x.width
        vsep = c.offsetHeight + x.height

        for i in range(cardCount):
            col = i % columns
            row = (i - col) / columns
            r = self.createRank(i + 1, x.left + (hsep) * (col), x.top + (vsep) * row)
            x <= r
            rankSlots.append(r)
            assignedSlots.append(None)

        rfirst = document[rankSlots[0].id]
        rlast = document[rankSlots[-1].id]
        for i in range(cardCount):
            col = i % columns
            row = (i - col) / columns
            document[dd[i].card].top = rlast.offsetTop + rlast.offsetHeight + 40 * i
            document[dd[i].card].left = rfirst.offsetLeft







