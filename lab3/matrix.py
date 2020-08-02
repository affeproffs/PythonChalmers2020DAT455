def transpose(m):
    return m if not m else [[row[i] for row in m] for i in range(len(m[0]))]

def powers(lst, p1, p2):
    return [[v ** p for p in range(p1, p2 + 1)] for v in lst]

def sumLists(l1, l2):
    return sum([l1[i] * l2[i] for i in range(len(l1))])

def matmul(m1, m2):
    return [[sumLists(m1[r], [l[c] for l in m2]) for c in range(len(m2[0]))] for r in range(len(m1))]

def invert(m):
    det = m[0][0] * m[1][1] - m[0][1] * m[1][0]
    return [[m[1][1] / det, -m[0][1] / det], [-m[1][0] / det, m[0][0] / det]]

def loadtxt(fName):
    return [list(map(float, l.strip().split("\t"))) for l in open(fName)]
