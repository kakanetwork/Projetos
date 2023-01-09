var1 = str(input('Insira uma palavra: '))
var2 = len(var1)
for x in range((len(var1) +1) * 2):
    if x < len(var1):
        print(var1[:x])
    elif x > len (var1):
        print(var1[:var2])    
        var2 -= 1