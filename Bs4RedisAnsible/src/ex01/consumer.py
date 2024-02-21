import argparse
import json
import redis
import logging

CHANNEL = "cash_flow"


logging.basicConfig(level=logging.INFO)


def consume_message(channel):
    bad_guys = parser_args()
    consumer = redis.Redis().pubsub()
    consumer.subscribe(channel)
    for message in consumer.listen():
        if message['type'] == 'message':
            logging.info(f"received data: {message['data']}")
            get_sender_reciever(message=message["data"], bad_accounts=bad_guys)


def parser_args():
    parser = argparse.ArgumentParser(description="Redis publish/subscribe")
    parser.add_argument('-e', '--accounts', required=True,
                        help='flags -e <account1>,<account2>')
    args = parser.parse_args()
    return [account for account in str(args.accounts).split(',')]


def get_sender_reciever(message, bad_accounts):
    data = json.loads(message)
    sender = data["metadata"]["from"]
    receiver = data["metadata"]["to"]
    amount = data["amount"]
    if amount >= 0 and receiver in bad_accounts:
        data["metadata"]["from"] = receiver
        data["metadata"]["to"] = sender
        logging.info(f"Sender and Reciever are swapped: {data}")
    return json.dumps(data)


def main():
    consume_message(CHANNEL)


if __name__ == "__main__":
    main()
