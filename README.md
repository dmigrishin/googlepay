s2ap-quickstart-Python
==============================

[How to work with this quickstart](https://developers.google.com/pay/passes/samples/quickstart-python)

This sample demonstrates integration of the basic components of the Save to Google Pay API.  Review the [quickstart guide](https://developers.google.com/pay/save/samples/quickstart-python) to run the sample.

This sample showcases several aspects of the API
* Creation of Classes and Objects
* Save to Google Pay insertion of classes and objects
* The Web Service API

## Creation of Classes and Objects
The code for creation of classes and objects can be found in the offer.py and loyalty.py files.  Each Object type, such as loyalty, is broken out into its own file.  Classes are inserted using the WobInsertServlet.

## Save to Google Pay insertion of Classes and Objects
Save to Google Pay is handled on both the client and server. The index.html file is the landing page for the application and includes app.js. The app.js file makes a request to jwt/ to generate Object type-specific JWTs. The app.js inserts the appropriate g:wallet tags and the Save to Google Pay JavaScript after all of the JWTs are generated. 

## Webservice API
The Webservice API handler is the handleWebService function in main.py. This function handles Webservice requests, generates Loyalty Objects converts Loyalty Objects to JWTs, and responds with the JWT.

[![Analytics](https://ga-beacon.appspot.com/UA-46956809-1/walletobjects-quickstart-python/README.md)](https://github.com/igrigorik/ga-beacon)
