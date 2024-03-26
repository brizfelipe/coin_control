// Função para mostrar uma mensagem de alerta temporária
function mostrarAlerta(msg,id_alerta,tempo = 5000) {
    // Seleciona a div de alerta
    var alerta = $(`#${id_alerta}`);

    // Define o texto da mensagem
    alerta.text(msg);

    // Mostra a div de alerta
    alerta.fadeIn();

    // Programa o desaparecimento da div após o tempo especificado
    setTimeout(function () {
        alerta.fadeOut();
    }, tempo);
}


$(document).ready(function () {

    $('#create_bank_forms').submit(function (event) {
        console.log('rola')
        event.preventDefault(); // Impede o envio padrão do formulário

        // Verificar se os campos estão preenchidos
        var nameBank = $('#name-bank').val();
        var descriptionBank = $('#description-bank').val();
        if (!nameBank || !descriptionBank) {
            var msg = "Por favor, preencha todos os campos."
            console.log(msg)
            mostrarAlerta(msg=msg,id_alerta="create-bank-alert-danger")
            return;
        }

        // Criar objeto de dados do formulário
        var formData = {
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
            'name': nameBank,
            'description': descriptionBank
        };

        // Enviar os dados do formulário via AJAX
        $.ajax({
            type: 'POST',
            url: '/bank/ajax/create_bank',
            data: formData,
            dataType: 'json',
            success: function (response) {
                // Lógica para lidar com a resposta do servidor

                if(response.status===200){
                    mostrarAlerta(msg=response.message,id_alerta="create-bank-alert-primary")
                }else{
                    mostrarAlerta(msg=response.message,id_alerta="create-bank-alert-danger")
                }
            },
            error: function (xhr, errmsg, err) {
                // Lógica para lidar com erros de requisição
                console.log(xhr.status + ': ' + xhr.responseText);
            }
        });
    });
});
