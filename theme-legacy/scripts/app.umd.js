requirejs(['require',
        '/scripts/svg4everybody.js',
        '/scripts/flickity.pkgd.js',
        '/scripts/navbar.js',
        '/scripts/collapsible.js',
        '/scripts/accordion.js',
        '/scripts/slider.js',
        '/scripts/paneleditor.js',
        '/scripts/x-ray.js',
        '/scripts/dropmic.js',
        '/scripts/Sortable.min.js',
        '/scripts/fontfaceobserver.js',
        '/scripts/respimage.js',
        '/scripts/lazysizes-umd.js'
    ],
    function(require, svg4everybody, Flickity, navbar, collapsible, accordion, slider, panelEditor, xray, Dropmic, SortableJS) {
        'use strict';

        window.Date = Date;

        // Trigger font face observer protection
        var fontPrimary = new FontFaceObserver('Quicksand', {
            weight: 400
        });
        // var fontSecondary = new FontFaceObserver('Raleway');

        fontPrimary.load(null, 3000).then(function () {
            document.documentElement.className += " font__primary--loaded";
        });

        // fontSecondary.load(null, 3000).then(function () {
        //     document.documentElement.className += " font__secondary--loaded";
        // });

        Promise.all([
            fontPrimary.load(null, 3000),
            // fontSecondary.load(null, 3000)
        ])
            .then(function () {
                document.documentElement.className += " fonts--loaded";
            });

        if (navigator.userAgent.match(/iPhone|iPad|iPod/i)) {
            document.documentElement.className += " u-device--ios";
        };

        // SVG Sprite polyfill
        svg4everybody();

        // Viewport height variable helper
        let vh = window.innerHeight * 0.01;
        document.documentElement.style.setProperty('--vh', `${vh}px`);
        var resizeTimeout;
        window.addEventListener('resize', () => {
            if (resizeTimeout) {
                window.cancelAnimationFrame(resizeTimeout);
            }
            resizeTimeout = window.requestAnimationFrame(function () {
                let vh = window.innerHeight * 0.01;
                document.documentElement.style.setProperty('--vh', `${vh}px`);
            });
        });

        // Password toggle
        xray.init();


        // Choices select
        var choicesSelector = Array.prototype.slice.call(document.querySelectorAll('.js-choices-selector'));
        choicesSelector.forEach(function(el){
            let choices = new Choices(el, {
                itemSelectText: 'select',
            });
        });
        // if (choicesSelector !== null) {
        //     const choices = new Choices('.js-choices-selector', {
        //         itemSelectText: 'auswählen',
        //     });
        // }
        // Drop mic initialization
        let dropMicSelector = document.querySelector('[data-dropmic="quick-link-menu"]');
        if (dropMicSelector !== null) {
            var dropmic = new Dropmic(document.querySelector('[data-dropmic="quick-link-menu"]'), {
                onOpen: function() {
                    // dropmic.updateTargetBtn("Click to close");
                },
                onClose: function() {
                    // dropmic.updateTargetBtn("Bottom right (default)");
                }
            });
        }

        // Nav Bar
        navbar.init({
            backdropDisplay: true
        });

        // Collapsible element
        collapsible.init();

        // Collapsible element
        accordion.init();

        // Panel page and widget editor
        panelEditor.init();

        // Panel Editor Sortable
        let sortableSection = document.querySelector('.js-sortable');
        if (sortableSection !== null) {
            var sortable = SortableJS.create(sortableSection, {
                handle: ".js-sortable-handle",
                ghostClass: "c-sortable__ghost",  // Class name for the drop placeholder
                chosenClass: "c-sortable__chosen",  // Class name for the chosen item
                dragClass: "c-sortable__drag",  // Class name for the dragging item
                dataIdAttr: 'data-id',
                onSort: function (event) {
                    // same properties as onEnd
                    var items = event.to.children,
                        result = [];
                    for (var i = 0; i < items.length; i++) {
                        result.push(items[i].getAttribute('data-id'));
                    }
                    /* Do ajax call here */
                    var sourceUrl = sortableSection.dataset.storage,
                        targetEl = sortableSection,
                        formData = new FormData();
                    formData.append("order", JSON.stringify(result));
                    var request = new XMLHttpRequest();
                    request.open('POST', sourceUrl, true);

                    request.onload = function(e) {
                        if (request.status >= 200 && request.status < 400) {
                            // Success!
                            var response = request.responseText,
                                responseData = JSON.stringify(response),
                                returnData = JSON.parse(response);
                            if (returnData.message && returnData.message.length) {
                                var notice = document.createElement('div'),
                                    noticeText = document.createTextNode(returnData.message)
                                ;
                                notice.setAttribute('class', 'c-alert c-alert--success c-alert--toast');
                                notice.appendChild(noticeText);
                                targetEl.appendChild(notice);
                                setTimeout(function() {
                                    targetEl.removeChild(notice);
                                }, 5000);
                            }
                            // callback(JSON.parse(response), element);
                        } else {
                            // We reached our target server, but it returned an error
                            console.log('Widget sort order could not be saved.')
                        }
                    };

                    request.onerror = function() {
                        // There was a connection error of some sort
                        console.log('Connection error while storing widget order.')
                    };

                    request.send(formData);
                }
            });
        }

        slider.init({
            autoPlay: 6000
        });

        // Load Slider Resize
        window.addEventListener('load', function() {
            var sliders = Array.prototype.slice.call(document.querySelectorAll('.js-slider-resize'));
            if (sliders) {
                sliders.forEach(function(slider) {
                    var flkty = Flickity.data(slider);
                    flkty.resize()
                });
            }
        });



    });
