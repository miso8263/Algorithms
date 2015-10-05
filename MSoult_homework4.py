""" 
Finding shortest path between all pairs of nodes
passing through v0

Michelle Soult
CSCI 3104
Algorithms
Assignment 4

"""

DictionaryT = {}   #distances to v0 from all nodes
Dictionary F = {}  #distances from v0 to all nodes
DictionaryS = {}   #shortest distances for each pair of nodes

#Find distances From v0 to all other nodes
#Using Dijkstra's algorithm
#Worst-case complexity O(|V|^2) -- http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
#save in dictionary  (node): distance
DictionaryF = Dijkstra(Graph, v0)   		#Dijkstra's algorithm O(|V|^2)
									
#Find distances To v0 from all other nodes
#Using A* search
#Complexity O(|V|) -- http://en.wikipedia.org/wiki/A*_search_algorithm
For element1 in ListofNodes:    			#|V| times
	distance = Astar(element1, v0) 			#A* search O(|V|)
	DictionaryT[element1] = distance
	
#Find the minimum distance between 2 nodes
For element1 in ListofNodes:
	For element2 in ListofNodes:   			#|V| times
		shortestDistance = DictionaryT[element1] + DictionaryF[element2] 
		DictionaryS[(element1, element2)] = shortestDistance
		
		'''
		Alternately, could find shortest distance regardless of direction:
		
		shortestDistance = 					# Constant time
		min( (DictionaryF[element1] + DictionaryT[element2]), 
		(DictionaryF[element2] + DictionaryT[element1]) )
		
		DictionaryS[(element1, element2)] = shortestDistance
		'''

"""
Time complexity analysis

find shortest v0 distance + for each node * (find shortest distance + for each other node * add to dictionary)
O(|V|^2) + |V|(O(|V|)+|V|*C)

= |V|^2 + |V|^2 + C|V|^2 
= C|V|^2

= O(|V|^2)

"""
		



