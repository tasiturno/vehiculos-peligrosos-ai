# vehiculos-peligrosos-ai

Proyecto: Detección de vehículos peligrosos (pipas, cisternas, vehículos con materiales peligrosos) usando visión por computadora e IA.

## Objetivo
- Detectar y alertar sobre vehículos que transporten materiales peligrosos en cámaras de la ciudad.
- Proveer un flujo de trabajo reproducible para entrenamiento, inferencia y despliegue.

## Instalación
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

## Uso
python src/main.py --input videos/ --output results/

