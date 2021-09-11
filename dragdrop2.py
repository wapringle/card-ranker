from abc import ABC, abstractmethod

from browser import document, html, timer
import math


""" translate css strings
import re
dict(re.findall(r'(\w+): *(\w+);',s))
dict(re.findall(r'([\w-]+): *([^;]*);',s))
"""

rankSlots = []
assignedSlots = []

def px(x):
    return str(x) + "px"



class DragDrop(ABC):
    @abstractmethod
    def get_body_text(self, content):
        pass

    def getCard(self, ev):
        id = change_card_id(ev.currentTarget.id)
        return document[id]

    @abstractmethod
    def flipper1(self, card):
        pass

    @abstractmethod
    def flipper2(self, card):
        pass

    @abstractmethod
    def flipper3(self, card):
        pass

    @abstractmethod
    def shuffledone(self, freeSlots):
        pass


interface: DragDrop = None  # this will be instantiated by calling routine


def px(x):
    return str(x) + "px"


# offset of mouse relatively to dragged object when dragging starts
m0 = [None, None]


def mouseover(ev):
    """When mouse is over the draggable element, change cursor."""
    #print('mouse over ! ')
    ev.target.style.cursor = "move"


def dragstart(ev):
    """Function called when the user starts dragging the object."""
    global m0
    # compute mouse offset
    # ev.x and ev.y are the coordinates of the mouse when the event is fired
    # ev.target is the dragged element. Its attributes "left" and "top" are
    # integers, the distance from the left and top borders of the document
    m0 = [ev.x - ev.target.left, ev.y - ev.target.top]
    # associate data to the dragging process
    ev.dataTransfer.setData("text", ev.target.id)
    # allow dragged object to be moved
    ev.dataTransfer.effectAllowed = "move"


def dragover(ev):
    """Function called when the draggable object comes over the destination
    zone.
    """
    ev.dataTransfer.dropEffect = "move"
    # here we must prevent the default behaviour for this kind of event
    ev.preventDefault()


def drop(ev):
    """Function attached to the destination zone.
    Describes what happens when the object is dropped, ie when the mouse is
    released while the object is over the zone.
    """
    # retrieve data stored in drag_start (the draggable element's id)
    src_id = ev.dataTransfer.getData('text')
    elt = document[src_id]
    # set the new coordinates of the dragged object
    elt.style.left = "{}px".format(ev.x - m0[0])
    elt.style.top = "{}px".format(ev.y - m0[1])
    # don't drag the object any more
    elt.draggable = False
    # remove the callback function
    elt.unbind("mouseover")
    elt.style.cursor = "auto"
    ev.preventDefault()


sema4 = False


def mymouseover(ev):
    mouseover(ev)


def mousedown(ev):
    id = change_card_id(ev.currentTarget.id)
    # print(f'{ev.currentTarget.id} {id}')
    if id not in assignedSlots:
        # its not assigned to a slot
        document["play"].appendChild(document[id])


def mydragstart(ev):
    global sema4, m0
    id = ev.currentTarget.id
    # print('dragstart {id}')
    dragstart(ev)
    # compute mouse offset
    # ev.x and ev.y are the coordinates of the mouse when the event is fired
    # ev.target is the dragged element. Its attributes "left" and "top" are
    # integers, the distance from the left and top borders of the document
    m0 = [ev.x - document[id].left, ev.y - document[id].top]
    # print(f"dragstart {m0}")
    if sema4:
        ev.dataTransfer.effectAllowed = "none"


def setZindex(ev, z):
    return
    document[ev.currentTarget.id].parent.style.zIndex = z


def flipper(ev):
    card = interface.getCard(ev)
    flip(card)


def flip(card):
    frameCount = 20
    width = card.width
    delta_width = width / frameCount
    ll = card.offsetLeft

    interface.flipper1(card)

    def flipper2(card):

        # This is called to show the reverse side
        interface.flipper2(card)
        animateCSS(card, frameCount, 30, {
            "width": lambda frame, time: px((width * math.cos((frameCount - frame) / frameCount * math.pi / 2))),
            "left": lambda frame, time: px((ll + width / 2 - (width * math.cos((frameCount - frame) / frameCount * math.pi / 2)) / 2)),
        }, interface.flipper3)

    animateCSS(card, frameCount, 30, {
        'width': lambda frame, time: px(width * math.cos((frame) / frameCount * math.pi / 2)),
        'left': lambda frame, time: px(ll + width / 2 - (width * math.cos((frame) / frameCount * math.pi / 2)) / 2),
    }, flipper2)


def mydrop(ev):
    # retrieve data stored in drag_start (the draggable element's id)
    src_id = change_card_id(ev.dataTransfer.getData('text'))
    elt = document[src_id]
    rank_id = ev.currentTarget.id  # target
    snapoverRank(src_id, rank_id)
    document[rank_id].appendChild(document[src_id])

    # set the new coordinates of the dragged object
    margin = 0
    elt.style.left = px(margin)
    elt.style.top = px(margin)

    elt.style.cursor = "auto"
    ev.preventDefault()


def playdrop(ev):
    global m0
    # retrieve data stored in drag_start (the draggable element's id)
    src_id = change_card_id(ev.dataTransfer.getData('text'))
    # print(f'{ev.dataTransfer.getData("text")} {src_id}')
    elt = document[src_id]
    remove_from_slot(change_card_id(src_id))  # in case card was in a raking slot
    target = ev.currentTarget

    # set the new coordinates of the dragged object
    elt.style.left = px(ev.x - target.left + elt.parent.left - m0[0])
    elt.style.top = px(ev.y - target.top + elt.parent.top - m0[1])

    document["play"].appendChild(document[change_card_id(src_id)])
    setZindex(ev, 0)
    elt.style.cursor = "auto"
    ev.preventDefault()


class Ez():
    pass


ez = Ez()


def animateCSS(element, numFrames, timePerFrame, animation, whendone=None):
    """ Adapted from Flanagan's javascript version
    """
    # park these variables inside element - naughty
    element.frame = 0  # // Store current frame number
    element.time = 0.0  # // Store total elapsed time
    """
    // Arrange to call displayNextFrame() every timePerFrame milliseconds.
    // This will display each of the frames of the animation.
    """
    element.intervalId = None

    def displayNextFrame():
        if element.frame >= numFrames:  # // First, see if we're done
            timer.clear_interval(element.intervalId)  # // If so, stop calling ourselves
            """
            del element.frame
            del element.time
            del element.intervalId
            """
            if whendone:
                whendone(element)  # // Invoke whendone function
            return

        for cssprop in animation:
            """
                // For each property, call its animation function, passing the
                // frame number and the elapsed time. Use the return value of the
                // function as the new value of the corresponding style property
                // of the specified element. Use try/catch to ignore any
                // exceptions caused by bad return values.
            """
            element.style[cssprop] = animation[cssprop](element.frame, element.time)

        element.frame += 1  # // Increment the frame number
        element.time += timePerFrame  # // Increment the elapsed time

    element.intervalId = timer.set_interval(displayNextFrame, timePerFrame)

    """
    // The call to animateCSS() returns now, but the previous line ensures that
    // the following nested function will be invoked once for each frame
    // of the animation.

    // Now loop through all properties defined in the animation object
    """


def shuffleCards():
    """
    This routine shuffles cards one at a time by recursive calls from animateCSS
    """
    global shuffleSrc, shuffleFrom, shuffleDown  # parameters for call
    global sema4
    oldslot = shuffleFrom
    oldsrc = shuffleSrc
    if assignedSlots[shuffleFrom] == None:
        sema4 = False
    else:
        shuffleSrc = assignedSlots[shuffleFrom]
        to = shuffleFrom + 1 if shuffleDown else shuffleFrom - 1  # ither shuffle up or down
        originRank = document[rankSlots[shuffleFrom].id]
        targetRank = document[rankSlots[to].id]
        delta_top = targetRank.top - originRank.top
        delta_left = targetRank.left - originRank.left
        frameCount = 20
        shuffleFrom = to
        src = document[shuffleSrc]
        margin = 0
        """
        This piece of magic pops the rank to highest priority between slots. This means that
        the shuffled card is always slid from under the origin rank and over the target rank.
        Cool as a penguin's sit-upon.
        """
        document["Cool as a penguin's sit-upon"].appendChild(originRank)

        def shuffle2(src):
            src.style.left = px(margin)
            src.style.top = px(margin)
            targetRank.appendChild(src)
            shuffleCards()
        animateCSS(src, frameCount, 30, {
            "top": lambda frame, time: px(delta_top / frameCount * frame + margin),
            "left": lambda frame, time: px(delta_left / frameCount * frame + margin),
        }, shuffle2)

    assignedSlots[oldslot] = oldsrc
    interface.shuffledone(len([p for p in assignedSlots if p == None]))


def change_card_id(card_id):
    return "C" + card_id[1:]


def remove_from_slot(card_id):
    cardCount = len(assignedSlots)
    for i in range(cardCount):
        if assignedSlots[i] == card_id:
            assignedSlots[i] = None
            break


def snapoverRank(card_id, rank_id):
    global shuffleSrc, shuffleFrom, shuffleDown
    global sema4
    print(f"snapover {card_id} {rank_id} {assignedSlots} {[i.id for i in rankSlots]}")
    cardCount = len(assignedSlots)
    card_id = change_card_id(card_id)
    remove_from_slot(card_id)

    for r in range(cardCount):
        if rankSlots[r].id == rank_id:
            # this is our slot
            if assignedSlots[r] == None:
                # it's empty, so no shuffling
                assignedSlots[r] = card_id
                interface.shuffledone(len([p for p in assignedSlots if p == None]))
                break
            else:
                sema4 = True
                moved = False
                shuffleFrom = r
                for a in range(r + 1, cardCount):
                    if assignedSlots[a] == None:
                        shuffleSrc = card_id
                        shuffleDown = True
                        shuffleCards()
                        moved = True
                        break
                if not moved:
                    # else move up, assume there is an empty slot available
                    shuffleSrc = card_id
                    shuffleDown = False
                    shuffleCards()

            break
    assignedSlots[r] = card_id

