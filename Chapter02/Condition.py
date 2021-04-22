import logging
import threading

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
condition = threading.Condition()


class Consumer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def consume(self):

        with condition:

            if len(items) == 0:#kondisi stack kosong
                logging.info('no items to consume')
                logging.info('concume : ini mau berenti')
                condition.wait()#melakukan pause sampai dapat notify baru jalan lagi
                logging.info('consume : dapat notifi jalan lagi')

            items.pop()
            logging.info('consumed 1 item')

            condition.notify()

    def run(self):
        for i in range(20):
            #time.sleep(2)
            self.consume()


class Producer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def produce(self):

        with condition:

            if len(items) == 5:#kondisi penuh
                logging.info('items produced {}. Stopped'.format(len(items)))
                logging.info('produce : ini mau berenti')
                condition.wait()#pause disini setelah dapat notify baru jalan kembali
                logging.info('produce : dapat notifi jalan lagi')

            items.append(11)
            logging.info('total items {}'.format(len(items)))

            condition.notify()

    def run(self):
        for i in range(20):
            #time.sleep(0.5)
            self.produce()


def main():
    producer = Producer(name='Producer')
    consumer = Consumer(name='Consumer')

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()


if __name__ == "__main__":
    main()
