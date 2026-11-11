import random

def generate_random_quote():
    quotes = [
        "Keep learning, keep growing!",
        "Every bug is a lesson.",
        "Code today, succeed tomorrow.",
        "Consistency beats perfection.",
        "Build something amazing!"
    ]

    return random.choice(quotes)


if __name__ == "__main__":
    print(generate_random_quote())