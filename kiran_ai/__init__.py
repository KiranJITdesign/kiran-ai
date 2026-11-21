"""KiranAI by S Kiran: local conversation and research models.

Public objects load on first access so GGUF chat does not initialize PyTorch
training components merely by importing the package.
"""
from importlib import import_module

from kiran_ai.version import __version__

__author__ = "S Kiran"
_EXPORTS = {
    'KiranAI': ('kiran_ai.runtime.engine', 'KiranAI'),
    'Cluster': ('kiran_ai.cluster.coordinator', 'Cluster'),
    'ChatEngine': ('kiran_ai.runtime.chat', 'ChatEngine'),
    'SearchEngine': ('kiran_ai.search.engine', 'SearchEngine'),
    'KiranNanoModel': ('kiran_ai.model.transformer', 'KiranNanoModel'),
    'KiranNanoConfig': ('kiran_ai.model.config', 'KiranNanoConfig'),
}
__all__ = [*_EXPORTS, '__version__', '__author__']


def __getattr__(name):
    target = _EXPORTS.get(name)
    if target is None:
        raise AttributeError(f'module {__name__!r} has no attribute {name!r}')
    value = getattr(import_module(target[0]), target[1])
    globals()[name] = value
    return value


def __dir__():
    return sorted(set(globals()) | set(__all__))
