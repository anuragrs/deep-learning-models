base_files = ['../../../common/sagemaker_8x8.py',
              '../../../common/datasets/coco.py',
              '../../../common/lr_policy.py',
              '../../../common/runtime.py',]

# model settings
model = dict(
    type='FasterRCNN',
    norm_type='BN',
    backbone=dict(
        type='KerasBackbone',
        model_name='ResNet50V1_b',
        weights_path='resnet50v1_b',
        weight_decay=1e-4
    ),
    neck=dict(
        type='FPN',
        in_channels=[('C2', 256), ('C3', 512), ('C4', 1024), ('C5', 2048)],
        out_channels=256,
        num_outs=5,
        interpolation_method='bilinear',
        weight_decay=1e-4,
    ),
    rpn_head=dict(
        type='RPNHead',
        anchor_scales=[8.],
        anchor_ratios=[0.5, 1.0, 2.0],
        anchor_strides=[4, 8, 16, 32, 64],
        target_means=[.0, .0, .0, .0],
        target_stds= [1.0, 1.0, 1.0, 1.0],
        feat_channels=512,
        num_samples=256,
        positive_fraction=0.5,
        pos_iou_thr=0.7,
        neg_iou_thr=0.3,
        num_pre_nms_train=6000,
        num_post_nms_train=2000,
        num_pre_nms_test=2000,
        num_post_nms_test=1000,
        weight_decay=1e-4,
        use_smooth_l1=False,
    ),
    bbox_roi_extractor=dict(
        type='PyramidROIAlign',
        pool_shape=[7, 7],
        pool_type='avg',
        use_tf_crop_and_resize=True,
    ),
    bbox_head=dict(
    type='BBoxHead',
    num_classes=81,
    pool_size=[7, 7],
    target_means=[0., 0., 0., 0.],
    target_stds=[0.1, 0.1, 0.2, 0.2],
    min_confidence=0.005,
    nms_threshold=0.75,
    max_instances=100,
    weight_decay=1e-4,
    use_conv=False,
    use_bn=False,
    use_smooth_l1=False,
    soft_nms_sigma=0.5)
)

# log, tensorboard configuration with s3 path for logs
log_config=dict(
    _overwrite_=true,
    interval=50,
    hooks=[
        dict(
            type='textloggerhook'
        ),
        dict(
            type='tensorboardloggerhook',
            log_dir=none,
            image_interval=100,
            s3_dir='{}/tensorboard/{}'.format(sagemaker_job['s3_path'], sagemaker_job['job_name'])
        ),
        dict(
            type='visualizer',
            dataset_cfg=data['val'],
            interval=100,
            top_k=10,
            run_on_sagemaker=true,
        ),
    ]
)

work_dir = './work_dirs/faster_rcnn_r50v1_b_fpn_1x_coco'

