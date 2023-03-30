import json

def main():
    news1 = open("news.txt",'r').read()
    sub_fptr = open("subs.json","r")
    subsitutions = json.load(sub_fptr)
    
    for k, v in subsitutions.items():
        news1 = news1.replace(k,v)

    better_news = open("betternews.txt", "w")
    better_news.write(news1)
    better_news.close()


main()

