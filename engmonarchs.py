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
        return self.makeHeaderText(content.Title,cardno)

    
    def makeFrontImage(self,content,cardno):
        image_id = f'I{cardno}'
        body_id = f'B{cardno}'
        img = content.img_url
        return html.DIV(
            html.IMG(
                src=img, 
                id=image_id, 
                style={"width":px(self.card_width - 10 ),"height":px(self.card_height - 30 - 14)}
            ),
            Class="card-body",
            id=body_id
            )
    
    def makeBackImage(self,content,cardno):
        image_id = f'I{cardno}'
        body_id = f'B{cardno}'
        txt_id=f'T{cardno}'
        date_id=f'D{cardno}'
        img = content.img_url

        return html.DIV(
            html.DIV(
            html.A(content.text,href="https://en.wikipedia.org/"+content.WikiURL,target='_blank'),
            id=txt_id,
            Class="card-text"
            )+
            html.DIV(html.SPAN(content.Dates),id=date_id,Class="date"),
            id=body_id
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
        
        print(card.id, dk.flipped)
        if dk.flipped:
            txt=None
            try:
                txt= document['T'+card.id[1:]]
                date=document['D'+card.id[1:]]
            except:
                return
            print("XX", date.offsetTop)
            offset=date.offsetTop
            print("YY")
            print(card.id, offset, txt.offsetHeight)
            if txt:
                for s in range(20,1,-1):
                    print(f'{txt.id} S {s}')
                    txt.style.fontSize=px(s)
                    if txt.offsetHeight <= offset-35:
                        break            
        # whendone??
  

        
        
