# SAE-51-2
# Solutions libres de collecte, centralisation et présentation des logs
Dans ce document, nous allons présenter plusieurs solutions open-source permettant de collecter, centraliser et visualiser les logs. Nous nous intéresserons à leurs fonctionnalités principales, leurs avantages et inconvénients, et leur facilité de mise en place.

1. ELK Stack (Elasticsearch, Logstash, Kibana)
Description
L'ELK Stack est une suite d'outils composée de :

Elasticsearch : moteur de recherche et d'indexation.
Logstash : collecte et traitement des logs.
Kibana : visualisation des logs.
Avantages
Très complet avec de nombreuses fonctionnalités.
Dashboards interactifs et personnalisables avec Kibana.
Grande communauté et beaucoup de documentation.
Inconvénients
Complexe à installer et configurer (plusieurs composants).
Consomme beaucoup de ressources (surtout Elasticsearch).
Certaines fonctionnalités sont payantes (via Elastic).
Cas d'usage
L'ELK Stack est bien adaptée aux entreprises qui ont besoin de gérer de grands volumes de logs avec des visualisations avancées.

2. Loki + Promtail ou Alloy + Grafana
Description
Loki est un système léger de gestion des logs, souvent utilisé avec Promtail (pour la collecte) et Grafana (pour la visualisation).

Avantages
Plus simple et moins gourmand en ressources que ELK.
Très bien intégré avec Grafana pour les dashboards.
Idéal pour les environnements conteneurisés (comme Docker et Kubernetes).
Inconvénients
Moins puissant pour la recherche de logs complexes.
Indexation limitée par rapport à Elasticsearch.
Cas d'usage
Solution adaptée pour ceux qui recherchent une solution simple à mettre en place et légère, surtout dans des environnements Kubernetes.

3. Graylog
Description
Graylog est une solution open-source de gestion des logs basée sur Elasticsearch et MongoDB pour le stockage des données.

Avantages
Interface utilisateur facile à utiliser.
Bonne gestion des notifications et alertes basées sur les logs.
Capable de gérer de gros volumes de logs grâce à Elasticsearch.
Inconvénients
Moins de flexibilité pour les dashboards que Kibana ou Grafana.
Dépendance forte à Elasticsearch, qui peut rendre la gestion complexe.
Cas d'usage
Graylog convient bien aux petites et moyennes entreprises qui ont besoin d’une solution simple pour gérer et visualiser leurs logs sans trop de complexité.

Conclusion
ELK Stack : solution complète mais gourmande en ressources.
Loki + Grafana : léger et simple, parfait pour des environnements Kubernetes.
Graylog : bonne alternative à ELK, plus simple d’utilisation.
Chaque solution a ses forces et faiblesses, et le choix dépend des besoins spécifiques de l’entreprise ou du projet.
