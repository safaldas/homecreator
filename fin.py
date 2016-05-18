import numpy as np
import sys
import math
import rooms

abuf = []
bbuf = []
pc = []
puppet =[]
scale = 30
translate = 100

def generateroom(n):

	xa = 0
	ya = 0
	m=0 
	ee = 0
	w = 120 #int(input("enter width along x axis : "))		# plot width
	h = 120 #int(input("enter height along y axis : "))		# plot height
	#n = int(input("enter no of rooms: "))			# no of rooms

	p = []
	for e in range(n):
		p.append(e)
	#print "permutations input",p


	for a in range(math.factorial(len(p))):	 # taking each permutation

	        #abuf = [(0,0)]              #abuf initialised to (0,0)
		pc.append((np.random.permutation(len(p))))
	for pp in pc:
		abuf = [(0,0)]
		bbuf = []
		print "permutated outputs",pp
	#		out = []
		c,d = abuf[0][0],abuf[0][1]
		for b in pp:			#	for each object in a permuted set

			ee = ee + 1

			if b == 0:	# master bed  width and length
				room1 = rooms.bedroom()
			if b == 1:	# kitchen
				room1 = rooms.bedroom()
			if b == 2:	# bathroom
				room1 = rooms.bedroom()
			if b == 3:	# bedroom2
				room1 = rooms.bedroom()
			if b == 4:	# living space
				room1 = rooms.bedroom()
			if b == 5:	# another bed space
				room1 = rooms.bedroom()
			if b == 6: # car porch
				room1 = rooms.bedroom()
			if b == 7: # dining
				room1 = rooms.bedroom()



			#nn=n
			i = None
			j = 0
			k = 0
			l = []
			#c,d = abuf[0][0],abuf[0][0]
			#temp = []

			if ee == 1 or ee == 2:
				print c,d,xa,ya
				puppet.append((c*scale + translate,d*scale+ translate,xa*scale,ya*scale))      #this is it
			#	out.append((c,d,xa,ya))
				bbuf.append((c,d,xa,ya))

				abuf.append((c,d+ya))
				abuf.append((c+xa,d))
				abuf.pop(0)
				#print abuf
				c,d = abuf[0][0],abuf[0][1]

			else:
				if c+xa < w or d+ya < h:
					print "plan is huge than plot"
					break
				#tp.append(c,d,xa,ya)
				for bp in bbuf:
					a1 = xa/2
					a2 = c + a1
					#print bp[2]
					b1 = bp[2]
					b1 = b1/2
					b2 = bp[0] + b1

					c1 = ya/2
					c2 = d + c1
					d1 = bp[3]
					d1 = d1/2
					d2 = bp[1] + d1
					#print a1, a2,b1,b2,c1,c2,d1,d2
					error = 0
					#if (c+(xa/2))<(bp[0][0]+(bp[0][2]/2)) and (d+(ya/2))<(bp[0][1]+(bp[0][3]/2)):
					if  a2 < b2:
						error = 1
					if  c2 < d2:
						error = 1
				if error:
					print c,d,xa,ya
					puppet.append((c*scale+ translate,d*scale+ translate,xa*scale,ya*scale))                           #this is it
					out.append((c,d,xa,ya))
					bbuf.append((c,d,xa,ya))

					abuf.append((c,d+ya))
					abuf.append((c+xa,d))
					abuf.pop(0)
					#print c,d,xa,ya
					c,d = abuf[0][0],abuf[0][1]
			ee = 0

	return puppet		

def main():
	puppet = generateroom(3)
	print puppet

if __name__=="__main__":main()
	