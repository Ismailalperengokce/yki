# YKI — Ground Control Station

Ground control / communication console used for the TEKNOFEST Savasan IHA (Fighter UAV) competition — handles telemetry and API communication with the competition server during the mission.

---

### Project Structure

yki/
- backend/
  - main.py              (Main program)
  - api_client.py        (TEKNOFEST API client, empty)
  - telemetry_manager.py (Telemetry manager, empty)
  - requirements.txt     (Dependencies)
  - camera/              (Image capture and processing)
- config.py               (Configuration)
- README.md               (This file)

### Setup

cd backend
pip install -r requirements.txt
python main.py

### Status

Work in progress — core client/telemetry modules under active development.
