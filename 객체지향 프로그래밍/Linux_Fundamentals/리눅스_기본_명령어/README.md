# 리눅스 기본 명령어

## 명령어 라인 구성하기

### <span style="color:red">$ command [-options] [argument]</span>

- `command (명령)`
  - 리눅스를 사용하기 위해 사용자가 입력하는 다양한 명령
- `option (옵션)`
  - 옵션으로 명령어 세부 기능 선택
  - `short 형태 ( - )` 와 `long 형태 ( -- )` 존재
- `argument (인자)`
  - 명령어에 전달되는 값
  - `파일명이나 디렉토리명` 혹은 `명령어 실행에 필요한 정보` 등

```Linux
$ date
2023. 07. 16. (일) 20:46:28 KST

$ echo Hello world
Hello world

$ ls -F
backup/		empty_file.txt	공개/		  문서/	비디오/	음악/
date.out	hello_linux/	다운로드/	바탕화면  사진/	  템플릿/
```

* 옵션의 경우 여러 갖 기능을 함께 적용 가능

$ command -abc

$ command -a -b -c

$ command -a argument

```Linux
$ls -F
test.sh*

$ ls -a
.	.bash_history	.bash_profile	.cache	.lesshst	.viminfo
..	.bash_logout	.bashrc			.config	.mozilla	test.sh

$ ls -aF
./	.bash_history	.bash_profile	.cache/		.lesshst	.viminfo
../	.bash_logout	.bashrc			.config/	.mozila/	test.sh*
```



## 사용자 정보 확인_id

### <span style="color:red">사용자의 UID와 GID 확인 (id)</span>

* 현재 시스템에 로그인한 사용자 또는 인자로 지정한 사용자의 정보 확인



* 사용법

\- id [사용자 게정]

* 옵션

`- g` : 기본 그룹의 GID만 출력

`- G` : 기본 그룹과 추가 그룹의 GID들을 출력

```Linux
$ id
uid=1000(ubuntu) gid=1000(ubuntu) 그룹들=1000(ubuntu), 4(adm), 24(cdrom), 27(sudo), 30(dip), 46(plugdev), 120(lpadmin), 132(lxd), 133(sambashare)
```



## 로그인 세션_who

### <span style="color:red">현재 로그인 한 모든 사용자 정보 출력(who)</span>

* 현재 접속 되어 있는 사용자들의 계정들의 이름, 접속 회선, 접속시간, 접속한 위치 등 정보 확인



* 옵션

`- q` : 로그인한 계정의 이름과 계정의 수를 출력

`- H` : 출력 정보의 헤더를 표시

```Linux
$ who
ubuntu@ubuntu-VM:~$ who
ubuntu	pts/0		2023-07-16 20:46 (192.168.56.1)
```



## 사용자 암호 변경하기_passwd

### <span style="color:red">사용자 패스워드 지정 (passwd)</span>

* 생성된 계정은 패스워드 설정이 필요함

* 사용법

`- passwd [옵션] [사용자ID]`

```Linux
$ passwd
Changing password for linux.
(current) UNIX password:
Enter new UNIX password:
Retype new UNIX password:
passwd: password_updated successfully
```



## 시스템 정보 수집하기

### <span style="color:red">현재 로그인 된 사용자 정보</span>

```Linux
$ users
ubuntu
$ who
ubuntu	pts/0		2023-07-16	20:46	(192.168.56.1)
$ finger
Login	name	Tty		Idle	Login Time		office		office 	Phone
ubuntu	ubuntu	pts/0			Jul 16 20:46 	(192.168.56.1)
$ last
...
```

### <span style="color:red">운영체제 버전과 하드웨어 정보</span>

```Linux
$ cat /etc/os-release
$ uname -a
$ free					($ less /proc/meminfo: 메모리 정보확인)
$ less /proc/cpuinfo	(processor 정보 확인)
$ lsscsi				($ cat /proc/scsi/scsi: disk 정보 확인)
```

### <span style="color:red">네트워크 정보</span>

```Linux
$ uname -a			($ hostname, $ cat /etc/hostsname)
$ ip address		($ ifconfig)
```



## 사용자 전환

### <span style="color:red">사용자 전환 (Switch User: su)</span>

* 다른 계정 전환을 위해서 로그아웃 -> 로그인 과정이 필요
* 일시적 다른 게정 전환 시 su 명령어 사용

``` Linux
$ su - root
Password:
# id
uid=0(root)	gid=0(root)	그룹들=0(root)
```

### <span style="color:red">다른 사용자의 권한을 명령어 실행 (Switch User Do: sudo)</span>

* 명령어를 다른 사용자 권한으로 실행 (/etc/sudoers)

```Linux
$ sudo useradd hpedu
[sudo] password for linux:
```


