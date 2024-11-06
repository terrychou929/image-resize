## Image Resize with Python

#### Steps

1. git clone

```shell
    git clone {this directory}
```

2. create venv

```shell
    python -m venv venv
```

3. install requirements

```shell
    pip install -r requirements.txt
```

4. put pictures into input folder

```shell
# find all files start with 2022 and 2023, then 15 digits + .jpg. Lastly zip them together.
find . -type f \( -name "2022?????????????????.jpg" -o -name "2023?????????????????.jpg"  \) -print | zip test.zip -@
```

5. execute main script

```shell
    python main.py [scale|float]
```
