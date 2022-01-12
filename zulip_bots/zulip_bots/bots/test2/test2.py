# See readme.md for instructions on running this code.

from typing import Any, Dict

from zulip_bots.lib import BotHandler


class JsLeadHandler:
    def usage(self) -> str:
        return """
        Simple Zulip bot that will respond to any query with a asked to the "js Lead".

        This bot answers all the queries related to the javascript which are asked to the javascript lead in the javascript stream.

        """

    def handle_message(self, message: Dict[str, Any], bot_handler: BotHandler) -> None:
        print("sender data:", message)

        content = "beep boop"  # type: str
        bot_handler.send_reply(message, content)

        emoji_name = "wave"  # type: str
        bot_handler.react(message, emoji_name)
        return


handler_class = JsLeadHandler
