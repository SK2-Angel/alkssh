from channels.generic.websocket import WebsocketConsumer
from medivh.kube import KubeApi
from threading import Thread

class K8SStreamThread(Thread):
    def __init__(self, websocket, container_stream):
        Thread.__init__(self)
        self.websocket = websocket
        self.stream = container_stream

    def run(self):
        while self.stream.is_open():
            if self.stream.peek_stdout():
                stdout = self.stream.read_stdout()
                self.websocket.send(stdout)
            if self.stream.peek_stderr():
                stderr = self.stream.read_stderr()
                self.websocket.send(stderr)
        else:
            self.websocket.close()


class SSHConsumer(WebsocketConsumer):
    def connect(self):
        path = self.scope.get('path')
        #hard code the name of container
        if ':' in path:
            self.container = path.split(':')[-1]
            self.name = path.split('/')[-1].split(':')[0]
            self.namespace_pod = path.split('/')[-2]
            self.cols_s = path.split('/')[-3]
            self.rows_s = path.split('/')[-4]
            self.stream = KubeApi().pod_exec(self.name,self.namespace_pod,self.rows_s,self.cols_s,self.container)
        else:
            self.container = ""
            self.name = path.split('/')[-1]
            self.namespace_pod = path.split('/')[-2]
            self.cols_s = path.split('/')[-3]
            self.rows_s = path.split('/')[-4]
            self.stream = KubeApi().pod_exec(self.name,self.namespace_pod,self.rows_s,self.cols_s)

        kub_stream = K8SStreamThread(self, self.stream)
        kub_stream.start()
        self.accept()

    def disconnect(self, close_code):
        self.stream.write_stdin('exit\r')

    def receive(self, text_data):
        self.stream.write_stdin(text_data)

