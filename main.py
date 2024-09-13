from flask import Flask
from flask import redirect
from numpy import loadtxt
from flask import request
from flask import Response
import flask
import numpy
import random
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True
from flask import after_this_request
import filecmp
import io
import os
import requests

app = Flask(__name__)
app._static_folder = ''

counter = 0


def rewrite(url):
  view_func, view_args = app.create_url_adapter(request).match(url)
  return app.view_functions[view_func](**view_args)


def discordredir(url, img):
  if (request.headers.get('User-Agent') != None
      and request.headers.get('User-Agent').find("Gecko/20100101 Firefox/92.0")
      == -1 and request.headers.get('User-Agent').find("Discord") == -1):
    return redirect(url)
  else:
    return rewrite(img)


@app.route("/rat.jpg")
def rat():
  return discordredir("https://www.youtube.com/watch?v=OXQwx1EolD8",
                      "/static/rat1.jpg")


@app.route("/windef.png")
def windef():
  return discordredir("windowsdefender:", "/static/windef1.png")


@app.route("/deryoil.png")
def deryoil():
  return discordredir("https://www.youtube.com/watch?v=BgUeQz3-eig",
                      "/static/deryoil1.png")


@app.route("/buranya")
def buranya():
  return discordredir("https://www.youtube.com/watch?v=i-6ybStkFXI",
                      "/static/buranya.png")


@app.route("/ziplash")
def gameblows():
  return discordredir("https://youtu.be/rFFREGXa_Gs?t=4",
                      "/static/freeziplash.jpg")


@app.route("/spamtong")
def cybercity():
  return discordredir("https://youtu.be/z3LP73PVOKI", "/static/spamtong.jpg")


@app.route("/discord")
def DISCOOOOOOORD():
  return discordredir("discord:", "/static/blurple.png")


@app.route("/burnerurl")
def test():
  return discordredir("discord:", "/static/blurple.png")


@app.route("/scott")
def gameblowsagain():
  user_agent = request.headers.get('User-Agent')
  if user_agent and ("Gecko/20100101 Firefox/92.0" not in user_agent
                     and "Discord" not in user_agent):
    lines = numpy.loadtxt("scottwoz.txt",
                          dtype=str,
                          comments="#",
                          delimiter=",")
    random_line = random.choice(lines)
    return redirect(f"https://www.youtube.com/watch?v={random_line}")
  else:
    return rewrite("/static/scottwhenhewozes.jpg")


@app.route("/theratandscottgame")
def tomfoolery():
  """im1 = Image.open('troll/gametemplate.png')
  im2 = Image.open(random.choice(['troll/scottagain.jpg', 'troll/ratahah.jpg']))
  im1 = im1.convert('RGB')
  im2 = im2.resize((700, 600))
  im1.paste(im2, (0, 160))
  im1.save("troll/gameresult1.png", quality=95)
  """

  @after_this_request
  def add_header(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    #response.headers['Cache-Control'] = 'no-cache, no-store, public, max-age=0'
    #response.headers["Pragma"] = "no-cache"
    #response.headers['Expires'] = '0'
    return response

  randomchoice = random.choice(
    ['/static/troll/scottsees.png', '/static/troll/ratsees.png'])
  return rewrite(randomchoice)


@app.route("/theepicimagesgame1")
def tomfooleryagain():
  im1 = Image.open('troll/gametemplate.png')
  response = requests.get('https://source.unsplash.com/random?')
  file = open('troll/unsplash/image.jpg', 'wb')
  file.write(response.content)
  im2 = Image.open(r"troll/unsplash/image.jpg")
  im1 = im1.convert('RGB')
  im2 = im2.resize((800, 600))
  im1.paste(im2, (0, 140))

  @after_this_request
  def add_header(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    #response.headers['Cache-Control'] = 'no-cache, no-store, public, max-age=0'
    #response.headers["Pragma"] = "no-cache"
    #response.headers['Expires'] = '0'
    return response

  im1.save("troll/unsplash/gameresult1.png", quality=95)
  return rewrite("/static/troll/unsplash/gameresult1.png")


@app.route("/agoofymovie")
def tomfoolery1():

  @after_this_request
  def add_header(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    #response.headers['Cache-Control'] = 'no-cache, no-store, public, max-age=0'
    #response.headers["Pragma"] = "no-cache"
    #response.headers['Expires'] = '0'
    return response

  randomchoice = random.choice(
    ['/static/goofymovie/amovie.png', '/static/goofymovie/agoofymovie.png'])
  return rewrite(randomchoice)


@app.route("/agoofymovie002")
def tomfoolery2():
  if (request.headers.get('User-Agent') != None
      and request.headers.get('User-Agent').find("Gecko/20100101 Firefox/92.0")
      == -1 and request.headers.get('User-Agent').find("Discord") == -1):
    return "nuh uh, you trynna mess up the order or smth?"
  else:
    global counter

    images = [
      '/static/goofymovie/amovie.png', '/static/goofymovie/agoofymovie.png'
    ]
    moviebefore = images[counter % len(images)]
    counter += 1

    @after_this_request
    def add_header(response):
      response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
      response.headers["Pragma"] = "no-cache"
      response.headers["Expires"] = "0"
      return response

    return rewrite(moviebefore)


@app.route('/duckify', methods=['GET', 'POST'], defaults={'path': ''})
@app.route('/duckify/<path:path>', methods=['GET', 'POST'])
def catch_duck(path):

  @after_this_request
  def add_header(response):
    response.headers[
      "Cache-Control"] = "private, no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    #response.headers['Cache-Control'] = 'no-cache, no-store, public, max-age=0'
    #response.headers["Pragma"] = "no-cache"
    #response.headers['Expires'] = '0'
    return response

  img = Image.new('RGB', (256, 256), color='white')
  d = ImageDraw.Draw(img)
  font = ImageFont.truetype("HelveticaNowDisplay-Black.ttf",
                            size=(35 / (len(path) / 6)))
  d.text((10, 95), path + " has been\nduckified", fill=(0, 0, 0), font=font)
  img.save('duckifier/ducked.png')
  return rewrite("/static/duckifier/ducked.png")


@app.route('/tti', methods=['GET', 'POST'], defaults={'path': ''})
@app.route('/tti/<path:path>', methods=['GET', 'POST'])
def catch_text(path):

  @after_this_request
  def add_header(response):
    response.headers[
      "Cache-Control"] = "private, no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    #response.headers['Cache-Control'] = 'no-cache, no-store, public, max-age=0'
    #response.headers["Pragma"] = "no-cache"
    #response.headers['Expires'] = '0'
    return response

  if ("thatonepizzatowerfan" not in path):
    img = Image.new('RGB', (256, 256), color='white')
  else:
    img = Image.new('RGB', (256, 256), color='red')
  if ("QuantumV" in path):
    img = Image.new('RGB', (256, 256), color='black')
  d = ImageDraw.Draw(img)
  font = ImageFont.truetype("HelveticaNowDisplay-Black.ttf",
                            size=(35 / (len(path) / 10)))
  if ("QuantumV" not in path):
    d.text((10, 95), path, fill=(0, 0, 0), font=font)
  else:
    d.text((10, 95), path, fill=(255, 255, 255), font=font)
  img.save('duckifier/normal/texted.png')
  return rewrite("/static/duckifier/normal/texted.png")


@app.route('/')
def index():
  test = "Hello!"
  return test


app.run(host='0.0.0.0', port=81)
