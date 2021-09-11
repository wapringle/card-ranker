from dataclasses import dataclass

from browser import document, html#, timer, window
#from dragdrop2 import dragover, mydragstart, mydrop, mymouseover, playdrop, mouseover, mousedown, flipper, change_card_id
from dragdrop2 import px
import dragdrop


@dataclass
class AirContent(dragdrop.Content):
    name: str
    front: str
    back: str



class DragDrop(dragdrop.DragDrop):
    """"""

    def getDeck(self,deck):
        self.contentDeck= [AirContent(**p) for p in deck]

    
        
    def makeHeader(self,content,cardno):
        header_id = f'H{cardno}'
        header = html.DIV(content.name,
                          id=header_id,
                          style={'height': px(20), 'background-color': 'gray', 'border-bottom': 'dotted black', 'padding': '3px', 'font-family': 'sans-serif', 'font-weight': 'bold', "border-radius": "inherit", "margin": px(4), }
                          )
        return header
    
    def makeFrontImage(self,content,cardno):
        image_id = f'I{cardno}'
        body_id = f'B{cardno}'
        img= 'include/' + content.front
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
        img= 'include/' + content.back
        return html.DIV(
            html.IMG(
                src=img, 
                id=image_id, 
                style={"border-radius": "inherit"}
            ),
            Class="card-body",
            id=body_id
            )
        pass
    
        
    
    