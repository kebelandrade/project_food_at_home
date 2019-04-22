axios.get('categoria').
then(function(res){
  let html = "";
  for(var i=0; i< res.data.length; i++){
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

  var botones = elemento.getElementsByClassName('btn-ver-res')
  for(let i = 0; i < botones.length; i++) {
    botones[i].addEventListener('click', function() {
      axios.get('../administrador/verrestaurante/' + botones[i].dataset.id ).
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


  axios.get('restaurante').
  then(function(res){
    let html = "";
    // console.log(res.data)
    for(var i=0; i< res.data.length; i++){
      html +=`
          <div class="col-sm" >
              <div class="card text-center" style="width: 18rem; margin-top: 50px">
              <img style="height:100px; width:100px; background-color: #4e555b; margin: 20px" src="../media/${res.data[i].fields.img}"
                               class="card-img-top rounded-circle mx-auto d-block" alt="...">
                  <div class="card-body">
                  <h5 class="card-title">${res.data[i].fields.nombre}</h5>
                  <p class="card-text">${res.data[i].fields.descripcion}</p>
                  <a href="" class="btn btn-primary" data-toggle="modal" >Ver Menu</a>
                  </div>
                </div>
            </div>
      `
    }
    var elemento = document.getElementById('seccion-cliente-restaurante')
    elemento.innerHTML=html

  })

  axios.get('ciudad').
  then(function(res){
    let html = "";
    var ids = []
    for(var i=0; i< res.data.length; i++){
      html +=`

            <hr class="m-0">
            <section id="ccc-${res.data[i].pk}">
              <h5 >${res.data[i].fields.nombre}</h5>
              <section id="ccccc${res.data[i].pk}">
              </section>
            </section>
            <hr class="m-0">
      `
      ids.push(res.data[i].pk)
    }

    var elemento = document.getElementById('seccion-cliente-item-ciudades')
    elemento.innerHTML=html




    for (var c = 0; c < ids.length; c++) {
      axios.get('query-ciudad/' +(ids[c])).then(function(rest){
        console.log("entro");
        let html = "";
        //   for(var i=0; i< rest.data.length; i++){
        //     html +=`
        //
        //           <p>${rest.data[i].fields.nombre} </p>
        //     `
        // }
        // var element = document.getElementById('ccccc'+2)
        // elemento.innerHTML=html

      })
    }


  })

  // axios.get('query-ciudad').
  // then(function(rest){
  //   console.log("entro");
  //   let html = "";
  //   // console.log(res.data)
  //   for(var i=0; i< rest.data.length; i++){
  //     html +=`
  //
  //           <p>${rest.data[i].fields.nombre} </p>
  //     `
  //   }
  //   var elemento = document.getElementById('probando')
  //   elemento.innerHTML=html
  //
  // })
