"""
Gate DL-BETA P50R -- assembles gate_DLBETA_P50R_RESULT.md from the prose sections and the generated tables, so
that no number is retyped. Written after the verdict. Computes nothing: every figure comes from OUT/tables.md,
OUT/analysis.json, OUT/verdict.txt or OUT/state.json.
Usage: python3 -I dlbpr_assemble.py OUTDIR PROSE_DIR P50_ANALYSIS_JSON > gate_DLBETA_P50R_RESULT.md
"""
import json, os, sys


def main(out, prose, p50_json):
    t = open(os.path.join(out, "tables.md")).read()

    def between(a, b):
        i = t.index(a)
        j = t.index(b) if b else len(t)
        return t[i:j].rstrip() + "\n"

    parts = {
        "KTABLE": between("## K table", "### z4_8:").replace("## K table\n", ""),
        "LATTICES": between("### z4_8:", "**Integrity margins.**"),
        "MARGINS": between("**Integrity margins.**", "## Extrapolations"),
        "EXTRAP": between("## Extrapolations", "## Diagnostics (Q5)").replace("## Extrapolations\n", ""),
        "DIAG": between("## Diagnostics (Q5)", "## Appendix A").replace("## Diagnostics (Q5)\n", ""),
        "APPA": between("## Appendix A", "## Timing").replace("## Appendix A — every mixed chain\n", ""),
        "TIMING": between("## Timing", None).replace("## Timing\n", ""),
    }
    parts["VERDICT"] = open(os.path.join(out, "verdict.txt")).read().rstrip()
    parts["CROSSCHECK"] = open(os.path.join(out, "crosscheck_output.txt")).read().rstrip()
    parts["NUMHASH"] = open(os.path.join(out, "dlbpr_numbers.sha256")).read().split()[0]
    parts["HASHED_AT"] = open(os.path.join(out, "dlbpr_numbers_hashed_at.txt")).read().strip()
    parts["VERDICT_AT"] = open(os.path.join(out, "verdict_run_at.txt")).read().strip()

    body = open(os.path.join(prose, "RESULT_prose.md")).read()
    for k, v in parts.items():
        body = body.replace("{{" + k + "}}", v.rstrip())
    sys.stdout.write(body)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
