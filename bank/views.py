from django.shortcuts import render,redirect
from .src import database,schema
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required
def index(request):
    user_id = request.user.id
    context = {}
    bank_is_true = database.check_there_banks_registered_by_user(user_id)
    if bank_is_true:
        context['banks_existis'] = True
    else:
        context['banks_existis'] = False
    return render(request,"bank/index.html",context)

def ajax_get_banks(request):
    user_id = request.user.id
    my_banks = schema.banks_to_index_page(user_id)
    return JsonResponse({'data': my_banks, 'status': 200})

def ajax_create_bank(request):
    if request.method == 'POST':
        # Obtém os dados do formulário POST
        nome = request.POST.get('name')
        descricao = request.POST.get('description')
        user_id = request.user.id
        
        # Insere os dados no modelo Bank usando a função inserir_dados_bank
        try:
            novo_banco = database.inserir_dados_bank(user_id, nome, descricao)
            
            if novo_banco:
                return JsonResponse({'message': 'Banco criado com sucesso', 'status': 200})
            else:
                return JsonResponse({'message': 'Erro ao criar o banco', 'status': 500})
        except Exception as e:
            return JsonResponse({'message':str(e), 'status': 500})
    else:
        
        return JsonResponse({'message': 'Método inválido', 'status': 400})

def ajax_delete_bank(request,id):
    status = database.delete_bank_by_bank_id(bank_id=id)
    if status:
        return JsonResponse({'message': 'Banco deletado com sucesso.', 'status': 200})
    else:
        return JsonResponse({'message': 'Erro ao deletar banco de dados.', 'status': 200})


def ajax_udpate_bank(request) :
    status = database.update_bank_by_bank_id(
        id=request.POST['id_bank'],
        name=request.POST['name_bank'],
        description=request.POST['description_bank']
    )
    if status:
        return JsonResponse({'message': 'Banco atualizado com sucesso.', 'status': 200})
    else:
        return JsonResponse({'message': 'Erro ao atualizar banco.', 'status': 400})