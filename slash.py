import cgi 
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app 

class RedirectToDirectory(webapp.RequestHandler): 
	def get(self): self.redirect(self.request.path + "/", permanent=True) 
	
app = webapp.WSGIApplication([('/.*', RedirectToDirectory)], debug=True)
def main(): run_wsgi_app(application) 
	
if __name__ == "__main__": main()