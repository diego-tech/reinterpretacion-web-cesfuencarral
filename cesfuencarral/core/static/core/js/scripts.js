// Go Top
$(document).ready(function() {
    $('.go-top').click(function() {
        $('body, html').animate({
            scrollTop: '0px'
        }, 300);
    });

    $(window).scroll(function() {
        if ($(this).scrollTop() > 0) {
            $('.go-top').slideDown(300);
        } else {
            $('.go-top').slideUp(300);
        }
    });
});

// Ciclos


function visualiza_primero() {
    document.getElementById('primero').style.visibility = 'visible';
    document.getElementById('primero').style.display = 'block';
    document.getElementById('segundo').style.visibility = 'hidden';
    document.getElementById('segundo').style.display = 'none';
    document.getElementById('tercero').style.visibility = 'hidden';
    document.getElementById('tercero').style.display = 'none';
    document.getElementById('cuarto').style.visibility = 'hidden';
    document.getElementById('cuarto').style.display = 'none';
    document.getElementById('quinto').style.visibility = 'hidden';
    document.getElementById('quinto').style.display = 'none';
};

function visualiza_segundo() {
    document.getElementById('segundo').style.visibility = 'visible';
    document.getElementById('segundo').style.display = 'block';
    document.getElementById('primero').style.visibility = 'hidden';
    document.getElementById('primero').style.display = 'none';
    document.getElementById('tercero').style.visibility = 'hidden';
    document.getElementById('tercero').style.display = 'none';
    document.getElementById('cuarto').style.visibility = 'hidden';
    document.getElementById('cuarto').style.display = 'none';
    document.getElementById('quinto').style.visibility = 'hidden';
    document.getElementById('quinto').style.display = 'none';
};

function visualiza_tercero() {
    document.getElementById('tercero').style.visibility = 'visible';
    document.getElementById('tercero').style.display = 'block';
    document.getElementById('segundo').style.visibility = 'hidden';
    document.getElementById('segundo').style.display = 'none';
    document.getElementById('primero').style.visibility = 'hidden';
    document.getElementById('primero').style.display = 'none';
    document.getElementById('cuarto').style.visibility = 'hidden';
    document.getElementById('cuarto').style.display = 'none';
    document.getElementById('quinto').style.visibility = 'hidden';
    document.getElementById('quinto').style.display = 'none';
};

function visualiza_cuarto() {
    document.getElementById('cuarto').style.visibility = 'visible';
    document.getElementById('cuarto').style.display = 'block';
    document.getElementById('primero').style.visibility = 'hidden';
    document.getElementById('primero').style.display = 'none';
    document.getElementById('segundo').style.visibility = 'hidden';
    document.getElementById('segundo').style.display = 'none';
    document.getElementById('tercero').style.visibility = 'hidden';
    document.getElementById('tercero').style.display = 'none';
    document.getElementById('quinto').style.visibility = 'hidden';
    document.getElementById('quinto').style.display = 'none';
};

// Menu Responsive
$(".submenu").click(function() {
    $(this).children("ul").slideToggle();
})

$("ul").click(function(p) {
    p.stopPropagation();
})