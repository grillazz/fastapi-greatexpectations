# guardian oss :shield:
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

![fastapi-greatexpectations](/static/wunsz.jpg)

In this place two personas William Shakespeare as [Data Feed](https://github.com/catherinedevlin/opensourceshakespeare)
and Charles Dickens as [Data Validation](https://greatexpectations.io/expectations/)
will be hosted by Almighty Monty Python as Guardian OSS :)

[greatexpectations.io](https://greatexpectations.io/expectations/) is a tool for data quality validation, documentation, and profiling.
Here we will use latest version of [great-expectations = "0.16.12"](https://pypi.org/project/great-expectations/) 
and [fastapi = "0.95.0"](https://pypi.org/project/fastapi/).

Can we be better prepared for expected unexpected philosophy ?
The `expect the unexpected` philosophy leads to the freedom of
choice and the freedom of others people judgment,
creating a future full of possibilities, accepting that whatever will be,
will be; the future's not ours to see, que será, será.

### :cook: How to Set up project locally

To build , run and more... use magic of make help to play with this project.

```shell
make help
```

and you receive below list:

```text
black                apply black in project code.
build                Build project with compose
clean                Clean Reset project containers with compose
down                 Reset project containers with compose
feed_db              create database objects and insert data
flake8               apply black in project code.
help                 Show this help
isort                sort imports in project code.
mypy                 apply black in project code.
requirements         Refresh requirements.txt from pipfile.lock
up                   Run project with compose
```

### How to Play

1. Build project with docker compose: `make build`
2. Run project with docker compose: `make up`
3. Create database objects and insert data: `make feed_db`

### Backbone

...
Hope you enjoy it.

ps. previous implementation of this project for `great-expectations = "0.16.3"` 
is available [in this branch](https://github.com/grillazz/fastapi-greatexpectations/tree/gx_0163)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/grillazz/fastapi-greatexpectations.svg?style=for-the-badge
[contributors-url]: https://github.com/grillazz/fastapi-greatexpectations/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/grillazz/fastapi-greatexpectations.svg?style=for-the-badge
[forks-url]: https://github.com/grillazz/fastapi-greatexpectations/network/members
[stars-shield]: https://img.shields.io/github/stars/grillazz/fastapi-greatexpectations.svg?style=for-the-badge
[stars-url]: https://github.com/grillazz/fastapi-greatexpectations/stargazers
[issues-shield]: https://img.shields.io/github/issues/grillazz/fastapi-greatexpectations.svg?style=for-the-badge
[issues-url]: https://github.com/grillazz/fastapi-greatexpectations/issues
[license-shield]: https://img.shields.io/github/license/grillazz/fastapi-greatexpectations.svg?style=for-the-badge
[license-url]: https://github.com/grillazz/fastapi-greatexpectations/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/python-has-powers/