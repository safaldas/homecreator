import numpy as np
import sys
import math

abuf = []
bbuf = []
pc = []
puppet =[]
scale = 30

def generateroom(n):

	xa = 0
	ya = 0
	m=0
	ee = 0
	#w = int(input("enter width along x axis : "))		# plot width
	#h = int(input("enter height along y axis : "))		# plot height
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
				xa = 6
				ya = 5
			if b == 1:	# kitchen
				xa = 5
				ya = 4
			if b == 2:	# bathroom
				xa = 2
				ya = 2
			if b == 3:	# bedroom2
				xa = 3
				ya = 2
			if b == 4:	# living space
				xa = 6
				ya = 5
			if b == 5:	# another bed space
				xa = 5
				ya = 5
			if b == 6: # car porch
				xa == 5
				ya == 3
			if b == 7: # dining
				xa = 5
				ya = 5



			#nn=n
			i = None
			j = 0
			k = 0
			l = []
			#c,d = abuf[0][0],abuf[0][0]
			#temp = []

			if ee == 1 or ee == 2:
				print c,d,xa,ya
				puppet.append((c*scale,d*scale,xa*scale,ya*scale))                           #this is it
			#	out.append((c,d,xa,ya))
				bbuf.append((c,d,xa,ya))

				abuf.append((c,d+ya))
				abuf.append((c+xa,d))
				abuf.pop(0)
				#print abuf
				c,d = abuf[0][0],abuf[0][1]

			else:
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
					puppet.append((c*scale,d*scale,xa*scale,ya*scale))                           #this is it
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
	