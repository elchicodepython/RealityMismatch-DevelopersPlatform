# Developers platform for Reality Mismatch Game

![](https://travis-ci.org/ElChicoDePython/RealityMismatch-DevelopersPlatform.svg?branch=master)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Install

The project is prepared to be developed and run in GNU/Linux systems.
Tested in Debian 9.

- Install python3.7.
- Create a virtual environment for the project.
- Activate the virtual environment.
- Clone the repository.
- Install local requirements. `pip install -r requirements/local.txt`
- Install nvm. If you don't have it already you can run inside the project root folder `invoke install-nvm`.
- Install nodejs project version (Nowadays: 10). You can do it if you have already nvm inside de project root folder running `invoke install-project-node`.
- If you dont have docker and you are in Debian/Ubuntu you can run inside de project root folder `invoke install-docker` and docker will be installed automatically in your system.
- Every time you want to start developing the project or just running locally you should activate and configure first the database and other services involved with the project configuration. This can be easily done (and automatically) by running `invoke start-development`.
- Every time you finish running the platform, to save resources you can deactivate the database and other services involved by running `invoke finish-development`.

The invoke commands should be executed from the root folder of the repository.
