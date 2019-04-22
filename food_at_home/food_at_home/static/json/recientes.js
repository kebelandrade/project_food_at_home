axios.get('categorias').
then(function(res){
  let html = "";
  console.log(res.data);
  for(var i=0; i< res.data.length; i++){
    html +=`
    <div class="card" style="width: 18rem; margin: 20px 20px; height:25rem; ">
        <img src="media/${res.data[i].fields.img}" class="card-img-top rounded-circle mx-auto d-block" style="height:200px; width:200px; margin-top:10px;">
        <div class="card-body">
            <h5 class="card-title">${res.data[i].fields.nombre}</h5>
            <p class="card-text">${res.data[i].fields.descripcion}</p>
            <a href="" class="btn btn-warning btn-ver-res" data-toggle="modal" data-id="${res.data[i].pk}" data-target="#modalVerRestaurante">Ver restaurantes</a>
        </div>
    </div>

    `
  }
  var elemento = document.getElementById('cats');
  elemento.innerHTML=html;

  // agregar event listeners
  var botones = elemento.getElementsByClassName('btn-ver-res');
  for(let i = 0; i < botones.length; i++) {
    botones[i].addEventListener('click', function() {
      axios.get('administrador/verrestaurante/' + botones[i].dataset.id ).
      then(function(res){
        let html = "";
        console.log(res.data);
        for(var i=0; i< res.data.length; i++){
          html +=`
          <tr >
            <td>${res.data[i].fields.nombre}</td>
            <td><a href="cliente/vermenu/${res.data[i].pk}">Ver menu</a></td>
          </tr>
          `
        }
      var elemento = document.getElementById('table-res');
      elemento.innerHTML=html
      })
    })
  }

});
axios.get('todos-res').
then(function(resta){
  let html = "";
  // console.log(res.data)
  for(var i=0; i< resta.data.length; i++){
    html +=`
    <div class="card" style="width: 18rem; margin: 20px 20px; height:25rem; ">
        <img src="media/${resta.data[i].fields.img}" class="card-img-top rounded-circle mx-auto d-block" style="height:200px; width:200px; margin-top:10px;">
        <div class="card-body">
            <h5 class="card-title">${resta.data[i].fields.nombre}</h5>
            <p class="card-text">${resta.data[i].fields.descripcion}</p>
            <a href="menu/${resta.data[i].pk}" class="btn btn-warning btn-ver-res">Ver Menu</a>
        </div>
    </div>
    `
  }
  var elemento = document.getElementById('restaurante')
  elemento.innerHTML=html

})
// <div class="card" style="width: 18rem; margin: 20px 20px ">
//     <img src="media/${res.data[i].fields.img}" class="card-img-top rounded-circle mx-auto d-block" style="height:100px; width:100px;">
//     <div class="card-body">
//         <h5 class="card-title">${res.data[i].fields.nombre}</h5>
//         <p class="card-text">${res.data[i].fields.descripcion}</p>
//         <a href="" class="btn btn-warning btn-ver-res" data-toggle="modal" data-id="${res.data[i].pk}" data-target="#modalVerRestaurante">Ver restaurantes</a>
//     </div>
// </div>
