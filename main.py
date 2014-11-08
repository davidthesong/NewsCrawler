import newspaper
from xhtml2pdf import pisa
from newspaper import news_pool

while True:
  yahoo = newspaper.build('http://news.yahoo.com/us/')
  print "yahoo built"
  google = newspaper.build('http://www.usnews.com/')
  print "google built"
  bbc = newspaper.build('http://www.bbc.com/news/world/us_and_canada/')
  print "bbc built"

  papers = [yahoo, google, bbc]
  news_pool.set(papers, threads_per_source=2)
  news_pool.join()

  for Source in papers:
      for article in Source.articles:
          url = article.url
          htmlcode = article.html

          print url
          filename = "html/" + article.title + ".html"
          filename = filename.replace("'", "")
          pdfilename = "pdf/" + article.title + ".pdf"
          print filename.encode('utf-8')
          htmlfile = open(filename.encode('utf-8'), "wb")
          htmlfile.write(htmlcode.encode('utf-8'))
          htmlfile.close()
