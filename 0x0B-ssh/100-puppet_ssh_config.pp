# Create the SSH directory if it does not exist
file_line { 'specify Identity File':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}
