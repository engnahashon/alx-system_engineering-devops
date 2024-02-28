# Create the SSH directory if it does not exist
file_line { 'ssh-config-1':
  path => '/etc/ssh/ssh_config',
  line => 'Host 112184-web-01',
}

file_line { 'ssh-config-2':
  path => '/etc/ssh/ssh_config',
  line => 'User ubuntu',
}

file_line { 'ssh-config-3':
  path => '/etc/ssh/ssh_config',
  line => 'HostName 34.229.184.165',
}

file_line { 'ssh-config-4':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}

file_line { 'ssh-config-5':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}

