import json
import random
import redis
import logging

CHANNEL = "cash_flow"
logging.basicConfig(level=logging.INFO)


def generate_message():
    account_from = random.randint(10**9, 10**10 - 1)
    account_to = random.randint(10**9, 10 ** 10 - 1)
    amount = random.randint(-10000, 10000)
    message = {
        "metadata": {
            "from": str(account_from),
            "to": str(account_to)
        },
        "amount": amount
    }
    return json.dumps(message)


def publish_message(channel, json_data):
    client = redis.Redis()
    client.publish(channel, message=json_data)
    logging.info(f"produced message: {json_data}")


def main(arg):
    if arg < 0:
        messages = [
            {"metadata": {"from": str(1111111111), "to": str(
                2222222222)}, "amount": 10000},
            {"metadata": {"from": str(3333333333), "to": str(
                4444444444)}, "amount": -3000},
            {"metadata": {"from": str(2222222222), "to": str(
                5555555555)}, "amount": 5000},
        ]
        for message in messages:
            publish_message(channel=CHANNEL, json_data=json.dumps(message))
    else:
        for _ in range(arg):
            publish_message(channel=CHANNEL, json_data=generate_message())


if __name__ == "__main__":
    main(-1)
