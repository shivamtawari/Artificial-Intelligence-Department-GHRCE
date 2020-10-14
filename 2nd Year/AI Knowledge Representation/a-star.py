# Shivam Tawari A-58
class Node:
	def __init__(self,pattern,gfunc,move='start'):
		self.pattern = pattern
		self.gfunc = gfunc
		self.move = move
		for (row,i) in zip(pattern,range(3)):
			if 0 in row:
				self.blankloc=[i,row.index(0)]

	def __eq__(self,other):
		if other==None:
			return False

		for i in range(3):
			for j in range(3):
				if self.pattern[i][j]!=other.pattern[i][j]:
					return False
		return True

	def __getitem__(self,key):
		if isinstance(key,tuple)!=True:
			raise TypeError
		if len(key)!=2:
			raise KeyError

		return self.pattern[key[0]][key[1]]

	def calc_hfunc(self,goal):
		self.hfunc = 0
		for i in range(3):
			for j in range(3):
				if self.pattern[i][j]!=goal.pattern[i][j]:
					self.hfunc+=1
		if self.blankloc != goal.blankloc:
			self.hfunc-=1

		self.ffunc=self.hfunc+self.gfunc

		return self.hfunc,self.gfunc,self.ffunc

	def moveleft(self):
		if self.blankloc[1]==0:
			return None

		left = [[self.pattern[i][j] for j in range(3)]for i in range(3)]
		left[self.blankloc[0]][self.blankloc[1]]=left[self.blankloc[0]]\
                                                        [self.blankloc[1]-1]
		left[self.blankloc[0]][self.blankloc[1]-1]=0

		return Node(left,self.gfunc+1,'left')

	def moveright(self):
		if self.blankloc[1]==2:
			return None

		right = [[self.pattern[i][j] for j in range(3)]for i in range(3)]
		right[self.blankloc[0]][self.blankloc[1]]=right[self.blankloc[0]]\
                                                        [self.blankloc[1]+1]
		right[self.blankloc[0]][self.blankloc[1]+1]=0

		return Node(right,self.gfunc+1,'right')

	def moveup(self):
		if self.blankloc[0]==0:
			return None

		up = [[self.pattern[i][j] for j in range(3)]for i in range(3)]
		up[self.blankloc[0]][self.blankloc[1]]=up[self.blankloc[0]-1]\
                                                    [self.blankloc[1]]
		up[self.blankloc[0]-1][self.blankloc[1]]=0

		return Node(up,self.gfunc+1,'up')

	def movedown(self):
		if self.blankloc[0]==2:
			return None

		down = [[self.pattern[i][j] for j in range(3)]for i in range(3)]
		down[self.blankloc[0]][self.blankloc[1]]=down[self.blankloc[0]+1]\
                                                        [self.blankloc[1]]
		down[self.blankloc[0]+1][self.blankloc[1]]=0

		return Node(down,self.gfunc+1,'down')

	def moveall(self,game):
		left = self.moveleft()
		left = None if game.isclosed(left) else left
		right = self.moveright()
		right = None if game.isclosed(right) else right
		up = self.moveup()
		up = None if game.isclosed(up) else up
		down = self.movedown()
		down = None if game.isclosed(down) else down

		game.closeNode(self)
		game.openNode(left)
		game.openNode(right)
		game.openNode(up)
		game.openNode(down)

		return left,right,up,down

	def print(self):

		print('Move:', self.move, end='\t')
		print("g:", self.gfunc, "h:", self.hfunc, "f:", self.ffunc)
		print(self.pattern[0])
		print(self.pattern[1])
		print(self.pattern[2])


class Game:
	def __init__(self,start,goal):
		self.start = start
		self.goal = goal
		self.open = {}
		self.closed = {}
		hfunc,gfunc,ffunc = self.start.calc_hfunc(self.goal)
		self.open[ffunc] = [start]


	def isclosed(self,node):
		if node==None:
			return True

		hfunc,gfunc,ffunc = node.calc_hfunc(self.goal)

		if hfunc in self.closed:
			for x in self.closed[hfunc]:
				if x==node:
					return True

		return False

	def closeNode(self,node):
		if node==None:
			return

		hfunc,gfunc,ffunc= node.calc_hfunc(self.goal)
		self.open[ffunc].remove(node)
		if len(self.open[ffunc])==0:
			del self.open[ffunc]

		if hfunc in self.closed:
			self.closed[hfunc].append(node)
		else:
			self.closed[hfunc] = [node]

		return

	def openNode(self,node):
		if node==None:
			return

		hfunc,gfunc,ffunc = node.calc_hfunc(self.goal)
		if ffunc in self.open:
			self.open[ffunc].append(node)
		else:
			self.open[ffunc] = [node]

	def solve(self):

		presentNode = None

		while(presentNode!=self.goal):
			i=0
			while i not in self.open:
				i+=1
			presentNode = self.open[i][-1]
			presentNode.moveall(self)

		print("Backtracking From Goal to Start state: ")

		while presentNode.move!='start':
			presentNode.print()
			if presentNode.move == 'up':
				presentNode = presentNode.movedown()
			elif presentNode.move == 'down':
				presentNode = presentNode.moveup()
			elif presentNode.move == 'right':
				presentNode = presentNode.moveleft()
			elif presentNode.move == 'left':
				presentNode = presentNode.moveright()

			hfunc,gfunc,ffunc = presentNode.calc_hfunc(self.goal)
			for i in self.closed[hfunc]:
				if i==presentNode:
					presentNode = i
		start.print()

if __name__ == '__main__':
	startrow = [2, 0, 3, 1, 4, 6, 7, 5, 8]
	goalrow = [1, 2, 3, 4, 5, 6, 7, 8, 0]

	startloc = [startrow[0:3],startrow[3:6],startrow[6:]]
	goalloc = [goalrow[0:3],goalrow[3:6],goalrow[6:]]

	start = Node(startloc,0)
	goal = Node(goalloc,0,'goal')

	game = Game(start, goal)
	game.solve()
