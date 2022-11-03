const dropArea = document.querySelector(".box");
const dragText = dropArea.querySelector("h2");
const button = dropArea.querySelector("button");
const input =dropArea.querySelector("#input-file");
let files;

//evento del click
button.addEventListener("click", (e) => {
    input.click();
});


//evento de arrastre (se pondra de azul el contorno)
input.addEventListener("change", (e) =>{
    files= this.files;
    dropArea.classList.add(".active");
    showFiles(files);
    dropArea.classList.remove(".active");
});



//evento de arrastre y suelta  de la imagen
dropArea.addEventListener("drogover", (e) => {
    e.preventDefault();
    dropArea.classList.add(".active");
    dragText.textContent="Suelta para subir los archivos";
});

dropArea.addEventListener("dragleave", (e) => {
    dropArea.classList.remove("active");
    dragText.textContent="Arrastra y suelta imagenes";
});

dropArea.addEventListener("drop", (e) => {
    dropArea.classList.remove("active");
    dragText.textContent="Arrastra y suelta imagenes";
});



function processFiles(file){}