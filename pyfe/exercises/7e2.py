mbox = open('../provided/mbox-short.txt')

count = 0
sum = 0
value = 0

def find_dspam():
    for line in mbox:
        found = line.find('X-DSPAM-Confidence:')
        grab = line[found+1:]
        # num = grab.lstrip()
        # Python trims white space during float conversion
        value  = float(grab)

def find_totals():
    for value in mbox:
        count = count + 1
        sum = sum + value
            


