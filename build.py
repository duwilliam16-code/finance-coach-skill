"""Package the finance-coach skill folder into dist/finance-coach.zip."""
import pathlib
import zipfile

ROOT = pathlib.Path(__file__).parent
SKILL = ROOT / "finance-coach"
OUT = ROOT / "dist" / "finance-coach.zip"


# Zip the skill folder so every entry starts with "finance-coach/",
# which is the layout claude.ai requires for an uploaded skill.
def build():
    OUT.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(SKILL.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(ROOT).as_posix())
    print(f"Built {OUT}")


if __name__ == "__main__":
    build()
