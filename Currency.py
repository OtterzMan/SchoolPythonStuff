def Convert(pounds,currency):
    if currency == "USD":
        print(pounds * 1.11)
    
    if currency == "EUR":
        print(pounds * 1.14)
    
    if currency == "Yuan":
        print(pounds * 7.91)
    
    if currency == "Yen":
        print(pounds * 161.37)
    
Convert(46,"Yuan")