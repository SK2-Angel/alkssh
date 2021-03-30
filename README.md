# ALKSSH
简介：

    一个集成了终端页面,后端整条kubernetes调动的组件,可以实现pod在web页面的连接,方便各位大佬的使用,二次开发和集成项目,通过url的方式识别和连接pod容器,不需要侵入到k8s环境中,可在kubernetes外部部署使用,
    
演示图片:
![image](https://user-images.githubusercontent.com/49671782/112960034-9ceedb80-9176-11eb-8c3b-4a900d1eb268.png)
  
环境说明:

    centos7.3+
    python==3.6
    Django==2.0.5
    kubernetes==12.0.0
    channels==2.0.2
    
    
部署方式:

物理机部署:

    拉取源码到本地
    1.git clone https://github.com/SK2-Angel/alkssh.git
    
    安服务所需要的模块
    2.pip install django==2.0.5 kubernetes==12.0.0 channels==2.0.2
    
    将集群的权限文件kubelet.conf放置到/root/kubernetes.yaml,以至于组件可以正常的访问k8s集群
    3.cp -rp /etc/kubernetes/kubelet.conf /root/kubernetes.yaml
    说明：如果要更权限文件的路径,可在代码的
    
    进入到目录中启动运行服务
    4.python3 manage.py runserver 0.0.0:3578  #端口号可以根据自己的需求更改
    
