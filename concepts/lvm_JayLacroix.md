# [Linux Logical Volume Manager (LVM) Deep Dive Tutorial](https://www.youtube.com/watch?v=MeltFN-bXrQ)
# Jay LaCroix (LearnLinuxTV)

## Install LVM
* Create volume group
* Partition physical devices to create physical volumes
* Add physical volumes to volume group
* Partition logical volumes

## Commands
* mounted device shown as `/dev/mapper/vg_name-lv_name`
* `lsblk` shows as `vg_name-lv_name` under physical volume (i.e. `/dev/sda1/`)
* `pvdisplay`
* `vgdisplay`


## Add physical volume any time after install
    `pvcreate /dev/sdb` &&
    `vgextend vg_name-lv_name /dev/sdb`

## Extend logical volume
    `lvextend -L +20G /dev/mapper/vg_name-lv_name` &&
    `resize2fs /dev/mapper/vg_name-lv_name`
