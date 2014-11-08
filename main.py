import newspaper

from newspaper import news_pool


while True:
  yahoo = newspaper.build('http://news.yahoo.com/us/')
  print "yahoo built"
  google = newspaper.build('http://www.usnews.com/')
  print "google built"
  bbc = newspaper.build('http://www.bbc.com/news/world/us_and_canada/')
  print "bbc built"
  nbc = newspaper.build('http://www.nbcnews.com/news/us-news')
  print "nbcbuild"
  cnn = newspaper.build('http://www.cnn.com/US/')
  print "cnn"
  abc = newspaper.build('http://abcnews.go.com/US/')
  print "abc built"
  fox = newspaper.build('http://www.foxnews.com/us/index.html')
  print "fox built"

  papers = [yahoo, google, bbc, nbc, cnn, abc, fox]
  news_pool.set(papers, threads_per_source=2)
  news_pool.join()

  for Source in papers:
      for article in Source.articles:
          url = article.url
          htmlcode = article.html

          print url
          filename = "html/" + article.title + ".html"
          filename = filename.replace("'", "")
          pngfilename = "png/" + article.title + ".png"
          print filename.encode('utf-8')
          htmlfile = open(filename.encode('utf-8'), "wb")
          htmlfile.write(htmlcode.encode('utf-8'))
          htmlfile.close()
          #HTML(filename).write_png(pngfilename)
