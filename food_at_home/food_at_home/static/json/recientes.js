axios.get('categorias').
then(function(res){
  let html = "";
  console.log(res.data)
  for(var i=0; i< res.data.length; i++){
    html +=`
        <div class="col-sm" >
            <div class="card text-center" style="width: 18rem; margin-top: 50px">
            <img style="height:100px; width:100px; background-color: #4e555b; margin: 20px" src="media/${res.data[i].fields.img}"
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
  var elemento = document.getElementById('seccion-seccion2')
  elemento.innerHTML=html

  // agregar event listeners
  var botones = elemento.getElementsByClassName('btn-ver-res')
  for(let i = 0; i < botones.length; i++) {
    botones[i].addEventListener('click', function() {
      axios.get('administrador/verrestaurante/' + botones[i].dataset.id ).
      then(function(res){
        let html = "";
        console.log(res.data)
        for(var i=0; i< res.data.length; i++){
          html +=`
          <tr >
            <td>${res.data[i].fields.nombre}</td>
          </tr>
          `
        }
      var elemento = document.getElementById('table-res')
      elemento.innerHTML=html
      })
    })
  }

})
