FROM python:3.11-slim

RUN pip install --no-cache-dir nltk

ENV NLTK_DATA=/usr/local/nltk_data

RUN python -m nltk.downloader vader_lexicon -d $NLTK_DATA

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
