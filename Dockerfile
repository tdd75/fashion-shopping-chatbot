FROM rasa/rasa:3.4.2-full

WORKDIR /app/chatbot

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

COPY . .