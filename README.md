
# 📁 Adobe India Hackathon 2025 (Rounds 1A & 1B)

This repository contains two modular, lightweight, and containerized solutions developed for Adobe’s *Persona-Driven Document Intelligence Hackathon*. Each round targets a unique document understanding task under strict resource constraints (≤1GB Docker image, ≤60s runtime).

---

## 🚀 Challenge Summary

| Round | Task Description | Key Capabilities |
|-------|------------------|------------------|
| **1A** | PDF Outline Extraction | Extracts structured title and headings (H1, H2, H3) with page numbers |
| **1B** | Persona-Based Section Relevance | Ranks relevant sections based on persona and job-to-be-done using ONNX |

---

## 🧩 Directory Structure

```
Adobe-India-Hackathon25/
├── challenge_1a/                  # Round 1A: PDF Outline Extractor
│   ├── app/
│   ├── input/
│   ├── output/
│   ├── Dockerfile
│   └── README.md
│
├── challenge_1b/                  # Round 1B: Persona-Driven Section Relevance
│   ├── app/
│   ├── Collection 1/
│   ├── Collection 2/
│   ├── Collection 3/
│   ├── Dockerfile
│   └── README.md
└── README.md                      # This file (root-level overview)
```

---

## 🐳 How to Run (Dockerized)

### 🔹 Challenge 1A: PDF Outline Extractor

```bash
docker build -t pdf-outline-extractor ./challenge_1a

docker run --rm \
  -v "$(pwd)/challenge_1a/input:/app/input:ro" \
  -v "$(pwd)/challenge_1a/output:/app/output" \
  --platform linux/amd64 \
  pdf-outline-extractor
```

**📤 Output:** JSON with heading structure (`H1`, `H2`, `H3`) per PDF.

---

### 🔹 Challenge 1B: Persona-Based Relevance

```bash
docker build -t persona-doc-intel:1b ./challenge_1b

docker run --rm \
  -v "$(pwd)/challenge_1b/Collection 1:/workspace/input:ro" \
  -v "$(pwd)/challenge_1b/Collection 1:/workspace/output" \
  persona-doc-intel:1b
```

**📤 Output:** JSON showing ranked sections & subsections per persona-task combination.

---

## 🔧 Tech Stack

| Component | Used In | Description |
|----------|---------|-------------|
| Python 3.11 | 1A & 1B | Main language |
| PyPDF2 | 1A | Heuristic-based outline parsing |
| PyMuPDF | 1B | Fast PDF content extraction |
| ONNX + MiniLM | 1B | Embedding & semantic ranking |
| SpaCy + Tokenizers | 1B | Keyword boosting and lemmatization |
| Docker (≤1 GB) | All | Portable, reproducible deployment |

---

## 👨‍💻 Author

**Bhavik Kumar / Deewanshi Gujral**  
B.E. Computer Science and Engineering  
Hackathon Participant – Adobe India Hackathon 2025 (Rounds 1A & 1B)

---
