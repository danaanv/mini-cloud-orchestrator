"""
Uso: coordina slices (grupos de VMs) y sus topologías.
Propósito: orquestar creación/borrado de slices, persistencia en JSON y conexión a red L2.
Estado: stub inicial; se completará en fases siguientes.
"""

from typing import Any


def create_slice(definition: Any) -> None:
    """Stub: crear un slice con su topología y VMs."""
    raise NotImplementedError("Implementar create_slice en Fase 2+")


def delete_slice(name: str) -> None:
    """Stub: borrar un slice y sus recursos."""
    raise NotImplementedError("Implementar delete_slice en Fase 2+")


def list_slices() -> None:
    """Stub: listar slices persistidos."""
    raise NotImplementedError("Implementar list_slices en Fase 2+")
