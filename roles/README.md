# nginx

Role for installation and configuration nginx.

## Usage (example)

```yaml
    - role: nginx
      configs: '{{ configs_ }}'
      ssl_renewal: '{{ ssl_renewal_ }}'
      ssl: '{{ ssl_ }}'
      vhosts: '{{ vhosts_ }}'
```

## Available parameters

| Param | Default | Description |
| -------- | -------- | -------- |
| `configs` | `False` | Path from where nginx configs will be copied (conf.d, nginx.conf, etc.), leave False if you don’t want to copy them. |
| `ssl_renewal` | `False` | Update existing ssl certificates? |
| `ssl` | `no by default` | Which domains should you install SSL certificates on, example `domain1.com`. |
| `vhosts` | `no by default` | Which virtual hosts need to be activated, example `domain1.com`. |

# nginx

Role for installation and configuration nginx.

## Usage (example)

```yaml
    - role: users
      username: '{{ username_ }}'
      password: '{{ password_ }}'
      sudo: '{{ sudo_ }}'
      sudoers: '{{ sudoers_ }}'
      ssh_key: '{{ ssh_key_ }}'
```

## Available parameters

| Param | Default | Description |
| -------- | -------- | -------- |
| `username` | `no by default` | User to check which to do the rest of the actions. |
| `password` | `False` | Password to which you need to change the user password. |
| `sudo` | `False` | Add in group sudo? |
| `sudoers` | `False` | What command add in sudoers? example `'/usr/bin/nano'` |
| `ssh_key` | `False` | Your pub ssh key to login by ssh. |