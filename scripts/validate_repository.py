"""Validate the curriculum inventory and file contracts without network access."""
from pathlib import Path
import ast
import json
import re
ROOT=Path(__file__).resolve().parents[1]
REQUIRED=('app.py','requirements.txt','.env.example','.gitignore','README.md','INSTRUCTIONS.md','EXPLANATION.md','EXERCISES.md','EXAM_NOTES.md','TROUBLESHOOTING.md','tests/test_app.py','sample_data/examples.json')

def validate():
    inventory=json.loads((ROOT/'docs/PROJECT_STATUS.json').read_text())
    errors=[];seen=set();files=0
    if len(inventory)!=65:errors.append('Inventory must contain 65 projects.')
    for item in inventory:
        path=item['path'];folder=(ROOT/path).resolve()
        if not folder.is_relative_to(ROOT) or path in seen:errors.append('Unsafe/duplicate project path: '+path);continue
        seen.add(path)
        for name in REQUIRED:
            p=folder/name
            if not p.is_file() or not p.read_text().strip():errors.append(path+': missing/empty '+name)
        for p in folder.rglob('*.py'):
            if any(part in ('.venv','__pycache__','.local') for part in p.parts):continue
            files+=1
            try:ast.parse(p.read_text(),filename=str(p))
            except SyntaxError as exc:errors.append(str(exc))
            if re.search(r'sk-[A-Za-z0-9]{25,}',p.read_text()):errors.append('Possible hardcoded credential in '+str(p))
        samples=json.loads((folder/'sample_data/examples.json').read_text())
        if len(samples)<3:errors.append(path+': fewer than three sample interactions')
    for number in (1,2,3):
        questions=json.loads((ROOT/f'04_Certification_Preparation/Mock_Exam_{number:02}/exam.json').read_text())
        for domain in ('Building','Testing','Deploying','Monitoring'):
            if sum(q['domain']==domain for q in questions)!=10:errors.append(f'Exam {number} weighting error for {domain}')
        for q in questions:
            if len(q['options'])!=4 or set(q['explanations'])!=set('ABCD'):errors.append('Incomplete question '+q['id'])
            if not (ROOT/q['project']/'app.py').is_file():errors.append('Missing practice project '+q['id'])
    if errors:raise SystemExit('\n'.join(errors))
    print(f'Validated {len(inventory)} project file contracts, {files} Python files, and 120 practice questions.')

if __name__=='__main__':validate()
