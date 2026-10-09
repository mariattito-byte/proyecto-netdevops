# 🚀 Proyecto Integrador NetDevOps

Este repositorio contiene la infraestructura como código (IaC) para el despliegue de servidores virtualizados, automatización con Ansible y monitoreo de red vía RESTCONF.

---

## 📌 Guía Rápida para Exposición

### 1. Despliegue de Servidores (Docker)
- **Red `macvlan`:** Subred `172.23.18.0/24` en interfaz `ens37`.
- **Servidores desplegados (Ubuntu 22.04):**
  - `srv-web`: `172.23.18.11`
  - `srv-ftp`: `172.23.18.12`
  - `srv-mail`: `172.23.18.13`
  - `srv-dns`: `172.23.18.14`
- **Interfaz Shim (`mac0`):** `172.23.18.250` para comunicación host-contenedor.

---

## 🛠️ Archivos del Proyecto

- **`hosts`:** Archivo de inventario de Ansible con conector nativo de Docker.
- **`playbook.yml`:** Aprovisionamiento automático de servicios (NGINX, VSFTPD, Postfix y BIND9).
- **`script_profesor.py`:** Script en Python para consulta de telemetría e interfaces mediante **RESTCONF/YANG** en Switches Cisco (`172.23.18.224` y `.223`).

---

## ⚡ Comandos Rápidos de Demostración

```bash
# 1. Ver contenedores en ejecución
sudo docker ps

# 2. Ejecutar Playbook de Ansible
ansible-playbook -i hosts playbook.yml

# 3. Ejecutar script de telemetría
python3 script_profesor.py
