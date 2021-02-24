from kubernetes import client, config
from kubernetes.stream import stream
import json

class KubeApi:
    def __init__(self,):
        config.load_kube_config("/root/kubernetes.yaml")
    def pod_exec(self,pod,namespace_pod,row,cols,container=""):
        api_instance = client.CoreV1Api()
        exec_command = [
            "/bin/sh",
            "-c",
            'TERM=xterm-256color; export TERM; [ -x /bin/bash ] '
            '&& ([ -x /usr/bin/script ] '
            '&& /usr/bin/script -q -c "/bin/bash" /dev/null || exec /bin/bash) '
            '|| exec /bin/sh'
            '&& cp -rp /etc/skel/.bash* /root/']

        cont_stream = stream(api_instance.connect_get_namespaced_pod_exec,
                             name=pod,
                             namespace=namespace_pod,
                             container=container,
                             command=exec_command,
                             stderr=True, stdin=True,
                             stdout=True, tty=True,
                             _preload_content=False
                             )
        cont_stream.write_channel(4, json.dumps({"Height": int(row), "Width": int(cols)}))
        return cont_stream

