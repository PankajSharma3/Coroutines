def searcher():
    import time 
    book="Pankaj Sharma is a good boy and a very tellented person"
    time.sleep(4)
    while True:
        text = (yield)
        if text in book:
            print("Your text in the book")
        else:
            print("Your text is not in the book")
search=searcher()
print("Search Exicuted")
next(search)
print("Print Exicuted")
search.send("Pankaj Sharma good")
search.close