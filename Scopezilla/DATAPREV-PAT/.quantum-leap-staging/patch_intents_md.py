#!/usr/bin/env python3
"""Patch the '### 5. Acceptance' body of each intent block in the rendered
11-intents-*.md bundle files to match data/intents.json — without a full
quantum-leap re-render (which would revert the hand-done PT-BR localization on
00/04/10-phase-*/92). Idempotent: matches intent blocks by their '## INT-NNN'
header; only touches the acceptance paragraph, nothing else."""
import json, pathlib, re, sys

PROJ = pathlib.Path("/Users/nfilho/claude/Scopezilla/DATAPREV-PAT")
BUNDLE = PROJ / "outputs" / "quantum-leap"
INTENTS = PROJ / "data" / "intents.json"

data = json.loads(INTENTS.read_text(encoding="utf-8"))
acc_by_id = {i["id"]: (i.get("acceptance") or "").strip() for i in data["intents"]}

# Split a file into intent blocks on the '## INT-NNN' header (keep the header).
block_re = re.compile(r"(?=^## INT-\d+ )", re.MULTILINE)
id_re = re.compile(r"^## (INT-\d+) ", re.MULTILINE)
# Acceptance body: from the heading + blank line, up to the next '### ' or '---'.
acc_re = re.compile(r"(### 5\. Acceptance\n\n)(.*?)(\n\n(?:### |---))", re.DOTALL)

patched, files_changed = [], []
for md in sorted(BUNDLE.glob("11-intents-*.md")):
    text = md.read_text(encoding="utf-8")
    parts = block_re.split(text)
    changed = False
    for idx, part in enumerate(parts):
        m = id_re.match(part)
        if not m:
            continue
        iid = m.group(1)
        if iid not in acc_by_id:
            continue
        new_acc = acc_by_id[iid]

        def _sub(mm):
            return mm.group(1) + new_acc + mm.group(3)

        new_part, n = acc_re.subn(_sub, part, count=1)
        if n != 1:
            print(f"WARN: no acceptance section matched for {iid} in {md.name}", file=sys.stderr)
            continue
        if new_part != part:
            parts[idx] = new_part
            changed = True
            patched.append(iid)
    if changed:
        md.write_text("".join(parts), encoding="utf-8")
        files_changed.append(md.name)

print(f"patched {len(patched)} intent acceptances across {len(files_changed)} files")
print("files:", ", ".join(files_changed))
print("intents:", ", ".join(sorted(patched)))
