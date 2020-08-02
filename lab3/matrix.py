def transpose(m):
    return m if not m else [[row[i] for row in m] for i in range(len(m[0]))]

def powers(lst, p1, p2):
    return [[v ** p for p in range(p1, p2 + 1)] for v in lst]

def sumLists(l1, l2):
    return sum([l1[i] * l2[i] for i in range(len(l1))])

def matmul(m1, m2):
    return [[sumLists(m1[r], [l[c] for l in m2]) for c in range(len(m2[0]))] for r in range(len(m1))]




        
    
