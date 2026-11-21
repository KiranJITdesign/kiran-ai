"""Explicit desktop tasks with observable, bounded action execution."""
from kiran_ai.agent.autonomous import AutonomousAgent, AutonomousOverlay, AutonomousResult
from kiran_ai.agent.controller import DesktopAgentController
from kiran_ai.agent.desktop import Action, Decision, DesktopCancelled, DesktopDriver, DesktopError, Region

__all__ = [
    "Action",
    "AutonomousAgent",
    "AutonomousOverlay",
    "AutonomousResult",
    "Decision",
    "DesktopCancelled",
    "DesktopDriver",
    "DesktopError",
    "DesktopAgentController",
    "Region",
]

