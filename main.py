#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from google.appengine.ext.webapp import template
import webapp2
import wsgiref.handlers

class Index(webapp2.RequestHandler):
  def get(self):
    self.response.out.write( template.render('index.html', {}) )

# Configure app routes
app = webapp2.WSGIApplication([('/', Index)], debug=True)
