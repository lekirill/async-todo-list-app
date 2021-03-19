from sanic.request import Request
from app.utils.decorators import validate_json
from datetime import datetime

from app.schema.todo_note import AddNoteSchema
from app.utils import http_responses
from app import scripts


@validate_json(AddNoteSchema)
async def add(request: Request):
    payload = dict(request.json)
    query, data = scripts.prepare_todo_list_insert(payload)
    await request.app.todo_db.insert(query, data.values())
    return http_responses.http_ok('Note was added')


@validate_json(AddNoteSchema)
async def edit(request: Request, id):
    payload = dict(request.json)
    query, data = scripts.prepare_todo_list_update(payload, id)
    await request.app.todo_db.update(query, list(data.values()))
    return http_responses.http_ok(f'Note {id} was updated')


@validate_json(AddNoteSchema)
async def edit(request: Request, id):
    payload = dict(request.json)
    query, data = scripts.prepare_todo_list_update(payload, id)
    await request.app.todo_db.update(query, list(data.values()))
    return http_responses.http_ok(f'Note {id} was updated')


async def del_by_id(request: Request, id):
    await request.app.todo_db.update("DELETE FROM public.to_do_list WHERE id = $1", (id,))
    return http_responses.http_ok(f'Note {id} was DELETED')


async def set_done(request: Request, id):
    await request.app.todo_db.update(f"""
        UPDATE public.to_do_list
        SET is_finished = True, finished_at = NOW(), updated_at = NOW()
        WHERE id = $1
        """, (id,))
    return http_responses.http_ok(f'Note {id} id done')


async def set_in_progress(request: Request, id):
    await request.app.todo_db.update(f"""
            UPDATE public.to_do_list
            SET is_in_progress = True, started_at = NOW(), updated_at = NOW()
            WHERE id = $1
            """, (id,))
    return http_responses.http_ok(f'Note {id} is in progress')


async def set_undone(request: Request, id):
    await request.app.todo_db.update(f"""
            UPDATE public.to_do_list
            SET is_finished = False, finished_at = Null, updated_at = NOW()
            WHERE id = $1
            """, (id,))
    return http_responses.http_ok(f'Note {id} set undone')


async def set_off_progress(request: Request, id):
    await request.app.todo_db.update(f"""
            UPDATE public.to_do_list
            SET is_in_progress = False, updated_at = NOW()
            WHERE id = $1
            """, (id,))
    return http_responses.http_ok(f'Note {id} set off progress')
