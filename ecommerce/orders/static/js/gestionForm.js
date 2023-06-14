(function () {

    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {

            const confirmacion = confirm('¿Esta seguro de eliminarlo?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });

    document.getElementsByClassName("close")[0].onclick = function(event) {
       event.preventDefault();
       var alert = document.getElementsByClassName("close")[0].offsetParent.className.split(' ')[0];
       document.querySelector('.' + alert).classList.add('d-none')
    }
    
})();