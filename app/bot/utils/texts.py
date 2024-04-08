from abc import abstractmethod, ABCMeta

# Adicione outros idiomas e seus códigos correspondentes conforme necessário.
# Você também pode manter apenas um idioma removendo a linha com o idioma indesejado.
SUPPORTED_LANGUAGES = {
    "br": "🇧🇷 Português Brasileiro",
    "en": "🇬🇧 English",
}


class Text(metaclass=ABCMeta):
    """
    Classe base abstrata para lidar com dados de texto em diferentes idiomas.
    """

    def __init__(self, language_code: str) -> None:
        """
        Inicializa a instância Text com o código de idioma especificado.

        :param language_code: O código do idioma (por exemplo, "en" ou "br").
        """
        self.language_code = language_code if language_code in SUPPORTED_LANGUAGES.keys() else "en"

    @property
    @abstractmethod
    def data(self) -> dict:
        """
        Propriedade abstrata a ser implementada por subclasses. Representa os dados de texto específicos do idioma.

        :return: Dicionário contendo dados de texto específicos do idioma.
        """
        raise NotImplementedError

    def get(self, code: str) -> str:
        """
        Recupera o texto correspondente ao código fornecido no idioma atual.

        :param code: O código associado ao texto desejado.
        :return: O texto no idioma atual.
        """
        return self.data[self.language_code][code]


class TextMessage(Text):
    """
    Subclasse de Text para gerenciar mensagens de texto em diferentes idiomas.
    """

    @property
    def data(self) -> dict:
        """
        Fornece dados de texto específicos do idioma para mensagens de texto.

        :return: Dicionário contendo dados de texto específicos do idioma para mensagens de texto.
        """
        return {
            "en": {
                "select_language": "👋 <b>Hello</b>, {full_name}!\n\nSelect language:",
                "change_language": "<b>Select language:</b>",
                "main_menu": "<b>Write your question</b>, and we will answer you as soon as possible:",
                "message_sent": "<b>Message sent!</b> Expect a response.",
                "message_edited": (
                    "<b>The message was edited only in your chat.</b> "
                    "To send an edited message, send it as a new message."
                ),
                "source": (
                    "Source code available at "
                    "<a href=\"https://github.com/nessshon/support-bot\">GitHub</a>"
                ),
                "user_started_bot": (
                    "<b>User {name} started the bot!</b>\n\n"
                    "List of available commands:\n\n"
                    "• /ban\n"
                    "Block/Unblock user"
                    "<blockquote>Block the user if you do not want to receive messages from him.</blockquote>\n\n"
                    "• /silent\n"
                    "Activate/Deactivate silent mode"
                    "<blockquote>When silent mode is enabled, messages are not sent to the user.</blockquote>\n\n"
                    "• /information\n"
                    "User information"
                    "<blockquote>Receive a message with basic information about the user.</blockquote>"
                ),
                "user_restarted_bot": "<b>User {name} restarted the bot!</b>",
                "user_stopped_bot": "<b>User {name} stopped the bot!</b>",
                "user_blocked": "<b>User blocked!</b> Messages from the user are not accepted.",
                "user_unblocked": "<b>User unblocked!</b> Messages from the user are being accepted again.",
                "blocked_by_user": "<b>Message not sent!</b> The bot has been blocked by the user.",
                "user_information": (
                    "<b>ID:</b>\n"
                    "- <code>{id}</code>\n"
                    "<b>Name:</b>\n"
                    "- {full_name}\n"
                    "<b>Status:</b>\n"
                    "- {state}\n"
                    "<b>Username:</b>\n"
                    "- {username}\n"
                    "<b>Blocked:</b>\n"
                    "- {is_banned}\n"
                    "<b>Registration date:</b>\n"
                    "- {created_at}"
                ),
                "message_not_sent": "<b>Message not sent!</b> An unexpected error occurred.",
                "message_sent_to_user": "<b>Message sent to user!</b>",
                "silent_mode_enabled": (
                    "<b>Silent mode activated!</b> Messages will not be delivered to the user."
                ),
                "silent_mode_disabled": (
                    "<b>Silent mode deactivated!</b> The user will receive all messages."
                ),
            },
            "br": {
                "select_language": "👋 <b>Olá</b>, {full_name}!\n\nSelecione o idioma:",
                "change_language": "<b>Selecione o idioma:</b>",
                "main_menu": "<b>Escreva sua pergunta</b> e responderemos o mais rápido possível:",
                "message_sent": "<b>Mensagem enviada!</b> Aguarde uma resposta.",
                "message_edited": (
                    "<b>A mensagem foi editada apenas no seu chat.</b> "
                    "Para enviar uma mensagem editada, envie-a como uma nova mensagem."
                ),
                "source": (
                    "Código-fonte disponível em "
                    "<a href=\"https://github.com/nessshon/support-bot\">GitHub</a>"
                ),
                "user_started_bot": (
                    "<b>O usuário {name} iniciou o bot!</b>\n\n"
                    "Lista de comandos disponíveis:\n\n"
                    "• /ban\n"
                    "Bloquear/Desbloquear usuário"
                    "<blockquote>Bloqueie o usuário se não quiser receber mensagens dele.</blockquote>\n\n"
                    "• /silent\n"
                    "Ativar/Desativar modo silencioso"
                    "<blockquote>Quando o modo silencioso está ativado, as mensagens não são enviadas para o usuário.</blockquote>\n\n"
                    "• /information\n"
                    "Informações do usuário"
                    "<blockquote>Receba uma mensagem com informações básicas sobre o usuário.</blockquote>"
                ),
                "user_restarted_bot": "<b>O usuário {name} reiniciou o bot!</b>",
                "user_stopped_bot": "<b>O usuário {name} parou o bot!</b>",
                "user_blocked": "<b>Usuário bloqueado!</b> Mensagens do usuário não são aceitas.",
                "user_unblocked": "<b>Usuário desbloqueado!</b> Mensagens do usuário estão sendo aceitas novamente.",
                "blocked_by_user": "<b>Mensagem não enviada!</b> O bot foi bloqueado pelo usuário.",
                "user_information": (
                    "<b>ID:</b>\n"
                    "- <code>{id}</code>\n"
                    "<b>Nome:</b>\n"
                    "- {full_name}\n"
                    "<b>Status:</b>\n"
                    "- {state}\n"
                    "<b>Nome de usuário:</b>\n"
                    "- {username}\n"
                    "<b>Bloqueado:</b>\n"
                    "- {is_banned}\n"
                    "<b>Data de registro:</b>\n"
                    "- {created_at}"
                ),
                "message_not_sent": "<b>Mensagem não enviada!</b> Ocorreu um erro inesperado.",
                "message_sent_to_user": "<b>Mensagem enviada para o usuário!</b>",
                "silent_mode_enabled": (
                    "<b>Modo silencioso ativado!</b> As mensagens não serão entregues ao usuário."
                ),
                "silent_mode_disabled": (
                    "<b>Modo silencioso desativado!</b> O usuário receberá todas as mensagens."
                ),
            },
        }
