# diy.py-starter-kit
A docker-based python environment for DIY investors

#### Build container

```shell
docker-compose up -d
```

#### Destroy container

```
docker-compose down
```

#### Rebuild container

Use this when you update requirements.txt

```shell
docker-compose up -d --build
```

Remember to remove dangling images

```shell
docker image rm IMAGE ID
```

