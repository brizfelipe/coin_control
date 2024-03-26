from .database import get_all_banks_by_user_id


def banks_to_index_page(user_id):
    banks = get_all_banks_by_user_id(user_id)
    return list(banks.values())
    