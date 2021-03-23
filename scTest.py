from smartcard.CardType import AnyCardType
from smartcard.CardRequest import CardRequest
from smartcard.util import toHexString
from smartcard import Exceptions
import time

def stringParser(dataCurr):
#--------------String Parser--------------#
    #([85, 203, 230, 191], 144, 0) -> [85, 203, 230, 191]
    if isinstance(dataCurr, tuple):
        temp = dataCurr[0]
        code = dataCurr[1]
    #[85, 203, 230, 191] -> [85, 203, 230, 191]
    else:
        temp = dataCurr
        code = 0

    dataCurr = ''

    #[85, 203, 230, 191] -> bfe6cb55 (int to hex reversed)
    for val in temp:
        # dataCurr += (hex(int(val))).lstrip('0x') # += bf
        dataCurr += format(val, '#04x')[2:] # += bf

    #bfe6cb55 -> BFE6CB55
    dataCurr = dataCurr.upper()

    #if return is successful
    if (code == 144):
        return dataCurr

while True:
    cardtype = AnyCardType()
    cardrequest = CardRequest(timeout=1, cardType=cardtype)

    cardservice = None

    print("Waiting for card",end="")
    while cardservice is None:
        try:
            cardservice = cardrequest.waitforcard()
        except Exceptions.CardRequestTimeoutException:
            print('.', end="")


    cardservice.connection.connect()
    resp = cardservice.connection.transmit([0xFF, 0xB0, 0x00, int(0), 0x04])
    print()
    print(stringParser(resp))
    print("Waiting for card removal",end="")

    while cardservice is not None:
        cardservice = None
        try:
            cardservice = cardrequest.waitforcard()
            print('.',end="")
            time.sleep(0.5)
        except Exceptions.CardRequestTimeoutException:
            print("Finally!")
