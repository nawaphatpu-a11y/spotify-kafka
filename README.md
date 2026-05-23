## Project Overview
Real-time data streaming pipeline for Spotify track data using Apache Kafka.
Simulates streaming where Producer reads tracks from dataset 
and publishes to Kafka topic, Consumer receives and processes messages in real-time.

## Architecture diagram
dataset.csv → producer.py → Kafka Topic (spotify-tracks) → consumer.py
Docker: runs Kafka + Zookeeper

## Tech stack
- Language: Python 3.11
- Containerization: Docker
- Streaming: Apache Kafka

## How to run
1. Clone repo
2. docker-compose up
3. python producer.py 
4. python consumer.py

