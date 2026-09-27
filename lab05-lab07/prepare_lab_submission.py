from pathlib import Path
import zipfile
EXCLUDE={".git","__pycache__",".ipynb_checkpoints","data","datasets"}
def main():
    root=Path(__file__).resolve().parent; out=root/"computer_vision_lab_code.zip"
    with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED) as z:
        for p in root.rglob("*"):
            if p.is_file() and p!=out and not any(x in EXCLUDE for x in p.parts) and p.suffix.lower() in {".py",".ipynb",".pyx",".sh",".txt",".md"}: z.write(p,p.relative_to(root))
    print(f"Created: {out}")
if __name__=="__main__": main()
