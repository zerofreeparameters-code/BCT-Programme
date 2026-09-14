#!/usr/bin/env python3
"""Gate XI — census of the symbol xi across the pinned BCT corpus.
Distinguishes the scalar healing length from the (asserted) three-component
displacement field. Run against the extracted repo + extracted appendix text."""
import re, sys, os, unicodedata

def contexts(path, radius=55):
    t = open(path, encoding='utf-8', errors='replace').read()
    out=[]
    for m in re.finditer('ξ', t):
        a=max(0,m.start()-radius); b=min(len(t),m.start()+radius)
        out.append(' '.join(t[a:b].split()))
    return out

def classify(ctx):
    c=ctx.lower()
    if 'healing length' in c or 'coherence' in c or 'core' in c or '2.32' in c or '2.318' in c or '8πα' in c or '8pi' in c:
        return 'scalar: healing/coherence length'
    if 'displacement field' in c or 'ξi' in ctx or 'ξ_i' in ctx:
        return 'THREE-COMPONENT DISPLACEMENT FIELD'
    if 'conformal' in c or '1/6' in c:
        return 'scalar: conformal coupling'
    if 'flag' in c or 'δm' in c or 'δm' in ctx.lower():
        return 'scalar: lattice-QCD B-mixing parameter'
    if 'ξ_geom' in ctx or 'ξgeom' in c or 'casimir' in c:
        return 'scalar: Casimir/geometric coefficient'
    return 'unclassified (inspect)'

if __name__=='__main__':
    files=sys.argv[1:]
    tally={}
    for f in files:
        if not os.path.exists(f): continue
        for ctx in contexts(f):
            k=classify(ctx); tally[k]=tally.get(k,0)+1
    print("== xi occurrence classification across corpus ==")
    for k,v in sorted(tally.items(), key=lambda x:-x[1]):
        print(f"  {v:4d}  {k}")
