import re
#split
#sub
#search
#findall

s = 'begum'
s1 = 'bengu-'
s2 = 'betul'
s3= 'ghj:234ytua'


#\w [0-9a-zA-Z_]
#\W [^0-9a-zA-Z_]
#\d [0-9]
#\D [^0-9]


c1 = '12BetulAygun'
deneme = 'ghehehhe'
c2 = '123EceAygun'
c3 = '41145OmerAygun'
c4 = 'ElifCicek'
print(re.search('[0-9]{11}' , c4))
st = "saat aat zanaat"
print(re.findall('[a-z]{2}[a]{2}t', st))




