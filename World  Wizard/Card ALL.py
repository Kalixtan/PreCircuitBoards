


def card_pins_to_int( pins, back=False ):
    table = [ 1,2,3,5,6,7,9,11,13,15 ]
    
    if pins in table:
        return ((table.index(pins))*2)+int(back)
    
    elif back == False: # if not it must be flipped
        return card_pins_to_int( int('{:05b}'.format(pins)[::-1], 2), True )
    
    else:
        #print("ERROR")
        return -1

def to_string(answers):
    s = "( "
    for i in range(8):
        s += "ABCDEFGH"[i]
        s += ": "
        s += str(answers[i])
        s += " - "
    return s[:-3]+" )"

def ganswers( offset ):
    Sheets = [
        "71846253",
        "16382574"
    ]
    
    Sheets_id = int(offset >= 9) # SHEET

    answers = []
    for i in range(8):
        off = ((offset)+i)%8
        answers.append( Sheets[Sheets_id][off] )
    return answers
    
def get_answers( pins ):

    #print(int('{:05b}'.format(1)[::-1], 2))
    
    offset1 = card_pins_to_int(pins)
    if offset1 == -1:
        return
    offset2 = card_pins_to_int(int('{:05b}'.format(pins)[::-1], 2))
    if offset2 == -1:
        return
    
    answers1 = ganswers( offset1 )
    answers2 = ganswers( offset2 )


    # pritty print it
    s = '{:05b}'.format(pins)+"  "
    s += to_string( answers1 )+"  -  "
    s += to_string( answers2 )
    print(s)

get_answers( int('01111', 2) )

for i in range(0xf):
    get_answers( i )














