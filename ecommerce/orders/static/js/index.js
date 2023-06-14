    // tabla

    $(document).ready(function () {
        $('#myTable').pageMe({
            pagerSelector: '#pagination',
            activeColor: 'blue',
            prevText: 'Anterior',
            nextText: 'Siguiente',
            showPrevNext: true,
            hidePageNumbers: false,
            perPage: 5
        });
    });
    // end tabla
    
    // slider
    
    var swiperEl = document.querySelector(".mySwiper");
    Object.assign(swiperEl, {
        grabCursor: true,
        effect: "creative",
        creativeEffect: {
            prev: {
                shadow: true,
                translate: [0, 0, -400],
            },
            next: {
                translate: ["100%", 0, 0],
            },
        },
    });
    swiperEl.initialize()
    
    // end slider
    
    // charts
    var bar = document.getElementById("barras-arboles").getContext("2d");
    
    
    var myBarGraph = new Chart(bar, {
        type: "bar",
        data: {
            labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
            datasets: [
                {
                    label: "2021",
                    data: [50, 100, 450, 70, 200, 300, 405, 508, 305, 550, 370, 300, 320],
    
                    backgroundColor: "#76c781",
                    borderColor: "#76c781",
                    borderWidth: 0
                },
                {
                    label: "2022",
                    data: [108, 30, 105, 350, 600, 420, 300, 505, 350, 480, 425, 560, 340],
                    backgroundColor: "#7693c7",
                    borderColor: "#7693c7",
                    borderWidth: 0
                }
            ]
        },
        options: {
            tooltips: {
                cornerRadius: 0,
                caretSize: 1,
                xPadding: 12,
                yPadding: 14,
                backgroundColor: "rgba(0, 150, 100, 0.9)",
                titleFontStyle: "normal",
                titleMarginBottom: 15
            },
            scales: {
                yAxes: [
                    {
                        ticks: {
                            beginAtZero: true
                        }
                    }
                ]
            },
            title: {
                display: true,
                fontSize: 30,
                text: "Arboles sembrados - 2021 - 2022"
            }
        }
    });
    
    var barDesktop = document.getElementById("barras-arboles-desktop").getContext("2d");
    
    
    var myBarGraph = new Chart(barDesktop, {
        type: "bar",
        data: {
            labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
            datasets: [
                {
                    label: "2021",
                    data: [50, 100, 450, 70, 200, 300, 405, 508, 305, 550, 370, 300, 320],
    
                    backgroundColor: "#76c781",
                    borderColor: "#76c781",
                    borderWidth: 0
                },
                {
                    label: "2022",
                    data: [108, 30, 105, 350, 600, 420, 300, 505, 350, 480, 425, 560, 340],
                    backgroundColor: "#7693c7",
                    borderColor: "#7693c7",
                    borderWidth: 0
                }
            ]
        },
        options: {
            tooltips: {
                cornerRadius: 0,
                caretSize: 1,
                xPadding: 12,
                yPadding: 14,
                backgroundColor: "rgba(0, 150, 100, 0.9)",
                titleFontStyle: "normal",
                titleMarginBottom: 15
            },
            scales: {
                yAxes: [
                    {
                        ticks: {
                            beginAtZero: true
                        }
                    }
                ]
            },
            title: {
                display: true,
                fontSize: 30,
                text: "Arboles sembrados - 2021 - 2022"
            }
        }
    });

    
    