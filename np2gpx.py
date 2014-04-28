from flask import Flask, request, make_response
from werkzeug.contrib.fixers import ProxyFix
import json
import dateutil.parser
import datetime
import StringIO
import sys
from elementtree.SimpleXMLWriter import XMLWriter
 
app = Flask(__name__)
app.debug=True

@app.route('/', methods=['GET'])
def get():
   return make_response("oh, i'm post-only")

@app.route('/', methods=['POST'])
def post():
   try:
      d = request.form['thedata']
      ds = json.loads(d)['activity']
      stime = ds['startTimeUtc']
      stime = dateutil.parser.parse(stime)
      points = ds['geo']['waypoints']
      name = ds['name']

      f = StringIO.StringIO()
      w = XMLWriter(f)
      gpx_attribs = {"version":"1.1",
                        "creator":"unrealduck.com",
                        "xmlns:xsi":"http://www.w3.org/2001/XMLSchema-instance",
                        "xmlns:gpxtpx":"http://www.garmin.com/xmlschemas/TrackPointExtension/v1",
                        "xmlns":"http://www.topografix.com/GPX/1/1",
                        "xsi:schemaLocation":"http://www.topografix.com/GPX/1/1 http://www.topografix.com/gpx/1/1/gpx.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd"}
      gpx = w.start("gpx", gpx_attribs)
      w.start("metadata")
      w.element("name", name)
      w.element("time", str(stime).replace(" ", "T"))
      w.element("desc", "Import from nikeplus.com")
      w.end()

      w.start("trk")
      w.element("name", name)
      w.start("trkseg")

      for i,pt in zip(range(len(points)), points):            
         time = stime + datetime.timedelta(seconds=i)
         w.start("trkpt", lon=str(pt['lon']), lat=str(pt['lat']))
         w.element("ele", str(pt['ele']))
         w.element("time", str(time).replace(" ", "T"))
         w.end()
                     
      w.end()
      w.end()
         
      w.close(gpx)

      filename = '_'.join([ds['activityType'], ds['deviceType'], str(stime.date()), str(stime.time())])
      response = make_response("<?xml version=\"1.0\" ?>"+f.getvalue())
      response.headers['Content-Type'] = 'application/gpx+xml'         
      response.headers['Content-Disposition'] = 'attachment; filename='+filename+'.gpx'                 
      return response
      
   except KeyError:
      print "KeyError"
      return make_response("KeyError")
   except:
      print "UnexpectedError"
      print sys.exc_info()[0]
      return make_response("Unexpected error")


app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == "__main__":
   app.run()



