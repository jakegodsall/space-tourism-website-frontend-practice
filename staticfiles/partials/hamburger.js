const overlayMenu = document.getElementById('overlay__menu');
const hamburger = document.getElementById('hamburger');

const hamburgerHandler = () => {
    hamburger.classList.toggle('opened');

    if (hamburger.classList.contains('opened')) {
        console.log('opened');
        overlayMenu.classList.toggle('opened');
    } else {
        overlayMenu.classList.toggle('opened');
    }
};

// hamburger click event
hamburger.addEventListener('click', hamburgerHandler);
