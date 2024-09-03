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
      configs: 'host_files/configs_host_01'
      ssl_renewal: False
      ssl:
        - boba.uberdoghouse.ru
      vhosts:
        - boba.uberdoghouse.ru
```

## Available parameters

| Param | Default | Description |
| -------- | -------- | -------- |
| `configs` | `False` | Path from where nginx configs will be copied (conf.d, nginx.conf, etc.), leave False if you don’t want to copy them. |
| `ssl_renewal` | `False` | Update existing ssl certificates? |
| `ssl` | `False` | Gets list, which domains should you install SSL certificates on, example `domain1.com`. |
| `vhosts` | `False` | Gets list, which virtual hosts need to be activated, example `domain1.com`. |

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
      username: 'dev-user'
      password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          38343139323638626266356363616232323832653963643132623161353331333635613435343665
          3230343138633730373063313264353838386239323833380a643164633562356539616232353534
          31313536346437626436383766323134653664303938366632383933623234373936643836383534
          3663353539333337390a636465616633356338613631613331313532656161336264303430656166
          6530
      sudo: True
      sudoers: 
        - '/usr/bin/systemctl stop systemd-journald'
        - '/usr/bin/systemctl start systemd-journald'
      ssh_keys: 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFgWsNtteONXmQ3Hj1XA5wFvGHnpDHMrA6iZD7LhNxHx'
```

## Available parameters

| Param | Default | Description |
| -------- | -------- | -------- |
| `username` | `no by default` | User to check which to do the rest of the actions. |
| `password` | `False` | Password to which you need to change the user password. |
| `sudo` | `False` | Add in group sudo? |
| `sudoers` | `False` | Gets list, what command add in sudoers? example `'/usr/bin/nano'` |
| `ssh_key` | `False` | Your pub ssh key to login by ssh. |