#!/usr/bin/env python3
# GATE ICE - STEP 0: FCC (c/a=sqrt2) void network built COLD.
# Deterministic. Nodes = octahedral+tetrahedral voids; edges = shared triangular windows (=shared FACE = 3 common bounding atoms).
# No inheritance: geometry, adjacency, girth, cycle rank all derived here.
import itertools, numpy as np
from collections import defaultdict, deque

L = 3  # LxLxL conventional cubic cells, periodic
def wrap(v): return tuple(round((x % L),6) for x in v)

# --- FCC atoms (conventional cell basis, 4 atoms) ---
atom_basis = [(0,0,0),(0.5,0.5,0),(0.5,0,0.5),(0,0.5,0.5)]
atoms=set()
for i,j,k in itertools.product(range(L),repeat=3):
    for b in atom_basis:
        atoms.add(wrap((b[0]+i,b[1]+j,b[2]+k)))
atoms=sorted(atoms)
atom_set=set(atoms)

# --- Octahedral voids: body centre + edge centres ---
oct_basis=[(0.5,0.5,0.5),(0.5,0,0),(0,0.5,0),(0,0,0.5)]
# --- Tetrahedral voids: (1/4,3/4)^3, 8 per cell ---
tet_basis=[(x,y,z) for x in (0.25,0.75) for y in (0.25,0.75) for z in (0.25,0.75)]

def build(basis,tag):
    d={}
    for i,j,k in itertools.product(range(L),repeat=3):
        for b in basis:
            p=wrap((b[0]+i,b[1]+j,b[2]+k)); d[p]=tag
    return d
oct_v=build(oct_basis,'O'); tet_v=build(tet_basis,'T')
voids={**oct_v,**tet_v}
V=sorted(voids); vidx={p:n for n,p in enumerate(V)}
nO=sum(1 for p in V if voids[p]=='O'); nT=len(V)-nO
print(f"cells L^3={L**3}  atoms={len(atoms)}  voids V={len(V)}  (O={nO}, T={nT})")
print(f"per cell: V={len(V)/L**3:.3f}  O={nO/L**3:.3f}  T={nT/L**3:.3f}")

# bounding atoms of a void = the atoms at the void's coordination distance (min-image)
def dist2(a,b):
    d=[min(abs(a[i]-b[i]),L-abs(a[i]-b[i])) for i in range(3)]
    return sum(x*x for x in d)
def bounding(p):
    ds=sorted((dist2(p,a),a) for a in atoms)
    dmin=ds[0][0]
    return frozenset(a for d,a in ds if abs(d-dmin)<1e-9)
bnd={p:bounding(p) for p in V}
# sanity: O bounded by 6 atoms, T by 4
from collections import Counter
print("bounding-atom counts:",Counter(len(bnd[p]) for p in V), "(expect O:6, T:4)")

# EDGE = two voids sharing a triangular FACE = exactly 3 common bounding atoms
adj=defaultdict(set)
for a,b in itertools.combinations(V,2):
    if len(bnd[a]&bnd[b])>=3:
        adj[a].add(b); adj[b].add(a)
E=sum(len(adj[p]) for p in V)//2
print(f"edges E={E}  per cell={E/L**3:.3f}")

# degrees by type
degO=Counter(len(adj[p]) for p in V if voids[p]=='O')
degT=Counter(len(adj[p]) for p in V if voids[p]=='T')
print("O degrees:",dict(degO)," T degrees:",dict(degT))

# edge-type breakdown
et=Counter()
for a in V:
    for b in adj[a]:
        if vidx[a]<vidx[b]:
            et[tuple(sorted((voids[a],voids[b])))]+=1
print("edge types:",dict(et))

# connected components + bipartite test
seen=set(); comps=0; bip=True; color={}
for s in V:
    if s in seen: continue
    comps+=1; color[s]=0; q=deque([s]); seen.add(s)
    while q:
        u=q.popleft()
        for w in adj[u]:
            if w not in color:
                color[w]=color[u]^1; seen.add(w); q.append(w)
            elif color[w]==color[u]:
                bip=False
print(f"components C={comps}  bipartite={bip}")

# cycle rank of the periodic (torus) quotient graph, per cell
b1=E-len(V)+comps
print(f"b1 = E-V+C = {b1}  per cell={b1/L**3:.3f}")

# GIRTH + count of shortest cycles (BFS from each node)
def girth_and_count():
    g=10**9
    for s in V:
        dst={s:0}; par={s:None}; q=deque([s])
        while q:
            u=q.popleft()
            for w in adj[u]:
                if w not in dst:
                    dst[w]=dst[u]+1; par[w]=u; q.append(w)
                elif par[u]!=w:
                    c=dst[u]+dst[w]+1
                    if c<g: g=c
    return g
girth=girth_and_count()
print(f"girth = {girth}")

# count shortest cycles of length = girth (undirected simple), then per cell
def count_cycles(Lc):
    cyc=set()
    for s in V:
        # DFS depth <= Lc
        stack=[(s,[s])]
        while stack:
            u,path=stack.pop()
            if len(path)>Lc: continue
            for w in adj[u]:
                if w==s and len(path)==Lc:
                    cyc.add(frozenset(path))
                elif w not in path and len(path)<Lc:
                    stack.append((w,path+[w]))
    return len(cyc)
ncyc=count_cycles(girth)
print(f"shortest ({girth}-)cycles total={ncyc}  per cell={ncyc/L**3:.3f}")
