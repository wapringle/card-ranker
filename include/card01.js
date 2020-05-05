var topmargin=100,
    lhmargin=100,
    rhmargin=100,
    gap=30,
    width=250,
    height=166;
    rankwidth=width;
    rankheight=height;
    
var deck=[
    { name: "Beijing, China", front: "beijing_front.jpg", back: "kampala_back.jpg"},
    { name: "Delhi, India", front: "delhi_front.jpg", back: "kampala_back.jpg"},
    { name: "Doha, Qatar ", front: "doha_front.jpg", back: "kampala_back.jpg"},
    { name: "Istanbul, Turkey", front: "istanbul_front.jpg", back: "kampala_back.jpg"},
    { name: "Kampala, Uganda", front: "kampala_front.jpg", back: "kampala_back.jpg"},
    { name: "Leeds, England", front: "leeds_front.jpg", back: "kampala_back.jpg"},
    { name: "Lima, Peru", front: "lima_front.jpg", back: "kampala_back.jpg"},
    { name: "London, England", front: "london_front.jpg", back: "kampala_back.jpg"},
    { name: "New York, USA", front: "new_york_front.jpg", back: "kampala_back.jpg"},
    { name: "Paris, France", front: "paris_front.jpg", back: "kampala_back.jpg"},
    { name: "Sydney, Australia", front: "sydney_front.jpg", back: "kampala_back.jpg"},
];



function Card(i) {
    this.txt= deck[i].name;
    this.cardno=i;
}

/*
 * This lot is a mess
 */
 
function get_deck_for_card(c) {
    for(i=0;i<deck.length;i++) {
        if(deck[i].card==c)
            return deck[i];
    }
    return null; // not found - shouldn't happen haha
}

function get_body_text(dk) {
    /*
     * We may want to replace the back image with some html text
     */
    body_height=height - 20; // a guess
    jpg=dk.flipped? dk.back : dk.front;
    return  "<div><img style='height: "+body_height+"px;' src='include/" + jpg +"'></div>";
    /*
    if(dk.flipped)
        return "<DIV><h>A Message</h></div";
    else
        return  "<div><img style='height: "+body_height+"px;' src='include/" + jpg +"'></div>";
    */

}


function flipper(card,event) {
    /*
     * flip card front to back or vice versa
     */
    frameCount=20;
    delta_width=width / frameCount;
    ll=card.offsetLeft;
    var txt=card.firstChild.innerText;
    card.firstChild.innerText="";
    function flipper3(card) {
        card.firstChild.innerText=txt;
    }
    function flipper2(card) {
        /* This is called to show the reverse side */
        dk=get_deck_for_card(card);
        dk.flipped= !dk.flipped;
        card.lastChild.innerHTML=get_body_text(dk);
        animateCSS(card,frameCount,50,{ 
            width:  function(frame,time) {return (width * Math.cos((frameCount - frame -1 )/frameCount * Math.PI / 2)).toFixed(0) +  "px"; },
            left:  function(frame,time) { lll=(ll+width/2 - (width * Math.cos((frameCount - frame -1 )/frameCount * Math.PI / 2))/2).toFixed(0) ;  return lll +  "px"; },
        },flipper3);
    }
    
    animateCSS(card,frameCount,25,{ 
        width:  function(frame,time) { return (width * Math.cos((frame+1)/frameCount * Math.PI / 2)).toFixed(0) +  "px"; },
        left:  function(frame,time) { lll=(ll+width/2 - (width * Math.cos((frame+1)/frameCount * Math.PI / 2))/2).toFixed(0) ;  return lll +  "px"; },
    },flipper2);

}

Card.prototype.create=function(left,top) {
        var c=document.createElement('DIV');
        this.div=c;
        deck[this.cardno].card=c;
        this.flipped=false;
        c.id="C"+this.cardno;
        c.className='card';
        c.style="position:absolute; left: "+ left+ "px; top: "+top+"px; width: "+width+"px;  height: "+height+"px;";
        
        /*
         * the card has a header which the mouse uses to drag the card, plus a body. 
         * This bit will be expanded
         */

        var header=document.createElement('DIV');
        header.style="background-color: gray; border-bottom: dotted black; padding: 3px; font-family: sans-serif; font-weight: bold; height: 20px";
        header.innerText=this.txt;
        header.addEventListener('mousedown',function (e) { 
            event.target.parentNode.className="clicked";
            event.target.parentNode.style.zIndex=3; // When card is dragged, it should pass over all other items
            drag(c,e); // This is the David Flanagan function. [ a lot of the detail between browsers is now redundant ]
        },false);
        
        c.appendChild(header);
        var body=document.createElement('DIV');
        /* 
         * Body is just a placeholder for card image etc.
         */
         
        body.innerHTML=get_body_text(deck[this.cardno]);
        c.appendChild(body);
        /*
         * click over the body to flip the card ( will this get confused with dragging header ? )
         */
        body.addEventListener('mousedown',function (e) { 
            flipper(c,e);
        },false);

        return c;
}



var rankno=1;
function Rank(t) {
    this.txt= t;
    this.rankno=rankno;
    rankno += 1;
}

Rank.prototype.create=function(left,top) {
    this.left=left;
    this.top=top;
    this.right=left+rankwidth;
    this.bottom=top+rankheight;
    var r=document.createElement('DIV');
    r.id="R"+this.rankno;
    this.div=r;
    r.className='rank';
    r.style="position:absolute; left: "+ left+ "px; top: "+top+"px; width: "+rankwidth+"px;  height: "+rankheight+"px;";
    r.innerHTML="<div style='font-size: xx-large; text-align: left'>"+this.txt+"</div>";
    return r;
}
Rank.prototype.contains=function(x,y) {
    if (x>=this.left && x < this.right && y >= this.top && y < this.bottom)
        return true;
    else
        return false;
    
}

var rankSlots=[];
var assignedSlots=[];
var activeSlot=-1;
var shuffling=false;
function CreateCards() {
    var board = document.getElementById('board');
    for (var i=0;i<deck.length; i++) {
        board.appendChild(new Card(i).create(lhmargin,topmargin+(height+gap -170)*i) );
        
    }
    for (var i=0;i<deck.length; i++) {
        var r=new Rank(""+(i+1));
        row = i % 4;
        col = (i - row)/4;
        board.appendChild(r.create(lhmargin+(width+rhmargin)*(col+1),topmargin+(height+gap)*row));
        rankSlots[i]=r;
        assignedSlots[i]=null;
    }
    
}


function mouseoverRank(x,y) {
    /*
     * What happens when mouse enters or leaves target landing pad
     */
    if(shuffling) return;
    if(activeSlot>=0)
        if(rankSlots[activeSlot].contains(x,y))
            return;
        else {
            rankSlots[activeSlot].div.className="rank";
            activeSlot= -1;
            console.log("mouse out");
        }
    for(var i=0;i<rankSlots.length;i++) {
        if(rankSlots[i].contains(x,y)) {
            rankSlots[i].div.className="selected";
            activeSlot=i;
            console.log("mouse in");
            return;
        }
    }

}
var shuffleFrom=null;
var shuffleDown=true;

function shuffleCards(card) {
    /*
     * This routine shuffles cards one at a time by recursive calls from animateCSS
     */
    var oldslot=shuffleFrom;
    if(assignedSlots[shuffleFrom]!=null) {
        var src=assignedSlots[shuffleFrom];
        var to= shuffleDown? shuffleFrom+1 : shuffleFrom-1;
        var delta_left=rankSlots[to].left - rankSlots[shuffleFrom].left;
        var delta_top=rankSlots[to].top - rankSlots[shuffleFrom].top;
        var frameCount=10;

        with(rankSlots[to].div) {
            appendChild(src);
        }
        
        
        with(src) {
            style.left = "0px";
            style.top =  shuffleDown? "-"+delta_top+"px" : (-delta_top) +"px";
            
        }
        
        /*
         * This bit animates moving the cards between slots. Unecessary but cool. 
         * Another Flanagan script
         */
        shuffleFrom=to;
        animateCSS(src,frameCount,30,{ 
            top:  function(frame,time) { return delta_top/frameCount*(frame - frameCount +1) +  "px"; },
            left: function(frame,time) { return delta_left/frameCount*(frame - frameCount +1) + "px"; }
        },shuffleCards);
    }
    assignedSlots[oldslot]=card;
}

function snapoverRank(elementToDrag) {
    console.log("snapover",activeSlot);
    shuffling=true;
    elementToDrag.className='card';
    elementToDrag.style.zIndex=1;
    var as=activeSlot; /* activeSlot appears to be overridden when this is running */
    if(as>=0) {
        /*
         * Card has landed over a destination slot. Snap it to slot.
         */
        for(var i=0;i<assignedSlots.length;i++) {
            if(assignedSlots[i]==elementToDrag) {
                /*
                 * Card has been moved from a ranking slot. Deassign it
                 */
                 assignedSlots[i]=null;
                 break;
            }
        }
        if(assignedSlots[as]!=null) {
            /*
             * There is someone here already, move them.
             * If there is a lower priority slot free, shuffle down, else shuffle up.
             */
            var moved=false;
            shuffleFrom=as;
            for(var i=as+1;i<assignedSlots.length;i++) {
                if(assignedSlots[i]==null) {
                    shuffleDown=true;
                    shuffleCards(elementToDrag);
                    moved=true;
                    break;
                }
            }
            if(!moved) {
                    shuffleDown=false;
                    shuffleCards(elementToDrag);
            }
        } else {
                activeSlot= -1;

        }
        /* 
         * Card now safely assigned to slot, make the visuals correct.
         */
        with(rankSlots[as].div) {
            appendChild(elementToDrag);
            className="card";
        }
        assignedSlots[as]=elementToDrag;
        ret=[0,0]; /* card child of slot, so position relative to slot */
        shuffling=false;
        return ret;
    } else 
        /*
         * Not over a slot, so snap back to original position
         */
        shuffling=false;
        return [];
}

function mousein(event) {
  event.target.className="selected";
  console.log("mouse in");
}
function mouseout(event) {
  event.target.className="rank";
  console.log("mouse out");
}

function mousedown(e) { 
  event.target.className="clicked";
  console.log("mouse down");
}
