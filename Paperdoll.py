# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'


def paper_doll(text):
    result = ""
    for i in range(len(text)):
        text_trip = text[i]*3
        result += text_trip
    
    return result

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))
        

