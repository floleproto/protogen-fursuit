from flask import Flask, escape, request, render_template
import os
#import mpd

app = Flask(__name__)

#if __name__ == "__main__":
#  app.run(host='0.0.0.0')

@app.route('/')
def main():
   #return 'Hello'
   return render_template("led/main.html")

@app.route('/led')
def led():
   #return 'Hello'
   return render_template("led/main.html")

@app.route('/mpd')
def mpd():
   #return 'Hello'
   return render_template("mpd/main.html")

@app.route('/api/addmusic', methods=['GET'])
def addmusic():
   
   if "url" in request.args:
      os.system("cd /home/pi/fursuit/lib && node addmusic.js " + request.args["url"])
      return {"msg" : "Success"}
   else:
      return {"msg" : "No URL provided"}

#mpd.ForcePlaySong("REMIX (Orchestral)  - 'Funa' (Galshi Revolution) - TahuyNet-Qzp3opSNgF4")
