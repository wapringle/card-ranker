import time,copy,sys
from dataclasses import dataclass
from browser import document, html, timer, window

import  dragdrop, engmonarchs 
from dragdrop import px
import random



@dataclass
class PresContent(dragdrop.Content):
    Dates: str
    Height: str
    President: str
    Title: str 
    Width: str
    WikiURL: str
    img_url: str
    text: str


class DragDrop(engmonarchs.DragDrop):

    def getDeck(self,deck):
        self.contentDeck= [PresContent(**p) for p in deck]

    def makeHeader(self,content,cardno):
        header_id = f'H{cardno}'
        
        fs= "small" if len(content.President)>11 else "large"
        header = html.DIV(
            html.SPAN(
                content.President,id=f'Q{cardno}'
                ),
                id=header_id,
                style={'text-align': 'center', 'font-size': fs, 'height': px(30), 'background-color': 'gray', 'border-bottom': 'dotted black', 'padding': '3px', 'font-family': 'sans-serif', 'font-weight': 'bold', "border-radius": "inherit", "margin": px(4), }
            )
        return header
    
  
    def makeBackImage(self,content,cardno):
        image_id = f'I{cardno}'
        body_id = f'B{cardno}'
        img = content.img_url
        return html.DIV(
            #html.DIV(content['Monarch'])+
            html.DIV(html.SPAN(content.Dates),Class="date")+
            html.DIV(html.P(content.Title))+
            html.A("X",href="https://en.wikipedia.org/"+content.WikiURL,target='_blank'),
            Class="card-text",
            #style={'font_size': 'small', "text-align": 'center'},
            id=body_id,
            text_align='center'
            )
        pass

