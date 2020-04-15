from copy import copy
from math import log, ceil

class Node:
	def __init__(
		self,
		sum,
		prefix,
		left   = None,
		right  = None
	):
		self.sum    = sum
		self.prefix = prefix
		self.left   = left
		self.right  = right
		self.parent = None
		
	def update(self):
		self.sum    = self.left.sum + self.right.sum
		self.prefix = max(
			self.left.prefix, 
			self.left.sum + self.right.prefix 
		)  
		
def make_leave(val):
	return Node(val, val)
	
def make_parent(left, right):
	node = Node(
		sum    = left.sum + right.sum,
		prefix = max(left.prefix, left.sum + right.prefix),
		left   = left,
		right  = right
	)
	left.parent  = node
	right.parent = node
	return node	
		
def update_tree(val, node):
	
	node.sum      = val
	node.prefix   = val
	node          = node.parent
	
	while node is not None:
		node.update()
		node = node.parent

def solution1(S, N, A):

	C = dict((c, 0) for c in set(A))
	G = dict()
	X = [0] * N
	
	for i, t in enumerate(A):
		C[t] += 1
		if C[t] < S + 1:
			X[i] = 1
		elif C[t] == S + 1:
			X[i] = -S
			G[t] = [i]
		else:
			X[i] = 0
			G[t].append(i)
	
	B = None
	U = None
	H = N
	
	for i in range(ceil(log(N, 2) + 2)):
		if i == 0:
			U = [make_leave(val) for val in X]
			B = copy(U)
			continue
		d, m = divmod(H, 2)
		for j in range(d):
			l = 2 * j
			r = 2 * j + 1
			U[j] = make_parent(U[l], U[r])
		if m == 1:
			U[d] = U[H - 1]
		H = d + m
			
	root = U[0]		
	res  = root.prefix
	W    = dict((k, 0) for k in G)
	M    = dict((k, len(v)) for k, v in G.items())
	
	for i, e in enumerate(A[:N - S - 1], 1):
		
		n = B[i - 1]
		p = n.parent.parent
		
		if p is None:
			root = n.parent.right
			n.parent.right.parent = None
		else:
			p.left = n.parent.right
			n.parent.right.parent = p
			
		k1 = W.get(e, -1)
		
		if k1 != -1 and k1 < M[e]:
		
			t1 = G[e][k1]
			X[t1] = 1
			n = B[t1]
			update_tree(1, n)
			k2 = k1 + 1
			W[e] = k2
			
			if k2 < M[e]:
			
				t2 = G[e][k2]
				X[t2] = -S
				n = B[t2]
				update_tree(-S, n)
				
		update_tree(1, B[i])
				
		res = max(root.prefix, res)
		
	return res

if __name__ == "__main__":
	T = int(input())
	for i in range(T):
		N, S = map(int, input().split())
		A = list(map(int, input().split()))	
		result = solution1(S, N, A)
		answer = "Case #%s: %s" % (i + 1, result)
		print(answer)
	