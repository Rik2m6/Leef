import random

def ChuncksConfig():
    chunks = {}

    for y in range(16):

        for i in range(12):
            nameKey = f"x{(y+1)*50}y{(i+1)*50}"
            chunks[nameKey] = {
                "bio": "padrão",
                "folhasLim": random.randint(1, 5),
                "folhas": 0,
                "range": {"InitX": y*50,
                        "InitY": i*50,
                        "EndX": (y*50) + 50,
                        "EndY": (i*50) + 50}
            }

    return chunks

if __name__ == "__main__":
    chunks = ChuncksConfig()
    print(chunks)