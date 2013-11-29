import webapp2

import valid

import cgi

import rot13


form="""

<form method="post">
	What is you'r birthday?
	<br>
	<label>Month <input type="text" name="month" value="%(month)s"></label>

	<label>Day <input type="text" name="day" value="%(day)s"></label>

	<label>Year <input type="text" name="year" value="%(year)s"></label>

	<div style="color: red">%(error)s</div>

	<br>
	<br>

	<input type="submit">
</form>

"""



class MainPage(webapp2.RequestHandler):
	def write_form(self, error="", month="", day="", year=""):
		self.response.out.write(form % {"error": error,
										"month": escape_html(month),
										"day": escape_html(day),
										"year": escape_html(year)})


	def get(self):
		self.write_form()


	def post(self):
		user_month = self.request.get('month')
		user_day = self.request.get('day')
		user_year = self.request.get('year')

		month = valid.valid_month(user_month)
		day = valid.valid_day(user_day)
		year = valid.valid_year(user_year)

		#user_month = valid.valid_month(self.request.get('month'))
		#user_day = valid.valid_day(self.request.get('day'))
		#user_year = valid.valid_year(self.request.get('year'))


		if not (month and day and year):
			self.write_form("That dosen't look very valid.",
							user_month, user_day, user_year)

		else:
			self.redirect("/thanks")
			#self.response.out.write("Thanks! Thats a totally valid day!")



class ThanksHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("Thanks! Thats a totally valid day!")


		





def escape_html(s):
	esc = cgi.escape
	return esc(s, quote = True)

print escape_html("test")









application = webapp2.WSGIApplication([('/', MainPage), ('/thanks', ThanksHandler), ('/rot13', rot13.RotHandler)], debug=True)
