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

        query = {}
        # query_messages = []

        entities = tracker.latest_message['entities']
        for entity in entities:
            if entity['entity'] not in query:
                query[entity['entity']] = entity['value']
                # query_messages.append(
                #     f'Category: {tracker.get_slot("category")}')
                continue
            if entity['entity'] == 'price':
                price = entity['role']
                if price:
                    query['ordering'] = 'min_price' if price[0] == 'asc' else '-max_price'
                    # query_messages.append(
                    #     f'Price: {"Low" if price[0] == "asc" else "High"}')

        # dispatcher.utter_message(
        #     text=' | '.join(query_messages))
        dispatcher.utter_template('utter_list_product', tracker)
        dispatcher.utter_message(json_message={
            'payload': 'list_product',
            'data': query
        })
        dispatcher.utter_template('utter_sorry_product', tracker)

        return []


class ActionPlaceOrder(Action):
    def name(self) -> Text:
        return 'action_place_order'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_template('utter_place_order', tracker)
        dispatcher.utter_message(json_message={
            'payload': 'place_order',
            'data': {}
        })
        dispatcher.utter_template('utter_sorry_cart', tracker)

        return []


class ActionOrderStatus(Action):
    def name(self) -> Text:
        return 'action_order_status'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_template('utter_order_status', tracker)
        dispatcher.utter_message(json_message={
            'payload': 'order_status',
            'data': {}
        })
        dispatcher.utter_template('utter_sorry_order', tracker)

        return []
