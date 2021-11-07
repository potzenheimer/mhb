// Main site navigation
function navigationBar() {

    let _settings = {
        backdropClass: "u-backdrop",
        backdropDisplay: true,
        bodyMarkerClass: "u-no-scroll",
        containedDropdownClass: "c-nav__item--has-dropdown",
        drawerCloseTrigger: ".js-drawer-close",
        drawerToggle: '.js-dropdown-toggle',
        drawerToggleClass: 'js-dropdown-toggle',
        dropdownOpenClass: "c-nav__link--open",
        menu: ".c-nav",
        menuContainer: ".app-header",
        menuContainerActive: "app-header--overlay",
        menuContainerOffsetMarker: "app-header--offset",
        menuDropdown: ".c-nav__dropdown",
        menuDropdownOpen: "c-nav__dropdown--open",
        menuDropdownDisabled: "c-nav__dropdown--hidden",
        navBar: ".c-nav-bar",
        navBarHidden: "c-nav-bar--hidden",
        navBarOverlay: "c-nav-bar--overlay",
        navBarToggle: ".js-nav-toggle",
        navBarToggleActiveClass: "js-nav-toggle--active",
        navBarToggleCloseClass: "js-nav-toggle--close"
    };

    let navBarIsActive = false;
    let contentScrollPosition = 0;

    console.log("Site navigation initialized");
    initNavigation(_settings);

    function navigationOffsetMarker(options) {
        var $menuContainer = document.querySelector(options.menuContainer),
            $menuContainerScrolled = $menuContainer.offsetTop || 0;
        window.addEventListener("scroll", function() {
            if (window.pageYOffset > $menuContainerScrolled) {
                $menuContainer.classList.add(options.menuContainerOffsetMarker);
            } else {
                $menuContainer.classList.remove(options.menuContainerOffsetMarker);
            }
        })
    }

    function activateNavigation(element, options) {
        var $elBody = document.getElementsByTagName('body')[0],
            $menuContainer = document.querySelector(options.menuContainer),
            $menuContainerActiveClass = options.menuContainerActive,
            $navBar = document.querySelector(options.navBar);
        if ($navBar !== null) {
            element.classList.add(options.navBarToggleActiveClass);
            $navBar.classList.add(options.navBarOverlay);
            $navBar.classList.remove(options.navBarHidden);
            $menuContainer.classList.add($menuContainerActiveClass);
            $elBody.classList.add(options.bodyMarkerClass);
            if (options.backdropDisplay === true) {
                $menuContainer.classList.add(options.backdropClass);
            }
        }
    }

    function deactivateNavigation(options) {
        var $elBody = document.getElementsByTagName('body')[0],
            $menuContainer = document.querySelector(options.menuContainer),
            $menuContainerActiveClass = options.menuContainerActive,
            $navBar = document.querySelector(options.navBar),
            navBarToggle = Array.prototype.slice.call(document.querySelectorAll(options.navBarToggle));
        if ($navBar !== null) {
            navigationDrawerClose(options);
            navBarToggle.forEach(function(el) {
                el.classList.remove(options.navBarToggleActiveClass);
            });
            $navBar.classList.remove(options.navBarOverlay);
            $navBar.classList.add(options.navBarHidden);
            $menuContainer.classList.remove($menuContainerActiveClass);
            $elBody.classList.remove(options.bodyMarkerClass);
            if (options.backdropDisplay === true) {
                $menuContainer.classList.remove(options.backdropClass);
            }
        }
    }

    function navigationToggleHandler(element, options) {
        let bodyElement = document.getElementsByTagName('body')[0];
        // Handle navigation states
        if (navBarIsActive) {
            deactivateNavigation(options);
            bodyElement.style.top = 0;
            window.scrollTo(0, contentScrollPosition);
            console.log('Navigation disabled');
        } else {
            contentScrollPosition = window.pageYOffset;
            bodyElement.style.top = -contentScrollPosition + 'px';
            activateNavigation(element, options);
            console.log('Navigation active');
        }
        navBarIsActive = !navBarIsActive;
    }

    function navigationDrawerClose(options) {
        let navigationDrawers = document.getElementsByClassName(options.menuDropdownOpen),
            activeDrawers = document.getElementsByClassName(options.containedDropdownClass);
        [].forEach.call(navigationDrawers, function(el) {
            el.classList.remove(options.menuDropdownOpen);
            el.classList.add(options.menuDropdownDisabled);
        });
        [].forEach.call(activeDrawers, function(el) {
            el.classList.remove(options.containedDropdownClass);
        });
    }

    function navigationDrawerOpen(el, options) {
        // Toggle sub level navigation drawers
        let $dropdownToggle = el,
            navListItem = $dropdownToggle.parentNode,
            $elementParent = el.closest(options.menu),
            currentDropDown = el.nextElementSibling,
            $activeNavLink = document.querySelector(options.dropdownOpenClass),
            $menuDropDownContained = document.querySelector(options.containedDropdownClass);
        navListItem.classList.add(options.containedDropdownClass);
        currentDropDown.classList.remove(options.menuDropdownDisabled);
        currentDropDown.classList.add(options.menuDropdownOpen);
        setTimeout(function() {
            $elementParent.classList.remove(options.menuDropdown);
            if ($activeNavLink !== null) {
                $activeNavLink.classList.remove(options.dropdownOpenClass);
                $menuDropDownContained.classList.remove(options.containedDropdownClass);
            }
        }, 250);
    }

    function handleBackDropEvent(options, event, bodyElement) {
        event.stopPropagation();
        // If the click happened inside the the container, bail
        if (!event.target.closest(options.navBar)) {
            // Handle already active navigation elements
            if (navBarIsActive && !event.target.classList.contains(options.navBarToggle)) {
                // deactivateNavigation(options);
                navigationToggleHandler(event.target, options);
                bodyElement.style.top = 0;
                window.scrollTo(0, contentScrollPosition);
            }
        }
    }


    function initNavigation(options) {
        let navBarToggle = Array.prototype.slice.call(document.querySelectorAll(options.navBarToggle)),
            bodyElement = document.getElementsByTagName('body')[0];
        // Add navigation marker
        navigationOffsetMarker(options);
        // Sub Navigation drawer
        // navigationDrawer(options);
        // Close navigation via ESC key
        document.addEventListener('keydown', function (event) {
            if ((event.key === 'Escape' || event.key === 'Esc' || event.keyCode === 27)) {
                event.preventDefault();
                if (navBarIsActive) {
                    // deactivateNavigation(options);
                    navigationToggleHandler(event.target, options);
                    bodyElement.style.top = 0;
                    window.scrollTo(0, contentScrollPosition);
                }
            }
        });
        // Close navigation via backdrop clicks or tabs
        document.addEventListener('click', function (event) {
            handleBackDropEvent(options, event, bodyElement);
        });
        // Nav bar toggle
        navBarToggle.forEach(function(el) {
            el.addEventListener("click", function(event) {
                event.preventDefault();
                event.stopPropagation();
                navigationToggleHandler(el, options);
            })
        });
    }
}

document.addEventListener("DOMContentLoaded", () => {
    navigationBar();
});