Ce document détaille les étapes de transformation du kit SO-AMR100 en plateforme de développement robotique professionnelle sous ROS 2.

**Architecture de Développement :**
*   **Poste de Contrôle (Host) :** PC Windows 10/11.
*   **Cerveau Robot (Target) :** Raspberry Pi 5 (Ubuntu Server / Headless).
*   **Méthode :** Développement à distance via VS Code (Remote-SSH).


## ⚙️ Phase 2 : Le Driver Moteur (Reverse Engineering)
*Objectif : Abstraire le matériel. ROS 2 doit envoyer des angles sans savoir que ce sont des moteurs Feetech.*

- [ ] **Création du Package ROS 2**
    - 1[ ] Créer le package `my_robot_driver`.
    - 2[ ] Développer le **Publisher Node** (Lecture position moteurs -> `/joint_states`).
    - 3[ ] Développer le **Subscriber Node** (Ordre `/joint_commands` -> Moteurs).
    - 4[ ] Créer un fichier de config `motors.yaml` (Offsets, Limites, IDs).
- [ ] **Calibration & Sécurité**
    - [ ] Implémenter les limites angulaires (Min/Max) dans le code du driver.
    - [ ] Créer un **service ROS 2** pour la calibration des offsets (Zeroing).
    - [ ] Développer un **script client** qui appelle ce service pour lancer la calibration.

## 🎮 Phase 3 : Téléopération Maître-Esclave
*Objectif : Contrôler le robot en temps réel avec un bras jumeau.*

- [ ] **Logique de Contrôle**
    - [ ] Implémenter le mode "Torque Off" pour le bras maître.
    - [ ] Créer un noeud de mapping (Maître -> Esclave) avec inversion des axes si nécessaire.
- [ ] **Sécurité**
    - [ ] Ajouter un "Watchdog" : Si le PC plante, le robot s'arrête en 0.5s.

## 🌍 Phase 4 : Connectivité & Vision (Le Niveau Pro)
*Objectif : Pilotage à distance (Internet) et perception.*

- [ ] **Réseau Robotique**
    - [ ] Installer **Husarnet** (ou Tailscale) sur le PC Windows et le Raspberry Pi.
- [ ] **Interface Opérateur**
    - [ ] Installer `ros-foxglove-bridge` sur le Pi.
    - [ ] Configurer un Dashboard Foxglove sur Windows (Vidéo + Sliders Moteurs).

## 🧠 Phase 5 : Intégration IA (LeRobot)
*Objectif : Le robot exécute des tâches apprises.*

- [ ] **Collecte de Données**
    - [ ] Enregistrer des datasets (Images + Positions moteurs) via `rosbag`.
- [ ] **Inférence**
    - [ ] Wrapper le modèle LeRobot dans un noeud ROS 2.
    - [ ] Créer une machine à état : "Mode Manuel" vs "Mode IA".

## 🧠 Phase 6 : Autonomie (Navigation & Perception)
*Objectif : Permettre au robot de naviguer de manière autonome vers un point GPS.*

- [ ] **Intégration des Capteurs**
    - [ ] Créer un nœud pour le GPS/IMU.
    - [ ] Configurer le nœud de la caméra.
- [ ] **Localisation & Navigation**
    - [ ] Configurer le package `robot_localization` pour la fusion de capteurs.
    - [ ] Déployer et configurer la stack de navigation Nav2.
    - [ ] Adapter le `motor_manager` pour qu'il accepte les commandes `/cmd_vel`.