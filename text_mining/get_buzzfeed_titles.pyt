"""
      Nora Mohamed
      ~*2015 FEB*~

      Goes to BuzzFeed and puts article titles into .txt
"""

from pattern.web import *

def get_buzzfeed_titles(url):
      """ Gets buzzfeed article titles and puts them into a text file or string
            url: List of buzzfeed URLs that 
            return: string of buzzfeed article titles
      """
      HTML = URL(url).download()
      index = 0
      title = ""
      while index != -1:
            index = HTML.find("rel:gt_act='post/title' >\n")
            if index == -1:
                  break
            HTML = HTML[index + 34:]
            title += HTML[0:HTML.find("      </a>")]
      return title

titles = ""
buzzfeed = ["http://www.buzzfeed.com/buzz", "http://www.buzzfeed.com/news",
            "http://www.buzzfeed.com/entertainment", "http://www.buzzfeed.com/quizzes"]
for page in buzzfeed:
      titles += get_buzzfeed_titles(page)
text_file = open("buzzfeed_titles.txt", "w")
text_file.write(titles)
text_file.close()

#use http://www.buzzfeed.com/archive/2014/1/2 !!!