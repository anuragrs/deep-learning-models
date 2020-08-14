base_files = ['../../../common/datasets/coco.py',
              '../../../common/lr_policy.py',
              '../../../common/runtime.py',
              '../../../common/models/faster_rcnn_fpn.py']
# overwrite default optimizer
optimizer = dict(
    _overwrite_=True,
    type='SGD',
    learning_rate=1e-2,
    momentum=0.9,
    nesterov=False,
)
work_dir = './work_dirs/faster_rcnn_r50_fpn_1x_coco'
