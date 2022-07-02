topics = [
    "Rénovation énergétique",
    "transition bas carbone",
    "passoire thermique",
]
topic_for_search = " OR ".join(['"' + keyword + '"' for keyword in topics])

from ex import x

if __name__ == "__main__":
    print(x)