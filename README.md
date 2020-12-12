[![build-test](https://github.com/darkwizard242/ansible-role-virtualbox/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-virtualbox/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-virtualbox/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-virtualbox/actions?query=workflow%3Arelease)  ![Ansible Role](https://img.shields.io/ansible/role/48401?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/48401?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/48401?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-virtualbox&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-virtualbox) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-virtualbox&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-virtualbox) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-virtualbox&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-virtualbox) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-virtualbox&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-virtualbox) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-virtualbox?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-virtualbox?color=orange&style=flat-square)

# Ansible Role: virtualbox

Role to install (_by default_) [virtualbox-6.1](https://www.virtualbox.org/) package for Debian based systems or uninstall (_if passed as var_).

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
virtualbox_version: 6.1
virtualbox_app_name: virtualbox
virtualbox_desired_state: present
virtualbox_gpg_key: https://www.virtualbox.org/download/oracle_vbox_2016.asc
virtualbox_repo_debian: "deb [arch=amd64] https://download.virtualbox.org/virtualbox/debian {{ ansible_lsb['codename'] }} contrib"
virtualbox_repo_debian_filename: {{ virtualbox_app_name }}
```

### Variables table:

Variable                        | Value (default)                                                                                              | Description
------------------------------- | ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------
virtualbox_version              | `6.1`                                                                                                        | Version of virtualbox to append to the virtualbox_app variable during the installation task.
virtualbox_app                  | `virtualbox`                                                                                                 | Defines the app to install i.e. **virtualbox**
virtualbox_desired_state        | `present`                                                                                                    | Defined to dynamically set whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Defaults to `present`
virtualbox_gpg_key              | <https://www.virtualbox.org/download/oracle_vbox_2016.asc>                                                   | GPG key for Virtualbox
virtualbox_repo_desired_state   | `present`                                                                                                    | State for repo to download Virtualbox from. Can either be 'present' or 'absent'.
virtualbox_repo_debian          | "deb [arch=amd64] <https://download.virtualbox.org/virtualbox/debian> {{ ansible_lsb['codename'] }} contrib" | Virtualbox's repo link for Debian based systems.
virtualbox_repo_debian_filename | `{{ virtualbox_app }}`                                                                                       | Name of file to save for virtualbox's repo in `/etc/apt/sources.list.d/`

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **virtualbox-6.1** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.virtualbox
```

For customizing behavior of role (i.e. installation of latest **virtualbox-6.1** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.virtualbox
  vars:
    virtualbox_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **virtualbox-6.1** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.virtualbox
  vars:
    virtualbox_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-virtualbox/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
