from pathlib import Path


def test_no_private_absolute_paths():
    root = Path(__file__).resolve().parents[1]
    mac_home = "/" + "Users/"
    remote_home = "/" + "home/" + "saop/"
    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() in {".svg", ".zip"}:
            continue
        text = path.read_text(errors="ignore")
        assert mac_home not in text
        assert remote_home not in text
