"""Local chat and research inference, loaded only when requested."""
from importlib import import_module

_EXPORTS = {
    'HardwareBackend': ('kiran_ai.runtime.engine', 'HardwareBackend'),
    'GenerationConfig': ('kiran_ai.runtime.engine', 'GenerationConfig'),
    'detect_best_hardware': ('kiran_ai.runtime.engine', 'detect_best_hardware'),
    'InferenceEngine': ('kiran_ai.runtime.engine', 'InferenceEngine'),
    'KiranAI': ('kiran_ai.runtime.engine', 'KiranAI'),
    'ChatEngine': ('kiran_ai.runtime.chat', 'ChatEngine'),
    'ChatMessage': ('kiran_ai.runtime.chat', 'ChatMessage'),
}
__all__ = list(_EXPORTS)


def __getattr__(name):
    target = _EXPORTS.get(name)
    if target is None:
        raise AttributeError(f'module {__name__!r} has no attribute {name!r}')
    value = getattr(import_module(target[0]), target[1])
    globals()[name] = value
    return value


def __dir__():
    return sorted(set(globals()) | set(__all__))

