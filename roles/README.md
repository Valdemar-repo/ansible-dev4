# nginx

Role for installation and configuration nginx.

## Step-by-Step

- install nginx and certbot
- remove default nginx host
- copy nginx configs
- renew ssl certificates
- add ssl certs
- activate vhosts

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
| `ssl` | `False` | Which domains should you install SSL certificates on, example `domain1.com`. |
| `vhosts` | `False` | Which virtual hosts need to be activated, example `domain1.com`. |

# users

Role for configuration existing user.

## Step-by-Step

- check if user exist
- change his password (optional)
- add in sudo (optional)
- add in sudoers (optional)
- add ssh key (optional)


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