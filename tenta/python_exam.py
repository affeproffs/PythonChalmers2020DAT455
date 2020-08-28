# Jag bekräftar härmed att jag inte kommunicerar med andra personer än kursens lärare
# under tentans gång.
# Jag är medveten om att fusk i tentan kan leda till disciplinåtgärder.

def movieTickets():
    tickets = int(input("Hur många biljetter vill du köpa? "))
    teens = int(input("Hur många av er är under 18 år? "))
    start = int(input("Vilken föreställning (ange klockslag i hela timmar)? "))
    return int(((tickets - teens) * 100 + teens * 50) * (0.9 if start < 18 else 1))

def pepLineLength(filename):
    longLines = 0
    for i, line in enumerate(open(filename)):
        if(len(line) > 79):
            longLines += 1
            print("line", i + 1, "too long:", len(line) - 1)
    print(longLines, "lines are too long")

class Tree:
    def __init__(self,node,trees):
        self.root = node
        self.subtrees = trees
        
    def getParts(self):
        return self.root, self.subtrees

def preorder(tree):
    nodes = [tree.root]
    for node in tree.subtrees:
        nodes += preorder(node)
    return nodes

def postorder(tree):
    nodes = []
    for node in tree.subtrees:
        nodes += postorder(node)
    return nodes + [tree.root]

royal = Tree('CarlGustaf',
             [Tree("Victoria", [Tree("Estelle", []), Tree("Oscar", [])]),
              Tree("CarlPhilip", [Tree("Alexander", [])]),
              Tree("Madeleine", [Tree("Leonore", []), Tree("Nicolas", [])])
             ])
