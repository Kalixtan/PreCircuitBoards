


def card_pins_to_int( pins, back=False ):
    table = [ 1,2,3,5,6,7,9,11,13,15 ]
    
    if pins in table:
        return ((table.index(pins))*2)+int(back)
    
    elif back == False: # if not it must be flipped
        return card_pins_to_int( int('{:05b}'.format(pins)[::-1], 2), True )
    else:
        #print("ERROR")
        return -1

def get_answers( pins ):
    Sheets = [
        "71846253",
        "16382574"
    ]

    #print(int('{:05b}'.format(1)[::-1], 2))
    
    offset = card_pins_to_int(pins)
    if offset == -1:
        print('{:05b}'.format(pins))
        return
    
    Sheets_id = int(offset >= 9) # SHEET

    answers = []
    for i in range(8):
        off = ((offset)+i)%8
        answers.append( Sheets[Sheets_id][off] )


    # pritty print it
    s = '{:05b}'.format(pins)+"  ( "
    for i in range(8):
        s += "ABCDEFGH"[i]
        s += ": "
        s += str(answers[i])
        s += " - "
    #print(s[:-3]+" )")

#get_answers( int('01111', 2) )

for i in range(0x1f):
    get_answers( i )














