#! /usr/bin/env python

"""
main.py - our python file handling dynamic requests
"""

import webapp2

class HelloWorld(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("""
<!DOCTYPE html>
<html>
  <head>
    <title>Hello World - Dynamic</title>
  </head>
  <body>
    <h1>Hello World - Dynamic</h1>
    <p>This output is generated using Python. Yeah!</p>
  </body>
</html>
			""")

# The app object which was mentioned in the app.yaml file - here it comes!
app = webapp2.WSGIApplication([
    ('/', HelloWorld),
], debug=True)