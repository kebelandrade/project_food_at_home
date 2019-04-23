$(function () {
        $("#Nombres").keyup(function () {
            var This = $("#Nombres");
            var user = $("#Nombres").val();
            var expre = /^[a-zA-z]+$/;
            var valido = expre.test(user);
            if (user == "" || user == null) {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            }

            if (valido) {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            } else {
                This.attr(
                    'style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
            }
        });

        $("#Apellidos").keyup(function () {
            var This = $("#Apellidos");
            var apellido = $("#Apellidos").val();
            var expre = /^[a-zA-z]+$/;
            var valido = expre.test(apellido);
            if (apellido == "" || apellido == null) {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            }

             if (valido) {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
            }
        });

        $("#Telefono").keyup(function () {
            var This = $("#Telefono");
            var tel = $("#Telefono").val();
            var expre = /^[0-9]+$/
            var valido = expre.test(tel);
            if (tel == "" || tel == null) {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            }

            if (tel.length > 9 || tel.length < 9) {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            }

             if (valido) {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
            }
        });

        $("#Usuario").keyup(function () {
            var This = $("#Usuario");
            var user = $("#Usuario").val();
            if (user == "" || user == null) {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            }
        });

        $("#Correo").keyup(function () {
            var This = $("#Correo");
            var correo = $("#Correo").val();
            var expre = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
            var valido = expre.test(correo);
            if (correo == "" || correo == null) {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            }

             if (valido) {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
            }
        });

        $("#Correo2").keyup(function () {
            var This = $("#Correo2");
            var correo1 = $("#Correo").val();
            var correo2 = $("#Correo2").val();
            if (correo2 == "" || correo2 == null) {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            }

            if (correo1 != correo2){
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            }

        });

        $("#Contra").keyup(function () {
           var This = $("#Contra");
           var contra = $("#Contra").val();
           if (contra == "" || contra == null) {
               This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
            } else {
               This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            }
        });

        $("#VerContra").keyup(function () {
            var This = $("#VerContra");
            var contra1 = $("#Contra").val();
            var contra2 = $("#VerContra").val();

            if (contra2 == "" || contra2 == null) {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            }

            if (contra1 != contra2){
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            }
        });
    });


/*--------------------------------------------------------------------------------------------------------------------------------------*/