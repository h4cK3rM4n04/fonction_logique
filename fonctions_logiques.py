def XOR(a, b):
	return (a and not(b)) + (not(a) and b)

assert XOR(False,False)==False
assert XOR(False,True)==True
assert XOR(True,False)==True
assert XOR(True,True)==False

def logique1(A, B):
	return not(A or B)
def logique2(A, B):
	return not(A) and not(B)

assert logique2(False,False)==logique2(False,False)
assert logique2(False,True)==logique2(False,True)
assert logique2(True,False)==logique2(True,False)
assert logique2(True,True)==logique2(True,True)


def logique3(A, B, C):
	s = (not(A) or B) and C
	return s

assert logique3(False,False,False) == False
assert logique3(False,True,True) == True
assert logique3(False,False,True) == True
assert logique3(True,True,False) == False

def logique4(A, B, C):
	return not(C) or (A and B)

assert logique4(False,False,False) == True
assert logique4(False,True,True) == False
assert logique4(True,True,False) == True
assert logique4(True,True,True) == True

def logique5(A, B, C):
	return not(A and B) or not(C)

assert logique5(False,False,False) == True
assert logique5(False,True,True) == True
assert logique5(True,False,True) == True
assert logique5(True,True,True) == False