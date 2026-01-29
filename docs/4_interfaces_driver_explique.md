# Explication des Interfaces avec le Driver

Un driver bien conçu ne contient aucune interface utilisateur (IHM). Il se comporte comme une API, exposant des points d'accès que des outils externes (clients) peuvent utiliser.

```mermaid
graph TD
    subgraph "Clients / Outils Externes"
        direction LR
        IHM["IHM / GUI<br/>(ex: Foxglove, RQT)"]
        CLI["Script de Calibration<br/>(Python)"]
        RViz["RViz2<br/>(Visualisation 3D)"]
    end

    subgraph "Driver Matériel (Notre Nœud)"
        Node[motor_manager_node]
    end

    subgraph "Canaux de Communication ROS 2"
        direction TB
        TopicJS(Topic: /joint_states); TopicCMD(Topic: /joint_commands)
        ServiceCalib(Service: /calibrate_motors); ServiceLimits(Service: /set_motor_limits)
    end

    Node -- Publie l'état --> TopicJS; TopicCMD -- Envoie des ordres --> Node
    CLI -- "1. Requête" --> ServiceCalib -- "2. Exécute" --> Node
    Node -- "3. Réponse" --> ServiceCalib --> CLI
    IHM -- Appelle --> ServiceLimits; RViz -- S'abonne à --> TopicJS
```

## 👨‍🏫 Analyse du Schéma

Le driver `motor_manager` est un serviteur qui ne fait que ce qu'on lui demande via les canaux ROS 2. Les outils de diagnostic et de contrôle sont des **clients** qui consomment les services et les données qu'il expose.

1.  **Topics (Flux de données)** : Le driver publie en continu l'état des moteurs sur `/joint_states`. Des outils comme **RViz2** peuvent s'abonner à ce topic pour afficher un modèle 3D du robot en temps réel. Il écoute aussi sur `/joint_commands` pour recevoir des ordres de mouvement.

2.  **Services (Actions ponctuelles)** : Pour des actions qui ne sont pas continues (comme "calibrer" ou "fixer une limite"), on utilise un **Service**. C'est une communication de type **Requête/Réponse**.
    *   Un **script de calibration** (un simple programme Python) est lancé. Il appelle le service `/calibrate_motors`.
    *   Le driver reçoit la requête, exécute la procédure de calibration, puis renvoie une réponse ("Succès" ou "Échec").
    *   Le script client reçoit la réponse, l'affiche, et se termine.

Cette architecture rend le driver totalement indépendant de toute interface graphique, ce qui le rend extrêmement modulaire, testable et réutilisable.