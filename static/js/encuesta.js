// Leer el contador de establecimientos desde localStorage
let establecimientosVisitados = parseInt(localStorage.getItem('establecimientosVisitados')) || 0;

// Función para actualizar el texto de la encuesta
function actualizarTextoDeEncuesta() {
    const faltantes = 1 - establecimientosVisitados;  // Cambia 3 por el número necesario
    const texto = `¡Visita ${faltantes} establecimiento para acceder a la encuesta y a la rifa!`;
    document.getElementById("survey-text").textContent = texto;
}

// Cuando se hace clic en "Cómo llegar" en cualquier página, se aumenta el contador
document.querySelectorAll(".establecimiento-boton, .boton").forEach(boton => {
    boton.addEventListener("click", () => {
        console.log("¡Botón 'Cómo llegar' clickeado!"); // Imprime un mensaje en consola cuando el botón es clickeado
        
        if (establecimientosVisitados < 3) {
            establecimientosVisitados++;
            localStorage.setItem('establecimientosVisitados', establecimientosVisitados);
            actualizarTextoDeEncuesta();
            habilitarEncuesta(); // Habilita el botón de expandir cuando se llega a 3
        }
    });
});

// Habilitar la encuesta cuando se hayan visitado los 3 establecimientos
function habilitarEncuesta() {
    if (establecimientosVisitados >= 3) {
        document.querySelector('.expand-btn').style.display = 'block'; // Mostrar el botón de expandir
        document.querySelector('.encuesta-container').classList.remove('minimized'); // Mostrar la encuesta
        document.querySelector('.encuesta-container').style.display = 'block';
        document.querySelector('.encuesta-container').style.height = '300px';
        
        document.querySelector('.encuesta-container').classList.add('expanded');
        document.querySelector('.encuesta-container').classList.remove('minimized');
        document.querySelector('.encuesta-container iframe').style.display = "block";

         // Aseguramos que se muestre
        document.querySelector('.minimize-btn').style.display = 'block';
    }
    else{
        document.querySelector('.minimize-btn').style.display = 'none';
    }
}

// Función para expandir la encuesta
document.getElementById('expand-survey').addEventListener('click', function() {
    document.querySelector('.encuesta-container').classList.add('expanded');
    document.querySelector('.encuesta-container').classList.remove('minimized');
    document.querySelector('.encuesta-container iframe').style.display = "block"; // Mostrar iframe al expandir
});

// Función para minimizar la encuesta
document.getElementById('minimize-survey').addEventListener('click', function() {
    document.querySelector('.encuesta-container').classList.remove('expanded');
    document.querySelector('.encuesta-container').classList.add('minimized');
    document.querySelector('.encuesta-container iframe').style.display = "none"; // Ocultar iframe al minimizar
});

// Función para cerrar la encuesta
document.getElementById('close-survey').addEventListener('click', function() {
    document.querySelector('.encuesta-container').style.display = 'none'; // Cerrar encuesta completamente
});

// Para asegurarnos de que la encuesta y el contador se inicien correctamente
document.addEventListener("DOMContentLoaded", () => {
    actualizarTextoDeEncuesta();
    habilitarEncuesta();
});
