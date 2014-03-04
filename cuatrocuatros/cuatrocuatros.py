from collections import deque
from math import sqrt, pow
from time import time

def evalSolution(ev):
	ev = ev.replace('.4p', '(4.0/9.0)').replace('4!', '24.0')
	valor = -1
	try:
		valor = eval(ev)
		if int(valor)==valor:
	 		return int(valor) 
	except :
		return -1
	

eRules = ['(E)','4.0','44.0','sqrt(.4p)','sqrt(4.0)','0.4','.4p','4!','E+E','E*E','E/E','E-E','sqrt(E)']

axioms = deque([x for x in eRules if 'E' in x])
solutions = {}

inicio = time()
while len (axioms) > 0 and len(solutions) < 100:
	axiom = axioms.popleft()
	for er in eRules:
		s = axiom.replace('E', er, 1)
		if  ('E' in s) and (s.count('E') <= 4):
			axioms.append(s)
		elif s.count('4') == 4: # candidate solution
			val = evalSolution(s)
			if (0 < val <= 100) and (val not in solutions):
					solutions[val] = s
					print "ENCONTRADO: ", val, "Solucion: "+s+ " (a partir de :", axiom, ")  encontrados: ", len(solutions)
					missing = [x for x in range(1,101) if x not in solutions]
					print "MISSING: ", missing

for x in range(1,101):
	print x, solutions[x].replace('.0','').replace('**', '^').replace('p', '\'')

fin = time()

print('Tiempo total %g' % (fin - inicio))

