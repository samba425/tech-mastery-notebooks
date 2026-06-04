# Ansible Interview Questions — Zero to Hero

320+ questions covering fundamentals through advanced topics with hands-on labs, mock interview sets, scenario-based questions, comparison tables, cheat sheet, and curated resources.

> Aligned with **EX407 / EX374 (Red Hat Ansible Automation Platform)** objectives and common DevOps/SRE interview formats.

---

## Table of Contents

- [A. Fundamentals & Core Concepts](#a-fundamentals--core-concepts)
- [B. Architecture & Internals](#b-architecture--internals)
- [C. Configuration & Day-to-Day Usage](#c-configuration--day-to-day-usage)
- [D. Advanced Topics](#d-advanced-topics)
- [E. Security, Performance & Best Practices](#e-security-performance--best-practices)
- [F. Troubleshooting & Debugging](#f-troubleshooting--debugging)
- [G. Real-World Scenario-Based Questions](#g-real-world-scenario-based-questions)
- [H. Comparison Tables](#h-comparison-tables)
- [I. Hands-On Labs](#i-hands-on-labs)
- [J. Mock Interview Sets](#j-mock-interview-sets)
- [K. Cheat Sheet](#k-cheat-sheet)
- [L. Curated Resources](#l-curated-resources)

---

## A. Fundamentals & Core Concepts

**1. What is Ansible?**
An open-source IT automation tool written in Python. Uses SSH (or WinRM) to push declarative state to managed nodes — no agent required.

**2. Agentless: what does it mean?**
Managed nodes need only Python and SSH access. The controller pushes modules over SSH and executes them remotely.

**3. Who uses Ansible and for what?**
DevOps, SRE, sysadmins for configuration management, application deployment, orchestration, provisioning, patching, network/security automation, and continuous compliance.

**4. Control node vs managed node?**
Control node: where `ansible`, `ansible-playbook`, and inventory live. Managed nodes: targets receiving changes.

**5. What is a playbook?**
A YAML file with an ordered list of plays. Each play maps a group of hosts to tasks, handlers, and variables.

**6. What is a play?**
A unit inside a playbook that targets a set of hosts and runs an ordered list of tasks.

**7. What is a task?**
A single action — invocation of a module with parameters and optional name/when/loop.

**8. What is a module?**
A unit of work (e.g., `apt`, `yum`, `copy`, `service`, `template`, `command`). Ansible ships hundreds; collections add thousands more.

**9. What is a collection?**
A distribution format bundling modules, plugins, roles, and playbooks under a namespace (e.g., `community.general`, `ansible.posix`, `kubernetes.core`).

**10. What is a role?**
A reusable, self-contained structure for organizing tasks/handlers/vars/files/templates, with a defined directory layout.

**11. What is an inventory?**
A file (INI, YAML, or dynamic script) listing hosts and groups. Default: `/etc/ansible/hosts`.

**12. What is idempotency?**
Running the same playbook repeatedly produces the same result — modules detect existing state and only change when necessary.

**13. What is a handler?**
A task triggered by a `notify:` from another task; runs once at the end of the play (or earlier via `meta: flush_handlers`).

**14. What's `when:` for?**
Conditional execution per host or per item: `when: ansible_os_family == 'Debian'`.

**15. What's `loop:` for?**
Iterate a task over a list: `loop: [nginx, postgresql, redis]`.

**16. Difference between `loop` and `with_items`?**
`with_items` is older; `loop` is preferred since 2.5. Behavior is similar.

**17. What is a fact?**
Auto-discovered system data (OS, IP, memory, mounts) collected by the `setup` module on each play unless `gather_facts: false`.

**18. What is `ansible.cfg`?**
A configuration file at the project root or `/etc/ansible/ansible.cfg`. Controls defaults (inventory path, forks, callbacks, SSH, fact caching).

**19. What is `ansible-galaxy`?**
A CLI to install roles and collections from Ansible Galaxy or Git: `ansible-galaxy collection install community.general`.

**20. What is Ansible Vault?**
A built-in mechanism for encrypting variables/files with AES-256-CTR + HMAC-SHA-256. Used for secrets in source-controlled inventories.

**21. What's a vars file?**
A YAML file referenced by `vars_files:` to externalize variables from a play.

**22. group_vars vs host_vars?**
Directories or files keyed by group/host name; auto-loaded and merged with appropriate precedence.

**23. What is a template?**
A Jinja2 file (`.j2`) rendered by the `template` module with variables substituted.

**24. What is Jinja2?**
A Python templating engine. Ansible uses it for variable interpolation, filters, conditionals, and loops in templates and tasks.

**25. `command` vs `shell` vs `raw`?**
`command`: runs a binary with args (no shell, safer). `shell`: full shell features (pipes, globbing). `raw`: bypasses module subsystem; needed when Python isn't installed.

**26. Why prefer modules over `shell`?**
Modules are idempotent, return structured data, and integrate with check mode. `shell` defeats those.

**27. What is `become`?**
Privilege escalation (default to sudo): `become: yes`. Use `become_user`, `become_method`.

**28. What is `delegate_to`?**
Run a task on a different host than the play target — common for load balancer removal, DNS updates.

**29. What is `run_once`?**
Run a task only once per play, regardless of how many hosts; useful with `delegate_to`.

**30. What is `serial`?**
Limit how many hosts a play touches at a time — e.g., `serial: 2` for batched rolling updates.

**31. What is `strategy`?**
Controls task execution order across hosts. `linear` (default) waits for all hosts before next task; `free` lets each host run as fast as it can.

**32. What's a play `block`?**
Groups tasks for shared `when`, `tags`, `become`, or for error handling with `rescue:` and `always:`.

**33. What's `rescue:`?**
Like `catch`: runs if any task in the block fails.

**34. What's `always:`?**
Like `finally`: runs whether the block succeeded or not.

**35. What's `ignore_errors`?**
Continues play even if a task fails. Use sparingly; consider `failed_when:` or `block/rescue` for clearer intent.

**36. What's `failed_when`?**
Override module's success/failure determination based on output/registered values.

**37. What's `changed_when`?**
Override Ansible's change detection. Useful for `command`/`shell` which always report changed.

**38. What's `register`?**
Save module output to a variable for later use.

**39. Ad-hoc command?**
One-off CLI invocation: `ansible all -m ping -i inventory.ini`.

**40. What does `--check` do?**
Dry run: don't make changes. Modules that don't support check mode skip.

**41. What does `--diff` do?**
Show file-change diffs for `template`, `copy`, etc.

**42. What does `--tags` do?**
Run only tasks tagged with the given tag(s): `--tags "config,restart"`.

**43. What does `--skip-tags` do?**
Inverse of `--tags`.

**44. What is `meta: end_play`?**
Stops the current play for the current host(s). Useful to short-circuit.

**45. What is `meta: flush_handlers`?**
Forces handlers to run immediately instead of at end of play.

**46. `static: yes` in `import_tasks` vs `dynamic: yes` in `include_tasks`?**
`import_*` is preprocessed (static, like a C `#include`); `include_*` is processed at runtime (dynamic, supports loops/vars).

**47. What is `roles/`?**
Default directory Ansible searches for roles defined in plays (`roles:` keyword).

**48. Role directory structure?**
```
roles/myrole/
  tasks/main.yml
  handlers/main.yml
  templates/
  files/
  vars/main.yml
  defaults/main.yml
  meta/main.yml
  library/        # custom modules
  filter_plugins/
  README.md
```

**49. Difference between `vars/` and `defaults/`?**
`defaults/` is lowest-precedence (easy to override). `vars/` is higher-precedence and harder to override.

**50. What's `meta/main.yml` in a role?**
Role metadata: dependencies, supported platforms, Galaxy info.

**51. What is `ansible-pull`?**
Reverse mode where the managed node pulls and applies its own playbook from a Git repo. Useful for autonomous, agent-like behavior.

**52. What's a dynamic inventory?**
A script or plugin returning JSON inventory at runtime. Used for cloud providers (`aws_ec2`, `azure_rm`, `gcp_compute`), Kubernetes, etc.

**53. What's `ansible-inventory`?**
Tool to inspect resolved inventory: `ansible-inventory --list -i inventory.aws_ec2.yml`.

**54. What's the `setup` module?**
Gathers facts (`ansible_*` variables). Implicit at the start of each play unless `gather_facts: false`.

**55. What are facts cached for?**
Speed: avoid re-gathering on subsequent plays. Configure with `fact_caching` (`jsonfile`, `redis`, `memcached`).

**56. What's `gather_subset`?**
Limit fact gathering to subsets (`min`, `network`, `hardware`, `virtual`) for speed.

**57. What's `delegate_facts`?**
Apply registered/`set_fact` data to the delegated host instead of the inventory host.

**58. Difference between `set_fact` and `vars`?**
`set_fact` defines a fact at runtime (persists across the play and survives caching). `vars` is play/task scope.

**59. What's `include_vars`?**
Loads variables from a file at runtime, optionally with conditions.

**60. What is `localhost`?**
Implicit host used when no remote host is needed; runs tasks on the control node.

---

## B. Architecture & Internals

**61. How does Ansible connect to managed nodes?**
By default OpenSSH (Paramiko fallback), or specific connection plugins (`winrm`, `local`, `docker`, `kubectl`, `network_cli`, `httpapi`, `netconf`).

**62. What's the execution flow of a task?**
1) Render module + args 2) Transfer to remote (or use pipelining) 3) Execute under remote Python 4) Return JSON via stdout 5) Controller parses result and continues.

**63. What is pipelining?**
Sends module data over the open SSH session's stdin without writing temp files. Big speedup; requires `requiretty=false` in sudoers.

**64. Where do modules execute?**
On the managed node (remote interpreter). Some "action plugins" (`template`, `copy`) preprocess on the controller before invoking the matching remote module.

**65. What's the difference between a module and a plugin?**
Modules run on managed nodes. Plugins (callback, action, connection, lookup, filter, inventory, vars) run on the controller and extend Ansible itself.

**66. List plugin types.**
- Connection: how to talk to a node
- Action: pre/post processing for a task
- Lookup: data retrieval at evaluation (`with_file`, `password`)
- Filter / Test: Jinja2 transformations
- Callback: hook into events (logging, JSON output)
- Inventory: dynamic host sources
- Vars: load variable data
- Cache: fact caching backends
- Strategy: task execution model
- Become: privilege escalation methods

**67. What is a `library/` directory?**
A role's local custom modules — `library/mymodule.py` becomes available as `mymodule:`.

**68. How is variable precedence determined?**
22+ levels (see official docs). Roughly low → high:
1) `defaults/main.yml`
2) inventory file vars
3) inventory `group_vars/all`
4) inventory `group_vars/<group>`
5) inventory `host_vars/<host>`
6) playbook `group_vars`/`host_vars`
7) host facts / cached facts
8) play vars / vars_files / vars_prompt
9) role vars / `vars/main.yml`
10) block vars / task vars
11) include_vars
12) set_facts / registered vars
13) role params (`roles: - { role: x, var: 1 }`)
14) include params
15) extra vars (`-e`) — highest

**69. What are extra vars?**
Variables passed at CLI: `-e foo=bar` or `-e @vars.json`. Highest precedence.

**70. What is `ansible_connection`?**
The connection plugin used per host (`ssh`, `local`, `winrm`, etc.).

**71. What is the `_meta` field in dynamic inventory output?**
Holds `hostvars`, allowing efficient one-call inventory retrieval (avoids per-host inventory script invocations).

**72. What is `inventory_hostname` vs `ansible_host`?**
`inventory_hostname`: name in inventory (Ansible's identifier). `ansible_host`: IP/DNS used for the connection.

**73. What are magic variables?**
Auto-populated: `hostvars`, `groups`, `group_names`, `inventory_hostname`, `play_hosts`, `ansible_play_hosts`, etc.

**74. What is `hostvars`?**
A dict keyed by inventory hostname containing every variable that host has. Use to query other hosts' facts: `hostvars['db1'].ansible_default_ipv4.address`.

**75. What is `groups`?**
A dict keyed by group name with lists of hosts: `groups['web']`.

**76. What's an action plugin example?**
`template`: copies a rendered Jinja2 file. Runs partly on controller (rendering) and partly on managed node (copying).

**77. What is `ansible-doc`?**
CLI to view module/plugin documentation: `ansible-doc apt`, `ansible-doc -l`, `ansible-doc -t connection ssh`.

**78. How does fact gathering interact with caching?**
With `fact_caching` set, facts from a host persist across plays/playbooks until `fact_caching_timeout`. Subsequent plays can run without `setup` and still have facts.

**79. What is `mitogen`?**
A third-party "Mitogen for Ansible" strategy plugin that drastically reduces SSH round-trips. Big perf gains; some compatibility caveats.

**80. What are forks?**
Number of parallel SSH workers. Default 5. Tune in `ansible.cfg` (`forks = 50`) for large fleets.

**81. What does `gather_facts: smart` do?**
Skips re-gathering for hosts whose facts are already in the cache.

**82. What is `ANSIBLE_*` environment override?**
Most `ansible.cfg` options have env equivalents: `ANSIBLE_INVENTORY`, `ANSIBLE_REMOTE_USER`, `ANSIBLE_BECOME=true`.

**83. What is `--syntax-check`?**
Validates playbook YAML and structure without executing.

**84. What is `ansible-lint`?**
A linter for style and best practices (avoid command/shell, naming conventions, no `latest`, FQCN).

**85. What is `ansible-test`?**
Test framework for collection authors — sanity, units, integration tests.

**86. What is Molecule?**
Role-testing framework. Spins up containers/VMs, applies the role, runs `verify` tasks (often with Testinfra), then destroys.

**87. What is `ansible-builder`?**
Builds Execution Environments (container images bundling ansible-core + collections + Python deps + system packages). Standard since AAP 2.

**88. What is `ansible-navigator`?**
Modern TUI/CLI for running playbooks inside Execution Environments. Replaces direct `ansible-playbook` in AAP workflows.

**89. What's AWX vs Tower vs AAP?**
AWX is open source; Tower was the commercial product (legacy name); Ansible Automation Platform (AAP) is the current Red Hat commercial offering — includes automation controller (Tower), private automation hub, EDA controller, etc.

**90. What is Event-Driven Ansible?**
Reacts to events (webhooks, Kafka, Watchdog) and triggers playbooks. Uses `ansible.eda.rulebooks`.

**91. What's a callback plugin?**
Hooks into events (`v2_runner_on_failed`, etc.). Examples: `yaml` (default in 2.x), `json`, `profile_tasks`, `mail`, `slack`.

**92. What's a lookup plugin?**
Looked up at evaluation: `{{ lookup('file', 'secret.txt') }}`, `{{ lookup('env', 'HOME') }}`, `{{ lookup('hashi_vault', 'secret/data/db pwd') }}`.

**93. What's a filter plugin?**
Jinja2 filters applied with `|`: `{{ list | unique | length }}`, `{{ dict | dict2items }}`.

**94. What's a test plugin?**
Used after `is`: `when: var is defined`, `when: x is failed`.

**95. What's `ansible_python_interpreter`?**
Path to Python on the managed node. Set per host/group when distros ship different defaults.

**96. What is the difference between `ansible` (engine) and `ansible-core`?**
`ansible-core` ships only the engine plus a small built-in module set. The `ansible` community package bundles `ansible-core` + many community collections.

**97. Where do collections install?**
`~/.ansible/collections/ansible_collections/<ns>/<name>` by default; configurable via `collections_paths` in `ansible.cfg`.

**98. What is FQCN?**
Fully Qualified Collection Name: `ansible.builtin.copy`, `community.general.docker_container`. Recommended for forward compatibility.

**99. How is task output structured?**
Per host: `changed`, `failed`, `ok`, `msg`, plus module-specific keys. Use callbacks to format.

**100. How do `vars_prompt` work?**
Asks the user interactively at play start. Supports `private: yes` to hide input.

**101. How are Jinja2 expressions evaluated?**
Lazily by default; `set_fact` materializes them. `{{ x }}` at task render time uses values available at that point in the play.

**102. What is `ansible_check_mode`?**
A magic variable; `true` when running with `--check`. Use to skip destructive logic.

**103. What's the cost of high `forks`?**
Memory and CPU on controller + SSH session count to nodes (consider sshd `MaxSessions`/`MaxStartups`).

**104. SSH multiplexing with ControlPersist?**
Reuses TCP connections; massive speedup. Enabled by default in Ansible's SSH args.

**105. Can Ansible manage Windows?**
Yes via WinRM (or PowerShell over SSH). Modules in `ansible.windows`, `community.windows`.

**106. Network device modules?**
Use connection `network_cli`, `httpapi`, or `netconf` with appropriate `ansible_network_os` (e.g., `cisco.ios.ios`).

**107. What's `become_method`?**
How to escalate: `sudo` (default), `su`, `pbrun`, `doas`, `runas` (Windows), `dzdo`.

**108. What's `become_flags`?**
Extra flags passed to the become method, e.g., `become_flags: '-H -S -n'`.

**109. What's the `meta:` module used for?**
`refresh_inventory`, `clear_facts`, `flush_handlers`, `end_play`, `end_host`, `noop`, `reset_connection`.

**110. What's a `ConfigMap`-like primitive in Ansible?**
None natively; combine `template`, `copy`, and `set_fact` with external sources (Vault, lookups). AWX has surveys and credentials.

---

## C. Configuration & Day-to-Day Usage

**111. Minimal inventory file (INI):**
```ini
[web]
web1.example.com
web2.example.com ansible_host=10.0.1.12 ansible_user=ubuntu

[db]
db1.example.com

[all:vars]
ansible_python_interpreter=/usr/bin/python3
```

**112. Minimal inventory (YAML):**
```yaml
all:
  vars:
    ansible_python_interpreter: /usr/bin/python3
  children:
    web:
      hosts:
        web1.example.com: {}
        web2.example.com:
          ansible_host: 10.0.1.12
          ansible_user: ubuntu
    db:
      hosts:
        db1.example.com: {}
```

**113. Run ad-hoc ping?**
`ansible all -i inventory.ini -m ping`

**114. Run a shell command across hosts?**
`ansible web -m command -a "uptime" -i inventory.ini`

**115. Install a package with apt?**
`ansible web -b -m ansible.builtin.apt -a "name=nginx state=present update_cache=yes"`.

**116. Restart a service?**
`ansible web -b -m service -a "name=nginx state=restarted"`

**117. Copy a file?**
`ansible web -b -m copy -a "src=./nginx.conf dest=/etc/nginx/nginx.conf owner=root group=root mode=0644"`

**118. Write a Hello-World playbook:**
```yaml
- name: Hello world
  hosts: all
  gather_facts: false
  tasks:
    - name: Show OS family
      ansible.builtin.debug:
        msg: "Hello from {{ inventory_hostname }} ({{ ansible_facts.os_family | default('unknown') }})"
```

**119. Install + start nginx idempotently:**
```yaml
- name: Web server
  hosts: web
  become: true
  tasks:
    - name: Install nginx
      ansible.builtin.package:
        name: nginx
        state: present
    - name: Ensure nginx running and enabled
      ansible.builtin.service:
        name: nginx
        state: started
        enabled: true
```

**120. Use a handler:**
```yaml
- name: Web
  hosts: web
  become: true
  tasks:
    - name: Render nginx config
      ansible.builtin.template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf
        owner: root
        group: root
        mode: '0644'
      notify: Restart nginx
  handlers:
    - name: Restart nginx
      ansible.builtin.service:
        name: nginx
        state: restarted
```

**121. Loop installing multiple packages:**
```yaml
- name: Install web stack
  ansible.builtin.package:
    name: "{{ item }}"
    state: present
  loop:
    - nginx
    - python3
    - certbot
```

**122. Loop with dictionary list:**
```yaml
- name: Create users
  ansible.builtin.user:
    name: "{{ item.name }}"
    uid: "{{ item.uid }}"
    state: present
  loop:
    - { name: alice, uid: 1101 }
    - { name: bob,   uid: 1102 }
  loop_control:
    label: "{{ item.name }}"
```

**123. Conditional on OS family:**
```yaml
- name: Install on Debian
  ansible.builtin.apt:
    name: nginx
    state: present
  when: ansible_facts.os_family == "Debian"

- name: Install on RedHat
  ansible.builtin.dnf:
    name: nginx
    state: present
  when: ansible_facts.os_family == "RedHat"
```

**124. Use a template:**
`templates/nginx.conf.j2`:
```jinja
user {{ nginx_user | default('www-data') }};
worker_processes {{ ansible_processor_vcpus }};
events { worker_connections {{ worker_connections | default(1024) }}; }
http {
{% for site in sites %}
  server { listen 80; server_name {{ site.host }}; }
{% endfor %}
}
```

Reference:
```yaml
vars:
  sites:
    - { host: a.example.com }
    - { host: b.example.com }
tasks:
  - ansible.builtin.template:
      src: nginx.conf.j2
      dest: /etc/nginx/nginx.conf
```

**125. Register and use task output:**
```yaml
- name: Get uptime
  ansible.builtin.command: uptime
  register: up
  changed_when: false
- ansible.builtin.debug: msg="{{ up.stdout }}"
```

**126. Filter list, get unique:**
`{{ all_ips | unique }}`

**127. Merge dicts:**
`{{ defaults_dict | combine(overrides_dict, recursive=True) }}`

**128. Conditional with multiple criteria:**
`when: ansible_facts.distribution == 'Ubuntu' and ansible_facts.distribution_version is version('22.04', '>=')`

**129. Wait for a port to open:**
```yaml
- ansible.builtin.wait_for:
    host: "{{ ansible_host }}"
    port: 22
    delay: 5
    timeout: 60
    state: started
```

**130. Wait for a string in a file:**
```yaml
- ansible.builtin.wait_for:
    path: /var/log/app.log
    search_regex: "READY"
    timeout: 120
```

**131. Use `block/rescue/always`:**
```yaml
- block:
    - ansible.builtin.command: /bin/false
  rescue:
    - ansible.builtin.debug: msg="Failure handled"
  always:
    - ansible.builtin.debug: msg="Cleanup"
```

**132. Tag tasks:**
```yaml
- name: Install
  ansible.builtin.package: { name: nginx, state: present }
  tags: [install, web]

- name: Configure
  ansible.builtin.template: { src: nginx.conf.j2, dest: /etc/nginx/nginx.conf }
  tags: [config, web]
```
Run: `ansible-playbook play.yml --tags config`.

**133. Use roles in a playbook:**
```yaml
- hosts: web
  become: true
  roles:
    - common
    - { role: nginx, nginx_user: www-data }
```

**134. Use the new role include style:**
```yaml
- hosts: web
  become: true
  tasks:
    - ansible.builtin.import_role: { name: common }
    - ansible.builtin.include_role:
        name: nginx
      vars:
        nginx_user: www-data
```

**135. Install a role from Galaxy:**
`ansible-galaxy role install geerlingguy.nginx -p roles/`

**136. Install collections from a requirements file:**
`requirements.yml`:
```yaml
collections:
  - name: community.general
    version: ">=8.0.0"
  - name: ansible.posix
  - name: kubernetes.core
roles:
  - src: geerlingguy.nginx
    version: 3.1.4
```
`ansible-galaxy install -r requirements.yml`

**137. Use `set_fact`:**
```yaml
- ansible.builtin.set_fact:
    db_dsn: "postgresql://{{ db_user }}:{{ db_pass }}@{{ db_host }}/{{ db_name }}"
```

**138. Asynchronous task (long-running):**
```yaml
- name: Long backup
  ansible.builtin.command: /usr/local/bin/backup.sh
  async: 3600
  poll: 0
  register: backup_job
- name: Wait for completion
  ansible.builtin.async_status:
    jid: "{{ backup_job.ansible_job_id }}"
  register: result
  until: result.finished
  retries: 60
  delay: 60
```

**139. Use `delegate_to` for load balancer:**
```yaml
- name: Drain from LB
  community.general.haproxy:
    state: disabled
    backend: web
    host: "{{ inventory_hostname }}"
  delegate_to: lb1.example.com
```

**140. Run one task on one host:**
```yaml
- name: DB migration
  ansible.builtin.command: /usr/bin/migrate
  run_once: true
  delegate_to: "{{ groups['web'] | first }}"
```

**141. Rolling update with serial:**
```yaml
- hosts: web
  serial: 25%
  max_fail_percentage: 0
  tasks:
    - import_tasks: deploy.yml
```

**142. Conditional include_tasks:**
```yaml
- name: OS-specific tasks
  ansible.builtin.include_tasks: "{{ ansible_facts.os_family | lower }}.yml"
```

**143. Use Vault for a single value:**
`ansible-vault encrypt_string '<PASSWORD_TO_ENCRYPT>' --name 'db_password'`
Then paste output into `group_vars/db/secrets.yml`.

**144. Encrypt an entire file:**
`ansible-vault create secrets.yml`
Edit: `ansible-vault edit secrets.yml`
Rekey: `ansible-vault rekey secrets.yml`

**145. Run playbook with vault password file:**
`ansible-playbook play.yml --vault-password-file ~/.vault_pass`
Where `~/.vault_pass` (mode `0600`) holds the passphrase.

**146. Use multiple vault IDs?**
`ansible-vault encrypt --vault-id prod@~/.vault-prod --vault-id dev@~/.vault-dev`
Pass at runtime with `--vault-id prod@~/.vault-prod`.

**147. Dynamic inventory for AWS EC2?**
`inventory.aws_ec2.yml`:
```yaml
plugin: amazon.aws.aws_ec2
regions: [us-east-1]
keyed_groups:
  - key: tags.Role
    prefix: role
hostnames: [tag:Name]
compose:
  ansible_host: public_ip_address | default(private_ip_address)
```
Use AWS credentials via env vars or AWS profile.

**148. Run only on hosts with a specific tag (AWS):**
`ansible role_web -i inventory.aws_ec2.yml -m ping`.

**149. Use a YAML inventory plugin (constructed)?**
```yaml
plugin: constructed
strict: true
groups:
  high_mem: ansible_memtotal_mb > 30000
keyed_groups:
  - key: ansible_distribution
    prefix: dist
```

**150. Use `lookup` for a file:**
`{{ lookup('file', 'path/to/key.pub') }}`

**151. Lookup an env var:**
`{{ lookup('env', 'DEPLOY_USER') }}`

**152. Lookup HashiCorp Vault:**
`{{ lookup('community.hashi_vault.vault_kv2_get', 'secret/data/db', engine_mount_point='secret').secret.password }}`

**153. Use `template` to render conditionally:**
```yaml
- ansible.builtin.template:
    src: app.conf.j2
    dest: /etc/app.conf
  when: app_enabled | bool
```

**154. Jinja2 filter examples:**
- `{{ x | default('foo') }}`
- `{{ list | join(',') }}`
- `{{ dict | to_nice_yaml }}`
- `{{ '/etc/passwd' | basename }}`
- `{{ ip | ipaddr('host/prefix') }}`
- `{{ secret | b64encode }}`

**155. Jinja2 tests:**
- `when: var is defined`
- `when: pkg is changed`
- `when: result is failed`

**156. Use `until` to retry:**
```yaml
- name: Wait for app endpoint
  ansible.builtin.uri:
    url: http://{{ inventory_hostname }}:8080/health
    status_code: 200
  register: r
  until: r.status == 200
  retries: 12
  delay: 5
```

**157. Use `with_fileglob`:**
```yaml
- name: Copy all certs (placeholders only, see security note)
  ansible.builtin.copy:
    src: "{{ item }}"
    dest: /etc/ssl/certs/
    mode: '0644'
  with_fileglob: "certs/*.crt"
```
Certs should be checked against the project's certificate guidance: validity not expired, RSA ≥2048 / EC ≥P-256, SHA-2+ signature.

**158. Use `with_subelements`:**
```yaml
- name: Add users to groups
  ansible.builtin.user:
    name: "{{ item.0.name }}"
    groups: "{{ item.1 }}"
  with_subelements:
    - "{{ users }}"
    - groups
```

**159. Loop over a dict:**
```yaml
loop: "{{ packages | dict2items }}"
# item.key, item.value
```

**160. Use `vars_files` with sensitive file:**
```yaml
- hosts: web
  vars_files:
    - vars/main.yml
    - vars/secrets.yml   # vault-encrypted
```

**161. Run an Ad-hoc Yum upgrade:**
`ansible db -b -m dnf -a "name=* state=latest"`

**162. Cron module example:**
```yaml
- ansible.builtin.cron:
    name: "Nightly backup"
    minute: "0"
    hour: "2"
    job: "/usr/local/bin/backup.sh"
```

**163. Manage SSH keys:**
```yaml
- name: Authorize deploy key
  ansible.posix.authorized_key:
    user: deploy
    state: present
    key: "{{ lookup('file', 'keys/deploy.pub') }}"
```

**164. Manage `iptables`:**
```yaml
- ansible.builtin.iptables:
    chain: INPUT
    protocol: tcp
    destination_port: 22
    jump: ACCEPT
```

**165. Manage Linux firewalld:**
```yaml
- ansible.posix.firewalld:
    port: 80/tcp
    permanent: true
    immediate: true
    state: enabled
```

**166. Selinux module:**
```yaml
- ansible.posix.selinux:
    policy: targeted
    state: enforcing
```

**167. Manage Docker container:**
```yaml
- community.docker.docker_container:
    name: redis
    image: redis:7-alpine
    state: started
    restart_policy: unless-stopped
    published_ports: ["6379:6379"]
```

**168. Manage K8s objects:**
```yaml
- kubernetes.core.k8s:
    state: present
    src: deploy.yaml
    namespace: apps
```

**169. Use `lineinfile`:**
```yaml
- ansible.builtin.lineinfile:
    path: /etc/sysctl.conf
    regexp: '^net.ipv4.ip_forward'
    line: 'net.ipv4.ip_forward = 1'
```

**170. Use `blockinfile`:**
```yaml
- ansible.builtin.blockinfile:
    path: /etc/hosts
    block: |
      10.0.0.10 db1
      10.0.0.11 db2
    marker: "# {mark} ANSIBLE MANAGED HOSTS"
```

**171. Manage git repos:**
```yaml
- ansible.builtin.git:
    repo: https://github.com/example/app.git
    dest: /opt/app
    version: main
    update: yes
```

**172. Use `unarchive`:**
```yaml
- ansible.builtin.unarchive:
    src: https://releases.example.com/app-1.2.3.tgz
    dest: /opt
    remote_src: yes
```

**173. Use `file` module to create directories:**
```yaml
- ansible.builtin.file:
    path: /opt/app/data
    state: directory
    owner: app
    group: app
    mode: '0750'
```

**174. Use `archive`:**
```yaml
- community.general.archive:
    path: /var/log/app
    dest: /tmp/app-logs.tgz
    format: gz
```

**175. Use `cron_file`:**
```yaml
- ansible.builtin.cron:
    name: "logrotate"
    cron_file: ansible_logrotate
    user: root
    minute: "0"
    hour: "3"
    job: "/usr/sbin/logrotate /etc/logrotate.conf"
```

**176. Show stats per host:**
`ansible-playbook play.yml -v` prints summary; `--stats` shows totals.

**177. Output as JSON:**
`ANSIBLE_STDOUT_CALLBACK=json ansible-playbook play.yml`

**178. Profile task durations:**
`ANSIBLE_CALLBACKS_ENABLED=profile_tasks ansible-playbook play.yml`

**179. Limit run to subset:**
`ansible-playbook play.yml --limit web1.example.com`
or pattern: `--limit 'web:!web3.example.com'`

**180. Start from a specific task:**
`ansible-playbook play.yml --start-at-task "Render nginx config"`

---

## D. Advanced Topics

**181. Write a custom module (Python).**
```python
# library/my_demo.py
#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule

def run():
    m = AnsibleModule(argument_spec=dict(
        name=dict(type='str', required=True),
        state=dict(type='str', default='present', choices=['present','absent'])
    ), supports_check_mode=True)

    changed = False  # detect drift here
    if m.check_mode:
        m.exit_json(changed=changed)

    # ... do work ...
    m.exit_json(changed=changed, name=m.params['name'])

if __name__ == '__main__':
    run()
```

**182. Why support `check_mode` in your module?**
Lets users preview changes safely; integral to compliance and idempotency.

**183. Write a custom filter plugin.**
```python
# filter_plugins/json_path.py
class FilterModule(object):
    def filters(self):
        return {'reverse_str': lambda s: s[::-1]}
```
Use: `{{ "abc" | reverse_str }}`.

**184. Write a custom lookup plugin.**
```python
# lookup_plugins/upper.py
from ansible.plugins.lookup import LookupBase
class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        return [t.upper() for t in terms]
```
Use: `{{ lookup('upper', 'hello') }}`.

**185. Write a custom callback plugin.**
Subclass `ansible.plugins.callback.CallbackBase`, override `v2_runner_on_failed`, etc. Enable in `ansible.cfg`'s `callbacks_enabled`.

**186. Write a custom inventory plugin.**
Subclass `BaseInventoryPlugin`, implement `verify_file`, `parse`. YAML config file selects it via `plugin:` key.

**187. What is Ansible Galaxy NG (private hub)?**
A private repository for collections and roles; uses pulp under the hood. Replaces classic `ansible-galaxy login` flow with token-based auth.

**188. What is Execution Environment (EE)?**
A container image that bundles `ansible-core`, collections, Python deps, and system packages. Reproducible runtime — eliminates "works on my controller" issues.

**189. Build an EE:**
`execution-environment.yml`:
```yaml
version: 3
images:
  base_image:
    name: quay.io/ansible/ansible-runner:latest
dependencies:
  ansible_core:
    package_pip: ansible-core==2.18.*
  galaxy: requirements.yml
  python: requirements.txt
  system: bindep.txt
```
Build: `ansible-builder build -t my-ee:1.0`.

**190. Run a playbook in an EE:**
`ansible-navigator run play.yml --eei my-ee:1.0 --mode stdout`.

**191. What is `ansible-runner`?**
Python library/CLI to run Ansible programmatically inside EEs. AWX/AAP uses it under the hood.

**192. How does AAP execute jobs?**
A job template + EE + credentials + inventory is dispatched to an execution node (a host that runs `ansible-runner` against the EE).

**193. What is `EDA` (Event-Driven Ansible)?**
Rulebooks define sources (Kafka, webhooks), conditions, and actions (run playbook). Useful for automated remediation.

**194. Sample rulebook:**
```yaml
- name: Watch CPU alerts
  hosts: all
  sources:
    - ansible.eda.webhook:
        host: 0.0.0.0
        port: 5000
  rules:
    - name: Restart on high CPU
      condition: event.cpu > 90
      action:
        run_playbook:
          name: restart.yml
```

**195. What's the difference between `import_*` and `include_*`?**

| Feature | import_* | include_* |
|---------|---------|-----------|
| When parsed | Play start (static) | At runtime (dynamic) |
| Loop support | No | Yes |
| Conditional applies to | Each child task | The include statement |
| Tags applied to | Each child task | The include statement |

**196. Use `import_playbook`:**
```yaml
- import_playbook: base.yml
- import_playbook: web.yml
- import_playbook: db.yml
  when: deploy_db | bool      # NOT supported on import; use include_playbook for conditions
```

**197. Use a strategy plugin:**
```yaml
- hosts: all
  strategy: free
  tasks: ...
```
`free` lets each host advance independently.

**198. Pin module versions per environment?**
Use `requirements.yml` with `version:` per collection, and an EE per environment.

**199. Test a role with Molecule:**
```yaml
# molecule/default/molecule.yml
driver: { name: docker }
platforms:
  - name: ubuntu22
    image: geerlingguy/docker-ubuntu2204-ansible
    pre_build_image: true
provisioner: { name: ansible }
verifier: { name: ansible }
```
`molecule init role myrole && molecule test`.

**200. Why use `pre_build_image: true` in Molecule?**
Uses a pre-built image with `systemd` working — faster, more reliable than installing on top of stock `ubuntu:22.04`.

**201. Run Ansible from Python?**
Use `ansible-runner`:
```python
import ansible_runner
r = ansible_runner.run(private_data_dir='./demo', playbook='play.yml')
print(r.status, r.rc)
```

**202. Schedule playbooks with AWX/AAP?**
Define Job Templates and Schedules; surveys collect input. RBAC determines who can launch.

**203. Workflow templates in AAP?**
Chain multiple jobs with success/failure branches and approval gates.

**204. What is a `Survey` in AWX?**
A web form attached to a Job Template — captures `extra_vars` from operators.

**205. Use Ansible with Kubernetes Operators (Operator SDK Ansible mode)?**
Operator-SDK scaffolds an operator whose reconcile logic is an Ansible Role. Watches CRDs and runs roles on change.

**206. Use of `delegate_facts`?**
```yaml
- ansible.builtin.set_fact:
    db_endpoint: "{{ inventory_hostname }}"
  delegate_to: db1
  delegate_facts: true
```
Now `hostvars['db1'].db_endpoint` is set.

**207. What's `add_host`?**
Dynamically adds a host to an in-memory inventory mid-play (useful when you provision a new VM and want to act on it immediately).

**208. What's `group_by`?**
Dynamically creates groups from host facts mid-play:
```yaml
- ansible.builtin.group_by:
    key: "os_{{ ansible_facts.os_family | lower }}"
```

**209. Use `ansible.builtin.assert`:**
```yaml
- ansible.builtin.assert:
    that:
      - ansible_facts.memtotal_mb >= 2048
      - ansible_facts.architecture == 'x86_64'
    fail_msg: "Host doesn't meet requirements"
```

**210. Use `meta: reset_connection`:**
After modifying a user's groups (e.g., adding to docker), reconnect to pick up new groups:
```yaml
- ansible.builtin.user: { name: deploy, groups: docker, append: yes }
- ansible.builtin.meta: reset_connection
```

**211. Concurrency with `async`?**
Use `async` for parallelism beyond `forks` — Ansible polls status periodically.

**212. Ansible + Vault HCP integration?**
Use `community.hashi_vault` collection: configure `VAULT_ADDR`, `VAULT_TOKEN` (or AppRole), then lookup KV secrets.

**213. What is `ANSIBLE_KEEP_REMOTE_FILES=1`?**
Persists the module's temp dir on the remote node — useful for debugging modules.

**214. What is `ANSIBLE_DEBUG`?**
Prints verbose internal debug logs. Use with `-vvvv` for very detailed SSH/module output.

**215. Custom strategy plugin example?**
Rarely needed. Could implement, e.g., a "fail-fast and abort other hosts" behavior.

**216. Caching facts in Redis?**
```ini
[defaults]
fact_caching = redis
fact_caching_connection = localhost:6379:0
fact_caching_timeout = 86400
```

**217. Encrypted variables with environment-specific vaults?**
Multiple vault ids; tag variables with `!vault | $ANSIBLE_VAULT;1.2;AES256;prod\n...`.

**218. Combining Ansible with Terraform?**
Terraform provisions infra, then triggers Ansible: pass IPs via Terraform output to dynamic inventory or generate inventory with `local_file`.

**219. Use `ansible.builtin.uri` for an API check:**
```yaml
- ansible.builtin.uri:
    url: https://api.example.com/health
    method: GET
    return_content: yes
    validate_certs: yes
    status_code: [200, 204]
  register: api_health
```
Note: leave `validate_certs: yes` unless interacting with a trusted internal endpoint with a non-public CA (then install the CA, don't disable validation).

**220. Templating with macros:**
```jinja
{% macro user_block(u) %}
user {{ u.name }} {{ u.uid }};
{%- endmacro %}

{% for u in users %}{{ user_block(u) }}{% endfor %}
```

**221. Use Jinja2 `do` extension?**
Already enabled in Ansible. Use sparingly; prefer `set_fact` for mutation.

**222. Test a role's idempotency in Molecule?**
Run twice and confirm second run is `changed=0`. `molecule converge && molecule idempotence`.

**223. Test a role against multiple distros?**
Add multiple `platforms:` to `molecule.yml` and run `molecule test`.

**224. Lint everything in CI?**
`ansible-lint -p`, `yamllint .`, `ansible-playbook play.yml --syntax-check`.

**225. Custom inventory plugin example?**
Subclass `BaseInventoryPlugin`, implement `verify_file` (config detection), `parse` (populate hosts/groups). Document `DOCUMENTATION` block for `ansible-doc`.

**226. Use `ansible.builtin.expect` for interactive commands?**
```yaml
- ansible.builtin.expect:
    command: /usr/bin/setup
    responses:
      "Password:": "{{ admin_password }}"
    no_log: true
```
`no_log: true` prevents secrets from leaking to logs.

**227. Use `no_log` more broadly?**
Any task: `no_log: true` to suppress output. Critical for secrets.

**228. Use environment variables per task:**
```yaml
- ansible.builtin.command: ./build.sh
  environment:
    BUILD_ENV: prod
    PATH: /opt/tools:{{ ansible_env.PATH }}
```

**229. Use `vars:` to scope:**
```yaml
- name: Deploy with custom value
  ansible.builtin.import_role: { name: web }
  vars:
    nginx_workers: 4
```

**230. Handle hosts with no Python?**
`raw` module: `ansible <host> -m raw -a "apt-get install -y python3"`. Then run normal modules.

**231. Handle reboot inside a play:**
```yaml
- ansible.builtin.reboot:
    msg: "Kernel upgrade"
    reboot_timeout: 600
    pre_reboot_delay: 10
```

**232. Manage Linux kernel parameters:**
```yaml
- ansible.posix.sysctl:
    name: vm.swappiness
    value: '10'
    state: present
    reload: true
```

**233. Use `ansible.builtin.cron` with env vars:**
```yaml
- ansible.builtin.cron:
    name: PATH
    env: yes
    value: /usr/local/bin:/usr/bin:/bin
```

**234. Use `ansible.builtin.lvol` and `filesystem`:**
```yaml
- community.general.lvol:
    vg: vg0
    lv: data
    size: 100g
- community.general.filesystem:
    fstype: xfs
    dev: /dev/vg0/data
- ansible.posix.mount:
    path: /data
    src: /dev/vg0/data
    fstype: xfs
    state: mounted
```

**235. Use `ansible.builtin.systemd`:**
```yaml
- ansible.builtin.systemd:
    name: chronyd
    state: started
    enabled: yes
    daemon_reload: yes
```

**236. Use `loop_control`:**
- `label`: friendly per-item label.
- `pause`: seconds between iterations.
- `index_var`: capture iteration index.

```yaml
loop: "{{ users }}"
loop_control:
  label: "{{ item.name }}"
  index_var: idx
```

**237. Use `community.general.ini_file`:**
```yaml
- community.general.ini_file:
    path: /etc/myapp.conf
    section: db
    option: host
    value: db1
```

**238. Implement zero-downtime deploys?**
- Drain from LB (`delegate_to: lb`)
- Update host
- Health-check
- Re-add to LB
- Repeat with `serial:`

**239. Use `max_fail_percentage`?**
Abort the play if more than X% of hosts fail in a serial batch.

**240. Use `any_errors_fatal`?**
If any host fails, the entire play aborts (useful for orchestrated changes that must be all-or-nothing).

---

## E. Security, Performance & Best Practices

**241. Secret management best practices?**
1) Never commit plaintext secrets.
2) Use Vault (encrypted file or string) for static secrets.
3) Prefer external secret managers (HashiCorp Vault, AWS SM) via lookup plugins for rotated secrets.
4) Use `no_log: true` on any task touching secrets.
5) Restrict access to `~/.vault_pass` (mode `0600`); never check in.
6) Avoid passing secrets via `-e` on shared CI machines.

**242. Where to store the vault password?**
- Local file `~/.vault_pass` (mode 600), never committed.
- CI: encrypted CI secret env var, read by a `vault_password_file` script.
- AAP: built-in credential store backed by an HSM/cloud KMS.

**243. Why prefer `command`/`shell` only as last resort?**
They aren't idempotent and break check mode. Use a proper module when available.

**244. Why use `ansible.builtin` FQCN?**
Future-proof: collections may shadow builtins; explicit FQCN avoids ambiguity.

**245. Why prefer roles over giant playbooks?**
Reusability, testability (Molecule), scoped variables, clearer ownership.

**246. SSH best practice?**
- ControlPersist (default on)
- Pipelining enabled (requires `requiretty=no` in sudoers)
- ED25519 or RSA-3072+ keys
- Disable password auth on managed nodes
- Use SSH agent forwarding sparingly (security risk)

**247. Performance: forks tuning?**
Start with 25-50; profile with `profile_tasks`. Beware controller CPU/memory and managed node `sshd MaxSessions`.

**248. Performance: gather_facts?**
Use `gather_facts: false` if not needed; or `gather_subset: !all,!min,network` to skip costly facts; cache to Redis.

**249. Performance: avoid `set_fact` in tight loops?**
Each `set_fact` is a roundtrip. Build a list once, then iterate.

**250. Mitogen for big speedups?**
Drop-in strategy plugin replacing default SSH. Reduces network round-trips significantly. Test compatibility with your modules.

**251. Idempotency in `command`/`shell`?**
Add `creates:` / `removes:` to skip when target exists/doesn't:
```yaml
- ansible.builtin.command: /usr/bin/build.sh
  args:
    creates: /opt/app/.built
```

**252. Validating templates before deploy?**
Use `validate:` on `template`/`copy` for files like sshd/sudoers/nginx:
```yaml
- ansible.builtin.template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    validate: 'nginx -t -c %s'
```

**253. Lint and test in CI?**
- `ansible-lint`, `yamllint`
- `ansible-playbook --syntax-check`
- `molecule test` per role
- `ansible-test` for collections

**254. Avoid `latest` package state?**
Reproducibility — pin versions, especially for upgrades.

**255. Use `become_user: root` only when needed?**
Apply `become` per task, not per play, when feasible.

**256. Centralize credentials?**
Use AAP credential vault, HashiCorp Vault, or external KMS. Avoid scattered `.vault_pass` files.

**257. Audit logging?**
AAP records every job and change. For OSS, push callback output to ELK or CloudWatch.

**258. Naming convention?**
Use clear `name:` on every task; tags use kebab-case; vars snake_case; never re-use core variable names.

**259. Manage drift?**
Periodic compliance runs in `--check --diff`; gate on changes via CI.

**260. Use immutable Execution Environments?**
Pin EE digest in CI for reproducibility; build SBOM; scan with Trivy.

**261. Don't ship images with secrets?**
Inject secrets at runtime via env vars or mounted files; never `ENV PASS=` in EE.

**262. Handler dedup?**
Multiple notifies of the same handler still run only once per play.

**263. Avoid hot loops?**
`loop` of 10k items will be slow; redesign to batch (e.g., `community.general.batch`).

**264. Output redaction?**
`no_log: true`, and don't include secrets in error messages.

**265. Don't disable TLS validation?**
`validate_certs: yes` (default). For internal CAs, install the CA on the managed node and reference it (`ca_path: /etc/ssl/certs/my_ca.crt`).

**266. Use `ansible-lint` rules?**
Examples: `no-changed-when`, `name[casing]`, `risky-shell-pipe`, `fqcn[action-core]`, `package-latest`.

**267. Limit privilege escalation?**
Configure sudoers narrowly: allow `deploy` to run only required commands without password.

**268. Test new collections in isolation?**
Use a dedicated EE; pin version; run integration tests via `ansible-test`.

**269. Avoid `ANSIBLE_HOST_KEY_CHECKING=False` in production?**
Disabling host-key checking exposes you to MITM. Pre-populate `known_hosts` from a trusted source instead.

**270. Use `ssh-keyscan` properly?**
`ssh-keyscan -t ed25519,rsa <host> >> ~/.ssh/known_hosts`. Only trust output from a secure provisioning channel.

---

## F. Troubleshooting & Debugging

**271. Tasks all skip on a host — likely cause?**
A `when:` condition referencing an undefined variable or failed gather_facts. Run with `-vv` to see condition evaluation.

**272. Variable not defined error?**
Check precedence; `{{ var | default('') }}` to avoid hard failures; ensure inventory/file paths are correct.

**273. SSH connection fails — diagnostics?**
`ansible <host> -m ping -vvvv` shows the SSH command. Try direct SSH; check `known_hosts`, key permissions, sshd config, port, firewall.

**274. Module returns "MODULE FAILURE"?**
Often Python missing on remote, or Python version mismatch. Set `ansible_python_interpreter`. Run with `-vvv` to see remote stderr.

**275. Permission denied — privilege escalation?**
Confirm `become: true`; ensure `become_method` works (`sudo -n true`); set `become_password` via Vault if `NOPASSWD` not configured.

**276. Slow playbook — how to profile?**
`ANSIBLE_CALLBACKS_ENABLED=profile_tasks ansible-playbook play.yml` outputs per-task timings.

**277. Idempotency report shows lots of changes?**
Often `command`/`shell` reporting changed every time. Add `changed_when:`/`creates:` or switch to a proper module.

**278. Handler not firing?**
Check task is actually changing state; handler name matches `notify`; not skipped by `--tags`.

**279. Vault decryption fails?**
Wrong password file, mismatched vault-id, file not actually vault-encrypted (check `head -1 file`).

**280. Inventory plugin returning nothing?**
`ansible-inventory --graph -i inv.yml`. Check plugin name, env credentials, region, filters.

**281. Templating returns empty?**
Variable not defined or scope. Add `{{ var | default('UNSET') }}` and check.

**282. Async task stuck?**
`async_status` keeps polling — check remote `/tmp/ansible-runner-async-*` files; might need bigger `timeout`.

**283. Unable to install packages — slow apt?**
DNS issue or mirror down. Try `update_cache: yes`, `cache_valid_time: 3600`, or fall back to a known-good mirror.

**284. SELinux blocks something module needs?**
Use `ansible.posix.seboolean`/`selinux` to allow it explicitly; don't `setenforce 0`.

**285. Connection plugin reset to default?**
Verify per-host `ansible_connection`; environment isn't overriding (`ANSIBLE_CONNECTION`).

**286. Playbook hangs at gather_facts?**
Firewall blocking SSH, slow DNS, or fact subsystem fetching from broken module. `gather_subset: '!all,!min,network'` to narrow.

**287. Random task failures with `Connection reset`?**
sshd `MaxStartups` limiting. Reduce `forks`, raise sshd limits, enable pipelining.

**288. Vault file edits corrupt YAML?**
Always edit with `ansible-vault edit`, not `cat | vim`. View with `ansible-vault view`.

**289. `lineinfile` doesn't change because regex doesn't match?**
Use `backrefs: true` to allow regex back-references; ensure regex escapes special chars.

**290. Different Python interpreter found per host?**
Pin per group: `ansible_python_interpreter: /usr/bin/python3`. Suppress warning with `interpreter_python = auto_silent` in `ansible.cfg`.

**291. Cron job from `cron` module fires twice?**
You likely created similar entries with different names; remove old ones with `state: absent` and a matching `name:`.

**292. Module reports changed every run?**
Some modules (e.g., `command`) always report changed. Use `changed_when: false` for read-only commands.

**293. Network module unsupported facts?**
Use `gather_facts: false` and explicit `ansible_facts` calls; some network OSes need vendor-specific facts modules.

**294. EE missing a collection?**
Rebuild with updated `execution-environment.yml` requirements; verify with `ansible-galaxy collection list` inside the EE.

**295. Connection plugin can't find binary on PATH?**
Some connection plugins require an executable (e.g., `kubectl`, `docker`). Install in the EE.

**296. Output truncated for large debug?**
`callback_format_pretty`: use `-vv`. For huge output, dump to file: `register: r` then `copy: content="{{ r | to_nice_json }}" dest=/tmp/out.json delegate_to=localhost`.

**297. Permissions wrong after file copy?**
Set `owner`, `group`, `mode` explicitly. `preserve: true` to copy mtime/mode from source.

**298. Slow `apt` because cache stale?**
Use `update_cache: yes`, `cache_valid_time: 600` to update intelligently.

**299. `community.general.docker_*` doesn't connect?**
Ensure `docker` SDK installed in EE; user has access to Docker socket; on macOS, use `docker context` or run on Linux.

**300. Suspect a flaky inventory cache?**
`-i inventory.yml --flush-cache`.

---

## G. Real-World Scenario-Based Questions

**301. Roll out a security patch to 1000 hosts without downtime.**
- Inventory grouped by role
- `serial: 5%`
- `pre_tasks`: remove from LB
- `tasks`: apply patch, reboot, wait for SSH
- `post_tasks`: smoke test, re-add to LB
- `max_fail_percentage: 0`
- Run from AAP with notifications

**302. Configure a 3-tier web app from scratch.**
Roles: `common`, `nginx`, `python_app`, `postgres`. Use `group_vars/{web,app,db}.yml`. Vault stores DB passwords. Playbook orchestrates: db → app (migrate) → web (config).

**303. Decommission a node safely.**
Drain from LB, stop services, backup data to S3, remove from monitoring, remove from inventory, terminate VM (Terraform), notify owners.

**304. Migrate from Vault file secrets to HashiCorp Vault.**
- Stand up Vault HA cluster
- Populate KV with secrets
- Replace `vars/secrets.yml` references with `lookup('community.hashi_vault.vault_kv2_get', ...)`
- Vault auth via AppRole or AWS IAM
- Add tests to fail if lookup returns null
- Rotate any previously-leaked Vault file passwords

**305. Make plays runnable from local dev and CI uniformly.**
Use EE built in CI and downloadable locally; standardize on `ansible-navigator`; checked-in `ansible.cfg`, `collections/requirements.yml`, `roles/requirements.yml`.

**306. Detect & remediate drift continuously.**
Schedule check-mode run hourly (`--check --diff`) per env; alert on diffs; manual approval to apply.

**307. Move ad-hoc remediation to Event-Driven Ansible.**
Define webhook/Kafka source receiving Prometheus alerts; rulebook maps `alertname` → remediation playbook (e.g., disk_full → cleanup play).

**308. AWS EC2 inventory grows daily — keep playbooks fast.**
- Use `compose:` and `keyed_groups:` to pre-classify
- Limit playbook to relevant groups
- Cache inventory (`cache: true`, `cache_plugin: jsonfile`)
- Use `gather_subset: min` and Redis fact caching

**309. Handle mixed Linux + Windows + network gear.**
Split playbooks by `connection`/OS; pin `ansible_connection` per host group; use vendor collections (`cisco.ios`, `arista.eos`, `juniper.junos`).

**310. Run Ansible across regions with low latency to control node?**
Deploy execution nodes per region (AAP) or run a controller per region; route inventory per region; use mesh networking.

**311. Implement compliance scans?**
Use OpenSCAP via `ansible.posix.openscap` (or community modules); run weekly; ship results to compliance dashboard.

**312. Develop a custom module for a proprietary appliance.**
Use `library/` first, then promote to a collection. Implement REST calls; return diff in `result['diff']`; support check mode.

**313. Pipeline secrets through CI without leaking?**
CI injects `VAULT_PASSWORD_FILE` from secret store at job start; `no_log: true` on tasks; rotate on suspected leak.

**314. Replace shell scripts with Ansible?**
Audit scripts; create roles; ensure idempotency with `creates`/`changed_when`; migrate piecemeal; gate adoption with parallel runs comparing outcomes.

**315. Implement multi-stage deployments (dev/stage/prod)?**
Per-env inventory + `group_vars/<env>.yml` overrides. CI runs same playbook with `-i inventories/<env>` and Vault for that env.

**316. Add an approval step in AAP workflow?**
Workflow node `approval` pauses until a privileged user approves. Wraps risky downstream nodes.

**317. Migrate from Ansible Tower to AAP 2?**
Backup Tower DB; export job templates with `awx-manage`; install AAP 2; import objects; rebuild EEs from your existing requirements; reattach external auth (LDAP/SAML).

**318. Run only changed roles in PR validation?**
Compare changed files in PR; map to role names; skip Molecule tests for unchanged roles.

**319. Avoid double rollout on Argo CD + Ansible managing the same K8s objects.**
Pick one source of truth: Argo for K8s manifests; Ansible only for cluster prerequisites (storage, secrets, RBAC) — never both managing the same resource.

**320. Backup/restore strategy for inventory and secrets?**
Git for inventory; Vault-managed encrypted files committed; key backups in offline encrypted storage (printed paper backup + secure vault); test restore quarterly.

---

## H. Comparison Tables

### Ansible vs Puppet vs Chef vs SaltStack

| Aspect | Ansible | Puppet | Chef | SaltStack |
|--------|---------|--------|------|-----------|
| Language | YAML + Jinja2 | DSL | Ruby DSL | YAML / Python |
| Agent? | Agentless | Agent | Agent | Agent or salt-ssh |
| Push/Pull | Push (or ansible-pull) | Pull | Pull | Push |
| Learning curve | Low | Medium | High | Medium |
| Community | Very large | Large | Medium | Medium |
| Best for | Ad-hoc + config + orchestration | Long-term server lifecycle | Complex prescriptive infra | Event-driven, high speed |

### Roles vs Collections

| Aspect | Role | Collection |
|--------|------|------------|
| Scope | Single configuration unit | Bundle of roles, modules, plugins |
| Distribution | Galaxy or Git | Galaxy / Automation Hub (OCI in 2.13+) |
| Versioning | `meta/main.yml` + Git tag | `galaxy.yml` |
| Namespacing | None | `namespace.collection` |

### Vault Options

| Method | When |
|--------|------|
| `ansible-vault encrypt_string` | Single value, in plain YAML |
| `ansible-vault create file.yml` | Entire vars file |
| `hashi_vault` lookup | Centralized secret manager |
| AAP credentials | Managed, audited, RBAC-controlled |

### Inventory Sources

| Source | Use |
|--------|-----|
| Static INI/YAML | Small, stable infra |
| AWS/Azure/GCP plugins | Cloud-native |
| `kubernetes.core.k8s` | K8s pods/services |
| Constructed | Group/keying overlays |
| Script | Legacy custom systems |
| AAP smart inventory | Filtered subsets from CMDB |

### import_* vs include_*

| Behavior | import_* (static) | include_* (dynamic) |
|----------|------------------|---------------------|
| Parsed at | Play start | Runtime |
| Variables | Resolved at parse | Resolved at execution |
| Loops | Not allowed | Allowed |
| Tags applied to | Each task | Statement |
| When applied to | Each task | Statement |

---

## I. Hands-On Labs

Prereqs: Ansible-core installed; two or three local VMs (Multipass / Vagrant) reachable via SSH.

### Lab 1 — Bootstrap Inventory & Ping

```ini
# inventory.ini
[web]
web1 ansible_host=192.168.64.10
web2 ansible_host=192.168.64.11

[all:vars]
ansible_user=ubuntu
ansible_ssh_private_key_file=~/.ssh/id_ed25519
```

```bash
ansible all -i inventory.ini -m ping
```

Expected: `pong` from each host.

---

### Lab 2 — Install + Configure Nginx

`playbooks/nginx.yml`:
```yaml
- name: Provision Nginx
  hosts: web
  become: true
  vars:
    server_name: example.local
  tasks:
    - ansible.builtin.apt:
        name: nginx
        state: present
        update_cache: yes
    - ansible.builtin.template:
        src: templates/site.conf.j2
        dest: /etc/nginx/sites-available/{{ server_name }}.conf
        validate: 'nginx -t -c %s'
      notify: Reload nginx
    - ansible.builtin.file:
        src: /etc/nginx/sites-available/{{ server_name }}.conf
        dest: /etc/nginx/sites-enabled/{{ server_name }}.conf
        state: link
      notify: Reload nginx
    - ansible.builtin.service:
        name: nginx
        state: started
        enabled: yes
  handlers:
    - name: Reload nginx
      ansible.builtin.service:
        name: nginx
        state: reloaded
```

`templates/site.conf.j2`:
```
server { listen 80; server_name {{ server_name }}; root /var/www/html; }
```

Run twice; confirm second run shows `changed=0`.

---

### Lab 3 — Build a Role

```bash
ansible-galaxy role init roles/postgres
```

Fill `roles/postgres/tasks/main.yml`, `defaults/main.yml`. Use it from a playbook:

```yaml
- hosts: db
  become: true
  roles:
    - role: postgres
      vars:
        postgres_version: "16"
```

Add Molecule scenario and run `molecule test`.

---

### Lab 4 — Vault Workflow

```bash
echo "<STRONG_VAULT_PASSWORD>" > ~/.vault_pass
chmod 600 ~/.vault_pass

ansible-vault create group_vars/db/secrets.yml
# add:
# db_password: <STRONG_DB_PASSWORD>

ansible-vault encrypt_string '<API_KEY>' --name 'api_key' \
  --vault-password-file ~/.vault_pass
# paste into group_vars/web/secrets.yml

ansible-playbook playbooks/site.yml \
  --vault-password-file ~/.vault_pass
```

---

### Lab 5 — Dynamic Inventory for AWS EC2

`inventory/aws.yml` (see Q147). Tag your EC2 instances with `Role=web` or `Role=db`. Configure AWS creds via `aws configure sso` or environment variables, then:

```bash
ansible-inventory -i inventory/aws.yml --graph
ansible role_web -i inventory/aws.yml -m ping
```

---

### Lab 6 — Multi-Tier Web App

Roles: `common`, `db`, `app`, `web`.

`site.yml`:
```yaml
- import_playbook: db.yml
- import_playbook: app.yml
- import_playbook: web.yml
```

Validate end-to-end with `curl http://<web-vip>/`.

---

### Lab 7 — Rolling Deploy with Drain

```yaml
- name: Rolling deploy
  hosts: web
  become: true
  serial: 1
  pre_tasks:
    - name: Drain from LB
      community.general.haproxy:
        state: disabled
        backend: web
        host: "{{ inventory_hostname }}"
      delegate_to: lb1
  tasks:
    - import_role: { name: app_deploy }
    - name: Smoke test
      ansible.builtin.uri:
        url: http://{{ inventory_hostname }}:8080/health
        status_code: 200
      register: r
      until: r.status == 200
      retries: 10
      delay: 3
  post_tasks:
    - name: Add back to LB
      community.general.haproxy:
        state: enabled
        backend: web
        host: "{{ inventory_hostname }}"
      delegate_to: lb1
```

---

### Lab 8 — Custom Module

Create `library/my_demo.py` (Lab 181). Use in a playbook:

```yaml
- hosts: localhost
  gather_facts: false
  tasks:
    - my_demo:
        name: hello
        state: present
      register: out
    - ansible.builtin.debug: var=out
```

---

### Lab 9 — Molecule for Role Testing

```bash
pipx install molecule molecule-plugins[docker]
cd roles/nginx
molecule init scenario default
molecule test
```

Read the generated `molecule/default/`; add an Ansible verifier:

```yaml
# molecule/default/verify.yml
- hosts: all
  tasks:
    - ansible.builtin.uri:
        url: http://localhost
        status_code: 200
```

---

### Lab 10 — Build & Run an EE

`execution-environment.yml`:
```yaml
version: 3
images:
  base_image:
    name: quay.io/ansible/ansible-runner:latest
dependencies:
  ansible_core:
    package_pip: ansible-core==2.18.*
  galaxy: requirements.yml
  python: requirements.txt
```

```bash
ansible-builder build -t my-ee:1.0
ansible-navigator run playbooks/site.yml --eei my-ee:1.0 --mode stdout
```

---

## J. Mock Interview Sets

60 minutes / 15 questions each.

### Mock Set 1 — Foundations

1. What is Ansible and how does it connect?
2. Difference between playbook, play, task, module, role, collection.
3. INI vs YAML inventory.
4. What is idempotency and how do modules achieve it?
5. Explain `when`, `loop`, `register`, `notify`, `handler`.
6. Vault: create, edit, view, rekey commands.
7. Variable precedence top-5 sources.
8. group_vars and host_vars layout.
9. `command` vs `shell`; when is each acceptable?
10. Tags: how to run only some tasks.
11. Roles directory layout; what's in `defaults` vs `vars`?
12. `delegate_to` example.
13. `become` and `become_user`.
14. Difference between `include_tasks` and `import_tasks`.
15. How to debug a failing play (`-vv`, `--check`, `--diff`, etc.).

### Mock Set 2 — Patterns & Advanced

1. Write a rolling-update play with drain/return-to-LB.
2. Custom module skeleton (Python).
3. Custom filter plugin.
4. Dynamic inventory plugin for AWS.
5. Fact caching tradeoffs.
6. `async` and `async_status` example.
7. Performance tuning: forks, pipelining, gather_subset.
8. Mitogen — what it does, risks.
9. Build an Execution Environment from scratch.
10. EDA rulebook example.
11. AAP credentials vs Vault encrypted strings.
12. Molecule scenario for a role across two distros.
13. Strategy plugins; when to use `free`.
14. `block/rescue/always` pattern.
15. Custom callback plugin idea.

### Mock Set 3 — Production Scenarios

1. Roll out a kernel patch to 500 hosts with PDB-like safety.
2. Detect drift continuously without applying changes.
3. Migrate secrets from Vault file to HashiCorp Vault.
4. Run Ansible from a CI pipeline securely.
5. Multi-stage env strategy (dev/stage/prod).
6. Mixed Linux/Windows fleet patterns.
7. Network device automation playbook structure.
8. Replace 400 lines of shell with Ansible — approach.
9. Cross-region execution architecture in AAP.
10. Build approval workflows in AAP.
11. EDA pattern for auto-remediation on Prometheus alerts.
12. Audit who ran what when.
13. RBAC strategy in AAP for tenants.
14. Choose between collections, roles, ad-hoc commands.
15. End-to-end CI: lint, syntax, molecule, build EE, deploy via AAP.

---

## K. Cheat Sheet

### CLI Essentials

```bash
ansible --version
ansible all -i inventory.ini -m ping
ansible web -m setup -i inventory.ini
ansible all -b -m apt -a "name=curl state=present" -i inventory.ini
ansible-playbook play.yml -i inventory.ini --diff --check
ansible-playbook play.yml --tags "config" --skip-tags "destroy"
ansible-playbook play.yml --limit web1.example.com
ansible-inventory -i inventory.yml --graph
ansible-doc apt
ansible-doc -l | grep cron
```

### Vault

```bash
ansible-vault create  secrets.yml
ansible-vault edit    secrets.yml
ansible-vault view    secrets.yml
ansible-vault rekey   secrets.yml
ansible-vault encrypt secrets.yml
ansible-vault decrypt secrets.yml
ansible-vault encrypt_string '<value>' --name 'mykey'
ansible-playbook play.yml --vault-password-file ~/.vault_pass
ansible-playbook play.yml --vault-id prod@~/.vault-prod --vault-id dev@~/.vault-dev
```

### Galaxy

```bash
ansible-galaxy collection install community.general
ansible-galaxy collection install -r requirements.yml -p ./collections
ansible-galaxy role install geerlingguy.nginx -p ./roles
ansible-galaxy collection list
```

### Lint & Test

```bash
ansible-lint -p
ansible-playbook play.yml --syntax-check
yamllint .
molecule test
ansible-test sanity
```

### Playbook Patterns

```yaml
# Skeleton
- name: <Play name>
  hosts: <pattern>
  become: true
  gather_facts: true
  serial: "25%"
  max_fail_percentage: 0
  vars_files: [vars/main.yml, vars/secrets.yml]
  pre_tasks: []
  tasks: []
  post_tasks: []
  handlers: []
```

### Useful Filters & Tests

```jinja
{{ var | default('') }}
{{ list | unique | sort | join(',') }}
{{ dict | dict2items }}                  {# [{key:, value:}] #}
{{ items | items2dict(key_name='k') }}
{{ 'foo bar' | split | last }}
{{ ip | ipaddr('host/prefix') }}
{{ pwd | password_hash('sha512') }}      {# system password hash #}
{{ '/etc/passwd' | basename }}
{{ var | b64encode }}
{{ json | from_json }}
{{ obj | to_nice_yaml }}
{% if x is defined %}{% endif %}
{% if r is changed %}{% endif %}
```

### Common Modules (FQCN)

```
ansible.builtin.{ ping, command, shell, raw, copy, file, template,
                  service, systemd, cron, lineinfile, blockinfile,
                  user, group, get_url, uri, set_fact, debug, assert,
                  wait_for, apt, dnf, yum, package, pip, git, unarchive }
ansible.posix.{   sysctl, mount, firewalld, selinux, authorized_key }
community.general.{ ini_file, htpasswd, archive, haproxy, docker_container, datadog }
community.docker.{ docker_container, docker_image, docker_network, docker_compose }
kubernetes.core.{  k8s, helm, helm_repository }
community.hashi_vault.vault_kv2_get
```

### ansible.cfg Starter

```ini
[defaults]
inventory = ./inventory.ini
roles_path = ./roles
collections_paths = ./collections
host_key_checking = True
retry_files_enabled = False
forks = 25
gathering = smart
fact_caching = jsonfile
fact_caching_connection = ~/.ansible/cache
fact_caching_timeout = 7200
stdout_callback = yaml
callbacks_enabled = profile_tasks, timer
interpreter_python = auto_silent

[ssh_connection]
pipelining = True
ssh_args = -o ControlMaster=auto -o ControlPersist=60s
```

---

## L. Curated Resources

### Official

- Ansible docs — https://docs.ansible.com
- Module index — https://docs.ansible.com/ansible/latest/collections/index_module.html
- Galaxy — https://galaxy.ansible.com
- AAP — https://www.redhat.com/en/technologies/management/ansible
- EDA — https://www.redhat.com/en/technologies/management/ansible/event-driven

### Books

- *Ansible for DevOps* — Jeff Geerling
- *Ansible: Up & Running* — Lorin Hochstein & René Moser
- *Mastering Ansible* — James Freeman & Jesse Keating
- *Ansible Automation Cookbook* — Lokesh Krishna

### Courses

- Red Hat EX407/EX374 prep
- Sander van Vugt's Ansible courses
- TechWorld with Nana — Ansible playlist
- Jeff Geerling's YouTube series

### Repos

- https://github.com/geerlingguy (huge collection of high-quality roles)
- https://github.com/ansible/awx
- https://github.com/ansible/molecule
- https://github.com/ansible-community/ansible-lint
- https://github.com/ansible/ansible-runner

### Tools

- `ansible-lint`, `yamllint`, `ansible-test`, `molecule`
- `ansible-builder`, `ansible-navigator`, `ansible-runner`
- AAP Controller (Tower), Private Automation Hub, EDA Controller

---

End of Ansible interview guide. Pair this with at least one full end-to-end role + Molecule test before any onsite.
