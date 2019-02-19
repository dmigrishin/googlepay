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

import config
import time


class WOB_Payload:
  TYPE_MAP = {
      'LoyaltyClass': 'loyaltyClasses',
      'LoyaltyObject': 'loyaltyObjects',
      'OfferClass': 'offerClasses',
      'OfferObject': 'offerObjects',
      'GiftCardClass': 'giftCardClasses',
      'GiftCardObject': 'giftCardObjects'
  }

  def __init__(self):
    self.audience = config.AUDIENCE
    self.type = config.SAVE_TO_ANDROID_PAY
    self.iss = config.SERVICE_ACCOUNT_EMAIL_ADDRESS
    self.origins = config.ORIGINS
    self.iat = int(time.time())
    self.payload = {}

  def addWalletObjects(self, payload, wob_type):
    if not payload:
      # Raise some other exception.
      pass
    try:
      self.payload[self.TYPE_MAP[wob_type]] = [payload]
    except KeyError:
      # Raise some exception (???) to indicate invalid type
      pass

  def getSaveToWalletRequest(self):
    request_body = {}
    request_body['iss'] = self.iss
    request_body['aud'] = self.audience
    request_body['typ'] = self.type
    request_body['iat'] = self.iat
    request_body['payload'] = self.payload
    request_body['origins'] = self.origins
    return request_body
