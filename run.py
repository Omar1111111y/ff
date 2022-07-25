import json
import threading
import requests
import cloudscraper
from itertools import zip_longest
from bs4 import BeautifulSoup as bs
from time import sleep as t
from flask import Flask, jsonify, request
##################################################
def tutorialbar():
    global tb_links
    global z
    tb_links = []
    big_all = []
    an = []
    ttt = []
    uur = []
    for page in range(1):
        r = requests.get("https://www.tutorialbar.com/all-courses/page/" + str(page))
        soup = bs(r.content, "html5lib")
        small_all = soup.find_all(
            "h3", class_="mb15 mt0 font110 mobfont100 fontnormal lineheight20"
        )
        big_all.extend(small_all)
    for index, item in enumerate(big_all):
        title = item.a.string
        url = item.a["href"]
        r = requests.get(url)
        soup = bs(r.content, "html5lib")
        link = soup.find("a", class_="btn_offer_block re_track_btn")["href"]
        if "www.udemy.com" in link:
           # tb_links.append(title + "|:|" + link)
             print (link)
             pass
###################   bul   #########
        s = cloudscraper.CloudScraper()
        lu = s.get(link).text
        try:
            soup_p = bs(lu,'html.parser')
            bb = soup_p.findAll("div",{"class":"course-landing-page__main-content"})
            tt = soup_p.findAll("h1",{"class": "udlite-heading-xl clp-lead__title clp-lead__title--small"})[0].text
            tbb = soup_p.findAll("div",{"class":"udlite-text-md clp-lead__headline"})[0].text
        except:
            pass
###############

######################################
        an.append(tt)
        ttt.append(tbb)
        uur.append(link)
####################
    z = list(zip_longest(an,ttt,uur))
    mm = "name"
    m = {mm:z}
    with open('omar.json','w') as f:
        gg = json.dumps(m)
        f.write(gg)
   # t()
###################################
    #print (z)
######################
#tutorialbar()
#print (z)
    app = Flask(__name__)
    @app.route('/',methods=['GET','POST'])
    def hello_world():
        if request.method == 'POST':
            pass
        else: #GET
            return jsonify({'help':'Omar => Omar'})
    
######################
    #z = list(zip_longest(an,ttt,uur)) 
    #print (z)
##################### API
    @app.route('/omar_style/<om>')
    def get_tmm(om):
        with open("omar.json","r") as f :
            con = json.loads(f.read())

    #nn = list.get(om)
        if om == 'omar':
            nn = con.get("name")
            return jsonify({'name':nn})
        else:
            return jsonify({'Eerrrrlo => Omar_Style ':om})

    app.run(debug=True)
if __name__ == '__main__':
    tutorialbar()
    #app.run(host='8.8.8.8')
#    tutorialbar()
#    tt = threading.Thread(target = app.run(port=3399),args=())
 #   tm = threading.Thread(target = tutorialbar,args=())
    #tt = threading.Thread(target = app.run,args=())

###############################################

  #  tm.start()
   # tt.start()
#    tutorialbar()
    #app.run(port=3333)
#####################

