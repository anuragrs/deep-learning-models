# -*- coding: utf-8 -*-
base_files = ['../../../common/datasets/coco.py',
              '../../../common/lr_policy.py',
              '../../../common/runtime.py',
              '../../../common/models/retinanet_fpn.py']

# dataset settings
dataset_type = 'CocoDataset'
data_root = '/data/COCO/'
preproc_mode = 'caffe'
image_mean = (123.68, 116.78, 103.94)
image_std = (1., 1., 1.)
data = dict(
    _overwrite_ = True,
    imgs_per_gpu=4,
    train=dict(
        type=dataset_type,
        train=True,
        dataset_dir=data_root,
        subset='train',
        flip_ratio=0.5,
        pad_mode='fixed',
        preproc_mode=preproc_mode,
        mean=image_mean,
        std=image_std,
        scale=(800, 1333)),
    val=dict(
        type=dataset_type,
        train=False,
        dataset_dir=data_root,
        subset='val',
        flip_ratio=0,
        pad_mode='fixed',
        preproc_mode=preproc_mode,
        mean=image_mean,
        std=image_std,
        scale=(800, 1333)),
    test=dict(
        type=dataset_type,
        train=False,
        dataset_dir=data_root,
        subset='val',
        flip_ratio=0,
        pad_mode='fixed',
        preproc_mode=preproc_mode,
        mean=image_mean,
        std=image_std,
        scale=(800, 1333)),
)

# overwrite default optimizer
optimizer = dict(
    _overwrite_=True,
    type='SGD',
    learning_rate=5e-3,
    momentum=0.9,
    nesterov=False,
)

# extra options related to optimizers
optimizer_config = dict(
    _overwrite_=True,
    amp_enabled=True,
    gradient_clip=5.0,
)

# learning policy
lr_config = dict(
    _overwrite_=True,
    policy='step',
    warmup='linear',
    warmup_iters=500,
    warmup_ratio=1.0 / 10,
    step=[8, 11])

work_dir = './work_dirs/retinanet_r50_fpn_1x_coco'

