#!/usr/bin/env python3
"""
Gate BULK — prints every source line cited in the Q1 ledgers of gate_BULK_RESULT.md, from the pinned
files at commit 9582c54b6f22fc78eee0dc356f6d49cdfadd68b3, after re-verifying their SHA-256.
Usage:  python3 bulk_ledger_cites.py /path/to/checkout-of-9582c54
(The PDF is extracted with `pdftotext -layout`; page N below = N-th form-feed-separated page of that
extraction, whose printed folio is also N for the pages cited here.)
"""
import sys, hashlib, pathlib, subprocess, tempfile
root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
PIN = {
 'tex/BCT_Appendix_AZ6.tex':          '7495750530f385e74d0d9ef00286939cc7244f468f49d941c039005e004677e7',
 'tex/BCT_Letter20_GR_AllOrders.tex': '4e2a625c64eec455fddcd0706d5b9868cbbc33092f1992b55b95ee0fb34d7ed5',
 'tex/BCT_Appendix_AZ7.tex':          'ef27d5dea9c5104791919b24431859d2965a0c98e7f4b6b6f079e51b25280476',
 'tex/BCT_Letter27_GPAxiom.tex':      'd15dbf6c6949a3a2f51e187525c4e49193478de845967f1cb77247d2aa81270e',
 'BCT_Volume1_Foundations.tex':       '5787bd00ced79bffadd82369ce60e11985facee64144e1da469ec1979fe5dde3',
 'BCT_Appendices_Volume1_2026_compressed_Part1.pdf': '6e14b6c0183d089c8b1f56701878addef43f9b21d4533ddf5dccf464a00dbb8b',
}
ok = True
for f, h in PIN.items():
    d = hashlib.sha256((root/f).read_bytes()).hexdigest()
    print(f"{'OK ' if d == h else 'BAD'} {f}")
    ok &= (d == h)
if not ok:
    sys.exit("hash mismatch: stop")

CITES = {  # file -> list of (first, last) line numbers (1-based, inclusive)
 'tex/BCT_Appendix_AZ6.tex': [(91,92),(139,142),(168,169),(209,209),(261,261),(310,310),(353,354),(362,362),(373,374),(393,399)],
 'tex/BCT_Letter20_GR_AllOrders.tex': [(96,97),(137,141),(226,231),(233,242),(311,319),(433,437),(441,443)],
 'tex/BCT_Appendix_AZ7.tex': [(108,109),(112,113),(154,170)],
 'tex/BCT_Letter27_GPAxiom.tex': [(60,62),(68,69),(75,80)],
 'BCT_Volume1_Foundations.tex': [(209,215)],
}
for f, spans in CITES.items():
    lines = (root/f).read_text(encoding='utf-8').split('\n')
    print(f"\n######## {f}")
    for a, b in spans:
        print(f"--- L{a}-{b}")
        for i in range(a, b+1):
            print(f"{i:4d}| {lines[i-1]}")

PDF = root/'BCT_Appendices_Volume1_2026_compressed_Part1.pdf'
with tempfile.TemporaryDirectory() as td:
    out = pathlib.Path(td)/'p1.txt'
    subprocess.run(['pdftotext', '-layout', str(PDF), str(out)], check=True)
    pages = out.read_text(encoding='utf-8', errors='replace').split('\f')
PCITES = {  # page -> list of (first,last) line numbers within the page (non-blank lines kept as-is)
 49: [(41,46)], 72: [(5,36)], 120: [(40,41)], 121: [(1,2),(11,11)], 20: [(9,11)],
 265: [(3,8),(22,34)], 273: [(5,12),(18,32)], 274: [(21,31)], 269: [(1,999)],
}
for p, spans in PCITES.items():
    lines = pages[p-1].split('\n')
    print(f"\n######## PDF page {p} (printed folio: see last line)")
    for a, b in spans:
        print(f"--- p{p} L{a}-{min(b,len(lines))}")
        for i in range(a, min(b, len(lines))+1):
            if p == 269 and 'K_BCT' not in lines[i-1]:   # p269: only the Koide symbol-collision line
                continue
            print(f"{i:4d}| {lines[i-1].rstrip()}")
