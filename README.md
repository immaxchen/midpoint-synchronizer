# msync

synchronize directory through an intermediate storage device

only non-identical files will be copied into storage, it could be a shared folder or usb drive, etc.

it is a cross-platform command line tool and requires python >= 3.2

# Installation

```shell
$ git clone https://github.com/immaxchen/msync.git
$ cd msync
$ pip install .
```

# Usage

[PC1]
```shell
$ mount nas:/sharedfolder /mnt
$ msync request myproj/ /mnt
```

[PC2]
```shell
$ mount nas:/sharedfolder /mnt
$ msync respond /mnt/myproj.mreq myproj/
```

[PC1]
```shell
$ cp -rp /mnt/myproj/* myproj/
$ rm -rf /mnt/myproj
```
