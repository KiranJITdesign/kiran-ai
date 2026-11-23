"""Execution entrypoint for python -m kiran_ai.cli."""
try:
    from kiran_ai.runtime.hardware import preload_windows_dlls
    preload_windows_dlls()
except Exception:
    pass

from kiran_ai.cli.main import main

if __name__ == "__main__":
    main()

