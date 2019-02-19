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

SERVICE_ACCOUNT_EMAIL_ADDRESS = 'google-pay-for-passes@qronus.iam.gserviceaccount.com'
ISSUER_ID = '3293346916822849083'
SERVICE_ACCOUNT_PRIVATE_KEY = 'qronus-f4c51341a49c.json'
APPLICATION_NAME = 'QRONUS TEST APP'
LOYALTY_CLASS_ID = 'LoyaltyClass'
LOYALTY_OBJECT_ID = 'LoyaltyObject'
OFFER_CLASS_ID = 'OfferClass'
OFFER_OBJECT_ID = 'OfferObject'
GIFTCARD_CLASS_ID = 'GiftCardClassPython'
GIFTCARD_OBJECT_ID = 'GiftCardObjectPython'
# List of origins for save to wallet button
ORIGINS = [
    'http://localhost:8080']

# Constants that are application agnostic.
AUDIENCE = 'google'
BAD_REQUEST = 400
LOYALTY_WEB = 'loyaltywebservice'
SAVE_TO_ANDROID_PAY = 'savetoandroidpay'
SCOPES = 'https://www.googleapis.com/auth/wallet_object.issuer'
