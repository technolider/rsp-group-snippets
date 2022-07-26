# def tui_append_person():
#     msg = {"ray_id": None,
#           "previous": [],
#           "service": "test",
#           "method": "test_append_person",
#           "ctx": {"person": {
#                         'type': 'маркетолог',
#                         'fio': 'Бурундуков Алексей Анатольевич',
#                         'age': 28,
#                         'exp': 6
#                  }}}
#
#     ask(BaseMessage(**msg), 'storage', 'append_person')

# def tui_search_person():
#     msg = {"ray_id": None,
#           "previous": [],
#           "service": "tui",
#           "method": "tui_search_person",
#           "ctx": {"type": "разработчик"}}
#
#     ask(BaseMessage(**msg), 'validate', 'validate_prof')
#
#
# @worker.method
# def tui_print(msg: BaseMessage):
#     for person in msg.ctx['persons']:
#         print(person)
#     quit()