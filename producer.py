from kafka import KafkaProducer
import json 
import pandas as pd

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

df = pd.read_csv(r"C:\Users\User\Desktop\Project\dataset.csv")

for _, row in df.head(5).iterrows():
    data = {
        "track_name": row["track_name"],
        "artists": row["artists"],
        "popularity": int(row["popularity"]),
        "track_genre": row["track_genre"]
    }
    producer.send('spotify-tracks', value=data)
    print(f"Sent: {data['track_name']}")

producer.flush()
producer.close()