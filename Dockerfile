# Utilise une image Python légère
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose le port Flask
EXPOSE 8080

# Commande de démarrage
#CMD ["python", "croissantage.py"]
CMD ["gunicorn","--bind", "0.0.0.0:8080", "croissantage:app"]
