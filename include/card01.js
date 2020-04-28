var topmargin=100,
    lhmargin=100,
    rhmargin=100,
    gap=30,
    width=250,
    height=170;
    rankwidth=100;
    rankheight=100;
    
function Card(t) {
    this.txt= t;
}

Card.prototype.create=function(left,top) {
        var c=document.createElement('DIV');
        this.div=c;
        //c.id="C1";
        c.className='card';
        c.style="position:absolute; left: "+ left+ "px; top: "+top+"px; width: "+width+"px;  height: "+height+"px;";

        var header=document.createElement('DIV');
        header.style="background-color: gray; border-bottom: dotted black; padding: 3px; font-family: sans-serif; font-weight: bold;";
        header.innerText="Drag Me";
        header.addEventListener('mousedown',function (e) { event.target.parentNode.className="clicked";drag(c,e); },false);
        c.appendChild(header);
        var body=document.createElement('DIV');
        body.innerHTML="<div style='font-size: xx-large; text-align: center'>"+this.txt+"</div>";
        c.appendChild(body);
        
        return c;
}

function Rank(t) {
    this.txt= t;
}

Rank.prototype.create=function(left,top) {
    this.left=left;
    this.top=top;
    this.right=left+rankwidth;
    this.bottom=top+rankheight;
    var r=document.createElement('DIV');
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
var activeSlot=-1;
function CreateCards() {
    var board = document.getElementById('board');
    var deck=[
        "Rome",
        "Edinburgh",
        "Tokyo",
    ];
    
    for (var i=0;i<deck.length; i++) {
        board.appendChild(new Card(deck[i]).create(lhmargin,topmargin+(height+gap)*i) );
    }
    for (var i=0;i<deck.length; i++) {
        var r=new Rank(""+(i+1));
        board.appendChild(r.create(lhmargin+width+rhmargin,topmargin+(height+gap)*i));
        rankSlots[i]=r;
    }
    
}


function mouseoverRank(x,y) {
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

function snapoverRank(elementToDrag,x,y) {
    elementToDrag.className='card';
    if(activeSlot>=0) {
        rankSlots[activeSlot].div.appendChild(elementToDrag);
        rankSlots[activeSlot].div.className="rank";
        elementToDrag.style.zIndex=2;
        ret=[rankSlots[activeSlot].left,rankSlots[activeSlot].top ];
        ret=[0,0];
        activeSlot= -1;
        return ret;
}
    else 
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
