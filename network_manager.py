"""
Uso: gestiona redes L2 para las VMs (bridges de Linux).
Propósito: crear/eliminar bridges, conectar interfaces virtuales y soportar topologías (lineal/anillo).
Estado: stub inicial; se completará en fases siguientes.
"""

from typing import Any


def create_bridge(name: str) -> None:
    """Stub: crear un bridge Linux."""
    raise NotImplementedError("Implementar create_bridge en Fase 2+")


def delete_bridge(name: str) -> None:
    """Stub: eliminar un bridge Linux."""
    raise NotImplementedError("Implementar delete_bridge en Fase 2+")


def attach_interface(bridge: str, iface: str) -> None:
    """Stub: unir interfaz virtual al bridge."""
    raise NotImplementedError("Implementar attach_interface en Fase 2+")
