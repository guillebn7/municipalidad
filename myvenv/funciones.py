def max2(a,b):
    if (a>b):
        return a
    elif (a<b):
        return b
    else:
        return("iguales " , a , " y " ,b)


def max3(a,b,c):
    lista = [a,b,c]
    lista.sort()
    return lista[-1]


def long(lista):
	i = 0
	for elemento in lista:
		i = i + 1
	return i
	    
def esVocal(letra):
	lower(letra)
	if (letra == 'a') or (letra == 'e') or (letra == 'i') or (letra == 'o') or (letra == 'u')
	    return True
	else:
	    return False
