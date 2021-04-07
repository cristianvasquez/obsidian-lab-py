# Obsidian lab

Say you have a terrific script in python to:

- Find similar notes to the current one.
- Translate a text.
- Know what was your mood the last three months, just reading your Obsidian vault.
- Whatever wonder you have under the sleeve :D

And you want to see if it's helpful in Obsidian.

One way is to expose your script with this, and consume it using the [obsidian lab](https://github.com/cristianvasquez/obsidian-lab) plugin.

## To install

```sh
pip install obsidian-lab
```

Usage:

```sh
obsidian-lab <scripts directory>
```

This will run a mini web server that exposes the scripts of the directory specified

Example:

```sh
obsidian-lab ./examples
```

After running, you can list all the available scripts:

> GET: http://127.0.0.1:5000/

```json
{
  "scripts": [
    "http://127.0.0.1:5000/scripts/hello_world",
    "http://127.0.0.1:5000/scripts/random",
    "http://127.0.0.1:5000/scripts/to_upper_case"
  ]
}
```

To add new scripts, copy them in the scripts directory.

## Build

Install the dependencies

```sh
pip install -r requirements.txt
```

try the app

```sh
python ./app.py <scripts directory>
```

## Status

This is a proof of concept.