# live.hackery.site

Simple authentication for nginx-rtmp

## Operation

```
$ cp auth.sample.json auth.json
$ $EDITOR auth.json
$ pipenv install
$ pipenv run ./run.sh
```

## Usage

With the sample nginx config, the broadcaster simply sets the stream key to `[username]?psk=[token]`. Viewers can simply use `[username]` as the stream key to watch.
