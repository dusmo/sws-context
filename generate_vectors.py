#!/usr/bin/env python
"""Genera context/vectors.json.gz a partire da sws_context.txt.
Richiede: pip install sentence-transformers
"""
import pathlib, json, gzip, textwrap
from sentence_transformers import SentenceTransformer

CTX_PATH = pathlib.Path(__file__).parent / "context" / "sws_context.txt"
OUT_PATH = pathlib.Path(__file__).parent / "context" / "vectors.json.gz"
CHUNK_SIZE = 400  # caratteri


def chunk_text(text, size):
    for i in range(0, len(text), size):
        yield text[i : i + size]


def main():
    if not CTX_PATH.exists():
        raise SystemExit("sws_context.txt mancante; esegui prima generate_context.py")

    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    txt = CTX_PATH.read_text(encoding="utf-8")
    chunks = list(chunk_text(txt, CHUNK_SIZE))
    embs = model.encode(chunks, batch_size=32, normalize_embeddings=True)

    data = [{"text": t, "vec": e.tolist()} for t, e in zip(chunks, embs)]
    OUT_PATH.parent.mkdir(exist_ok=True)
    with gzip.open(OUT_PATH, "wt", encoding="utf-8") as f:
        json.dump(data, f)

    print("vectors salvato in", OUT_PATH)


if __name__ == "__main__":
    main() 