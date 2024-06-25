# Simulate Timeout 

You can see that the `/health` endpoint takes a long time when another request is running.

## 1. Install Packages

```
pip install -r requirements.txt
```

## 2. Start the Gunicorn Server

```
gunicorn main:app --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80 --timeout 60
```

## 3. Send a request to the `/health ` endpoint

You can send a request to the `/helath` endpoint. It will return quickly.

```
curl -XGET http://localhost/health
```

## 4. Send a request to the `/health ` endpoint during running the `/long` endpoint

Please open another terminal and send a request to the `/long` endpoint using the following command. It will take 30 secondes.

```
curl -XGET http://localhost/long
```

During running the above command, please try to send a request to the `/health` endpoint in the previous terminal.

```
curl -XGET http://localhost/health
```

You can see that it takes a long time to return.
