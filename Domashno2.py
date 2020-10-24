ar = [ int(x) for x in input().split()]

smol = ar[0]
big = ar[0]
length = len(ar)



for x in range(length):

	if smol > ar[x]:

		smol = ar[x]

	if big < ar[x]:

		big = ar[x]

print(big - smol)