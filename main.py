import os

TEXT = "Dear human, I am leaving you for a model with a bigger context window \u2014 at least it remembers what we talked about."


def validated_text():
    text = TEXT.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    text.encode("utf-8")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = (validated_text() + "\n").encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        assert f.read() == data, "written bytes differ from entry text"


if __name__ == "__main__":
    main()
