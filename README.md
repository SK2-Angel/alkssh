# ALKSSH
<h3>简介</h3>

  一个集成了终端页面,后端整条kubernetes调动的组件,可以实现pod在web页面的连接,方便各位大佬的使用,二次开发和集成项目,通过url的方式识别和连接pod容器,不需要侵入到k8s环境中,可在kubernetes外部部署使用,

<h3>演示</h3>

![image](https://img-blog.csdnimg.cn/20201224183506387.gif#pic_center)
  
<h3>环境说明</h3>

    centos7.3+
    python==3.6
    Django==2.0.5
    kubernetes==12.0.0
    channels==2.0.2
    
    
<h3>部署方式</h3>

<h3>物理机部署</h3>

    1.拉取源码到本地
    git clone https://github.com/SK2-Angel/alkssh.git
    
    2.安服务所需要的模块
    pip install django==2.0.5 kubernetes==12.0.0 channels==2.0.2
    
    3.将集群的权限文件kubelet.conf放置到/root/kubernetes.yaml,以至于组件可以正常的访问k8s集群
    cp -rp /etc/kubernetes/kubelet.conf /root/kubernetes.yaml
    
    说明：如果要更权限文件的路径,可在代码的/alkssh/medivh/kube.py这个文件中的config.load_kube_config("/root/kubernetes.yaml")更改
    
    4.进入到目录中启动运行服务
    python3 manage.py runserver 0.0.0:3578  #端口号可以根据自己的需求更改
 
 
<h3>容器化部署</h3>
      
     利用docker启动组件
     docker run -v -d /root/kubernetes.yaml:/root/kubernetes.yaml -p 3578:3578 --add-host apiserver.cluster.local:172.3.59.166 czl1041484348/alkssh:v1
     
     说明:
          /root/kubernetes.yaml: kubernetes的认证文件,组件需要获取kubernetes权限,用来调用api和数据传输。
          -p 3578:3578: 容器内部的默认启动端口是3578,根据个人的需求进行改变。
          –add-host apiserver.cluster.local:172.3.59.166: 这参数是添加一个hosts到容器中,这里是因为作者的kube-apiserver是通过名称进行访问的,所以要加一个hosts否则无法解析地址,根据个人的需求进行改变。

<h3>访问方式</h3>
    http://部署此组件的机器地址加端口号/index/namespace命名空间/pod的名称
    
    例如:
    
     http://225.145.56.221:3578/index/alkssh/nginx-alktest-5bfb49576d-875f9

<h3>API集成方法</h3>

   集成组件可以用url的方式,例如在调用组件前,获取接口的ip:port,命令空间名称指定的pod名称,然后可以利用window.open(url)的方式,打开并跳转页面,实现pod终端的连接
 
 
<h3>结尾</h3>
  
  此开源组件除了docker也可部署在宿主机和kubernetes中，后续会更新kubernetes的部署方法，如果有任何疑问或者发现了BUG，可以提交问题，我看到第一时间会回复，运维开发是将来的发展趋势，自动化运维已经满足不了部分需求，谢谢大家的支持！！
<h3>博客连接:</h3> https://blog.csdn.net/qq_42647772/article/details/111663376
  
  
  
  
  
  <h4>作者微信,有什么问题可以加我微信问,也可以探讨运维开发的奥妙,谢谢</h4>
  
  <img src="https://user-images.githubusercontent.com/49671782/112968052-79c82a00-917e-11eb-8b1a-b85f7ef21328.png" width="400" height="400" /><br/>






 
 
