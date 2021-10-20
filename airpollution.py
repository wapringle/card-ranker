from dataclasses import dataclass

from browser import document, html#, timer, window
#from dragdrop2 import dragover, mydragstart, mydrop, mymouseover, playdrop, mouseover, mousedown, flipper, change_card_id
from dragdrop2 import px
import dragdrop, engmonarchs


@dataclass
class AirContent(dragdrop.Content):
    name: str
    front: str
    back: str



class DragDrop(engmonarchs.DragDrop):
    """"""

    def __init__(self,deck,sortOrder):
        super().__init__(deck,sortOrder)
                      
        self.ratio=0.9
        self.rank_seperator=40
                      

    def getDeck(self,deck):
        self.contentDeck= [AirContent(**p) for p in deck]

    
        
    def makeHeader(self,content,cardno):
        return self.makeHeaderText(content.name,cardno)    
    
    def makeFrontImage(self,content,cardno):
        image_id = f'I{cardno}'
        body_id = f'B{cardno}'
        img= 'include/' + content.front
        return html.DIV(
            html.IMG(
                src=img, 
                id=image_id, 
                style={"width":px(self.card_width - 10),"height":px(self.card_height - 30 - 14)}
                
            ),
            Class="card-body",
            id=body_id
            )
        
    def makeBackImage(self,content,cardno):
        image_id = f'I{cardno}'
        body_id = f'B{cardno}'
        img= 'include/' + content.back
        return html.DIV(
            html.IMG(
                src=img, 
                id=image_id, 
                style={"width":px(self.card_width - 10),"height":px(self.card_height - 30 - 14)}
            ),
            Class="card-body",
            style={"border-radius": px(25)},
            id=body_id
            )
        pass
    
        
    
    