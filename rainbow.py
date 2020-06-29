from browser import document, html, timer, window
from dragdrop2 import dragover, mydragstart, mydrop, mymouseover, playdrop, mouseover, mousedown, flipper, flip
from dragdrop2 import rankSlots, assignedSlots
import dragdrop

import copy


name = "name"
front = "front"
back = "back"
flipped = "flipped"

rainbow = [
    {name: "red"},
    {name: "orange"},
    {name: "yellow"},
    {name: "green"},
    {name: "blue"},
    {name: "indigo"},
    {name: "violet"},
]


def px(x):
    return str(x) + "px"


class Rainbow(dragdrop.DragDrop):
    shuffled = False

    def get_body_text(self, content):
        pass

    def getDeck(self):
        t = "Richard of York gained battles in vain".split(" ")
        for i in range(len(rainbow)):
            rainbow[i]["more"] = t[i]
        return sorted(rainbow, key=lambda n: n["name"])

    def flipper1(self, card):
        """ Called before flip
        """
        dk = self.get_deck_for_card(card)
        if dk["flipped"]:
            elt = document[card.id]
            elt.clear()
            dk["back_image"].clear()
            elt <= dk["back_image"]

    def flipper3(self, card):
        dk = self.get_deck_for_card(card)
        if dk["flipped"]:
            elt = document[card.id]
            elt.clear()
            dk["back_image"] <= dk["back_detail"]
            elt <= dk["back_image"]

            # elt.firstChild.html=elt.html

    def shuffledone(self, freeSlots):
        if freeSlots == 0:
            if not self.shuffled:
                self.shuffled = True
                for r in rainbow:
                    card = r["card"]
                    document[card].bind("dblclick", flipper)
                    flip(document[card])

    def createCard(self, cardno, content, left, top):
        # self.id=f'C{self.cardno}'

        card_id = f'C{cardno}'
        content[flipped] = False
        content["card"] = card_id
        inner_id = f'I{cardno}'
        span_id = f'S{cardno}'
        ss = {"border-radius": "inherit", "width": "inherit", "height": "inherit", "background-color": content["name"], "text-align": "center"}
        content["front_image"] = html.DIV(id=inner_id, style=ss)
        ss["background-color"] = "grey"
        content["back_image"] = html.DIV(id=inner_id, style=ss)
        content["back_detail"] = html.SPAN(f'<br>{content["name"]}<br><br>{content["more"]}', Class="sansserif", style={'font-size': 'large', "color": content["name"]}, id=span_id)

        card = html.DIV(content["front_image"],
                        id=card_id,
                        Class="rainbow",
                        style={"position": "absolute", "left": px(left), "top": px(top), }
                        )

        card.bind("mouseover", mouseover)
        card.bind("mousedown", mousedown)
        # card.bind("dblclick",flipper)

        card.draggable = True
        card.bind("dragstart", mydragstart)

        return card
    