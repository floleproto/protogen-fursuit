from flask import Flask, escape, request, render_template

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
