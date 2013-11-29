# -*- coding: utf-8 -*-
import codecs
import webapp2
import helloworld
import cgi


htmlrot="""

<br>
<hr>

  <head>
    <title>Sindre D.L ROT 1 3 </title>
  </head>

  <body>
    <h2>Text to ROT13:</h2>
    <form method="post">
      <textarea name="text" style="height: 100px; width: 400px;">%(text)s</textarea>
      <br>
      <input type="submit">
    </form>
  </body>

"""
class RotHandler(webapp2.RequestHandler):

	def get(self):
		self.write_htmlrot()


	def write_htmlrot(self, text = ""):
		self.response.out.write(htmlrot % {"text" : helloworld.escape_html(text)})



	def post(self):
		s = self.request.get('text')
		s = codecs.encode(s, 'rot13')
		self.write_htmlrot(s)


	#return codecs.encode(s, 'rot13')





#def post(self):
#	user_input = self.request.get("text")
#	user_input = codecs.encode(user_input,'rot13')
#	self.write_form(user_input)