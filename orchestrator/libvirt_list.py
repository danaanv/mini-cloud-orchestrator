#!/usr/bin/env python3
"""Script simple que se conecta a libvirt (qemu:///system) y lista dominios/VMs.
Ejecutar: python3 orchestrator/libvirt_list.py
"""
import sys

try:
    import libvirt
except Exception as e:
    print("No se puede importar 'libvirt'. Asegúrate de instalar 'python3-libvirt' o 'libvirt-python'.\nError:", e)
    sys.exit(1)


def state_to_str(state):
    mapping = {
        libvirt.VIR_DOMAIN_NOSTATE: 'no state',
        libvirt.VIR_DOMAIN_RUNNING: 'running',
        libvirt.VIR_DOMAIN_BLOCKED: 'blocked',
        libvirt.VIR_DOMAIN_PAUSED: 'paused',
        libvirt.VIR_DOMAIN_SHUTDOWN: 'shutdown',
        libvirt.VIR_DOMAIN_SHUTOFF: 'shutoff',
        libvirt.VIR_DOMAIN_CRASHED: 'crashed',
        libvirt.VIR_DOMAIN_PMSUSPENDED: 'pmsuspended',
    }
    return mapping.get(state, str(state))


def main():
    try:
        conn = libvirt.open('qemu:///system')
    except libvirt.libvirtError as e:
        print('Error: no se pudo conectar a libvirt en qemu:///system. Detalle:', e)
        sys.exit(2)

    try:
        print('Conectado a libvirt:', conn.getURI())
        domains = conn.listAllDomains(0)
        if not domains:
            print('No hay dominios definidos.')
            return

        print(f'Se encontraron {len(domains)} dominios:')
        for d in domains:
            try:
                name = d.name()
            except Exception:
                name = '<nombre-desconocido>'
            try:
                dom_id = d.ID()
            except Exception:
                dom_id = -1
            try:
                uuid = d.UUIDString()
            except Exception:
                uuid = '<uuid-desconocida>'
            try:
                state, reason = d.state()
                state_s = state_to_str(state)
            except Exception:
                state_s = '<estado-desconocido>'

            print(f"- {name} (id={dom_id}, uuid={uuid[:8]}...) estado={state_s}")
    finally:
        conn.close()


if __name__ == '__main__':
    main()
