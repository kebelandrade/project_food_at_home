var cont = [];
var suma = [];
var datos = new Array();
function pedido(id) {
    var ids = [];
    axios.get('/cliente/pedido/'+id).
    then(function (pla) {
        console.log(pla.data);
        let html = "";
        for (var i = 0 ; i<pla.data.length; i++){
            suma.push(pla.data[i].fields.precio);
            //contador que almacena los id de los platos para luego sacar su longitud y usarlo en otro for
            cont.push(pla.data[i].pk);
            //ids es una lista que guarda los elementos de la consulta en una lista
            ids.push(pla.data[i].pk);
            ids.push(pla.data[i].fields.nombre);
            ids.push(pla.data[i].fields.precio);
            //datos es un array que que guarda la lista ids
            datos[pla.data[i].pk] = ids;
        }
        for(var c = 0 ; c<cont.length; c++){
            for (var d = 0; d<ids.length; d++){
                html +=`
                <div class="row">
                    <input type="text" name="id_plato-${c}" hidden readonly value="${datos[cont[c]][d]}">
                    <input type="text" hidden readonly value="${datos[cont[c]][d+1]}">
                    <input type="text" hidden readonly name="precio-${c}" value="${datos[cont[c]][d+2]}">
                    <input type="text" name="longitud"  hidden readonly value="${cont.length}">
                    <div class="col-6 col-md-6">${datos[cont[c]][d+1]}</div>
                    <div class="col-6 col-md-3">${datos[cont[c]][d+2]}</div>
                    <div class="col-6 col-md-3"><button class="btn btn-warning"><span class="icon-cross text-light"></span></button></div>
                </div>
            `

                break
            }
        }

        var elemento = document.getElementById('cont-recibo');
        elemento.innerHTML=html;
        let sum = 0 ;
        for(var i=0; i < suma.length; i++){
            sum = sum + suma[i]

        }
        document.getElementById("totalsuma").innerHTML = sum;
        document.getElementById("totals").innerText = sum;
        // console.log(cont);
        // console.log(ids);
        // console.log(datos);
        console.log(sum);
    });

}