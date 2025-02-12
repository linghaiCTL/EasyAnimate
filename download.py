#模型下载
from modelscope import snapshot_download
model_dir = snapshot_download('PAI/EasyAnimateV5.1-12b-zh', local_dir="/ceph/home/chentianle/diffusion/EasyAnimate/models/EasyAnimate")