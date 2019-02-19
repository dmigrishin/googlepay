/**
 * Copyright 2013 Google Inc. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 * Save to Wallet success handler.
 */
var successHandler = function(params) {
  console.log('Object added successfully' + params);
}

/**
 * Save to Wallet failure handler.
 */
var failureHandler = function(params) {
  console.log('Object insertion failed' + params);
}

/**
 * Initialization function
 */
function init() {
  // Bind click event for 'Insert Loyalty Class' button.
  document.getElementById('loyalty').addEventListener('click', function() {
    $.get('insert?type=loyalty', function(data) {
      console.log(data);
    });
  });
  // Bind click event for 'Insert Offer Class' button.
  document.getElementById('offer').addEventListener('click', function() {
    $.get('insert?type=offer', function(data) {
      console.log(data);
    });
  });
  // Bind click event for 'Insert Gift Card Class' button.
  document.getElementById('giftcard').addEventListener('click', function() {
    $.get('insert?type=giftcard', function(data) {
      console.log(data);
    });
  });

  $.when(
    // Get jwt of loyalty object and render 'Save to Android Pay' button.
    $.get('jwt?type=loyalty', function(data) {
      saveToAndroidPay = document.createElement('g:savetoandroidpay');
      saveToAndroidPay.setAttribute('jwt', data);
      saveToAndroidPay.setAttribute('onsuccess', 'successHandler');
      saveToAndroidPay.setAttribute('onfailure', 'failureHandler');
      document.querySelector('#loyaltysave').appendChild(saveToAndroidPay);
      }
    ),
    // Get jwt of offer object and render 'Save to Android Pay' button.
    $.get('jwt?type=offer', function(data) {
      saveToAndroidPay = document.createElement('g:savetoandroidpay');
      saveToAndroidPay.setAttribute('jwt', data);
      saveToAndroidPay.setAttribute('onsuccess', 'successHandler');
      saveToAndroidPay.setAttribute('onfailure', 'failureHandler');
      document.querySelector('#offersave').appendChild(saveToAndroidPay);
      }
    ),
    // Get jwt of giftcard object and render 'Save to Android Pay' button.
    $.get('jwt?type=giftcard', function(data) {
      saveToAndroidPay = document.createElement('g:savetoandroidpay');
      saveToAndroidPay.setAttribute('jwt', data);
      saveToAndroidPay.setAttribute('onsuccess', 'successHandler');
      saveToAndroidPay.setAttribute('onfailure', 'failureHandler');
      document.querySelector('#giftcardsave').appendChild(saveToAndroidPay);
      }
    )
    ).done(function() {
      // it will execute after all above ajax requests are successful.
      script = document.createElement('script');
      script.src = 'https://apis.google.com/js/plusone.js';
      document.head.appendChild(script);
      }
    );
}

$(window).ready(function() {
  init();
});
