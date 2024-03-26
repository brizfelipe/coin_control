from ..models import Bank
from django.contrib.auth.models import User


def get_user_by_id(user_id):
    user = User.objects.get(id=user_id)
    return user

def check_there_banks_registered_by_user(user_id:int)->bool:
    banks = get_all_banks_by_user_id(user_id)
    if banks.exists():
        return True 
    return False


def get_all_banks_by_user_id(user_id):
    banks = Bank.objects.filter(user=user_id)
    return banks


def inserir_dados_bank(user_id, nome, descricao):
    try:
        user = get_user_by_id(user_id)
        novo_banco = Bank.objects.create(
            user=user,
            name=nome,
            description=descricao
        )
        return novo_banco
    except Exception as e:
        raise Exception("Erro ao inserir dados no banco")


def delete_bank_by_bank_id(bank_id):
    bank = Bank.objects.filter(id=bank_id)
    bank.delete()
    return True


def update_bank_by_bank_id(id, name, description):
    try:
        bank = Bank.objects.get(id=id)
        bank.name = name
        bank.description = description
        bank.save()
        return bank  
    except Bank.DoesNotExist:
        return None  
    except Exception as e:
        print(e)  
        return None 