


//var BotonGuardar = document.getElementById("idGuardarTrabajo");


// ELEMENTOS para los trabajos y suministros(ESCUCHADORES)
var boton_incrementa_productos = document.getElementById("AgregarProductoNuevo");
var ListaProductos = document.getElementById("listaProductos");



function eliminar(){//Funcion para eliminar los elementos (TR)


    //console.log("Llamamos para eliminar");
    //console.log(this.parentNode.parentNode.parentNode);
    this.parentNode.parentNode.parentNode.remove();
    
}


function AgregarCamposTrabajo(){//Funcion para agregar nuevos campos en la vista

    console.clear();
    console.log("Agregando campos de trabajos");
    var TrClonar = document.getElementById("clonacionProductos");
    var padre = TrClonar.parentNode;
    var elemento_clon = TrClonar.cloneNode(true);
    //padre.appendChild(descripcion);
    //padre.appendChild(cantidad);
    //padre.appendChild(costo);
    //Con ChilNodes vamos accediendo a la lista nodos de el elemento elegido
    console.log(elemento_clon.childNodes);


    //Primer inputs(Productos)
    //console.log(elemento_clon.childNodes[1].childNodes[1]);
    SelectProductos = elemento_clon.childNodes[1].childNodes[1];
    //InputDescripcion.value ="";
    //console.log(SelectProductos);

    //Segundo inputs(Calidad)
    SelectCalidad = elemento_clon.childNodes[2].childNodes[1];
    //SelectCalidad.value ="";
    //console.log(SelectCalidad);

    //Tercer inputs(Cantidad)
    InputCantidad = elemento_clon.childNodes[3].childNodes[1].childNodes[1];
    InputCantidad.value ="1";
    //console.log(InputCantidad);


    console.log("Div donde engloba el boton y el icon: ",elemento_clon.childNodes[3].childNodes[1]);
    console.log("boton dentro del div: ",elemento_clon.childNodes[3].childNodes[1].childNodes[3]);
    console.log("icono dentro del div: ",elemento_clon.childNodes[3].childNodes[1].childNodes[3].childNodes[1]);

    var boton = elemento_clon.childNodes[3].childNodes[1].childNodes[3];
    var icono = elemento_clon.childNodes[3].childNodes[1].childNodes[3].childNodes[1]
    icono.remove();//Eliminamos el icono que esta aqui colocado

    var icono = document.createElement("img");
    icono.setAttribute("src","/static/peticiones/svg/dash-square.svg");
    icono.setAttribute("width","16");
    icono.setAttribute("height","16");

    boton.appendChild(icono);


    //element.setAtributte
    boton.removeAttribute("disabled");
    boton.setAttribute("class","btn btn-danger btn-flat");
 
    //AQUI ASIGNAMOS LA FUNCION PARA ELIMINAR LOS ELEMENTOS
    boton.addEventListener('click',eliminar);
    //boton.setAttribute("onclick","eliminar(this)");
     
    //icono.setAttribute("class","fa fa-minus");
    //console.log(boton);
    //console.log(icono);
    ListaProductos.appendChild(elemento_clon);

    console.log("llegamos aqui");


} 


boton_incrementa_productos.addEventListener('click',AgregarCamposTrabajo);

















