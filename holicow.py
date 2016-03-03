__author__ = 'Shweta Yakkali'
__author__ = 'Aishwarya Desai'

"""
CSCI-603: Graphs

An implementation of a graphs where 1 paintball will trigger the other within its radius and this results in a cow within that radius being painted

"""

from math import sqrt
from graph import Graph
from vertex import Vertex
from sys import argv

class Holicow:
    """
    A graph implemented as an adjacency list of vertices.

    :slot: cownames (dict):  A dictionary that contains all the cow names with their values(x & y value)
    :slot: paintball (dict): A dictionary that contains all the colours names with their values(x y & radius)
    :slot: graph : Create an empty graph with no nodes and no edges.
    :slot: nodelist (dict): A dictionary that contains all the cows and paintballs with their values
    """
    __slots__ ='cownames','paintball','graph','nodelist'

    def __init__(self, filename):
     """
     Initialize the graph
     :param filename: The name of the file
     :return: None
     """
     self.cownames={}
     self.paintball={}
     self.graph = Graph()
     self.nodelist={}

     with open(filename) as file:
            for line in file:
                if len(line) > 0 and line[0] != '#':
                    fields = line.split()
                    if fields[0]=='cow':
                        vertex=Vertex(fields[1])
                        self.graph.vertList[fields[1]]=vertex
                        self.nodelist[fields[1]]=[fields[2],fields[3]]
                        self.cownames[fields[1]]=[fields[2],fields[3]]

                    else:
                        vertex=Vertex(fields[1])
                        self.graph.vertList[fields[1]]=vertex
                        self.nodelist[fields[1]]=[fields[2],fields[3],fields[4]]
                        self.paintball[fields[1]]=[fields[2],fields[3],fields[4]]


     self.makeTheGraph()

    def makeTheGraph(self):
        """
        Graph gets created here.
        :return: None
        """
        for ball in self.paintball:
            templist=self.paintball[ball]
            x1=int(templist[0])
            y1=int(templist[1])
            radius=int(templist[2])
            for node in self.nodelist:
                if node in self.cownames:
                    tempcowlist=self.cownames[node]
                    x2=int(tempcowlist[0])
                    y2=int(tempcowlist[1])

                    if radius>= sqrt(abs(pow(abs((x1)-(x2)),2)+(pow(abs((y1)-(y2)),2)))):
                         self.graph.addEdge(ball,node)
                else:
                    if(node!=ball):
                        tempcowlist=self.paintball[node]
                        x2=int(tempcowlist[0])
                        y2=int(tempcowlist[1])
                        if radius>= sqrt(abs(pow(abs((x1)-(x2)),2)+(pow(abs((y1)-(y2)),2)))):
                                 self.graph.addEdge(ball,node)

        print('Field of Dreams')
        print('---------------')

        for key in self.graph:
            print(key)

        self.trigger()

    def optimal(self,maxnode):
        """
        Which is the optimal paintball and each cow is coloured in which color is calculated here
        :param maxnode: The paintabll which paints the max number of cows
        :return: None
        """
        resultdict={}
        for cow in self.cownames:
            resultdict[cow]=[]

        self.dictfinder(resultdict,maxnode)

    def dictfinder(self,resultdict,maxnode):
        """
        Each cow is coloured in which color is displayed with this method
        :param resultdict(dict):Contains all the cows with the color they get painted in
        :param maxnode: The paintabll which paints the max number of cows
        :return: None
        """
        for node in self.graph:
            if node==maxnode:
                connected=[str(x.id) for x in node.connectedTo]
                for x in connected:
                    if x in self.cownames:
                        resultdict[x].append(maxnode.id)

                    else:
                        self.dictfinder2(x,resultdict)


        self.displaydictionary(resultdict)


    def dictfinder2(self,x,resultdict):
        """
        Each cow is coloured in which color is displayed with this method similar to the dictfinder
        :param resultdict(dict):Contains all the cows with the color they get painted in
        :param x:
        :return: None
        """
        for node in self.graph:
            if node.id==x:
                connected=[str(x.id) for x in node.connectedTo]
                for acow in connected:
                    if acow in self.cownames:
                        resultdict[acow].append(x)

                    else:
                        self.dictfinder2(acow,resultdict)


    def displaydictionary(self,resultdict):
        """
        This displays the cows affected by the paintball which was the best choice
        :param resultdict(dict):Contains all the cows with the color they get painted in
        :return: None
       """
        for key in resultdict:
            s=set(resultdict[key])
            if not s:
                print(key,"'s colors: ",'{}')
            else:
                print(key,"'s colors: ", set(resultdict[key]))


    def results(self):
        """
        This displays the the paintball which was the best choice

        :return: None
       """
        maximum=0
        maxnode=Vertex(None)
        print('Results:')

        for node in self.graph:

            if node.id in self.paintball:

                if(maximum<=node.counter):
                    #print(node.id,'    ',node.counter)
                    maximum=node.counter
                    maxnode=node

        '''if(node.counter==0):
            maxnode=node'''
        if(maximum>0):
            print('Triggering the',maxnode.id,'paint ball is the best choice with',maximum,'total paint on the cows:')
            self.optimal(maxnode)
        else:
            print('None of the cows were painted by any starting ball!')


    def trigger(self):
        """
        Displays which paintball is triggered by which paintball.
        :return: None
        """
        print('Beginning simulation. . .')

        for node in self.graph:
            if (node.id) in self.paintball:
                print('Triggering',node.id,'paint ball. . .')
                connections=[str(x.id) for x in node.connectedTo]
                for name in connections:
                    if name in self.cownames:
                        print('       ',name,'is painted ',node.id,'!')
                        node.counter=node.counter+1
                    else:

                        print('       ',name,'paint ball is triggerred by',node.id,'paint ball')
                        self.simulate(name,node)

        self.results()

    def simulate(self,name1,node):
        """
        If a cow comes within the radius of the paintball then this cow will get painted
        :param name1:The value of name got from the trigger
        :param node: The paintabll and what it is connected to
        :return: None
        """
        for a in self.graph:
            if a.id==name1:
                newlist=[str(x.id) for x in a.connectedTo]
                for item in newlist:
                    if item in self.cownames:
                        print('       ',item,'is painted ',a.id,'!')
                        node.counter=node.counter+1
                    else:
                        print('       ',item,'paint ball is triggerred by',a.id,'paint ball')
                        #self.simulate(name,a)
                        self.simulate(item,node)




def main():
    """
    The main function prompts for the file name and enters the
    main loop.
    :return: None
    """
    if len(argv)!=2:
        print('Usage: python3 holicow.py source-file.in')
    try:
        #filename=input('Enter filename: ')
        holicow = Holicow(argv[1])

    except IOError as err:  # if error with file name
        print('File not found: {',argv[1],'}')

if __name__ == '__main__':
    main()



