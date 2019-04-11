axios.get('categorias').
then(function(res){
  let html = "";
  console.log(res.data)
  for(var i=0; i< res.data.length; i++){
    html +=`

        <div class="col-sm" >
            <div class="card text-center" style="width: 18rem; margin-top: 50px">
            <img style="height:100px; width:100px; background-color: #4e555b; margin: 20px" src="#"
                             class="card-img-top rounded-circle mx-auto d-block" alt="...">
                <div class="card-body">
                <h5 class="card-title">${res.data[i].fields.nombre}</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                <a href="" class="btn btn-primary">Ver restaurantes</a>
                </div>
              </div>
          </div>
    `
  }
  var elemento = document.getElementById('seccion-seccion2')
  elemento.innerHTML=html
})
