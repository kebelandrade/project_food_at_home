var cont = []
var datos = new Array();
function pedido(id) {
    var ids = [];
    axios.get('/cliente/pedido/'+id).
    then(function (pla) {
        console.log(pla.data);
        let html = "";
        for (var i = 0 ; i<pla.data.length; i++){
            //contador que almacena los id de los platos para luego sacar su longitud y usarlo en otro for
            cont.push(pla.data[i].pk);
            //ids es una lista que guarda los elementos de la consulta en una lista
            ids.push(pla.data[i].pk);
            ids.push(pla.data[i].fields.nombre);
            ids.push(pla.data[i].fields.precio);
            //datos es un array que que guarda la lista ids
            datos[pla.data[i].pk] = ids;
            // html +=`
            //     <th><input type="text" readonly value="${pla.data[i].fields.nombre} " name="plato"> </th>
            //     <th><input type="text" readonly value="${pla.data[i].fields.precio}"></th>
            // `
        }
        for(var c = 0 ; c<cont.length; c++){
            for (var d = 0; d<ids.length; d++){
                html +=`
                <tr>
                    <th>${c+1}</th>
                    <th><input type="text" hidden readonly value="${datos[cont[c]][d]}">
                        <input type="text" hidden readonly value="${datos[cont[c]][d+1]}">
                        ${datos[cont[c]][d+1]}
                    </th>
                    <th>${datos[cont[c]][d+2]}</th>
                </tr>
                
            `
                break
            }
        }
        var elemento = document.getElementById('a_pedido');
        elemento.innerHTML=html;
        console.log(cont);
        console.log(ids);
        console.log(datos);
    });

}