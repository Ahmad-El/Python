import time
import grpc
import time
from concurrent import futures
from data import Data
import air_craft_pb2_grpc


class ShipsService(air_craft_pb2_grpc.ShipsService):
    def GetAircraft(self, request, context):
        data = Data()
        print(request.coordinates)
        for _ in range(1, 10):
            time.sleep(1)
            yield data.generate_data()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    air_craft_pb2_grpc.add_ShipsServiceServicer_to_server(ShipsService(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    print("Server started. Listening on port 50051.")
    try:
        while True:
            time.sleep(86400)  # One day in seconds
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()
