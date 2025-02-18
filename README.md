# BIRD-method
This is the Pytorch implementation for the classification part of our paper "Data Augmentation using Bitplane Information Recombination Model", IEEE Transactions on Image Processing, DOI :10.1109/TIP.2022.3175429 (https://ieeexplore.ieee.org/document/9779584).

For the detection part of our proposed BIRD data augmentation method, the newly POBIT data augmentation method (https://www.mdpi.com/2072-4292/16/24/4806) is developed based on this and will be released soon.

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
CIFAR-100: We used 1 GPUs to train CIFAR-100 dataset as follows:
``` 
    python train.py \
    --net_type resnet \
    --dataset cifar100 \
    --depth 50 \
    --batch_size 16 \
    --lr 0.02 \
    --expname ResNet50 \
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
For more details about the algorithm, please refer to our article (https://ieeexplore.ieee.org/document/9779584).  
If you have any questions or suggestions, please contact Huan Zhang: zhanghuan19@mails.tsinghua.edu.cn          
Recently, the email zhanghuan19@mails.tsinghua.edu.cn has been changed to zhanghuan19@tsinghua.org.cn

----------
Citation
----------
H. Zhang, Z. Xu, X. Han and W. Sun, "Data Augmentation Using Bitplane Information Recombination Model," in IEEE Transactions on Image Processing, vol. 31, pp. 3713-3725, 2022, doi: 10.1109/TIP.2022.3175429.
