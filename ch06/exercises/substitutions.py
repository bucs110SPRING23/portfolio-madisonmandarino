import json

def main():
    news1 = open("news.txt")
    ideas = json.load(news1)
    news1.close()

    idea = input("betternews.txt")
    ideas.append(idea)
    print(ideas)

    news1 = open("news.txt", "w")
    json.dump(ideas, news1)

    news1.close()

main()

