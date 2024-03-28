// Função para preencher os campos de edição com os dados do perfil
function preencherCamposEdicao() {
    // Captura dos valores dos elementos no card de perfil
    var username = $('#username').text();
    var email = $('#email').text();
    var firstName = $('#first_name').text();
    var lastName = $('#last_name').text();

    // Preenchimento dos campos de edição com os valores capturados
    $('#edit_username').val(username);
    $('#edit_email').val(email);
    $('#edit_first_name').val(firstName);
    $('#edit_last_name').val(lastName);
}


$(document).ready(function () {
    $('.nav_list a#perfil-page').addClass('active');
    
    $('#editarPerfilModal').on('show.bs.modal', function (event) {
        preencherCamposEdicao();
    });



});