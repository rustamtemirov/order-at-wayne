# order-at-wayne

Before running download packages Flask, requests, telebot, pymemecache using  package manager [pip](https://pip.pypa.io/en/stable/).


## Running

Run the project using following commands:

```python
(venv)$ export FLASK_APP=app.py
(venv)$ flask run
 * Running on http://127.0.0.1:5000/
 
```

Then, setup NGROK to the localhost and enter following command:

```python
$ ./ngrok http 5000
```

We need to let Telegram know our local server, in order to receive messages from it. We simply need to report our tunnel address that we created through NGROK.
It can be done using following command:

```python
$ curl --location --request POST 'https://api.telegram.org/bot{token}/setWebhook' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "{url}"
}'
```

where {token} is the Token created by BotFather,
and url is the NGROK url, it should look like this ->  https://32515a83.ngrok.io


## Contributors

Nadine Razoki


