# listas para guardar os dados manipulados
a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
i = []
j = []
k = []
l = []
m = []
n = []
o = []
p = []
q = []
r = []
s = []
t = []

# abrindo arquivo
arquivo = open('amazon.csv', 'r')
for linha in arquivo:

	# retirando os pontos das strings
	dados_sem_ponto = linha.replace('.', '')

	# quebrando em linhas
	dados = dados_sem_ponto.strip('\n').split(',')

	# coleta de dados especificos
	if dados[0] == '1998' and dados[1] == '"Ceara"':
		a_str = int(dados[3])
		a.append(a_str)
	elif dados[0] == '1999' and dados[1] == '"Ceara"':
		b_str = int(dados[3])
		b.append(b_str)
	elif dados[0] == '2000' and dados[1] == '"Ceara"':
		c_str = int(dados[3])
		c.append(c_str)
	elif dados[0] == '2001' and dados[1] == '"Ceara"':
		d_str = int(dados[3])
		d.append(d_str)
	elif dados[0] == '2002' and dados[1] == '"Ceara"':
		e_str = int(dados[3])
		e.append(e_str)
	elif dados[0] == '2003' and dados[1] == '"Ceara"':
		f_str = int(dados[3])
		f.append(f_str)
	elif dados[0] == '2004' and dados[1] == '"Ceara"':
		g_str = int(dados[3])
		g.append(g_str)
	elif dados[0] == '2005' and dados[1] == '"Ceara"':
		h_str = int(dados[3])
		h.append(h_str)
	elif dados[0] == '2006' and dados[1] == '"Ceara"':
		i_str = int(dados[3])
		i.append(i_str)
	elif dados[0] == '2007' and dados[1] == '"Ceara"':
		j_str = int(dados[3])
		j.append(j_str)
	elif dados[0] == '2008' and dados[1] == '"Ceara"':
		k_str = int(dados[3])
		k.append(k_str)
	elif dados[0] == '2009' and dados[1] == '"Ceara"':
		l_str = int(dados[3])
		l.append(l_str)
	elif dados[0] == '2010' and dados[1] == '"Ceara"':
		m_str = int(dados[3])
		m.append(m_str)
	elif dados[0] == '2011' and dados[1] == '"Ceara"':
		n_str = int(dados[3])
		n.append(n_str)
	elif dados[0] == '2012' and dados[1] == '"Ceara"':
		o_str = int(dados[3])
		o.append(o_str)
	elif dados[0] == '2013' and dados[1] == '"Ceara"':
		p_str = int(dados[3])
		p.append(p_str)
	elif dados[0] == '2014' and dados[1] == '"Ceara"':
		q_str = int(dados[3])
		q.append(q_str)
	elif dados[0] == '2015' and dados[1] == '"Ceara"':
		r_str = int(dados[3])
		r.append(r_str)
	elif dados[0] == '2016' and dados[1] == '"Ceara"':
		s_str = int(dados[3])
		s.append(s_str)
	elif dados[0] == '2017' and dados[1] == '"Ceara"':
		t_str = int(dados[3])
		t.append(t_str)

# troca de valores irregulares do arquivo
del(g[10])
g.insert(10, 2900)

del(h[11])
h.insert(11, 1360)

del(s[9])
s.insert(9, 1310)

# resultado "Media de queimadas no Estado do Ceara no intervalo de 1998 a 2017"
print(a)
print(round(sum(a) / len(a)))
print(b)
print(round(sum(b) / len(b)))
print(c)
print(round(sum(c) / len(c)))
print(d)
print(round(sum(d) / len(d)))
print(e)
print(round(sum(e) / len(e)))
print(f)
print(round(sum(f) / len(f)))
print(g)
print(round(sum(g) / len(g)))
print(h)
print(round(sum(h) / len(h)))
print(i)
print(round(sum(i) / len(i)))
print(j)
print(round(sum(j) / len(j)))
print(k)
print(round(sum(k) / len(k)))
print(l)
print(round(sum(l) / len(l)))
print(m)
print(round(sum(m) / len(m)))
print(n)
print(round(sum(n) / len(n)))
print(o)
print(round(sum(o) / len(o)))
print(p)
print(round(sum(p) / len(p)))
print(q)
print(round(sum(q) / len(q)))
print(r)
print(round(sum(r) / len(r)))
print(s)
print(round(sum(s) / len(s)))
print(t)
print(round(sum(t) / len(t)))

arquivo.close()