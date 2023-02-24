# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from .services import web_service

import logging
_logger = logging.getLogger(__name__)


class ActionFindProduct(Action):
    def name(self) -> Text:
        return 'action_find_product'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        _logger.error(tracker.get_slot('category'))

        query = {}
        query_messages = []

        if tracker.get_slot('category') != None:
            query['category'] = tracker.get_slot('category')
            query_messages.append(f'Category: {tracker.get_slot("category")}')

        if tracker.get_slot('color') != None:
            query['color'] = tracker.get_slot('color')
            query_messages.append(f'Color: {tracker.get_slot("color")}')

        if tracker.get_slot('size') != None:
            query['size'] = tracker.get_slot('size')
            query_messages.append(f'Size: {tracker.get_slot("size")}')

        _logger.error(tracker.latest_message['entities'])
        price = [entity['role'] for entity in tracker.latest_message['entities']
                 if entity['entity'] == 'price']

        if price:
            query['ordering'] = 'price' if price[0] == 'asc' else '-price'
            query_messages.append(
                f'Price: {"Low" if price[0] == "asc" else "High"}')

        list_product = web_service.get_product(query)

        if len(list_product) > 0:
            dispatcher.utter_message(
                text=' | '.join(query_messages))
            dispatcher.utter_template('utter_list_product', tracker)
            dispatcher.utter_message(json_message={
                'payload': 'list_product',
                'data': {
                    'list_product': list_product,
                    'type': 'list_product'
                }
            })
        else:
            dispatcher.utter_template('utter_sorry', tracker)

        return []
