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