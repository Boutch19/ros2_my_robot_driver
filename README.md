# 🚀 ROS2 Workspace — Feetech STS Driver (my_robot_driver)

Workspace ROS2 complet (`ros2_ws_2`) contenant un driver autonome pour les servos **Feetech STS**, basé sur le SDK Python vendorisé (`scservo_sdk`).  
Projet minimaliste, propre, sans dépendances externes (pas de LeRobot).

---

# 📦 Contenu du workspace

```
ros2_ws_2/
  src/
    my_robot_driver/
      my_robot_driver/
        motor_manager.py
        vendor/
          scservo_sdk/
            port_handler.py
            sms_sts.py
            scscl.py
            packet_handler.py
            protocol_packet_handler.py
            scservo_def.py
            __init__.py
        __init__.py
      setup.py
      package.xml
```

- **`motor_manager.py`** — Node ROS2 :
  - ouvre le port série
  - active le torque
  - lit les positions
  - publie `JointState`
  - convertit ticks ↔ radians
  - supporte `SMS_STS` et `SMS_STS_1M`

- **`vendor/scservo_sdk/`**  
  SDK Feetech **copié localement** (MIT), aucun pip externe.

---

# 🎯 Objectifs du projet

- Workspace ROS2 propre et autonome  
- Driver Feetech simple et 100% local  
- Lecture de positions et publication ROS2  
- Contrôle par `JointState` (optionnel)  
- Base parfaite pour un futur robot perso  

---

# 🛠️ Installation

### 1) Cloner le workspace

```bash
git clone git@github.com:<TON_USER>/ros2_ws_2.git
cd ros2_ws_2
```

### 2) (Optionnel) Environnement virtuel

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Build ROS2

```bash
colcon build
source install/setup.bash
```

---

# 🎮 Utilisation du driver

### Lancer le node

```bash
ros2 run my_robot_driver motor_manager
```

### Lire les positions des moteurs

```bash
ros2 topic echo /motors/joint_states
```

Exemple :

```
name: ['m1', 'm2']
position: [0.12, 1.57]
```

---

# 🔌 Configuration

Modifiable dans `motor_manager.py` :

```python
self.port_name = '/dev/ttyACM0'
self.baud = 1_000_000
self.ids = [1, 2]
```

---

# 📡 Topics ROS2

### Publie :

| Topic | Type | Description |
|-------|------|-------------|
| `/motors/joint_states` | `sensor_msgs/JointState` | Position des moteurs en radians |

### Souscrit (optionnel) :

| Topic | Type | Description |
|-------|------|-------------|
| `/motors/goal_positions` | `sensor_msgs/JointState` | Commande de position |

---

# 🔧 Dépendances Python internes

Gérées via `setup.py` :

```
pyserial>=3.5
```

---

# 🧪 Test matériel rapide

```bash
python3 - <<'PY'
from my_robot_driver.vendor.scservo_sdk.port_handler import PortHandler
from my_robot_driver.vendor.scservo_sdk.sms_sts import SMS_STS

PORT = "/dev/ttyACM0"
ID = 1

p = PortHandler(PORT)
p.openPort()
p.setBaudRate(1_000_000)

servo = SMS_STS(p)
pos = servo.ReadPos(ID)

print("Position servo ID 1 :", pos)
p.closePort()
PY
```

---

# 🛂 Permissions Linux

```bash
sudo usermod -a -G dialout $USER
```

Puis **déconnexion / reconnexion**.

---

# 🗂️ Structure interne du package

```
my_robot_driver/
  motor_manager.py
  vendor/
    scservo_sdk/
  __init__.py
setup.py
package.xml
```

---

# 📝 Licence

- Le SDK Feetech (scservo_sdk) → **MIT**
- Le code du projet → **MIT** (modifiable selon ton besoin)

---

# 🚀 Roadmap

- [ ] launch file ROS2  
- [ ] config YAML des moteurs  
- [ ] support vitesse / couple  
- [ ] diagnostics ROS2  
- [ ] CI GitHub Actions (build & test)  
- [ ] URDF + rviz  

---

# 🤝 Auteur

**Marc-André Bouchard**  
Projet personnel — Feetech x ROS2  
Intégrateur de systèmes et passionné de robotique
