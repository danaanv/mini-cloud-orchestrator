"""
Uso: capa de gestión de VMs sobre libvirt.
Propósito: centralizar creación, destrucción, consulta de estado y configuración de dominios.
Estado: stub inicial; se implementará en fases siguientes con libvirt.
"""

from typing import Any


def create_vm(config: Any) -> None:
    """Stub: crear VM con la configuración provista."""
    raise NotImplementedError("Implementar create_vm con libvirt en Fase 2+")


def delete_vm(name: str) -> None:
    """Stub: eliminar VM por nombre."""
    raise NotImplementedError("Implementar delete_vm con libvirt en Fase 2+")


def get_vm_status(name: str) -> str:
    """Stub: devolver estado de la VM."""
    raise NotImplementedError("Implementar get_vm_status en Fase 2+")
