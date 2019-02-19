"""
Copyright 2013 Google Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

def generate_offer_class(issuer_id, class_id):
  offer_class = {
      'kind': 'walletobjects#offerClass',
      'id': '%s.%s' % (issuer_id, class_id),
      'issuerName': 'Baconrista Coffee',
      'issuerData': {
          'kind': 'walletobjects#typedValue'
      },
      'title': '20% off one bacon fat latte',
      'redemptionChannel': 'both',
      'provider': 'Baconrista Deals',
      'titleImage': {
          'kind': 'walletobjects#image',
          'sourceUri': {
              'kind': 'walletobjects#uri',
              'uri': 'http://farm4.staticflickr.com/3723/11177041115_6e6a3b6f49_o.jpg'
          }
      },
      'allowMultipleUsersPerObject': True,
      'locations': [{
          'kind': 'walletobjects#latLongPoint',
          'latitude': 37.424015499999996,
          'longitude': -122.09259560000001
          },{
          'kind': 'walletobjects#latLongPoint',
          'latitude': 37.424354,
          'longitude': -122.09508869999999
          },{
          'kind': 'walletobjects#latLongPoint',
          'latitude': 37.7901435,
          'longitude': -122.39026709999997
          },{
          'kind': 'walletobjects#latLongPoint',
          'latitude': 40.7406578,
          'longitude': -74.00208940000002
      }],
      'reviewStatus': 'underReview',
      'review': {
          'comments': 'Real auto approval by system'
      },
      'textModulesData': [{
        'header': 'Details',
        'body': '20% off one cup of coffee at all Baconrista Coffee locations. ' +
                'Only one can be used per visit.'
       },{
        'header': 'About Baconrista',
        'body': 'Since 2013, Baconrista Coffee has been committed to making high ' +
                'quality bacon coffee. Visit us in our stores or online at www.baconrista.com'
      }],
      'linksModuleData': {
        'uris': [
          {
            'kind': 'walletobjects#uri',
            'uri': 'http://maps.google.com/?q=google',
            'description': 'Nearby Locations'
          },{
            'kind': 'walletobjects#uri',
            'uri': 'tel:6505555555',
            'description': 'Call Customer Service'
          }]
      },
      'imageModulesData': [
        {
          'mainImage': {
            'kind': 'walletobjects#image',
            'sourceUri': {
              'kind': 'walletobjects#uri',
              'uri':  'http://farm4.staticflickr.com/3738/12440799783_3dc3c20606_b.jpg',
              'description': 'Coffee beans'
            }
          }
        }
      ],
    }
  return offer_class

def generate_offer_object(issuer_id, class_id, object_id):
  offer_object = {
      'kind': 'walletobjects#offerObject',
      'classId': '%s.%s' % (issuer_id, class_id),
      'id': '%s.%s' % (issuer_id, object_id),
      'state': 'active',
      'version': '1',
      'issuerData': {
          'kind': 'walletobjects#typedValue'
      },
      'barcode': {
          'kind': 'walletobjects#barcode',
          'type': 'upcA',
          'value': '123456789012',
          'label': 'Offer Code',
          'alternateText': '12345'
      }
  }
  return offer_object
