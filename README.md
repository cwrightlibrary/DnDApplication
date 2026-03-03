# 🗡️ DnD Application

This will use the [5etools](https://github.com/5etools-mirror-3/5etools-src) to work with the classes and races from the `.json` files.

## Download the [5etools](https://github.com/5etools-mirror-3/5etools-src) source files

First, download the source files:

- **Mac/Linux**: `curl -L -O https://github.com/5etools-mirror-3/5etools-src/releases/download/v2.25.0/5etools-v2.25.0.zip`
- **Windows**: `Invoke-WebRequest -Uri "https://github.com/5etools-mirror-3/5etools-src/releases/download/v2.25.0/5etools-v2.25.0.zip" -OutFile "5etools-v2.25.0.zip"`

Next, unzip the `.zip` file:

- **Mac/Linux**: `unzip 5etools-v2.25.0.zip`
- **Windows**: `tar -xf 5etools-v2.25.0.zip`

Move the files we need to `assets/`:

- **Mac/Linux**:
  - `mv 5etools-v2.25.0/data/class /assets/class`
  - `mv 5etools-v2.25.0/data/spells /assets/spells`
  - `mv 5etools-v2.25.0/data/backgrounds.json /assets/`
  - `mv 5etools-v2.25.0/data/items.json /assets/`
  - `mv 5etools-v2.25.0/data/languages.json /assets/`
  - `mv 5etools-v2.25.0/data/races.json /assets/`
  - `mv 5etools-v2.25.0/data/skills.json /assets/`
- **Windows**:
- `move "5etools-v2.25.0\data\class" "assets\class"`
- `move "5etools-v2.25.0\data\spells" "assets\spells"`
- `move "5etools-v2.25.0\data\backgrounds.json" "assets\"`
- `move "5etools-v2.25.0\data\items.json" "assets\"`
- `move "5etools-v2.25.0\data\languages.json" "assets\"`
- `move "5etools-v2.25.0\data\races.json" "assets\"`
- `move "5etools-v2.25.0\data\skills.json" "assets\"`

Cleanup:

- **Mac/Linux**:
  - `rm -rf 5etools-v2.25.0.zip`
  - `rm -rf 5etools-v2.25.0`
- **Windows**:
  - `del 5etools-v2.25.0.zip`
  - `RMDIR /S 5etools-v2.25.0`

Now the files in `src/` will work with it.
