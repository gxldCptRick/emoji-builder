# Emoji Builder

Simple python script to take in a message and symbols to use to create either a text art message of your string as characters or use of emojis by hard coding them into the script to build these cute little text diagrams.

## Old CLI Way

```bash
    > python -m builder cli -m "Some Message"
---
# output.txt
😭😭😭😭😭
😭💖💖💖😭
😭💖😭😭😭
😭💖💖💖😭
😭😭😭💖😭
😭💖💖💖😭
😭😭😭😭😭
😭😭😭😭😭
😭💖💖💖😭
😭💖😭💖😭
😭💖😭💖😭
😭💖💖💖😭
😭😭😭😭😭
😭😭😭😭😭
😭💖😭💖😭
😭💖💖💖😭
😭💖😭💖😭
😭💖😭💖😭
😭😭😭😭😭
😭😭😭😭😭
😭💖💖💖😭
😭💖😭😭😭
😭💖💖💖😭
😭💖😭😭😭
😭💖💖💖😭
😭😭😭😭😭
😭😭😭😭😭
😭💖💖💖😭
😭😭😭😭😭
😭😭😭😭😭
😭💖😭💖😭
😭💖💖💖😭
😭💖😭💖😭
😭💖😭💖😭
😭😭😭😭😭
😭😭😭😭😭
😭💖💖💖😭
😭💖😭😭😭
😭💖💖💖😭
😭💖😭😭😭
😭💖💖💖😭
😭😭😭😭😭
😭😭😭😭😭
😭💖💖💖😭
😭💖😭😭😭
😭💖💖💖😭
😭😭😭💖😭
😭💖💖💖😭
😭😭😭😭😭
😭😭😭😭😭
😭💖💖💖😭
😭💖😭😭😭
😭💖💖💖😭
😭😭😭💖😭
😭💖💖💖😭
😭😭😭😭😭
😭😭😭😭😭
😭💖💖💖😭
😭💖😭💖😭
😭💖💖💖😭
😭💖😭💖😭
😭😭😭😭😭
😭😭😭😭😭
😭💖💖💖😭
😭💖😭😭😭
😭💖😭😭😭
😭💖😭💖😭
😭💖💖💖😭
😭😭😭💖😭
😭😭😭😭😭
😭😭😭😭😭
😭💖💖💖😭
😭💖😭😭😭
😭💖💖💖😭
😭💖😭😭😭
😭💖💖💖😭
😭😭😭😭😭
```

## New Way with files

Allows you to emojify your messages using files if you don't want the message to be typed in the cli.

### input.yaml

Yaml files with the only requirements being a `message` key but allows you to override the following:
- `background`
- `foreground`
- `width`
- `output`

```yaml
message: Some Message
background: 😭
foreground: 💖
width: 100
output: output.txt
```

### input.yml

Supports the `yml` extensions as well as `yaml`

```yaml
message: Some Message
background: 😭
foreground: 💖
width: 100
output: output.txt
```

### input.json 

Json will share the same structure of the yaml where you need to define the `message` and allows you to override the following:
- `background`
- `foreground`
- `width`
- `output`

Only required to define the `message` key otherwise it will use the same defaults as the cli.

```json
{
    "message": "Some Message",
    "background": "😭",
    "foreground": "💖",
    "width": 100,
    "output": "output.txt"
}
```

### input.txt

We will just read in the text of the file as the message you wish to emojify

```txt
Some Message
```

### Command 

The command will be under the `file` subcommand group.

```bash
    > python -m builder file -i input.yaml
    > python -m builder file -i input.yml
    > python -m builder file -i input.json
    > python -m builder file -i input.txt
```


Very useful if you want to make cute little messages by default the foreground is the 💖 and the background is the 😭 however you can use any arbitrary string as foreground and any arbitrary string as background.