# CharacterCreator
Create a character for custom RPG. Utilizes [Vite](https://vitejs.dev/), docker-compose, and [mongodb](https://www.mongodb.com/)

## Running the app in docker
```
docker compose up mongodb
```

## Tools required for development
1. [nvm](https://github.com/nvm-sh/nvm#install--update-script)
    -
    ```
    wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
    source ~/.bashrc
    ```
1. npm and node v16
    - 
    ```
    nvm install 16
    ```
2. vite
    - 
    ```
    npm i vite
    ```
3. [docker](https://docs.docker.com/engine/install/ubuntu/)
4. docker-compose
    - 
    ```
    sudo apt-get install docker-compose-plugin
    ```
5. mongodb
    - managed through docker
