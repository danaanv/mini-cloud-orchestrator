# mini-cloud-orchestrator

Este proyecto corresponde al Proyecto 1 de la ruta de preparación para TEL141, y consiste en implementar un Mini Cloud Orchestrator que gestione el ciclo de vida de máquinas virtuales utilizando Python, libvirt y KVM. El objetivo es construir una base sólida en orquestación, virtualización y redes L2 antes de avanzar hacia placement inteligente, GitOps o telemetría avanzada.

El orquestador permite crear, eliminar y administrar slices, entendidos como conjuntos de VMs conectadas mediante una topología definida (lineal, anillo, etc.) y unidas a través de un bridge de Linux que actúa como switch virtual. También incorpora un sistema de persistencia en JSON para almacenar la configuración y el estado de cada slice.

Características principales
- Creación y destrucción de VMs usando la API de libvirt
- Gestión de slices y topologías simples (lineal, anillo)
- Networking L2 mediante bridges de Linux
- CLI desarrollada con Click para controlar toda la orquestación
- Persistencia del estado en slices.json

## Arquitectura
orchestrator.py      # CLI principal
vm_manager.py        # Creación/destrucción de VMs (libvirt)
network_manager.py   # Configuración del bridge y conexiones L2
slice_manager.py     # Coordinación completa de slices
slices.json          # Estado y configuración persistente

## Objetivo académico

Este proyecto establece los fundamentos necesarios para el curso TEL141, cubriendo la creación/borrado de slices, la orquestación básica, el manejo de topologías y la implementación de redes virtuales L2. Además, sirve como punto de partida para los proyectos posteriores:

- VM Placement con teoría de colas (Proyecto 2)
- Integración GitOps con Flux (Proyecto 3)
- Telemetría eBPF (Proyecto opcional)
