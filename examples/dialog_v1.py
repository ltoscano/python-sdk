# coding=utf-8
import json
from watson_developer_cloud import DialogV1 as Dialog


dialog = Dialog(username='YOUR SERVICE USERNAME',
                password='YOUR SERVICE PASSWORD')

print(json.dumps(dialog.get_dialogs(), indent=2))

with open('../resources/dialog.xml') as dialog_file:
    print(json.dumps(dialog.create_dialog(
        dialog_file=dialog_file, name='pizza_test_9'), indent=2))

# dialog_id = '98734721-8952-4a1c-bb72-ef9957d4be93'

# with open('../resources/dialog.xml') as dialog_file:
#     print(json.dumps(dialog.update_dialog(dialog_file=dialog_file, dialog_id=dialog_id), indent=2))

# print(json.dumps(dialog.get_content(dialog_id), indent=2))
#
# initial_response = dialog.conversation(dialog_id)
#
# print(json.dumps(initial_response, indent=2))
#
# print(json.dumps(dialog.conversation(dialog_id=dialog_id,
#                                      dialog_input='What type of toppings do you have?',
#                                      conversation_id=initial_response['conversation_id'],
# client_id=initial_response['client_id']), indent=2))

# print(json.dumps(dialog.delete_dialog(dialog_id='63b0489c-cd97-45ef-8800-4e7c310eeb19'), indent=2))