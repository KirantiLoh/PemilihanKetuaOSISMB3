const navbar = document.getElementsByTagName('header')[0];

if (navbar) {
    url = document.URL.split('/');
    end = url[url.length - 1]
    if (end !== '') {
        if (end.startsWith('#')) {
            window.onscroll = function() {
                if (window.scrollY > 200) {
                    navbar.style.backgroundColor = 'rgb(39 34 99)';
                } else {
                    navbar.style.backgroundColor = "transparent";
                }
            }
        }
        navbar.style.backgroundColor = 'rgb(39 34 99)';
    } else {
        window.onscroll = function() {
            if (window.scrollY > 200) {
                navbar.style.backgroundColor = 'rgb(39 34 99)';
            } else {
                navbar.style.backgroundColor = "transparent";
            }
        }
    }
}