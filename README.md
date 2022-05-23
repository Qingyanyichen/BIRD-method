# BIRD-method
This is the Pytorch implementation of our paper "Data Augmentation using Bitplane Information Recombination Model", IEEE Transactions on Image Processing, DOI :10.1109/TIP.2022.3175429.

----------
Requirements  
----------
* Python3  
* PyTorch (> 1.0)  
* torchvision (> 0.2)  
* NumPy  

----------
Train Examples
----------
CIFAR-100: We used 1 GPUs to train CIFAR-100 as follows:
``` 
    python train.py \
    --net_type resnet \
    --dataset cifar100 \
    --depth 50 \
    --alpha 240 \
    --batch_size 16 \
    --lr 0.025 \
    --expname PesNet50 \
    --epochs 400 \
    --beta 1.0 \
    --no-verbose
```

``` 
    python train.py \
    --net_type pyramidnet \
    --dataset cifar100 \
    --depth 200 \
    --alpha 240 \
    --batch_size 16 \
    --lr 0.05 \
    --expname PyraNet200 \
    --epochs 600 \
    --beta 1.0 \
    --no-verbose
```
For more details about the algorithm, please refer to our article.  
If you have any questions, please contact Huan Zhang: zhanghuan19@mails.tsinghua.edu.cn

----------
Citation
----------
Huan Zhang, Zhiyi Xu, Xiaolin Han, and Weidong Sun. "Data Augmentation using  Bitplane Information Recombination Model", IEEE Transactions on Image Processing, DOI :10.1109/TIP.2022.3175429.
