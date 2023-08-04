# Family Website

Żmudziński family website written using Python thanks to the Pelican package. The website shows our family members, animals and history.

The deployment is done through Github Actions and posted on GitHub Pages.

## Requirements

- Python 3.11
- Docker
- Docker Compose

## Environment Variables

| **Variable** | **Description** |
| :--- | :--- |
| `SITEURL` | The url of the final website |

## Useful commands

| **Action** | **Command** |
| :--- | :--- |
| Build the project | `docker compose build` |
| Run the project | `docker compose up` |
| Format project | `docker compose run web fmt` |
| Lint project | `docker compose run web lint` |
