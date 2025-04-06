# SHL Assessment Recommender

This project is a semantic recommendation system that uses local LLM embeddings (via Ollama) to match job descriptions or natural language queries with the most relevant SHL assessments. It is built using Flask for the backend and HTML/CSS/JavaScript for the frontend.

## Features

- Input can be free-text or a URL pointing to a job description.
- Retrieves the top 1–10 most relevant SHL assessments based on semantic similarity.
- Displays results in a user-friendly table with:
  - Assessment Name (linked to SHL catalog)
  - Remote Testing Support
  - Adaptive/IRT Support
  - Test Duration
  - Test Type
- Includes a public API endpoint for JSON-based programmatic access.
- Fully compatible with local deployment using Ollama and Docker.

## Tech Stack

- Flask (Python backend)
- Ollama (for local LLM-powered text embeddings)
- FAISS (for similarity search)
- BeautifulSoup (web scraping from job description URLs)
- HTML/CSS/JavaScript (frontend)
- Docker (for containerized deployment)

## Getting Started

### Prerequisites

- Python 3.8+
- [Ollama](https://ollama.com) installed locally
- Model used: `nomic-embed-text`

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/shl-assessment-recommender.git
   cd shl-assessment-recommender
