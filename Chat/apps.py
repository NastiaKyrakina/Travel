from django.apps import AppConfig
from django.utils.autoreload import autoreload_started


def my_watchdog(sender, **kwargs):
    sender.watch_file('/tmp/foo.bar')
    # to listen to multiple files, use watch_dir, e.g.
    # sender.watch_dir('/tmp/', '*.bar')


class ChatConfig(AppConfig):
    name = 'Chat'

    def ready(self):
        autoreload_started.connect(my_watchdog)