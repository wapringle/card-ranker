from browser import document, html, window
def px(x):
    return str(x) + "px"

def init():
    play = html.DIV("",
        id='play',
        Class='play',
        style={"position": "absolute", "left": px(0), "top": px(0), "width": px(window.innerWidth - 100), "height": px(window.innerHeight - 100)},
    )
    
    play <= html.DIV(
        html.H1("Card Ordering Game")+
        html.P("Follow the links below to date order the randomly selected cards"),
        Class="text"
    )
    list=[
        ("Air Pollution","air-pollution.html","Rank cities in order of Air Pollution"),
        ("Rainbow","rainbow.html","Order colours of the rainbow" ),
        ("English Kings & Queens","engmonarchs.html","Place a selection of English monarchs in date order"),
        ("US Presidents","uspresidents.html","Place a selection of US presidents in date order"),
        ("Male Oscar Winners","maleoscar.html","Place a selection of Oscar Winners for best Male Actor in date order"),
        ("Female Oscar Winners","femaleoscar.html","Place a selection of Oscar Winners for best female Actor in date order"),
        ("Nobel Literature Prizewinners","nobellit.html","Place a selection of Nobel Prize Winners for Literature in date order"),
    
    ]
    
    
    
    y=html.TABLE()
    for l in list:
        y<= html.TR(
                html.TD(
                    html.A(l[0], href=l[1], target='_blank'))+
                html.TD(l[2]),
                Class='text'
            )
    
    play <= y
    
    play <= html.P("""
    Drag a card over another to rearrange them.
        You can also drag cards to the shuffle space to help sort them.
    """, Class='text')
    
    play <= html.P("""
    Double-click a card to reveal its reverse. 
    """, Class='text')



    p2 = html.DIV(
        html.DIV(html.SPAN("SHUFFLE"), Class='shuffle')+
        html.DIV(html.SPAN("SPACE"), Class='shuffle'),
        Class='shuffle-box',
        style={
            #"margin-top": px(500),
            "margin-left": px(play.width -300), 
            #"margin-top": px(200),
            #"width": px(300), 
            },
        )
        
    p3=html.TABLE(html.TR(
        html.TD(play)+
        html.TD(p2)
        )
    )
    
    document <= play


    
    print("loaded")
