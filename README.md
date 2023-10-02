# guardian oss :shield:
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

![fastapi-greatexpectations](/static/wunsz.jpg)

<a name="readme-top"></a>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#make-will-help-you">Make will help you</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Available Integrations</a>
      <ul>
        <li><a href="#">PostgreSQL</a></li>
        <li><a href="#">Microsoft SQL Server</a></li>
        <li><a href="#">MySQL >> WIP</a></li>
        <li><a href="#">Oracle >> WIP</a></li>
      </ul>
    </li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


## About The Project

`Guardian OSS` project is REST API wrapper for [greatexpectations.io](https://greatexpectations.io/) library.

[greatexpectations.io](https://greatexpectations.io/expectations/) is a tool for data quality validation, documentation, and profiling.


Can we be better prepared for expected unexpected philosophy ?
The `expect the unexpected` philosophy leads to the freedom of
choice and the freedom of others people judgment,
creating a future full of possibilities, accepting that whatever will be,
will be; the future's not ours to see, que será, será.

### Built With

[![FastAPI][fastapi.tiangolo.com]][fastapi-url]
[![Pydantic][pydantic.com]][pydantic-url]
[![pytest][pytest.org]][pytest-url]
[![rich][rich.readthedocs.io]][rich-url]
[![GX OSS][greatexpectations.io/gx-oss]][gx-url]

## Getting Started

### Make will help you

To build , run and more... use magic of make help to play with this project.

```shell
make help
```

and you receive below list:

```text
build                Build project with compose
clean                Clean Reset project containers with compose
coverage             Run project tests with coverage
down                 Reset project containers with compose
help                 Show this help
restore_db_backup    Restore database backup on running sqlserver container
test                 Run project tests
up_code              Run project with compose
verify_db_backup     Verify database backup file names before restore on running sqlserver container
```


### Local development with poetry

Install poetry with pipx
```shell
pipx install --suffix "@1.6" poetry==1.6.1
```
Spawn new shell with poetry
```shell
poetry@1.6 shell
```
Install project dependencies
```shell
poetry@1.6 install
```

### How to setup project and feed database
1. Use make to build and run project. It will add local volumes with SQL Server database files. Check `./sqlserver` folder for more details.
```shell
make build && make up_code
```
2. Download `AdventureWorksLT2022` database backup from [here](https://github.com/Microsoft/sql-server-samples/releases/download/adventureworks/AdventureWorksLT2022.bak)


3. Copy database to `./sqlserver/restore` folder and restore it with make command
```shell
cp AdventureWorksLT2022.bak ./sqlserver/restore && make restore_db_backup
```

Hope you enjoy it.



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

[fastapi.tiangolo.com]: https://img.shields.io/badge/FastAPI-0.103.2-009485?style=for-the-badge&logo=fastapi&logoColor=white
[fastapi-url]: https://fastapi.tiangolo.com/
[pydantic.com]: https://img.shields.io/badge/Pydantic-2.4.2-e92063?style=for-the-badge&logo=pydantic&logoColor=white
[pydantic-url]: https://docs.pydantic.dev/latest/
[pytest.org]: https://img.shields.io/badge/pytest-7.4.0-fff?style=for-the-badge&logo=pytest&logoColor=white
[pytest-url]: https://docs.pytest.org/en/6.2.x/
[greatexpectations.io/gx-oss]: https://img.shields.io/badge/Great%20Expectations-0.17.19-ff6310?style=for-the-badge&logo=greatexpectations&logoColor=white
[gx-url]: https://greatexpectations.io/gx-oss/
[rich.readthedocs.io]: https://img.shields.io/badge/rich-13.5.2-black?style=for-the-badge&logo=rich&logoColor=white
[rich-url]: https://rich.readthedocs.io/en/latest/
