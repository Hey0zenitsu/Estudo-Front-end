class Temporizador {
    iniciar() {
        setInterval(() => {
            console.log("Executando...");
        }, 1000);
    }
}

const t = new Temporizador();
t.iniciar();