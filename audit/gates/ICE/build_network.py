#!/usr/bin/env python3
"""
GATE ICE - Step 0: build the FCC void network cold, from geometry only.
FCC (== BCT at c/a=sqrt(2)) atoms; nodes = octahedral + tetrahedral voids;
edges = shared triangular windows (3 common bounding atoms).
Deterministic. No inherited numbers.
"""
import numpy as np
from itertools import product, combinations

a = 1.0
N = 5                      # conventional cells per side
tol = 1e-6

def key(p): return tuple(np.round(p, 6))

# --- FCC atoms ---
fcc = [(0,0,0),(0.5,0.5,0),(0.5,0,0.5),(0,0.5,0.5)]
atoms = set()
for i,j,k in product(range(-1, N+2), repeat=3):
    for b in fcc:
        p = (i+b[0], j+b[1], k+b[2])
        atoms.add(key(p))
atoms = np.array(sorted(atoms))

# --- octahedral voids: FCC-type set with a point at (1/2,1/2,1/2) ---
octb = [(0.5,0.5,0.5),(0.5,0,0),(0,0.5,0),(0,0,0.5)]
octs = set()
for i,j,k in product(range(N+1), repeat=3):
    for b in octb:
        p = (i+b[0], j+b[1], k+b[2])
        octs.add(key(p))

# --- tetrahedral voids: coords in {1/4,3/4} mod 1 (SC lattice, spacing 1/2) ---
tets = set()
for i,j,k in product(range(N), repeat=3):
    for b in product([0.25,0.75], repeat=3):
        p = (i+b[0], j+b[1], k+b[2])
        tets.add(key(p))

octs = np.array(sorted(octs)); tets = np.array(sorted(tets))
print(f"atoms={len(atoms)}  oct candidates={len(octs)}  tet candidates={len(tets)}")

# atom lookup via KD-ish brute (small block)
from scipy.spatial import cKDTree
atree = cKDTree(atoms)

def bounding_atoms(center, kind):
    """Return frozenset of atom-keys forming the void's coordination shell."""
    ndist, nidx = atree.query(center, k=12)
    ndist = np.round(ndist, 6)
    if kind == 'oct':
        r = ndist[0]                      # expect 0.5
        sel = [atoms[i] for i,d in zip(nidx,ndist) if abs(d-r)<tol]
        return frozenset(key(atoms[i]) for i,d in zip(nidx,ndist) if abs(d-r)<tol), r, len(sel)
    else:
        r = ndist[0]                      # expect sqrt(3)/4
        sel = [i for i,d in zip(nidx,ndist) if abs(d-r)<tol]
        return frozenset(key(atoms[i]) for i in sel), r, len(sel)

# characterise coordination (only interior voids to avoid truncation)
def interior(c, m=1.0, M=None):
    M = N-1.0 if M is None else M
    return all(m-tol <= x <= M+tol for x in c)

oct_atoms = {}; oct_r=None; oct_nc=[]
for c in octs:
    if not interior(c): continue
    fs, r, n = bounding_atoms(c,'oct'); oct_atoms[key(c)] = fs; oct_r=r; oct_nc.append(n)
tet_atoms = {}; tet_r=None; tet_nc=[]
for c in tets:
    if not interior(c): continue
    fs, r, n = bounding_atoms(c,'tet'); tet_atoms[key(c)] = fs; tet_r=r; tet_nc.append(n)

print(f"oct coordination radius={oct_r} (expect 0.5), #atoms/oct={set(oct_nc)} (expect 6)")
print(f"tet coordination radius={round(tet_r,6)} (expect {round(3**0.5/4,6)}), #atoms/tet={set(tet_nc)} (expect 4)")

# --- adjacency: shared triangular window = exactly 3 common bounding atoms ---
nodes = list(oct_atoms.keys()) + list(tet_atoms.keys())
kindof = {**{k:'oct' for k in oct_atoms}, **{k:'tet' for k in tet_atoms}}
allsets = {**oct_atoms, **tet_atoms}
pos = {k:np.array(k) for k in nodes}

# only oct-tet pairs within plausible range
octkeys=list(oct_atoms); tetkeys=list(tet_atoms)
otree = cKDTree(np.array(octkeys)); ttree=cKDTree(np.array(tetkeys))
pairs = otree.query_ball_tree(ttree, r=0.6)   # oct-tet face distance ~0.433
edges=set()
for oi, tlist in enumerate(pairs):
    ok = octkeys[oi]
    for tj in tlist:
        tk = tetkeys[tj]
        common = allsets[ok] & allsets[tk]
        if len(common)==3:
            edges.add((ok,tk))
# also check for any oct-oct or tet-tet windows (should be none)
oo=0
for i,j in combinations(range(len(octkeys)),2):
    if len(allsets[octkeys[i]] & allsets[octkeys[j]])==3: oo+=1
tt=0
tkl=tetkeys
tt_tree=ttree.query_ball_tree(ttree, r=0.6)
for i,tl in enumerate(tt_tree):
    for j in tl:
        if j>i and len(allsets[tkl[i]] & allsets[tkl[j]])==3: tt+=1
print(f"oct-oct 3-common windows={oo}, tet-tet 3-common windows={tt} (expect 0,0)")

# degrees for FULLY interior nodes (all neighbours present)
from collections import defaultdict
adj=defaultdict(set)
for u,v in edges:
    adj[u].add(v); adj[v].add(u)

def deep_interior(c): return interior(c, m=1.5, M=N-1.5)
oct_deg=[len(adj[k]) for k in oct_atoms if deep_interior(np.array(k))]
tet_deg=[len(adj[k]) for k in tet_atoms if deep_interior(np.array(k))]
print(f"oct degrees (deep interior): {sorted(set(oct_deg))}  count={len(oct_deg)}  (expect 8)")
print(f"tet degrees (deep interior): {sorted(set(tet_deg))}  count={len(tet_deg)}  (expect 4)")

# per-cell topology from degree sum
Voct, Vtet = 4, 8
Vcell = Voct+Vtet
Ecell = (Voct*8 + Vtet*4)//2
b1 = Ecell - Vcell + 1
print(f"\nPER CONVENTIONAL CELL:  V={Vcell} (4 oct + 8 tet)  E={Ecell}  C=1  b1=E-V+C={b1}")
print(f"b1 per node = {b1/Vcell:.4f}")

# --- girth + shortest-cycle count on the deep-interior graph ---
import collections
core = [k for k in nodes if deep_interior(np.array(k))]
coreset=set(core)
def bfs_shortest_cycle_through(u):
    # shortest cycle containing u, standard BFS with parent tracking
    best=10**9
    dist={u:0}; par={u:None}
    dq=collections.deque([u])
    while dq:
        x=dq.popleft()
        for y in adj[x]:
            if y not in dist:
                dist[y]=dist[x]+1; par[y]=x; dq.append(y)
            elif par[x]!=y:
                c=dist[x]+dist[y]+1
                best=min(best,c)
    return best
girth = min(bfs_shortest_cycle_through(u) for u in core if len(adj[u])>0)
print(f"girth (deep interior) = {girth}")

# count shortest (girth) loops touching one interior body-centre oct, per cell
# enumerate simple cycles of length == girth around a reference oct at (2.5,2.5,2.5)
ref = key((N//2+0.5, N//2+0.5, N//2+0.5))
def cycles_of_len(start, L):
    found=set()
    def dfs(path):
        if len(path)==L:
            if start in adj[path[-1]]:
                cyc=tuple(sorted(path))
                found.add(cyc)
            return
        for y in adj[path[-1]]:
            if y in path: continue
            dfs(path+[y])
    dfs([start])
    return found
g4 = cycles_of_len(ref, girth)
print(f"shortest ({girth}-)loops through one octahedral void = {len(g4)}")
# shortest loops through one tet void
reft = key((N//2+0.25, N//2+0.25, N//2+0.25))
g4t = cycles_of_len(reft, girth)
print(f"shortest ({girth}-)loops through one tetrahedral void = {len(g4t)}")

# connectivity check
seen=set(); comp=0
for k in nodes:
    if k in seen: continue
    comp+=1; st=[k]
    while st:
        x=st.pop()
        if x in seen: continue
        seen.add(x)
        st.extend(adj[x]-seen)
print(f"connected components of block graph = {comp} (expect 1)")
