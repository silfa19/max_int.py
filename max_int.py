Skrifa kóða sem biður um integer þar til að neikvæð tala er slegin inn.
Biðja fyrist um tölu frá notanda 
Gera grein fyrir hvort talan sé jákvæð eða neikvæð
Ef talan er jákvæð, halda áfram að biðja um tölu 
Þegar talan verður neikvæð, gefa upp hvað hæsta integerið var. 




num_int = int(input("Input a number: "))    # Do not change this line

max_int = 0
while num_int > 0:
    num_int = int(input("Input a number: "))
    if num_int > max_int:
        max_int = num_int# Fill in the missing code
print("The maximum is", max_int)    # Do not change this line