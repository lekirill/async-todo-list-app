from datetime import datetime


def prepare_todo_list_insert(new_data: dict) -> (str, dict):
    """

    :param new_data:
    :return: prepared insert script and properly formatted data
    """
    for fld, value in new_data.items():
        if fld in ['plan_start', 'plan_finish']:
            new_data[fld] = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
    query = f"""
                    INSERT INTO public.to_do_list
                    ({', '.join(fld for fld in new_data.keys())})
                    VALUES({', '.join(f'${num + 1}' for num in range(len(new_data)))});
                """
    return query, new_data


def prepare_todo_list_update(new_data: dict, id: int) -> (str, dict):
    """
    :param new_data:
    :param id:
    :return: prepared update script and properly formatted data
    """
    for fld, value in new_data.items():
        if fld in ['plan_start', 'plan_finish']:
            new_data[fld] = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
    query = f"""
                UPDATE public.to_do_list 
                SET 
                    {', '.join(f'{key} = ${num + 1}' for key, num in zip(new_data.keys(), range(len(new_data))))},
                    updated_at = NOW()
                WHERE id = {id}
                """
    return query, new_data
