'''
Copyright 2013 Google Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the 'License');
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an 'AS IS' BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
import datetime

def generate_giftcard_class(issuer_id, class_id):
  giftcard_class = {
      'kind': 'walletobjects#giftCardClass',
      'id': '%s.%s' % (issuer_id, class_id),
      'issuerName': 'Baconrista',
      'merchantName': 'Baconrista',
      'issuerData': {
          'kind': 'walletobjects#typedValue'
      },
      'programLogo': {
          'kind': 'walletobjects#image',
          'sourceUri': {
              'kind': 'walletobjects#uri',
              'uri': 'http://farm8.staticflickr.com/7340/11177041185_a61a7f2139_o.jpg'
          }
      },
      'textModulesData': [{
        'header': 'Where to Redeem',
        'body': 'All US gift cards are redeemable in any US and Puerto Rico' +
                ' Baconrista retail locations, or online at Baconrista.com where'
                ' available, for merchandise or services.'
      }],
      'linksModuleData': {
        'uris': [
          {
            'kind': 'walletobjects#uri',
            'uri': 'http://www.baconrista.com',
            'description': 'Baconrista'
          }]
      },
      'locations': [{
          'kind': 'walletobjects#latLongPoint',
          'latitude': 37.422601,
          'longitude': -122.085286
      }],
      'allowMultipleUsersPerObject': True,
      'reviewStatus': 'underReview'
    }
  return giftcard_class

def generate_giftcard_object(issuer_id, class_id, object_id):
  giftcard_object = {
      'kind' : 'walletobjects#giftCardObject',
      'classId' : '%s.%s' % (issuer_id, class_id),
      'id' : '%s.%s' % (issuer_id, object_id),
      'cardNumber' : '123jkl4889',
      'pin' : '1111',
      'eventNumber' : '123456',
      'balance' : {
        'kind' : 'walletobjects#money',
        'micros' : 20000000,
        'currencyCode' : 'USD'
      },
      'balanceUpdateTime' : {
        'date' : datetime.datetime.utcnow().isoformat("T") + "Z"
      },
      'barcode' : {
          'alternateText' : '12345',
          'label' : 'Gift Card Id',
          'type' : 'qrCode',
          'value' : '28343E3'
      },
      'textModulesData': [{
        'header': 'Earn double points',
        'body': 'Jane, don\'t forget to use your Baconrista Rewards when  ' +
                'paying with this gift card to earn additional points. '
      }],
      'linksModuleData': {
        'uris': [
          {
            'kind': 'walletobjects#uri',
            'uri': 'http://www.baconrista.com/mybalance?id=1234567890',
            'description': 'My Baconrista Gift Card Purchases'
          }]
      },
      'state': 'active',
      'version': '1'
  }
  return giftcard_object
