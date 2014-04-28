np2gpx
======

(grease|tamper)monkey userscript and python webservice to create a gpx file from nikeplus track data


Requirements
============

Userscript:
 - Tampermonkey (google chrome)
 - Greasemonkey (firefox)

np2gpx.py:
 - Python 2.x
 - Flask
 - ElementTree
 - werkzeug
 - WSGI compatible app server, eg. gunicorn


Installation:
=============

- On browser, get the userscript extension (tampermonkey if using chrome, greasemonkey if using firefox). 
- Fill in the url of your web service to form action of userscript.js
- Run the server:
-- gunicorn -w 3 np2gpx:app
