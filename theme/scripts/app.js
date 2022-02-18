import './polyfills.js';
import './respimage.js';
import './ls.parent-fit.js';
import './lazysizes.js';
import './navigation.js';
import './paneleditor.js';

import './fontfaceobserver.js';

// Trigger font face observer protection
var fontPrimary = new FontFaceObserver('Lora', {
    weight: 400
});
var fontSecondary = new FontFaceObserver('Montserrat');

fontPrimary.load(null, 3000).then(function () {
    document.documentElement.className += " font__primary--loaded";
});

fontSecondary.load(null, 3000).then(function () {
    document.documentElement.className += " font__secondary--loaded";
});

Promise.all([fontPrimary.load(null, 3000),
    fontSecondary.load(null, 3000)
])
    .then(function () {
        document.documentElement.className += " fonts--loaded";
    });

if (navigator.userAgent.match(/iPhone|iPad|iPod/i)) {
    document.documentElement.className += " u-device--ios";
};

let sendTelemetry = function (signalType) {
    fetch('https://nom.telemetrydeck.com/api/v1/apps/6D371B8B-9F26-4CCC-874D-C7263F1B1481/signals/', {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "clientUser": navigator.userAgent,
            "type": signalType,
            "payload": {
                "url": window.location.href,
                "useragent": navigator.userAgent,
                "language": navigator.language,
                "platform": navigator.platform,
                "vendor": navigator.vendor,
            }
        })
    });
}

sendTelemetry("pageLoad")
