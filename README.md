# Commands you can run

```bash
> ansible -i hosts webserver -m ping

[WARNING]: A duplicate localhost-like entry was found (127.0.0.1). First found localhost was
localhost
[WARNING]: Platform linux on host 127.0.0.1 is using the discovered Python interpreter at
/usr/bin/python3.9, but future installation of another Python interpreter could change the
meaning of that path. See https://docs.ansible.com/ansible-
core/2.12/reference_appendices/interpreter_discovery.html for more information.
127.0.0.1 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3.9"
    },
    "changed": false,
    "ping": "pong"
}

```

```bash
> ansible -i hosts webserver -m shell  -a 'echo ansible says it is fun'

[WARNING]: A duplicate localhost-like entry was found (127.0.0.1). First found localhost was
localhost
[WARNING]: Platform linux on host 127.0.0.1 is using the discovered Python interpreter at
/usr/bin/python3.9, but future installation of another Python interpreter could change the
meaning of that path. See https://docs.ansible.com/ansible-
core/2.12/reference_appendices/interpreter_discovery.html for more information.
127.0.0.1 | CHANGED | rc=0 >>
ansible says it is fun
```

```bash
> ansible all -i hosts -m shell  -a 'echo ansible says it is fun'

[WARNING]: A duplicate localhost-like entry was found (127.0.0.1). First found localhost was
localhost
[WARNING]: Platform linux on host 127.0.0.1 is using the discovered Python interpreter at
/usr/bin/python3.9, but future installation of another Python interpreter could change the
meaning of that path. See https://docs.ansible.com/ansible-
core/2.12/reference_appendices/interpreter_discovery.html for more information.
127.0.0.1 | CHANGED | rc=0 >>
ansible says it is fun
[WARNING]: Platform linux on host localhost is using the discovered Python interpreter at
/usr/bin/python3.9, but future installation of another Python interpreter could change the
meaning of that path. See https://docs.ansible.com/ansible-
core/2.12/reference_appendices/interpreter_discovery.html for more information.
localhost | CHANGED | rc=0 >>
ansible says it is fun

```

# Module `git`

```bash
> ansible mylaptop -i hosts -m git -a "repo='https://github.com/samarthya/spinnaker-hello.git' dest=/tmp/spinnaker"

[WARNING]: A duplicate localhost-like entry was found (127.0.0.1). First found localhost was
localhost
[WARNING]: Platform linux on host localhost is using the discovered Python interpreter at
/usr/bin/python3.9, but future installation of another Python interpreter could change the
meaning of that path. See https://docs.ansible.com/ansible-
core/2.12/reference_appendices/interpreter_discovery.html for more information.
localhost | CHANGED => {
    "after": "1b95b2e5dacb74dd86e1089702eb234d020fcede",
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3.9"
    },
    "before": null,
    "changed": true
}
```

## Output

```bash
> ls /tmp/spinnaker/

bin                Dockerfile  hellow-2.0.0.tgz  Jenkinsfile   node.yaml
cluster-cert.yaml  go.mod      history.txt       kubernetes    README.md
devspace_start.sh  go.sum      images            main.go       sa.yaml
devspace.yaml      hellow      install-ing.sh    main_test.go  server

```

## Using module shell to do the listing

```bash
> ansible mylaptop -i hosts -m shell -a 'ls -als /tmp/spinnaker'
[WARNING]: A duplicate localhost-like entry was found (127.0.0.1). First found localhost was
localhost
[WARNING]: Platform linux on host localhost is using the discovered Python interpreter at
/usr/bin/python3.9, but future installation of another Python interpreter could change the
meaning of that path. See https://docs.ansible.com/ansible-
core/2.12/reference_appendices/interpreter_discovery.html for more information.
localhost | CHANGED | rc=0 >>
total 4596
   4 drwxrwxr-x  7 saurabh saurabh    4096 Feb 17 21:10 .
   4 drwxrwxrwt 30 root    root       4096 Feb 17 21:11 ..
   4 drwxrwxr-x  2 saurabh saurabh    4096 Feb 17 21:10 bin
   4 -rw-rw-r--  1 saurabh saurabh     118 Feb 17 21:10 cluster-cert.yaml
   4 -rwxrwxr-x  1 saurabh saurabh     781 Feb 17 21:10 devspace_start.sh
   8 -rwxrwxr-x  1 saurabh saurabh    4373 Feb 17 21:10 devspace.yaml
   4 -rw-rw-r--  1 saurabh saurabh     320 Feb 17 21:10 Dockerfile
   4 drwxrwxr-x  8 saurabh saurabh    4096 Feb 17 21:10 .git
   4 -rw-rw-r--  1 saurabh saurabh      75 Feb 17 21:10 .gitignore
   4 -rw-rw-r--  1 saurabh saurabh     927 Feb 17 21:10 go.mod
   8 -rw-rw-r--  1 saurabh saurabh    4485 Feb 17 21:10 go.sum
   4 drwxrwxr-x  3 saurabh saurabh    4096 Feb 17 21:10 hellow
   4 -rw-rw-r--  1 saurabh saurabh    2654 Feb 17 21:10 hellow-2.0.0.tgz
   4 -rw-rw-r--  1 saurabh saurabh     389 Feb 17 21:10 history.txt
   4 drwxrwxr-x  2 saurabh saurabh    4096 Feb 17 21:10 images
   4 -rw-rw-r--  1 saurabh saurabh     141 Feb 17 21:10 install-ing.sh
   4 -rw-rw-r--  1 saurabh saurabh    3067 Feb 17 21:10 Jenkinsfile
   4 drwxrwxr-x  2 saurabh saurabh    4096 Feb 17 21:10 kubernetes
   4 -rw-rw-r--  1 saurabh saurabh    1008 Feb 17 21:10 main.go
   4 -rw-rw-r--  1 saurabh saurabh     911 Feb 17 21:10 main_test.go
   4 -rw-rw-r--  1 saurabh saurabh     794 Feb 17 21:10 node.yaml
   4 -rw-rw-r--  1 saurabh saurabh    1210 Feb 17 21:10 README.md
   4 -rw-rw-r--  1 saurabh saurabh     325 Feb 17 21:10 sa.yaml
4496 -rwxrwxr-x  1 saurabh saurabh 4602384 Feb 17 21:10 server
```

# Module `file`

```bash
> ansible -i hosts mylaptop -m file -a "path=/tmp/local owner=saurabh group=saurabh state=directory"
[WARNING]: A duplicate localhost-like entry was found (127.0.0.1). First found localhost was
localhost
[WARNING]: Platform linux on host localhost is using the discovered Python interpreter at
/usr/bin/python3.9, but future installation of another Python interpreter could change the
meaning of that path. See https://docs.ansible.com/ansible-
core/2.12/reference_appendices/interpreter_discovery.html for more information.
localhost | CHANGED => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3.9"
    },
    "changed": true,
    "gid": 1000,
    "group": "saurabh",
    "mode": "0775",
    "owner": "saurabh",
    "path": "/tmp/local",
    "size": 4096,
    "state": "directory",
    "uid": 1000
}

```

```bash
> ls -als /tmp/local
total 8
4 drwxrwxr-x  2 saurabh saurabh 4096 Feb 17 21:25 .
4 drwxrwxrwt 31 root    root    4096 Feb 17 21:25 ..
```

# Module `service`

```bash
> ansible -i hosts mylaptop -m service -a "name=firewalld state=started"

[WARNING]: A duplicate localhost-like entry was found (127.0.0.1). First found localhost was
localhost
[WARNING]: Platform linux on host localhost is using the discovered Python interpreter at
/usr/bin/python3.9, but future installation of another Python interpreter could change the
meaning of that path. See https://docs.ansible.com/ansible-
core/2.12/reference_appendices/interpreter_discovery.html for more information.
localhost | FAILED! => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3.9"
    },
    "changed": false,
    "msg": "Could not find the requested service firewalld: host"
}
```

```bash
> ansible -i hosts mylaptop -m service -a "name=virtualbox state=started"
[WARNING]: A duplicate localhost-like entry was found (127.0.0.1). First found localhost was
localhost
[WARNING]: Platform linux on host localhost is using the discovered Python interpreter at
/usr/bin/python3.9, but future installation of another Python interpreter could change the
meaning of that path. See https://docs.ansible.com/ansible-
core/2.12/reference_appendices/interpreter_discovery.html for more information.
localhost | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3.9"
    },
    "changed": false,
    "name": "virtualbox",
    "state": "started",
    "status": {
        "ActiveEnterTimestamp": "Wed 2022-02-16 16:14:24 IST",
        "ActiveEnterTimestampMonotonic": "13416341",
        "ActiveExitTimestampMonotonic": "0",
        "ActiveState": "active",
        "After": "network-online.target basic.target system.slice remote-fs.target sysinit.target systemd-journald.socket",
        "AllowIsolate": "no",
        "AssertResult": "yes",
        "AssertTimestamp": "Wed 2022-02-16 16:14:24 IST",
        "AssertTimestampMonotonic": "13357727",
        "Before": "shutdown.target graphical.target multi-user.target",
        "BlockIOAccounting": "no",
        "BlockIOWeight": "[not set]",
        "CPUAccounting": "yes",
        "CPUAffinityFromNUMA": "no",
        "CPUQuotaPerSecUSec": "infinity",
        "CPUQuotaPeriodUSec": "infinity",
        "CPUSchedulingPolicy": "0",
        "CPUSchedulingPriority": "0",
        "CPUSchedulingResetOnFork": "no",
        "CPUShares": "[not set]",
        "CPUUsageNSec": "0",
        "CPUWeight": "[not set]",
        "CacheDirectoryMode": "0755",
        "CanFreeze": "yes",
        "CanIsolate": "no",
        "CanReload": "no",
        "CanStart": "yes",
        "CanStop": "yes",
        "CapabilityBoundingSet": "cap_chown cap_dac_override cap_dac_read_search cap_fowner cap_fsetid cap_kill cap_setgid cap_setuid cap_setpcap cap_linux_immutable cap_net_bind_service cap_net_broadcast cap_net_admin cap_net_raw cap_ipc_lock cap_ipc_owner cap_sys_module cap_sys_rawio cap_sys_chroot cap_sys_ptrace cap_sys_pacct cap_sys_admin cap_sys_boot cap_sys_nice cap_sys_resource cap_sys_time cap_sys_tty_config cap_mknod cap_lease cap_audit_write cap_audit_control cap_setfcap cap_mac_override cap_mac_admin cap_syslog cap_wake_alarm cap_block_suspend cap_audit_read cap_perfmon cap_bpf cap_checkpoint_restore",
        "CleanResult": "success",
        "CollectMode": "inactive",
        "ConditionResult": "yes",
        "ConditionTimestamp": "Wed 2022-02-16 16:14:24 IST",
        "ConditionTimestampMonotonic": "13357724",
        "ConfigurationDirectoryMode": "0755",
        "Conflicts": "shutdown.target",
        "ControlGroup": "/system.slice/virtualbox.service",
        "ControlPID": "0",
        "CoredumpFilter": "0x33",
        "DefaultDependencies": "yes",
        "DefaultMemoryLow": "0",
        "DefaultMemoryMin": "0",
        "Delegate": "no",
        "Description": "LSB: VirtualBox Linux kernel module",
        "DevicePolicy": "auto",
        "Documentation": "\"man:systemd-sysv-generator(8)\"",
        "DynamicUser": "no",
        "EffectiveCPUs": "0-7",
        "EffectiveMemoryNodes": "0",
        "ExecMainCode": "0",
        "ExecMainExitTimestampMonotonic": "0",
        "ExecMainPID": "0",
        "ExecMainStartTimestampMonotonic": "0",
        "ExecMainStatus": "0",
        "ExecStart": "{ path=/etc/init.d/virtualbox ; argv[]=/etc/init.d/virtualbox start ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }",
        "ExecStartEx": "{ path=/etc/init.d/virtualbox ; argv[]=/etc/init.d/virtualbox start ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }",
        "ExecStop": "{ path=/etc/init.d/virtualbox ; argv[]=/etc/init.d/virtualbox stop ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }",
        "ExecStopEx": "{ path=/etc/init.d/virtualbox ; argv[]=/etc/init.d/virtualbox stop ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }",
        "FailureAction": "none",
        "FileDescriptorStoreMax": "0",
        "FinalKillSignal": "9",
        "FragmentPath": "/run/systemd/generator.late/virtualbox.service",
        "FreezerState": "running",
        "GID": "[not set]",
        "GuessMainPID": "no",
        "IOAccounting": "no",
        "IOReadBytes": "18446744073709551615",
        "IOReadOperations": "18446744073709551615",
        "IOSchedulingClass": "0",
        "IOSchedulingPriority": "0",
        "IOWeight": "[not set]",
        "IOWriteBytes": "18446744073709551615",
        "IOWriteOperations": "18446744073709551615",
        "IPAccounting": "no",
        "IPEgressBytes": "[no data]",
        "IPEgressPackets": "[no data]",
        "IPIngressBytes": "[no data]",
        "IPIngressPackets": "[no data]",
        "Id": "virtualbox.service",
        "IgnoreOnIsolate": "no",
        "IgnoreSIGPIPE": "no",
        "InactiveEnterTimestampMonotonic": "0",
        "InactiveExitTimestamp": "Wed 2022-02-16 16:14:24 IST",
        "InactiveExitTimestampMonotonic": "13358569",
        "InvocationID": "ce97dd7b58e94c959c5c49fdcef5bff2",
        "JobRunningTimeoutUSec": "infinity",
        "JobTimeoutAction": "none",
        "JobTimeoutUSec": "infinity",
        "KeyringMode": "private",
        "KillMode": "process",
        "KillSignal": "15",
        "LimitAS": "infinity",
        "LimitASSoft": "infinity",
        "LimitCORE": "infinity",
        "LimitCORESoft": "0",
        "LimitCPU": "infinity",
        "LimitCPUSoft": "infinity",
        "LimitDATA": "infinity",
        "LimitDATASoft": "infinity",
        "LimitFSIZE": "infinity",
        "LimitFSIZESoft": "infinity",
        "LimitLOCKS": "infinity",
        "LimitLOCKSSoft": "infinity",
        "LimitMEMLOCK": "65536",
        "LimitMEMLOCKSoft": "65536",
        "LimitMSGQUEUE": "819200",
        "LimitMSGQUEUESoft": "819200",
        "LimitNICE": "0",
        "LimitNICESoft": "0",
        "LimitNOFILE": "524288",
        "LimitNOFILESoft": "1024",
        "LimitNPROC": "127159",
        "LimitNPROCSoft": "127159",
        "LimitRSS": "infinity",
        "LimitRSSSoft": "infinity",
        "LimitRTPRIO": "0",
        "LimitRTPRIOSoft": "0",
        "LimitRTTIME": "infinity",
        "LimitRTTIMESoft": "infinity",
        "LimitSIGPENDING": "127159",
        "LimitSIGPENDINGSoft": "127159",
        "LimitSTACK": "infinity",
        "LimitSTACKSoft": "8388608",
        "LoadState": "loaded",
        "LockPersonality": "no",
        "LogLevelMax": "-1",
        "LogRateLimitBurst": "0",
        "LogRateLimitIntervalUSec": "0",
        "LogsDirectoryMode": "0755",
        "MainPID": "0",
        "ManagedOOMMemoryPressure": "auto",
        "ManagedOOMMemoryPressureLimit": "0",
        "ManagedOOMPreference": "none",
        "ManagedOOMSwap": "auto",
        "MemoryAccounting": "yes",
        "MemoryCurrent": "0",
        "MemoryDenyWriteExecute": "no",
        "MemoryHigh": "infinity",
        "MemoryLimit": "infinity",
        "MemoryLow": "0",
        "MemoryMax": "infinity",
        "MemoryMin": "0",
        "MemorySwapMax": "infinity",
        "MountAPIVFS": "no",
        "NFileDescriptorStore": "0",
        "NRestarts": "0",
        "NUMAPolicy": "n/a",
        "Names": "virtualbox.service",
        "NeedDaemonReload": "no",
        "Nice": "5",
        "NoNewPrivileges": "no",
        "NonBlocking": "no",
        "NotifyAccess": "none",
        "OOMPolicy": "stop",
        "OOMScoreAdjust": "0",
        "OnFailureJobMode": "replace",
        "Perpetual": "no",
        "PrivateDevices": "no",
        "PrivateIPC": "no",
        "PrivateMounts": "no",
        "PrivateNetwork": "no",
        "PrivateTmp": "no",
        "PrivateUsers": "no",
        "ProcSubset": "all",
        "ProtectClock": "no",
        "ProtectControlGroups": "no",
        "ProtectHome": "no",
        "ProtectHostname": "no",
        "ProtectKernelLogs": "no",
        "ProtectKernelModules": "no",
        "ProtectKernelTunables": "no",
        "ProtectProc": "default",
        "ProtectSystem": "no",
        "RefuseManualStart": "no",
        "RefuseManualStop": "no",
        "ReloadResult": "success",
        "RemainAfterExit": "yes",
        "RemoveIPC": "no",
        "Requires": "system.slice sysinit.target",
        "Restart": "no",
        "RestartKillSignal": "15",
        "RestartUSec": "100ms",
        "RestrictNamespaces": "no",
        "RestrictRealtime": "no",
        "RestrictSUIDSGID": "no",
        "Result": "success",
        "RootDirectoryStartOnly": "no",
        "RuntimeDirectoryMode": "0755",
        "RuntimeDirectoryPreserve": "no",
        "RuntimeMaxUSec": "infinity",
        "SameProcessGroup": "no",
        "SecureBits": "0",
        "SendSIGHUP": "no",
        "SendSIGKILL": "yes",
        "Slice": "system.slice",
        "SourcePath": "/etc/init.d/virtualbox",
        "StandardError": "inherit",
        "StandardInput": "null",
        "StandardOutput": "journal",
        "StartLimitAction": "none",
        "StartLimitBurst": "5",
        "StartLimitIntervalUSec": "10s",
        "StartupBlockIOWeight": "[not set]",
        "StartupCPUShares": "[not set]",
        "StartupCPUWeight": "[not set]",
        "StartupIOWeight": "[not set]",
        "StateChangeTimestamp": "Wed 2022-02-16 16:14:24 IST",
        "StateChangeTimestampMonotonic": "13416341",
        "StateDirectoryMode": "0755",
        "StatusErrno": "0",
        "StopWhenUnneeded": "no",
        "SubState": "exited",
        "SuccessAction": "none",
        "SuccessExitStatus": "5 6",
        "SyslogFacility": "3",
        "SyslogLevel": "6",
        "SyslogLevelPrefix": "yes",
        "SyslogPriority": "30",
        "SystemCallErrorNumber": "2147483646",
        "TTYReset": "no",
        "TTYVHangup": "no",
        "TTYVTDisallocate": "no",
        "TasksAccounting": "yes",
        "TasksCurrent": "0",
        "TasksMax": "38147",
        "TimeoutAbortUSec": "5min",
        "TimeoutCleanUSec": "infinity",
        "TimeoutStartFailureMode": "terminate",
        "TimeoutStartUSec": "5min",
        "TimeoutStopFailureMode": "terminate",
        "TimeoutStopUSec": "5min",
        "TimerSlackNSec": "50000",
        "Transient": "no",
        "Type": "forking",
        "UID": "[not set]",
        "UMask": "0022",
        "UnitFilePreset": "enabled",
        "UnitFileState": "generated",
        "UtmpMode": "init",
        "WantedBy": "multi-user.target graphical.target",
        "Wants": "network-online.target",
        "WatchdogSignal": "6",
        "WatchdogTimestampMonotonic": "0",
        "WatchdogUSec": "0"
    }
}

```

# Module `apt`

```bash
> ansible -i hosts mylaptop -m apt -a "name=python3 state=present"

[WARNING]: A duplicate localhost-like entry was found (127.0.0.1). First found localhost was
localhost
[WARNING]: Platform linux on host localhost is using the discovered Python interpreter at
/usr/bin/python3.9, but future installation of another Python interpreter could change the
meaning of that path. See https://docs.ansible.com/ansible-
core/2.12/reference_appendices/interpreter_discovery.html for more information.
localhost | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3.9"
    },
    "cache_update_time": 1645111441,
    "cache_updated": false,
    "changed": false
}

```

# Module `setup`

## Dumps a load of information

```bash
> ansible mylaptop -i hosts -m setup

[WARNING]: A duplicate localhost-like entry was found (127.0.0.1). First found localhost was
localhost
[WARNING]: Platform linux on host localhost is using the discovered Python interpreter at
/usr/bin/python3.9, but future installation of another Python interpreter could change the
meaning of that path. See https://docs.ansible.com/ansible-
core/2.12/reference_appendices/interpreter_discovery.html for more information.
localhost | SUCCESS => {
    "ansible_facts": {
        "ansible_all_ipv4_addresses": [
            "192.168.0.111"
        ],
        "ansible_all_ipv6_addresses": [
            "fe80::f131:9e0:9c64:aa7e"
        ],
        "ansible_apparmor": {
            "status": "enabled"
        },
        "ansible_architecture": "x86_64",
        "ansible_bios_date": "12/08/2021",
        "ansible_bios_vendor": "Dell Inc.",
        "ansible_bios_version": "1.17.0",
        "ansible_board_asset_tag": "NA",
        "ansible_board_name": "07WDVW",
        "ansible_board_serial": "NA",
        "ansible_board_vendor": "Dell Inc.",
        "ansible_board_version": "A01",
        "ansible_chassis_asset_tag": "SAURABH",
        "ansible_chassis_serial": "NA",
        "ansible_chassis_vendor": "Dell Inc.",
        "ansible_chassis_version": "NA",
        "ansible_cmdline": {
            "initrd": "\\EFI\\Pop_OS-bc44e656-f13f-45f3-ba2f-6793cb8b858f\\initrd.img",
            "loglevel": "0",
            "quiet": true,
            "ro": true,
            "root": "UUID=bc44e656-f13f-45f3-ba2f-6793cb8b858f",
            "splash": true,
            "systemd.show_status": "false"
        },
        "ansible_date_time": {
            "date": "2022-02-17",
            "day": "17",
            "epoch": "1645112100",
            "epoch_int": "1645112100",
            "hour": "21",
            "iso8601": "2022-02-17T15:35:00Z",
            "iso8601_basic": "20220217T210500832407",
            "iso8601_basic_short": "20220217T210500",
            "iso8601_micro": "2022-02-17T15:35:00.832407Z",
            "minute": "05",
            "month": "02",
            "second": "00",
            "time": "21:05:00",
            "tz": "IST",
            "tz_dst": "IST",
            "tz_offset": "+0530",
            "weekday": "Thursday",
            "weekday_number": "4",
            "weeknumber": "07",
            "year": "2022"
        },
        "ansible_default_ipv4": {
            "address": "192.168.0.111",
            "alias": "wlo1",
            "broadcast": "192.168.0.255",
            "gateway": "192.168.0.1",
            "interface": "wlo1",
            "macaddress": "08:d2:3e:48:73:6c",
            "mtu": 1500,
            "netmask": "255.255.255.0",
            "network": "192.168.0.0",
            "type": "ether"
        },
        "ansible_default_ipv6": {},
        "ansible_device_links": {
            "ids": {
                "dm-0": [
                    "dm-name-cryptswap",
                    "dm-uuid-CRYPT-PLAIN-cryptswap"
                ],
                "nvme0n1": [
                    "nvme-PC611_NVMe_SK_hynix_512GB_ND03N9792106Y4E60",
                    "nvme-eui.ace42e000a2de8de2ee4ac0000000001"
                ],
                "nvme0n1p1": [
                    "nvme-PC611_NVMe_SK_hynix_512GB_ND03N9792106Y4E60-part1",
                    "nvme-eui.ace42e000a2de8de2ee4ac0000000001-part1"
                ],
                "nvme0n1p2": [
                    "nvme-PC611_NVMe_SK_hynix_512GB_ND03N9792106Y4E60-part2",
                    "nvme-eui.ace42e000a2de8de2ee4ac0000000001-part2"
                ],
                "nvme0n1p3": [
                    "nvme-PC611_NVMe_SK_hynix_512GB_ND03N9792106Y4E60-part3",
                    "nvme-eui.ace42e000a2de8de2ee4ac0000000001-part3"
                ],
                "nvme0n1p4": [
                    "nvme-PC611_NVMe_SK_hynix_512GB_ND03N9792106Y4E60-part4",
                    "nvme-eui.ace42e000a2de8de2ee4ac0000000001-part4"
                ]
            },
            "labels": {
                "dm-0": [
                    "cryptswap"
                ]
            },
            "masters": {
                "nvme0n1p2": [
                    "dm-0"
                ]
            },
            "uuids": {
                "dm-0": [
                    "4a87272e-bd49-4ba3-b10f-3aec023966e3"
                ],
                "nvme0n1p1": [
                    "2865-4EB6"
                ],
                "nvme0n1p2": [
                    "17562efd-75b2-4547-b8ff-5da7c158144b"
                ],
                "nvme0n1p3": [
                    "edb857a3-6587-4427-99f3-595f8ca1dfe9"
                ],
                "nvme0n1p4": [
                    "bc44e656-f13f-45f3-ba2f-6793cb8b858f"
                ]
            }
        },
        "ansible_devices": {
            "dm-0": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [
                        "dm-name-cryptswap",
                        "dm-uuid-CRYPT-PLAIN-cryptswap"
                    ],
                    "labels": [
                        "cryptswap"
                    ],
                    "masters": [],
                    "uuids": [
                        "4a87272e-bd49-4ba3-b10f-3aec023966e3"
                    ]
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "0",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "",
                "sectors": "16382975",
                "sectorsize": "512",
                "size": "7.81 GB",
                "support_discard": "0",
                "vendor": null,
                "virtual": 1
            },
            "loop0": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "0",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "none",
                "sectors": "113680",
                "sectorsize": "512",
                "size": "55.51 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop1": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "0",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "none",
                "sectors": "6800",
                "sectorsize": "512",
                "size": "3.32 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop2": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "0",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "none",
                "sectors": "0",
                "sectorsize": "512",
                "size": "0.00 Bytes",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop3": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "0",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "none",
                "sectors": "0",
                "sectorsize": "512",
                "size": "0.00 Bytes",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop4": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "0",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "none",
                "sectors": "428760",
                "sectorsize": "512",
                "size": "209.36 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop5": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "0",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "none",
                "sectors": "89264",
                "sectorsize": "512",
                "size": "43.59 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop6": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "0",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "none",
                "sectors": "0",
                "sectorsize": "512",
                "size": "0.00 Bytes",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop7": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "none",
                "sectors": "0",
                "sectorsize": "512",
                "size": "0.00 Bytes",
                "support_discard": "0",
                "vendor": null,
                "virtual": 1
            },
            "nvme0n1": {
                "holders": [],
                "host": "Non-Volatile memory controller: SK hynix Device 1639",
                "links": {
                    "ids": [
                        "nvme-PC611_NVMe_SK_hynix_512GB_ND03N9792106Y4E60",
                        "nvme-eui.ace42e000a2de8de2ee4ac0000000001"
                    ],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": "PC611 NVMe SK hynix 512GB",
                "partitions": {
                    "nvme0n1p1": {
                        "holders": [],
                        "links": {
                            "ids": [
                                "nvme-PC611_NVMe_SK_hynix_512GB_ND03N9792106Y4E60-part1",
                                "nvme-eui.ace42e000a2de8de2ee4ac0000000001-part1"
                            ],
                            "labels": [],
                            "masters": [],
                            "uuids": [
                                "2865-4EB6"
                            ]
                        },
                        "sectors": "1023999",
                        "sectorsize": 512,
                        "size": "500.00 MB",
                        "start": "2048",
                        "uuid": "2865-4EB6"
                    },
                    "nvme0n1p2": {
                        "holders": [
                            "cryptswap"
                        ],
                        "links": {
                            "ids": [
                                "nvme-PC611_NVMe_SK_hynix_512GB_ND03N9792106Y4E60-part2",
                                "nvme-eui.ace42e000a2de8de2ee4ac0000000001-part2"
                            ],
                            "labels": [],
                            "masters": [
                                "dm-0"
                            ],
                            "uuids": [
                                "17562efd-75b2-4547-b8ff-5da7c158144b"
                            ]
                        },
                        "sectors": "16383999",
                        "sectorsize": 512,
                        "size": "7.81 GB",
                        "start": "1026048",
                        "uuid": "17562efd-75b2-4547-b8ff-5da7c158144b"
                    },
                    "nvme0n1p3": {
                        "holders": [],
                        "links": {
                            "ids": [
                                "nvme-PC611_NVMe_SK_hynix_512GB_ND03N9792106Y4E60-part3",
                                "nvme-eui.ace42e000a2de8de2ee4ac0000000001-part3"
                            ],
                            "labels": [],
                            "masters": [],
                            "uuids": [
                                "edb857a3-6587-4427-99f3-595f8ca1dfe9"
                            ]
                        },
                        "sectors": "266239999",
                        "sectorsize": 512,
                        "size": "126.95 GB",
                        "start": "17410048",
                        "uuid": "edb857a3-6587-4427-99f3-595f8ca1dfe9"
                    },
                    "nvme0n1p4": {
                        "holders": [],
                        "links": {
                            "ids": [
                                "nvme-PC611_NVMe_SK_hynix_512GB_ND03N9792106Y4E60-part4",
                                "nvme-eui.ace42e000a2de8de2ee4ac0000000001-part4"
                            ],
                            "labels": [],
                            "masters": [],
                            "uuids": [
                                "bc44e656-f13f-45f3-ba2f-6793cb8b858f"
                            ]
                        },
                        "sectors": "716564479",
                        "sectorsize": 512,
                        "size": "341.68 GB",
                        "start": "283650048",
                        "uuid": "bc44e656-f13f-45f3-ba2f-6793cb8b858f"
                    }
                },
                "removable": "0",
                "rotational": "0",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "none",
                "sectors": "1000215216",
                "sectorsize": "512",
                "serial": "ND03N9792106Y4E60",
                "size": "476.94 GB",
                "support_discard": "512",
                "vendor": null,
                "virtual": 1
            }
        },
        "ansible_distribution": "Pop!_OS",
        "ansible_distribution_file_parsed": true,
        "ansible_distribution_file_path": "/etc/os-release",
        "ansible_distribution_file_variety": "NA",
        "ansible_distribution_major_version": "21",
        "ansible_distribution_release": "impish",
        "ansible_distribution_version": "21.10",
        "ansible_dns": {
            "nameservers": [
                "127.0.0.53"
            ],
            "options": {
                "edns0": true,
                "trust-ad": true
            },
            "search": [
                "."
            ]
        },
        "ansible_domain": "",
        "ansible_effective_group_id": 1000,
        "ansible_effective_user_id": 1000,
        "ansible_env": {
            "DBUS_SESSION_BUS_ADDRESS": "unix:path=/run/user/1000/bus",
            "HOME": "/home/saurabh",
            "LANG": "en_US.UTF-8",
            "LANGUAGE": "en_US:en",
            "LC_ADDRESS": "en_US.UTF-8",
            "LC_IDENTIFICATION": "en_US.UTF-8",
            "LC_MEASUREMENT": "en_US.UTF-8",
            "LC_MONETARY": "en_US.UTF-8",
            "LC_NAME": "en_US.UTF-8",
            "LC_NUMERIC": "en_US.UTF-8",
            "LC_PAPER": "en_US.UTF-8",
            "LC_TELEPHONE": "en_US.UTF-8",
            "LC_TIME": "en_US.UTF-8",
            "LOGNAME": "saurabh",
            "MOTD_SHOWN": "pam",
            "PAPERSIZE": "letter",
            "PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin",
            "PWD": "/home/saurabh",
            "SHELL": "/bin/bash",
            "SHLVL": "0",
            "SSH_CLIENT": "::1 39596 22",
            "SSH_CONNECTION": "::1 39596 ::1 22",
            "SSH_TTY": "/dev/pts/2",
            "TERM": "xterm-256color",
            "USER": "saurabh",
            "XDG_RUNTIME_DIR": "/run/user/1000",
            "XDG_SESSION_CLASS": "user",
            "XDG_SESSION_ID": "20",
            "XDG_SESSION_TYPE": "tty",
            "_": "/bin/sh"
        },
        "ansible_fibre_channel_wwn": [],
        "ansible_fips": false,
        "ansible_form_factor": "Notebook",
        "ansible_fqdn": "samarthya-pop",
        "ansible_hostname": "samarthya-pop",
        "ansible_hostnqn": "",
        "ansible_interfaces": [
            "wlo1",
            "lo"
        ],
        "ansible_is_chroot": false,
        "ansible_iscsi_iqn": "",
        "ansible_kernel": "5.15.15-76051515-generic",
        "ansible_kernel_version": "#202201160435~1642693824~21.10~97db1bb SMP Thu Jan 20 17:35:05 U",
        "ansible_lo": {
            "active": true,
            "device": "lo",
            "ipv4": {
                "address": "127.0.0.1",
                "broadcast": "",
                "netmask": "255.0.0.0",
                "network": "127.0.0.0"
            },
            "ipv6": [
                {
                    "address": "::1",
                    "prefix": "128",
                    "scope": "host"
                }
            ],
            "mtu": 65536,
            "promisc": false,
            "type": "loopback"
        },
        "ansible_local": {},
        "ansible_lsb": {
            "codename": "impish",
            "description": "Pop!_OS 21.10",
            "id": "Pop",
            "major_release": "21",
            "release": "21.10"
        },
        "ansible_machine": "x86_64",
        "ansible_machine_id": "3306e45903727e725a90953b6059a2f0",
        "ansible_memfree_mb": 15502,
        "ansible_memory_mb": {
            "nocache": {
                "free": 24817,
                "used": 7049
            },
            "real": {
                "free": 15502,
                "total": 31866,
                "used": 16364
            },
            "swap": {
                "cached": 0,
                "free": 7999,
                "total": 7999,
                "used": 0
            }
        },
        "ansible_memtotal_mb": 31866,
        "ansible_mounts": [
            {
                "block_available": 17445034,
                "block_size": 4096,
                "block_total": 87902391,
                "block_used": 70457357,
                "device": "/dev/nvme0n1p4",
                "fstype": "ext4",
                "inode_available": 21691216,
                "inode_total": 22396928,
                "inode_used": 705712,
                "mount": "/",
                "options": "rw,noatime,errors=remount-ro",
                "size_available": 71454859264,
                "size_total": 360048193536,
                "uuid": "bc44e656-f13f-45f3-ba2f-6793cb8b858f"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 445,
                "block_used": 445,
                "device": "/dev/loop0",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 10847,
                "inode_used": 10847,
                "mount": "/snap/core18/2284",
                "options": "ro,nodev,relatime,errors=continue",
                "size_available": 0,
                "size_total": 58327040,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 27,
                "block_used": 27,
                "device": "/dev/loop1",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 4,
                "inode_used": 4,
                "mount": "/snap/exercism/5",
                "options": "ro,nodev,relatime,errors=continue",
                "size_available": 0,
                "size_total": 3538944,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 1675,
                "block_used": 1675,
                "device": "/dev/loop4",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 5095,
                "inode_used": 5095,
                "mount": "/snap/microk8s/2948",
                "options": "ro,nodev,relatime,errors=continue",
                "size_available": 0,
                "size_total": 219545600,
                "uuid": "N/A"
            },
            {
                "block_available": 5581674,
                "block_size": 4096,
                "block_total": 32626448,
                "block_used": 27044774,
                "device": "/dev/nvme0n1p3",
                "fstype": "ext4",
                "inode_available": 7848543,
                "inode_total": 8323072,
                "inode_used": 474529,
                "mount": "/home",
                "options": "rw,noatime,errors=remount-ro",
                "size_available": 22862536704,
                "size_total": 133637931008,
                "uuid": "edb857a3-6587-4427-99f3-595f8ca1dfe9"
            },
            {
                "block_available": 68003,
                "block_size": 4096,
                "block_total": 127745,
                "block_used": 59742,
                "device": "/dev/nvme0n1p1",
                "fstype": "vfat",
                "inode_available": 0,
                "inode_total": 0,
                "inode_used": 0,
                "mount": "/boot/efi",
                "options": "rw,relatime,fmask=0077,dmask=0077,codepage=437,iocharset=iso8859-1,shortname=mixed,errors=remount-ro",
                "size_available": 278540288,
                "size_total": 523243520,
                "uuid": "2865-4EB6"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 349,
                "block_used": 349,
                "device": "/dev/loop5",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 480,
                "inode_used": 480,
                "mount": "/snap/snapd/14978",
                "options": "ro,nodev,relatime,errors=continue",
                "size_available": 0,
                "size_total": 45744128,
                "uuid": "N/A"
            }
        ],
        "ansible_nodename": "samarthya-pop",
        "ansible_os_family": "Debian",
        "ansible_pkg_mgr": "apt",
        "ansible_proc_cmdline": {
            "initrd": "\\EFI\\Pop_OS-bc44e656-f13f-45f3-ba2f-6793cb8b858f\\initrd.img",
            "loglevel": "0",
            "quiet": true,
            "ro": true,
            "root": "UUID=bc44e656-f13f-45f3-ba2f-6793cb8b858f",
            "splash": true,
            "systemd.show_status": "false"
        },
        "ansible_processor": [
            "0",
            "GenuineIntel",
            "Intel(R) Core(TM) i7-8665U CPU @ 1.90GHz",
            "1",
            "GenuineIntel",
            "Intel(R) Core(TM) i7-8665U CPU @ 1.90GHz",
            "2",
            "GenuineIntel",
            "Intel(R) Core(TM) i7-8665U CPU @ 1.90GHz",
            "3",
            "GenuineIntel",
            "Intel(R) Core(TM) i7-8665U CPU @ 1.90GHz",
            "4",
            "GenuineIntel",
            "Intel(R) Core(TM) i7-8665U CPU @ 1.90GHz",
            "5",
            "GenuineIntel",
            "Intel(R) Core(TM) i7-8665U CPU @ 1.90GHz",
            "6",
            "GenuineIntel",
            "Intel(R) Core(TM) i7-8665U CPU @ 1.90GHz",
            "7",
            "GenuineIntel",
            "Intel(R) Core(TM) i7-8665U CPU @ 1.90GHz"
        ],
        "ansible_processor_cores": 4,
        "ansible_processor_count": 1,
        "ansible_processor_nproc": 8,
        "ansible_processor_threads_per_core": 2,
        "ansible_processor_vcpus": 8,
        "ansible_product_name": "Latitude 7400",
        "ansible_product_serial": "NA",
        "ansible_product_uuid": "NA",
        "ansible_product_version": "NA",
        "ansible_python": {
            "executable": "/usr/bin/python3.9",
            "has_sslcontext": true,
            "type": "cpython",
            "version": {
                "major": 3,
                "micro": 7,
                "minor": 9,
                "releaselevel": "final",
                "serial": 0
            },
            "version_info": [
                3,
                9,
                7,
                "final",
                0
            ]
        },
        "ansible_python_version": "3.9.7",
        "ansible_real_group_id": 1000,
        "ansible_real_user_id": 1000,
        "ansible_selinux": {
            "status": "disabled"
        },
        "ansible_selinux_python_present": true,
        "ansible_service_mgr": "systemd",
        "ansible_ssh_host_key_ecdsa_public": "AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBJ+nlnqYLLtX7itaFy52hUSDq4TErRqCrApkGCu+bv9D6OSndpTU/tFPab8lCkBk9t5zKpuLhX7RfzWHhXHs858=",
        "ansible_ssh_host_key_ecdsa_public_keytype": "ecdsa-sha2-nistp256",
        "ansible_ssh_host_key_ed25519_public": "AAAAC3NzaC1lZDI1NTE5AAAAIFvcLmubh+CkVYhMtMJlBo/q+pFFHQqTFDDMwGixEs7l",
        "ansible_ssh_host_key_ed25519_public_keytype": "ssh-ed25519",
        "ansible_ssh_host_key_rsa_public": "AAAAB3NzaC1yc2EAAAADAQABAAABgQCZBRCeB6lkcDZtFmZ3Tp24AGJB1GdxEhQyLgpn3FA2E+/oH4Gcn6Zb1bgpzkzAaHzxY6sxw/UUNmkhEe+9RimJf0Fa1RshfeMGpYnCoz93GaKQkvY+zIk2cEodVQqUSokgl6Fm8dqkdS8LFVzNfck9ZWqcLbomICw2/C6MZOAmnLJ02Us0ruQxCmCOCmRTQ72qknXNEeXiMQR+rWUdSjgCeuQmd7lc63ez6eNwCNqsQKx/rbS6BeAzKONUx7V4NxHfPR0tjjA8bsV5xYaCE6S5aBg6YICh3ck8Myb4ZyuOcFw9m3d9t19x3tyqE5ba2VmYwP+I0JYdd6ANjdN/q6ZYcwQVeoL+E87WpXpPFCep8/ip9JvTFLMPhMlyPHqts+mvjKKXCY259En1QHPDyD7eBdcr9OMUuRxOT1xGEpkKb5aX4VqrBAZ3yf6Fbu/+p8kAPXXnMnkSHtczVqXxeb0JEOO8Kje/EKmZmKsmsNBcceNXL1g7siN9G29OjyoYO58=",
        "ansible_ssh_host_key_rsa_public_keytype": "ssh-rsa",
        "ansible_swapfree_mb": 7999,
        "ansible_swaptotal_mb": 7999,
        "ansible_system": "Linux",
        "ansible_system_capabilities": [
            ""
        ],
        "ansible_system_capabilities_enforced": "True",
        "ansible_system_vendor": "Dell Inc.",
        "ansible_uptime_seconds": 103846,
        "ansible_user_dir": "/home/saurabh",
        "ansible_user_gecos": "Saurabh Sharma,,,",
        "ansible_user_gid": 1000,
        "ansible_user_id": "saurabh",
        "ansible_user_shell": "/bin/bash",
        "ansible_user_uid": 1000,
        "ansible_userspace_architecture": "x86_64",
        "ansible_userspace_bits": "64",
        "ansible_virtualization_role": "host",
        "ansible_virtualization_tech_guest": [],
        "ansible_virtualization_tech_host": [
            "kvm",
            "virtualbox"
        ],
        "ansible_virtualization_type": "kvm",
        "ansible_wlo1": {
            "active": true,
            "device": "wlo1",
            "ipv4": {
                "address": "192.168.0.111",
                "broadcast": "192.168.0.255",
                "netmask": "255.255.255.0",
                "network": "192.168.0.0"
            },
            "ipv6": [
                {
                    "address": "fe80::f131:9e0:9c64:aa7e",
                    "prefix": "64",
                    "scope": "link"
                }
            ],
            "macaddress": "08:d2:3e:48:73:6c",
            "module": "iwlwifi",
            "mtu": 1500,
            "pciid": "0000:00:14.3",
            "promisc": false,
            "type": "ether"
        },
        "discovered_interpreter_python": "/usr/bin/python3.9",
        "gather_subset": [
            "all"
        ],
        "module_setup": true
    },
    "changed": false
}saurb

```

# Copy ssh key into autorized_keys file

```bash
ssh-copy-od <remote machine>
```

# Glossary

We define our plays using the word tasks with all modules we need as part of our playbook.

# BECOME

## With `become_method: sudo`

```bash
ansible-playbook -i hosts webserver-playbook.yaml  --ask-become
BECOME password: 
[WARNING]: A duplicate localhost-like entry was found (127.0.0.1). First found localhost was
localhost

PLAY [webserver] ****************************************************************************

TASK [Gathering Facts] **********************************************************************
[WARNING]: Platform linux on host 127.0.0.1 is using the discovered Python interpreter at
/usr/bin/python3.9, but future installation of another Python interpreter could change the
meaning of that path. See https://docs.ansible.com/ansible-
core/2.12/reference_appendices/interpreter_discovery.html for more information.
ok: [127.0.0.1]

TASK [ensure apache is installed and up to date] ********************************************

changed: [127.0.0.1]

TASK [write the apache config file] *********************************************************
ok: [127.0.0.1]

TASK [apache is running (and enable it at boot)] ********************************************
ok: [127.0.0.1]

PLAY RECAP **********************************************************************************
127.0.0.1                  : ok=4    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```

## With `become_method: su`

```bash
saurabh@samarthya-pop:~/sourcebox/ansible$ ansible-playbook -i hosts webserver-playbook.yaml --ask-become -K
BECOME password: 
[WARNING]: A duplicate localhost-like entry was found (127.0.0.1). First found localhost was
localhost

PLAY [webserver] ****************************************************************************

TASK [Gathering Facts] **********************************************************************
[WARNING]: Platform linux on host 127.0.0.1 is using the discovered Python interpreter at
/usr/bin/python3.9, but future installation of another Python interpreter could change the
meaning of that path. See https://docs.ansible.com/ansible-
core/2.12/reference_appendices/interpreter_discovery.html for more information.
ok: [127.0.0.1]

TASK [ensure apache is installed and up to date] ********************************************
fatal: [127.0.0.1]: FAILED! => {"msg": "Incorrect su password"}

PLAY RECAP **********************************************************************************
127.0.0.1                  : ok=1    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0 
```