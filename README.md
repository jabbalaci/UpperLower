# UpperLower

A sample project for demonstrating how to make a project
that can be installed with **pipx** or with **uv**, directly from GitHub.

The project was made with poetry, but uv can also process it.

## With pipx

### Installation

    pipx install git+https://github.com/jabbalaci/UpperLower

After installing, you'll get two simple executables:

```
$ pipx list
   package upperlower 0.1.0, installed using Python 3.x.y
    - lower
    - upper
```

### Uninstallation

    pipx uninstall upperlower

## With uv

### Installation

    uv tool install git+https://github.com/jabbalaci/UpperLower

After installing, you'll get two simple executables:

```
$ uv tool list
upperlower v0.1.0
- lower
- upper
```

### Uninstallation

    uv tool uninstall upperlower
