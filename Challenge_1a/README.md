# 📄 Challenge 1A: PDF Outline Extractor

A lightweight, CPU-only Dockerized solution that extracts a structured outline (title, H1, H2, H3 headings with page numbers) from PDF documents using heuristics based on text formatting and structure.

---

## 🚀 Features

- Extracts outline from PDFs using:
  - Line length
  - Text casing (ALL CAPS, Title Case)
  - Page position
- Outputs structured JSON with heading hierarchy (`H1`, `H2`, `H3`)
- Built using `PyPDF2` with no dependencies on external tools (pure Python)
- Lightweight: Compatible with Docker containers under **1 GB**
- Fast: Parses 3–7 PDFs in under 60 seconds

---

## 🗂️ Project Structure

```
CHALLENGE_1A/
│
├── app/
│   ├── main.py             # Entrypoint: Reads input PDFs and writes JSON output
│   ├── pdf_parser.py       # Outline extraction logic using text heuristics
│   └── requirements.txt    # Python dependencies
│
├── input/                  # Input folder: Place PDF files here
├── output/                 # Output folder: JSON files are saved here
├── Dockerfile              # Minimal Alpine-based Docker setup
└── README.md               # Project documentation
```

---

## 🧪 Sample Output Format

```json
{
  "title": "Sample Document Title",
  "outline": [
    { "level": "H1", "text": "INTRODUCTION", "page": 1 },
    { "level": "H2", "text": "Background", "page": 2 },
    { "level": "H3", "text": "Motivation", "page": 3 }
  ]
}
```

---

## 🐳 Run with Docker

### 1. Build the Docker Image

```bash
docker build -t pdf-outline-extractor .
```

### 2. Run the Container

Ensure you have PDFs in the `input/` folder. Then run:

```bash
docker run --rm   -v "${PWD}/input:/app/input:ro"   -v "${PWD}/output:/app/output"   --platform linux/amd64   pdf-outline-extractor
```

> 📝 JSON outputs will be saved to `output/` with the same filename as the input PDF.

---

## 🧩 Tech Stack

- **Python 3.11**
- **PyPDF2 v3.0.1**
- **Docker (Alpine Linux base)**

---

## 📦 Requirements

If running outside Docker:

```bash
pip install -r app/requirements.txt
```

Then run:

```bash
python app/main.py
```

---

## 📜 License

This project is developed for internal evaluation purposes under the *Persona-Driven Document Intelligence Hackathon* and is licensed under MIT.

---

## 🙋‍♂️ Author

**Bhavik Kumar / Deewanshi Gujral**  
Computer Science and Engineering  
Hackathon Participant – Round 1A