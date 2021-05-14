import 'polyfills';
import 'respimage';
import 'ls.parent-fit';
import 'lazysizes';
import svg4everybody from 'svg4everybody';

var FontFaceObserver = require('fontfaceobserver');

// SVG Sprite polyfill
svg4everybody();


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
