const getId = (id) => document.getElementById(id);

class MaquinaEscribir{
    constructor(Objeto){
        [this.id, this.texto] = [Objeto.id, Objeto.texto];
        this.contador = this.texto.length;
        this.max = this.contador;
    }
    iniciarMaquina(){
        this.salida = getId(this.id);
        this.request = setInterval(() => this.loop(--this.contador), 60)
    }
    loop(contador){
        let letra = (-contador + (this.max-1)) % this.max;
        this.salida.innerHTML += this.texto[letra];
        if (contador <=0){
            window.clearInterval(this.request);
        }
    }
}
$("#cate").click(function() {
    $('html, body').animate({
        scrollTop: $("#categoria").offset().top
    }, 2000);
});
$("#promo").click(function() {
    $('html, body').animate({
        scrollTop: $("#promosiones").offset().top
    }, 2000);
});
$("#brand").click(function() {
    $('html, body').animate({
        scrollTop: $(".container-portada").offset().top
    }, 2000);
});

$(document).ready(main);

var contador = 1;

function main () {
    $('.menu_bar').click(function(){
        if (contador == 1) {
            $('nav').animate({
                left: '0'
            });
            contador = 0;
        } else {
            contador = 1;
            $('nav').animate({
                left: '-100%'
            });
        }
    });

    // Mostramos y ocultamos submenus
    $('.submenu').click(function(){
        $(this).children('.children').slideToggle();
    });
}

