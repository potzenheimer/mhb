function panelEditor() {

    var _panelEditorSettings = {
        widgetSelectForm: 'js-widget-select-form',
        widgetSelectable: '.js-widget-selectable',
        widgetSelected: 'c-widget-selector__item--selected',
        widgetSelectedInputID: 'panel-page-widget',
        dropDownActiveMarker: 'o-dropdown--active'
    };

    function widgetSelector(options) {
        let widgetSelect = document.querySelectorAll(options.widgetSelectable),
            formControl = document.getElementById(options.widgetSelectedInputID);
        [].forEach.call(widgetSelect, function(element) {
            element.addEventListener('click', function(event) {
                event.preventDefault();
                [].forEach.call(widgetSelect, function(element) {
                    if(element !== this) {
                        element.classList.remove(options.widgetSelected);
                    }
                }, this);
                console.log('Selected: ' + event.currentTarget);
                element.classList.add(options.widgetSelected);
                formControl.value = element.getAttribute('data-widget-type');
            });
        });
    }

    function initialisePanelEditor(options) {
        widgetSelector(options);
    }

    initialisePanelEditor(_panelEditorSettings);

}

document.addEventListener("DOMContentLoaded", () => {
    panelEditor();
});
