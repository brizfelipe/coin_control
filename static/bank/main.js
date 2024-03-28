function get_banks() {
    console.log('a')
    $.ajax({
        url: '/bank/ajax/ajax_get_bank',
        type: 'GET',
        dataType: 'json',
        success: function (response) {
            insert_banks(response);
            return true
        },
        error: function (xhr, status, error) {
            console.error("Error:", error);
            return false
        }
    });
}

function insert_banks(response) {
    var table = $("#my-banks-table")
    table.empty()
    for (var i = 0; i < response.data.length; i++) {
        var row = response.data[i];
        console.log(row.name)
        var new_row = `
        <div id="bank-id-${row.id}" class="col-md-4">
            <div class="card h-100 border-0 shadow position-relative">
                <div class="btn-group position-absolute top-0 end-0 mt-2 me-2" role="group" aria-label="Card Actions">
                    <button id="delete-bank-id-${row.id}:${row.name}" type="button" data-bs-toggle="modal" data-bs-target="#modal-delete-bank" class="btn btn-outline-danger" aria-label="Delete">
                        <i class="bi bi-trash-fill"></i>
                    </button>
                    <button id="modal-update-bank-id-${row.id}"  type="button"  data-bs-toggle="modal" data-bs-target="#modal-update-bank" class="btn btn-outline-dark" aria-label="Edit">
                    <i class="bi bi-gear-fill"></i>
                    </button>
                </div>
                <div class="card-header bg-transparent border-0">
                    <h5 class="card-title">
                        <a href="#" class="btn btn-outline-secondary" id="bank-name-id-${row.id}">${row.name}</a>
                    </h5>
                </div> 
                <div class="card-body">
                    <small class="card-text text-muted" id="bank-description-id-${row.id}">${row.description}</small>
                </div>
            </div>
        </div>
    
    
    
    `
        table.append(new_row)
    }
}

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
    $('.nav_list a#bank-page').addClass('active');
    get_banks();

    $(document).on('click', '[id^="delete-bank-id-"]', function () {
        var bank = $(this).attr('id').split('id-')[1];
        var bank_id = bank.split(':')[0]
        var bank_name = bank.split(':')[1]
        $("#delete-bank-title").empty().append(
            `Deletar o banco: ${bank_id} (${bank_name})`
        )
    });

    $("#search-banks").on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("[id^='bank-id-']").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
        });
    });

    $(document).ready(function () {
        const observer = new MutationObserver(function (mutationsList, observer) {
            // Verificar apenas a primeira mutação
            const mutation = mutationsList[0];
            // Verificar se a div mudou
            if (mutation && mutation.target.id === 'create-bank-alert-primary') {
                const displayValue = $(mutation.target).css('display');
                if (displayValue === 'block') {
                    // A div mudou para 'block', então chame sua função
                    const result = get_banks();
                    // Se get_banks() retornar true ou false, pare de monitorar
                    if (result === true || result === false) {
                        observer.disconnect();
                    }
                }
            }
        });

        // Configurar o MutationObserver para observar mudanças no DOM
        observer.observe(document.body, { childList: true, subtree: true });
    });

    $("#delete-bank-button").on("click", function () {
        var modal_title = $("#delete-bank-title")
        var bank_id = modal_title.text().split(":")[1].split("(")[0]
        $.ajax({
            url: `/bank/ajax/ajax_delete_bank/${parseInt(bank_id)}`,
            type: 'GET',
            dataType: 'json',
            success: function (response) {
                get_banks();
                $("#close-modal-delete-bank").click()
                return true
            },
            error: function (xhr, status, error) {
                console.error("Error:", error);
                return false
            }
        });

    });

    $(document).on("click", "[id^='modal-update-bank-id-']", function () {
        var bank_id = $(this).attr('id').split("id-")[1];
        var name = $(`#bank-name-id-${parseInt(bank_id)}`).text()
        var description = $(`#bank-description-id-${parseInt(bank_id)}`).text()

        var form = $('#update_bank_forms');
        var id_field = form.find('input[id="update-id-bank"]');
        var name_field = form.find('input[id="update-name-bank"]');
        var description_field = form.find('input[id="update-description-bank"]');
        name_field.val(name);
        description_field.val(description);
        id_field.val(parseInt(bank_id));
        $("#update-id-bank").prop('disabled', true);
    });

    $('#udpate-bank-button').click(function (e) {
        e.preventDefault(); // Impede o envio padrão do formulário


        var idBank = $('#update-id-bank').val();
        var nameBank = $('#update-name-bank').val();
        var descriptionBank = $('#update-description-bank').val();

        $.ajax({
            type: 'POST',
            url: '/bank/ajax/ajax_update_bank',
            data: {
                "csrfmiddlewaretoken": $('input[name="csrfmiddlewaretoken"]').val(),
                "id_bank": idBank,
                "name_bank": nameBank,
                "description_bank": descriptionBank
            },
            dataType: 'json',
            success: function (response) {
                console.log(response.status)
                if(response.status===200){
                    get_banks();
                    mostrarAlerta(msg=response.message,id_alerta="update-bank-alert-primary")
                }else{
                    mostrarAlerta(msg=response.message,id_alerta="update-bank-alert-danger")
                }
            },
            error: function (xhr, errmsg, err) {
                // Lógica a ser executada em caso de erro
                console.log('Erro:', xhr.status + ': ' + xhr.responseText);
            }
        });
    });

});
