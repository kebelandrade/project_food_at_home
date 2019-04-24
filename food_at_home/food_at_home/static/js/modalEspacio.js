$(function () {
        $("#Nombre-Espacio").keyup(function () {
            var This = $("#Nombre-Espacio");
            var user = $("#Nombre-Espacio").val();
            var expre = /^[a-zA-z]+$/;
            var valido = expre.test(user);
            if (user == "" || user == null) {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
                return false;
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            }

            if (valido) {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            } else {
                This.attr(
                    'style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
                return false;
            }
        });

        $("#Apellido-Espacio").keyup(function () {
            var This = $("#Apellido-Espacio");
            var apellido = $("#Apellido-Espacio").val();
            var expre = /^[a-zA-z]+$/;
            var valido = expre.test(apellido);
            if (apellido == "" || apellido == null) {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
                return false;
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            }

             if (valido) {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
                return false;
            }
        });

        $("#Telefono-Espacio").keyup(function () {
            var This = $("#Telefono-Espacio");
            var tel = $("#Telefono-Espacio").val();
            var expre = /^[0-9]+$/
            var valido = expre.test(tel);
            if (tel == "" || tel == null) {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
                return false;
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            }

            if (tel.length > 8 || tel.length < 8) {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
                return false;
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            }

             if (valido) {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
                return false;
            }
        });

        $("#Usuario-Espacio").keyup(function () {
            var This = $("#Usuario-Espacio");
            var user = $("#Usuario-Espacio").val();
            if (user == "" || user == null) {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
                return false;
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            }
        });

        $("#Correo-Espacio").keyup(function () {
            var This = $("#Correo-Espacio");
            var correo = $("#Correo-Espacio").val();
            var expre = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
            var valido = expre.test(correo);
            if (correo == "" || correo == null) {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
                return false;
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            }

             if (valido) {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
                return false;
            }
        });

        $("#Correo2-Espacio").keyup(function () {
            var This = $("#Correo2-Espacio");
            var correo1 = $("#Correo-Espacio").val();
            var correo2 = $("#Correo2-Espacio").val();
            if (correo2 == "" || correo2 == null) {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
                return false;
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            }

            if (correo1 != correo2){
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
                return false;
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            }

        });

        $("#Contra-Espacio").keyup(function () {
           var This = $("#Contra-Espacio");
           var contra = $("#Contra-Espacio").val();
           if (contra == "" || contra == null) {
               This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
               return false;
            } else {
               This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            }
        });

        $("#VerContra-Espacio").keyup(function () {
            var This = $("#VerContra-Espacio");
            var contra1 = $("#Contra-Espacio").val();
            var contra2 = $("#VerContra-Espacio").val();

            if (contra2 == "" || contra2 == null) {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
                return false;
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            }

            if (contra1 != contra2){
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
                return false;a
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            }
        });

        $("#Nombre-Restaurante").keyup(function () {
            var This = $("#Nombre-Restaurante");
            var user = $("#Nombre-Restaurante").val();
            var expre = /^[a-zA-z]+$/;
            var valido = expre.test(user);
            if (user == "" || user == null) {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
                return false;
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            }

            if (valido) {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            } else {
                This.attr(
                    'style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
                return false;
            }
        });

        $("#Telefono-Restaurante").keyup(function () {
            var This = $("#Telefono-Restaurante");
            var tel = $("#Telefono-Restaurante").val();
            var expre = /^[0-9]+$/;
            var valido = expre.test(tel);
            if (tel == "" || tel == null) {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
                return false;
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            }

            if (tel.length > 8 || tel.length < 8) {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
                return false;
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            }

             if (valido) {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
                return false;
            }
        });

        $("#Descripcion-Restaurante").keyup(function () {
            var This = $("#Descripcion-Restaurante");
            var user = $("#Descripcion-Restaurante").val();
            if (user == "" || user == null) {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(255,49,56,0.96)');
                return false;
            } else {
                This.attr('style', 'border:none; box-shadow:0px 0px 9px -1px rgba(145,245,42,0.96)');
            }
        });
    });