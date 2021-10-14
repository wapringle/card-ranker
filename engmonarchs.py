import time,copy,sys
from dataclasses import dataclass
from browser import document, html, timer, window
import  dragdrop 
from dragdrop import px
import random



@dataclass
class MonContent(dragdrop.Content):
    Dates: str
    Height: str
    Monarch: str
    Title: str 
    Width: str
    WikiURL: str
    img_url: str
    text: str



class DragDrop(dragdrop.DragDrop):

    def getDeck(self,deck):
        self.contentDeck= [MonContent(**p) for p in deck]

    def makeHeader(self,content,cardno):
        header_id = f'H{cardno}'
        
        
        fs= "small" if len(content.Title)>11 else "large"
        header = html.DIV(
            html.SPAN(
                content.Title,id=f'Q{cardno}'
                ),
                          id=header_id,
                          style={'text-align': 'center', 'font-size': fs, 'height': px(30), 'background-color': 'gray', 'border-bottom': 'dotted black', 'padding': '3px', 'font-family': 'sans-serif', 'font-weight': 'bold', "border-radius": "inherit", "margin": px(4), }
                          )
        return header
    
    def makeFrontImage(self,content,cardno):
        image_id = f'I{cardno}'
        body_id = f'B{cardno}'
        img = content.img_url
        return html.DIV(
            html.IMG(
                src=img, 
                id=image_id, 
                style={"width":px(self.card_width),"height":px(self.card_height - 30 - 14)}
            ),
            Class="card-body",
            id=body_id
            )
    
    def makeBackImage(self,content,cardno):
        image_id = f'I{cardno}'
        body_id = f'B{cardno}'
        img = content.img_url
        return html.DIV(
            #html.DIV(content['Monarch'])+
            html.DIV(html.SPAN(content.Dates),Class="date")+
            html.DIV(html.P(content.text))+
            html.A("X",href="https://en.wikipedia.org/"+content.WikiURL,target='_blank'),
            Class="card-text",
            #style={'font_size': 'small', "text-align": 'center'},
            id=body_id,
            text_align='center'
            )
        pass
    
    def flipper1(self, card):
        super().flipper1(card)

        dk = self.get_deck_for_card(card)
        if dk.flipped or True:
            txt = card.firstChild.nextSibling.innerHTML
            card.firstChild.nextSibling.innerHTML = ""
            # Naughty - parking txt in card structure
            #print(f'flipper1 {txt}')
            card.zz2 = txt   

    def flipper2(self, card):
        dk = self.get_deck_for_card(card)
        if dk.flipped or True:
            card.firstChild.nextSibling.innerHTML = card.zz2
        
        super().flipper2(card)

        if dk.flipped or True:
            
        
            txt = card.firstChild.nextSibling.innerHTML
            
            card.firstChild.nextSibling.innerHTML = ""
            # Naughty - parking txt in card structure
            #print(f'flipper2b {txt}')
            card.zz2 = txt   

        return
    
        
    def flipper3(self, card):
        super().flipper3(card)
        dk = self.get_deck_for_card(card)
        if dk.flipped or True:
            #print(f'flipper3 {card.zz2}')
            card.firstChild.nextSibling.innerHTML = card.zz2
        
        # whendone??
  

        
        
