FROM python:3.11-slim

WORKDIR /app

# System deps for matplotlib, scipy, pymupdf
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc g++ libglib2.0-0 libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps first (layer cache)
COPY api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download nltk data
RUN python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('punkt_tab')"

# Copy app code
COPY api/ ./api/

# Copy data (chroma, bm25, chunks, etc.)
COPY data/ ./data/

# Copy service account key
COPY true-shoreline-447519-g7.json ./true-shoreline-447519-g7.json

# Write .env for the app
RUN echo "GCP_SA_KEY_PATH=../true-shoreline-447519-g7.json" > ./api/.env && \
    echo "GCP_LOCATION=us-central1" >> ./api/.env && \
    echo "GEMINI_MODEL=gemini-2.5-flash" >> ./api/.env && \
    echo "GEMINI_EMBED_MODEL=text-embedding-004" >> ./api/.env && \
    echo "CHROMA_COLLECTION=coastal_chunks_v3" >> ./api/.env

# Ensure plots/uploads dirs exist
RUN mkdir -p ./api/plots ./api/uploads

ENV PORT=8080
EXPOSE 8080

WORKDIR /app/api

CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
