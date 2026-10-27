# Odoo Custom Addons

Dépôt personnel centralisant les modules Odoo développés et maintenus par Abdou Kamagate.

## Versions prises en charge

- Odoo 18
- Odoo 19

## Organisation

- La branche `18.0` contient les modules compatibles avec Odoo 18.
- La branche `19.0` contient les modules compatibles avec Odoo 19.
- Les modules Odoo sont placés dans le dossier `addons/`.
- Les contrôles CI/CD sont définis dans `.github/workflows/`.

## Structure

```text
addons/               Modules Odoo personnalisés
docker/               Configuration Docker pour les tests
scripts/              Scripts de validation et de déploiement
.github/workflows/     Pipelines GitHub Actions
