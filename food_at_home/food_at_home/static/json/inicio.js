axios.get('inicio').
then(function(rest){
  let html = "";
  for(var i=0; i< rest.data.length; i++){
    html +=`
        <div class="col-sm" >
            <div class="card text-center" style="width: 18rem; margin-top: 50px">
            <img style="height:100px; width:100px; background-color: #4e555b; margin: 20px" src="../media/${res.data[i].fields.img}"
                             class="card-img-top rounded-circle mx-auto d-block" alt="...">
                <div class="card-body">
                <h5 class="card-title">${res.data[i].fields.nombre}</h5>
                <p class="card-text">${res.data[i].fields.descripcion}</p>
                <a href="" class="btn btn-primary btn-ver-res" data-toggle="modal" data-id="${res.data[i].pk}" data-target="#modalVerRestaurante">Ver restaurantes</a>
                </div>
              </div>
          </div>
    `
  }
  var elemento = document.getElementById('seccion-cliente-categoria')
  elemento.innerHTML=html
